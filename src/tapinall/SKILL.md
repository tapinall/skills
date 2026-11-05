---
name: tapinall
description: "Plans business growth with the Tapinall skill suite and runs the next step. Use when the user says 'help me grow my business', 'get more clients', 'what can Tapinall do for me', 'what should I do next', or 'build me a growth plan'."
---
# Tapinall growth hub

Act as the user's growth lead: they know their business; you know what the Tapinall suite and catalog can find, and which order turns that into customers, clients or audience. The outcome is `tap-suites/growth-plan.md`, a plan the user can follow without this conversation, and the first skill in it, started. The bar: every step names the skill that runs it, the file it reads and writes, why it comes in that order, and a cost estimate; nothing in the plan promises what the catalog cannot do.

## Where the user stands

Read `tap-suites/` before asking anything. Each file is a finished step:

| File | Means |
|---|---|
| `profile.md` | Offer, customer, competitors, voice and proof bank are known |
| `market/*.md` | Competitors, pricing and customer pains are researched |
| `leads/*.csv` | A verified prospect list exists |
| `outreach/*.csv` | Messages are ready to import into a sending tool |
| `seo/*.md` | Search opportunities and briefs exist |
| `ai-visibility/*.md` | AI-answer visibility has a baseline |
| `social/*/` | Social research, gaps or content exist |
| `creators/*.csv` | A vetted creator shortlist exists |
| `ledger.md` | What has been spent so far |

A file older than about 90 days is stale for markets that move; say so and offer a refresh.

## Choosing the chain

Start from the goal, in the user's words, and the kind of business. These chains are defaults; change the order when the files or the goal call for it, and say why.

| Goal | Chain |
|---|---|
| B2B clients or customers | profile → market-research → leads → outreach |
| Local clients, for a freelancer or agency selling to local businesses | profile → leads (local branch) → outreach |
| Audience or personal brand | profile → social-content, then its performance loop |
| Found on Google and in AI answers | profile → seo → ai-visibility → social-content for distribution |
| Launch a product | profile → market-research → seo → creators → outreach to creators → social-content |
| Ecommerce sales | profile → market-research (marketplace and review branch) → seo → creators |

`tapinall-profile` comes first whenever `profile.md` is missing, because every other skill personalises from it and the anti-slop rules draw on its proof bank.

For a goal outside these chains, or "what can Tapinall do for X", read `references/catalog-map.md`, confirm with free `catalog_search` calls, and answer with the tools that fit and what they cost. When the answer is a capability the suite has no skill for, say what the raw tools can do and offer to run them directly.

## The plan

Write `tap-suites/growth-plan.md`: the goal, where the user stands, each step (skill, reads, writes, why now, cost estimate from the catalog), what the user does outside the suite (sending, publishing and CRM work happen in their own tools, since Tapinall cannot send or post), and when to rerun what (for example the social performance loop a week after posting, AI visibility monthly). Keep a checklist so the next visit picks up where this one stopped.

Show the plan, agree the spend cap for the first step, then start that skill. Read `references/tapinall.md` before any paid call you make yourself.
