# Demand and intent

The outcome is a keyword set where every row carries a volume with its source, a trend, and an intent label read from a fetched SERP, grouped into clusters where the SERPs show one page can serve them.

## Seeds

Start from the profile's offers and the audience's words in the market file (comments, reviews, questions). Customers search in their words, not the industry's; a seed list of jargon finds demand nobody has.

## Tools (confirm each with `catalog_get` at run time)

- `tap.google.keywords.ideas` (`keyword`, `country`, `language`, `limit`): the routed id may answer through an autocomplete provider that returns phrases with no volume. Check which provider answered; for volume and CPC with the ideas, call `serpstat.google.keywords.ideas` or `seranking.google.keywords.ideas` directly. `limit` is the price dial.
- `tap.google.keywords.volume` (`keywords` list, `country`, `language`): some providers bill per keyword. `serpstat.google.keywords.volume` takes up to 1,000 keywords per call (`method: "SerpstatKeywordProcedure.getKeywordsInfo"`, `params.keywords`, `params.se: "g_us"`, `id`), about $0.0012 per keyword, and can attach `params.withIntents`. Treat provider intent labels as a hint only.
- `tap.google.keywords.trends` (`keywords`, `country`): a 0–100 relative index, not volume. Use it for seasonality and direction, and to time a page before its peak.
- `tap.google.serp.organic` (`q`, `ai_overview: true`, `country`, `language`, `limit`): the live SERP. For full features (People Also Ask, local pack, AI Overview text) use `cloro.google.serp.organic` (`query`, `gl`, `hl`, `include: {"aioverview": true}`, which adds credits) or `dataforseo.x.serp-google-organic-live-advanced` (`keyword`, `location_code`, `language_code`, `load_async_ai_overview: true`).

## Volume is an estimate

Third-party volumes are modelled, and the tools disagree. Ahrefs' own check found its volumes roughly right for about 60% of keywords against Search Console (vendor figure); Semrush's study that crowned Semrush most accurate is also a vendor's. Use volume to order keywords, not to forecast traffic, and name the provider in the table. A keyword reported at zero volume that matches what buyers say can still be worth a page; mark it "low volume, high fit" rather than dropping it.

## Intent comes from the SERP

Fetch the SERP for each candidate worth ranking and read what Google rewards:

- The dominant page type in the top 10: product or category pages, service pages, listicles and comparisons, how-to guides, tools or calculators, videos, forums (Reddit, Quora), local pack. That type is the intent and the format to build. A guide aimed at a SERP of product pages will not rank, however good.
- A mixed SERP means split intent. Say so, and build for the larger share or the share that serves the business.
- SERP features: AI Overview, featured snippet, People Also Ask (questions for the briefs), local pack, shopping, video, discussions and forums. Record them in the table.
- Date every snapshot. SERPs vary by country, device and day, so one snapshot is evidence, not truth.

A missing AI Overview is not proven absent unless the request asked for it: the routed tool needs `ai_overview: true`, and DataForSEO returns AI Overviews only from cache unless `load_async_ai_overview` is true. Write "AI Overview not checked" rather than "none".

## What an AI Overview does to the click

Value informational keywords with an AI Overview lower for traffic, and keep them for citation:

- Ahrefs (vendor, 300,000 keywords, December 2025 data): an AI Overview was associated with a 58% lower CTR for the top-ranking page, up from 34.5% in its April 2025 study.
- Pew Research Center (independent, 900 US adults, March 2025 browsing): users clicked a traditional result on 8% of visits with an AI summary against 15% without; 1% clicked a link inside the summary. Google disputes the method.
- Seer Interactive (agency, 53 brands, 5.47M queries, 2025): on informational queries, organic CTR was 2.07% when the brand was cited in the AI Overview, 0.94% when not, 3.35% with no AI Overview. AI Overviews appeared on 36% of informational, 8% of commercial and 5% of transactional queries in its data. Correlation only; stronger brands are also cited more.

So commercial and transactional keywords keep more of their clicks, and on informational ones the realistic prize is being cited. Pass those queries to `tapinall-ai-visibility`.

## Clusters

Group keywords whose fetched top-10s share URLs: three or four shared URLs is the common practitioner threshold for "one page can rank for both" (vendor and practitioner guides, no formal study), tightened for transactional SERPs, where fewer distinct pages show. Keywords grouped only by meaning, without fetched SERPs, are marked "unconfirmed cluster". One page per cluster also avoids two of the user's own pages competing for the same query.

Done when every keyword kept has a volume with its source and every cluster's primary keyword has a dated SERP with its intent and features recorded.
