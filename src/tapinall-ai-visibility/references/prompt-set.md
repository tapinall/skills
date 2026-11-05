# Building the prompt set

The outcome is a frozen, versioned list of 20–40 buyer questions, each traceable to where a real buyer asked it, spread across the funnel, written the way people type into a chat box. It is the ruler every later run measures with, so a bent ruler ruins every comparison after it.

## Where the questions come from

Mine what is already in `tap-suites/` first: sales and support questions in `profile.md`, review complaints and Reddit threads in `market/*.md`, ranking and question keywords in `seo/*.md`. Buy only what is missing:

- Reddit threads where buyers ask for recommendations: `crawl4ai.reddit.search.posts` (`query`, `subreddit`, `sort`, `t`, `limit` up to 250; ~$0.002). Queries like "recommend <category>", "<competitor> alternative", "<problem> help". Without a `session` cookie, score and comment counts come back null, so judge threads by their text.
- People Also Ask and related searches: `cloro.google.serp.organic` (`query`, `gl` required; ~$0.007). `tap.google.serp.organic` is cheaper but provider-native and may omit PAA.
- Review text: Trustpilot, Google Maps and app-store review tools (`catalog_search "<platform> reviews"`); the questions buyers wish they had asked before buying are prompt material.
- Optional weighting: `dataforseo.x.ai-optimization-ai-keyword-data-keywords-search-volume-live` returns an estimated AI-tool search volume for up to 1,000 keywords in one call (~$0.026). Use it to rank intents, not to write the prompts, because AI prompts are longer and more varied than keywords.

Record the source URL of each prompt. A prompt nobody can trace to a buyer is the author's guess.

## Stages and what each measures

Tag every prompt with one stage; the report breaks results down by it.

| Stage | Example shape | Measures |
|---|---|---|
| problem | "how do I stop <pain> in <context>" | whether the brand is suggested before the buyer knows the category |
| category | "best <category> for <segment/constraint>" | the core consideration-set number |
| comparison | "<competitor> alternatives", "<A> vs <B> for <use>" | head-to-head share |
| validation | "is <brand> worth it", "<brand> pricing", "<brand> reviews" | accuracy and sentiment, not mention rate |
| local or constrained | "<service> near <city> open weekends" | only when the profile says the business is local or regional |

Validation prompts name the brand, so they always mention it: report them separately and keep them out of the mention rate and share of voice, or the headline is inflated. Unbranded prompts never contain the brand's name, its domain, or a phrase only its marketing uses.

## Wording

Write prompts as a buyer would type them, with the constraint that makes them real ("for a 5-person agency", "under $50", "in Leeds"). In the SparkToro/Gumshoe study, 142 people describing the same need wrote prompts with an average semantic similarity of 0.081, so a single phrasing per need under-samples what buyers actually ask. Group prompts into intents: each intent gets two or three paraphrases, and the intent, not the individual prompt, is the unit the statistics cluster on (see `measurement.md`). Paraphrases shift AI-cited sources less than switching language does (overlap about 0.3–0.7 in Chen et al. 2025), so paraphrases add coverage without making the run incomparable.

Keep the language and country of the buyer. GPT swaps to almost entirely different cited sites between languages, so a set translated for a second market is a second panel, measured and reported on its own.

## Size

Aim for 10–15 unbranded intents × 2–3 paraphrases, about 20–40 prompts, weighted towards category and comparison, which decide whether the brand enters the consideration set. The number of intents, more than the number of repeats, sets how precise the headline rate is (see `measurement.md`), so when the budget is tight, cut repeats before cutting intents.

## Freezing and changing the set

The set is versioned in the report as `v<n>` with the date it was created. Prompt ids (`P01`…) and intent ids (`I01`…) are never reused or edited.

- Repeat run: copy the previous set verbatim. Wording changes, even a typo fix, change the answers.
- New buyer questions: append with new ids and an `added` date, bump the version, and keep them out of "change since last run" until they have two runs.
- A prompt that stopped mattering is marked `retired` with the date, never deleted, so old reports still resolve.

## Prompt set table in the report

`| id | intent | stage | prompt | source | added | status |`

Show the draft set to the user before measuring; they know which questions actually close deals, and every prompt they add or cut now is one that cannot drift later.
