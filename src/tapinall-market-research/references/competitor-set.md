# Competitor set

The outcome is the `## Competitor set` table: 5–8 core competitors confirmed by evidence, typed as direct, substitute or status quo, each with the identifiers every later branch needs. Every later call is bought per competitor, so a wrong or bloated set wastes the whole run.

## What counts as a competitor

Start from the buyer, not the category. April Dunford's test for competitive alternatives is what the best customers would do if this business did not exist. That answer has three kinds, and the file types each row by them:

- Direct: same job, same kind of solution, same buyer (two scheduling apps for clinics).
- Substitute: same job, different kind of solution (an agency instead of software, a freelancer instead of an agency, a marketplace instead of a direct shop).
- Status quo: doing it in-house, a spreadsheet, or doing nothing. It is often the alternative a business loses to most, and it has no domain to research, so its evidence comes from reviews and Reddit ("we just use Excel").

Positioning against the status quo is a different message from positioning against a rival, so keep substitutes and status quo in the table even when they get no deep research.

## Sources, and what each one really finds

Triangulate, because each source has a known bias:

| Source | Tool (confirm with `catalog_get`) | What it returns | Bias |
|---|---|---|---|
| Profile list | `tap-suites/profile.md` | The owner's view | Misses new entrants and substitutes |
| Lookalikes | `tap.companies.similar` (`domain`) | Firmographic look-alikes | Similar is not competing: partners and same-size firms in other niches appear |
| Organic overlap | `spyfu.google.domain.competitors` (`domain`, `pageSize` is the cost dial, default 5); `serpstat.google.domain.competitors` (`params.size`) | Domains sharing ranking keywords | Publishers, review sites and marketplaces crowd in; keep them for seo, not as competitors |
| Paid overlap | `spyfu.google.domain.ppc_competitors` | Domains bidding on the same keywords | The strongest single signal: they pay for the same buyers |
| Keyword SERPs | `tap.google.serp.organic` (`q`, `country`, `limit`) | Who ranks for "best <category>", "<competitor> alternatives", "<category> for <segment>" | Listicles name who the market thinks of |
| Seed-keyword overlap | `dataforseo.x.dataforseo-labs-google-serp-competitors-live` (`keywords`, `location_code`, `limit`) | Domains ranking across up to 200 keywords | Use when the user has no domain yet |
| Local | `tap.google.serp.maps` (`q` with the city, `country`) | Places with rating, review count, place id | Proximity drives ranking, so search from the customer's area |
| Apps | `crawl4ai.app-store.search.apps`, `litescrape.google_play.search.apps` | Apps with rating counts and ids | Store search favours big apps |
| Marketplaces | `tap.amazon.search.products` | Products with price, rating, ASIN | Brands, resellers and private label mixed |
| Buyer talk | `crawl4ai.reddit.search.posts` ("<competitor> alternative", "switched from <competitor>", "<category> recommendation") | Who buyers compare and leave | Small samples |

## Confirming the set

- A candidate becomes core when two independent sources point to it, or when customers name it in reviews or threads. A lookalike-only or SERP-only hit stays a candidate.
- Prefer the competitors the target customer meets: same segment, geography and price band. A global leader the customer never considers adds cost and little insight.
- When a new business has no domain, seed from category keywords and the owner's description instead of `similar`.
- Record why each row is in the set in the overlap evidence column (for example "PPC overlap 140 keywords; named in 6 Reddit threads"), so a later reader can judge it.

## Identifiers to collect now

Later branches need ids, not names, and several tools refuse a name. Fill the identifiers column as you go:

- Domain as Trustpilot lists it, often with `www.` (the Trustpilot tool expects that form).
- Yelp alias (the part after `/biz/`) and Google Maps `place_id` from `tap.google.serp.maps`.
- App Store numeric id and Google Play package name.
- ASINs of the main products.
- Facebook page id: from the `page_id` field of a `meta-ad-library.meta-ads.library.search` keyword hit, or `scrapecreators.x.v1-facebook-adlibrary-search-companies`.
- LinkedIn company URL and the social handles the creators and social skills will need.

The step is done when every core row has a type, overlap evidence with a source, and the identifiers its business type needs, and the user has confirmed or edited the set.
