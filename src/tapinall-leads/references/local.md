# Local business lists

For freelancers and agencies selling to small businesses. The qualifying signal is a visible gap between the business's online presence and what the user sells, and it doubles as the opening line, so measure it rather than infer it. Tool ids were confirmed on 2026-11-05; `catalog_get` each before its first call.

## Choose the signal from the offer

| Offer | Qualifying signal | Measured from |
|---|---|---|
| Websites | No website; outdated site (no HTTPS, old copyright year, not mobile-ready, dated builder) | Listing `website` field; the site itself |
| Reviews, reputation | Rating under 4.0; under 20 reviews; newest review over three months old; owner never replies | Listing rating and count; recent reviews |
| Local SEO | Well rated but absent from the top results for `<category> <city>` | Position in Maps and local-pack results |
| Booking, ads, other | Whatever the offer fixes, stated as an observable fact | Site extraction or listing fields |

Default cut-offs come from BrightLocal's Local Consumer Review Survey 2026 (1,002 US adults): 68% only use businesses rated 4+ stars (55% a year earlier) and 31% need 4.5+; 47% will not use a business with fewer than 20 reviews; 74% look for reviews from the last three months; 54% visit the website after reading positive reviews; 89% expect owners to respond and 42% are unlikely to use a business that never replies. These figures are also what outreach can quote to explain why the gap costs the owner customers.

Base rate for "no website": Clutch's 2025 survey found about 17% of US small businesses without one (other 2025 surveys say 27–29%; definitions differ), so expect one qualifying row in four to six, varying by category and country.

## Chain

1. Places. `tap.google.serp.maps` with `q` as `<category> in <city>`, plus `country` and `language`. It takes no location field, so the place goes in `q`, and one call returns one results page; cover a wider area with one query per town or district. Listed from $0.0003 per call. For wide areas or a "no website" offer, `apify.google.serp.maps` is often cheaper per qualified row: `searchStringsArray`, `locationQuery`, `website` (`withoutWebsite` | `withWebsite`), `placeMinimumStars`, `maxCrawledPlaces`, `geo_split` for areas past one city, `scrapeContacts` (site emails included); $0.0225 per result, and places removed by its filters are not charged. On the router's key it requires `maxTotalChargeUsd` (above 0, at most 1), `memory` 1024 and `timeout` 90. `tap.google.serp.local` gives local-pack position for the SEO signal ($0.005).
2. Qualify on listing fields first, since they arrive with the search: rating, review count, website presence, permanently closed. Keep `place_id` on every row; it is the key for reviews and dedupe.
3. Reviews, only for rows still in play. `tap.google.maps.reviews` with `place_id`, `limit` 10 and `sort` `newest` ($0.0003) shows the newest review date and whether the owner replies.
4. Website. `tap.web.extract.structured` with `url` and a fixed `schema`, for example `{owner_name, emails[], phones[], copyright_year, uses_https, booking_link, social_links[]}`, at $0.025 per page. Start at the homepage and try the contact or about page only when the homepage yields no contact. `tomba.companies.tech_stack` ($0.022) names the builder or CMS when "outdated site" is the signal.
5. Email. With an owner name and domain, `tap.people.email.find` (`first_name`, `last_name`, `domain`). Addresses published on the site or listing go straight to `tap.people.email.verify`. A published `info@` or `hello@` is often the only route into a small business; mark it `email_type` `role`. Then tier every address with `references/verification.md`.

## Writing the rows

`signal_detail` is a fact the owner would recognise, with numbers and dates: "4.1★ from 12 reviews, newest 2026-03-02", "No website on the Google listing", "Footer © 2017, no HTTPS". `signal_url` is the Maps URL or the page that shows it. Put the business phone from the listing in `phone` with `phone_type` `business`.

## Small-business compliance traps

These change what can be sent, so set `compliance_flag` from `references/compliance.md`:

- Many local businesses are sole traders or partnerships. In the UK those count as individuals, so cold email needs consent; a limited company (Ltd, LLP, PLC in the name, footer or Companies House) does not. When the legal form is unclear, flag it rather than guess.
- Businesses without a website often publish a gmail.com or outlook.com address. Mark it `personal`: it loses the B2B footing in some jurisdictions, and it lands under the consumer mailbox providers' bulk-sender rules directly.
- Generic addresses of a company (`contact@`, `info@`) are not personal data in the CNIL's reading, which makes them the safer route in France.
