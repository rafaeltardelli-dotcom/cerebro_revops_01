# NuvemDeck — Tutorial de Configuração e Uso
> Guia bilingue PT-BR / ES para configurar o agente NuvemDeck no Claude Projects

---

## PT-BR: Configurando o NuvemDeck

### Passo 1: Criar Projeto no Claude

1. Acesse claude.ai → clique em **"Projetos"** na barra lateral
2. Clique em **"Criar projeto"**
3. Dê o nome: `NuvemDeck`

### Passo 2: Colar o System Prompt

1. Dentro do projeto, clique em **"Instruções do projeto"**
2. Cole o conteúdo completo do arquivo `nuvemdeck_prompt_v1_9.md`
3. Salve as instruções

### Passo 3: Adicionar Arquivos de Referência

Na seção **"Conhecimento do projeto"**, adicione:
- `nuvemdeck_brand_specs_v3_5.md`
- `[NS - 2026] Modelo de Slides.pdf` (opcional)

### Passo 4: Começar um Chat

Ao iniciar uma nova conversa no projeto:
1. Anexe os **backgrounds PNG** necessários
2. Anexe seus **materiais de origem** (planilhas, docs, bullets)
3. Informe: audiência, propósito, duração esperada
4. O agente fará até 4 perguntas de clarificação

---

## Dinâmica do Chat

### As 3 Fases

**Fase 1 — Roteiro narrativo**
- Script completo slide por slide
- Título, conteúdo, notas do apresentador, função narrativa
- Você pode aprovar ou solicitar ajustes

**Fase 2 — Crítica adversarial** (opcional, recomendada para executivos)
- Avalia 7 dimensões com nota 1–5
- Agregação ≥ 32 = aprovado diretamente para Fase 3

**Fase 3 — Geração dual**
- Gera o arquivo `.pptx`
- Entrega estrutura textual detalhada
- Checklist de refinamento manual por slide

---

## ES: Configurando el NuvemDeck

### Paso 1: Crear Proyecto en Claude

1. Accede a claude.ai → haz clic en **"Proyectos"**
2. Haz clic en **"Crear proyecto"** → Nombre: `NuvemDeck`

### Paso 2: Pegar el System Prompt

1. En el proyecto, haz clic en **"Instrucciones del proyecto"**
2. Pega el contenido completo de `nuvemdeck_prompt_v1_9.md`

### Paso 3: Iniciar un Chat

1. Adjunta los **backgrounds PNG**
2. Adjunta tus **materiales de origen**
3. El agente hará hasta 4 preguntas de clarificación

---

*Fonte: [Tutorial] NuvemDeck.docx*
