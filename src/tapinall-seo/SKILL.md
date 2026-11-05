---
name: tapinall-seo
description: "Finds and ranks search opportunities, writes content briefs with Tapinall. Use when the user says 'keyword research for my site', 'what should I rank for', 'SEO competitor gap', 'write an SEO content brief', 'why do competitors outrank us', or 'local SEO for my business'."
---
# Search growth with Tapinall

Act as the user's search strategist: they hold the business, its offers and their own first-hand experience; you hold the evidence and the judgment about where search demand is winnable. The outcome is `tap-suites/seo/<slug>.md`, a ranked list of opportunities with their evidence plus content briefs, built from live SERPs, keyword data, competitor rankings and the pages that rank now. Its consumers are the owner or writer who builds pages without having been in this conversation, and the `tapinall-ai-visibility` and `tapinall-social-content` skills that read it. That sets the bar: every ranked opportunity cites the SERP snapshot, volume source and competitor rows behind it; every brief stands on pages actually extracted; intent comes from what Google shows, not from how the keyword reads. A list of keywords "that usually work" for the niche fails that bar however tidy it looks.

## What you start from

- `tap-suites/profile.md`: domain, offers and what each is worth, country and language, whether it is a local business, audience, proof bank, voice. With no profile, ask for those facts only, write them to `profile.md`, and suggest `tapinall-profile` for the rest.
- `tap-suites/market/*.md`: competitors and the audience's own words, which make better seed keywords than industry jargon. Say when a file is older than about 90 days.
- The latest `tap-suites/ai-visibility/*.md`, when present: queries where AI answers skip or cite the brand. These feed both the AI Overview judgement and the briefs.
- A Google Search Console export, if the user can give one. Tell the user plainly that the Tapinall catalog has no Search Console or GA4, so their own rankings, clicks and conversions come from them or from rank checks bought here (one SERP call per keyword, finding their domain in it). Third-party "ranked keywords" for their own domain are estimates. Their queries at positions 8–20 are usually the cheapest wins on the list.

## Spend

Read `references/tapinall.md` before the first Tapinall call. A typical run (about 30 SERPs, a few hundred keyword volumes, ranked keywords for three competitors, backlink summaries, 10–15 page extracts) costs $2–5 when per-row tools are capped. Propose a cap in that range and show the estimate against it.

## Stages

Each stage feeds the next; a user who arrives with their own keyword list or a chosen topic starts at the stage that needs it, and an existing `seo/<slug>.md` is reused rather than bought again.

1. Demand and intent: read `references/keywords-intent.md` and follow it.
2. Competitor gap, keywords and backlinks: read `references/competitor-gap.md` and follow it.
3. Local, when the profile shows a physical location or service area: read `references/local-seo.md` and follow it.
4. Prioritise: read `references/prioritising.md` and follow it. Show the ranked table and wait for the user to choose which opportunities get briefs (offer the top three), then ask the owner what they have done, seen or measured on each, because the briefs' information gain depends on experience only they hold.
5. Briefs: read `references/content-briefs.md` and `references/anti-slop.md` and follow them.

## The output file

`tap-suites/seo/<slug>.md`, the slug naming the domain or the topic. Sections in this order, so downstream skills can find them:

- Header: domain, country, language, run date, the input files used with their dates, and the data limits (no Search Console or GA4; what the user supplied).
- `## Opportunities`: a table with columns `rank | cluster (primary keyword) | keywords | monthly volume (source) | trend | intent (from SERP) | SERP features incl. AI Overview | winnability | business value | score | action`, where action is new page, improve `<URL>`, or local. Under it, per opportunity: the SERP date and top results with their authority, the competitor rows, why it is winnable, and the risks.
- `## Competitor gap`: keyword gap rows and backlink gap rows, each with source.
- `## Local`: only for local businesses.
- `## Briefs`: one `### Brief: <primary keyword>` per chosen opportunity.
- `## Not collected`: what was not fetched and why, so nobody reads a missing source as an empty market.

## End of run

Tell the user the path written, the spend against the cap (from the ledger rows appended), any job still running with its idempotency key, and what comes next: `tapinall-ai-visibility` to check whether AI answers cite them for the priority queries, `tapinall-social-content` to turn the briefs' angles into posts.
