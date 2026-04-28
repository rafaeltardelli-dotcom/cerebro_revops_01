# NuvemDeck — Meta-Apresentação: Da Ideia ao Agente Funcional
> Documento de arquitetura, decisões técnicas e status do projeto NuvemDeck  
> Baseado na apresentação interna apresentada pela equipe Nuvem Pago

---

## O Desafio Inicial

### O Problema em Números

| Métrica | Valor |
|---------|-------|
| Tempo médio por apresentação criada | **4–6h** |
| Tempo gasto em formatação visual | **70%** |
| Apresentações fora do brand guidelines | **30%** |

> **Custo organizacional invisível:** multiplique 4–6h por apresentação × dezenas de áreas × várias apresentações por mês.

---

## Decisões Arquiteturais

### Agente Único vs. Agentes Separados

| Dimensão | Agente Único (Monolito cognitivo) | Agentes Separados (Microsserviços cognitivos) |
|----------|----------------------------------|-----------------------------------------------|
| **Vantagens** | Simplicidade operacional; contexto compartilhado entre fases; menor custo de tokens | Crítica genuinamente isolada; especialização cognitiva; falhas localizadas |
| **Desvantagens** | Context collapse em tarefas múltiplas; auto-validação inevitável; difícil debug | Orquestração explícita necessária; custo maior de tokens; loops mais lentos |

**→ Solução adotada: arquitetura híbrida** combinando o melhor dos dois mundos.

### Arquitetura Híbrida com Crítica Adversarial Forçada

```
FASE 1                    FASE 2                    FASE 3
Roteiro narrativo    →    Crítica adversarial   →   Geração dual
                          (persona externa)          PPTX + textual
         ↑                        ↑                       ↑
    Checkpoint              Checkpoint              Checkpoint
    humano                  humano                  humano
```

> **A persona adversarial é o segredo da qualidade.** Sem ela, o mesmo agente que escreve tende a aprovar seu próprio trabalho. A ativação explícita força rigor crítico genuíno.

---

## Desafios Técnicos e Iterações

### Evolução do Prompt e Estratégia

| Versão | Abordagem | Status | Fidelidade |
|--------|-----------|--------|------------|
| v1.0 | Apps Script | Descartado | ~75% |
| v1.1 | Estrutura textual | Parcial | Sem geração real de PPTX |
| v1.2 | python-pptx | Funcional | Sem backgrounds |
| v1.3 | PPTX + bg | **Atual** | **~95%** |

### Aprendizados-Chave

- **Apps Script é frágil para gradientes complexos** — API do Google Slides limita renderização de gradientes multi-stop.
- **Sandbox do Claude bloqueia internet** — URLs públicas não são acessíveis pelo ambiente Python. Solução: anexar backgrounds no chat (10 PNGs em `/mnt/user-data/uploads/`).
- **Fidelidade visual de ~95%** ao template original com a abordagem atual de backgrounds pré-renderizados + composição de texto via código.

---

## O Resultado: NuvemDeck v1.3

### Capacidades Entregues

| Capacidade | Descrição |
|-----------|-----------|
| Roteiro narrativo | 5 padrões de arco aplicáveis por contexto |
| Crítica adversarial | Persona externa em rubrica de 7 dimensões |
| Multilíngue | PT-BR, ES e EN com detecção automática |
| Template fiel | 10 layouts NP 2026 com fidelidade ~95% |
| Geração dual | PPTX + estrutura textual para refinamento |
| Speaker notes | Roteiro oral natural embutido em cada slide |
| Density discipline | Limites por layout impedem slides poluídos |
| Edge cases | Trata inputs ambíguos com perguntas direcionadas |

### Status de Produção

| Item | Status |
|------|--------|
| Arquitetura validada | ✅ |
| 10 backgrounds funcionais | ✅ |
| Brand specs v3.5 | ✅ |
| Prompt v1.9 | ✅ |
| Modular para 5 BUs | ✅ |
| Sistema de alertas | ✅ |
| Density rules sistêmicas | ✅ |

---

## Impact Summary

| Métrica | Antes | Depois |
|---------|-------|--------|
| Tempo por apresentação | 4–6h | **15–30 min** |
| Foco em formatação | 70% do tempo | **0% — automatizado** |
| Aderência ao brand | ~70% | **~95%** |
| Idiomas suportados | 1 | **3 (PT-BR, ES, EN)** |
| Unidades de negócio | Manual | **5 BUs modulares** |

> **Redução de tempo:** ~75% vs. criação manual

---

## Roadmap de Evolução

| Prazo | Iniciativa |
|-------|-----------|
| Próximas semanas | Lançar agente nos canais Slack de toda a companhia |
| Próximo mês | Adicionar 4 capas restantes (Envio, Chat, Marketing, PDV) |
| Q3–Q4 | Migrar para CDN corporativa quando infra estiver disponível |
| Contínuo | Iterar com base em feedback de uso real dos times |

---

## Timeline do Projeto

| Marco | Data | Evento |
|-------|------|--------|
| Concepção | Mar/26 | Identificação do problema e início do desenvolvimento |
| v1.0–v1.2 | Abr/26 | Iterações técnicas e descoberta dos constraints do ambiente |
| v1.3 | Abr/26 | Versão funcional com ~95% de fidelidade visual |
| Lançamento | Abr/26 | Distribuição interna para os times |

---

*Fonte: meta_apresentacao_nuvemdeck.pptx*
