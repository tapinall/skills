# Local SEO

The outcome is the `## Local` section: where the business stands in the local pack and Maps for its main service queries, against which competitors, and the actions the owner can take in their Google Business Profile, reviews and site. The catalog cannot read or edit a Business Profile, so every action is one the owner carries out.

## How Google ranks local results

Google's Business Profile help says local results are "mainly based on relevance, distance, and popularity", where prominence draws on links to the business and on reviews: "More reviews and positive ratings can help your business's local ranking", and "There's no way to request or pay for a better local ranking." Whitespark's 2026 Local Search Ranking Factors survey of local SEO practitioners puts the primary Business Profile category at the top, with proximity to the searcher and reviews close behind; the percentage weights quoted online for it disagree, so use the order, not the numbers.

## Tools (confirm with `catalog_get`)

- `tap.google.serp.local` and `tap.google.serp.maps` (`q`, `country`, `language`) take no location parameter. Put the town in the query ("emergency plumber leeds") to see the pack for that area.
- Distance changes the pack street by street. To see it from a point, as a searcher near the shop would, use `dataforseo.x.serp-google-local-finder-live-advanced` with `keyword`, `location_coordinate` ("lat,lng,zoom") and `language_code`; it rejects `location_name`. Two or three points across the service area show how far the business's visibility reaches.
- `tap.google.maps.reviews` (`place_id`, `limit`, `sort: "newest"`) needs the `place_id` from a Maps or local result.
- `tap.google.serp.organic` for the same queries, because local organic results sit under the pack and often hold directories the business can join.

## What to compare

For the business and the three to five pack competitors per query: primary and secondary categories, review count, average rating, how recent the reviews are, whether the owner replies, the services and words customers use in the review text, and whether the business name, website and phone match across listings. Review text is evidence of relevance, and it supplies the customer language for service pages.

## Actions within the rules

- Categories and services: match the primary category used by the pack leaders when it describes the business truthfully.
- Reviews: ask every customer, reply to reviews, mention the service in replies where natural. Google's contribution policy prohibits offering incentives for reviews and selectively soliciting positive ones, so plan a steady ask, not a filtered one.
- Business name: keywords in the name are a known ranking factor, and practitioners see competitors use them, but Google's Business Profile guidelines forbid service, product or location words that are not part of the real-world name and warn of suspension. Recommend the real name only.
- Location pages: one per real location or genuine service area with local proof (jobs done there, staff, photos, local reviews). Google's spam policies list "pages targeted at specific regions or cities that funnel users to one page" and "substantially similar pages" as doorway abuse.
- Links and citations: local directories, chambers, suppliers and local press from the backlink gap in `competitor-gap.md`.

Done when each main service query has a dated pack snapshot with the business's position (or absence), the competitor comparison, and actions the owner can take.
