# Sources

For maintainers refreshing `references/`. The skill does not load this file. Researched 2026-11-05. Cold email figures are vendor data from each vendor's own platform or clients; methods are thinly documented and the numbers disagree, so the references use them as ranges.

## Cold email datasets (vendor)
- Instantly, Cold Email Benchmark Report 2026 (2025 data: 3.43% average reply, top 10% 10.7%, step 1 = 58% of replies, 4–7 touches 3–4 days apart, under 80 words, warm-up 5–10/day over 4–6 weeks, bounces under 2%) — https://instantly.ai/cold-email-benchmark-report-2026
- Belkins, Sales follow-up statistics 2025 (7.53M emails, 112,005 LinkedIn sequences, 46k calls; steps 2–6 = 58.6% of replies; step 3 = 35.6% of meetings; LinkedIn note vs no note; channel connect rates) — https://belkins.io/blog/sales-follow-up-statistics
- Belkins, B2B cold email subject line statistics (5.5M emails, 2024; 2–4 words best; personalised subjects 7% vs 3% reply) — https://belkins.io/blog/b2b-cold-email-subject-line-statistics.md
- Gong Labs, interest CTA study (304,174 emails, 2020; success = meeting within 10 days) — https://www.gong.io/blog/this-surprising-cold-email-cta-will-help-you-book-a-lot-more-meetings
- Gong, Do execs really reply to cold email (2026; execs 30.2% less likely to reply; 50–100 words; offers beat meeting requests; 1–4 word subjects) — https://www.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says
- Hunter, Cold email word count (34M emails, 2022–24; bands 3.4–4.5%) — https://hunter.io/blog/cold-email-word-count
- Hunter, State of Cold Email 2025 (11M emails; 4.1% average; ≤50 recipients 5.8% vs 1,000+ 2.1%) — https://hunter.io/the-state-of-cold-email-2025

Dropped: Lavender reading-level and length figures (no primary source found), Belkins "4+ emails triple complaints" (not found in the primary page), signal-based "15–25% reply" claims (untraceable), Woodpecker personalisation 18% vs 9% (summary page only).

## LinkedIn
- LinkedIn Help, Invitation limit reached (free and Basic: notes on five requests a month; Premium unlimited) — https://www.linkedin.com/help/billing/answer/a550555
- LinkedIn Help, Personalize invitations — https://www.linkedin.com/help/linkedin/answer/46662
- LinkedIn User Agreement, §8.2 (no bots or automation) — https://www.linkedin.com/legal/user-agreement
- Vendor reports of ~100 invites a week and 200/300-character notes: lemlist — https://help.lemlist.com/en/articles/8514157 ; Hublead — https://www.hublead.io/linkedin-character-limit

## Deliverability
- Google, Email sender guidelines — https://support.google.com/a/answer/81126
- Microsoft, Outlook requirements for high-volume senders — https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730
- Yahoo, Sender best practices — https://senders.yahooinc.com/best-practices/
- Spam Resource, Microsoft joins the club — https://www.spamresource.com/2025/04/microsoft-joins-club-top-four-b2c-mbps.html

## Compliance
- FTC, CAN-SPAM compliance guide — https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- FTC civil penalty adjustments 2025 ($53,088) — https://www.federalregister.gov/documents/2025/01/17/2025-01361/adjustments-to-civil-penalty-amounts ; no 2026 adjustment — https://public-inspection.federalregister.gov/2026-18853.pdf
- ICO, Business-to-business marketing — https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/
- ICO, Marketing FAQs for small organisations — https://ico.org.uk/for-organisations/advice-for-small-organisations/frequently-asked-questions/marketing/
- UK GDPR Article 14 (data not obtained from the subject) — https://www.legislation.gov.uk/eur/2016/679/article/14
- Germany UWG §7 and France CNIL B2B rules (secondary summaries; check primary text when refreshing) — https://overloop.com/blog/b2b-cold-email-germany-gdpr-compliance ; https://www.ediware.eu/b2b-email-marketing/b2b-cold-emailing-legal-framework/
- CASL s.10(9) implied consent — https://laws-lois.justice.gc.ca/eng/acts/E-1.6/section-10.html ; s.11 unsubscribe — https://laws-lois.justice.gc.ca/eng/acts/E-1.6/section-11.html

## Catalog (confirmed with catalog_get, 2026-11-05)
`tap.linkedin.user.posts`, `tap.linkedin.user.profile`, `tap.x.user.posts`, `tap.companies.news`, `tap.companies.jobs.search`, `tap.companies.enrich`, `tap.web.extract`, `tap.web.extract.structured`, `tap.web.map`, `tap.web.search.news`, `tap.people.email.verify`. Found by search: `tap.instagram.user.posts`, `tap.x.user.profile`, LinkedIn company-post tools, `aviato.companies.funding_rounds`, `getleadsio.companies.funding.feed`. No DNS or authentication-check tool exists in the catalog.
