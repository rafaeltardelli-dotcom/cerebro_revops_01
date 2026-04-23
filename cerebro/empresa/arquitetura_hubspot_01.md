# Arquitetura de CRM e Dicionário de Dados (HubSpot)
**Área:** RevOps & Partnerships @ Nuvemshop
**Status:** Implementado (Arquitetura Global 2026)

## 1. Estrutura de Objetos e Relacionamentos (Entity-Relationship)
A fundação do CRM abandonou o uso genérico de "Companies" para parceiros e introduziu um **Custom Object** dedicado, permitindo escalabilidade e relação N:M.

* **Partner (Custom Object):** Objeto perene (nunca é fechado) dedicado à gestão do parceiro. Funciona como a "entidade mãe".
* **Company (Merchant):** Objeto perene dedicado à gestão dos lojistas/clientes.
* **Deal (Negócios):** Objeto transacional usado para medir pipeline. Subdividido em: *Partners Acquisition*, *Demand Gen* e *Services Request*.
* **Contacts:** Pessoas físicas subdivididas entre Contatos do Merchant e Contatos do Partner (Decisor / Influenciador).

**Mapeamento de Relacionamentos:**
* `Partner` (1:N) `Deals` (Um parceiro pode ter múltiplos projetos/negócios)
* `Partner` (N:M) `Companies/Merchants` (Múltiplos parceiros podem interagir com múltiplos lojistas ao longo do tempo).

## 2. Governança de Pipelines e Ciclo de Vida
O ciclo de vida do parceiro flui através de três pipelines principais:

### A. Global Partners Acquisition (Funil de Entrada)
Foco na prospecção e conversão inicial da agência/afiliado.
* **Lead / Prospect:** Levantada de mão via MKT ou prospecção manual. (Saída: 1ª reunião agendada).
* **Opportunity:** Em negociação. (Saída: Criação da conta no portal).
* **Activation:** Parceiro compromissado (Trial gerado). (Saída: Primeiro New Payment).
* **Active:** Parceiro ativado. (Ação: Owner atribuído e parceiro é transferido para o pipeline de Management).
* **Lost:** Não evoluiu na parceria (Gatilho automático após 90 dias sem avanço).

### B. Global Partners Management (Gestão de Carteira)
Foco na retenção, engajamento e geração recorrente de GMV.
* **Kickoff:** Parceiro pronto para onboarding.
* **Engaged:** Possui +1 loja ativa e trouxe indicação/NP nos últimos 3 meses.
* **Re-Engagement:** Esfriou (nenhum NP/Indicação nos últimos 3 meses).
* **At Risk:** Crítico (Nenhum NP há mais de 12 meses ou zerou lojas ativas).
* **Inactive / Lost:** Desligamento do programa ou inatividade severa (sai da régua de nutrição).

### C. Global Partner Services Request (Distribuição de Oportunidades)
* Fases: `Internal Request` > `Sent to agencies` > `First contact made` > `Proposal sent` > `Won` / `Lost`.

## 3. Dicionário de Propriedades Core (Objeto Partner)
As propriedades abaixo são vitais para o tracking de performance e automações (Make/DBT):

* **Partner ID:** Chave primária única do parceiro (usada em Supabase e Integrações).
* **Partner Unit:** Define a BU de atendimento (ex: `SMB`, `MM`).
* **Partner Type / Agencie Services:** Modelo de parceria e tipo de serviço prestado.
* **Partner Level:** Nível atual (Tier) da agência no programa de parceria.
* **Active Paying Stores Flg:** Volume em tempo real de lojistas ativos na carteira.
* **First / Last New Payment Date:** Datas críticas para gatilhos de automação (movimentação para Engaged ou At Risk).
* **Average L30D GMV Merchants:** Ticket médio de GMV da carteira nos últimos 30 dias.
* **Lost Reason:** Dropdown rigoroso (`Exclusive partnership with competitor`, `No response`, `Outside of IPP`, `Marketing nutrition [SMB]`, etc.).

## 4. Motor de Automações e SLAs (Rules Engine)
* **Criação do Partner (D+1):** Quando um painel é criado no produto, no dia seguinte (D+1) o objeto *Partner* é automaticamente instanciado no HubSpot.
* **SLA de Roteamento (Demand Gen):** Negócios (Leads de Merchants) parados há mais de 15 dias sem contato disparam alertas no Slack (`#mm-referral-[país]-notification`).
* **Transição Automática (Ativação):** O deal move-se sozinho da fase de Aquisição para "Kickoff" (Management) assim que o dado do primeiro New Payment entra no banco de dados.
