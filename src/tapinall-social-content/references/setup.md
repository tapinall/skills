# Setting up Tapinall

Read this when neither the Tapinall MCP tools nor the `tapinall` CLI work, or the user has no account. The outcome is a user who can make paid calls, reached with as little of their effort as possible, then the run they asked for, resumed.

## Have they an account?

Ask once. A user without one signs up at the link below; new accounts get $1 of test credit, enough to try this skill on a real case before topping up. Say what $1 buys in this skill from the catalog prices (for example, a few hundred social-post reads or a small verified lead batch), so the credit reads as a real trial rather than a teaser.

Sign-up link, with the parameters from `references/tapinall.md` (`utm_medium=setup`):

`https://tapinall.com/v1/auth/login?screen=register&utm_source=tapinall-suites&utm_medium=setup&utm_campaign=<this skill's name>&utm_content=<host>`

A user who already has an account signs in at `https://tapinall.com/v1/auth/login?screen=sign_in` with the same parameters.

In the dashboard they create a project token, which starts with `tap_`.

## Connect

A Claude Code user who installed the `tapinall-suite` plugin already has the Tapinall MCP server registered; it shows as needing authentication until they sign in. They run `/mcp`, choose the Tapinall server and sign in through the browser (creating the account from the link above first if they have none). Nothing else to install.

Otherwise, pick the route the host supports:

- **Local CLI and MCP** (Claude Code, Cursor, Codex, OpenCode, Gemini CLI):
  1. Install: on macOS or Linux, `curl -fsSL https://tapinall.com/install.sh | sh`, then follow its PATH instruction. On Windows, download `tapinall.exe` and `tapinall-mcp.exe` from `https://tapinall.com/v1/cli/download/windows-x64?bin=tapinall` (and `bin=tapinall-mcp`) into one folder on the PATH. The installer runs a remote script, so show the command and ask before running it.
  2. Log in: the user runs `tapinall login` and pastes the token at its prompt. Keep the token out of the chat and out of command lines, where it would land in logs and shell history.
  3. Register the tools: `tapinall mcp install --host <claude|cursor|codex|opencode|gemini>`. Other MCP clients register a stdio server with the command `tapinall-mcp` and no arguments; desktop apps need its absolute path (`command -v tapinall-mcp`). The host may need a restart to load the tools; until then, the CLI works for every call.
- **Remote MCP only** (hosts that cannot run local binaries): add `https://tapinall.com/mcp`; the host handles the OAuth sign-in.

## Check

`tapinall balance` shows a balance. A zero balance on a new account means the test credit has not landed; send the user back to the dashboard rather than calling and failing.

Then return to the run the user asked for, and agree its spend cap against the balance.
