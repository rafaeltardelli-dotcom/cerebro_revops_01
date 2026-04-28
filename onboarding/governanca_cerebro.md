# Governança do Partnerships Ops & Analytics

**Dono:** Time RevOps  
**Última revisão:** 2026-04-28

## O que é o Partnerships Ops & Analytics

É a base de conhecimento do time de RevOps & Partnerships. Vive no GitHub (`cerebro_revops_01`) e é sincronizado automaticamente com o Confluence (espaço **Ops & Analytics → Partnerships Ops & Analytics**) a cada `git push`.

Qualquer `.md` modificado dentro de `cerebro/` ou `onboarding/` é publicado no Confluence sem ação manual.

---

## O que pertence ao Partnerships Ops & Analytics

| Entra | Não entra |
| :--- | :--- |
| Decisões tomadas e o motivo | Rascunhos e brainstorms |
| Processos operacionais (como fazemos X) | Apresentações e decks |
| Regras de negócio dos canais | Dados brutos de planilhas |
| Contexto de parceiros e segmentos | Anotações de reunião sem conclusão |
| Projetos com status atual | Histórico de tentativas descartadas |

---

## Estrutura de pastas

```
cerebro/
  empresa/     → Contexto da Nuvemshop, HubSpot, brandbook
  areas/       → Contexto de cada canal (Agências, Tech Partners, Afiliados)
  projects/    → Projetos ativos e estratégicos
  agentes/     → Prompts e instruções para agentes de IA
  seguranca/   → Políticas e acessos

onboarding/    → Guias de entrada e governança (este arquivo)
```

---

## Estrutura de cada documento

```markdown
# [Título]
**Última revisão:** YYYY-MM
**Dono:** [nome ou time]

## Contexto
Por que este documento existe e qual problema resolve.

## Regras / Como funciona
Decisões e processos vigentes.

## Projetos ativos
O que está em andamento (remover quando concluir).

## Histórico de decisões
| Data | Decisão | Motivo |
```

---

## Como atualizar com o Claude

Dê comandos diretos e contextuais. Exemplos:

**Registrar uma decisão:**
> "Atualiza o `contexto_agencies_01.md` com esta decisão: [decisão]. O motivo foi [motivo]."

**Documentar um processo:**
> "Cria um doc de processo para [nome]. Os passos são: [passos]. Ferramenta: [HubSpot/etc]. Responsável: [quem]."

**Registrar uma regra de negócio:**
> "Adiciona a regra: [regra] no arquivo [arquivo]. Contexto: [por que existe]."

**Criar um novo documento:**
> "Cria `cerebro/areas/[nome].md` sobre [tema] e adiciona ao `confluence_map.json`."

**Limpar informação desatualizada:**
> "Revisa o `[arquivo].md` e remove o que está desatualizado. O que é atual: [contexto]."

---

## Cadência de manutenção

| Frequência | Ação |
| :--- | :--- |
| Após decisão relevante | Registrar no documento do canal ou projeto |
| Semanal | Após 1:1 ou reunião de time, passar decisões ao Claude |
| Mensal | Pedir revisão: "aponta o que pode estar desatualizado em [arquivo]" |
| Ao fechar projeto | "Arquiva o status final do `[projeto].md`" |

---

## Regra de ouro

> O repositório não precisa ser completo. Precisa ser **confiável**.  
> Informação desatualizada é pior do que informação ausente.
