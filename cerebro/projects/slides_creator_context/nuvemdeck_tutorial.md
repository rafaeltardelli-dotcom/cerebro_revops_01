# NuvemDeck — Tutorial de Configuração
> Guia passo a passo para configurar e usar o agente NuvemDeck no Claude  
> Bilíngue: PT-BR / ES

---

## Etapa 1 — Configuração Inicial do Projeto

### Criar o projeto / Crear el proyecto

1. Em sua conta no Claude, selecione **"Projetos"**  
   *(En tu cuenta de Claude, selecciona "Proyectos")*

2. Na aba de "Projetos", selecione **"Novo projeto"**  
   *(En la pestaña de "Proyectos", selecciona "Nuevo proyecto")*

3. Dê um nome ao agente. **Prefira a visibilidade "privado"** — assim você consegue personalizá-lo de acordo com seu uso.  
   *(Ponle un nombre a tu agente. Prefiere la visibilidad "privado", así podrás personalizarlo de acuerdo a tu uso.)*

### Colar o prompt / Pegar el prompt

4. Em **"Instruções"**, clique no botão **"+"**  
   *(En "Instrucciones", haz clic en "+")*

5. Cole o prompt completo do arquivo `Prompt Nuvem Deck V1.9.docx` e salve as instruções.  
   *(Pega el prompt de NuvemDeck (V1.9+) y guarda las instrucciones.)*

---

## Etapa 2 — Adicionar Arquivos de Referência ao Projeto

> Estes arquivos ficam **permanentes no projeto** — anexados uma vez e reutilizados em todos os chats.  
> *(Estos archivos quedan disponibles en todos los chats de este proyecto, sin necesidad de reenviarlos en cada conversación.)*

**Baixe e carregue 2 arquivos / Descarga y carga 2 archivos:**

| Arquivo | Função |
|---------|--------|
| `[NS - 2026] Modelo de Slides.pdf` | Referência visual do template NP 2026 |
| `nuvemshop_brand_specs.txt` | Especificações técnicas de brand para o agente |

**Caminho / Ruta:** `Arquivos → + → Carregar do aparelho`  
*(Archivos → + → Cargar desde el dispositivo)*

---

## Etapa 3 — Uso em Cada Nova Apresentação

### Sobre a dinâmica do agente / Sobre la dinámica del agente

O NuvemDeck é **interativo, questionador e provocador**. Ele opera com personas adversariais que criticam o roteiro original — propositadamente — para elevar o nível da entrega final.

*(NuvemDeck es interactivo, cuestionador y provocador. Opera con arquetipos adversariales que critican el guión original intencionalmente — para elevar el nivel de la entrega final.)*

> **Não é instantâneo / No es instantáneo.** O processo passa por 3 fases com checkpoints. Teste algumas vezes para se habituar à dinâmica.

### O que anexar a cada chat / Qué adjuntar en cada chat

> Máximo **10 imagens** por chat + documentos auxiliares (planilhas, docs, dados, transcrições)

#### SEMPRE — 7 fixos obrigatórios / SIEMPRE — 7 fijos obligatorios
- `bg_chapter_separator`
- `bg_subchapter_separator`
- `bg_clear_blue_01`
- `bg_pure_white_01`
- `bg_content_blue_panel_dark`
- `bg_content_blue_panel_white`
- `bg_content_half_half`

#### 1 COVER — escolher exatamente 1 / elegir exactamente 1
- `bg_cover`
- `bg_cover_nuvem`
- `bg_cover_nuvem_pago`
- `bg_cover_nuvem_envio`
- `bg_cover_nuvem_chat`
- `bg_cover_nuvem_marketing`
- `bg_cover_nuvem_pdv`

#### ≥1 CLOSING — escolher 1 ou ambos / elegir 1 o ambos
- `bg_closing_thank_you`
- `bg_closing_thank_you_alt`

### Próximos passos / Próximos pasos

1. Abra um novo chat / *Abre un nuevo chat*
2. Anexe materiais + 9 a 10 backgrounds / *Adjunta materiales + 9 a 10 backgrounds*
3. Diga ao agente o que quer gerar / *Dile al agente qué quieres generar*

---

## As 3 Fases do Agente

| Fase | Nome | Descrição |
|------|------|-----------|
| **Fase 1** | Roteiro narrativo | Transforma materiais brutos em roteiro estruturado. Output: script com layouts mapeados. |
| **Fase 2** | Crítica adversarial | Persona adversarial ativada — agente vira crítico. Output: rubrica em 7 dimensões, score /35. |
| **Fase 3** | Geração dual | Geração via python-pptx. Output: arquivo `.pptx` + estrutura textual detalhada. |

> Há um checkpoint humano entre cada fase — o agente não avança sem sua aprovação.

---

## Dúvidas?

Consulte o time responsável / *¿Dudas? Consulta al equipo responsable.*

*Fonte: [Tutorial] NuvemDeck.docx + tutorial_nuvemdeck_pt_es.pptx*
