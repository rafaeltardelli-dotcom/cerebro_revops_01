# Contexto Estratégico: Canal de Tech-Partners (Platform Ops)
**Área:** RevOps & Analytics @ Nuvemshop
**Fontes:** Assessment Tech-Partners, Platform Development & Ecosystem Data, Team Blueprint

## 1. Visão Geral e Objetivo do Ecossistema
O canal de Tech-Partners (Platform Development & Ecosystem) tem como foco fechar os *gaps* de produto da Nuvemshop através da integração de serviços de terceiros (Aplicações/Apps). 
O sucesso desta área baseia-se em 3 pilares (OKRs):
* **App Offer:** Melhorar a oferta de aplicações para resolver problemas dos lojistas (*merchants*).
* **App Quality & Experience:** Garantir estabilidade (redução de *Issues*) e boa experiência de utilização (Reviews/Ratings).
* **Monetization:** Aumentar a receita gerada pelo ecossistema através de *Revenue Share* e integração com o *Billing Engine* da Nuvemshop.

## 2. Segmentação de Parceiros e Apps
O ecossistema classifica as aplicações para definir o nível de acompanhamento e suporte:
* **Apps Orgânicos:** Sem prioridade estratégica imediata. O processo de homologação é feito exclusivamente pela equipa de *Tech Solutions*.
* **Apps Estratégicos:** Têm forte tração de mercado ou resolvem problemas críticos do *Mid-Market*. Têm acompanhamento dedicado de *Partner Managers*.
* **Visibilidade:** Podem ser **Públicos** (listados na App Store e obrigatoriamente homologados) ou **Privados** (como ERPs ocultos para *merchants* específicos, que não passam pela App Store).

## 3. Processos Operacionais e Gargalos (Dores de RevOps)

### A. Processo de Homologação (App Quality)
* **Fluxo Atual:** O parceiro pede a homologação no portal, o que gera um ticket no **Zendesk**. Toda a interação de recolha de artefactos (FAQ, POC, Dados de Publicação) ocorre por lá, com um SLA de 30 dias.
* **Gargalo:** Alta carga manual. Os dados ficam dispersos em folhas de cálculo (Google Sheets) e Zendesk, o que dificulta o *forecast* de homologações para a equipa técnica.

### B. Monetização e Revenue Share
* **Fluxo Atual:** A Nuvemshop fatura alguns serviços, mas em muitos casos (contratos externos), é o Parceiro que envia um relatório manual por e-mail com os valores das comissões devidas.
* **Gargalo:** Falta de visibilidade financeira automatizada. Não há uma projeção interna consolidada sobre quanto deveria ser pago pelo parceiro (com exceção das Apps de *Payments*). A consolidação é feita manualmente.

### C. Gestão de Issues (Bugs) e Problems (Gaps de Feature)
* **Fluxo Atual:** O *merchant* aciona o suporte da Nuvemshop, que precisa de acionar o parceiro. A equipa tem o OKR de controlar *Issues* com mais de 90 dias.
* **Gargalo:** A comunicação com o Tech-Partner é ruidosa e não padronizada (e-mail, Slack, formulários). Não há hierarquia ou criticidade definida para os alertas, e os *logs* são eliminados em 30 dias.

## 4. Liderança e Stakeholders (Pontos de Contacto)
* **Platform & Ecosystem:** Hendrick Aponte (Head SP LATAM), Flávia Almeida (SR Platform Ops Analyst - chave para processos históricos), Ana Borges (Tech Solutions & Professional Services), Luciana Bandeira (App Quality / Homologação).
* **RevOps (Squad Platform):** Débora Maffei (Process & Technology) e Lucas Abran (Data Analytics).

## 5. Arquitetura de Dados e North Star Metrics (NSM)
O modelo relacional no Data Lake (DBT) funciona através de uma ponte: `partner_id` → `app_id` → `store_id`. As principais métricas governadas são:
* **Adoção e Retenção:** MAU (*Monthly Active Users*), Instalações diárias/mensais, e *App Churn* (eliminando as reinstalações no mesmo dia).
* **Saúde e Qualidade:** *Density of Issues* (Issues/MAU), *App Health Score* (Uptime/Latência), *Average App Rating*.
* **Impacto no Negócio:** EMRR (*Ecosystem Monthly Recurring Revenue*), *Gross Apps Revenue Share*.

## 6. Diretrizes Estratégicas para RevOps (2026)
1.  **Migração para CRM (HubSpot):** Criar o objeto customizado "Partner" e mapear as propriedades para gerir a aquisição e o *lifecycle* no HubSpot, reduzindo a dependência exclusiva do Zendesk e das folhas de cálculo.
2.  **Centralização de Dados:** Criar *Data Products* no DBT que unifiquem os valores de *Revenue Share* real vs. estimado, automatizando a visão de P&E (*Platform & Ecosystem*) no Tableau.
