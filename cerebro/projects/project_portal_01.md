# Project: Portal CRM — Integração HubSpot <> Aplicação (Suite)
**Área:** RevOps & Analytics Partnerships @ Nuvemshop  
**Tipo:** Documento de projeto (arquitetura, roadmap e premissas)  
**Stack de referência:** HubSpot (CRM core) · Make (orquestração) · Supabase (persistência)

---

## 1. Introdução e Objetivo

O projeto endereça a lacuna entre **cadastro de leads no ecossistema de parceiros** e **ação comercial previsível**: parceiros precisam enxergar oportunidades cedo, com contexto mínimo viável, sem depender de filas manuais ou relatórios espalhados.

* **Time-to-market:** reduzir o ciclo entre evento de lead no CRM e disponibilização no portal (suite), com filas observáveis e retries controlados na orquestração.
* **Visibilidade para parceiros:** entregar visão consistente de pipeline (estágio, origem, responsável) e sinais de priorização alinhados às regras de GTM — sem duplicar fonte de verdade fora do HubSpot.
* **Valor de negócio:** aumentar conversão por parceiro ao diminuir atrito operacional e ambiguidade de ownership entre CRM, financeiro e operações regionais.

---

## 2. Arquitetura Técnica

| Camada | Papel | Detalhe executivo |
|--------|--------|-------------------|
| **HubSpot** | **Core / SSOT comercial** | Objetos, propriedades, associações e permissões de acesso definem o que é “verdade” para lead, empresa e deal. O portal consome apenas dados já governados no CRM. |
| **Make** | **Orquestração e integração** | Webhooks, agendamentos e cenários de mapeamento HubSpot ↔ Supabase ↔ Suite. Centraliza transformação leve, fan-out para notificações e tratamento de erro com logs rastreáveis. |
| **Supabase** | **Base operacional do portal** | Persistência para sessão, caches de leitura, agregados para UI e estados que não pertencem ao modelo nativo do HubSpot (ex.: preferências de exibição por tenant de parceiro), sempre com vínculo explícito ao ID HubSpot. |
| **Aplicação (Suite)** | **Experiência** | Front do parceiro: autenticação, listagens, detalhe de lead/oportunidade e ações permitidas pelo contrato de dados (read/write limitado via APIs seguras). |

**Princípio:** o HubSpot permanece dono do ciclo de vida comercial; Make move dados entre sistemas; Supabase acelera leitura e desacopla a UI de picos na API do CRM; a Suite não reimplementa regras de pipeline já existentes no HubSpot.

---

## 3. Roadmap Estruturado

| Fase | Foco principal | Entregas-chave | Indicadores de sucesso (exemplos) |
|------|----------------|----------------|-------------------------------------|
| **Fase 1 — Automação de Leads, Distribuição e Visibilidade** | Ingerir leads e deals do HubSpot, normalizar no Supabase e exibir no portal com **atribuição** e **estágio** corretos. | Cenários Make (sync incremental + reconciliação); modelo de dados Supabase; telas de lista e detalhe; regras de **distribuição** (round-robin ou por segmento) conforme política RevOps. | Latência média ingestão → portal; % leads com owner definido; zero duplicidade crítica por parceiro. |
| **Fase 2 — Profundidade comercial e governança** | Ações controladas (ex.: atualização de propriedades permitidas), histórico de interações e alinhamento com **reporting** regional (exportações / snapshots). | Contratos de API; auditoria de alterações; camadas de permissão por papel (parceiro vs. interno). | Redução de tickets “cadê meu lead?”; trilha de auditoria completa por evento. |
| **Fase 3 — Escala e monetização do ecossistema** | Conectar sinais financeiros (comissionamento, status de pagamento) com visão **misturada** CRM/financeiro já validada; automações avançadas e experimentos (ex.: scoring no portal). | Integrações adicionais; feature flags; observabilidade unificada (dashboards). | GMV atribuível; adoção por base ativa de parceiros; custo por 1k chamadas API estável. |

---

## 4. Decisões e Premissas (Pontos de Validação)

* **Acesso único por agência:** um tenant lógico por parceiro (agência) no portal; usuários compartilham o mesmo contexto contratual. Evita fragmentação de dados e simplifica compliance e offboarding.
* **Visibilidade mista CRM / Financeiro:** o parceiro pode ver campos comerciais **e** indicadores financeiros autorizados (ex.: comissão prevista, status de payout) apenas quando a política de dados e LGPD/privacidade estiver explícita no desenho de propriedades HubSpot + espelho Supabase.
* **Input manual de fases:** transições sensíveis de estágio podem exigir confirmação humana (RevOps ou parceiro senior) antes de propagar ao HubSpot — automação não substitui gates de negócio não modelados.
* **HubSpot como limite de verdade:** qualquer divergência entre Supabase e HubSpot é resolvida **a favor do HubSpot** após reconciliação; jobs de correção devem ser idempotentes.
* **Observabilidade:** cada cenário Make deve ter alerta mínimo (falha N vezes, fila parada) para não degradar time-to-market silenciosamente.

---

## 5. Próximos Passos (operacional)

1. Congelar **mapa de propriedades** HubSpot ↔ colunas Supabase (v1).  
2. Definir **matriz de permissões** por papel e por agência.  
3. Piloto com **N** agências e métricas da Fase 1 antes de expandir Fase 2.
