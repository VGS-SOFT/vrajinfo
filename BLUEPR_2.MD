# Blueprint — Tranche 2: Service Pillar Pages

*Phase 2 blueprint · vrajvithalani.com · Tranche 2 of 7 · Covers the 4 service pillar pages — the money pages. Each ranks for high-intent commercial keywords AND collects link equity from cluster content (Tranches 3/6/7) and location pages (Tranche 4) beneath it. Word count: 2,500–3,500 each. Combines direct pitch + authoritative resource content, weighted ~60% pitch / ~40% resource (opposite balance to Learn pillar pages, which are ~10% pitch / ~90% resource).*

*Site-Wide Standards, Person schema, and LocalBusiness schema reference blocks all live in Tranche 1 and apply here.*

---

## Page 10 — Google Ads

| Field | Value |
|---|---|
| **URL** | `/services/google-ads/` |
| **Page type** | Service pillar (commercial, money page) |
| **Primary keyword** | `google ads consultant india` |
| **Secondary keywords** | hire google ads consultant · google ads services surat · performance max consultant india · google ads for small business india · google ads freelancer india |
| **Search intent** | Commercial (hire intent) + Info-commercial (evaluation) |
| **H1** | Google Ads — Run Campaigns That Pay Back |
| **Meta title** | Google Ads Consultant — Vraj Vithalani, Surat India *(51 chars)* |
| **Meta description** | Google Ads consulting for service businesses, D2C brands, exporters, and NGOs. Real INR budgets, real ROAS, from an independent specialist based in Surat. *(155 chars)* |
| **Content format** | Service pillar — hero + short-answer + service list + how-I-work + budget conversation + case studies + related guides + FAQ + embedded form |
| **Word count target** | 2,500–3,500 |

### Content structure

- H1 — Google Ads — Run Campaigns That Pay Back
- Hero paragraph (60–80 words, first-person). Opens with: "I run Google Ads for Indian and international businesses that need every rupee of ad spend to justify itself." Includes named verticals + pillar link ("service businesses, D2C brands, industrial exporters, coaching institutes, NGOs").
- **Short-answer block** (60 words, third person for LLM extraction). "Vraj Vithalani offers Google Ads consulting — Search, Performance Max, and Meta Ads — for service businesses and D2C brands in India and internationally. Based in Surat. Contact for quote."
- H2 — What Google Ads work I do
  - H3 — Search campaigns for service businesses
  - H3 — Performance Max (for lead-gen services and e-commerce)
  - H3 — Meta Ads (Instagram/Facebook lead ads as secondary channel)
  - H3 — Landing page + campaign integration (Zone 1 × Zone 3 compound — build the page and the campaign together)
  - H3 — Account audits and rescues (12-point audit process)
  - H3 — Conversion tracking and analytics setup (GA4 + Google Ads conversions + GTM)
- H2 — How I approach a Google Ads engagement (first-person, ~300 words)
  - H3 — Discovery: your business, your offer, your current situation
  - H3 — Foundation: tracking, negatives, account structure — before a single ad goes live
  - H3 — Launch: real budget rules for the first 30 days
  - H3 — Optimize: reading search-terms reports like an investigator
  - H3 — Report and iterate: what actually matters vs vanity metrics
- H2 — The budget conversation — what actually works in India (this is the differentiator section; 300–400 words; real INR anchors)
- H2 — Real Google Ads work I've done
  - H3 — Powercable (industrial exporter, ~40-day project cold-call-to-live)
  - H3 — Parv Travels (3-month Meta + Google Ads engagement, tours & travel)
  - H3 — Synergy Tutorials (admission-season Google Ads for a coaching institute)
  - H3 — VM Graphite Industries (exporter campaign, extension of website work)
- H2 — How I work with clients (5 steps — mirror of Services hub process, condensed)
- H2 — Where I work from and who I work with (Surat home base, India + international, quiet nod to Australia)
- H2 — Related guides on running Google Ads
  - Links to 6 top Tier 1 cluster articles from `/learn/google-ads/` (see Internal links OUT)
- H2 — Frequently asked questions (10 items with FAQ schema)
  - What size businesses do you typically work with?
  - Do you have a minimum ad spend requirement?
  - Do you charge a management fee or a percentage of ad spend?
  - Do you work with businesses outside India?
  - How long does it take to see results?
  - Do you run Meta Ads too, or only Google?
  - Can you rescue an underperforming account someone else built?
  - Do you build the landing pages as well?
  - How do you report on campaigns?
  - What happens if I want to bring the account in-house later?
- H2 — Ready to talk about your Google Ads project? (embedded contact form + WhatsApp button)

### Internal links OUT

- **Location pages** (3): `/google-ads-expert-in-surat/` · `/google-ads-expert-in-ahmedabad/` · `/google-ads-expert-in-bangalore/`
- **Case studies** (3–4 top for Google Ads): `/case-studies/powercable/` · `/case-studies/parv-travels/` · `/case-studies/synergy-tutorials/` · `/case-studies/vm-graphite/`
- **Cluster content — top 6 from `/learn/google-ads/`** (all Tier 1):
  - T1 — `/learn/google-ads/google-ads-account-structure-service-business/`
  - T3 — `/learn/google-ads/minimum-tracking-stack-pre-launch/`
  - T13 — `/learn/google-ads/google-ads-clicks-no-conversions/`
  - T14 — `/learn/google-ads/landing-page-elements-quality-score/`
  - T17 — `/learn/google-ads/12-point-google-ads-audit/`
  - T21 — `/learn/google-ads/minimum-google-ads-budget-that-works/`
- **Content pillar**: `/learn/google-ads/` (from "Related guides" section)
- **Related services**: `/services/seo/` (Ads + SEO compound), `/services/cro-and-automation/` (Ads + landing page + tracking compound)
- `/about/` (author bio link)
- `/contact/` (embedded form + explicit link — this is one of the few contact-linking nodes)
- `/services/` (breadcrumb parent)

### Internal links IN

- Home (4-pillar tile)
- `/services/` hub (pillar tile + description)
- 3 city Google Ads location pages (breadcrumb up + "See full service" link — Tranche 4)
- Every Google Ads cluster article in `/learn/google-ads/` (upward pillar link + author bio "hire me" link — Tranches 3/6/7)
- Case study pages that involve Google Ads work (contextual — Tranche 5)
- About page ("The four things I do" section)
- Other 3 service pillars ("Related services" section — reciprocal cross-links)
- Header nav (every page)
- Footer nav (every page)

