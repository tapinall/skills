---
name: tapinall-ai-visibility
description: "Measures and improves brand visibility in AI answers. Use when the user says 'does ChatGPT recommend us', 'AI visibility audit', 'track our brand in AI Overviews', 'why does Perplexity cite competitors', or 'GEO plan'."
---
# AI visibility with Tapinall

Act as the user's AI-search analyst: they know their buyers and their market; you hold the measurement method and the evidence on what AI engines cite. The outcome is a dated report of how often ChatGPT, Gemini, Perplexity, Copilot and Google's AI answers name the brand for the questions buyers ask, who they name instead, which sources they lean on, and what to do about it. Its consumers are the owner deciding where to spend effort, tapinall-seo turning the content gaps into pages, and the next run of this skill comparing against this one. That sets the bar: every rate comes from repeated runs of a frozen prompt set and carries its interval, every fix points at a cited URL or a prompt the brand lost, and no change is called real unless it clears the noise.

## Reads and writes

Reads, when present: `tap-suites/profile.md` (brand, name variants, domain, category, country, competitors, sales questions), `tap-suites/market/*.md` (buyer language, review and Reddit evidence), `tap-suites/seo/*.md` (owned pages, ranking keywords), and the latest `tap-suites/ai-visibility/*.md`, whose prompt set this run reuses. With no profile, ask for brand name and variants, domain, category, country and three competitors, write them to `tap-suites/profile.md` under its `Identity`, `Customer` and `Competitors` headings, and suggest tapinall-profile for the rest.

Writes:

- `tap-suites/ai-visibility/<YYYY-MM-DD>.md`, the contract file, with these sections in order: Run (date, country, language, engines and tool ids, repeats, prompt-set version, spend), Summary, Prompt set, Results per engine, Per-prompt grid, Competitor share of voice, Sources cited, Accuracy and sentiment issues, Change since last run, Fix plan (Cited sources missing the brand; Content gaps for tapinall-seo; Listings and communities), Not collected. Column layouts are in the references that produce them.
- `tap-suites/ai-visibility/<YYYY-MM-DD>-answers.csv`, one row per answer so a later run can re-score: `date,prompt_id,intent_id,stage,engine,tool_id,repeat,model,web_search,brand_mentioned,brand_position,brands_named,sentiment,accuracy_issue,cited_urls,answer_excerpt`. Lists inside a cell are `|`-separated; `brand_position` is blank when not mentioned.
- One ledger row per paid call in `tap-suites/ledger.md`.

Read `references/tapinall.md` before the first Tapinall call.

## Stages

1. Prompt set: read `references/prompt-set.md` and follow it. On a repeat run, reuse the previous set unchanged and only append; comparisons are made on prompts present in both runs.
2. Measurement: read `references/measurement.md` and follow it. Show the call count and cost against the agreed cap, and wait for a yes before the first paid call, since a full panel is hundreds of calls.
3. Fix plan: read `references/citation-and-fixes.md` and follow it. Write it only from what this run's answers and cited pages show.

A user who asks only for a quick check on one or two questions gets the measurement stage on those prompts, still with repeats, and a report that says it is a spot check rather than a baseline.

## End of run

Tell the user the file paths written; the headline unbranded mention rate with its interval and the change since the last run, if any; the top three fixes; the spend and running total from the ledger; and that tapinall-seo picks up the content gaps (and tapinall-outreach the listicle and publisher asks, if they want to pursue them). Suggest re-running with the same prompt set monthly or after a batch of fixes has gone live; weekly runs on a small budget mostly re-measure the noise.
