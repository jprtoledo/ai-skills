---
name: acli-skill
description: >
  Consulta dinamicamente a documentação oficial dos comandos do Atlassian CLI.
  Use quando for necessário descobrir, explicar ou executar comandos do acli, incluindo suas opções, exemplos e permissões.
---

# Atlassian CLI skill

Referência dinâmica dos comandos do Atlassian CLI.

## Carregamento dinâmico

A referência completa de qualquer comando deve ser carregada pelo script `scripts/acli_command_reference.py`. Isso evita manter o conteúdo detalhado de todos os comandos no contexto da skill.

Execute a partir do diretório `acli-skill`:

```bash
python3 scripts/acli_command_reference.py jira workitem search
```

O comando pode ser informado com espaços, com o prefixo `acli` ou como slug:

```bash
python3 scripts/acli_command_reference.py "acli jira workitem search"
python3 scripts/acli_command_reference.py acli-jira-workitem-search
```

O script busca a página correspondente em `https://developer.atlassian.com/cloud/acli/reference/commands/{command}` e imprime a referência completa em Markdown.

## Comandos

| Comando acli | Comando a ser pesquisado no script Python | Permission tree | Descrição |
|---|---|---|---|
| `acli admin auth login` | `admin auth login` | `acli:admin:auth:write` | Authenticate for the organization admin-specific tasks. Use cases: authenticating an account before using protected commands. |
| `acli admin auth logout` | `admin auth logout` | `acli:admin:auth:write` | Remove authentication and log out of organization admin account. Use cases: ending the current authenticated session. |
| `acli admin auth status` | `admin auth status` | `acli:admin:auth:read` | Show status for organization admin account. Use cases: checking the current authentication or resource status. |
| `acli admin auth switch` | `admin auth switch` | `acli:admin:auth:write` | Switch between Atlassian organization admin accounts. Use cases: changing the active account or context. |
| `acli admin auth` | `admin auth` | `acli:admin:auth:read` | Authenticate to use Atlassian CLI for organization admin tasks. Use cases: discovering the available auth subcommands. |
| `acli admin user activate` | `admin user activate` | `acli:admin:user:write` | Activate a user. Use cases: activating a managed user when access should be restored. |
| `acli admin user cancel-delete` | `admin user cancel delete` | `acli:admin:user:cancel:write` | Cancel deletion of a managed account from Atlassian Administration. Use cases: removing a resource or record that is no longer needed. |
| `acli admin user deactivate` | `admin user deactivate` | `acli:admin:user:write` | Deactivate a user. Use cases: suspending access for a managed user. |
| `acli admin user delete` | `admin user delete` | `acli:admin:user:write` | Delete a managed account from Atlassian Administration. Use cases: removing a resource or record that is no longer needed. |
| `acli admin user` | `admin user` | `acli:admin:user:read` | Manage a user within your Atlassian organization. Use cases: discovering the available user subcommands. |
| `acli admin` | `admin` | `acli:admin:read` | Admin commands. Use cases: discovering the available admin subcommands. |
| `acli feedback` | `feedback` | `acli:write` | Submit a request or report a problem. Use cases: reporting a problem or submitting a request to Atlassian. |
| `acli jira auth login` | `jira auth login` | `acli:jira:auth:write` | Authenticate with an Atlassian host. Use cases: authenticating an account before using protected commands. |
| `acli jira auth logout` | `jira auth logout` | `acli:jira:auth:write` | Logout from Jira account. Use cases: ending the current authenticated session. |
| `acli jira auth status` | `jira auth status` | `acli:jira:auth:read` | Show Jira account status. Use cases: checking the current authentication or resource status. |
| `acli jira auth switch` | `jira auth switch` | `acli:jira:auth:write` | Switch between Jira accounts. Use cases: changing the active account or context. |
| `acli jira auth` | `jira auth` | `acli:jira:auth:read` | Authenticate to use Atlassian CLI. Use cases: discovering the available auth subcommands. |
| `acli jira board list-sprints` | `jira board list sprints` | `acli:jira:board:read` | Get all sprints. Use cases: listing resources for review or further processing. |
| `acli jira board search` | `jira board search` | `acli:jira:board:read` | Search through all the boards. Use cases: finding resources by text, filters, or query criteria. |
| `acli jira board` | `jira board` | `acli:jira:board:read` | Jira board commands. Use cases: discovering the available board subcommands. |
| `acli jira dashboard search` | `jira dashboard search` | `acli:jira:dashboard:read` | Searches for the Jira dashboards. When multiple search parameters are present, the search ensures that all the parameters are satisfied. Use cases: finding resources by text, filters, or query criteria. |
| `acli jira dashboard` | `jira dashboard` | `acli:jira:dashboard:read` | Jira dashboard commands. Use cases: discovering the available dashboard subcommands. |
| `acli jira field cancel-delete` | `jira field cancel delete` | `acli:jira:field:cancel:write` | Restores the field from the trash. Use cases: removing a resource or record that is no longer needed. |
| `acli jira field create` | `jira field create` | `acli:jira:field:write` | Create a custom field in Jira. Use cases: creating a new resource or record. |
| `acli jira field delete` | `jira field delete` | `acli:jira:field:write` | Moves a custom field to trash. Use cases: removing a resource or record that is no longer needed. |
| `acli jira field` | `jira field` | `acli:jira:field:read` | Jira field commands. Use cases: discovering the available field subcommands. |
| `acli jira filter add-favourite` | `jira filter add favourite` | `acli:jira:filter:add:favourite:read` | Add a filter as favourite. Use cases: discovering the available favourite subcommands. |
| `acli jira filter change-owner` | `jira filter change owner` | `acli:jira:filter:change:owner:read` | Change the owner of the provided filters. Use cases: discovering the available owner subcommands. |
| `acli jira filter list` | `jira filter list` | `acli:jira:filter:read` | List filter that are either my or favourite. Use cases: listing resources for review or further processing. |
| `acli jira filter search` | `jira filter search` | `acli:jira:filter:read` | Searches for Jira filters. When multiple search parameters are present, the search ensures that all the parameters are satisfied. Use cases: finding resources by text, filters, or query criteria. |
| `acli jira filter` | `jira filter` | `acli:jira:filter:read` | Jira filter commands. Use cases: discovering the available filter subcommands. |
| `acli jira project archive` | `jira project archive` | `acli:jira:project:write` | Archives a Jira project. Use cases: removing inactive items from the active workspace while preserving the ability to restore them. |
| `acli jira project create` | `jira project create` | `acli:jira:project:write` | Create a Jira project which is a collection of work items (stories, bugs, tasks, etc). You would typically use a project to represent the development work for a product, project, or service in Jira. Use cases: creating a new resource or record. |
| `acli jira project delete` | `jira project delete` | `acli:jira:project:write` | Deletes a Jira project. Use cases: removing a resource or record that is no longer needed. |
| `acli jira project list` | `jira project list` | `acli:jira:project:read` | List of projects visible to the user. Use cases: listing resources for review or further processing. |
| `acli jira project restore` | `jira project restore` | `acli:jira:project:write` | Restore a Jira project. Use cases: recovering an archived or deleted resource. |
| `acli jira project update` | `jira project update` | `acli:jira:project:write` | Update a Jira project. Use cases: changing the configuration or properties of an existing resource. |
| `acli jira project view` | `jira project view` | `acli:jira:project:read` | Fetches a Jira project. Use cases: retrieving details for inspection or automation. |
| `acli jira project` | `jira project` | `acli:jira:project:read` | Jira project commands. Use cases: discovering the available project subcommands. |
| `acli jira sprint list-workitems` | `jira sprint list workitems` | `acli:jira:sprint:read` | List work items in a sprint. Use cases: listing resources for review or further processing. |
| `acli jira sprint` | `jira sprint` | `acli:jira:sprint:read` | Jira sprint commands. Use cases: discovering the available sprint subcommands. |
| `acli jira workitem archive` | `jira workitem archive` | `acli:jira:workitem:write` | Archives a work item or multiple work items. Archive a work item if you want to remove it from your project without deleting it. If you archive a work item, it will only appear in Archived work items and can no longer be edited. You can restore an archived work item if you need it in the future. Use cases: removing inactive items from the active workspace while preserving the ability to restore them. |
| `acli jira workitem assign` | `jira workitem assign` | `acli:jira:workitem:write` | Assign a work item to an assignee or multiple work items to multiple assignees. Use cases: assigning work to a specific user, the current user, or a default assignee. |
| `acli jira workitem attachment delete` | `jira workitem attachment delete` | `acli:jira:workitem:attachment:write` | Delete an attachment from a workitem. Use cases: removing a resource or record that is no longer needed. |
| `acli jira workitem attachment list` | `jira workitem attachment list` | `acli:jira:workitem:attachment:read` | List all the attachments of a workitem. Use cases: listing resources for review or further processing. |
| `acli jira workitem attachment` | `jira workitem attachment` | `acli:jira:workitem:attachment:read` | Work item attachments commands. Use cases: discovering the available attachment subcommands. |
| `acli jira workitem clone` | `jira workitem clone` | `acli:jira:workitem:write` | Create a duplicate of a work item or multiple work items by cloning within the same project or site, copying over most information from a work item like the Summary and Description fields and more. Use cases: creating a duplicate while reusing the source configuration or content. |
| `acli jira workitem comment create` | `jira workitem comment create` | `acli:jira:workitem:comment:write` | Add a comment to a work item or multiple work items using the default visibility for the project. Use cases: creating a new resource or record. |
| `acli jira workitem comment delete` | `jira workitem comment delete` | `acli:jira:workitem:comment:write` | Delete a comment for a given workitem. Use cases: removing a resource or record that is no longer needed. |
| `acli jira workitem comment list` | `jira workitem comment list` | `acli:jira:workitem:comment:read` | List comments for a work item. Use cases: listing resources for review or further processing. |
| `acli jira workitem comment update` | `jira workitem comment update` | `acli:jira:workitem:comment:write` | Update a comment on a work item. Use cases: changing the configuration or properties of an existing resource. |
| `acli jira workitem comment visibility` | `jira workitem comment visibility` | `acli:jira:workitem:comment:read` | Get visibility options for work item comments. Use cases: checking available visibility settings for a resource. |
| `acli jira workitem comment` | `jira workitem comment` | `acli:jira:workitem:comment:read` | Work item comments commands. Use cases: discovering the available comment subcommands. |
| `acli jira workitem create-bulk` | `jira workitem create bulk` | `acli:jira:workitem:write` | Bulk create Jira issues. Use cases: creating a new resource or record. |
| `acli jira workitem create` | `jira workitem create` | `acli:jira:workitem:write` | Create a Jira work item to track individual pieces of work that must be completed. Use cases: creating a new resource or record. |
| `acli jira workitem delete` | `jira workitem delete` | `acli:jira:workitem:write` | Delete a work item or multiple work items. Use cases: removing a resource or record that is no longer needed. |
| `acli jira workitem edit` | `jira workitem edit` | `acli:jira:workitem:write` | Edit a Jira work item or multiple work items. Use cases: updating fields on an existing resource. |
| `acli jira workitem link create` | `jira workitem link create` | `acli:jira:workitem:write` | Create links between work items. Use cases: creating a new resource or record. |
| `acli jira workitem link delete` | `jira workitem link delete` | `acli:jira:workitem:write` | Delete links between work items. Use cases: removing a resource or record that is no longer needed. |
| `acli jira workitem link list` | `jira workitem link list` | `acli:jira:workitem:write` | List all the links of a workitem. Use cases: listing resources for review or further processing. |
| `acli jira workitem link type` | `jira workitem link type` | `acli:jira:workitem:write` | Get available workitem link types. Use cases: checking the available types for a resource. |
| `acli jira workitem link` | `jira workitem link` | `acli:jira:workitem:write` | Link work items commands. Use cases: discovering the available link subcommands. |
| `acli jira workitem search` | `jira workitem search` | `acli:jira:workitem:read` | Searches for work item or multiple work items. Use cases: finding resources by text, filters, or query criteria. |
| `acli jira workitem transition` | `jira workitem transition` | `acli:jira:workitem:write` | Transitioning a work item can mean moving it to another status, or performing a looped transition where the transition allows you to perform an action but keep the work item in its current status. Use cases: moving a work item to another workflow status or executing a workflow action. |
| `acli jira workitem unarchive` | `jira workitem unarchive` | `acli:jira:workitem:write` | Unarchives work item or multiple work items. Use cases: returning an archived resource to active use. |
| `acli jira workitem view` | `jira workitem view` | `acli:jira:workitem:read` | Retrieve information about Jira work items. Use cases: retrieving details for inspection or automation. |
| `acli jira workitem watcher remove` | `jira workitem watcher remove` | `acli:jira:workitem:watcher:write` | Remove a watcher from an issue. Use cases: removing an association, watcher, or related resource. |
| `acli jira workitem watcher` | `jira workitem watcher` | `acli:jira:workitem:watcher:read` | Work item watcher commands. Use cases: discovering the available watcher subcommands. |
| `acli jira workitem` | `jira workitem` | `acli:jira:workitem:read` | Jira work item commands. Use cases: discovering the available workitem subcommands. |
| `acli jira` | `jira` | `acli:jira:read` | Jira Cloud commands. Use cases: discovering the available jira subcommands. |
| `acli rovodev auth login` | `rovodev auth login` | `acli:rovodev:auth:write` | Authenticate to use Rovo Dev specific tasks. Use cases: authenticating an account before using protected commands. |
| `acli rovodev auth logout` | `rovodev auth logout` | `acli:rovodev:auth:write` | Remove authentication for a Rovo Dev account. Use cases: ending the current authenticated session. |
| `acli rovodev auth status` | `rovodev auth status` | `acli:rovodev:auth:read` | Show status for Rovo Dev account. Use cases: checking the current authentication or resource status. |
| `acli rovodev auth` | `rovodev auth` | `acli:rovodev:auth:read` | Authenticate to use Rovo Dev CLI. Use cases: discovering the available auth subcommands. |
| `acli rovodev` | `rovodev` | `acli:rovodev:read` | Atlassian’s AI coding agent: Rovo Dev (Beta). Use cases: discovering the available rovodev subcommands. |
| `acli` | `acli` | `acli:acli:read` | Utilize Atlassian Command Line Interface (CLI) to effortlessly engage with our suite of products through a streamlined command-line interface. Atlassian CLI provides a powerful toolset that allows users to automate tasks, integrate processes, and interact with various Atlassian products such as Jira, all from the comfort of your terminal. Use cases: discovering the available Atlassian CLI commands. |
