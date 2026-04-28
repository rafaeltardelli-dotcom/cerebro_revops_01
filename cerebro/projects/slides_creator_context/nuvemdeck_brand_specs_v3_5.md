# NuvemDeck — Brand Specs v3.5
> Documento de referência consolidado para o agente NuvemDeck  
> Versão: 3.5 | Última atualização: inclui ícones via 3 modos, modularidade BU, sistema de alertas

---

## 1. Paleta de Cores Oficial

### Cores Primárias

| Cor | Hex | RGB | Uso |
|-----|-----|-----|-----|
| Azul Profundo | `#001F5C` | rgb(0, 31, 92) | Gradientes escuros, painéis laterais, footer, texto navy |
| Azul Royal | `#0033A0` | rgb(0, 51, 160) | Gradiente base, painéis sólidos |
| Azul Brilhante | `#0052CC` | rgb(0, 82, 204) | Transição de gradiente, áreas de luz |

### Cores de Apoio

| Cor | Hex | Uso |
|-----|-----|-----|
| Branco | `#FFFFFF` | Texto sobre azul, fundos claros, logo |
| Azul Acento | `#0099FF` | Accent color, ícones, linhas decorativas |
| Navy Light BG | `#E8EFF7` | Fundo sutil de boxes, agrupamento |

### Sistema de Alertas (paleta pastel)

| Tipo | BG | Text | Accent | Ícone | Casos de uso |
|------|----|------|--------|-------|--------------|
| **DANGER** | `#FDE2E4` | `#B02030` | `#E53E3E` | warning | Erros técnicos, incidentes, riscos críticos, bloqueadores |
| **WARNING** | `#FFF4CC` | `#8B6F00` | `#E0A810` | warning | Limitações, custos ocultos, trade-offs, dependências |
| **SUCCESS** | `#D4EDDA` | `#1E6B32` | `#28A745` | check | Conquistas, validações, KPIs atingidos, soluções funcionais |
| **INFO** | `#D1ECF1` | `#0C5A70` | `#17A2B8` | info | Notas adicionais, dicas, contexto, próximos passos opcionais |

---

## 2. Tipografia

**Família oficial:** Plus Jakarta Sans SemiBold (peso 600)  
**Fallbacks aceitáveis:** Inter, DM Sans, Helvetica Neue, Arial

### Hierarquia Tipográfica

| Elemento | Tamanho | Peso | Cor |
|----------|---------|------|-----|
| Título de capa | 30pt | SemiBold | `#FFFFFF` |
| Badge de unidade (capa) | 8pt | SemiBold | `#FFFFFF` |
| Título de separador de capítulo | 30pt | SemiBold | `#FFFFFF` |
| Badge de tema (separador) | 8pt | SemiBold | `#FFFFFF` |
| Título de separador de subcapítulo | 30pt | SemiBold | `#FFFFFF` |
| Texto de slide temático (clear blue/pure white) | 12–22pt | SemiBold | `#001F5C` |
| Título de slide de conteúdo | 18–22pt | SemiBold | `#FFFFFF` / NAVY |
| Subtítulo de slide de conteúdo | 10–11pt | SemiBold/Regular | matching |
| Corpo de slide de conteúdo | 11–14pt | SemiBold | matching |
| Métricas hero | 32–56pt | SemiBold | NAVY |
| Texto auxiliar de métrica | 9–11pt | Regular | NAVY |
| Texto de finalizador | 30–48pt | SemiBold | `#FFFFFF` |

---

## 3. Dimensões e Coordenadas

- **Aspect ratio:** 16:9
- **Em pontos:** 960 × 540 pt
- **Em EMU:** 9.144.000 × 5.143.500 (1 ponto = 9.525 EMU)

---

## 4. Inventário de Backgrounds

> Arquivos devem ser anexados pelo usuário em cada chat. Caminho esperado: `/mnt/user-data/uploads/`

| Arquivo | Layout key | Função |
|---------|-----------|--------|
| `bg_cover_nuvem_pago.png` | `cover_nuvem_pago` | Capa Nuvem Pago (cartão 3D) |
| `bg_cover_nuvem_envio.png` | `cover_nuvem_envio` | Capa Nuvem Envio (caixa 3D) |
| `bg_cover_nuvem_chat.png` | `cover_nuvem_chat` | Capa Nuvem Chat (avatares 3D) |
| `bg_cover_nuvem_marketing.png` | `cover_nuvem_marketing` | Capa Nuvem Marketing |
| `bg_cover_nuvem_pdv.png` | `cover_nuvem_pdv` | Capa Nuvem PDV |
| `bg_chapter_separator.png` | `chapter_separator` | Separador de capítulo |
| `bg_subchapter_separator.png` | `subchapter_separator` | Separador de subcapítulo |
| `bg_clear_blue_01.png` | `clear_blue_01` | Slide temático azul claro |
| `bg_pure_white_01.png` | `pure_white_01` | Slide temático branco |
| `bg_content_blue_panel_dark.png` | `content_blue_panel_dark` | Conteúdo painel azul + área azul |
| `bg_content_blue_panel_white.png` | `content_blue_panel_white` | Conteúdo painel azul + área branca |
| `bg_content_half_half.png` | `content_half_half` | Split 50/50 azul/branco |
| `bg_closing_thank_you.png` | `closing_thank_you` | Encerramento — logo CENTRAL |
| `bg_closing_thank_you_alt.png` | `closing_thank_you_alt` | Encerramento — logo + painel direito |

