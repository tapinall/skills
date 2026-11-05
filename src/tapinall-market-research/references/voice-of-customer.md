# Voice of customer

The outcome is the `## Voice of customer` section: themes coded from real reviews and threads, each with its frequency and verbatim quotes, plus a list of the phrases customers use. Outreach, seo and social build hooks, keywords and objections straight from this section, so the quotes must be exact and the frequencies honest.

## Sources by business type

Confirm each tool with `catalog_get`; prices are about $0.0003–0.005 a call.

| Business | Tools | Notes |
|---|---|---|
| B2B, SaaS, online services | `crawl4ai.trustpilot.business.reviews` (`domain` as Trustpilot names it, `stars`, `page` of 20); `crawl4ai.reddit.search.posts` then `crawl4ai.reddit.post.comments` (`url`, `limit`, `sort`) | G2 and Capterra are not in the catalog; list them under Not collected rather than filling the gap from memory |
| Local | `tap.google.maps.reviews` (`place_id`, `limit` defaults to 5, so set it; `sort`); `crawl4ai.yelp.business.reviews` (`business` alias; Yelp shows only about 10 recommended reviews); `litescrape.tripadvisor.business.reviews` | Get place ids from `tap.google.serp.maps` |
| Apps | `litescrape.app_store.reviews` (`product_id` numeric, `country`, `sort` mostrecent or mosthelpful, `page`); `litescrape.google_play.reviews` (`product_id` package, `rating` filter, `num` up to 199, `sort_by`) | Play rows include developer replies, which show how the competitor handles complaints |
| Ecommerce | `crawl4ai.amazon.product.reviews` (`product` ASIN, `limit` up to 100; past the 8–13 top reviews it is slower and billed per review); TikTok Shop review tools via search | Note the variant bought |
| Employee view | `crawl4ai.glassdoor.company.reviews` | Not customer voice; staff complaints about support cuts or churn often predict customer pain, so file them under signals |

Reddit search without the `session` cookie returns no score or comment count. To rank threads by engagement, ask the user for the cookie or use `scrapecreators.reddit.search.posts`, checking its fields first.

## Sample by star band, not by average

Online ratings are a poor summary. Schoenmueller, Netzer and Stahl (JMR 2020, over 280 million reviews on 25 platforms) found most platforms heavily polarised because people with extreme views are the ones who review, and that polarity weakens the link between average rating and what buyers do. Hu, Pavlou and Zhang showed the same self-selection makes the usual distribution J-shaped. So:

- Do not rank competitors by star average or compare averages across platforms.
- Read each band for what it holds: 1–2 stars for pains and switching triggers, 3 stars for trade-offs (Mudambi and Schuff, MISQ 2010, found moderate reviews more helpful than extreme ones for experience goods, though later studies disagree), 4–5 stars for desired outcomes and the words customers use for value.
- On Trustpilot, invited reviews run higher than organic ones (non-peer-reviewed analyses put the gap near one star), so record the verified or invited flag and treat ratings of companies with different invitation habits as incomparable.
- Use the last 12–24 months unless the user asks for history, because products and prices change; state the window.

## How many to read

Stop on saturation, not a fixed count. Adapting Guest, Namey and Chen (PLOS ONE 2020): code a base batch (about 40 reviews across bands and competitors), then read in runs of 20; stop when a run adds 5% or fewer new themes relative to the base. Report it in the method line as base plus run ("40+20, 3% new"). A theme found in one review is an anecdote; say so.

## Coding

Code each review or comment with the jobs-to-be-done forces of progress (Moesta and Spiek): a switch happens only when push and pull outweigh anxiety and habit.

- Push: what about the old way forced a change ("our last tool kept double-booking").
- Pull: what drew them to the new option.
- Anxiety: what worried them about switching. These become the objections outreach must answer.
- Habit: what kept them on the old way, usually the status quo.
- Desired outcome: the result they hired the product for, often after "so I can" or "now we".
- Switching trigger: the event that started the search (price rise, acquisition, outage, team growth, contract renewal, new regulation). Triggers tell leads and outreach when to reach out.

Count frequency as n of N reviews read, per competitor.

## Quotes

- Quote exactly, trimming only with an ellipsis, with platform, date, rating and link. Downstream skills reuse customers' words as hooks, and a polished paraphrase loses the very wording that makes them work.
- Leave reviewer names out; the link is the citation, and names are personal data nobody downstream needs.
- Discount likely fakes, which persist despite the FTC's 2024 ban on fake and incentivised reviews (16 CFR 465): bursts of same-day reviews, one-review accounts with generic praise, and Reddit "recommendations" from accounts that only post about one vendor.

The step is done when every core competitor with public reviews has been read to saturation or exhaustion, each theme carries type, frequency and at least one linked quote, and unreachable sources are listed under Not collected.
