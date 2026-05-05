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

---

## 6. Round Robin de Partners — Documentação Técnica

**Versão:** 1.0 · 2026  
**Autora:** lorena.fernandes@nuvemshop.com.br  
**Stack:** HubSpot · Make · Supabase

### 6.1 Visão Geral

Quando um deal é criado no HubSpot e atende às condições de roteamento, o cenário distribui automaticamente um `partner_id` no deal com base em rotação sequencial (round-robin), segmentada por `partner_unit` e `service_demand_gen`.

A solução foi construída fora do HubSpot Custom Code porque a Search API apresentava latência de indexação que causava colisões no round-robin. A lógica de estado foi movida para o Supabase, tornando o processo determinístico e auditável.

> **Contexto:** O objeto customizado `Partner` no HubSpot não é exposto via conectores nativos (MCP, Claude AI). O round-robin via Make + Supabase contorna essa limitação sem alterar a estrutura do objeto.

---

### 6.2 Arquitetura

**Fluxo completo:**

```
Webhook (HubSpot → Make) → Router (3 rotas) → Edge Function (Supabase) → Update Deal (HubSpot API)
```

**Responsabilidades por camada:**

| Camada | Responsabilidade |
|--------|-----------------|
| `HubSpot Workflow` | Detecta o deal, dispara o webhook com `dealId`, `unit` e `demand_type` |
| `Make — Router` | Ramifica por segmento com base nas propriedades do deal |
| `Make — HTTP` | Chama a Edge Function com o `segment` correto |
| `Supabase Edge Function` | Busca partners no HubSpot, calcula o próximo ID, atualiza o estado |
| `Supabase Table` | Guarda o estado do round-robin por segmento |
| `HubSpot API` | Recebe o `partner_id` calculado e atualiza o deal |

---

### 6.3 Segmentos

| Segmento | partner_unit | service_demand_gen | Partners ativos |
|----------|--------------|--------------------|----------------|
| `SMB_impl` | SMB | Implantation | 12 |
| `SMB_both` | SMB | Both | 13 |
| `MM_both` | mid_market | any | 7 |

**Regras de roteamento no Make:**

| Rota | Condição | Segment |
|------|----------|---------|
| 1ª — SMB Implantation | `unit = SMB` AND `demand_type = Creation/Customization of layout` | `SMB_impl` |
| 2ª — SMB Both | `unit = SMB` AND `demand_type ≠ Creation/Customization of layout` | `SMB_both` |
| 3ª — MM Both | `unit = MM` | `MM_both` |

---

### 6.4 HubSpot

**Objeto Partner — propriedades relevantes:**

| Label | Internal name | Tipo | Valores |
|-------|---------------|------|---------|
| Partner Unit | `partner_unit` | Radio | SMB, mid_market |
| Service Demand Gen | `service_demand_gen` | Radio | Both, Implantation, Performance |
| Partner ID | `partner__id` | Text/Number | ID numérico único |

**Object Type ID:** `2-54017777` (necessário para chamadas diretas à CRM API)