> `clear_blue_02` foi removido por redundância com `clear_blue_01`.

---

## 5. Coordenadas de Textbox por Layout

> Coordenadas em PONTOS. Origem (0,0) = canto superior esquerdo do slide.

### Capas (cover_*) e chapter_separator
- **REGRA CRÍTICA:** pílula visual já existe no background (top=317, left=46, 99×30pt)
- Badge text: `pos=(54, 322)`, size=(83×20), font=8pt, anchor='middle', align='center'
- Título principal: `pos=(47, 362)`, size=(690×138), font=30pt — **NUNCA y=315** (cortaria a pílula)

### Subchapter separator
- Título único: `pos=(47, 362)`, size=(800×138), font=30pt
- Sem badge — logo+seta já no background

### Slides temáticos (clear_blue_01, pure_white_01)
> Canvas livres para conteúdo denso — **não** slides de citação
- Título de seção: `pos=(47, 30)`, size=(850×40), font=22pt
- Linha decorativa: x=47–200, y=78, color=ACCENT, width=2
- Conteúdo principal: ocupa 60–80% do corpo do slide

### Content slides (content_blue_panel_*)
- **Painel esquerdo (azul):** Título `pos=(28, 32)`, Subtítulo `pos=(28, 60)`, Linha x=28–130 y=95, Conteúdo `pos=(28, 120+)`
- **Painel direito:** Título `pos=(350, 32)`, Subtítulo `pos=(350, 60)`, Linha x=350–480 y=95, Conteúdo `pos=(350, 110+)`

### Content half_half
- **Painel esquerdo (azul):** Título `pos=(47, 35)` font=20pt WHITE, Subtítulo `pos=(47, 75)`, Linha x=47–200 y=110
- **Painel direito (branco):** Título `pos=(555, 35)` font=20pt NAVY, Subtítulo `pos=(555, 75)`, Linha x=555–708 y=110

### Closing slides
- **closing_thank_you (Final_01):** "Obrigado!" centralizado no painel direito: `pos=(470, 220)`, size=(470×100), font=48pt, WHITE, align='center', anchor='middle'
- **closing_thank_you_alt (Final_02):** sem texto — tela de transição limpa

---

## 6. Regras de Densidade de Conteúdo

| Layout | Densidade alvo |
|--------|---------------|
| `cover_*` | ~30% |
| `chapter_separator` | ~30% |
| `subchapter_separator` | ~30% |
| `clear_blue_01` / `pure_white_01` | 60–80% (canvas livre) |
| `content_blue_panel_*` | 75–90% |
| `content_half_half` | 75–90% |
| `closing_thank_you` | apenas "Obrigado!" |
| `closing_thank_you_alt` | sem texto |
| Executive one-pager | 85–90% |

> Densidade < 50% em slides de conteúdo = slide subutilizado.

---

## 7. Sistema de Posicionamento Vertical (OBRIGATÓRIO)

```python
def text_height(font_size_pt, num_lines=1, line_spacing=1.15):
    """Altura visual REAL ocupada por um texto em pontos."""
    return int(font_size_pt * 1.3 * num_lines * line_spacing) + 4
```

**Aplicação obrigatória:** ao posicionar elemento N+1 abaixo de N:
```python
y_n_plus_1 = y_n + text_height(font_size_n, num_lines_n) + gap_desejado
```

**NUNCA chutar valores Y.** SEMPRE calcular com `text_height()`.

---

## 8. Sistema de Ícones (3 Modos)

### Filosofia
Ícones devem ser monocromáticos com cor adaptativa ao contexto.

| Contexto | Cor recomendada |
|----------|----------------|
| Sobre fundo branco/claro | ACCENT (`#0099FF`) |
| Sobre fundo navy/azul | WHITE |
| Dentro de NAVY_LIGHT_BG | ACCENT |
| Dentro de alert DANGER/WARNING/SUCCESS/INFO | accent da categoria |

### Modo A — Unicode Geometric Shapes (rápido, padrão)

> **Nunca usar emojis** (📝🎨🚀) — PowerPoint os renderiza com glifos coloridos do SO, ignorando `font.color.rgb`.

