# Referência de comandos — Administração

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
