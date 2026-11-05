# Sources

For maintainers refreshing `references/`. The skill does not load this file. Researched 2026-11-05. Catalog ids and prices observed with `catalog_get` on the same date.

## Mailbox-provider rules
- Google, Email sender guidelines — https://support.google.com/a/answer/81126
- Yahoo, Sender best practices — https://senders.yahooinc.com/best-practices/
- Microsoft, Fix NDR 550 5.7.515 in Outlook.com — https://support.microsoft.com/en-us/outlook/fix-ndr-error-550-5-7-515-in-outlook-com
- Microsoft, Postmaster policies — https://substrate.office.com/ip-domain-management-snds/Postmaster/Policies
- Secondary: Gmail enforcement ramp from November 2025 and lower-volume senders classed as bulk — https://www.suped.com/learn/email-deliverability/what-are-the-recent-changes-to-googles-bulk-sender-guidelines

## Bounce thresholds
- Amazon SES, Reputation metrics messages (5% review, 10% possible pause) — https://docs.aws.amazon.com/ses/latest/dg/reputationdashboardmessages.html
- Amazon Pinpoint, Bounce and complaint rates (below 2%; complaints below 0.1%) — https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-deliverability-dashboard-bounce-complaint.html (Pinpoint reached end of support 2026-10-30; SES thresholds unchanged)

## Catch-all addresses (vendor data)
- Hunter, Accept-all guide (27% vs 1% bounce test; 38% of domains) — https://hunter.io/blog/ultimate-guide-accept-all-catch-all/
- BounceZero, catch-all domains (22.8% of B2B domains) — https://bouncezero.io/blog/catch-all-domains-cold-email-strategy
- Kustiq, B2B catch-all benchmark (66.8%, SMB-skewed sample of 211) — https://kustiq.com/blog/b2b-catch-all-email-benchmark

## Reply-rate base rates and signals (vendor data)
- Belkins, Cold email response rates 2026 (7.5M emails, 0.45%, by seniority) — https://belkins.io/blog/cold-email-response-rates.md
- Autobound, Cold email guide 2026 (signal-based 15–25%) — https://www.autobound.ai/blog/cold-email-guide-2026
- Komo, Signal-triggered outreach — https://komo.ai/glossary/signal-triggered-outreach
- Vibe Prospecting, Signal-based prospecting 2026 (cites Instantly 3.43% average) — https://www.vibeprospecting.ai/blog/cold-email-dying-signal-based-prospecting-2026
- No independent controlled study of signal versus static lists was found.

## Local businesses
- BrightLocal, Local Consumer Review Survey 2026 (n=1,002 US) — https://www.brightlocal.com/research/local-consumer-review-survey/
- Clutch, Small business websites 2025 (17% without) — https://www.businesswire.com/news/home/20250821848152/en/Clutch-Report-No-Code-Tools-Fuel-Website-Growth-Yet-17-of-Small-Businesses-are-Still-Offline
- Review42, roundup of other estimates (27–29%) — https://resources.review42.com/what-percentage-of-small-businesses-have-a-website/

## Compliance
- GDPR Article 14 — https://gdpr-info.eu/art-14-gdpr/
- CNIL, La prospection commerciale par courrier électronique — https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique
- ICO, Business-to-business marketing — https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/ (blocked automated fetch; content via search snippets and secondary summaries)
- Germany UWG §7, secondary only — https://www.dealfront.com/guides/guide-to-cold-calling-and-emailing-europe ; https://overloop.com/blog/b2b-cold-email-germany-gdpr-compliance
- FTC, CAN-SPAM compliance guide — https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- CASL s.10(9) implied consent — https://laws-lois.justice.gc.ca/eng/acts/E-1.6/page-2.html
- CASL s.20(4) penalties — https://laws-lois.justice.gc.ca/eng/acts/E-1.6/page-3.html
