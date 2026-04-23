# Dicionário de Métricas e KPIs: Canal de Agências
**Documento de Referência:** Closing Pack - Global Agencies (MBR/QBR Vision)
**Escopo:** Global (BR, AR, MX, CO, CL)

## 1. Métricas de Volume (The Big Four)
Estas são as métricas fundamentais que acompanham o ciclo de vida do lojista trazido pela agência:

* **[#] Trials:** Quantidade de lojas criadas (período de teste) associadas a um Partner ID. É o topo do funil de aquisição.
* **[#] New Payments (NP):** Lojistas que realizaram o primeiro pagamento da mensalidade. É o marco que valida a conversão da venda. No Closing Pack, acompanhamos o acumulado L12m (Last 12 Months).
* **[#] New Sellers (NS):** Lojistas que realizaram sua primeira venda (faturaram). Representa a "ativação" real do cliente no ecossistema.
* **[#] Active Sellers:** Lojistas que venderam pelo menos uma vez nos últimos 30 dias. É o indicador de saúde e retenção da carteira.

## 2. Métricas Financeiras e GMV
O GMV é a nossa "Estrela Guia" para medir o tamanho e o impacto dos parceiros:

* **Managed GMV (Gross Merchandise Volume):** Volume total de vendas processado pelas lojas da carteira da agência. 
    * Reportado em **USD** (para visão global) e **Local Currency** (para gestão regional).
* **Monthly AVG GMV (L3m):** Média móvel do GMV dos últimos 3 meses. Filtra sazonalidades e reflete o momento atual do parceiro.
* **Share of Nuvemshop GMV:** Porcentagem do GMV total da Nuvemshop que é gerada através do canal de agências.
* **Managed Revenue (SaaS):** Receita de mensalidades gerada pela base de lojistas ativos do parceiro.

## 3. Funil de Conversão e Cohorts
Medimos a eficiência do canal através das taxas de passagem (CVR):

* **Trial to Payment CVR:** Eficiência da agência em transformar interessados em clientes pagantes (Média global esperada: ~55%).
* **Payment to Seller CVR:** Eficiência em colocar o cliente para vender ("Go-live"). 
* **Cohort Analysis:** Acompanhamento da maturação dos lojistas por mês de entrada (M0, M1, M2...). Vital para identificar se o "tempo para vender" está aumentando.

## 4. Segmentação e Perfil (SMB vs. Next)
As métricas são segmentadas para diferenciar o volume da complexidade:

* **Next / Mid-Market (MM) Deals:** Foco em lojistas de alto ticket. Inclui métricas de **Upgrades** (lojas que cresceram e migraram para o plano Next).
* **SMB / Escala:** Foco em volume e tração orgânica.
* **Assigned Merchants:** Lojistas que não foram adquiridos pela agência, mas que foram atribuídos à sua carteira para gestão e farming.

## 5. O Partner Performance Score (Ranking)
Utilizamos uma lógica de **Min-Max Scaling (0-100)** para classificar as agências globalmente e por país, baseada em um mix de:
* Volume de Active Stores.
* Volume de Sellers.
* GMV L12m.
* New Payments L12m.

**Classificação de Performance:**
| Categoria | Percentil | Descrição |
| :--- | :--- | :--- |
| **Top Performer** | Top 5% | Elite do canal, foco total em benefícios exclusivos e co-marketing. |
| **High Performer** | Top 25% | Agências em escala, potenciais candidatas ao topo. |
| **Medium Performer** | Top 50% | Base estável do canal. |
| **Low Performer** | Bottom 50% | Agências com baixa ativação ou em declínio (Candidatas à carteira Phoenix). |

## 6. Governança de Dados
* **Ponto de Corte:** Os dados de performance são fechados no 3º dia útil de cada mês.
* **Fontes de Dados:** Tabelas de Databricks (SQL), Tableau Import e bases manuais de FP&A para Budgets.