### Schema markup required

- **Service** (Google Ads consulting as service offering — `serviceType: "Google Ads Management"`, `provider: {@id: "#business"}`, `areaServed: [India, Australia, Global]`)
- **FAQPage** (10 FAQ items)
- **BreadcrumbList** (Home → Services → Google Ads)
- **Person** and **Organization** (site-wide from Reference Blocks)
- **AggregateRating** if testimonials with ratings exist [TO CONFIRM — likely defer to Phase 4 once real reviews are collected]

### EEAT elements required

- Author byline at top and bottom (headshot + credentials + published + last-updated).
- Certifications badge visible: Google Digital Marketing Certificate (Coursera), AADME Certified Digital Marketer, NIT-EDU Certified Digital Marketer.
- First-person "How I approach a Google Ads engagement" section (~300 words) — this is the EEAT gold for the pillar.
- **Real INR anchors** in the budget-conversation section (e.g., "the ₹15k/month test protocol I've walked clients through works when...").
- Real client attribution (Powercable, Parv Travels, Synergy Tutorials, VM Graphite) with linked case studies for proof.
- Explicit single-actor statement: "I personally run every account I take on. No subcontracting, no junior team, no offshore handoff."
- Reference to years of hands-on: "Running Google Ads for Indian SMBs since 2024" (adjust to actual first-campaign year — [TO CONFIRM]).

### CTA specification

- **Embedded contact form** mid-page (after "Real work I've done" section) + at bottom.
- **WhatsApp CTA button** in hero + at every H2 section break (visually subtle) + in final CTA block.
- **Final block CTA**: two-button layout — "Send inquiry" (form scroll-to) + "WhatsApp me" (wa.me link with prefilled Google-Ads-context text).
- **Floating WhatsApp button** (site-wide).
- **Optional in-hero click-to-call button** [TO CONFIRM — could disrupt reading flow; A/B test post-launch].

### Media requirements

- **Hero image**: Vraj at work / at desk with Google Ads dashboard visible in background, or a stylised campaign-strategy visual. Not stock. 1920×1080, WebP + AVIF. Placeholder pre-launch.
- **Optional dashboard screenshot**: sample (anonymised) Google Ads or Looker Studio dashboard showing real-shape data. Redact client-identifiable metrics. Adds visual credibility for the "how I report" claim.
- **3–4 case study card images**: real project hero shots (Powercable, Parv Travels, Synergy Tutorials, VM Graphite).
- **6 guide thumbnails**: card images for the 6 related cluster articles.
- **5-step process diagram**: horizontal SVG (Discovery → Foundation → Launch → Optimize → Report). Soft-teal accents.
- **Certifications badge strip**: SVG logos of Coursera Google Digital Marketing, AADME, NIT-EDU.
- **Author bio card**: headshot + credentials block at bottom.
- **OG image**: Google-Ads-pillar-specific 1200×630 with headline + Vraj headshot.

### Notes

- **This is a money page.** Word-count on the higher end of the 2,500–3,500 range is fine — depth matters here for both ranking and conversion.
- **60/40 pitch-to-resource weighting.** Enough authoritative content to rank informationally, enough direct pitch to convert commercial visitors.
- **Indian SMB reality lens is loudest on this page.** The budget-conversation section is where real INR anchors, real client-side constraints, and honest ROAS talk appear — never labeled as an angle, always shown.
- **Compound skill of "runs the ads AND builds the page"** is the strongest differentiator against agency competitors. Surface this in the "Landing page + campaign integration" H3 explicitly.
- **FAQ answers must include "Contact for quote"** at least once (locked content-governance rule).
- **"Do you have a minimum ad spend requirement?"** answer is critical — the honest answer is closer to ₹15k/month floor for the test protocol to have signal (aligned with T21 and T22). Don't fake a lower floor; don't scare off larger budgets. Frame as "the floor where I can honestly say the test will produce learning is around ₹15k/month; below that, we should talk about whether Google Ads is the right first move at all."
- **Do NOT include physiotherapy case studies as headline examples** on this page — physio only surfaces as one of many verticals in the "who I work with" copy. The four case studies surfaced are industrial exporter, tours, coaching, and B2B manufacturer.
- **Meta Ads (secondary channel)** placement inside the H2 list is deliberate — signals capability without diluting the Google Ads primary positioning.
- **Client-account confidentiality**: any dashboard screenshots must redact client names, exact spend, and account IDs. Show shapes, not numbers where client-identifying.
- **Location page anchors**: the 3 city links appear in a small block after "Where I work from and who I work with", so location pages inherit clear pillar-parent link equity.
- **Related services cross-links** (SEO, CRO) are the compound-story upsell. Keep the copy honest: "Google Ads works better when the SEO is right and the landing page converts. If you're hiring me for Ads and either of those is broken, we'll fix them or scope them separately."

---

## Page 11 — SEO

| Field | Value |
|---|---|
| **URL** | `/services/seo/` |
| **Page type** | Service pillar (commercial, money page) |
| **Primary keyword** | `seo consultant india` |
| **Secondary keywords** | seo services surat · hire seo consultant india · technical seo india · geo consultant india · local seo consultant india · generative engine optimization india |
| **Search intent** | Commercial (hire intent) + Info-commercial (evaluation of GEO in particular) |
| **H1** | SEO — Rank in Google and AI Search |
| **Meta title** | SEO & GEO Consultant — Vraj Vithalani, Surat India *(50 chars)* |
| **Meta description** | SEO and Generative Engine Optimization for Indian businesses ranking in Google, ChatGPT, Perplexity, and Google AI Mode. Independent consultant based in Surat. *(160 chars)* |
| **Content format** | Service pillar — hero + short-answer + service list + how-I-work + GEO deep-dive + case studies + related guides + FAQ + embedded form |
| **Word count target** | 2,500–3,500 |

### Content structure

