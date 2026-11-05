# Measuring the engines

The outcome is a scored answer set: every prompt run on every chosen engine, repeated, each answer scored the same way, rolled up into rates with honest intervals. AI answers change from run to run, so a single run per prompt is an anecdote, not a measure.

## Engines and tools

Confirm each id with `catalog_get` at run time. Prices are listed "from" prices observed 2026-11-05.

| Engine | Start with | Key inputs | From | Notes |
|---|---|---|---|---|
| ChatGPT | `cloro.ai-search.chatgpt.scrape` | `prompt`, `country` (both required); `include` `{markdown}` free; `searchQueries` adds 2 credits; `disableWebSearch` | $0.009 | Live web UI. Fallback `crawl4ai.ai-search.chatgpt.scrape` (`prompt`, `country`, `web_search`), $0.008, 30 s–2 min |
| Perplexity | `tap.ai-search.perplexity.answer` | `prompt`, `country` (default US) | $0.006 | Record `source_kind`: website answers are what buyers see; model-API answers are not |
| Gemini | `cloro.ai-search.gemini.scrape` | `prompt`, `country` | $0.006 | |
| Copilot | `cloro.ai-search.copilot.scrape` | `prompt`, `country` | $0.007 | |
| Google AI Mode | `crawl4ai.google.serp.ai_mode` | `q`, `deep:"0"` (required), `gl`, `hl`, `nocache:"1"` | $0.0003 | `answer.source` says AI Mode or AI Overview; `answered:false` is free. Richer sibling `cloro.google.serp.ai_mode` (`prompt`, `gl`), $0.006 |
| Google AI Overviews | `tap.google.serp.organic` with `ai_overview:true` | `q`, `country` | $0.0003 | Overviews trigger on keyword-style queries; use the short keyword form of the intent. `cloro.google.serp.organic` with `include.aioverview` (+2 credits) also returns PAA |
| Claude | `dataforseo.x.ai-optimization-claude-llm-responses-live` | `user_prompt` (≤500 chars), `model_name` (current name from DataForSEO's models list; bare aliases fail), `web_search:true` | $0.061 | API, not the consumer app; label it so. Costs ten times the others, so run it on category and comparison prompts only unless the user wants more |

Prefer the web-interface scrapers over model APIs. A 2026 preprint (arXiv 2610.15382) matched only about a quarter of the pages ChatGPT's app cited using OpenAI's API plus Google results, and vendor studies report brand overlap between API and app answers of roughly 6–12%. The DataForSEO `*-llm-responses-live` tools for ChatGPT and Gemini are API answers: a last resort, labelled.

## Repeats and budget

Repeats of the same prompt are correlated, so they add less information than new intents. The brand-level rate is precise to the extent the intents agree, not to the number of calls; treating 25 prompts × 20 repeats as 500 independent answers overstates precision several-fold.

- Default: 3 repeats per prompt per engine. That is enough to mark each grid cell always, sometimes or never, and to average within an intent. Beyond about 5, extra repeats barely narrow the headline, because the spread between intents dominates.
- Money prompts: when the user needs a per-prompt number for two or three key questions, run those 30+ times. At 30 runs a 50% rate carries a Wilson interval of about ±17 points; at 10 runs, about ±26. SparkToro, after 2,961 runs where the same brand list recurred under 1 in 100 times, recommends 60–100 runs for prompt-level claims.
- Budget sketch: 30 prompts × ChatGPT, Perplexity, Gemini, Copilot and AI Mode ≈ $0.03 per prompt per repeat, so about $2.60 at 3 repeats. Claude on 15 prompts × 3 repeats adds about $2.75. Show the user the arithmetic for their own set.

Each repeat must be a fresh answer. Tapinall serves identical calls from cache at a 75% discount, which returns the same answer again: pass `nocache:"1"` where the tool has it, otherwise vary a field that never reaches the engine (cloro's free `include` flags, DataForSEO's `tag`), and treat a discounted meter line or a byte-identical answer as one sample, not two. Spreading repeats across hours or days, when the run can wait, also samples the day-to-day drift a monthly figure is meant to represent.

## Scoring each answer

Score into the answers CSV defined in SKILL.md.

- Mentioned: the brand's name, a listed variant, or its domain appears in the answer text, read in context to rule out same-name entities. A brand page cited without the brand named is "cited, not named", recorded in `cited_urls` but not as a mention.
- Position: order of first appearance among brands named. SparkToro found the same list in the same order under 1 in 1,000 runs, so position is reported as first-named share and median position only, never as a headline or a change.
- Brands named: every brand in the answer, normalised to one spelling, including ones not in the profile; unknown recurring names are competitors the owner may not track.
- Sentiment, read from the sentence, not a sentiment model: `recommended` (picked for the buyer's need), `listed` (named neutrally), `caveated` (named with a drawback), `negative` (advised against). Classifier scores swing with the query language more than with the brand (arXiv 2607.13304), so they are not used.
- Accuracy: any wrong fact about the brand (price, features, location, status, ownership) goes in `accuracy_issue` with the correct fact and its source from `profile.md` or the brand's site.
- Citations: every cited URL in order, plus fan-out search queries when returned.

## Rates and intervals

Unbranded prompts only. For each engine, compute each intent's mention rate across its paraphrases and repeats; the engine rate is the mean over intents, with SE = standard deviation of the intent rates ÷ √(number of intents) and a 95% interval of rate ± 1.96 × SE, clipped to 0–100%. When every intent is 0 or every one is 100%, report "0 of k intents" or "k of k" instead of a zero-width interval. The all-engine rate averages each intent across engines first, then applies the same formula.

Share of voice: a brand's mentions ÷ all brand mentions across unbranded answers, per engine and overall.

## The no-search check

Run one repeat of the category and comparison prompts on ChatGPT with search off (`disableWebSearch:true`, or `web_search:false` on the crawl4ai tool). Graphite's study of 3,115 brand-question pairs (vendor) found brands ChatGPT rarely named without search stayed low even when they appeared on 15%+ of the cited pages. Read the two together:

- Named without search, missing with search: a retrieval gap; the cited pages lack the brand, so fix sources and content.
- Missing both ways while present on cited pages: a familiarity gap; it closes slowly through broad third-party mentions, so weight earned media in the fix plan.

## Market-wide cross-check (optional)

`dataforseo.x.ai-optimization-llm-mentions-multi-target-metrics-live` (~$0.26) compares 2–10 brands across DataForSEO's mention database; `platform` is `google` (default) or `chat_gpt` (US and English only). It is a rolling window whose identical calls return different aggregates, so use it as a second opinion on share of voice, never for change since last run; `...-llm-mentions-historical-live` gives a monthly series from 2025-08 for one target per call. These return HTTP 200 with errors inside: check `tasks[].status_code`.

## Change since last run

Compare only prompts, engines, country and tools present in both runs. A change is real when |Δ| > 1.96 × √(SE₁² + SE₂²); otherwise write "within noise". When every tracked brand moved the same way, or the engine's model or citation behaviour changed (logged-out ChatGPT answers carrying citations rose from 57% to 89% over eight weeks in 2026, per Graphite), attribute the move to the engine first.

## Report tables

- Results per engine: `| engine | tool id | answers | mention rate (95% CI) | intents with ≥1 mention | first-named share | recommended share | caveated or negative | accuracy issues |`
- Per-prompt grid: `| prompt id | stage | <one column per engine> |`, cells `k/n`; validation prompts in a separate block showing sentiment.
- Competitor share of voice: `| brand | answers naming it | mention rate | share of voice | first-named share | engines |`
- Accuracy and sentiment issues: `| prompt id | engine | what the answer says | correct fact | source | cited URL it likely came from |`
- Change since last run: `| metric | engine | last run | this run | Δ | beyond noise? |`
