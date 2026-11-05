# Citations and the fix plan

The outcome is the report's Sources cited table and a fix plan in which every action names the prompts it should win back, the URL or gap it works on, and what kind of effort it takes. Fixes come from this run's evidence; the research below tells you how to read that evidence, not what to recommend regardless of it.

## What the evidence says drives citation

Labels: peer-reviewed, preprint, platform documentation, vendor (a company that sells AI-visibility tools or services).

- Peer-reviewed, Aggarwal et al., "GEO", KDD 2024: on a 10,000-query benchmark, adding quotations from credible sources, adding statistics, and citing sources raised a page's visibility in generated answers by up to about 40%; on Perplexity, quotations gave about +22%. Keyword stuffing scored below the unedited page. Gains were largest for lower-ranked pages (cite sources: about +115% for rank-5 sources, −30% for rank-1), and the best method varied by domain (statistics for law, government and opinion; quotations for people, society and history; citations for factual queries).
- Preprint, Chen et al. 2025 (arXiv 2509.08919): AI engines cite earned media (independent publications, reviews, comparison sites) far more than Google does: for US software queries, 72.7% earned in GPT answers against 45.4% in Google, with brand-owned and social sources squeezed out. Niche brands face a "big brand bias".
- Vendor, Ahrefs, 26,283 ChatGPT source URLs: "best X" lists were 43.8% of cited pages on top-of-funnel prompts; 79% of cited lists had been updated that year and 35% sat on low-authority domains; brands placed higher on third-party lists were recommended more often.
- Vendor, Ahrefs, 75,000 brands: brand web mentions correlated 0.664 with Google AI Overview visibility, backlinks 0.218.
- Vendor, Ahrefs, 863,000 keywords (2026): only 38% of AI Overview citations rank in the top 10 for the same query; about a third rank outside the top 100, reached through fan-out queries. YouTube was 5.6% of citations.
- Vendor, Profound and others: the source mix differs by engine and moves. Wikipedia led ChatGPT's top cited domains while Reddit led Perplexity's and Google AI Overviews'; ChatGPT's Reddit share fell sharply in September 2025. Studies disagree on the numbers, so read this run's own source mix rather than assume one.
- Platform documentation, Google: AI Overviews and AI Mode need no special optimisation, files or schema; a page must be indexed and eligible for a snippet, and both features fan out into related searches.

## Sources cited table

Normalise every cited URL to its domain and label it with one type: `owned`, `competitor`, `listicle` (third-party "best X" or comparison page), `editorial` (news, reviews and guides by a publication), `review-directory` (Trustpilot, G2, Capterra, Clutch, Yelp, Tripadvisor, Google Business), `community` (Reddit, Quora, forums), `video`, `reference` (Wikipedia, Wikidata), `marketplace`, `other`.

For the most-cited URLs on prompts the brand lost (about 15–25, by citation count), read the page with `tap.web.extract` and record whether the brand and each competitor appear on it. That check is what turns "competitors win" into a list of pages to work on.

`| url | domain | type | times cited | engines | prompt ids | brand on page | competitors on page |` (brand on page: yes, no, unreachable)

Add a one-line source-mix summary per engine: share of citations by type. It tells the owner where that engine looks, which is where effort pays.

## Fix plan

Rank actions by how many lost answers they touch across prompts and engines, and mark effort as quick (hours), project (weeks) or slow (months of earned coverage). Use the no-search check from `measurement.md`: retrieval gaps get source and content fixes first; familiarity gaps get earned-media work, and the owner should expect them to move slowly.

### Cited sources missing the brand

`| url | type | cited for (prompt ids, engines) | competitors listed | action | effort |`

Actions by source type:

- listicle: ask the author to consider the brand at the next update, with the facts that meet the list's own criteria and an offer to test the product. Lists are refreshed often, so there is a window. Any paid placement is labelled as sponsored by the publisher. tapinall-outreach can draft the asks.
- review-directory: claim and complete the profile with facts matching the site and `profile.md`; ask real customers for honest reviews. The FTC rule on reviews (in force since 21 October 2024) bans fake reviews, undisclosed insider reviews and incentives tied to positive sentiment, with civil penalties.
- community: answer threads where the product genuinely fits, from an account that states the affiliation, under each subreddit's self-promotion rules. A useful answer that names alternatives is what gets kept and cited; link drops get removed.
- reference: a Wikipedia article only when independent coverage already establishes notability. People with a conflict of interest propose edits on the article's talk page with `{{edit COI}}` rather than editing directly, and paid editors disclose employer and client under the Wikimedia Terms of Use. Factual errors are raised the same way.
- video: a demo or honest comparison video, or creator coverage through tapinall-creators.
- competitor: cannot be fixed on that page; answer the same question on an owned page, which becomes a content gap below.
- editorial: pitch data or expertise journalists can cite; original statistics are what the GEO results reward.

### Content gaps for tapinall-seo

`| gap id | intent and prompt ids | stage | what the answers cite instead | owned page (url or none) | change needed | evidence |`

Three kinds, in priority order: intents where competitors are named and the brand is not and no owned page answers (create one, for example a comparison or "best for <segment>" page); owned pages that exist but are not cited (add sourced statistics, quotations and citations, an answer-first opening, a visible updated date, and a fair comparison); and fan-out queries ChatGPT ran (from `searchQueries`) that no owned page ranks for. Write the evidence so tapinall-seo can act without this conversation: prompt ids, the cited URLs it is up against, and the answers' wording.

### Listings and communities

`| place | type | url | competitors present | brand present | how to earn a presence |`

Directories, publications, subreddits and forums where competitors appear in cited sources and the brand does not.

### Accuracy fixes

For each wrong fact, name the cited page that most likely carries it, correct the owned page first, then request corrections on third-party pages, and keep the same facts across every profile.

## Out of bounds

Every action earns a presence a reader would also value. Hidden text or instructions aimed at AI crawlers, fake or incentivised-for-praise reviews, sock-puppet or undisclosed community accounts, vote buying, undisclosed paid placements, mass-generated pages and keyword stuffing break platform rules or consumer-protection law, and get the brand's sources discounted once found. A user who asks for one gets the reason and the legitimate alternative.
