# Guia para Integrar GitHub ao Confluence

**Dono:** Rafael Tardelli  
**Última revisão:** 2026-04-28  
**Para quem é este guia:** Qualquer pessoa do time que queira contribuir com o repositório Partnerships Ops & Analytics.

---

## Como funciona o fluxo

```
Você edita um .md no GitHub → git push → GitHub Actions roda → Confluence atualiza
```

O Confluence é somente leitura para o time. Toda edição acontece no GitHub. O sync é automático.

---

## Parte 1: Configurar acesso (feito uma vez pelo dono do repositório)

### 1.1 Convidar a equipe no GitHub

1. Acesse o repositório: `https://github.com/rafaeltardelli-dotcom/cerebro_revops_01`
2. Clique em **Settings → Collaborators → Add people**
3. Adicione o usuário GitHub de cada pessoa do time
4. Peça para cada pessoa aceitar o convite no e-mail

### 1.2 Dar acesso ao espaço no Confluence

O espaço **Ops & Analytics (OPSAN)** já é acessível para pessoas da Tiendanube. Se alguém não conseguir visualizar:

1. Acesse o espaço no Confluence
2. Clique em **Space Settings → Permissions**
3. Adicione o usuário com permissão de **View**

---

## Parte 2: Configurar o ambiente local (feito uma vez por cada pessoa)

### 2.1 Instalar o Git

- **Windows:** Baixe em [git-scm.com](https://git-scm.com/) e instale com as opções padrão
- **Mac:** Abra o Terminal e rode `git --version` (instala automaticamente se não tiver)

### 2.2 Clonar o repositório

Abra o terminal e rode:

```bash
git clone https://github.com/rafaeltardelli-dotcom/cerebro_revops_01.git
cd cerebro_revops_01
```

### 2.3 Configurar seu nome no Git (só na primeira vez)

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@nuvemshop.com.br"
```

---

## Parte 3: Fluxo de trabalho do dia a dia

### 3.1 Antes de começar a editar — sempre atualize sua cópia local

```bash
git pull origin main
```

### 3.2 Edite o arquivo desejado

Abra qualquer arquivo `.md` dentro de `cerebro/` ou `onboarding/` com o editor de sua preferência (VS Code, Cursor, Notepad++, etc.) e faça as alterações.

### 3.3 Envie as alterações

```bash
git add nome-do-arquivo.md
git commit -m "docs: descreva o que você alterou"
git push origin main
```

**Exemplos de mensagens de commit:**
- `docs: atualiza regras de roteamento de leads MX`
- `feat: adiciona contexto de novo canal de parceiros`
- `fix: corrige nome do responsável no blueprint`

### 3.4 Aguarde o sync

Após o push, o GitHub Actions roda automaticamente em ~1 minuto. Abra o Confluence e a página já estará atualizada.

Para acompanhar o andamento do sync:  
`https://github.com/rafaeltardelli-dotcom/cerebro_revops_01/actions`

---

## Parte 4: Criar um novo documento

Para criar uma nova página no Confluence, você precisa fazer duas coisas:

**1. Criar o arquivo `.md`** na pasta correta:

```bash
# Exemplo: novo contexto de canal
cerebro/areas/contexto_novo_canal.md
```

**2. Adicionar a entrada no `confluence_map.json`** na raiz do repositório:

```json
{
  "file": "cerebro/areas/contexto_novo_canal.md",
  "title": "Título que aparece no Confluence",
  "space_key": "OPSAN",
  "parent_page_id": "1197768717"
}
```

Após o push, a página é criada automaticamente no Confluence dentro de **Partnerships Ops & Analytics**.

---

## Parte 5: Estrutura de pastas — onde cada documento vai

| O que você vai documentar | Pasta |
| :--- | :--- |
| Contexto de canal (Agências, Tech Partners, Afiliados) | `cerebro/areas/` |
| Contexto da empresa, HubSpot, brandbook | `cerebro/empresa/` |
| Projetos ativos e estratégicos | `cerebro/projects/` |
| Prompts e instruções para agentes de IA | `cerebro/agentes/` |
| Guias de entrada e governança | `onboarding/` |

---

## Dúvidas frequentes

**"Meu push foi rejeitado"**  
Rode `git pull origin main` antes de tentar o push novamente. Alguém pode ter enviado uma atualização enquanto você editava.

**"O Confluence não atualizou"**  
Verifique o status do workflow em `Actions` no GitHub. Se tiver um erro vermelho, abra o job `sync` e veja a mensagem de erro.

**"Quero editar direto no Confluence"**  
Não recomendado. Na próxima vez que o GitHub fizer push, a edição do Confluence será sobrescrita. O GitHub é sempre a fonte da verdade.

**"Não sei usar Git"**  
Peça ao Rafael ou use o Claude Code — ele executa todos os comandos de git por você. Basta descrever o que quer alterar.