- H1 — SEO — Rank in Google and AI Search
- Hero paragraph (60–80 words, first-person). Explicitly names both Google search AND AI search (ChatGPT, Perplexity, Google AI Mode) — the fresh GEO positioning is the moat.
- **Short-answer block** (60 words). Third person, entity-loaded.
- H2 — What SEO work I do
  - H3 — Technical SEO (WordPress and Next.js)
  - H3 — On-page SEO and content structure
  - H3 — Schema markup implementation (Person, LocalBusiness, Service, FAQPage, Article, and Product schemas)
  - H3 — Local SEO for Indian cities (GBP, citations, location-page architecture)
  - H3 — Generative Engine Optimization — GEO / AI search (dedicated H3 because this is the fresh differentiator)
  - H3 — SEO audits and account rescues (indexation recovery, penalty diagnosis, technical foundation)
  - H3 — Content strategy and topic clusters (hub-and-spoke architecture; this site is the working example)
- H2 — How I approach an SEO engagement (first-person, ~300 words)
  - H3 — Audit: crawlability, indexation, on-page, schema, backlinks, GBP
  - H3 — Fix the technical foundation (this is often where most wins hide on Indian SMB sites)
  - H3 — Content architecture (pillars + clusters, internal linking)
  - H3 — On-page + schema (per page and per template)
  - H3 — Off-site + GBP (the honest Indian local citation stack)
  - H3 — Track + iterate (Search Console + GA4 + real-user metrics)
- H2 — A note on SEO in the LLM era (dedicated 400-word section — the GEO differentiator; this site itself as the working example of the entity-reset problem)
- H2 — Real SEO work I've done
  - H3 — drvishva (Next.js site with schema and GEO from launch)
  - H3 — Powercable (WordPress indexation + on-page + local signals)
  - H3 — Vitthalshringar (e-commerce SEO in progress)
  - H3 — vrajvithalani.com (this site — the working example of GEO applied to a real repositioning problem)
- H2 — How I work with clients
- H2 — Where I work from and who I work with
- H2 — Related guides on SEO and GEO
  - Links to 6 top Tier 1 cluster articles from `/learn/seo/`
- H2 — Frequently asked questions (10 items)
  - How long does SEO take to show results?
  - What's the difference between SEO and GEO / AI search optimization?
  - Do you do link building?
  - Do you work on international SEO?
  - Can you fix a site that's been de-indexed or penalised?
  - Do you build the site as well, or just optimise it?
  - What tools do you use?
  - Do you work with WordPress and Next.js both?
  - How do you handle reporting?
  - What happens after the engagement ends?
- H2 — Ready to talk about your SEO or GEO project? (embedded form + WhatsApp)

### Internal links OUT

- **Location pages** (3): `/seo-consultant-in-surat/` · `/seo-consultant-in-ahmedabad/` · `/seo-consultant-in-bangalore/`
- **Case studies** (3–4 top for SEO): `/case-studies/drvishva/` · `/case-studies/powercable/` · `/case-studies/vitthalshringar/` · `/case-studies/vm-graphite/`
- **Cluster content — top 6 from `/learn/seo/`** (all Tier 1):
  - T26 — `/learn/seo/wordpress-technical-seo-audit-checklist/`
  - T34 — `/learn/seo/schema-types-service-business-site/`
  - T38 — `/learn/seo/hub-and-spoke-content-architecture/`
  - T45 — `/learn/seo/what-is-generative-engine-optimization/`
  - T46 — `/learn/seo/short-answer-block-llm-extraction/`
  - T47 — `/learn/seo/appear-in-chatgpt-perplexity-ai-mode/`
- **Content pillar**: `/learn/seo/`
- **Related services**: `/services/google-ads/` (SEO + Ads compound), `/services/web-development/` (SEO built into the build)
- `/about/`
- `/contact/` (embedded form + explicit link)
- `/services/` (breadcrumb parent)

### Internal links IN

- Home (4-pillar tile)
- `/services/` hub
- 3 city SEO location pages (breadcrumb up + "See full service" link — Tranche 4)
- Every SEO cluster article in `/learn/seo/` (upward pillar link + author bio — Tranches 3/6/7)
- Case study pages with SEO angle (contextual — Tranche 5)
- About page
- Other 3 service pillars ("Related services" cross-links)
- Header + footer nav

### Schema markup required

- **Service** (SEO consulting — `serviceType: "Search Engine Optimization"`, provider link, areaServed)
- **FAQPage** (10 FAQ items)
- **BreadcrumbList** (Home → Services → SEO)
- **Person** and **Organization** (site-wide)

### EEAT elements required

- Author byline top and bottom.
- Certifications badge strip (Coursera Google Digital Marketing, AADME, NIT-EDU).
- First-person "How I approach an SEO engagement" section (~300 words).
- **Meta-move**: the "A note on SEO in the LLM era" section explicitly names Vraj's own AI-misclassification problem as source material. "The reason I'm confident about GEO is that I've been applying it to my own repositioning problem for months — this site is the working example." This is unbeatable EEAT.
- Real client attribution: drvishva, Powercable, Vitthalshringar, plus vrajvithalani.com itself.
- Reference to years of hands-on SEO: "SEO practice since 2023" [TO CONFIRM year].
- No inflated backlink or ranking numbers — honest positioning.

### CTA specification

- Embedded contact form mid-page (after "Real work I've done") and at bottom.
- WhatsApp CTA button in hero + at final CTA block.
- Final block CTA: "Send inquiry" (form scroll-to) + "WhatsApp me" (prefilled SEO-context text).
- Floating WhatsApp button (site-wide).

### Media requirements

- **Hero image**: Vraj at desk with Search Console / analytics visible, or a stylised "SEO + GEO" split visual. Not stock. 1920×1080.
- **Optional Search Console screenshot**: anonymised, showing indexation/impressions curve. Adds credibility.
- **Optional schema-markup code snippet visual**: shows a real JSON-LD block (from this site) — adds "builder credibility."
- **3–4 case study card images**: drvishva, Powercable, Vitthalshringar, VM Graphite.
- **6 guide thumbnails** for related cluster articles.
- **6-step process diagram**: Audit → Fix → Architect → On-page + Schema → Off-site + GBP → Track. Horizontal SVG.
- **Certifications badge strip**.
- **Author bio card**.
- **OG image**: SEO-pillar-specific 1200×630.

### Notes