```python
ICON_UNICODE = {
    'document': '▤', 'design': '◆', 'launch': '▲', 'global': '◯',
    'box': '▣', 'time': '◷', 'fight': '✦', 'mic': '◉',
    'shield': '◈', 'ruler': '▬', 'arrow': '→', 'check': '✓',
    'cross': '✗', 'star': '★', 'circle': '●', 'square': '■',
    'gear': '⚙', 'warning': '⚠', 'info': 'ⓘ',
}
```

**Quando usar:** apresentações rápidas, prototipação.

### Modo B — Geração via matplotlib (melhor visual)

Desenha ícones vetoriais com matplotlib (Patches) salvos como PNG transparente.  
**Quando usar:** board, executivos, apresentações importantes.

### Modo C — PNG simplificado via matplotlib

Formas básicas (círculo, quadrado, triângulo), menos complexidade.  
**Quando usar:** meio termo entre velocidade e qualidade.

> O agente **deve perguntar** ao usuário qual modo usar no início de cada chat.

---

## 9. Sistema de Alertas (Alert Boxes)

### Estrutura visual obrigatória
1. Box arredondado (cor pastel da categoria)
2. Barra lateral 4pt à esquerda (cor accent)
3. Ícone semântico (14pt, cor accent)
4. Título (11pt bold)
5. Corpo (9pt regular)

### Regra de uso
- **DANGER:** máx 1 por apresentação
- **WARNING:** máx 2–3 por apresentação
- **SUCCESS / INFO:** livre uso

---

## 10. Controle de Sombras (CRÍTICO)

Shapes criados via python-pptx herdam sombras do tema. Função obrigatória:

```python
def remove_all_effects(shape):
    element = shape._element
    spPr = element.find('.//' + qn('p:spPr'))
    if spPr is not None:
        for effectLst in spPr.findall(qn('a:effectLst')):
            spPr.remove(effectLst)
        etree.SubElement(spPr, qn('a:effectLst'))
    style = element.find(qn('p:style'))
    if style is not None:
        effectRef = style.find(qn('a:effectRef'))
        if effectRef is not None:
            effectRef.set('idx', '0')  # CRÍTICO: '0', não '1'
    ln = element.find('.//' + qn('a:ln'))
    if ln is not None:
        for el in ln.findall(qn('a:effectLst')):
            ln.remove(el)
        etree.SubElement(ln, qn('a:effectLst'))
```

---

## 11. Modularidade por Unidade de Negócio

```python
COVER_TO_BU = {
    'bg_cover_nuvem_pago.png':      'Nuvem Pago',
    'bg_cover_nuvem_envio.png':     'Nuvem Envio',
    'bg_cover_nuvem_chat.png':      'Nuvem Chat',
    'bg_cover_nuvem_marketing.png': 'Nuvem Marketing',
    'bg_cover_nuvem_pdv.png':       'Nuvem PDV',
    'bg_cover.png':                 None,  # → perguntar
    'bg_cover_nuvem.png':           None,  # → perguntar
}
```

**Fluxo:** 1 cover específico → usar BU; múltiplos → perguntar; nenhum → pedir anexo.

---

## 12. Padrão Executive One-Pager

5 linhas horizontais:
1. **Header** (y=24–78): título + subtítulo + tag de status
2. **Hero Metrics** (y=100–240): 3–5 colunas com ícone + número grande + label
3. **Comparação** (y=260–360): 2–3 boxes com cores semânticas e setas
4. **Timeline** (y=380–490): linha horizontal com 4–6 marcos
5. **CTA Footer** (y=503–535): box NAVY largura total, texto WHITE centralizado

**Densidade alvo:** 85–90%. Usar como penúltimo slide em apresentações executivas.

---

## 13. Adaptação Multilíngue

| Elemento | PT-BR | Español | English |
|----------|-------|---------|---------|
| Slide finalizador | "Obrigado!" | "¡Gracias!" | "Thank You!" |
| Badges de BU | "Nuvem Pago" | "Nuvem Pago" | "Nuvem Pago" |

> Nomes de produto (Nuvem Pago, etc.) **sempre** em PT-BR.

---

## 14. Regras de Alinhamento em Duplos Painéis

- Em layouts duplos, o título do lado simples deve iniciar no **mesmo Y** do título do lado mais completo (topo-com-topo).
- **NUNCA** colocar texto que atravesse o split azul/branco do `half_half`. Usar faixa NAVY unificada: `pos=(28, 470)`, size=(907×50), corner_radius=20000.

---

## 15. Informações de Marca

| Campo | Valor |
|-------|-------|
| Nome oficial | Nuvemshop (Brasil) / Tiendanube (LATAM hispano) |
| Categoria | Plataforma de e-commerce |
| Unidades | Nuvem Pago, Nuvem Envio, Nuvem Chat, Nuvem Marketing, Nuvem PDV |
| Tom (template 2026) | Premium, tech-forward, B2B sério, confiável |
| Público | Micro, pequenas, médias e grandes empresas |

---

*Fonte: nuvemshop_brand_specs.txt / nuvemshop_brand_specs_v3.5.docx*
