# Tapinall catalog map

A starting point for matching a goal to tools, observed 2026-11-05. The catalog changes, so confirm any id with `catalog_get` before calling it, and use `catalog_search` for anything not listed.

| Family | What it does | Routed and best-value ids | Typical price |
|---|---|---|---|
| Company search | Account lists by description, industry, tech, country; lookalikes | `tap.companies.search` (`limit` sets the bill), `tap.companies.similar`; free counts via `catalog_search "companies search count"` | $0–0.15 per row |
| Company enrichment | Firmographics, headcount, domain ↔ LinkedIn | `tap.companies.enrich` (domain, name, linkedin_url or email) | $0.001–3 |
| Buying signals | Hiring, news, funding, tech stack, intent | `tap.companies.jobs.search`, `tap.companies.news`; tech-stack and funding tools via search | $0.02–0.30 |
| People search | People by title, company domain, keywords, location | `tap.people.search`; several free providers (apollo, dropleads, quickenrich) | $0–0.75 per row |
| Contact data | Work email, verification, phone, enrichment | `tap.people.email.find`, `tap.people.email.verify`, `tap.people.phone.find`, `tap.people.enrich`, `tap.people.identity.resolve` | from $0.001; reveals $1–5 |
| Social | Profiles, posts, comments, search on TikTok, Instagram, YouTube, X, LinkedIn, Facebook, Reddit, Threads | `tap.<platform>.<resource>.<action>` | $0.0005–0.025 |
| Transcripts, trends | Video transcripts, trending hashtags and topics | transcript and trending tools via search | $0.003–0.05 |
| Creators | Find creators, similar creators, contacts, audience overlap | influencersclub.creators.*, exa.creators.search | $0.02–1.50 |
| Search results, local | Google organic with AI Overview, Maps, local pack, reviews | `tap.google.serp.organic`, `tap.google.serp.maps`, `tap.google.serp.local`, `tap.google.maps.reviews` (needs `place_id`) | $0.0003–0.04 |
| Reviews | Yelp, Trustpilot, Glassdoor, Tripadvisor, app stores, Amazon | review tools via search | about $0.0003 |
| Keyword SEO | Ideas, volume, trends, ranked keywords, competitors | `tap.google.keywords.ideas`, `.volume`, `.trends`; domain tools from serpstat, spyfu, dataforseo | $0.001–0.38 |
| Backlinks | Summary, list, anchors, authority | `tap.web.backlinks.summary`, `.list`, `tap.web.anchors.list`, `tap.web.url.metrics` | $0.0004–0.06 |
| AI visibility | Answers from ChatGPT, Gemini, Perplexity, Copilot; LLM mention metrics | `tap.ai-search.perplexity.answer`, cloro.ai-search.*.scrape, dataforseo LLM-mention tools | $0.006–0.26 |
| Ad intelligence | Meta, TikTok, LinkedIn, Google ad libraries; paid keyword history | `tap.meta-ads.library.advertiser`; free meta-ad-library.* | free–0.04 |
| Web research | Search, news, page extraction, site maps, crawl | `tap.web.search`, `tap.web.search.news`, `tap.web.extract`, `tap.web.extract.structured`, `tap.web.map` | free–0.025; crawl to $0.50 per page |
| Page monitoring | Change alerts in plain English, e.g. competitor pricing | crawl4ai.watch.* | watch credits |
| Ecommerce, apps | Amazon, Shopify, Etsy, TikTok Shop; App Store, Google Play | `tap.amazon.search.products`, `tap.amazon.product.detail`, store and app tools via search | $0.0003–0.05 |
| Media generation | Image, video, voice, music | image-gen.*, video-gen.*, voice and music tools | image $0.03–5; video $1.40–66 |
| Markets | Stocks, crypto | `tap.stocks.quote.live`, `tap.stocks.eod.history` | low |

## What the catalog cannot do

No sending email or SMS, no posting or scheduling to social platforms, no CRM writes, no calendar, no Search Console or GA4, no G2 or Capterra reviews. Outputs leave the suite as files for the user's own tools.