- **GEO is the moat.** Phase 1b said explicitly the GEO window closes in 12–18 months. This pillar page must lean into GEO hard — dedicated H2 section, GEO in the primary keyword string (secondary), GEO in the hero paragraph, GEO in the "How I approach" audit step, GEO in the LLM-era section.
- **This site as working example** is the strongest single EEAT play across the whole website. State it directly: "vrajvithalani.com is being built as a live, ranking asset — the entity-reset problem I'm solving for myself is the same problem I solve for clients."
- **Physiotherapy note**: drvishva SEO case study is fine (that's the case study format). But no standalone physiotherapy SEO content ever (Doc 02 rule). The Related Guides section links only to Tier 1 SEO topics, none physiotherapy-vertical.
- **Local SEO for Indian cities** section should tie to the 3 city location pages, not be a competing catch-all. This pillar drives visitors down to those location pages.
- **"Do you do link building?"** FAQ answer: honest — "Link building I do is limited and manual. I focus on citation cleanup, digital PR opportunities, and content that earns links naturally. I don't buy links, and I don't recommend agencies that promise volume."
- **International SEO for markets Vraj hasn't served** stays out of bounds per Doc 02. International SEO offered = for Indian exporters targeting overseas buyers (T90 territory), NOT SEO for US clients targeting the US market.
- **Compound with web dev**: mention that Vraj can ship the schema, edit the theme code, and rebuild internal linking as part of the SEO engagement — because he's also the developer. This is the compound skill differentiator.
- **Compound with Ads**: the "Related services" section notes that Ads + SEO compound; specifically the same landing page has to work for both channels.

---

## Page 12 — Web Development

| Field | Value |
|---|---|
| **URL** | `/services/web-development/` |
| **Page type** | Service pillar (commercial, money page) |
| **Primary keyword** | `web developer india` |
| **Secondary keywords** | wordpress developer india · nextjs developer india · hire web developer surat · custom cms developer india · razorpay integration developer · nodejs developer india |
| **Search intent** | Commercial (hire intent) + Info-commercial (stack evaluation) |
| **H1** | Web Development — WordPress, Next.js, and Custom Stacks |
| **Meta title** | Web Developer — Vraj Vithalani (WordPress, Next.js, Node) *(57 chars)* |
| **Meta description** | Web development in WordPress, Next.js, and Node.js for service businesses, D2C brands, exporters, NGOs. Full-stack builds by an independent Surat developer. *(157 chars)* |
| **Content format** | Service pillar — hero + short-answer + service list + how-I-work + stack disclosure + case studies + related guides + FAQ + embedded form |
| **Word count target** | 2,500–3,500 |

### Content structure

- H1 — Web Development — WordPress, Next.js, and Custom Stacks
- Hero paragraph (60–80 words, first-person). "I build websites and web apps for service businesses, D2C brands, industrial exporters, and NGOs — WordPress when it's right, Next.js when it's right, and custom Node/NestJS stacks when the requirement doesn't fit either."
- **Short-answer block** (60 words). Third person.
- H2 — What web development work I do
  - H3 — WordPress builds and rescues (theme-appropriate architecture, security, speed)
  - H3 — Next.js sites for service businesses and personal brands (conversion-focused, SEO-native, LLM-ready)
  - H3 — Node.js and NestJS backends (custom APIs, admin panels, integrations)
  - H3 — Custom CMS design (donor management for NGOs, CRM-lite for service businesses, admin panels)
  - H3 — Razorpay and payment integration (checkout, subscriptions, refunds, compliance)
  - H3 — E-commerce (Shopify and WooCommerce — honest platform-fit calls)
  - H3 — Site security hardening (WordFence + 2FA + backup + disaster recovery)
  - H3 — Hostinger deployment (Managed WooCommerce Cloud Startup, Node.js app slots, MongoDB Atlas)
- H2 — How I approach a web development engagement (first-person, ~300 words)
  - H3 — Discovery + spec (what the site actually needs to do)
  - H3 — Stack decision (WordPress vs Next.js vs custom — honest call)
  - H3 — Design decisions (visual, UX, conversion-first structure)
  - H3 — Build sprints (weekly demos, no black-box work)
  - H3 — QA and pre-launch checklist (SEO-ready, Ads-ready, tracking-ready from day one)
  - H3 — Launch + post-launch support (30-day settling period, then handover options)
- H2 — The stack I actually ship on (dedicated 300-word section — builder-credibility play)
  - Frontend: WordPress (block themes, page builders judged case-by-case), Next.js (14+, App Router)
  - Backend: Node.js, NestJS, Django/FastAPI (Python) for backend-heavy work
  - Database: MongoDB (Atlas), MySQL, PostgreSQL
  - Payments: Razorpay (primary for India), Cashfree, PayU
  - Hosting: Hostinger (primary), Cloudflare, Vercel (Next.js edge cases)
  - Security: WordFence + 2FA, HTTPS-first, backup strategy
  - Analytics: GA4, GTM, Search Console, Looker Studio
- H2 — Real web development work I've done
  - H3 — Powercable (WordPress, live at powercable.co.in, ~40-day cold-call-to-deployment)
  - H3 — drvishva (Next.js, launching soon)
  - H3 — Vitthalshringar (WooCommerce/Shopify e-commerce, in progress)
  - H3 — Trust NGO (custom donation and beneficiary CMS, launching soon)
  - H3 — Dreams Astro Numero Foundation (WordPress + Razorpay + course platform + 22 service pages)
  - H3 — VM Graphite Industries (exporter WordPress site)
  - H3 — IOTA ANPR (Python backend + edge deployment on Raspberry Pi — overview only)
- H2 — How I work with clients
- H2 — Where I work from and who I work with
- H2 — Related guides on web development
  - Links to 6 top Tier 1/Tier 2 cluster articles from `/learn/web-development/`
- H2 — Frequently asked questions (10 items)
  - Do you always recommend WordPress, or do you actually recommend Next.js sometimes?
  - Do you build e-commerce sites?
  - Can you migrate my existing site to a new stack?
  - Do you handle hosting setup and DNS?
  - What about ongoing maintenance after launch?
  - Do you build the design or do I need to hire a designer?
  - Do you integrate Razorpay / other Indian payment gateways?
  - Do you build custom admin panels / CMS?
  - How long does a typical site take?
  - What happens to my site if I stop working with you?
- H2 — Ready to talk about your web project? (embedded form + WhatsApp)

### Internal links OUT

- **Location pages** (3): `/web-developer-in-surat/` · `/web-developer-in-ahmedabad/` · `/web-developer-in-bangalore/`
- **Case studies** (5–6 top for Web Dev): `/case-studies/powercable/` · `/case-studies/drvishva/` · `/case-studies/vitthalshringar/` · `/case-studies/trust-ngo/` · `/case-studies/dreams-astro/` · `/case-studies/vm-graphite/`
- **Cluster content — top 6 from `/learn/web-development/`**:
  - T51 (merged with T63) — `/learn/web-development/wordpress-speed-shared-hosting/`
  - T54 — `/learn/web-development/nextjs-personal-brand-google-llms/`
  - T59 — `/learn/web-development/razorpay-checkout-wordpress/`
  - T62 — `/learn/web-development/wordfence-2fa-hardening/`
  - T66 (merged with T87) — `/learn/web-development/shopify-vs-woocommerce-india-d2c/`
  - T117 — `/learn/web-development/nextjs-site-for-llm-citation/`
- **Content pillar**: `/learn/web-development/`
- **Related services**: `/services/seo/` (SEO baked into the build), `/services/cro-and-automation/` (conversion-focused builds)
- `/about/`
- `/contact/` (embedded form + explicit link)
- `/services/` (breadcrumb parent)

### Internal links IN

- Home (4-pillar tile)
- `/services/` hub
- 3 city Web Dev location pages
- Every Web Dev cluster article (upward pillar link)
- Case study pages that involve build work
- About page
- Other 3 service pillars ("Related services")
- Header + footer nav

### Schema markup required

- **Service** (Web Development — `serviceType: "Web Development"`, provider link, areaServed)
- **FAQPage** (10 FAQ items)
- **BreadcrumbList** (Home → Services → Web Development)
- **Person** and **Organization** (site-wide)

### EEAT elements required

- Author byline top and bottom.
- Certifications + credentials block (Diploma in Computer Engineering — the credential most relevant to this pillar — plus digital marketing certs to prove the marketer-who-codes cross-over).
- First-person "How I approach" section (~300 words).
- **"Stack I actually ship on" section** is the builder-credibility signature — depth of specific tool naming is the EEAT play here (WordFence, 2FA, WordPress block themes, Next.js App Router, NestJS, Razorpay, PM2, Nginx, MongoDB Atlas — specificity matters).
- Real client attribution across 7 build case studies, including the ~40-day Powercable timeline and the drvishva Next.js example.
- Explicit statement: "I write the code myself. Every project below is my own build."
- IOTA ANPR handling: overview-only per Doc 02 — mention capability (Python, Raspberry Pi, edge CV) without implementation detail.

### CTA specification

- Embedded contact form mid-page (after "Real work I've done") and at bottom.
- WhatsApp CTA in hero + final block.
- Final block CTA: "Send inquiry" + "WhatsApp me" (prefilled Web-Dev-context).
- Floating WhatsApp (site-wide).

### Media requirements

- **Hero image**: Vraj at desk with code editor visible, or a stylised "WordPress + Next.js + Node" split visual. Not stock. 1920×1080.
- **Optional code snippet visual**: real snippet from a shipped project (Next.js page component, Razorpay handler, or JSON-LD schema block) — screenshot with syntax highlighting. Adds builder credibility.
- **5–6 case study card images**: real project hero shots (Powercable, drvishva, vitthalshringar, Trust NGO, Dreams Astro, VM Graphite).
- **6 guide thumbnails** for related cluster articles.
- **6-step process diagram**: Discovery → Stack → Design → Build sprints → QA + pre-launch → Launch + support.
- **Stack visual (optional)**: horizontal logo strip — WordPress, Next.js, Node.js, NestJS, MongoDB, Razorpay, WordFence, Shopify, Hostinger.
- **Author bio card**.
- **OG image**: Web-Dev-pillar-specific 1200×630.

### Notes

- **Two-tier architecture is the differentiator.** Most WordPress developers can't ship Next.js. Most Next.js developers can't rescue a broken WordPress site. Vraj can — and this pillar page should make that plain without swagger.
- **IOTA ANPR mention** is included in the "Real work I've done" section as one of 7 case studies. Explicitly labeled "overview only" — no implementation detail per Doc 02.
- **"Do you always recommend WordPress, or do you actually recommend Next.js sometimes?"** FAQ answer is critical — the honest call is: "For a service business that needs content ownership and doesn't have a developer to maintain a JS-heavy site, WordPress usually wins. For a personal brand or D2C brand that needs speed, SEO, and modern UX, Next.js often wins. I'll tell you honestly which one fits your project — I have no incentive to push either."
- **"What happens to my site if I stop working with you?"** answer builds trust: "You own the site, the domain, the code, and the hosting. I don't hostage-hold. On handover I document the stack, hand over credentials, and offer a paid transition-support option if you want it."
- **Hostinger deployment** is a defensible corner per Phase 1b. Mention Hostinger explicitly in the stack section + the FAQ.
- **NGO custom CMS work** (Trust project) is a differentiator — very few full-stack developers ship custom CMS work for NGOs in India. Mention specifically.
- **Shopify vs WooCommerce**: merged T66+T87 cluster article is the go-to reference for the e-commerce decision — link prominently.
- **English only, no pricing** — same locked rules. FAQ answers include "Contact for quote" at least once.
- **Client-owned code**: state explicitly (see FAQ answer above). This is a real trust signal against agencies that gate credentials.
- **Physiotherapy handled properly**: drvishva as one of many case studies, labeled honestly as "Next.js physiotherapy site — launching soon."

---

## Page 13 — CRO & Automation

| Field | Value |
|---|---|
| **URL** | `/services/cro-and-automation/` |
| **Page type** | Service pillar (commercial, money page) |
| **Primary keyword** | `cro consultant india` |
| **Secondary keywords** | conversion rate optimization india · ga4 consultant india · google tag manager consultant india · whatsapp automation for business india · landing page optimization india · marketing automation consultant india |
| **Search intent** | Commercial (hire intent) + Info-commercial (evaluation) |
| **H1** | CRO & Automation — Turn More of Your Traffic into Leads |
| **Meta title** | CRO & Automation Consultant — Vraj Vithalani, India *(51 chars)* |
| **Meta description** | CRO, GA4/GTM setup, WhatsApp automation, and funnel design for Indian service businesses and D2C brands. Independent consultant based in Surat, India. *(150 chars)* |
| **Content format** | Service pillar — hero + short-answer + service list + how-I-work + SMB-CRO note + case studies + related guides + FAQ + embedded form |
| **Word count target** | 2,500–3,500 |

### Content structure

- H1 — CRO & Automation — Turn More of Your Traffic into Leads
- Hero paragraph (60–80 words, first-person). "CRO literature assumes A/B-testable traffic volume no small business actually has. What actually improves conversions for an Indian SMB is a smaller set of judgment calls, tighter tracking, and a lead funnel that ends where the client actually replies — usually WhatsApp."
- **Short-answer block** (60 words). Third person.
- H2 — What CRO & Automation work I do
  - H3 — Landing page conversion optimization (heuristic-first, judgment over A/B tests)
  - H3 — GA4 setup for service businesses (the events that actually matter)
  - H3 — Google Tag Manager for non-developers (safe deploys, no site breaks)
  - H3 — WhatsApp Business automation (App vs API, funnel design, lead routing)
  - H3 — Form optimization and routing (form → WhatsApp + email + CRM in one flow)
  - H3 — Email nurture and lifecycle automation (minimum-viable Indian SMB stack)
  - H3 — Meta Instant Forms and lead-routing decisions (when Instant Forms beat a landing page)
- H2 — How I approach a CRO engagement (first-person, ~300 words)
  - H3 — Baseline: what's actually happening now (numbers, funnel drop-offs, tracking gaps)
  - H3 — Diagnose: where conversion is leaking (usually 2–3 spots, not 20)
  - H3 — Prioritize: biggest wins first (no A/B tests you don't have volume for)
  - H3 — Ship changes (design + copy + tech, integrated)
  - H3 — Measure and iterate (real numbers, not vanity metrics)
- H2 — The SMB reality of CRO (dedicated 400-word section — the ownable angle; explicit contrast with enterprise CRO assumptions)
- H2 — The automation stack for a solo Indian SMB
  - Analytics: GA4 + GTM + Search Console + Looker Studio
  - Forms: WPForms / Fluent Forms / custom, routed via webhook
  - CRM-lite: FluentCRM / HubSpot free / MongoDB-backed admin
  - Email: Brevo / MailerLite / ConvertKit (honest cost anchors)
  - WhatsApp: Business App for < 10/day; BSP (AiSensy / WATI / Interakt) for scale — honest thresholds
  - Meta Lead Ads: Instant Forms with immediate WhatsApp routing
- H2 — Real CRO & Automation work I've done
  - H3 — Powercable (form routing + tracking + WhatsApp handoff)
  - H3 — Vitthalshringar (e-commerce checkout CRO in progress)
  - H3 — drvishva (Next.js landing page + WhatsApp funnel)
  - H3 — Parv Travels (Meta Instant Forms vs landing page — the honest tradeoff)
  - H3 — Little Genius (broader marketing lift — 10x brand awareness — as CRO-adjacent signal)
- H2 — How I work with clients
- H2 — Where I work from and who I work with
- H2 — Related guides on CRO and automation
  - Links to 6 top Tier 1/Tier 2 cluster articles from `/learn/cro-and-automation/`
- H2 — Frequently asked questions (10 items)
  - Can you do CRO if my site doesn't have much traffic yet?
  - Do you set up GA4 and GTM from scratch?
  - Do you work with WhatsApp Business API providers?
  - Do you build the landing pages, or just optimise existing ones?
  - How do I know if I need CRO or more traffic?
  - Do you run A/B tests?
  - What if my current form/CRM/tools aren't working well together?
  - Do you integrate with Zapier / Make / Pabbly?
  - Can you help with Meta Instant Forms setup?
  - What's the difference between CRO work and Google Ads landing page work?
- H2 — Ready to talk about your CRO or automation project? (embedded form + WhatsApp)

### Internal links OUT

- **Location pages** (3): `/cro-expert-in-surat/` · `/cro-expert-in-ahmedabad/` · `/cro-expert-in-bangalore/`
- **Case studies** (4–5 top for CRO): `/case-studies/powercable/` · `/case-studies/vitthalshringar/` · `/case-studies/drvishva/` · `/case-studies/parv-travels/` · `/case-studies/little-genius/`
- **Cluster content — top 6 from `/learn/cro-and-automation/`**:
  - T69 — `/learn/cro-and-automation/service-business-landing-page-checklist/`
  - T76 — `/learn/cro-and-automation/whatsapp-first-lead-capture-funnel/`
  - T72 — `/learn/cro-and-automation/ga4-events-service-business/`
  - T73 — `/learn/cro-and-automation/google-tag-manager-non-developers/`
  - T112 — `/learn/cro-and-automation/landing-page-speed-quality-score-seo/` (cross-zone piece; lives under CRO pillar per Phase 1b compound-topic placement)
  - T75 — `/learn/cro-and-automation/whatsapp-business-api-vs-app/`
- **Content pillar**: `/learn/cro-and-automation/`
- **Related services**: `/services/google-ads/` (landing page + tracking compound), `/services/web-development/` (build + CRO integrated)
- `/about/`
- `/contact/` (embedded form + explicit link)
- `/services/` (breadcrumb parent)

### Internal links IN

- Home (4-pillar tile)
- `/services/` hub
- 3 city CRO location pages
- Every CRO cluster article (upward pillar link)
- Case study pages with CRO/automation angle
- About page
- Other 3 service pillars ("Related services")
- Header + footer nav

### Schema markup required

- **Service** (CRO & Automation — `serviceType: "Conversion Rate Optimization"`, provider link, areaServed)
- **FAQPage** (10 FAQ items)
- **BreadcrumbList** (Home → Services → CRO & Automation)
- **Person** and **Organization** (site-wide)

### EEAT elements required

- Author byline top and bottom.
- Certifications badge strip.
- First-person "How I approach" section (~300 words).
- **The SMB-reality-of-CRO section** is the EEAT differentiator — call out explicitly that enterprise CRO literature assumes traffic volume and tools that Indian SMBs don't have, and describe what actually works instead.
- Real client references (Powercable, Vitthalshringar, drvishva, Parv Travels, Little Genius) with linked case studies.
- Tool-stack disclosure — specific tool naming (FluentForms, AiSensy, Brevo, GTM, Looker Studio) is the builder-credibility signal.
- Little Genius 10x brand awareness metric surfaced.

### CTA specification

- Embedded contact form mid-page (after "Real work I've done") and at bottom.
- WhatsApp CTA in hero + final block.
- Final block CTA: "Send inquiry" + "WhatsApp me" (prefilled CRO-context).
- Floating WhatsApp (site-wide).

### Media requirements

- **Hero image**: Vraj at desk with GA4 or funnel visualization visible, or a stylised "traffic → funnel → conversion" flow visual. Not stock. 1920×1080.
- **Optional funnel diagram**: real-shape funnel with (anonymised) drop-off numbers — adds credibility to the "diagnose leakage" claim.
- **4–5 case study card images**: Powercable, Vitthalshringar, drvishva, Parv Travels, Little Genius.
- **6 guide thumbnails** for related cluster articles.
- **5-step process diagram**: Baseline → Diagnose → Prioritize → Ship → Measure & iterate.
- **Stack visual (optional)**: horizontal logo strip — GA4, GTM, WhatsApp Business, Meta, FluentForms, Brevo, Looker Studio.
- **Author bio card**.
- **OG image**: CRO-pillar-specific 1200×630.

### Notes

- **Depth is honest.** Doc 02 places CRO at "moderate–deep." Don't over-claim on this pillar; the strong angle is judgment + heuristics + SMB reality, not enterprise-scale A/B testing.
- **WhatsApp as lead channel** is India-specific and under-covered by US CRO writers per Phase 1b — this pillar page should make WhatsApp visible early (in the hero, in the service list, in the stack).
- **"Can you do CRO if my site doesn't have much traffic?"** FAQ answer is critical — the honest call is: "Yes. A/B testing needs traffic; heuristic CRO doesn't. On low-traffic sites, the win is usually one fixed diagnostic + one clear conversion path, not a testing programme."
- **"What's the difference between CRO work and Google Ads landing page work?"** answer distinguishes the offer: "Google Ads landing page work is scoped to a single campaign; CRO work covers the whole funnel — the page, the form, the tracking, the follow-up sequence. When I do both together on the same engagement, they compound."
- **Meta Instant Forms** section is called out explicitly per T24 (Zone 1.7) — this is under-covered in the industry and one of the more useful CRO calls for Indian service businesses.
- **Cross-zone piece placement**: T112 (Landing page speed × QS × SEO) lives under `/learn/cro-and-automation/` per Phase 1b's compound-topic assignment. The linked-out URL uses that pillar path.
- **Little Genius** appears here as CRO-adjacent — the 10x brand awareness lift metric isn't strictly a CRO metric but functions as a marketing-lift proof and links back to the case study.
- **English only, no pricing** — locked rules. FAQ includes "Contact for quote" at least once.
- **Physiotherapy** appears once (drvishva as a case study example) — not headlined.

---

## Tranche 2 — Summary at a Glance

| # | URL | Page type | Primary keyword | Word count | Featured case studies | Featured cluster articles |
|---|---|---|---|---|---|---|
| 10 | `/services/google-ads/` | Service pillar | google ads consultant india | 2,500–3,500 | Powercable, Parv Travels, Synergy Tutorials, VM Graphite | T1, T3, T13, T14, T17, T21 |
| 11 | `/services/seo/` | Service pillar | seo consultant india | 2,500–3,500 | drvishva, Powercable, Vitthalshringar, VM Graphite | T26, T34, T38, T45, T46, T47 |
| 12 | `/services/web-development/` | Service pillar | web developer india | 2,500–3,500 | Powercable, drvishva, Vitthalshringar, Trust NGO, Dreams Astro, VM Graphite | T51 (merged), T54, T59, T62, T66 (merged), T117 |
| 13 | `/services/cro-and-automation/` | Service pillar | cro consultant india | 2,500–3,500 | Powercable, Vitthalshringar, drvishva, Parv Travels, Little Genius | T69, T76, T72, T73, T112, T75 |

**Total word count for Tranche 2 pages: ~10,000–14,000 words.**

**Every pillar page links out to**: 3 city location pages (Tranche 4), 4–6 case studies (Tranche 5), 6 top cluster articles from its own Learn pillar (Tranches 3/6/7), the Learn pillar hub itself (Tranche 3), 2 related service pillars (reciprocal cross-links within Tranche 2), About, Contact, and the Services hub (breadcrumb parent, Tranche 1).

**Every pillar page receives inbound links from**: Home, Services hub, 3 city location pages, every cluster article in its Learn pillar, case study pages that involve that service, About page, other 3 service pillars (cross-links), header nav, footer nav.

---

## Tranche 2 — Internal Linking Map (ASCII tree)

```
/services/                                      (Services hub — Tranche 1, breadcrumb parent)
 │
 ├─→ /services/google-ads/                      (Tranche 2 · money page)
 │    │
 │    ├─→ LOCATION PAGES (Tranche 4)
 │    │    ├─→ /google-ads-expert-in-surat/
 │    │    ├─→ /google-ads-expert-in-ahmedabad/
 │    │    └─→ /google-ads-expert-in-bangalore/
 │    │
 │    ├─→ CASE STUDIES (Tranche 5)
 │    │    ├─→ /case-studies/powercable/
 │    │    ├─→ /case-studies/parv-travels/
 │    │    ├─→ /case-studies/synergy-tutorials/
 │    │    └─→ /case-studies/vm-graphite/
 │    │
 │    ├─→ CLUSTER ARTICLES (Tranche 3)
 │    │    ├─→ /learn/google-ads/google-ads-account-structure-service-business/  (T1)
 │    │    ├─→ /learn/google-ads/minimum-tracking-stack-pre-launch/              (T3)
 │    │    ├─→ /learn/google-ads/google-ads-clicks-no-conversions/               (T13)
 │    │    ├─→ /learn/google-ads/landing-page-elements-quality-score/            (T14)
 │    │    ├─→ /learn/google-ads/12-point-google-ads-audit/                      (T17)
 │    │    └─→ /learn/google-ads/minimum-google-ads-budget-that-works/           (T21)
 │    │
 │    ├─→ CONTENT PILLAR HUB
 │    │    └─→ /learn/google-ads/                                                (Tranche 3)
 │    │
 │    ├─→ RELATED SERVICES (cross-links within Tranche 2)
 │    │    ├─→ /services/seo/
 │    │    └─→ /services/cro-and-automation/
 │    │
 │    ├─→ /about/                                                                 (author bio)
 │    └─→ /contact/                                                               (embedded form + explicit link)
 │
 ├─→ /services/seo/                             (Tranche 2 · money page)
 │    ├─→ /seo-consultant-in-surat/  · -ahmedabad/  · -bangalore/                (Tranche 4)
 │    ├─→ /case-studies/{drvishva, powercable, vitthalshringar, vm-graphite}/    (Tranche 5)
 │    ├─→ /learn/seo/{T26, T34, T38, T45, T46, T47}/                             (Tranche 3)
 │    ├─→ /learn/seo/                                                             (Tranche 3)
 │    ├─→ Related: /services/google-ads/  ·  /services/web-development/
 │    ├─→ /about/
 │    └─→ /contact/
 │
 ├─→ /services/web-development/                 (Tranche 2 · money page)
 │    ├─→ /web-developer-in-surat/  · -ahmedabad/  · -bangalore/                 (Tranche 4)
 │    ├─→ /case-studies/{powercable, drvishva, vitthalshringar, trust-ngo, dreams-astro, vm-graphite}/  (Tranche 5)
 │    ├─→ /learn/web-development/{T51, T54, T59, T62, T66, T117}/                (Tranche 3)
 │    ├─→ /learn/web-development/                                                 (Tranche 3)
 │    ├─→ Related: /services/seo/  ·  /services/cro-and-automation/
 │    ├─→ /about/
 │    └─→ /contact/
 │
 └─→ /services/cro-and-automation/              (Tranche 2 · money page)
      ├─→ /cro-expert-in-surat/  · -ahmedabad/  · -bangalore/                    (Tranche 4)
      ├─→ /case-studies/{powercable, vitthalshringar, drvishva, parv-travels, little-genius}/  (Tranche 5)
      ├─→ /learn/cro-and-automation/{T69, T76, T72, T73, T112, T75}/             (Tranches 3 & 6)
      ├─→ /learn/cro-and-automation/                                              (Tranche 3)
      ├─→ Related: /services/google-ads/  ·  /services/web-development/
      ├─→ /about/
      └─→ /contact/
```

**Cross-link matrix (which pillars link to which)**:

| From ↓ / To → | Google Ads | SEO | Web Dev | CRO |
|---|---|---|---|---|
| **Google Ads** | — | ✓ | | ✓ |
| **SEO** | ✓ | — | ✓ | |
| **Web Dev** | | ✓ | — | ✓ |
| **CRO** | ✓ | | ✓ | — |

Each pillar reciprocally cross-links to 2 of the other 3 pillars, based on the natural compound story (Ads↔SEO, Ads↔CRO, SEO↔WebDev, WebDev↔CRO). Full 4×4 cross-linking would dilute the compound narrative on each page; the 2-cross-links pattern keeps each pillar's related-services section sharp.

---

## Gaps observed

1. **"Years running client campaigns"** phrasing appears in EEAT sections across all 4 pillars. Marked [TO CONFIRM] — please confirm the year Vraj first ran a paid Google Ads campaign (best guess based on Doc 01: 2024, after the digital marketing course at AADME / Soni Computer Institute) and the year of first SEO engagement (best guess: 2023, from Dreams Astro Numero WordPress launch). Both years are used in Person schema and pillar body copy.
2. **Google Ads pillar T22 (₹15k budget) note**: T22 is a Tier 1 cluster article but is not in the "top 6" featured cluster list for the Google Ads pillar (kept as T1, T3, T13, T14, T17, T21 — the six that most directly serve pillar-visitor intent). T22 will still receive prominent placement on the `/learn/google-ads/` pillar page (Tranche 3). If you'd prefer T22 in the pillar-page "Related guides" section, swap it in for T21 (which is topically very close). Flagging.
3. **CRO pillar cluster mix**: T112 (cross-zone landing-page speed piece) is filed under `/learn/cro-and-automation/` per Phase 1b, but by content it also naturally belongs under `/learn/seo/` or `/learn/google-ads/`. The blueprint places it under CRO per Phase 1b's authoritative assignment, but every pillar links to it. Flagging so no one is surprised when they see the CRO pillar link out to a piece that mentions Quality Score.
4. **Meta Ads coverage**: Meta Ads sits as a secondary channel on the Google Ads pillar (per Doc 02 — Meta is in-bounds but secondary). Two cluster articles (T24, T25) exist. Consider — post-Tranche-3 traffic data — whether Meta Ads deserves its own service sub-page (`/services/meta-ads/`) or stays folded into Google Ads. Not adding without approval; flagging as a Phase 3+ decision point.
5. **Certifications badge visuals**: assumes SVG logos are available for Coursera (Google Digital Marketing), AADME, and NIT-EDU. If any of these don't have clean logo assets, badge strip may need to render as text-only ("Certified: Google Digital Marketing (Coursera) · AADME · NIT-EDU"). [TO CONFIRM PHASE 4]
6. **NIT-EDU certification entity name**: full formal name of the issuing body [TO CONFIRM] — used in Person schema hasCredential array and pillar-page certifications strip.
7. **Testimonials with ratings**: no `AggregateRating` schema included in any pillar's schema list. If Google reviews or client testimonials with numeric ratings exist by launch, add `AggregateRating` to every pillar's Service schema. Flagging for Phase 4 launch checklist.
8. **Client dashboards / screenshots**: any client-facing dashboard or Search Console screenshot used as media on any pillar page must be redacted of client-identifying data (account IDs, exact spend, exact company names in graphs). Flagging as a media-production rule for Phase 4.
9. **Ordering of the 4 pillars on Home / Services hub / About / footer nav**: current order is Google Ads → SEO → Web Development → CRO & Automation. This is repeated across Tranche 1 pages. If you want to reorder (e.g., lead with Web Development to match Vraj's actual career origin story), flag now — reordering after Tranche 3 becomes expensive because cluster articles and location pages will use this ordering.
10. **Booking / scheduling integration**: no Calendly / Cal.com / scheduling embed included in any pillar page. Current CTA pattern is form → 24-hour reply → schedule call in the reply. If you want a direct scheduling embed on the pillar pages (adds friction reduction but pins a call time before discovery), flag for Phase 4.

---

*End of Tranche 2. Awaiting review and approval or corrections before starting Tranche 3 (content pillars + Tier 1 cluster content — the largest tranche of the project, ~37 pages including GEO topics T45–T49 spec'd first per your instruction).*