**Workflow trigger:** [app.hubspot.com · workflow 1810311966](https://app.hubspot.com/workflows/8180620/platform/flow/1810311966/edit)

**Objeto Deal — propriedade atualizada:**

| Label | Internal name | Tipo |
|-------|---------------|------|
| Partner ID | `partner_id` | Text |

**Webhook payload:**

```json
{
  "dealId": "{{dealId}}",
  "unit": "{{unit}}",
  "demand_type": "{{demand_type_to_the_agency}}"
}
```

---

### 6.5 Supabase

**Projeto:**

| Campo | Valor |
|-------|-------|
| Project name | Partners_CRM |
| Project ID | `jgublibcuopybkuxiagc` |
| URL | `https://jgublibcuopybkuxiagc.supabase.co` |

**Tabela — `round_robin_counters`:**

```sql
create table round_robin_counters (
  key             text primary key,
  call_count      integer not null default 0,
  last_partner_id text
);

insert into round_robin_counters (key, call_count, last_partner_id) values
  ('SMB_impl', 0, NULL),
  ('SMB_both', 0, NULL),
  ('MM_both',  0, NULL);
```

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `key` | text PK | Identificador do segmento: `SMB_impl`, `SMB_both`, `MM_both` |
| `call_count` | integer | Total de deals processados — auditoria |
| `last_partner_id` | text | ID do último partner atribuído — base do round-robin |

**Secrets da Edge Function:**

| Nome | Descrição |
|------|-----------|
| `HUBSPOT_TOKEN` | Private App token do HubSpot (`pat-na1-XXXX`) |
| `SUPABASE_URL` | Injetado automaticamente pelo runtime |
| `SUPABASE_SERVICE_ROLE_KEY` | Injetado automaticamente pelo runtime |

---

### 6.6 Edge Function

**Nome:** `round-robin-partner`  
**URL:** `https://jgublibcuopybkuxiagc.supabase.co/functions/v1/round-robin-partner`

Recebe o `segment`, busca partners ativos na HubSpot CRM API com os filtros do segmento, consulta o `last_partner_id` no Supabase, avança uma posição na lista e salva o novo estado.

```typescript
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'

Deno.serve(async (req) => {
  const supabase = createClient(
    Deno.env.get('SUPABASE_URL')!,
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!
  )
  const { segment } = await req.json()

  // Filtros por segmento
  const SEGMENT_FILTERS = {
    'SMB_both': { filters: [
      { propertyName: 'partner_unit', operator: 'EQ', value: 'SMB' },
      { propertyName: 'service_demand_gen', operator: 'IN', values: ['Both'] }
    ]},
    'SMB_impl': { filters: [
      { propertyName: 'partner_unit', operator: 'EQ', value: 'SMB' },
      { propertyName: 'service_demand_gen', operator: 'IN', values: ['Implantation'] }
    ]},
    'MM_both': { filters: [
      { propertyName: 'partner_unit', operator: 'EQ', value: 'mid_market' }
    ]}
  }

  // 1. Busca partners ativos no HubSpot
  const hsRes = await fetch('https://api.hubapi.com/crm/v3/objects/2-54017777/search', {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${Deno.env.get('HUBSPOT_TOKEN')}` },
    body: JSON.stringify({
      filterGroups: [{ filters: SEGMENT_FILTERS[segment].filters }],
      properties: ['partner_id', 'partner__id'],
      limit: 100
    })
  })
  const hsData = await hsRes.json()
  const idsArray = hsData.results
    .map((r) => r.properties?.partner__id || r.properties?.partner_id)
    .filter(Boolean)

  // 2. Busca estado atual no Supabase
  const { data } = await supabase
    .from('round_robin_counters')
    .select('last_partner_id, call_count')
    .eq('key', segment).single()

  // 3. Calcula próximo índice
  const lastIndex = data.last_partner_id
    ? idsArray.indexOf(data.last_partner_id) : -1
  const nextIndex = (lastIndex + 1) % idsArray.length
  const nextPartnerId = idsArray[nextIndex]

  // 4. Atualiza estado
  await supabase.from('round_robin_counters')
    .update({ last_partner_id: nextPartnerId, call_count: data.call_count + 1 })
    .eq('key', segment)

  return new Response(
    JSON.stringify({ partner_id: nextPartnerId, index: nextIndex }),
    { headers: { 'Content-Type': 'application/json' } }
  )
})
```

---

### 6.7 Make

**Links:**

| Recurso | Link |
|---------|------|
| Cenário no Make | [us1.make.com · scenario 4705304](https://us1.make.com/402681/scenarios/4705304/edit) |
| Workflow HubSpot (trigger) | [app.hubspot.com · workflow 1810311966](https://app.hubspot.com/workflows/8180620/platform/flow/1810311966/edit) |

**Módulos por rota:**

| # | Módulo | Configuração |
|---|--------|-------------|
| 1 | Webhooks → Custom Webhook | Recebe `dealId`, `unit`, `demand_type` |
| 8 | Flow Control → Router | 3 rotas por `unit` e `demand_type` |
| 19 | HTTP → Make a Request | POST para Edge Function com `{"segment":"SMB_both"}` |
| — | HubSpot → Update a Deal | `partner_id = {{19.Data.partner_id}}` |

**Configuração do módulo HTTP:**

| Campo | Valor |
|-------|-------|
| URL | `https://jgublibcuopybkuxiagc.supabase.co/functions/v1/round-robin-partner` |
| Method | POST |
| Authorization | `Bearer <anon_key>` |
| Body SMB Both | `{"segment":"SMB_both"}` |
| Body SMB Impl | `{"segment":"SMB_impl"}` |
| Body MM Both | `{"segment":"MM_both"}` |

---

### 6.8 Operacional

**Resetar o contador de um segmento:**

```sql
-- Reinicia o round-robin do SMB_both do zero
update round_robin_counters
set call_count = 0, last_partner_id = NULL
where key = 'SMB_both';
```

**Adicionar ou remover partners:** nenhuma alteração necessária no Make ou na Edge Function — a lista é buscada dinamicamente no HubSpot a cada execução. Basta atualizar as propriedades `partner_unit` e `service_demand_gen` no objeto Partner.

> **Atenção:** Se um partner for removido e o `last_partner_id` apontar para ele, o `indexOf` retornará `-1` e o round-robin reiniciará do índice 0 automaticamente — sem quebrar o fluxo.

**Limitações conhecidas:**

- **Concorrência:** dois deals simultâneos podem ler o mesmo `last_partner_id` e receber o mesmo partner. Para volume alto, considerar lock otimista no Supabase.

**Scopes necessários — HubSpot Private App:**

| Scope | Uso |
|-------|-----|
| `crm.objects.deals.read` | Leitura dos deals |
| `crm.objects.deals.write` | Atualização do `partner_id` no deal |
| `crm.objects.custom.read` | Busca dos partners no objeto customizado |
