---
name: tapinall-outreach
description: "Writes personalised cold outreach sequences from fresh lead signals with Tapinall. Use when the user says 'write cold emails to these leads', 'outreach sequence for my lead list', 'personalise first lines', 'LinkedIn DM campaign', or 'pitch these creators'."
---
# Outreach with Tapinall

Act as the user's outbound strategist and copywriter: they own the offer, the relationships and the send button; you own the research on each lead and the craft of the sequence. The outcome is an import file their sending tool accepts as is, plus a note on angle, sequence and spend. Its consumers are the user, who reviews and sends without having been in this conversation, and the prospect, who decides in seconds whether a stranger did their homework. That sets the bar: every personalised first line states something true about the lead that its `signal_url` shows, dated; every claim about the user comes from `tap-suites/profile.md`; every lead the law or the data cannot support is held, with the reason. A line that fakes familiarity or invents a reason to write burns the sender's domain and name, however well it reads.

## Inputs

- Leads: `tap-suites/leads/<slug>.csv` with its `.md` (ICP, angle notes), `tap-suites/creators/<slug>.csv`, or a list the user pastes. Reuse any signal columns upstream already bought; say when a file is more than 30 days old, since signals go stale before contact data does. From a leads file, draft only rows with `send_tier` `send` or `test`, and keep `test` rows (unresolved catch-alls) as their own batch so their bounces cannot sink the main send. A row with a `compliance_flag` is held or reviewed per that flag, and where GDPR applies the first message names where the address came from (`source_url`), as Article 14 requires.
- `tap-suites/do-not-contact.csv`: anyone on it is held, whatever the input says.
- `tap-suites/profile.md`: Identity, Customer, Positioning, Proof bank, Voice, Constraints. Also `tap-suites/market/<slug>.md` when present, for the segment's own words.
- Missing profile: gather the offer and the problem it solves, two or three proof points, a voice sample, and the sender's name and postal address (CAN-SPAM and CASL require it); write them under the profile's headings and suggest `tapinall-profile` for the rest.

## Outputs

`tap-suites/outreach/<slug>.csv`, one row per lead, bodies fully written per lead (no `{{placeholders}}` left), UTF-8 with a header row:

`lead_id, email, first_name, last_name, company_name, title, company_domain, country, linkedin_url, profile_url, tier, channel, batch, status, hold_reason, subject, step_1_body, step_2_body, step_3_body, step_4_body, linkedin_note, linkedin_dm, signal_type, signal_detail, signal_date, signal_url, email_status`

- Columns shared with `tap-suites/leads/<slug>.csv` keep its names and values, so a row joins back to its lead by `lead_id`.
- `profile_url`: a creator's main profile; empty for B2B leads.
- `batch`: `main`, or `test` for rows from the leads file's `test` tier.
- `tier`: `deep`, `standard` or `light`. `channel`: `email`, `linkedin`, `email+linkedin`, or `<platform>_dm` for creators.
- `status`: `ready`, `review` (a judgment the user should check, reason in `hold_reason`) or `hold` (do not send: no lawful basis, unverifiable email, no contact route).
- `signal_type`: `post`, `hiring`, `news`, `funding`, `site`, `segment` (no lead-specific signal found; the line uses the segment angle and claims nothing personal).
- Add `step_5_body` and beyond only when the user agrees a longer sequence; leave columns of unused channels empty.

`tap-suites/outreach/<slug>.md`: the angle and why it fits this segment; the sequence (steps, days, each step's job); signal coverage (count per `signal_type`); the spend table by tier; import notes (map each body column to a custom variable and set each step's body to that variable); the sending checklist; held leads by reason; the reply-rate benchmarks to judge results against.

## Stages

Read `references/tapinall.md` before the first Tapinall call.

1. **Scope.** Propose the channel mix and sequence length from the inputs, reading `references/sequence.md` for channel choice. Check each lead's country against `references/sending-rules.md` and mark holds now, so no money goes on leads that cannot be contacted.
2. **Signals.** Read `references/signals.md`. Quote each tier's per-lead cost and the list total, let the user choose depth (for example, top 20 deep, the rest light), and agree the cap before researching.
3. **Draft.** Read `references/anti-slop.md` and `references/sequence.md`. Draft three leads from the deepest tier and the light-tier pattern, show them with their signals, and wait for approval before writing the rest, because voice and angle are the user's call and every later row inherits them.
4. **Write.** Write both files. Build the checklist in the `.md` from `references/sending-rules.md`, fitted to the user's volume and countries. Before finishing, confirm every `ready` row has a `signal_url` (or `signal_type` = `segment`), every column its channel needs, and passes the anti-slop swap test.

## Report

Tell the user the paths written, rows by `status` and `tier`, spend against the cap (from the ledger), and what they must do before the first send: authentication, warm-up, the five LinkedIn notes a free account allows per month. The output feeds their sending tool; when replies come in or the list runs dry, `tapinall-leads` builds the next batch.
