# Partnerships Ops & Analytics

Bem-vindo ao repositório central de inteligência da área de RevOps & Partnerships. Este não é apenas um backup de arquivos, mas uma **Infraestrutura de Conhecimento** desenhada para ser lida e executada por humanos e IAs.

## O Framework: Contexto > Skill > Rotina

Operamos sob uma tríade que garante que o conhecimento se transforme em ação:

1. **Contexto (Onde pensamos):** Localizado na pasta `/cerebro/`. É a base de dados bruta, regras de negócio, histórico de decisões e cultura da empresa. Sem contexto, a IA alucina; com contexto, ela decide.
2. **Skill (O que fazemos):** Localizado na pasta `/rotinas_e_skills/`. São os "Playbooks" ou scripts ensinados. É o passo a passo técnico para realizar uma tarefa repetitiva (ex: como qualificar um MQL).
3. **Rotina (Quando agimos):** Também em `/rotinas_e_skills/`. É o Heartbeat da área. Define a cadência (Cron), os rituais e o que deve ser conferido em cada ciclo (WBR/MBR).

---

## Estrutura de Pastas

- `/onboarding/`: Documentação de setup e este manual.
- `/cerebro/empresa/`: Visão macro Nuvemshop (Brandbook, Contexto Global).
- `/cerebro/areas/`: Deep-dives específicos (Affiliates, Agencies, Tech-Partners).
- `/cerebro/projects/`: Documentação técnica de iniciativas (Portal/Suite).
- `/cerebro/agentes/`: Perfis de execução e personas dos líderes e times.
- `/rotinas_e_skills/`: O motor de execução (Prompts, automações Make/N8N e rituais).

---

## Regras de Ouro para Atualização

1. **Markdown First:** Todos os arquivos devem ser `.md`. Use cabeçalhos (`#`, `##`), tabelas e listas para facilitar a leitura por IAs.
2. **Atomicidade:** Um assunto, um arquivo. Evite arquivos gigantes; prefira documentos específicos e bem nomeados.
3. **Versionamento:** Toda mudança significativa deve ser enviada ao GitHub via commit com mensagens claras (ex: `feat: add contexto tech-partners`).
4. **Single Source of Truth (SSOT):** Se uma regra de negócio mudou no HubSpot ou na estratégia da diretoria, o arquivo correspondente em Partnerships Ops & Analytics **deve** ser atualizado imediatamente.

Para diretrizes completas de governança — o que documentar, como estruturar e cadência de atualização — veja `onboarding/governanca_cerebro.md`.

---

## Tech Stack Conectada

| Ferramenta | Papel |
| :--- | :--- |
| **GitHub** | Source of truth. Controle de versão e histórico institucional. Todo conteúdo nasce aqui. |
| **Confluence** | Publicação automática. Cada push no GitHub sincroniza as páginas em Ops & Analytics > Partnerships Ops & Analytics. |
| **Claude Code** | IDE principal para escrita, estruturação e atualização do repositório. |
| **Make / N8N** | Orquestradores que executam as Skills baseadas nestas regras. |

> O Google Drive não é mais utilizado como repositório. O GitHub é a fonte e o Confluence é a visualização.
