# Projeto Estratégico: Governança e Escala - Agências México
**Área:** RevOps & Analytics @ Nuvemshop
**Líder Técnico RevOps:** Rafael Tardelli
**Status:** Em Execução (Foco em Campanha de Aceleração Q2/2026)

## 1. Contexto e Desafio (The Gap)
A operação de Agências no México (Tiendanube) está em fase de tração e escalabilidade, suportada pelo fechamento do Mercado Shops e a entrada de parceiros estratégicos. No entanto, identificou-se um **gargalo de governança local**: falta de processos padronizados, dependência de conhecimento centralizado e fricção no roteamento de leads entre Vendas Diretas e Agências.
* **O Papel de RevOps:** Assumir a liderança tática na construção da infraestrutura de CRM, Dados e Processos para garantir que o *Country Manager* e o time local consigam executar a Campanha de Aceleração (início em 04/Maio) sem bloqueios operacionais.

## 2. Mapeamento de Iniciativas (RevOps Track)

| Frente de Atuação | Descrição da Entrega | Status | Owner |
| :--- | :--- | :--- | :--- |
| **Visibilidade de Dados** | Deploy do *Closing Pack Global* e do Dashboard Regional para acompanhamento de Performance (GMV, NPs, Sellers) no MX. | ✅ Concluído | RevOps Partnerships |
| **Arquitetura de CRM** | Implementação do objeto customizado "Partner" e pipelines de *Lifecycle* no HubSpot MX. | ✅ Concluído | RevOps Partnerships |
| **Formulário Service Request** | Criação do formulário dedicado para entrada de leads Mid-Market (Evolución) via agências. | ✅ Concluído | RevOps Partnerships |
| **Tracking de Leads MX** | Lista dinâmica no HubSpot para monitoramento em tempo real do pipeline gerado pelos formulários MX. | ✅ Concluído | RevOps Partnerships |
| **Política de Blindagem** | Regra de CRM para gerenciar conflitos de canal (Agência vs. Venda Direta / Sales). | ⏳ Pendente | RevOps Partnerships |
| **Higiene de Pipeline** | Automação de "Auto-lost" para expurgar deals inativos e liberar capacidade do funil comercial. | ⏳ Pendente | RevOps Sales |
| **Reciclagem (Non-ICP)** | Fluxo de envio de leads que não têm *fit* para Vendas Diretas (SMBs) para a base de Agências. | ⏳ Pendente | MKT / Growth |

## 3. Definições de Processos e Regras de Negócio
Estas regras definem o "SLA" de operação no CRM e devem ser estritamente seguidas:
* **Gatilho de Oportunidade:** Um negócio (Deal) só entra oficialmente na fase de "Oportunidade" a partir da etapa de *Problem Discovery*.
* **Triagem Obrigatória:** Todo formulário com perfil *Mid-Market* deve passar por triagem técnica de BizDev/SDR antes de ser roteado para a equipe de Sales.
* **Fluxo de Autoatendimento (SMB):** Se o lojista for classificado como SMB no formulário de Service Request, um fluxo automático enviará um aviso instruindo a agência a criar a loja diretamente em seu Portal (Self-service), sem onerar o time comercial.

## 4. Estratégia de Enablement (Descentralização)
Para evitar que o *Partner Manager* local seja o único ponto de falha (SPOF) no fluxo de informações:
1.  **Treinamento Cross-Team:** Sessão técnica agendada com toda a equipe do MX para nivelamento sobre a arquitetura do HubSpot e leitura dos Dashboards.
2.  **Documentação SSOT:** Utilização do Cérebro RevOps como base de conhecimento assíncrona para consultas de regras de roteamento e atribuição.
