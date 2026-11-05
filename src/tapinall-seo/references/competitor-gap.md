# Competitor gap

The outcome is two sets of rows with sources: keywords competitors rank for that the user does not (or ranks for weakly), and sites that link to competitors but not to the user, each judged on whether the user could earn it.

## Search competitors are not always business competitors

The domains that take the clicks are often publishers, marketplaces, directories and forums, not the rivals in the market file. Build the list from both: the market file's competitors, the domain-competitor tools run on the user's domain, and the domains that recur across the SERPs already fetched. Drop giants the user cannot displace (Wikipedia, Amazon, Reddit) from the gap analysis, but note where they hold the top spots, because that lowers winnability.

## Tools (confirm parameters with `catalog_get`; they differ by provider)

Domain competitors:
- `spyfu.google.domain.competitors`: `domain`, `countryCode`, `pageSize` (cost dial, default 5, max 550), about $0.0005 per row.
- `serpstat.google.domain.competitors`: `method: "SerpstatDomainProcedure.getOrganicCompetitorsPage"` (the `getCompetitors` spelling is deprecated), `params.domain`, `params.se` (e.g. `g_us`), `params.size` (1–100, default 20), `id`.
- `dataforseo.x.dataforseo-labs-google-competitors-domain-live`: `target`, `location_code`, `language_code`, `exclude_top_domains: true`, `max_rank_group: 10` to count only top-10 overlap, `limit`.

Ranked keywords:
- `serpstat.google.domain.ranked_keywords`: `method: "SerpstatDomainProcedure.getDomainKeywords"`, `params.domain`, `params.se`, `params.size` (cost dial, default 100, max 1,000, about $0.0012 per keyword), `params.filters` such as `position_to: 20`, `params.sort`, `params.withIntents`. The cheapest at depth.
- `spyfu.google.domain.ranked_keywords`: `query`, `pageSize` (default 5, up to 10,000), `compareDomain` adds the second domain's rank to every row, which turns it into a gap report. About $0.0125 per row, ten times Serpstat, so 1,000 rows is about $12.50: quote it first.
- `dataforseo.google.domain.ranked_keywords`: `target`, `location_code` (2840 = US), `language_code`, `limit` (1–1,000), `order_by` as flat strings like `["keyword_data.keyword_info.search_volume,desc"]`; the nested filters shape fails.
- `dataforseo.x.dataforseo-labs-google-domain-intersection-live`: `target1`, `target2`, `intersections`. True gives shared keywords; false gives keywords where target1 ranks and target2 does not (check the parameter note at run time). With competitor as target1 and the user as target2, that is the gap.
- `semrush.google.domain.ranked_keywords` and `semrush.google.domain.competitors` show no price ("—"). Omitting `display_limit` (or sending 0) bills 10,000 lines, and a past `display_date` makes it a historical request at five times the units. Use Semrush only if the user accepts an unknown price, always with `display_limit` set and no past date.

## Keyword gap

Fetch competitors' keywords filtered to positions 1–20 and sorted by volume, then sort into:
- Missing: competitors rank and the user has no page.
- Weak: the user ranks 11–30, from Search Console or the tools' estimate.
- Shared but behind: both rank, the competitor higher.

Keep only keywords that fit the user's offers. Competitors' traffic figures are rough: in Ahrefs' study of 1,635 sites against Search Console the median error was about 50% for Ahrefs and 68% for Semrush (reported secondhand), so compare domains with one provider's numbers and never present a traffic estimate as fact.

## Backlink gap

- `tap.web.backlinks.summary` (`target`) for the user and the three or four main competitors: referring domains and the provider's authority score, which feed winnability.
- `dataforseo.x.backlinks-domain-intersection-live`: `targets` as `{"1":"comp1.com","2":"comp2.com"}` (up to 20), `exclude_targets: ["user.com"]`, `limit`. It returns domains linking to the competitors and not to the user. A domain linking to two or more competitors is the strongest prospect.
- `tap.web.backlinks.list` and `tap.web.anchors.list` (`target`, `limit` as price dial) on a competitor show what kind of link each is: directory, resource page, supplier or partner page, press mention, review, guest article, event. Anchors show whether the competitor's links are branded or keyword-rich.

Authority scores are each vendor's own model (Moz DA, Majestic Trust Flow, DataForSEO rank, Serpstat). They are not Google's and are not comparable across providers, so compare within one.

Recommend only links the user can earn: listings they qualify for, resources their content could deserve, partners and suppliers they already work with, press for something newsworthy. Google's link spam policy names buying or selling links, exchanging goods or services for links, and sending a product in exchange for a post with a link, so leave those prospects out of the plan rather than flag them as risky.

Done when each gap row names its source tool and date, and each backlink prospect carries its link type and the reason the user could earn it.
