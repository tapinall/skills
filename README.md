# Tapinall skills

Nine agent skills that help brands, freelancers and founders grow: market research, lead lists, outreach, SEO, AI-answer visibility, social content and creator partnerships. They chain together through shared files, and every claim they write is backed by data fetched live from [Tapinall](https://tapinall.com/?utm_source=github&utm_medium=readme&utm_campaign=tapinall-skills), one metered API over about a thousand data tools.

## Install

With the [skills CLI](https://skills.sh) (Claude Code, Cursor, Codex, OpenCode, Gemini CLI and more):

```bash
npx skills add tapinall/skills
```

Install one skill only:

```bash
npx skills add tapinall/skills --skill tapinall-leads
```

As a Claude Code plugin:

```text
/plugin marketplace add tapinall/skills
/plugin install tapinall-suite@tapinall
```

The plugin also connects Tapinall's MCP server: run `/mcp`, pick Tapinall and sign in, and the skills are ready.

## Connect Tapinall

New accounts get $1 of test credit. [Create an account](https://tapinall.com/v1/auth/login?screen=register&utm_source=github&utm_medium=readme&utm_campaign=tapinall-skills), make a project token, then:

```bash
curl -fsSL https://tapinall.com/install.sh | sh
tapinall login
tapinall mcp install --host claude   # or cursor, codex, opencode, gemini
```

Or just run any skill: if Tapinall is not set up yet, it walks you through it.

## Start here

Ask your agent: **"help me grow my business"**. The `tapinall` hub reads what you have, picks the chain for your goal, and starts it.

| Skill | What it does |
|---|---|
| `tapinall` | Plans the chain for your goal and runs the next step |
| `tapinall-profile` | Your offer, customer, competitors, voice and proof bank, read by every other skill |
| `tapinall-market-research` | Competitors, pricing, review pains, hiring and ad signals |
| `tapinall-leads` | Verified B2B and local-business prospect lists |
| `tapinall-outreach` | Personalised sequences from real, dated signals, exported for your sending tool |
| `tapinall-seo` | Keyword and backlink gaps, ranked opportunities, content briefs |
| `tapinall-ai-visibility` | Whether ChatGPT, Gemini and Perplexity recommend you, and what to fix |
| `tapinall-social-content` | Research, content gaps, production and a performance loop |
| `tapinall-creators` | Find and vet creators for partnerships and UGC |

Typical chains:

- **B2B clients**: profile → market-research → leads → outreach
- **Local clients**: profile → leads (local) → outreach
- **Audience**: profile → social-content
- **Found on Google and in AI answers**: profile → seo → ai-visibility

Everything is written to `tap-suites/` in your project. The skills never send, post or publish; you stay in control of every send.

## Costs

Each skill agrees a spend cap with you before its first paid call, sets a per-call limit, and logs every charge to `tap-suites/ledger.md`. Catalog searches are free.

## Contributing

Shared knowledge lives once in `src/shared/` and is copied into each skill by `uv run scripts/sync_shared.py`; edit the shared file, then run the sync. Conventions are in [src/CONVENTIONS.md](src/CONVENTIONS.md); each skill cites its research in its own `SOURCES.md`.
