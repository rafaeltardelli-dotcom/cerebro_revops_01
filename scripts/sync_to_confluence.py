"""
Syncs markdown files from the cerebro repo to Confluence pages.
Reads confluence_map.json to know which file maps to which page/space.
Creates the page if it doesn't exist; updates if it does.
"""

import json
import os
import sys
import re
import requests
from pathlib import Path
from base64 import b64encode

BASE_URL = os.environ["CONFLUENCE_BASE_URL"].rstrip("/")
EMAIL = os.environ["CONFLUENCE_EMAIL"]
TOKEN = os.environ["CONFLUENCE_API_TOKEN"]

AUTH = b64encode(f"{EMAIL}:{TOKEN}".encode()).decode()
HEADERS = {
    "Authorization": f"Basic {AUTH}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

REPO_ROOT = Path(__file__).parent.parent


def md_to_confluence(md_text: str) -> str:
    """Minimal markdown → Confluence Storage Format conversion."""
    text = md_text

    # Headings
    for level in range(6, 0, -1):
        text = re.sub(
            rf"^{'#' * level} (.+)$",
            rf"<h{level}>\1</h{level}>",
            text,
            flags=re.MULTILINE,
        )

    # Bold and italic
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)

    # Inline code
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)

    # Fenced code blocks
    text = re.sub(
        r"```(\w*)\n([\s\S]*?)```",
        lambda m: (
            f'<ac:structured-macro ac:name="code">'
            f'<ac:parameter ac:name="language">{m.group(1) or "none"}</ac:parameter>'
            f"<ac:plain-text-body><![CDATA[{m.group(2).rstrip()}]]></ac:plain-text-body>"
            f"</ac:structured-macro>"
        ),
        text,
    )

    # Horizontal rule
    text = re.sub(r"^---+$", "<hr/>", text, flags=re.MULTILINE)

    # Unordered lists (simple single-level)
    def replace_ul(m):
        items = re.findall(r"^[-*] (.+)$", m.group(0), re.MULTILINE)
        lis = "".join(f"<li>{i}</li>" for i in items)
        return f"<ul>{lis}</ul>"

    text = re.sub(r"(^[-*] .+\n?)+", replace_ul, text, flags=re.MULTILINE)

    # Ordered lists (simple single-level)
    def replace_ol(m):
        items = re.findall(r"^\d+\. (.+)$", m.group(0), re.MULTILINE)
        lis = "".join(f"<li>{i}</li>" for i in items)
        return f"<ol>{lis}</ol>"

    text = re.sub(r"(^\d+\. .+\n?)+", replace_ol, text, flags=re.MULTILINE)

    # Links
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)

    # Paragraphs: wrap non-tag lines
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("<"):
            lines.append(f"<p>{stripped}</p>")
        else:
            lines.append(line)
    text = "\n".join(lines)

    return text


def get_page(space_key: str, title: str):
    url = f"{BASE_URL}/wiki/rest/api/content"
    params = {
        "spaceKey": space_key,
        "title": title,
        "expand": "version",
    }
    r = requests.get(url, headers=HEADERS, params=params)
    r.raise_for_status()
    results = r.json().get("results", [])
    return results[0] if results else None


def create_page(space_key: str, parent_id: str, title: str, body: str):
    url = f"{BASE_URL}/wiki/rest/api/content"
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": space_key},
        "ancestors": [{"id": parent_id}],
        "body": {
            "storage": {
                "value": body,
                "representation": "storage",
            }
        },
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    r.raise_for_status()
    page_id = r.json()["id"]
    print(f"  CREATED  '{title}' (id={page_id})")
    return page_id


def update_page(page_id: str, title: str, body: str, version: int):
    url = f"{BASE_URL}/wiki/rest/api/content/{page_id}"
    payload = {
        "type": "page",
        "title": title,
        "version": {"number": version + 1},
        "body": {
            "storage": {
                "value": body,
                "representation": "storage",
            }
        },
    }
    r = requests.put(url, headers=HEADERS, json=payload)
    r.raise_for_status()
    print(f"  UPDATED  '{title}' → version {version + 1}")


def sync_file(entry: dict):
    file_path = REPO_ROOT / entry["file"]
    if not file_path.exists():
        print(f"  SKIP (not found): {entry['file']}")
        return

    md_text = file_path.read_text(encoding="utf-8")
    body = md_to_confluence(md_text)

    space_key = entry["space_key"]
    parent_id = entry["parent_page_id"]
    title = entry.get("title") or file_path.stem.replace("_", " ").title()

    existing = get_page(space_key, title)
    if existing:
        update_page(existing["id"], title, body, existing["version"]["number"])
    else:
        create_page(space_key, parent_id, title, body)


def main():
    map_path = REPO_ROOT / "confluence_map.json"
    if not map_path.exists():
        print("confluence_map.json not found — nothing to sync.")
        sys.exit(1)

    entries = json.loads(map_path.read_text(encoding="utf-8"))
    errors = []

    for entry in entries:
        print(f"Syncing: {entry['file']}")
        try:
            sync_file(entry)
        except Exception as exc:
            print(f"  ERROR: {exc}")
            errors.append(entry["file"])

    if errors:
        print(f"\nFailed: {errors}")
        sys.exit(1)

    print("\nSync complete.")


if __name__ == "__main__":
    main()
