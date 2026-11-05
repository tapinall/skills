# Verification, tiers and dedupe

The outcome is a list the user can mail without damaging their sending domain. Bounces and spam complaints are scored per sending domain by the mailbox providers, and a burned domain costs weeks to recover, so every address is tiered by what a verifier said and the `.md` states the bounce rate the user should expect.

## Statuses

Map each verifier's provider-native answer onto `email_status`: `valid`, `catch_all` (accept-all), `unknown`, `invalid`. Disposable addresses count as `invalid`; no address found is `not_found`.

## Tiers

- `valid` → `send`.
- `catch_all` → resolve before tiering. `filtrat.people.email.verify.resolve_catchall` (`email`, `resolve_catchall: true`; $0.0031) settles a catch-all address to deliverable or bounce: deliverable becomes `valid`, with "catch-all resolved" in `email_verifier`; bounce becomes `invalid`. Still unresolved → `test`. In Hunter's controlled test (vendor; 100 accept-all against 100 valid addresses, same campaign) accept-all bounced 27% and valid 1%. Vendor estimates of the share of B2B domains that accept all mail run from 23% to 67% depending on sample, so expect a large `test` tier and report its size.
- `unknown` → re-verify once with a different sibling verifier listed in `tap.people.email.verify`'s `catalog_get`, since greylisting and timeouts clear on retry. Still unknown → `hold`.
- `invalid` or `not_found` → `drop`.
- `role` addresses: `send` in the local branch when it is the business's published contact; `hold` in the B2B branch unless no named person exists at the account.
- Any row whose `compliance_flag` blocks cold email → `hold`, whatever its status.

## Bounce budget

Keep hard bounces under 2% of each send: Amazon SES documents 2% as the healthy ceiling, puts an account under review at 5%, and may pause sending at 10%.

Mixing `test` into a send breaks that budget fast. With valid rows bouncing about 1% and unresolved catch-alls about 27%, unresolved catch-alls must stay under about 4% of a batch to keep the batch under 2%. So `test` rows go out as a separate small batch the user watches, never mixed in. Write the arithmetic in the `.md`: expected bounces for `send` alone, and for `send` plus `test`.

Complaints weigh more than bounces at Gmail and Yahoo, and fit is what drives them. Off-criteria rows are the likeliest to be marked as spam, which is another reason to drop rather than pad.

## Mailbox-provider rules the sending setup must meet

The leads skill sends nothing, but the `.md` lists these so the user can check their setup before mailing:

- Google, all senders: SPF or DKIM; spam rate in Postmaster Tools below 0.3%, with Google advising below 0.1%. Above 5,000 messages a day to Gmail: SPF and DKIM, DMARC (`p=none` is enough), From domain aligned with SPF or DKIM, one-click unsubscribe plus a visible unsubscribe link on marketing mail. Google lists buying addresses as a practice to avoid and advises unsubscribing recipients after repeated bounces. Google can treat lower-volume senders as bulk, so meeting the bulk rules at cold-email volumes is the safe default.
- Yahoo: the same tiers and 0.3% spam ceiling; bulk senders honour unsubscribes within two days.
- Microsoft, Outlook.com, Hotmail and Live, since 5 May 2025: domains sending over 5,000 a day must pass SPF and DKIM and publish DMARC (`p=none` or stricter) aligned with the From domain; failing mail is rejected with `550 5.7.515`.

These rules govern consumer mailboxes. Company mail hosted on Google Workspace or Microsoft 365 is filtered by its own tenant settings, but local-business lists are full of gmail.com, outlook.com and yahoo.com addresses, so the rules apply to them directly.

## Dedupe

Match keys in this order: email (lowercased); `linkedin_url` (lowercased, query string and trailing slash removed); first name + last name + domain; for companies, root domain without `www`; in the local branch, `place_id`, then phone digits.

- Match the dedupe set before buying emails, on person and company keys, so nothing already held is paid for twice.
- Remove anyone on a do-not-contact, unsubscribe or bounce list outright; the UK ICO recommends screening every new B2B list against a do-not-email list.
- Rows already in an earlier `tap-suites/outreach/*.csv` are dropped unless the user asks to re-contact them.
- Record in the `.md` which files were matched and how many rows each removed.

## Freshness

A verification result is a snapshot: people change jobs and domains change mail settings. Set the re-verify-by date in the `.md` and re-run `tap.people.email.verify` on rows whose `verified_at` is more than a few weeks older than the planned send.
