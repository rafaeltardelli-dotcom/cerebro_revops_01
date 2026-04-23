# Deep-Dive Estratégico: Canal de Agências (Especialistas)
**Área:** RevOps & Analytics @ Nuvemshop
**Status:** Versão Consolidada 2026 (BR & MX)

## 1. Diagnóstico e Validação de Mercado (O Caso Mercado Shops)
O ano de 2025 serviu como a "Prova de Conceito" definitiva para o canal de agências focado em Mid-Market (NEXT).
* **Tração Real:** O fechamento do Mercado Shops foi o principal catalisador, provando que agências estratégicas (como *Digital Growth*, *Hobby Digital*, *Suma* e *Estúdio Merca*) conseguem mover o ponteiro de receita rapidamente quando há uma narrativa clara.
* **KPIs de Sucesso:** Foram gerados **57 deals Won de NEXT** (YTD Nov/25), totalizando aproximadamente **R$ 15 milhões em GMV**. Isso demonstra que o canal de agências é a alavanca mais barata e eficiente para aquisição de contas de alto ticket.

## 2. Infraestrutura de RevOps: A "Limpeza" dos Sistemas
A complexidade técnica herdada de anos de operação fragmentada está sendo substituída por um modelo escalável liderado por RevOps:
* **Objeto "Partner" no HubSpot:** O movimento mestre de 2026. Saímos de uma arquitetura baseada em "Empresas" genéricas para um objeto nativo que permite o cálculo de **RUM (Revenue Under Management)** e a relação direta entre `PSM (Partner Success Manager) x Partner x Deal`.
* **Consolidação de Pipelines:** Redução drástica de **17 pipelines locais para ~4 pipelines globais**. Isso não apenas simplifica o reporting, mas remove o risco técnico de atingir os limites de automação do HubSpot.
* **Sincronização de Dados:** Unificação entre HubSpot e sistemas internos via **Make/DBT**, garantindo que o Partner ID seja a chave única em todo o ecossistema.

## 3. Motor de Demand Gen: Roteamento e Game Theory
Para manter as agências engajadas, implementamos um sistema de reciprocidade baseado em meritocracia e urgência:
* **O Modelo de Distribuição:**
    * **Leads SMB (Escala):** Roteamento sequencial (Round Robin) para 1 parceiro.
    * **Leads Mid-Market (Next):** Envio simultâneo para 3 parceiros para estimular a competitividade e velocidade de atendimento.
* **A Regra do SLA de 48h:** Leads que não sofrerem interação da agência em 48h disparam uma automação para o lojista oferecendo o Marketplace, garantindo que a oportunidade não "morra" no pipeline do parceiro.
* **Conecta D2C:** Implementação de campos de origem específicos para eventos presenciais, permitindo medir o ROI de patrocínios e prospecções em campo.

## 4. O "Churn" Invisível: A Curva de Decaimento
Analisamos um padrão crítico: agências apresentam um pico de produtividade nos primeiros 3 meses após o onboarding e entram em um **decaimento de geração de deals** subsequente.
* **Hipótese:** Perda de *momentum* comercial e falta de rituais de re-onboarding ou atualização técnica.
* **Ação RevOps:** Estruturação de estratégias de **Nurturing para a Base Phoenix** (agências ativas mas estagnadas) e criação do papel de *Partner Success* focado exclusivamente em expansão de carteira (Farming).

## 5. Diferenciação Regional (Visão LatAm)
* **Brasil (Madureza):** Foco em tierização (Silver, Gold, Platinum) e especialização em migrações complexas. A meta é aumentar o número de agências que geram mais de 5 deals de NEXT por ano.
* **México (Comunidade):** Fase de atração de "Shopify-like agencies". O foco é criar uma comunidade de elite (~10 agências) para sustentar o lançamento de novas features e o crescimento da Tiendanube no mercado local.

## 6. Governança e Staffing
Divisão clara de papéis para evitar sobreposição:
* **Partner Acquisition (Hunting):** Foco em trazer agências com ICP de Mid-Market.
* **Partner Success (Farming):** Gestão 1:1 para agências Platinum/Next.
* **Community Manager:** Gestão da cauda longa e parceiros SMB através de automações e portais *self-service*.
