# NuvemDeck — Índice de Assets Visuais
> Inventário completo dos backgrounds PNG e arquivos de referência do template NP 2026

---

## Backgrounds PT-BR

| Arquivo | Tipo | Uso |
|---------|------|-----|
| `bg_cover.png` | Cover genérica | Capa sem BU específica |
| `bg_cover_nuvem.png` | Cover Nuvemshop | Capa genérica com marca |
| `bg_cover_nuvem_pago.png` | Cover BU | Capa Nuvem Pago (cartão 3D) |
| `bg_cover_nuvem_envio.png` | Cover BU | Capa Nuvem Envio (caixa 3D) |
| `bg_cover_nuvem_chat.png` | Cover BU | Capa Nuvem Chat (avatares 3D) |
| `bg_cover_nuvem_marketing.png` | Cover BU | Capa Nuvem Marketing |
| `bg_cover_nuvem_pdv.png` | Cover BU | Capa Nuvem PDV |
| `bg_chapter_separator.png` | Separador | Separador de capítulo |
| `bg_subchapter_separator.png` | Separador | Separador de subcapítulo |
| `bg_clear_blue_01.png` | Temático | Canvas livre — azul claro |
| `bg_pure_white_01.png` | Temático | Canvas livre — branco |
| `bg_content_blue_panel_dark.png` | Conteúdo | Painel azul + área azul |
| `bg_content_blue_panel_white.png` | Conteúdo | Painel azul + área branca |
| `bg_content_half_half.png` | Conteúdo | Split 50/50 azul/branco |
| `bg_closing_thank_you.png` | Encerramento | Logo central + painel direito |
| `bg_closing_thank_you_alt.png` | Encerramento | Logo + painel direito completo (sem texto) |

## Backgrounds ES (Espanhol)

Mesmos layouts disponíveis para apresentações em Español:
`bg_cover.png`, `bg_cover_nuvem.png`, `bg_cover_nuvem_chat.png`, `bg_cover_nuvem_envio.png`, `bg_cover_nuvem_marketing.png`, `bg_cover_nuvem_pago.png`, `bg_cover_nuvem_pdv.png`, `bg_chapter_separator.png`, `bg_subchapter_separator.png`, `bg_clear_blue_01.png`, `bg_pure_white_01.png`, `bg_content_blue_panel_dark.png`, `bg_content_blue_panel_white.png`, `bg_content_half_half.png`, `bg_closing_thank_you.png`, `bg_closing_thank_you_alt.png`

---

## Regra de Uso dos Backgrounds por Chat

### Fixos (sempre enviar — 7 arquivos)
- `bg_chapter_separator`
- `bg_subchapter_separator`
- `bg_clear_blue_01`
- `bg_pure_white_01`
- `bg_content_blue_panel_dark`
- `bg_content_blue_panel_white`
- `bg_content_half_half`

### Covers (escolher exatamente 1)
- `bg_cover` | `bg_cover_nuvem` | `bg_cover_nuvem_pago` | `bg_cover_nuvem_envio` | `bg_cover_nuvem_chat` | `bg_cover_nuvem_marketing` | `bg_cover_nuvem_pdv`

### Closing (escolher ao menos 1, pode usar ambos)
- `bg_closing_thank_you` — contém "Obrigado!" / "¡Gracias!" / "Thank You!"
- `bg_closing_thank_you_alt` — tela limpa sem texto

> **Máximo:** 10 imagens por chat. Com 7 fixos + 1 cover + 1 closing = 9. Sobra 1 slot opcional.

---

## Arquivos de Referência do Projeto

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `nuvemshop_brand_specs.txt` | TXT | Brand specs v3.5 — referência técnica para o agente |
| `nuvemshop_brand_specs_v3.5.docx` | DOCX | Idem em formato Word |
| `[NS - 2026] Modelo de Slides.pdf` | PDF | Modelo visual de referência do template NP 2026 |
| `[NS - 2026] Modelo de Slides.pptx` | PPTX | Modelo editável do template NP 2026 |
| `Prompt Nuvem Deck V1.9.docx` | DOCX | System prompt do agente NuvemDeck v1.9 |
| `[Tutorial] NuvemDeck.docx` | DOCX | Tutorial de configuração PT-BR / ES |
| `tutorial_nuvemdeck_pt_es.pptx` | PPTX | Tutorial em slides (bilíngue PT-BR / ES) |
| `meta_apresentacao_nuvemdeck.pptx` | PPTX | Meta-apresentação sobre arquitetura e decisões do NuvemDeck |

---

## Notas de Governança

- **Backgrounds PT-BR e ES são intercambiáveis** — mesmos layouts, variações de idioma para elementos pré-renderizados.
- **Não recriar gradientes via código.** Sempre usar os PNGs pré-renderizados.
- **`bg_closing_thank_you_alt`** é tela de transição limpa — nunca sobrepor texto.
- **Ordem de encerramento obrigatória:** `closing_thank_you` (com "Obrigado!") → `closing_thank_you_alt` (limpo).

*Fonte: Assets-20260427T132030Z-3-001.zip*
