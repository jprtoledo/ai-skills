---
name: atlassian-cli
description: >
  Consulta dinamicamente a documentação oficial dos comandos do Atlassian CLI.
  Use quando for necessário descobrir, explicar ou executar comandos do acli, incluindo suas opções, exemplos e permissões.
---

# Atlassian CLI skill

Referência dinâmica dos comandos do Atlassian CLI.

## Carregamento dinâmico

A referência completa de qualquer comando deve ser carregada pelo script `scripts/acli_command_reference.py`. Isso evita manter o conteúdo detalhado de todos os comandos no contexto da skill.

Execute a partir do diretório `atlassian-cli`:

```bash
python3 scripts/acli_command_reference.py jira workitem search
```

O comando pode ser informado com espaços, com o prefixo `acli` ou como slug:

```bash
python3 scripts/acli_command_reference.py "acli jira workitem search"
python3 scripts/acli_command_reference.py acli-jira-workitem-search
```

O script busca a página correspondente em `https://developer.atlassian.com/cloud/acli/reference/commands/{command}` e imprime a referência completa em Markdown.

## Pré-requisitos

- Ter o [Atlassian CLI (`acli`)](https://developer.atlassian.com/cloud/acli/guides/install/) instalado e disponível no `PATH` (`acli --version` deve funcionar).
- Ter o Python 3 instalado e disponível como `python3` (`python3 --version` deve funcionar), pois o script de carregamento da documentação é executado em Python.
- Ter uma conta Atlassian e autenticar antes de executar comandos protegidos, usando a referência de autenticação correspondente.

## Referências por grupo

Consulte a referência de acordo com o primeiro grupo do comando que o usuário quiser executar:

| Comando | Referência |
|---|---|
| `acli admin ...` | [Administração](references/admin.md) |
| `acli jira ...` | [Jira](references/jira.md) |
| `acli rovodev ...` | [Rovo Dev](references/rovodev.md) |
| `acli feedback` ou `acli` | [Comandos gerais](references/geral.md) |

As tabelas contêm o comando completo, o caminho aceito pelo script, a permission tree e a descrição. Para obter detalhes atualizados de opções, exemplos e permissões, carregue a documentação oficial do comando com o script abaixo:

```bash
python3 scripts/acli_command_reference.py <comando>
```

Por exemplo, para `acli jira workitem search`, consulte primeiro [references/jira.md](references/jira.md) e depois execute:

```bash
python3 scripts/acli_command_reference.py jira workitem search
```

## Exemplos de prompts e resultados esperados

### Consultar opções de um comando Jira

**Prompt:**

> Como uso `acli jira workitem search` para buscar itens de trabalho? Mostre as opções disponíveis.

**Resultado esperado:**

- Consultar primeiro [references/jira.md](references/jira.md) para confirmar o grupo e o caminho do comando.
- Executar `python3 scripts/acli_command_reference.py jira workitem search`.
- Responder com a sintaxe, opções, exemplos, permissões necessárias e observações da documentação oficial.

### Autenticar no Jira

**Prompt:**

> Preciso autenticar minha conta do Jira para usar o acli. Qual comando devo executar?

**Resultado esperado:**

- Consultar a entrada `acli jira auth login` em [references/jira.md](references/jira.md).
- Informar o comando `acli jira auth login`.
- Se necessário, carregar a referência detalhada com `python3 scripts/acli_command_reference.py jira auth login`.
- Lembrar que o `acli` precisa estar instalado e que a autenticação deve ser concluída antes dos comandos protegidos.

### Listar projetos

**Prompt:**

> Liste os projetos Jira que estão visíveis para mim usando o Atlassian CLI.

**Resultado esperado:**

- Identificar `acli jira project list` em [references/jira.md](references/jira.md).
- Apresentar o comando `acli jira project list` e sua finalidade.
- Consultar a documentação dinâmica para informar flags, formato de saída e permissões atuais.

### Administrar um usuário

**Prompt:**

> Como desativo um usuário na organização pelo acli?

**Resultado esperado:**

- Identificar `acli admin user deactivate` em [references/admin.md](references/admin.md).
- Carregar a referência oficial com `python3 scripts/acli_command_reference.py admin user deactivate`.
- Explicar os parâmetros obrigatórios, a permission tree `acli:admin:user:write` e alertar que a operação altera o acesso do usuário.

### Comando não reconhecido ou documentação necessária

**Prompt:**

> Execute `acli jira workitem search` no meu ambiente e busque itens do projeto ABC.

**Resultado esperado:**

- Verificar se o pré-requisito está atendido (`acli --version`) e se há autenticação válida.
- Consultar [references/jira.md](references/jira.md) e a documentação dinâmica do comando.
- Solicitar os parâmetros ausentes, como a consulta e os filtros desejados, antes de executar.
- Após confirmação dos parâmetros, executar o comando com segurança e relatar o resultado ou o erro retornado.
