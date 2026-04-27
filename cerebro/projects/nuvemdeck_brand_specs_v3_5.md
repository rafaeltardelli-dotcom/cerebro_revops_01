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
| Título de separador de subcapítulo | 30pt | SemiBold | `#FFFFFF` |
| Texto de slide temático | 12–22pt | SemiBold | `#001F5C` |
| Título de slide de conteúdo | 18–22pt | SemiBold | `#FFFFFF` |
| Corpo de slide de conteúdo | 11–14pt | SemiBold | matching |
| Métricas hero | 32–56pt | SemiBold | NAVY |
| Texto de finalizador | 30–48pt | SemiBold | `#FFFFFF` |

---

## 3. Dimensões

- **Aspect ratio:** 16:9
- **Em pontos:** 960 × 540 pt
- **Em EMU:** 9.144.000 × 5.143.500

---

## 4. Inventário de Backgrounds

| Arquivo | Layout key | Função |
|---------|-----------|--------|
| `bg_cover_nuvem_pago.png` | `cover_nuvem_pago` | Capa Nuvem Pago |
| `bg_cover_nuvem_envio.png` | `cover_nuvem_envio` | Capa Nuvem Envio |
| `bg_chapter_separator.png` | `chapter_separator` | Separador de capítulo |
| `bg_subchapter_separator.png` | `subchapter_separator` | Separador de subcapítulo |
| `bg_clear_blue_01.png` | `clear_blue_01` | Slide temático azul |
| `bg_pure_white_01.png` | `pure_white_01` | Slide temático branco |
| `bg_content_blue_panel_dark.png` | `content_blue_panel_dark` | Conteúdo painel escuro |
| `bg_content_blue_panel_white.png` | `content_blue_panel_white` | Conteúdo painel branco |
| `bg_content_half_half.png` | `content_half_half` | Split 50/50 |
| `bg_closing_thank_you.png` | `closing_thank_you` | Encerramento |
| `bg_closing_thank_you_alt.png` | `closing_thank_you_alt` | Encerramento alt |

---

## 5. Helpers de Código

```python
def text_height(font_size_pt, num_lines=1, line_spacing=1.15):
    return int(font_size_pt * 1.3 * num_lines * line_spacing) + 4

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
            effectRef.set('idx', '0')
```

---

*Fonte: nuvemshop_brand_specs_v3.5.docx*
