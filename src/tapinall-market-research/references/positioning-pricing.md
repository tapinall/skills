# Positioning and pricing

The outcome is the `## Positioning and pricing` table: what each competitor claims, to whom, with what proof, and what it charges, all verbatim from fetched pages with URL and date. Downstream skills quote these claims and prices, so a paraphrase or a remembered price becomes a false statement in someone's outreach.

## Pages to fetch

Locate them first with `tap.web.map` (`url`, `q` such as "pricing", "vs", "alternative", "customers", `limit`), then read them with `tap.web.extract` (`url`):

- Home page: the headline and subhead are the positioning they chose.
- Pricing page.
- Comparison and alternative pages ("X vs Y", "Y alternative"): they show who the competitor thinks it is fighting and the differentiators it believes win. A comparison page aimed at the user's business is a direct statement of how it will be attacked.
- Customers or case studies: the segments they actually win, and their proof.
- The landing pages their long-running ads point to (from the ad-libraries branch): the message they pay to test.

## Messaging to capture

For each competitor record, verbatim where it is text:

- Headline and subhead.
- The category they claim ("all-in-one practice platform", "CRM for agencies").
- The customer they name.
- Their top three claims and the proof type behind each (numbers, logos, testimonials, awards, none).
- The primary call to action: "Book a demo" means sales-led and a higher price; "Start free" means product-led.

Read the set across rows before writing anything. Claims every competitor makes are table stakes and win nobody; a claim only one makes is a position. Then hold each claim against the voice-of-customer evidence: a promise the reviews contradict ("easy setup" against repeated onboarding complaints) is an attack angle, and the gap belongs in whitespace with both sources.

## Pricing

Extract plans with `tap.web.extract.structured` (`url`, plus a `schema` or `instruction`), asking for plan name, price, currency, billing period, annual discount, unit (per seat, per location, per usage), included limits, free tier or trial, and "contact sales" plans. Then normalise to one unit (monthly price per seat, per location or per order) so rows compare.

- A "contact sales" plan is data: record it as hidden, and look for the price in Reddit threads or reviews ("they quoted us").
- Pricing pages can change by visitor region and currency. Record the currency shown, and note that the extracting provider fetched from its own location.
- Price history: `tap.web.extract` on `https://web.archive.org/web/<YYYYMMDD>/<pricing-url>` shows an older version when the archive holds one. A recent price rise or a removed plan is a switching trigger; check whether reviews from after that date mention it.
- Local services rarely publish prices: use price mentions in Google Maps and Yelp reviews ("charged me", "quote") and say they are reported, not listed.
- Ecommerce: `tap.amazon.search.products` and `tap.amazon.product.detail` give the price band, rating and review count of each product; record the band the user's product would enter.

## Watching for change

When the user wants to hear about competitor price or plan changes later, offer `crawl4ai.watch.create`: free to create, it needs `url`, `agent` (the team label, which an error message names if wrong) and a plain-language `watch` condition such as "a plan gets more expensive or is removed"; checks draw on the team's watch budget (`crawl4ai.watch.budget.add`). Quote that budget before creating monitors.

The step is done when every core competitor has a row with headline, claims, CTA and price points or a stated reason they are missing, each with its URL and fetch date.
