# Referência de comandos — Rovo Dev

| Comando acli | Comando a ser pesquisado no script Python | Permission tree | Descrição |
|---|---|---|---|
| `acli rovodev auth login` | `rovodev auth login` | `acli:rovodev:auth:write` | Authenticate to use Rovo Dev specific tasks. Use cases: authenticating an account before using protected commands. |
| `acli rovodev auth logout` | `rovodev auth logout` | `acli:rovodev:auth:write` | Remove authentication for a Rovo Dev account. Use cases: ending the current authenticated session. |
| `acli rovodev auth status` | `rovodev auth status` | `acli:rovodev:auth:read` | Show status for Rovo Dev account. Use cases: checking the current authentication or resource status. |
| `acli rovodev auth` | `rovodev auth` | `acli:rovodev:auth:read` | Authenticate to use Rovo Dev CLI. Use cases: discovering the available auth subcommands. |
| `acli rovodev` | `rovodev` | `acli:rovodev:read` | Atlassian’s AI coding agent: Rovo Dev (Beta). Use cases: discovering the available rovodev subcommands. |
