# Blueprint — Tranche 3: Content Pillars + Tier 1 Cluster Content

*Phase 2 blueprint · vrajvithalani.com · Tranche 3 of 7 · Covers 4 content pillar pages + 34 cluster pieces (30 Tier 1 + 3 additions T127/T128/T129 + T49 pulled forward from Tier 2 per user's "T45–T49 first" instruction for the closing GEO window). 38 pages total.*

*Ordering inside this tranche per user instruction:*
1. *Phase 1b addendum defining T127, T128, T129 (Phase 1b did not spec them)*
2. *Site-wide Learn-content standards (author byline, EEAT template, GEO structure template — applies to every cluster and pillar entry below)*
3. *4 content pillar pages (Pages 14–17)*
4. *GEO cluster content FIRST — T45, T46, T47, T48, T49 (Pages 18–22)*
5. *T127, T128, T129 (Pages 23–25 — GEO-adjacent, logically grouped)*
6. *Remaining Tier 1 clusters in T# order (Pages 26–51)*

*Site-Wide Standards, Person schema, and LocalBusiness schema reference blocks live in Tranche 1 and apply here. Service pillar internal-link targets live in Tranche 2.*

---

## Phase 1b addendum — T127, T128, T129 specification

Cowork surfaced these three during Phase 1b SERP research; user approved them for blueprint entry. Phase 1b did not spec primary keyword, variants, intent, difficulty, or angle — done here so they can be blueprinted below.

### T127 — AI Overviews for local service businesses · Guide · SEO pillar (Zone 2.6 GEO)

Primary: `ai overviews local service business`
Variants: how to appear in google ai overviews · ai overviews for local seo · google ai overviews local business · ai overviews small business
Intent: Informational · Difficulty: Low-Medium · **Tier: T1 (new)**
SERP: Very thin at the local-service intersection — AI Overviews content is dominated by general SEO takes; the local-business-specific angle is empty. Real break-in slot.
Angle: What actually surfaces a local service business inside AI Overviews — GBP signals, entity clarity, review velocity, structured citations. Grounded in the 3-city location page work Vraj is deploying on this site.

### T128 — Bing indexing and its role in ChatGPT visibility · Guide · SEO pillar (Zone 2.6 GEO)

Primary: `bing indexing chatgpt visibility`
Variants: how to get indexed on bing for chatgpt · bing webmaster tools for llm · chatgpt search index bing · appear in chatgpt via bing
Intent: Informational · Difficulty: Low · **Tier: T1 (new)**
SERP: Emerging — one or two Mersel/StackMatix pieces cover the connection but nobody has a step-by-step "here's the Bing Webmaster setup and here's what ChatGPT actually pulls." Empty slot.
Angle: The concrete Bing Webmaster + IndexNow + sitemap setup, then the observed evidence of what ChatGPT actually retrieves from Bing's index vs Google's, with Vraj's own site as the working example.

### T129 — GBP posting frequency and engagement in 2026 · Guide · SEO pillar (Zone 2.5 Local SEO)

Primary: `gbp posting frequency 2026`
Variants: google business profile posts how often · gbp post engagement 2026 · gbp posts still work · gbp posting strategy 2026
Intent: Informational · Difficulty: Low-Medium · **Tier: T1 (new)**
SERP: Whitespark, Sterling Sky have this; still tactical enough that 2026-fresh answers rank. Freshness matters — Google has changed GBP post display rules multiple times.
Angle: The honest 2026 answer — GBP posts still matter, but not for the reason most guides say. Actual ranking-signal impact vs engagement-only, tested on Vraj's own GBP for the 3-city profiles.

---

## Site-wide Learn-content standards (applies to every pillar and cluster entry below)

Rather than repeating on every entry, these are locked defaults for all Learn content. Individual entries override only where specifically noted.

### Author byline block (top of every Learn article)

Circular headshot · "Vraj Vithalani — [role]" · publish date · last-updated date · reading time · linked "About the author →" to `/about/`.

### EEAT scaffolding (every Learn article)

- Author byline block (top)
- Author bio card (bottom) — headshot + 60-word bio + credentials line + link to `/about/` and to service pillar
- Published date + last-updated date visible top and bottom
- First-person "In my client work..." or "What I ship for clients..." block (mid-article) — the EEAT gold
- Real client / project references where credible (Powercable, drvishva, Vitthalshringar, VM Graphite, Trust NGO, etc.)
- Real data anchors — INR budgets, real percentages, real timelines
- Registration and qualification citations where relevant
- No AI-generated content declaration (in author bio card footer)
- Related articles block (2–3 siblings) at bottom for lateral internal linking

### GEO / AI-search structure (every Learn article)

- **Short-answer block** (60–80 words) at top, boxed visually — third-person, entity-loaded, LLM-extractable
- Table of contents with jump links (client-side, no JS required — anchor links)
- H2 questions phrased as natural queries where possible (matches how people prompt LLMs)
- FAQ block near bottom (5–10 items) with FAQPage schema
- Semantic HTML5 landmarks (`article`, `section` per H2)
- Author + published + updated dates in visible byline AND in Article schema `datePublished` / `dateModified`

### Schema pattern (every Learn cluster article)

- **Article** or **BlogPosting** (author = Person from Reference Block, publisher = Organization, mainEntityOfPage = self)
- **FAQPage** (from on-page FAQ section)
- **BreadcrumbList** (Home → Learn → [Pillar] → [Article])
- **Person** and **Organization** (site-wide)

Pillar pages use **CollectionPage** + **ItemList** (of cluster articles) in place of Article schema.

### CTA pattern (every Learn cluster article)

- Soft CTA at bottom → relevant service pillar (NOT to `/contact/` per critical rule 9)
- Author bio card at bottom with secondary link to service pillar
- No embedded contact form on cluster content
- Floating WhatsApp button (site-wide)

### Word count guardrails (Tier 1 clusters)

- 2,500–4,500 words range depending on scope
- Definitions and short-tactical pieces at the lower end (2,500–3,000)
- Comprehensive guides and frameworks at the upper end (3,500–4,500)
- Pillar pages: 5,000+ words

### Media pattern (every Learn cluster article)

- Hero illustration or diagram (soft-teal accents, glassmorphism-friendly)
- Author photo in byline
- Diagram / table / screenshot for at least one major H2 (varies by topic)
- OG image: article-specific 1200×630
- All images WebP + AVIF, `loading="lazy"` below fold, explicit width/height

---

## Page 14 — Content pillar: /learn/google-ads/

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/` |
| **Page type** | Content pillar (topical authority hub + index of Google Ads cluster content) |
| **Primary keyword** | `google ads guide india` |
| **Secondary keywords** | google ads for small business india · google ads tutorial india · learn google ads india · google ads strategy small business · performance max guide india |
| **Search intent** | Informational + Educational (research-mode users learning Google Ads) |
| **H1** | Google Ads — The Working Playbook for Indian SMBs |
| **Meta title** | Google Ads Guides & Playbook by Vraj Vithalani, India *(53 chars)* |
| **Meta description** | In-depth Google Ads guides, audits, and playbooks written from real client campaigns across Indian service businesses, D2C brands, exporters, and coaching. *(159 chars)* |
| **Content format** | Long-form content pillar — authoritative resource + index of cluster articles (~90% resource / ~10% pitch, opposite balance to service pillar) |
| **Word count target** | 5,000–7,000 |

### Content structure

- H1 — Google Ads — The Working Playbook for Indian SMBs
- Author byline block
- **Short-answer block** (60–80 words) — LLM extraction target
- Table of contents (jump links)
- H2 — Who this playbook is for (SMB owners, D2C founders, exporters, consultants — not enterprise media buyers)
- H2 — Start here: the honest state of Google Ads for Indian SMBs in 2026 (context + trends — AI Overviews on ads, PMax adoption, INR CPC realities)
- H2 — Foundation before you launch anything
  - H3 — Account structure that matches a service business (link to T1 cluster)
  - H3 — Minimum tracking stack you must have working (link to T3 cluster)
  - H3 — Choosing between Search, PMax, and Display (link to T2 cluster — Tranche 6)
- H2 — Running Search campaigns for local service businesses
  - H3 — Match-type strategy in 2026 (link to T9 cluster — Tranche 6)
  - H3 — Negative-keyword lists (link to T10 cluster — Tranche 6)
  - H3 — Ad copy that converts when you can't compete on price (link to T11 cluster — Tranche 6)
- H2 — Performance Max without a full creative team
  - H3 — Structuring PMax when you're solo (link to T5 cluster)
  - H3 — Asset-group strategy for service businesses (link to T6 cluster — Tranche 6)
  - H3 — When PMax is the wrong choice (link to T7 cluster — Tranche 7)
- H2 — Landing page + campaign integration (the compound skill)
  - H3 — Why your campaign underperforms even when the ads are fine (link to T13)
  - H3 — Landing page elements Google Ads actually rewards (link to T14)
  - H3 — WordPress vs Next.js for Ads landing pages (link to T15 — Tranche 6)
- H2 — Diagnosing underperforming campaigns
  - H3 — The 12-point audit I run (link to T17)
  - H3 — Ads vs offer vs landing page (link to T18 — Tranche 6)
  - H3 — Reading the search-terms report (link to T19 — Tranche 6)
- H2 — Budget realities for Indian SMBs
  - H3 — The minimum budget that actually works (link to T21)
  - H3 — Running a real ₹15k/month test (link to T22)
- H2 — Meta Ads as a secondary channel
  - H3 — When Instant Forms beat landing pages (link to T24 — Tranche 6)
  - H3 — Meta Ads for local service businesses (link to T25)
- H2 — Vertical-specific playbooks
  - H3 — Google Ads for industrial exporters (link to T89)
  - H3 — Google Ads for coaching institutes (link to T81 — Tranche 6)
  - H3 — Google Ads for a small Indian D2C brand launching cold (link to T85 — Tranche 6)
- H2 — All Google Ads articles on this site (index — every cluster article, grouped by sub-topic)
- H2 — Working with me on your Google Ads (soft pitch — 200 words, link to `/services/google-ads/`)
- H2 — Frequently asked questions about Google Ads (10 items with FAQ schema)
- H2 — Related pillars (links to other 3 Learn pillars + `/services/google-ads/`)
- Author bio card

### Internal links OUT

- Every Google Ads Learn cluster article (Tranches 3, 6, 7 populate this list)
- `/services/google-ads/` (upsell path — soft pitch section)
- Other 3 Learn pillars (`/learn/seo/`, `/learn/web-development/`, `/learn/cro-and-automation/`)
- `/learn/` (breadcrumb parent)
- `/case-studies/powercable/`, `/case-studies/parv-travels/`, `/case-studies/synergy-tutorials/` (in-context proof links)
- `/about/` (author bio)

### Internal links IN

- `/learn/` hub (from the 4-pillar tile)
- `/services/google-ads/` (from "Related guides" section, cluster upsell)
- Every Google Ads cluster article (upward pillar link — mandatory per Doc 03)
- Home page (via nav)
- Header + footer nav

### Schema markup required

- **CollectionPage** (this page is a collection of cluster articles)
- **ItemList** (ordered list of all Google Ads cluster articles, with position numbers)
- **BreadcrumbList** (Home → Learn → Google Ads)
- **FAQPage** (10 pillar-level FAQs)
- **Person** and **Organization** (site-wide)

### EEAT elements required

- Author byline top + author bio card bottom
- First-person opening H2 ("Who this playbook is for") — sets voice
- Real client references (Powercable, Parv Travels, Synergy Tutorials, VM Graphite) named in-context
- Real INR anchors in budget-related H2s
- Certifications visible in author bio card
- Reference to hands-on experience: "Every cluster article below is written from a real campaign I've run or an account I've audited."

### CTA specification

- Soft "Working with me" section ~10% weight (not 60/40 like Service pillars — Learn pillar is 90/10 resource/pitch)
- One link to `/services/google-ads/` from soft-pitch H2
- Author bio card links to `/about/` + `/services/google-ads/`
- Floating WhatsApp button (site-wide)
- No embedded contact form on Learn pillar

### Media requirements

- Hero illustration: stylised "Google Ads playbook" visual (funnel + dashboard + INR anchor) — soft-teal
- Section-divider icons for each major H2 (SVG)
- Article-card thumbnails for the article-index section
- Author bio card (headshot)
- OG image: pillar-specific 1200×630

### Notes

- **Pillar page weighting is 90% resource / 10% pitch** (opposite of Service pillar's 60/40). Ranks informationally and hosts cluster content; service pillar handles commercial intent.
- **This page is the topical authority hub for Google Ads.** Every cluster article links up here; this page links down to every cluster (index at bottom).
- **Grouping H2s by sub-topic** (foundation, search, PMax, landing page, diagnosis, budget, Meta, vertical) mirrors Phase 1a Zone 1 structure — makes the sub-territory boundaries visible to both readers and LLMs.
- **Cluster links use the (Tranche N)** annotation only in this blueprint document — final published page has clean links only.
- **T2, T4, T6, T15, T24 etc. are Tier 2** — they will exist by the time this pillar is finalized in Tranche 6; the pillar page publishes with links to Tier 1 clusters at launch and gets updated as Tier 2 clusters ship.
- **FAQ answers include "Contact for quote"** at least once — locked rule.
- **The "Who this playbook is for"** opening H2 explicitly excludes enterprise media buyers — sharpens the audience and matches the silent SMB angle.

## Page 15 — Content pillar: /learn/seo/

| Field | Value |
|---|---|
| **URL** | `/learn/seo/` |
| **Page type** | Content pillar (topical authority hub for SEO + GEO) |
| **Primary keyword** | `seo guide india` |
| **Secondary keywords** | seo for small business india · technical seo india · local seo india · generative engine optimization guide · seo and geo india · llm search optimization india |
| **Search intent** | Informational + Educational |
| **H1** | SEO & GEO — The Playbook for Ranking in Google and AI Search |
| **Meta title** | SEO & GEO Playbook — Guides by Vraj Vithalani, India *(51 chars)* |
| **Meta description** | In-depth SEO and Generative Engine Optimization guides for Indian businesses ranking in Google, ChatGPT, Perplexity, and Google AI Mode. From real client work. *(160 chars)* |
| **Content format** | Long-form content pillar — 90% resource / 10% pitch |
| **Word count target** | 5,000–7,000 |

### Content structure

- H1 — SEO & GEO — The Playbook for Ranking in Google and AI Search
- Author byline block
- **Short-answer block** (60–80 words)
- Table of contents
- H2 — Who this playbook is for
- H2 — The 2026 state of SEO — and why GEO is now inseparable from it
- H2 — Technical SEO foundations
  - H3 — WordPress technical audit checklist (link to T26)
  - H3 — Fixing indexation problems on WordPress (link to T27)
  - H3 — Next.js SEO — SSR vs SSG vs ISR (link to T28 — Tranche 7)
  - H3 — Debugging GSC coverage errors (link to T29 — Tranche 7)
- H2 — On-page SEO and content structure
  - H3 — Heading hierarchy that readers and crawlers parse (link to T30 — Tranche 6)
  - H3 — Meta titles surviving Google's rewrite (link to T31 — Tranche 7)
  - H3 — Content structure for snippet + AI answer era (link to T32 — Tranche 6)
- H2 — Schema markup implementation
  - H3 — Schema types every service-business site needs (link to T34)
  - H3 — FAQPage schema without a plugin (link to T35 — Tranche 6)
  - H3 — Person schema for personal brands (link to T36 — Tranche 6)
- H2 — Site architecture and internal linking
  - H3 — Hub-and-spoke architecture (link to T38)
  - H3 — URL structure decisions to lock at launch (link to T39 — Tranche 6)
- H2 — Local SEO for Indian cities
  - H3 — GBP for a solo service business (link to T41)
  - H3 — Location page content that isn't a doorway page (link to T43)
  - H3 — Indian local citation strategy — honest version (link to T42 — Tranche 6)
  - H3 — Getting reviews from Indian clients (link to T44 — Tranche 6)
  - H3 — GBP posting frequency in 2026 (link to T129)
- H2 — Generative Engine Optimization (GEO / AI search)
  - H3 — What GEO actually is (link to T45)
  - H3 — Short-answer block for LLM extraction (link to T46)
  - H3 — Appear in ChatGPT, Perplexity, and AI Mode (link to T47)
  - H3 — Entity establishment in the LLM era (link to T48)
  - H3 — Auditing your site for LLM extraction (link to T49)
  - H3 — AI Overviews for local service businesses (link to T127)
  - H3 — Bing indexing and ChatGPT visibility (link to T128)
- H2 — Vertical-specific SEO
  - H3 — SEO for B2B manufacturing India → overseas (link to T90)
  - H3 — SEO for coaching institutes (link to T82 — Tranche 6)
  - H3 — SEO for D2C on WooCommerce (link to T86 — Tranche 6)
- H2 — All SEO articles on this site (index)
- H2 — Working with me on your SEO or GEO project (soft pitch)
- H2 — Frequently asked questions about SEO and GEO (10 items)
- H2 — Related pillars
- Author bio card

### Internal links OUT

- Every SEO/GEO cluster article (Tranches 3, 6, 7)
- `/services/seo/` (soft pitch section)
- Other 3 Learn pillars
- `/learn/` (breadcrumb parent)
- `/case-studies/drvishva/`, `/case-studies/powercable/`, `/case-studies/vitthalshringar/` (in-context)
- `/about/`

### Internal links IN

- `/learn/` hub
- `/services/seo/` (Related guides section)
- Every SEO cluster article (upward pillar link)
- Home page (via nav)
- Header + footer nav

### Schema markup required

- **CollectionPage** + **ItemList**
- **BreadcrumbList** (Home → Learn → SEO)
- **FAQPage** (10)
- **Person** + **Organization**

### EEAT elements required

- Author byline top + author bio card bottom
- First-person opening
- **The "2026 state of SEO" opening H2** is a fresh, dated, first-person perspective — updated at least quarterly (last-updated date visible)
- Real client references (drvishva, Powercable, Vitthalshringar, VM Graphite) named in-context
- **Meta-move**: reference to vrajvithalani.com itself as the working example of the GEO/entity-reset problem — appears in the GEO H2 intro
- Certifications in author bio card

### CTA specification

- Soft "Working with me" section ~10% weight
- One link to `/services/seo/`
- Author bio card links to `/about/` + `/services/seo/`
- Floating WhatsApp
- No embedded contact form

### Media requirements

- Hero illustration: "Google + AI" split visual (search-result box + ChatGPT-style answer box)
- Section-divider icons for each major H2
- Article-card thumbnails for index section
- Author bio card
- OG image: SEO-pillar 1200×630

### Notes

- **GEO gets a full H2 with 7 sub-topics** — this is the pillar's differentiation moat per Phase 1b's 12–18 month window warning.
- **Local SEO H2 groups T41, T42, T43, T44, T129** — the 5-piece local SEO cluster; makes local dominance visible.
- **Physiotherapy** does NOT appear as a vertical H2 (Doc 02 rule — no physio Learn content). Drvishva referenced only as a case study in context.
- **T28, T29, T30, T31, T32, T33, T35, T36, T39, T40, T42, T44, T82, T86** are Tier 2 or Tier 3 — populated in Tranches 6 and 7 respectively; pillar publishes at launch with Tier 1 links, updated as later tiers ship.
- **FAQ answers include "Contact for quote"** at least once.
- **This site as working example** stated explicitly in the GEO H2 intro.

## Page 16 — Content pillar: /learn/web-development/

| Field | Value |
|---|---|
| **URL** | `/learn/web-development/` |
| **Page type** | Content pillar (topical authority hub for web development) |
| **Primary keyword** | `web development guide india` |
| **Secondary keywords** | wordpress guide india · nextjs guide india · hostinger deployment guide · razorpay integration guide · web development for indian small business |
| **Search intent** | Informational + Educational |
| **H1** | Web Development — The Working Playbook for Indian SMB Sites |
| **Meta title** | Web Development Playbook — WordPress, Next.js, Node by Vraj *(60 chars)* |
| **Meta description** | In-depth guides on WordPress, Next.js, Node.js, Razorpay, Hostinger, and site security for Indian service businesses, D2C brands, exporters, and NGOs. *(154 chars)* |
| **Content format** | Long-form content pillar — 90% resource / 10% pitch |
| **Word count target** | 5,000–7,000 |

### Content structure

- H1 — Web Development — The Working Playbook for Indian SMB Sites
- Author byline block
- **Short-answer block** (60–80 words)
- Table of contents
- H2 — Who this playbook is for
- H2 — Choosing your stack in 2026 — WordPress vs Next.js vs custom (context section)
- H2 — WordPress for service businesses
  - H3 — Fast WordPress on shared hosting (link to T51 — merged with T63)
  - H3 — WordPress theme choice — page builder vs block theme (context — T50 cut; the insight lives inside T51 per Phase 1b consolidation)
  - H3 — Migrating from Wix / GoDaddy to WordPress (link to T52 — Tranche 7)
- H2 — Next.js for personal brands and service businesses
  - H3 — When Next.js beats WordPress (link to T53 — Tranche 6)
  - H3 — Building a Next.js personal-brand site for Google + LLMs (link to T54)
  - H3 — Hosting Next.js — Hostinger vs Vercel vs Cloudflare (link to T55 — Tranche 6)
- H2 — Backend and custom builds
  - H3 — Deploying Node.js on Hostinger Managed Cloud (link to T56 — Tranche 6)
  - H3 — When to build a custom CMS (link to T67 — Tranche 7)
- H2 — Hostinger deployment specifics
  - H3 — WordPress on Hostinger — performance settings that matter (link to T57 — Tranche 7)
  - H3 — What Hostinger's plans actually support (link to T58 — Tranche 7)
- H2 — Razorpay and Indian payment integration
  - H3 — Razorpay checkout on WordPress the right way (link to T59)
  - H3 — Razorpay vs Cashfree vs PayU (link to T60 — Tranche 6)
  - H3 — GST and invoicing compliance (link to T61 — Tranche 7)
- H2 — Site security, speed, and health
  - H3 — WordFence + 2FA hardening (link to T62)
  - H3 — Recovering a hacked WordPress site (link to T64 — Tranche 7)
  - H3 — Backup and disaster recovery for solo owners (link to T65 — Tranche 7)
- H2 — E-commerce and CMS decisions
  - H3 — Shopify vs WooCommerce for Indian D2C (link to T66 — merged with T87)
  - H3 — E-commerce launch checklist India (link to T68 — Tranche 7)
- H2 — Building for LLM citation
  - H3 — Next.js site engineered for LLM citation (link to T117)
- H2 — Vertical-specific website work
  - H3 — Website structure for an exporter (link to T91 — Tranche 6)
  - H3 — Website essentials for a small Indian NGO (link to T94 — Tranche 7)
  - H3 — Custom donation / beneficiary CMS for NGO (link to T95 — Tranche 7)
- H2 — All web development articles on this site (index)
- H2 — Working with me on your web development project (soft pitch)
- H2 — Frequently asked questions about web development (10 items)
- H2 — Related pillars
- Author bio card

### Internal links OUT

- Every Web Dev cluster article (Tranches 3, 6, 7)
- `/services/web-development/` (soft pitch section)
- Other 3 Learn pillars
- `/learn/` (breadcrumb parent)
- `/case-studies/powercable/`, `/case-studies/drvishva/`, `/case-studies/vitthalshringar/`, `/case-studies/trust-ngo/`, `/case-studies/dreams-astro/`, `/case-studies/iota-anpr/` (in-context, overview-only for IOTA)
- `/about/`

### Internal links IN

- `/learn/` hub
- `/services/web-development/` (Related guides section)
- Every Web Dev cluster article (upward pillar link)
- Home page (via nav)
- Header + footer nav

### Schema markup required

- **CollectionPage** + **ItemList**
- **BreadcrumbList** (Home → Learn → Web Development)
- **FAQPage** (10)
- **Person** + **Organization**

### EEAT elements required

- Author byline top + author bio card bottom
- First-person opening
- Real project references — Powercable (WordPress, ~40 days), drvishva (Next.js), Vitthalshringar (WooCommerce), Trust NGO (custom CMS), Dreams Astro (Razorpay + courses)
- IOTA ANPR referenced overview-only (no implementation details per Doc 02)
- Certifications in author bio card

### CTA specification

- Soft "Working with me" section ~10% weight
- One link to `/services/web-development/`
- Author bio card links to `/about/` + `/services/web-development/`
- Floating WhatsApp
- No embedded contact form

### Media requirements

- Hero illustration: "WordPress + Next.js + Node" split visual with soft-teal accents
- Section-divider icons for major H2s
- Article-card thumbnails for index section
- Author bio card
- OG image: Web-Dev-pillar 1200×630

### Notes

- **T50 (WP theme choice) was cut in Phase 1b** — insight is folded into T51 per Phase 1b consolidation. Referenced above as context, no standalone link.
- **T51+T63 merged** into a single entry at T51 (Tranche 6) per user instruction. Covers plugins + server-level speed together.
- **T66+T87 merged** into a single entry at T66 (Tranche 6) per user instruction. Combined platform-first + founder-first framing.
- **IOTA ANPR case study** referenced overview-only; no standalone Learn content on ANPR (Zone 7.1 topics T106–T108 are Tier 3, in Tranche 7).
- **Custom CMS for NGO (T95)** and **Website essentials for NGO (T94)** — the `[VERIFY]` flag was lifted by user; they'll be published as Trust project delivery matures.
- **FAQ answers include "Contact for quote"** at least once.
- **Physiotherapy handled**: drvishva referenced as a Next.js build example only, not as a physiotherapy vertical.

## Page 17 — Content pillar: /learn/cro-and-automation/

| Field | Value |
|---|---|
| **URL** | `/learn/cro-and-automation/` |
| **Page type** | Content pillar (topical authority hub for CRO + Automation) |
| **Primary keyword** | `cro guide india` |
| **Secondary keywords** | conversion rate optimization guide india · ga4 setup guide india · whatsapp automation for business india · gtm guide india · landing page optimization india |
| **Search intent** | Informational + Educational |
| **H1** | CRO & Automation — The Working Playbook for Indian SMB Funnels |
| **Meta title** | CRO & Automation Playbook — Guides by Vraj Vithalani *(51 chars)* |
| **Meta description** | In-depth CRO, GA4, GTM, WhatsApp automation, and funnel design guides for Indian service businesses and D2C brands. From real client work, honest angles. *(155 chars)* |
| **Content format** | Long-form content pillar — 90% resource / 10% pitch |
| **Word count target** | 5,000–7,000 |

### Content structure

- H1 — CRO & Automation — The Working Playbook for Indian SMB Funnels
- Author byline block
- **Short-answer block** (60–80 words)
- Table of contents
- H2 — Who this playbook is for
- H2 — The SMB reality of CRO — why enterprise A/B testing frameworks don't apply
- H2 — Landing page conversion optimization
  - H3 — The 8-element service-business landing page checklist (link to T69)
  - H3 — Form length and field choices (link to T70 — Tranche 7)
  - H3 — Trust signals with no big-brand logos (link to T71 — Tranche 7)
- H2 — Analytics setup for SMBs
  - H3 — GA4 events that matter for a service business (link to T72 — Tranche 6)
  - H3 — Google Tag Manager for non-developers (link to T73 — Tranche 6)
  - H3 — Debugging GA4 vs Google Ads mismatches (link to T74 — Tranche 7)
- H2 — WhatsApp and lead-capture automation
  - H3 — WhatsApp-first lead-capture funnel (link to T76)
  - H3 — WhatsApp Business API vs App (link to T75 — Tranche 6)
  - H3 — Routing form submissions to WhatsApp + email + CRM (link to T77 — Tranche 7)
- H2 — Funnel design and email automation
  - H3 — Funnel design for a 2–8 week sales cycle (link to T78 — Tranche 7)
  - H3 — Minimum-viable email automation stack India (link to T79 — Tranche 7)
  - H3 — Nurture sequences for high-consideration services (link to T80 — Tranche 7)
- H2 — Cross-zone compounding topics
  - H3 — Landing page speed × Quality Score × SEO (link to T112)
  - H3 — Meta Instant Forms vs landing page (link to T24 — Tranche 6)
- H2 — Vertical-specific CRO
  - H3 — Landing pages for coaching-institute enrolment (link to T83 — Tranche 7)
  - H3 — Product-page CRO checklist for Shopify / WooCommerce (link to T88 — Tranche 7)
  - H3 — Lead qualification flow for industrial-exporter inquiries (link to T92 — Tranche 7)
  - H3 — Fundraising landing pages for individual donors (link to T96 — Tranche 7)
- H2 — All CRO & Automation articles on this site (index)
- H2 — Working with me on your CRO project (soft pitch)
- H2 — Frequently asked questions about CRO and automation (10 items)
- H2 — Related pillars
- Author bio card

### Internal links OUT

- Every CRO/Automation cluster article (Tranches 3, 6, 7)
- `/services/cro-and-automation/` (soft pitch section)
- Other 3 Learn pillars
- `/learn/` (breadcrumb parent)
- `/case-studies/powercable/`, `/case-studies/vitthalshringar/`, `/case-studies/drvishva/`, `/case-studies/parv-travels/`, `/case-studies/little-genius/` (in-context)
- `/about/`

### Internal links IN

- `/learn/` hub
- `/services/cro-and-automation/` (Related guides section)
- Every CRO cluster article (upward pillar link)
- Home page (via nav)
- Header + footer nav

### Schema markup required

- **CollectionPage** + **ItemList**
- **BreadcrumbList** (Home → Learn → CRO & Automation)
- **FAQPage** (10)
- **Person** + **Organization**

### EEAT elements required

- Author byline top + author bio card bottom
- First-person opening — this is where the "SMB reality" angle voice is loudest
- Real project references — Powercable (form + tracking), Vitthalshringar (checkout), drvishva (funnel), Parv Travels (Instant Forms), Little Genius (10x lift)
- Real tools named specifically (FluentForms, AiSensy, Brevo, GTM, Looker Studio)
- Certifications in author bio card

### CTA specification

- Soft "Working with me" section ~10% weight
- One link to `/services/cro-and-automation/`
- Author bio card links to `/about/` + `/services/cro-and-automation/`
- Floating WhatsApp
- No embedded contact form

### Media requirements

- Hero illustration: funnel visualisation with WhatsApp handoff — soft-teal accents
- Section-divider icons for major H2s
- Article-card thumbnails for index section
- Author bio card
- OG image: CRO-pillar 1200×630

### Notes

- **T112 (Landing page speed × QS × SEO)** filed here per Phase 1b's compound-topic assignment even though it also touches Google Ads and SEO — cross-links from all three pillars.
- **T24 (Meta Instant Forms vs landing page)** filed under CRO pillar even though topically Google Ads adjacent — cross-links.
- **Physiotherapy** referenced only as a case study (drvishva as one of several client examples). No physio-vertical CRO content.
- **NGO topics (T96)** — `[VERIFY]` lifted by user; publishes as Trust project matures.
- **FAQ answers include "Contact for quote"** at least once.
- **The "SMB reality" H2** is the ownable angle — explicitly names the enterprise-CRO assumptions that don't hold and describes what actually works instead.

# GEO cluster content (spec'd FIRST — the closing window)

## Page 18 — T45: What is GEO

| Field | Value |
|---|---|
| **URL** | `/learn/seo/what-is-generative-engine-optimization/` |
| **Page type** | Cluster content — definition + framework |
| **Primary keyword** | `what is generative engine optimization` |
| **Secondary keywords** | geo vs seo · generative engine optimization definition · what is aeo · geo meaning seo |
| **Search intent** | Informational (top of funnel, definition-seekers) |
| **H1** | What GEO Actually Is — And How It Differs From SEO |
| **Meta title** | What Is Generative Engine Optimization (GEO)? — Vraj Vithalani *(62 chars — trim: What Is Generative Engine Optimization? — Vraj Vithalani = 59 chars)* |
| **Meta description** | Generative Engine Optimization (GEO) explained — the exact overlap with traditional SEO and the 20% that's genuinely new for AI search in 2026. *(146 chars → expand: ... 2026, from a practitioner applying it live.)* *(155 chars)* |
| **Content format** | Definition + framework (medium-length definitive answer) |
| **Word count target** | 2,500–3,000 |
| **CTA** | Soft link at bottom → `/services/seo/` |

### Content structure

- H1
- Author byline block
- **Short-answer block** (60–80 words defining GEO in one paragraph)
- Table of contents
- H2 — GEO in one sentence
- H2 — Why the term exists (the AI-search shift 2023 → 2026)
- H2 — GEO vs SEO — where they overlap
- H2 — GEO vs SEO — where they diverge (the 20% that's genuinely new)
  - H3 — Content structure for extraction, not just crawling
  - H3 — Entity clarity across the web (not just on-site)
  - H3 — Answer-first content patterns
  - H3 — LLM training-data authority vs live-search authority
- H2 — What GEO is NOT (myths — LLM optimization ≠ keyword stuffing, ≠ hidden text, ≠ new schema types)
- H2 — The current LLMs that matter for Indian businesses (ChatGPT, Perplexity, Google AI Mode, Claude, Gemini — brief on each's retrieval source)
- H2 — In my client work — the first GEO changes I make on any site (first-person block)
- H2 — Where to go next (2 sibling links — T46 short-answer block, T47 how to appear)
- H2 — Frequently asked questions (7 items with FAQ schema)
- Author bio card

### Internal links OUT

- `/learn/seo/short-answer-block-llm-extraction/` (T46)
- `/learn/seo/appear-in-chatgpt-perplexity-ai-mode/` (T47)
- `/learn/seo/entity-establishment-llm-era/` (T48)
- `/learn/seo/llm-content-audit-website/` (T49)
- `/learn/seo/` (pillar)
- `/services/seo/` (soft CTA)
- `/about/` (author bio)

### Internal links IN

- `/learn/seo/` pillar (from GEO H2 section)
- `/services/seo/` (top 6 cluster links)
- Sibling GEO clusters (T46, T47, T48, T49, T127, T128) — lateral links
- Home page ("recent articles" section — this is likely the first published GEO piece)

### Schema markup required

- **Article** (author = Vraj, publisher = Organization, datePublished, dateModified, mainEntityOfPage)
- **FAQPage** (7 FAQ items)
- **BreadcrumbList** (Home → Learn → SEO → Article)
- **DefinedTerm** (optional — for the "GEO" definition itself, tied to the short-answer block)

### EEAT elements required

- Full byline top + author bio card bottom
- Published + updated dates visible
- First-person "In my client work" block (mid-article)
- Reference to vrajvithalani.com as working example — "The site you're reading this on is being built as a live GEO experiment. I'll link out to the audit and results as they publish."
- Real named LLMs in the "current LLMs" H2 (ChatGPT, Perplexity, Claude, Gemini, Google AI Mode) — this is entity signal density
- No AI-generated content declaration in author bio card footer

### Media requirements

- Hero illustration: split visual — "SEO (blue search box)" vs "GEO (AI answer box)" — soft-teal accents
- Overlap diagram (Venn — SEO ⊃ GEO for the 80%, unique GEO for the 20%)
- Screenshot examples of a Google AI Overview + a ChatGPT answer with source citations (real, anonymised if needed)
- Author photo in byline
- OG image: 1200×630 with "What is GEO?" headline

### Notes

- **This is likely the highest-value single GEO article on the site** — publishes early, ranks for the definitional query, feeds every other GEO piece as the referenced definition source.
- **Short-answer block is critical** — this article ranks for a definitional query and must give the answer in the first 100 words.
- **Meta-move**: this site as working example is stated explicitly — the article makes the vrajvithalani.com repositioning visible.
- **FAQ answers include "Contact for quote"** at least once (in the "Do you offer GEO consulting?" answer).
- **Word count deliberately at the middle of the range** — the topic is definitional, not exhaustive; over-writing dilutes ranking value.

---

## Page 19 — T46: Short-answer block for LLM extraction

| Field | Value |
|---|---|
| **URL** | `/learn/seo/short-answer-block-llm-extraction/` |
| **Page type** | Cluster content — framework + template |
| **Primary keyword** | `short answer block seo llm` |
| **Secondary keywords** | content structure for ai · aeo content template · llm-friendly content structure · answer block for chatgpt |
| **Search intent** | Informational (practitioners looking for a concrete template) |
| **H1** | The Short-Answer Block — The Content Pattern LLMs Actually Extract |
| **Meta title** | Short-Answer Block for LLM Extraction — Vraj Vithalani *(55 chars)* |
| **Meta description** | The exact short-answer block template LLMs pull into ChatGPT, Perplexity, and Google AI Overviews, with 3 real examples from live indexed pages. *(148 chars → expand)* |
| **Content format** | Framework + copyable template |
| **Word count target** | 2,500–3,000 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1
- Author byline block
- **Short-answer block** — meta-example: this article's own short-answer block is a live demonstration of the pattern being taught
- Table of contents
- H2 — What a short-answer block is
- H2 — Why LLMs prefer this pattern (extraction mechanics — how retrieval indexes segment content)
- H2 — The exact template (60–80 words, third person, entity-loaded, factually complete)
- H2 — 3 real examples from live indexed pages (from vrajvithalani.com Home, /about/, and one Learn cluster)
- H2 — Where to place the short-answer block (above the fold on mobile; after H1 and hero paragraph; boxed visually with distinct background)
- H2 — Common mistakes (first-person voice, keyword stuffing, hiding it in a collapsed FAQ, placing below the fold)
- H2 — Short-answer block for different page types (home, service pillar, cluster article, case study — one paragraph each)
- H2 — How to test whether yours is working (feed the URL to ChatGPT / Perplexity + check AI Overview appearance)
- H2 — Frequently asked questions (6 items)
- Author bio card

### Internal links OUT

- `/learn/seo/what-is-generative-engine-optimization/` (T45)
- `/learn/seo/appear-in-chatgpt-perplexity-ai-mode/` (T47)
- `/learn/seo/llm-content-audit-website/` (T49)
- `/learn/seo/` (pillar)
- `/services/seo/` (soft CTA)
- `/about/`

### Internal links IN

- `/learn/seo/` pillar (top 6)
- `/services/seo/` (top 6)
- Sibling GEO clusters
- Every future GEO cluster piece (lateral)

### Schema markup required

- **Article** + **FAQPage** + **BreadcrumbList** + **Person**/**Organization**
- **HowTo** (optional — the template application is procedural)

### EEAT elements required

- Byline + bio card
- Published + updated dates
- First-person block — "In the last 6 months I've refined this pattern across every page on this site"
- 3 real (screenshot + linked) examples from the same site the visitor is on
- Meta demonstration: the article's own short-answer block IS the pattern

### Media requirements

- 3 annotated screenshots of live short-answer blocks (from Home, About, another cluster piece)
- One diagram: the block's anatomy (heading → block boundary → entity-loaded sentence 1 → entity-loaded sentence 2 → closing entity phrase)
- Author photo
- OG image with "Short-Answer Block Template" headline

### Notes

- **Meta demonstration** is the strongest single EEAT play in the whole tranche — the article's own top block is the taught pattern.
- **Copyable template** is the CTA-substitute; drives shares and citations.
- **Screenshots** must be live URLs on the same site so any LLM can retrieve and verify.
- **FAQ answers include "Contact for quote"** at least once.

---

## Page 20 — T47: How to appear in ChatGPT, Perplexity, and Google AI Mode

| Field | Value |
|---|---|
| **URL** | `/learn/seo/appear-in-chatgpt-perplexity-ai-mode/` |
| **Page type** | Cluster content — comprehensive framework + tactical guide |
| **Primary keyword** | `how to appear in chatgpt search results` |
| **Secondary keywords** | how to rank in perplexity · appear in ai search · llm citation seo · get cited by chatgpt · google ai mode ranking |
| **Search intent** | Informational (high-intent practitioners) |
| **H1** | How to Appear in ChatGPT, Perplexity, and Google AI Mode Responses |
| **Meta title** | Appear in ChatGPT, Perplexity & AI Mode — Vraj Vithalani *(55 chars)* |
| **Meta description** | The 4-part framework for getting cited by ChatGPT, Perplexity, and Google AI Mode in 2026 — entity clarity, off-site authority, answer-first content, schema. *(159 chars)* |
| **Content format** | Comprehensive framework + tactical guide |
| **Word count target** | 3,500–4,500 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1
- Author byline block
- **Short-answer block** (60–80 words summarising the 4-part framework)
- Table of contents
- H2 — Why appear in AI responses at all (traffic + entity + trust rationale)
- H2 — How each LLM actually retrieves in 2026 (short section per — ChatGPT via Bing + own index, Perplexity via multiple sources, Google AI Mode via Google's own index, Claude via web + curated, Gemini via Google index)
- H2 — The 4-part framework
  - H3 — Part 1: Entity clarity (who you are and what you do, unambiguously)
  - H3 — Part 2: Off-site authority (mentions in sources LLMs trust — Wikipedia, Wikidata, GitHub, industry directories, LinkedIn, verified profiles)
  - H3 — Part 3: Answer-first content (short-answer blocks, FAQ patterns, direct-answer H2s)
  - H3 — Part 4: Structured data (Person, Organization, Article, FAQPage schemas — feeding retrieval graphs)
- H2 — The exact technical setup
  - H3 — robots.txt for LLM crawlers (GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot, Google-Extended)
  - H3 — Bing Webmaster Tools + IndexNow (for ChatGPT retrieval)
  - H3 — Person and Organization schema (site-wide JSON-LD)
  - H3 — sameAs verification network across social profiles
- H2 — My own working example — vrajvithalani.com's repositioning problem (first-person 400-word block)
- H2 — How to test — the prompt battery (5 sample prompts to test whether ChatGPT/Perplexity/Claude retrieve you accurately)
- H2 — What doesn't work (myths — hidden text, LLM-specific schema types that don't exist, paying for "AI SEO" services that offer nothing SEO doesn't cover)
- H2 — The 12–18 month window — why this article ages fast
- H2 — Frequently asked questions (8 items)
- Author bio card

### Internal links OUT

- T45, T46, T48, T49, T127, T128 (all GEO siblings)
- `/learn/seo/schema-types-service-business-site/` (T34)
- `/learn/seo/` (pillar)
- `/services/seo/` (soft CTA)
- External refs to Bing Webmaster Tools, IndexNow (external, `rel="noopener"`)

### Internal links IN

- `/learn/seo/` pillar (top 6)
- `/services/seo/` (top 6)
- Sibling GEO clusters
- Case studies (drvishva especially — new site with GEO from launch)

### Schema markup required

- **Article** + **FAQPage** + **BreadcrumbList** + **Person**/**Organization**
- **HowTo** for the technical setup section

### EEAT elements required

- Byline + bio card
- Published + updated dates (update quarterly minimum — LLM retrieval mechanics shift fast)
- **First-person "my own working example" block** is the EEAT gold — 400 words on the physio-misclassification problem and the fix in progress
- Prompt battery = testable, verifiable EEAT
- Real named LLMs, real named tools, real named schemas — entity density

### Media requirements

- Hero illustration: 4-part framework diagram (Entity + Authority + Content + Schema converging on "cited by LLM")
- Diagram of retrieval flow per LLM
- Screenshot of Bing Webmaster Tools setup
- Screenshot of Person schema JSON-LD from this site
- Author photo
- OG image with "Appear in AI Search" headline

### Notes

- **This is the tactical anchor of the GEO cluster.** T45 defines, T46 templates, T47 gives the full playbook, T48 goes deeper on entities, T49 audits.
- **Update cadence quarterly** — flag this in the article itself; the `dateModified` and "last-updated" byline must stay fresh.
- **Bing Webmaster + IndexNow** section overlaps with T128 (Bing indexing + ChatGPT); T47 gives the setup, T128 goes deeper on the ChatGPT retrieval mechanics. Link both ways.
- **Meta-move**: the physio-misclassification example is the standout EEAT play.
- **FAQ answers include "Contact for quote"** at least once.
- **Word count high end of range** — comprehensive guide, cluster of tactics; visitor completes the whole thing.

---

## Page 21 — T48: Entity establishment for a person or business in the LLM era

| Field | Value |
|---|---|
| **URL** | `/learn/seo/entity-establishment-llm-era/` |
| **Page type** | Cluster content — framework + case study |
| **Primary keyword** | `entity establishment seo person` |
| **Secondary keywords** | entity based seo · llm entity signals · knowledge graph optimization person · become an entity google · personal brand entity signals |
| **Search intent** | Informational (advanced SEO / GEO practitioners) |
| **H1** | Entity Establishment — How to Get Google and LLMs to Understand Who You Are |
| **Meta title** | Entity Establishment for Persons in the LLM Era — Vraj *(53 chars)* |
| **Meta description** | How to establish a person or business as a clear entity for Google Knowledge Graph, ChatGPT, Perplexity, and Google AI Mode retrieval in 2026. Working example. *(159 chars)* |
| **Content format** | Framework + case study writeup |
| **Word count target** | 3,000–4,000 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1
- Author byline block
- **Short-answer block** (60–80 words)
- Table of contents
- H2 — What "an entity" actually is (Google's Knowledge Graph + LLM training vs live-retrieval graphs)
- H2 — Why entity establishment matters more in the LLM era (context switch from keyword-matching to entity-resolution)
- H2 — The signal set that moves an individual's LLM classification
  - H3 — Signal 1: Unambiguous name-role pairing across own site (Person schema + consistent copy)
  - H3 — Signal 2: Consistent name-role pairing across every controlled external profile (LinkedIn, Instagram, X, Facebook, GitHub, etc.)
  - H3 — Signal 3: sameAs verification network (cross-linked profiles)
  - H3 — Signal 4: Mentions in independent sources (bylines, guest posts, interviews, podcast credits)
  - H3 — Signal 5: Structured data at the entity level (Person, Organization, hasCredential, alumniOf, knowsAbout)
  - H3 — Signal 6: Wikipedia/Wikidata presence (if achievable — 3–5 year horizon)
- H2 — My own working case study — the physio-misclassification problem (600-word first-person case study)
  - H3 — What the LLMs currently say about me (with screenshots, as of publish date)
  - H3 — Diagnosis — why they're wrong
  - H3 — The signal changes I'm shipping across this site + external profiles
  - H3 — How I'll measure re-classification success
- H2 — What entity establishment looks like for a business (vs a person)
- H2 — Common mistakes (inconsistent name variations, empty Person schema, unverified sameAs, chasing Wikipedia before earning it)
- H2 — Where to go from here (T45 definitional, T47 tactical, T49 audit — sibling links)
- H2 — Frequently asked questions (7 items)
- Author bio card

### Internal links OUT

- T45, T46, T47, T49 (siblings)
- `/learn/seo/schema-types-service-business-site/` (T34)
- `/learn/seo/person-schema-personal-brand-website/` (T36 — Tranche 6)
- `/learn/seo/` (pillar)
- `/services/seo/` (soft CTA)
- `/about/` (referenced as the entity page for this site)

### Internal links IN

- `/learn/seo/` pillar (top 6 GEO)
- `/services/seo/` (top 6)
- Sibling GEO clusters (T45, T46, T47, T49)
- Other GEO clusters (T127, T128)

### Schema markup required

- **Article** + **FAQPage** + **BreadcrumbList** + **Person**/**Organization**
- **Person** on the working-example section (the Vraj entity being described is the same one in site-wide Person schema — check for @id consistency)

### EEAT elements required

- Byline + bio card
- Published + updated dates
- **The physio-misclassification case study is the article's spine** — 600 first-person words with screenshots, dates, and a testable claim ("re-check ChatGPT for 'vraj vithalani' in 90 days and see what changes")
- Screenshots of the current (as of publish) LLM misclassification — dated
- Reference to /about/ as the canonical entity page for this site

### Media requirements

- Hero illustration: "person as entity in a graph" diagram
- Screenshot: current ChatGPT response for "who is vraj vithalani" — dated
- Screenshot: current Perplexity response — dated
- Screenshot: current Google AI Mode response — dated
- Diagram of the 6-signal set
- Author photo
- OG image

### Notes

- **This is the article the physio-misclassification problem was made to feed.** The candour is the moat — nobody else can write it with the same first-person truthfulness.
- **Dated screenshots** are load-bearing — the article is a live experiment; readers will re-check to see if the fix worked.
- **`@id` consistency** on Person schema across the site is a real requirement for entity resolution — flagged inside the technical section.
- **90-day check-back** framing invites repeat visits + shares.
- **FAQ answers include "Contact for quote"** at least once.
- **Update cadence quarterly** with new LLM-response screenshots.

---

## Page 22 — T49: Auditing your website through the lens of what an LLM would extract (Tier 2 pulled forward)

| Field | Value |
|---|---|
| **URL** | `/learn/seo/llm-content-audit-website/` |
| **Page type** | Cluster content — tutorial + checklist |
| **Primary keyword** | `llm content audit website` |
| **Secondary keywords** | audit website for ai search · geo audit process · ai search readiness check · llm seo audit · how to audit content for chatgpt |
| **Search intent** | Informational (SEO practitioners running audits) |
| **H1** | How to Audit Your Website Through the Lens of What an LLM Would Extract |
| **Meta title** | LLM Content Audit — How to Check Your Site — Vraj Vithalani *(58 chars)* |
| **Meta description** | The step-by-step audit process for checking whether your website is LLM-extractable, with the exact prompt battery to test ChatGPT and Perplexity retrieval. *(157 chars)* |
| **Content format** | Tutorial + checklist |
| **Word count target** | 2,500–3,500 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1
- Author byline block
- **Short-answer block** (60–80 words)
- Table of contents
- H2 — Why a traditional SEO audit misses LLM-extractability
- H2 — The audit — what to check in what order
  - H3 — Step 1: Entity signal audit (name-role consistency, Person schema, sameAs)
  - H3 — Step 2: Short-answer block audit (page-by-page presence, placement, quality)
  - H3 — Step 3: Structured data audit (Person, Organization, Article, FAQPage, Service coverage)
  - H3 — Step 4: On-page content audit (heading hierarchy, question-phrased H2s, FAQ presence)
  - H3 — Step 5: External signals audit (sameAs verification, third-party mentions, GitHub/LinkedIn/Wikidata presence)
  - H3 — Step 6: Retrieval testing (the prompt battery)
- H2 — The prompt battery (10 exact prompts to feed ChatGPT/Perplexity/Claude/Gemini to test retrieval)
- H2 — Documenting the audit — the report template
- H2 — What to fix first (prioritization framework — entity, then extraction, then structure, then external)
- H2 — The re-audit cadence (quarterly minimum for active sites)
- H2 — In my client work (first-person block)
- H2 — Frequently asked questions (7 items)
- Author bio card

### Internal links OUT

- T45, T46, T47, T48 (siblings)
- T127, T128 (adjacent additions)
- `/learn/seo/wordpress-technical-seo-audit-checklist/` (T26)
- `/learn/seo/schema-types-service-business-site/` (T34)
- `/learn/seo/` (pillar)
- `/services/seo/` (soft CTA)

### Internal links IN

- `/learn/seo/` pillar (GEO section)
- `/services/seo/` (top cluster — replaces T21 if user swaps per Gap #2 in Tranche 2)
- Sibling GEO clusters
- T26 (technical audit checklist — cross-links to the LLM audit as a modern complement)

### Schema markup required

- **Article** + **FAQPage** + **BreadcrumbList** + **Person**/**Organization**
- **HowTo** on the audit steps

### EEAT elements required

- Byline + bio card
- Published + updated dates
- First-person "In my client work" block
- 10-prompt battery is a testable, copyable artifact (readers will actually run it)
- Reference to the audit Vraj is running on this site

### Media requirements

- Hero illustration: audit checklist + LLM icons
- Screenshot: example audit report template (blank, downloadable)
- Screenshot: sample prompt battery output from ChatGPT for a hypothetical or real site
- Diagram of the 6-step audit sequence
- Author photo
- OG image

### Notes

- **Tier 2 pulled forward per user's "T45–T49 first" instruction** — flagging that this changes Tranche 6's count (Tranche 6 becomes 35 pieces instead of 36 after this pull-forward; final Tranche 3 count 34 instead of 33).
- **The prompt battery is the article's shareable artifact** — treat as a copy-block, not a paragraph.
- **Cross-link with T26** (traditional WordPress SEO audit) — position T49 as the modern complement, not a replacement.
- **Downloadable report template** — Phase 4 asset; Google Doc or PDF link, gated by nothing.
- **FAQ answers include "Contact for quote"** at least once.
- **Update quarterly** — audit checklist evolves as LLM retrieval evolves.

# T127, T128, T129 — the three approved additions

## Page 23 — T127: AI Overviews for local service businesses

| Field | Value |
|---|---|
| **URL** | `/learn/seo/ai-overviews-local-service-business/` |
| **Page type** | Cluster content — guide |
| **Primary keyword** | `ai overviews local service business` |
| **Secondary keywords** | how to appear in google ai overviews · ai overviews for local seo · google ai overviews local business · ai overviews small business |
| **Search intent** | Informational (local business owners + local SEO practitioners) |
| **H1** | AI Overviews for Local Service Businesses — What Actually Surfaces You |
| **Meta title** | AI Overviews for Local Service Businesses — Vraj Vithalani *(58 chars)* |
| **Meta description** | What actually surfaces a local service business inside Google AI Overviews in 2026 — GBP signals, entity clarity, review velocity, structured citations. *(154 chars)* |
| **Content format** | Guide |
| **Word count target** | 2,500–3,500 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1
- Author byline block
- **Short-answer block** (60–80 words)
- Table of contents
- H2 — What "AI Overviews for local" actually looks like in 2026 (real screenshots)
- H2 — Why local SERPs got AI Overviews later than informational SERPs
- H2 — The 5 signals that surface a local service business
  - H3 — Signal 1: GBP completeness and category precision
  - H3 — Signal 2: Review velocity + review text quality (natural language mentions of the service)
  - H3 — Signal 3: Entity clarity in Person / LocalBusiness / Service schema
  - H3 — Signal 4: Local citation consistency (NAP alignment across sources)
  - H3 — Signal 5: Structured content on location pages (not doorway copy)
- H2 — The 3-city case (Surat / Ahmedabad / Bangalore) — how I'm setting this up on my own site (first-person, links to `/locations/` and the 12 location pages)
- H2 — What doesn't move AI Overviews for local (myths — post frequency alone, keyword-stuffed business descriptions, bulk citation blasts)
- H2 — Measuring AI Overview presence for your business (search-in-incognito + Perplexity + Bard AI Mode queries; document with dated screenshots)
- H2 — Frequently asked questions (7 items)
- Author bio card

### Internal links OUT

- T41 (GBP for solo service business), T43 (location pages not doorway), T129 (GBP posting frequency)
- T45, T47, T48 (GEO siblings)
- `/learn/seo/` (pillar), `/services/seo/` (soft CTA)
- `/locations/` (working example)

### Internal links IN

- `/learn/seo/` pillar (Local SEO + GEO sections)
- `/services/seo/` (Local SEO context)
- 12 location pages (Tranche 4 — upward-link the article as reference)
- Sibling GEO clusters

### Schema markup required

- **Article** + **FAQPage** + **BreadcrumbList** + **Person**/**Organization**
- **HowTo** on the measurement section

### EEAT elements required

- Byline + bio card, dates
- First-person 3-city case (links to live pages on this site)
- Dated screenshots of current AI Overviews for local Surat/Ahmedabad/Bangalore queries
- Reference to Vraj's GBP for the 3 cities

### Media requirements

- Hero: mocked-up AI Overview panel with local business result
- 3 dated screenshots (Surat, Ahmedabad, Bangalore) of real AI Overview appearances
- Signal-set diagram
- Author photo, OG image

### Notes

- **Cross-links with T129** — post frequency covered there, this article covers AI Overview surfacing specifically.
- **Working example** = the 12 location pages Vraj is deploying.
- **Update quarterly** — AI Overview local behavior is fresh territory.
- **FAQ answers include "Contact for quote"** at least once.

---

## Page 24 — T128: Bing indexing and its role in ChatGPT visibility

| Field | Value |
|---|---|
| **URL** | `/learn/seo/bing-indexing-chatgpt-visibility/` |
| **Page type** | Cluster content — tutorial |
| **Primary keyword** | `bing indexing chatgpt visibility` |
| **Secondary keywords** | how to get indexed on bing for chatgpt · bing webmaster tools for llm · chatgpt search index bing · appear in chatgpt via bing |
| **Search intent** | Informational (technical SEO + GEO practitioners) |
| **H1** | Bing Indexing and Its Role in ChatGPT Visibility |
| **Meta title** | Bing Indexing for ChatGPT Visibility — Vraj Vithalani *(53 chars)* |
| **Meta description** | The concrete Bing Webmaster + IndexNow setup and what ChatGPT actually retrieves from Bing's index vs Google's, with a working-example test on my own site. *(157 chars)* |
| **Content format** | Tutorial + evidence |
| **Word count target** | 2,500–3,000 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1
- Author byline block
- **Short-answer block** (60–80 words)
- Table of contents
- H2 — Why Bing matters for ChatGPT (and why most SEO writers still ignore it)
- H2 — The retrieval reality — what ChatGPT pulls from where in 2026
- H2 — The Bing Webmaster Tools setup — step by step
  - H3 — Verifying your site
  - H3 — Submitting your sitemap
  - H3 — Setting up IndexNow (WordPress + Next.js flavors)
  - H3 — Checking Bing's index for your pages
- H2 — What ChatGPT actually retrieves — the observed evidence
  - H3 — Test 1: brand-name query
  - H3 — Test 2: informational query
  - H3 — Test 3: local query
  - H3 — Documenting the retrieval sources ChatGPT cites (screenshots)
- H2 — Common failures and how to fix them (Bing not indexing, IndexNow silent, ChatGPT citing an old snapshot)
- H2 — Update cadence — re-check quarterly
- H2 — Frequently asked questions (6 items)
- Author bio card

### Internal links OUT

- T47 (how to appear in ChatGPT — the parent tactical piece), T49 (audit process), T26 (WordPress technical SEO)
- `/learn/seo/` (pillar), `/services/seo/` (soft CTA)
- External refs: Bing Webmaster Tools, IndexNow spec (`rel="noopener"`)

### Internal links IN

- `/learn/seo/` pillar (GEO section)
- T47 (tactical parent — cross-link)
- T49 (audit)
- Sibling GEO clusters

### Schema markup required

- **Article** + **FAQPage** + **BreadcrumbList** + **Person**/**Organization**
- **HowTo** on the Bing Webmaster setup

### EEAT elements required

- Byline + bio card, dates
- Live screenshots of Bing Webmaster Tools for vrajvithalani.com
- Live ChatGPT screenshots showing citation sources (dated)
- First-person block on the retrieval-testing process

### Media requirements

- Hero: Bing + ChatGPT visual link
- Screenshots: Bing Webmaster verification, sitemap submission, IndexNow setup
- Screenshots: 3 ChatGPT retrieval tests with sources visible
- Author photo, OG image

### Notes

- **Tactical companion to T47** — T47 is the framework; T128 goes deep on the Bing side.
- **Cross-links with T27 (WordPress indexation)** for WordPress-specific Bing setup.
- **Working-example site** = vrajvithalani.com; every screenshot is real and current.
- **Update quarterly** — ChatGPT retrieval shifts as OpenAI updates its indexing.
- **FAQ answers include "Contact for quote"** at least once.

---

## Page 25 — T129: GBP posting frequency and engagement in 2026

| Field | Value |
|---|---|
| **URL** | `/learn/seo/gbp-posting-frequency-2026/` |
| **Page type** | Cluster content — guide + honest opinion |
| **Primary keyword** | `gbp posting frequency 2026` |
| **Secondary keywords** | google business profile posts how often · gbp post engagement 2026 · gbp posts still work · gbp posting strategy 2026 |
| **Search intent** | Informational (local business owners) |
| **H1** | GBP Posting Frequency in 2026 — What Actually Moves Rankings vs What Just Fills the Feed |
| **Meta title** | GBP Posting Frequency 2026 — What Actually Matters — Vraj *(58 chars)* |
| **Meta description** | The honest 2026 answer on Google Business Profile posting frequency — what actually affects rankings vs engagement-only impact, tested on my own 3-city GBP. *(158 chars)* |
| **Content format** | Guide + opinion (honest read) |
| **Word count target** | 2,500–3,000 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1
- Author byline block
- **Short-answer block** (60–80 words with the honest tactical answer)
- Table of contents
- H2 — What GBP posts do and don't do in 2026 (context — the display rules have changed multiple times)
- H2 — The evidence — testing posting frequency on my own 3-city GBP
  - H3 — Test setup (Surat, Ahmedabad, Bangalore profiles; 3 different cadences)
  - H3 — What I measured (impressions, actions, ranking positions)
  - H3 — What the results showed
- H2 — The honest recommendation by business type
  - H3 — Solo service business (2–3 posts / week)
  - H3 — Multi-location business
  - H3 — E-commerce with local pickup
- H2 — Post types that actually earn engagement (updates > offers > events > booking)
- H2 — Post types that don't move anything (generic quotes, holiday greetings, sales-pitch language)
- H2 — Templates for the 4 post types worth publishing
- H2 — The engagement-ranking-signal question — where the real correlation is
- H2 — Frequently asked questions (7 items)
- Author bio card

### Internal links OUT

- T41 (GBP for solo service business — pillar reference)
- T127 (AI Overviews for local) — cross-link
- T43 (location pages) — cross-link
- `/learn/seo/` (pillar), `/services/seo/` (soft CTA)
- `/locations/` (working example — 3 city profiles)

### Internal links IN

- `/learn/seo/` pillar (Local SEO section)
- `/services/seo/` (Local SEO context)
- 3 location pages for Surat/Ahmedabad/Bangalore (Tranche 4)
- T41 (pillar reference — cross-link)

### Schema markup required

- **Article** + **FAQPage** + **BreadcrumbList** + **Person**/**Organization**

### EEAT elements required

- Byline + bio card, dates
- Test data from Vraj's own 3-city GBP (screenshots of insights + rankings, dated)
- First-person "test I ran" block
- Named-tool references (GBP insights, Local Falcon or equivalent rank-tracker if used)

### Media requirements

- Hero: GBP post + engagement visual
- Screenshots: 3 GBP profile insights panels (Surat, Ahmedabad, Bangalore) — dated
- 4 post-type template mockups
- Author photo, OG image

### Notes

- **Working example** = Vraj's own 3-city GBPs; the test data is the article's differentiator.
- **Update quarterly** — GBP display rules and ranking correlations shift regularly.
- **Cross-links with T41** (pillar) and T127 (AI Overviews) — the local SEO triad.
- **FAQ answers include "Contact for quote"** at least once.

# Remaining Tier 1 cluster content (T# order)

## Page 26 — T1: Google Ads account structure for a service business (one campaign type only)

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/google-ads-account-structure-service-business/` |
| **Page type** | Cluster content — guide |
| **Primary keyword** | `how to structure google ads account for small business` |
| **Secondary keywords** | google ads account structure best practices · google ads campaign structure for beginners · setting up google ads for service business |
| **Search intent** | Info-commercial |
| **H1** | The Google Ads Account Structure a Service Business Actually Needs |
| **Meta title** | Google Ads Account Structure for Service Business — Vraj *(56 chars)* |
| **Meta description** | The exact Google Ads account structure a service business should launch with — one campaign type, right ad groups, right conversions, right budget from day one. *(160 chars)* |
| **Content format** | Guide |
| **Word count target** | 3,000–4,000 |
| **CTA** | Soft link → `/services/google-ads/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why the standard "6 campaigns, 20 ad groups" advice fails Indian SMBs
- H2 — Start with one campaign type — here's how to pick which one
- H2 — Ad-group structure that matches how services actually convert
- H2 — Conversion actions you need before Day 1 (link out to T3)
- H2 — Keyword themes vs match-type structure
- H2 — Negatives to launch with (short list; deep list at T10 — Tranche 6)
- H2 — Bid strategy for a fresh account (link out to T12 — Tranche 7)
- H2 — The 30-day setup timeline (week-by-week)
- H2 — What to change (and what to leave alone) after the first learning period
- H2 — In my client work — the setup I actually shipped for Powercable
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T3 (tracking stack), T5 (PMax alt), T10, T12 (bidding), T13, T17, T21, T22
- `/services/google-ads/`, `/learn/google-ads/`, `/case-studies/powercable/`

### Internal links IN

- `/learn/google-ads/` pillar (Foundation H2), `/services/google-ads/` (top 6), sibling Google Ads clusters, T89 (industrial exporter vertical link)

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (setup timeline)

### EEAT

- Byline, dates, first-person Powercable setup block, INR-anchored budget numbers, real named tools (GA4, GTM, Google Ads editor)

### Media

- Hero: account-structure diagram (campaigns → ad groups → keywords)
- Screenshot: real account structure (anonymised)
- 30-day timeline visual
- Author photo, OG image

### Notes

- Foundational piece — every Google Ads cluster references this as the starting point.
- Powercable as working example.
- FAQ answers include "Contact for quote" at least once.

---

## Page 27 — T3: Minimum tracking stack pre-launch

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/minimum-tracking-stack-pre-launch/` |
| **Page type** | Cluster content — checklist + tutorial |
| **Primary keyword** | `google ads conversion tracking setup checklist` |
| **Secondary keywords** | ga4 google ads integration · gtm google ads conversion tracking · setup google ads conversions before launch |
| **Search intent** | Informational |
| **H1** | The Minimum Tracking Stack You Need Before Launching a Google Ads Campaign |
| **Meta title** | Google Ads Tracking Setup Checklist — Vraj Vithalani *(52 chars)* |
| **Meta description** | The exact GA4 + Google Ads Conversions + GTM stack you must have working before a single ad goes live, in the order to set them up and how to verify each. *(158 chars)* |
| **Content format** | Checklist + tutorial |
| **Word count target** | 2,500–3,500 |
| **CTA** | Soft link → `/services/google-ads/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why campaigns launched without tracking are always broken
- H2 — The 4-piece minimum stack (GA4 + Google Ads Conversions + GTM + Search Console)
- H2 — Setup order (GA4 → GTM → Google Ads Conversions → link accounts → test)
  - H3 for each — step-by-step
- H2 — The 5 conversion actions that matter for a service business
- H2 — Testing before launch — the verification checklist
- H2 — Common tracking failures and how to catch them early
- H2 — In my client work — the pre-launch tracking checklist I actually use
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T1 (account structure), T4 (conversion actions — Tranche 6), T14 (LP + QS), T17 (audit), T72 (GA4 events), T73 (GTM guide)
- `/services/google-ads/`, `/learn/google-ads/`, `/learn/cro-and-automation/` (cross-pillar)

### Internal links IN

- `/learn/google-ads/` pillar (Foundation H2), `/services/google-ads/` (top 6), T1, T13, T17

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (setup sequence)

### EEAT

- Byline, dates, first-person checklist mention, screenshots of real GA4/GTM/Ads links, checklist as downloadable artifact

### Media

- Hero: 4-piece stack diagram
- Screenshots: GA4 property setup, GTM container, Google Ads conversion action, GSC verification
- Author photo, OG image

### Notes

- Cross-pillar link with `/learn/cro-and-automation/` — same tracking stack matters for CRO.
- Downloadable checklist PDF as Phase 4 asset.
- FAQ answers include "Contact for quote" at least once.

---

## Page 28 — T5: Performance Max without a full creative team

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/performance-max-without-creative-team/` |
| **Page type** | Cluster content — guide |
| **Primary keyword** | `performance max campaign structure small business` |
| **Secondary keywords** | performance max for service business · asset group structure pmax · pmax without creative team |
| **Search intent** | Info-commercial |
| **H1** | Performance Max Without a Full Creative Team — The SMB Setup |
| **Meta title** | Performance Max for Small Business — No Creative Team *(52 chars)* |
| **Meta description** | How to structure a Performance Max campaign when you don't have a designer, a video team, or a copywriter — the minimum-asset path for an Indian SMB in 2026. *(159 chars)* |
| **Content format** | Guide |
| **Word count target** | 3,000–3,500 |
| **CTA** | Soft link → `/services/google-ads/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — What PMax actually needs (asset counts, feeds, signals) — the honest floor
- H2 — Why most SMB PMax attempts burn budget in week 1
- H2 — The minimum asset set that lets PMax learn
- H2 — Asset-group strategy by service line (link to T6 — Tranche 6)
- H2 — Audience signals — the manual inputs PMax needs from you
- H2 — Feed-less PMax vs feed-driven PMax (when to build a merchant feed)
- H2 — The 30-day PMax launch plan for a solo operator
- H2 — When to defer PMax entirely (link to T7 — Tranche 7)
- H2 — In my client work — a PMax setup that worked at ₹30k/month
- H2 — FAQ (6 items)
- Author bio card

### Internal links OUT

- T1, T2 (Tranche 6), T6, T7 (Tranche 7), T13, T17
- `/services/google-ads/`, `/learn/google-ads/`

### Internal links IN

- `/learn/google-ads/` pillar (PMax H2), `/services/google-ads/`, sibling Google Ads clusters

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo**

### EEAT

- Byline, dates, first-person client PMax setup, real INR budget anchor (₹30k/month)

### Media

- Hero: PMax asset-set visual
- Diagram: asset group by service line
- Screenshot: sample asset group (anonymised)
- Author photo, OG image

### Notes

- Focus on SMB constraints — creative bandwidth, budget floor.
- Real INR anchor differentiates against USD-framed international content.
- FAQ answers include "Contact for quote" at least once.

---

## Page 29 — T13: Google Ads clicks but no conversions

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/google-ads-clicks-no-conversions/` |
| **Page type** | Cluster content — teardown + diagnostic |
| **Primary keyword** | `google ads clicks but no conversions` |
| **Secondary keywords** | google ads not converting reasons · getting clicks but no leads google ads · why aren't my google ads working |
| **Search intent** | Info-commercial (troubleshooting) |
| **H1** | Google Ads Clicks But No Conversions — The 30-Minute Diagnostic |
| **Meta title** | Google Ads Clicks But No Conversions — Vraj Vithalani *(53 chars)* |
| **Meta description** | The 30-minute diagnostic sequence to run when Google Ads gets clicks but no conversions — biased toward the landing-page and tracking causes ads-only writers miss. *(163 chars → trim to 158)* |
| **Content format** | Teardown + diagnostic sequence |
| **Word count target** | 3,000–4,000 |
| **CTA** | Soft link → `/services/google-ads/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why the standard "10 reasons" listicles miss the real cause
- H2 — Check 1: Is tracking actually firing? (10-minute audit)
- H2 — Check 2: Is search intent aligned? (search-terms report deep-look)
- H2 — Check 3: Is the landing page holding up its end?
- H2 — Check 4: Is the offer the actual problem?
- H2 — Check 5: Is the follow-up (WhatsApp/email) losing leads before they convert?
- H2 — The diagnostic tree — visual flowchart
- H2 — In my client work — the diagnostic that fixed a real "no conversions" campaign
- H2 — What to do first based on which check failed
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T3, T14 (LP + QS), T17 (12-point audit), T18 (Tranche 6), T19 (search terms — Tranche 6), T20 (broken tracking — Tranche 7), T69 (landing page checklist), T76 (WhatsApp funnel)
- `/services/google-ads/`, `/learn/google-ads/`, `/learn/cro-and-automation/` (cross-pillar)

### Internal links IN

- `/learn/google-ads/` pillar (Landing page + Diagnosis H2s), `/services/google-ads/`, T17 (parent audit — cross-link)

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (diagnostic sequence)

### EEAT

- Byline, dates, first-person client diagnostic story, real numbers (click volume, conversion rate before/after)

### Media

- Hero: "clicks vs conversions" gap visual
- Diagnostic flowchart (5 checks → outcomes)
- Screenshot: real (anonymised) search-terms report showing the fix
- Author photo, OG image

### Notes

- Compound-skill signature piece — the LP+tracking bias is what a marketer-who-builds catches that a media-only agency misses.
- Cross-pillar link with `/learn/cro-and-automation/`.
- FAQ answers include "Contact for quote" at least once.

---

## Page 30 — T14: Landing page elements Google Ads actually rewards in Quality Score

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/landing-page-elements-quality-score/` |
| **Page type** | Cluster content — framework |
| **Primary keyword** | `landing page quality score google ads` |
| **Secondary keywords** | landing page experience google ads · improve quality score landing page · google ads landing page optimization |
| **Search intent** | Informational |
| **H1** | Landing Page Elements Google Ads Actually Rewards in Quality Score |
| **Meta title** | Landing Page Elements Google Ads Rewards — Vraj Vithalani *(58 chars)* |
| **Meta description** | The compound view of Quality Score — what the ad promises, what the page has to prove, what the tracking has to fire — from someone who ships both sides. *(154 chars)* |
| **Content format** | Framework |
| **Word count target** | 3,000–4,000 |
| **CTA** | Soft link → `/services/google-ads/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — What Quality Score actually measures in 2026 (three-part composite)
- H2 — The compound view — ad × page × tracking as one system
- H2 — Element 1: Message match (ad copy ↔ page H1 ↔ page body first paragraph)
- H2 — Element 2: Page speed (LCP, CLS, INP — targets)
- H2 — Element 3: Mobile experience (Google Ads is majority mobile in 2026)
- H2 — Element 4: Content depth (relevant, useful, transparent)
- H2 — Element 5: Contact/trust signals (real phone, real address, real reviews)
- H2 — Element 6: Conversion friction (form length, CTA clarity, load speed at submit)
- H2 — Element 7: Tracking hygiene (conversions firing, no double-count, no page-view false positives)
- H2 — Element 8: Post-click follow-up (WhatsApp/email response times)
- H2 — In my client work — building a Google-Ads-native landing page for Powercable
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T13 (no conversions), T15 (WP vs Next.js LP — Tranche 6), T16 (LP anatomy — Tranche 6), T17, T69 (LP checklist), T112 (speed × QS × SEO), T76 (WhatsApp funnel)
- `/services/google-ads/`, `/learn/google-ads/`, `/learn/cro-and-automation/`, `/learn/web-development/`

### Internal links IN

- `/learn/google-ads/` pillar (LP integration H2), `/services/google-ads/`, `/services/web-development/`, T13, T15, T112 (cross-pillar cluster)

### Schema

- **Article** + **FAQPage** + **BreadcrumbList**

### EEAT

- Byline, dates, first-person Powercable LP story with real speed/QS numbers, compound-skill statement ("I ship the page and the campaign")

### Media

- Hero: landing page annotated with QS-relevant elements
- Diagram: message-match visual (ad copy → page H1 → body first paragraph)
- Screenshot: real (anonymised) QS diagnostics from Google Ads
- Speed screenshot from PageSpeed Insights (real, live URL)
- Author photo, OG image

### Notes

- Compound-skill signature — one of the strongest single articles for the "builds + runs" positioning.
- Cross-pillar links to Web Dev and CRO — this article should be reachable from all three service pillars.
- FAQ answers include "Contact for quote" at least once.

## Page 31 — T17: The 12-point audit I run when a Google Ads account isn't performing

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/12-point-google-ads-audit/` |
| **Page type** | Cluster content — checklist |
| **Primary keyword** | `google ads account audit checklist` |
| **Secondary keywords** | how to audit a google ads account · google ads audit process · google ads performance audit |
| **Search intent** | Informational |
| **H1** | The 12-Point Google Ads Audit I Run on Every Underperforming Account |
| **Meta title** | 12-Point Google Ads Audit Checklist — Vraj Vithalani *(52 chars)* |
| **Meta description** | The 12 checks — in the exact order a consultant runs them — to diagnose an underperforming Google Ads account. No lead gate, no fluff, downloadable checklist. *(159 chars)* |
| **Content format** | Checklist |
| **Word count target** | 3,500–4,500 |
| **CTA** | Soft link → `/services/google-ads/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why the order matters (fixing symptoms before causes wastes time)
- H2 — Check 1: Account access + billing health
- H2 — Check 2: Conversion tracking sanity (link to T3)
- H2 — Check 3: Search-terms report review
- H2 — Check 4: Ad-group thematic tightness
- H2 — Check 5: Match-type distribution + intent match
- H2 — Check 6: Negative-keyword coverage
- H2 — Check 7: Ad copy quality + Quality Score inputs (link to T14)
- H2 — Check 8: Landing-page alignment (link to T13, T14)
- H2 — Check 9: Bid strategy + budget pacing
- H2 — Check 10: Audience signals + remarketing
- H2 — Check 11: Extensions coverage
- H2 — Check 12: Historical trend read (last 90 days vs current)
- H2 — What to fix first based on which checks failed
- H2 — In my client work — an audit that flipped a stalled account
- H2 — FAQ (8 items)
- Author bio card

### Internal links OUT

- T1, T3, T13, T14, T18, T19, T20 (Tranche 7), T21
- `/services/google-ads/`, `/learn/google-ads/`

### Internal links IN

- `/learn/google-ads/` pillar (Diagnosis H2), `/services/google-ads/` (top 6), T13, T29 (T13 blueprint page above)

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (12 checks as procedural steps)

### EEAT

- Byline, dates, first-person client turnaround story with real numbers, downloadable checklist PDF

### Media

- Hero: 12-point checklist visual
- Screenshot: real (anonymised) audit finding
- Downloadable checklist card (link to PDF)
- Author photo, OG image

### Notes

- Non-gated checklist download — differentiator against agency lead-magnet content per Phase 1b SERP note.
- FAQ answers include "Contact for quote" at least once.
- Cross-links with T13 (clicks-no-conversions) and T14 (LP + QS) as the diagnostic triad.

---

## Page 32 — T21: The minimum daily budget where Google Ads actually starts working

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/minimum-google-ads-budget-that-works/` |
| **Page type** | Cluster content — opinion + framework |
| **Primary keyword** | `minimum google ads budget small business` |
| **Secondary keywords** | how much to spend on google ads · minimum daily budget google ads · google ads budget for beginners |
| **Search intent** | Informational |
| **H1** | The Minimum Google Ads Budget That Actually Starts Working (Honest INR Numbers) |
| **Meta title** | Minimum Google Ads Budget That Works — Vraj Vithalani *(53 chars)* |
| **Meta description** | The honest INR floor for a Google Ads test that produces signal, what happens at each spend tier, and the "wait, save, launch bigger" alternative for SMBs. *(157 chars)* |
| **Content format** | Opinion + framework |
| **Word count target** | 2,500–3,500 |
| **CTA** | Soft link → `/services/google-ads/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why the USD-framed "$10/day" advice is wrong for India
- H2 — What "works" actually means (signal, not sales — at floor budgets)
- H2 — The INR floor by campaign type (Search, PMax, Meta)
- H2 — What happens at ₹5k / ₹10k / ₹15k / ₹25k / ₹50k monthly (tier-by-tier)
- H2 — When to wait, save, and launch bigger instead
- H2 — When to spend less than the floor (the honest edge cases — brand terms only, remarketing only)
- H2 — In my client work — the smallest budget I've made produce real leads
- H2 — What to spend the first ₹15k on (link to T22 for the full test protocol)
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T1, T22 (₹15k test), T25 (Meta local), T100 (SMB budget context)
- `/services/google-ads/`, `/learn/google-ads/`

### Internal links IN

- `/learn/google-ads/` pillar (Budget H2), `/services/google-ads/` (top 6), T1, T22, T100

### Schema

- **Article** + **FAQPage** + **BreadcrumbList**

### EEAT

- Byline, dates, first-person real client-story with rupee figures, honest "when not to spend" section

### Media

- Hero: budget-tier ladder visual
- Table: what each INR tier gets you
- Screenshot: real (anonymised) low-budget account showing signal
- Author photo, OG image

### Notes

- Under-served corner per Phase 1b — the honest INR floor answer is nowhere.
- Cross-links with T22 (the ₹15k test protocol) as the tactical follow-on.
- FAQ answers include "Contact for quote" at least once.

---

## Page 33 — T22: Running a real Google Ads test on a ₹15,000/month budget without wasting it

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/google-ads-15000-rupees-test-protocol/` |
| **Page type** | Cluster content — guide + protocol |
| **Primary keyword** | `google ads budget 15000 rupees test` |
| **Secondary keywords** | google ads on small budget india · minimum google ads budget india · low budget google ads campaign |
| **Search intent** | Info-commercial |
| **H1** | The ₹15,000/Month Google Ads Test — A 30-Day Protocol That Produces Real Signal |
| **Meta title** | ₹15k/Month Google Ads Test Protocol — Vraj Vithalani *(52 chars)* |
| **Meta description** | The exact 30-day Google Ads test protocol at ₹15,000/month — match-type choices, geo settings, bid strategy, and the reading of results that decides scale-up. *(160 chars)* |
| **Content format** | Guide + protocol |
| **Word count target** | 3,000–4,000 |
| **CTA** | Soft link → `/services/google-ads/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — What "test" means at this budget (signal vs sales; the honest goal)
- H2 — Pre-launch — the setup this budget can't afford to get wrong
- H2 — Week 1: Launch config (campaign type, keyword count, ad count, geo, bid strategy)
- H2 — Week 2: First data read + first optimisations
- H2 — Week 3: Continue vs cut vs pivot decisions
- H2 — Week 4: The read that determines whether to scale up, hold, or stop
- H2 — What ₹15k actually buys in CPCs across common Indian verticals (real data)
- H2 — Common mistakes at this budget (too many keywords, wrong match type, no negatives, chasing tCPA before data allows)
- H2 — In my client work — a real ₹15k test that turned into a ₹60k/month scaled campaign
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T1, T3, T9 (match type — Tranche 6), T10, T21, T22 self-context
- `/services/google-ads/`, `/learn/google-ads/`

### Internal links IN

- `/learn/google-ads/` pillar (Budget H2), `/services/google-ads/` (top 6 — consider swap with T21 per Tranche 2 gap #2), T21

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (30-day protocol as procedural)

### EEAT

- Byline, dates, first-person real client ₹15k → ₹60k story, real INR/CPC data, downloadable 30-day-schedule template

### Media

- Hero: 30-day-timeline visual
- Table: CPC ranges by Indian vertical
- Downloadable protocol PDF
- Author photo, OG image

### Notes

- Near-empty SERP per Phase 1b — this is a break-in opportunity.
- Downloadable 30-day protocol as Phase 4 asset.
- FAQ answers include "Contact for quote" at least once.

---

## Page 34 — T25: Meta Ads for local service businesses in 2026

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/meta-ads-local-service-business/` |
| **Page type** | Cluster content — opinion + guide |
| **Primary keyword** | `meta ads for local service business` |
| **Secondary keywords** | facebook ads for local business · instagram ads for service business · meta ads small business india |
| **Search intent** | Info-commercial |
| **H1** | Meta Ads for Local Service Businesses — What Actually Works in 2026 |
| **Meta title** | Meta Ads for Local Service Business 2026 — Vraj Vithalani *(58 chars)* |
| **Meta description** | The honest 2026 answer for local service business Meta Ads — what converts for coaching, physio, tours, and NGOs, from real client campaign data. *(147 chars → expand to 155)* |
| **Content format** | Opinion + guide |
| **Word count target** | 2,500–3,500 |
| **CTA** | Soft link → `/services/google-ads/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why most local-service Meta content is written by e-com marketers who don't run local
- H2 — What "local service business" actually looks like on Meta in 2026
- H2 — Instant Forms vs landing page — the honest tradeoff (link to T24 — Tranche 6)
- H2 — Creative choices that convert for local services (photo, testimonial, before-after, offer)
- H2 — Targeting that works (radius + interest layering; the algorithm-first approach)
- H2 — Budget floors for local Meta (what the algorithm needs to learn)
- H2 — Vertical-specific patterns
  - H3 — Coaching institutes (parents vs students)
  - H3 — Physiotherapy clinics (case study reference to drvishva only — no vertical Learn content)
  - H3 — Tours & travel
  - H3 — NGO fundraising
- H2 — What doesn't work (boost-post, cold-audience discount offers, ambiguous creative)
- H2 — In my client work — real Meta campaigns for Parv Travels, Synergy Tutorials, Little Genius
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T24 (Tranche 6), `/case-studies/parv-travels/`, `/case-studies/synergy-tutorials/`, `/case-studies/little-genius/`, T96 (fundraising LP — Tranche 7)
- `/services/google-ads/`, `/learn/google-ads/`

### Internal links IN

- `/learn/google-ads/` pillar (Meta Ads H2), `/services/google-ads/` (top 6), sibling clusters, vertical case studies

### Schema

- **Article** + **FAQPage** + **BreadcrumbList**

### EEAT

- Byline, dates, real client campaign references (Parv Travels 3-month, Synergy admissions, Little Genius brand awareness)
- Honest section on what doesn't work

### Media

- Hero: Meta Ads dashboard + local pin visual
- Real (anonymised) ad creative examples
- Screenshot: sample Instant Form vs LP comparison result
- Author photo, OG image

### Notes

- **Physiotherapy handled correctly** — referenced as a case study client only (drvishva), NOT as a vertical Learn topic (Doc 02 rule).
- SERP is near-empty of honest local-service Meta content per Phase 1b — real break-in slot.
- FAQ answers include "Contact for quote" at least once.

## Page 35 — T26: WordPress technical SEO audit checklist

| Field | Value |
|---|---|
| **URL** | `/learn/seo/wordpress-technical-seo-audit-checklist/` |
| **Page type** | Cluster content — checklist |
| **Primary keyword** | `wordpress technical seo audit checklist` |
| **Secondary keywords** | wordpress seo audit template · technical seo wordpress 2026 · wordpress seo checklist |
| **Search intent** | Informational |
| **H1** | The 15-Point WordPress Technical SEO Audit I Run Before Touching Any Site |
| **Meta title** | WordPress Technical SEO Audit Checklist — Vraj Vithalani *(56 chars)* |
| **Meta description** | The 15-point WordPress technical SEO audit ordered by likelihood-of-being-broken, plus the LLM-audit step most 2026 checklists still under-cover. *(148 chars → expand to 155)* |
| **Content format** | Checklist |
| **Word count target** | 3,500–4,500 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why "40-point" checklists usually waste your time
- H2 — The 15 checks in order of likelihood-of-being-broken
  - H3 for each — what to check, how to check, what the fix looks like
    - Robots.txt + sitemap + indexation basics
    - HTTPS + canonical + non-www vs www redirects
    - Core Web Vitals baseline
    - Theme code hygiene (bloat, render-blocking, image handling)
    - Plugin audit (SEO, cache, security — one of each maximum)
    - Schema coverage (Person, Organization, Article, FAQPage, LocalBusiness)
    - Heading hierarchy per template
    - Internal linking density + orphan pages
    - Meta title + description coverage (and length)
    - Image alt + WebP/AVIF adoption
    - XML sitemap health + submission status (GSC + Bing)
    - Search Console coverage errors triage
    - Backlink profile sanity (spam, broken, lost)
    - GBP + local citation NAP alignment
    - **LLM-audit step** — feed pages to ChatGPT/Perplexity, check retrieval accuracy (link to T49)
- H2 — What to fix first (priority matrix)
- H2 — In my client work — the audit I run on WordPress site handovers
- H2 — Downloadable audit checklist
- H2 — FAQ (8 items)
- Author bio card

### Internal links OUT

- T27 (indexation fix), T29 (GSC errors — Tranche 7), T34 (schema types), T49 (LLM audit), T38 (hub-and-spoke), T51 (fast WP — Tranche 6), T62 (WordFence + 2FA)
- `/services/seo/`, `/learn/seo/`, `/services/web-development/` (cross-pillar)

### Internal links IN

- `/learn/seo/` pillar (Technical SEO H2), `/services/seo/` (top 6), sibling SEO clusters, T27, T49

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (15-step audit)

### EEAT

- Byline, dates, first-person client audit story, downloadable checklist, LLM-audit step is fresh differentiator

### Media

- Hero: 15-point audit visual (numbered, soft-teal)
- Screenshot: real (anonymised) audit finding
- Downloadable checklist PDF card
- Author photo, OG image

### Notes

- 15 checks in likelihood order — the differentiator vs 40-point generic checklists per Phase 1b SERP note.
- LLM-audit step (T49) is the fresh 2026 addition that most WordPress SEO checklists miss.
- FAQ answers include "Contact for quote" at least once.

---

## Page 36 — T27: Fix WordPress indexation problems

| Field | Value |
|---|---|
| **URL** | `/learn/seo/wordpress-indexation-problems-fix/` |
| **Page type** | Cluster content — guide |
| **Primary keyword** | `wordpress indexation problems fix` |
| **Secondary keywords** | wordpress pages not indexed google · google search console coverage errors wordpress · deindexed pages wordpress |
| **Search intent** | Informational |
| **H1** | Fixing Indexation Problems on a WordPress Site That Used to Rank |
| **Meta title** | Fix WordPress Indexation Problems — Vraj Vithalani *(50 chars)* |
| **Meta description** | The diagnosis tree for WordPress pages that vanished from Google — from robots.txt to theme code, in the order a builder-SEO actually checks. *(146 chars → expand to 156)* |
| **Content format** | Guide |
| **Word count target** | 2,500–3,500 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — What "not indexed" actually means (crawled-not-indexed vs discovered-not-indexed vs excluded)
- H2 — The diagnosis tree
  - H3 — Branch 1: Robots.txt / noindex / canonical excludes
  - H3 — Branch 2: XML sitemap gaps
  - H3 — Branch 3: Internal linking (orphan pages)
  - H3 — Branch 4: Content quality (thin, duplicate, boilerplate)
  - H3 — Branch 5: Site speed / render issues (JS-blocked crawl)
  - H3 — Branch 6: Theme code (bad plugin, broken hooks)
  - H3 — Branch 7: Search Console + Bing Webmaster confirmations
- H2 — The recovery sequence (fix → resubmit → validate → wait)
- H2 — What "site-wide de-indexation" actually looks like (rare, but the checklist for it)
- H2 — In my client work — a real WordPress site recovery from crawled-not-indexed
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T26 (audit checklist), T29 (GSC errors — Tranche 7), T51, T128 (Bing indexing)
- `/services/seo/`, `/learn/seo/`

### Internal links IN

- `/learn/seo/` pillar (Technical SEO H2), `/services/seo/`, T26 (parent), sibling SEO

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (diagnosis tree)

### EEAT

- Byline, dates, first-person client recovery story, real GSC screenshots (anonymised)

### Media

- Hero: diagnosis-tree flowchart
- Screenshot: GSC coverage report showing before/after
- Author photo, OG image

### Notes

- Companion to T26 (audit) — the audit finds the problem; T27 walks the recovery.
- Cross-links with T128 for the Bing side of recovery.
- FAQ answers include "Contact for quote" at least once.

---

## Page 37 — T34: The schema types every service-business site should have

| Field | Value |
|---|---|
| **URL** | `/learn/seo/schema-types-service-business-site/` |
| **Page type** | Cluster content — framework |
| **Primary keyword** | `schema markup for service business` |
| **Secondary keywords** | what schema types to use · service schema vs local business schema · schema for small business website |
| **Search intent** | Informational |
| **H1** | The 5 Schema Types Every Service-Business Site Needs (And the 3 to Skip) |
| **Meta title** | Schema Types for Service Business Websites — Vraj Vithalani *(59 chars)* |
| **Meta description** | The 5 schema types every service-business site should ship at launch, the 3 to defer, and the JSON-LD templates you can copy from live pages on this site. *(157 chars)* |
| **Content format** | Framework |
| **Word count target** | 3,000–3,500 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why prescriptive beats exhaustive when you're solo
- H2 — The 5 schemas every service-business site needs
  - H3 — Person (for the operator / consultant / founder)
  - H3 — Organization (for the business entity)
  - H3 — LocalBusiness / ProfessionalService (for the service-area business)
  - H3 — Service (for each service line)
  - H3 — Article / BlogPosting + FAQPage (for content pages)
- H2 — The 3 schemas to skip (until you scale)
  - Product (for service businesses without a catalog)
  - Review / AggregateRating (until you have real, verified reviews)
  - Course / Event (unless you actually run one)
- H2 — Copy-paste JSON-LD templates for each (live examples from vrajvithalani.com)
- H2 — How to test schema (Rich Results Test + Schema.org validator + real SERP check)
- H2 — Common mistakes (duplicate @id, missing sameAs, wrong LocalBusiness subtype, over-marking testimonials)
- H2 — In my client work — the schema I ship on every new site
- H2 — FAQ (8 items)
- Author bio card

### Internal links OUT

- T26 (audit), T35 (FAQ schema — Tranche 6), T36 (Person schema — Tranche 6), T37 (LocalBusiness — Tranche 7), T48 (entity establishment)
- `/services/seo/`, `/learn/seo/`, `/services/web-development/` (cross-pillar — schema is a build activity)

### Internal links IN

- `/learn/seo/` pillar (Schema H2), `/services/seo/` (top 6), `/services/web-development/`, T48

### Schema

- **Article** + **FAQPage** + **BreadcrumbList**
- (Meta: the article itself demonstrates every schema being taught — live JSON-LD blocks visible in view-source)

### EEAT

- Byline, dates, copy-paste JSON-LD from live vrajvithalani.com pages, first-person "I ship this on every project" block

### Media

- Hero: schema-type set visual (5 in, 3 out)
- Screenshot: Rich Results Test passing for a real page
- Code blocks: JSON-LD templates (copyable)
- Author photo, OG image

### Notes

- Meta-demonstration: the site being read is the working example of every schema being recommended.
- Cross-pillar with `/services/web-development/` — schema is a build activity.
- FAQ answers include "Contact for quote" at least once.

---

## Page 38 — T38: Hub-and-spoke content architecture for a service-business site

| Field | Value |
|---|---|
| **URL** | `/learn/seo/hub-and-spoke-content-architecture/` |
| **Page type** | Cluster content — framework |
| **Primary keyword** | `hub and spoke content architecture seo` |
| **Secondary keywords** | pillar and cluster content strategy · content hub for service business · topic cluster seo strategy |
| **Search intent** | Informational |
| **H1** | Hub-and-Spoke Content Architecture — The Structure a Service-Business Site Actually Needs |
| **Meta title** | Hub-and-Spoke Architecture for Service Business Sites — Vraj *(60 chars)* |
| **Meta description** | The hub-and-spoke architecture Vraj is deploying on his own 4-pillar, 120-page service-business site — with the URL structure, linking rules, and word-count logic. *(163 → 158)* |
| **Content format** | Framework + case study |
| **Word count target** | 3,000–4,000 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — What "hub and spoke" actually means (pillar + cluster, not just tags)
- H2 — Why service-business sites need it (topical authority + internal-link economy)
- H2 — The architecture on this site (4 pillars × ~30 clusters + 12 location pages + 13 case studies)
- H2 — The linking rules
  - H3 — Cluster → pillar (mandatory upward link)
  - H3 — Pillar → cluster (index at bottom)
  - H3 — Cluster → sibling cluster (2–3 lateral links)
  - H3 — Case study → service pillar (soft CTA)
  - H3 — Location page → service pillar (breadcrumb + explicit link)
- H2 — Word-count logic per page type
- H2 — Common mistakes (too many pillars, thin clusters, no upward link, hub without index)
- H2 — How to build one from scratch (the 4-step sequence)
- H2 — In my working example — this site, laid open
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T39 (URL structure — Tranche 6), T40 (internal linking small site — Tranche 7), T43 (location pages)
- `/services/seo/`, `/learn/seo/`, `/case-studies/` (working example), `/locations/`

### Internal links IN

- `/learn/seo/` pillar (Architecture H2), `/services/seo/` (top 6), `/services/web-development/`, T26, T39, T40

### Schema

- **Article** + **FAQPage** + **BreadcrumbList**

### EEAT

- Byline, dates, this-site-as-working-example is the strongest single EEAT play — the reader is inside the architecture being described

### Media

- Hero: hub-and-spoke architecture diagram (this site's layout)
- Screenshot: the site's Learn hub with 4 pillars visible
- Diagram: linking rules visual (arrows between page types)
- Author photo, OG image

### Notes

- Meta-demonstration: the site is the example.
- Cross-links with `/services/web-development/` — architecture is a build decision.
- FAQ answers include "Contact for quote" at least once.

## Page 39 — T41: GBP setup and optimisation for a solo service business

| Field | Value |
|---|---|
| **URL** | `/learn/seo/google-business-profile-solo-consultant/` |
| **Page type** | Cluster content — guide |
| **Primary keyword** | `google business profile setup solo consultant` |
| **Secondary keywords** | gbp for solo business · google business profile no physical location · gbp for consultant |
| **Search intent** | Informational |
| **H1** | Setting Up and Optimising Google Business Profile for a Solo Service Business |
| **Meta title** | GBP for a Solo Service Business — Vraj Vithalani *(48 chars → expand: GBP Setup for Solo Service Business — Vraj Vithalani = 54 chars)* |
| **Meta description** | The solo-consultant GBP setup — service-area configuration, category precision, and the post-cadence that actually moves rankings, not just engagement. *(150 chars)* |
| **Content format** | Guide |
| **Word count target** | 3,000–4,000 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why solo GBP is different from multi-location GBP
- H2 — Setup — the fields that actually matter
  - H3 — Business name (real, no keyword stuffing)
  - H3 — Category — primary + secondary (precision > breadth)
  - H3 — Service area (SAB config — hiding the address correctly)
  - H3 — Services list (with descriptions matching your service pillar pages)
  - H3 — Products (usually skip for services)
  - H3 — Business description (short, keyword-informed, human)
  - H3 — Photos (real, geotagged, categorised)
- H2 — Verification — the postcard vs video vs instant path
- H2 — Ongoing optimisation — the weekly / monthly / quarterly cadence
- H2 — Post strategy (link to T129 for detailed frequency guide)
- H2 — Reviews strategy (link to T44 — Tranche 6)
- H2 — Q&A section (seed and monitor)
- H2 — Messaging (turn on or leave off? — honest answer)
- H2 — Insights — what to actually check monthly
- H2 — In my client work — the GBP setup I run for solo service businesses
- H2 — FAQ (8 items)
- Author bio card

### Internal links OUT

- T42 (citations — Tranche 6), T43 (location pages), T44 (Tranche 6), T127 (AI Overviews local), T129 (posting frequency)
- `/services/seo/`, `/learn/seo/`, `/locations/`

### Internal links IN

- `/learn/seo/` pillar (Local SEO H2 — pillar reference), `/services/seo/` (top 6), 3 location pages (Tranche 4 upward link), T127, T129

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (setup sequence)

### EEAT

- Byline, dates, first-person client GBP setup story, screenshots of Vraj's own 3-city GBP setups (dated)

### Media

- Hero: GBP profile visual
- Screenshots: real Vraj GBP for Surat, Ahmedabad, Bangalore (as anchors for Tranche 4 location pages)
- Setup checklist visual
- Author photo, OG image

### Notes

- Parent piece for the local SEO cluster (T41, T42, T43, T44, T127, T129).
- Working example = Vraj's 3-city GBPs.
- FAQ answers include "Contact for quote" at least once.

---

## Page 40 — T43: Location page content that's not a doorway page

| Field | Value |
|---|---|
| **URL** | `/learn/seo/location-pages-not-doorway-pages/` |
| **Page type** | Cluster content — framework |
| **Primary keyword** | `location pages seo doorway pages` |
| **Secondary keywords** | seo location pages best practices · avoid doorway pages location · unique content location pages |
| **Search intent** | Informational |
| **H1** | Location Pages That Google Ranks — And Doesn't Flag as Doorways |
| **Meta title** | Location Pages vs Doorway Pages — Vraj Vithalani *(48 chars → expand: SEO Location Pages Without Doorway Penalty — Vraj = 51 chars)* |
| **Meta description** | The concrete template for city × service location pages that carry real local content — landmarks, local FAQ, service-area schema — not spun copies. *(151 chars)* |
| **Content format** | Framework |
| **Word count target** | 3,000–3,500 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — What makes a page "a doorway page" in Google's eyes (2026 guidelines)
- H2 — The location-page template (from this site's 12 city × service pages)
  - H3 — Local landmarks section
  - H3 — Local relevance (why this city, what's different)
  - H3 — Local FAQ (city-specific concerns)
  - H3 — Local schema (LocalBusiness with areaServed + geo)
  - H3 — Local proof (real client references from the city where possible)
- H2 — Word-count logic (1,500–2,000 for a real page vs the 300-word doorway trap)
- H2 — The service-area-business framing (when you don't have a storefront in every city)
- H2 — In my working example — the 12 pages this site is deploying
- H2 — Common mistakes (find-and-replace city name, no landmarks, no local FAQ, LocalBusiness with fake address)
- H2 — How to scale beyond 3 cities without triggering doorway detection
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T38 (hub-and-spoke), T41 (GBP solo), T127 (AI Overviews local)
- `/services/seo/`, `/learn/seo/`, `/locations/`, all 12 location pages (Tranche 4)

### Internal links IN

- `/learn/seo/` pillar (Local SEO H2), `/services/seo/`, 12 location pages (upward link — Tranche 4), T41

### Schema

- **Article** + **FAQPage** + **BreadcrumbList**

### EEAT

- Byline, dates, working-example (12 pages on this site), first-person "what I ship for clients" block

### Media

- Hero: doorway vs real-location page comparison visual
- Screenshot: one of this site's actual location pages
- Location-page template diagram
- Author photo, OG image

### Notes

- Meta-demonstration: the 12 location pages are the working example.
- FAQ answers include "Contact for quote" at least once.

## Page 41 — T54: Next.js personal-brand site optimised for Google and LLMs

| Field | Value |
|---|---|
| **URL** | `/learn/web-development/nextjs-personal-brand-google-llms/` |
| **Page type** | Cluster content — guide |
| **Primary keyword** | `nextjs personal brand website seo` |
| **Secondary keywords** | nextjs seo llm optimization · nextjs for personal brand · nextjs site chatgpt visibility |
| **Search intent** | Informational |
| **H1** | Building a Next.js Personal-Brand Site Optimised for Both Google and LLMs |
| **Meta title** | Next.js for Personal Brand — Google + LLMs — Vraj Vithalani *(58 chars)* |
| **Meta description** | The exact Next.js build for a personal-brand site that ranks in Google AND gets cited by ChatGPT and Perplexity — with real code snippets from vrajvithalani.com. *(163 → 158)* |
| **Content format** | Guide + code walkthrough |
| **Word count target** | 3,500–4,500 |
| **CTA** | Soft link → `/services/web-development/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why Next.js is a good fit for a personal-brand site in 2026
- H2 — The rendering-strategy call (SSR vs SSG vs ISR for a content-first personal site)
- H2 — SEO-native from day one (metadata API, sitemap, robots, canonical, hreflang)
- H2 — LLM-native from day one
  - H3 — Person + Organization JSON-LD in root layout
  - H3 — Short-answer block components
  - H3 — Semantic HTML5 landmarks
  - H3 — Bing Webmaster + IndexNow (link to T128)
- H2 — Performance from day one (Core Web Vitals — LCP, CLS, INP)
- H2 — Content authoring workflow (MDX vs headless CMS choice)
- H2 — Deployment (Hostinger vs Vercel — link to T55 — Tranche 6)
- H2 — In my working example — vrajvithalani.com's build laid open
- H2 — Copyable code snippets
  - H3 — Root layout with Person + Organization schema
  - H3 — Short-answer block component
  - H3 — Article page with Article + FAQPage schema
  - H3 — sitemap.xml generation
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T34 (schema types), T47, T48, T117 (Next.js for LLM citation — closest sibling), T128, T55 (Tranche 6)
- `/services/web-development/`, `/services/seo/`, `/learn/web-development/`, `/learn/seo/`

### Internal links IN

- `/learn/web-development/` pillar (Next.js H2), `/services/web-development/` (top 6), `/services/seo/`, T117, T47

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (build sequence)

### EEAT

- Byline, dates, working-example is this site, live code from the same build being described, first-person "how I shipped this" block

### Media

- Hero: Next.js + Google + LLM stack visual
- Code screenshots (annotated)
- Screenshot: real Google search result showing this site
- Screenshot: real ChatGPT/Perplexity retrieval citing this site
- Author photo, OG image

### Notes

- Sibling to T117; T54 is the "how to build it" guide, T117 is the "engineered specifically for LLM citation" deeper piece.
- Cross-pillar with SEO (schema, GEO) — link both directions.
- FAQ answers include "Contact for quote" at least once.

---

## Page 42 — T59: Razorpay checkout on WordPress the right way

| Field | Value |
|---|---|
| **URL** | `/learn/web-development/razorpay-checkout-wordpress/` |
| **Page type** | Cluster content — tutorial |
| **Primary keyword** | `razorpay woocommerce integration` |
| **Secondary keywords** | razorpay wordpress integration · razorpay checkout wordpress · razorpay plugin woocommerce |
| **Search intent** | Informational |
| **H1** | Integrating Razorpay Checkout on WordPress — the Complete 2026 Setup |
| **Meta title** | Razorpay Checkout on WordPress — Vraj Vithalani *(47 chars → expand: Razorpay Checkout on WordPress the Right Way — Vraj = 51 chars)* |
| **Meta description** | The full Razorpay + WordPress integration with pre-launch testing, failure handling, refund flow, and GST invoice generation — from a live production setup. *(159 chars)* |
| **Content format** | Tutorial |
| **Word count target** | 3,000–4,000 |
| **CTA** | Soft link → `/services/web-development/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Choosing your integration path (WooCommerce plugin, custom plugin, custom code)
- H2 — Prerequisites — Razorpay account, KYC, API keys, webhook endpoint
- H2 — The setup — step by step
  - H3 — Installing + configuring the Razorpay WooCommerce plugin
  - H3 — Test-mode integration + test cards
  - H3 — Payment flow (order → checkout → capture → webhook)
  - H3 — Webhook setup for order confirmation
  - H3 — Refund handling
  - H3 — Subscription setup (if relevant)
- H2 — GST invoice generation post-payment (link to T61 — Tranche 7)
- H2 — Failure handling (what to show on failed payment, retry logic, customer support flow)
- H2 — Pre-launch testing checklist (10 items)
- H2 — Common integration failures and fixes
- H2 — In my client work — the Razorpay setup I shipped for Dreams Astro (courses + payment plans)
- H2 — Comparison with Cashfree and PayU (link to T60 — Tranche 6)
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T60 (Tranche 6), T61 (Tranche 7), T68 (Tranche 7)
- `/services/web-development/`, `/learn/web-development/`, `/case-studies/dreams-astro/`

### Internal links IN

- `/learn/web-development/` pillar (Razorpay H2), `/services/web-development/` (top 6), Dreams Astro case study, T60

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (integration steps)

### EEAT

- Byline, dates, first-person Dreams Astro live-integration story, real code snippets, real webhook payload examples

### Media

- Hero: Razorpay + WooCommerce integration visual
- Code screenshots (annotated)
- Screenshot: test-mode transaction flow
- Author photo, OG image

### Notes

- Working example = Dreams Astro (WordPress + Razorpay + course platform, per Doc 01).
- Cross-links with T60 (comparison) and T61 (GST).
- FAQ answers include "Contact for quote" at least once.

---

## Page 43 — T62: Hardening a WordPress site with WordFence and 2FA

| Field | Value |
|---|---|
| **URL** | `/learn/web-development/wordfence-2fa-hardening/` |
| **Page type** | Cluster content — guide |
| **Primary keyword** | `wordpress 2fa wordfence setup` |
| **Secondary keywords** | wordpress security wordfence 2fa · secure wordpress login two factor · wordpress hardening checklist |
| **Search intent** | Informational |
| **H1** | The 8-Step WordPress Hardening Setup with WordFence and 2FA (30 Minutes) |
| **Meta title** | WordPress Hardening with WordFence + 2FA — Vraj Vithalani *(58 chars)* |
| **Meta description** | The 8-step WordPress hardening a solo owner can complete in 30 minutes — WordFence, 2FA, login lockdown, file permissions, and backup basics. *(146 chars → expand to 155)* |
| **Content format** | Guide |
| **Word count target** | 2,500–3,000 |
| **CTA** | Soft link → `/services/web-development/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why the "solo owner, no security team" framing changes the answer
- H2 — The 8 steps in order
  - H3 — Install + configure WordFence (free tier is enough for most)
  - H3 — Enable 2FA on all admin logins
  - H3 — Change default admin username + strong password
  - H3 — Lock down wp-admin (IP allowlist if practical)
  - H3 — Disable file editing in wp-config
  - H3 — Set correct file permissions (644/755)
  - H3 — Set up a scheduled backup (link to T65 — Tranche 7)
  - H3 — Monitor + review WordFence alerts weekly
- H2 — What NOT to over-do (30 plugins, aggressive firewall rules, over-tight cache rules)
- H2 — When to graduate from free WordFence to paid or to a managed WAF
- H2 — In my client work — the hardening I run on every WordPress handover
- H2 — Recovery — if you're reading this because you're already hacked (link to T64 — Tranche 7)
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T26 (audit), T64 (Tranche 7), T65 (Tranche 7)
- `/services/web-development/`, `/learn/web-development/`

### Internal links IN

- `/learn/web-development/` pillar (Security H2), `/services/web-development/` (top 6), T26, T64

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (8 steps)

### EEAT

- Byline, dates, first-person client-handover story, real WordFence screenshots

### Media

- Hero: WordPress + shield visual
- Screenshots: WordFence config, 2FA setup, file permissions
- Author photo, OG image

### Notes

- 30-minute framing per Phase 1b — "solo owner, no security team" positioning.
- Cross-links with T64 (recovery) and T65 (backup).
- FAQ answers include "Contact for quote" at least once.

## Page 44 — T69: The 8-element service-business landing page checklist

| Field | Value |
|---|---|
| **URL** | `/learn/cro-and-automation/service-business-landing-page-checklist/` |
| **Page type** | Cluster content — checklist |
| **Primary keyword** | `service business landing page checklist` |
| **Secondary keywords** | high converting landing page checklist · lead gen landing page elements · landing page elements that convert |
| **Search intent** | Info-commercial |
| **H1** | The 8-Element Service-Business Landing Page That Converts |
| **Meta title** | Service Business Landing Page Checklist — Vraj Vithalani *(56 chars)* |
| **Meta description** | The 8 elements every service-business landing page needs — in the order to build them and the mistakes that skip them. From real client conversions. *(150 chars)* |
| **Content format** | Checklist + framework |
| **Word count target** | 3,000–3,500 |
| **CTA** | Soft link → `/services/cro-and-automation/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why 8 elements (not 4, not 20)
- H2 — Element 1: Above-fold value proposition (H1 + one-line clarity)
- H2 — Element 2: Trust bar (client logos or credentials, real, no stock)
- H2 — Element 3: Problem framing (the user's actual problem, in their words)
- H2 — Element 4: Service description (what you actually deliver, no jargon)
- H2 — Element 5: Social proof (testimonials, case study links, real results)
- H2 — Element 6: Objection handling (the 3 real objections, addressed)
- H2 — Element 7: Clear CTA (form + WhatsApp, no ambiguity)
- H2 — Element 8: Post-click clarity (what happens after they submit)
- H2 — The order to build them (spine first, then flesh, then polish)
- H2 — The 3 mistakes that skip these elements
- H2 — In my client work — a landing page rebuild that improved conversion 3x
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T14 (LP + QS), T70 (form length — Tranche 7), T71 (trust signals — Tranche 7), T76 (WhatsApp funnel), T112 (speed × QS × SEO)
- `/services/cro-and-automation/`, `/learn/cro-and-automation/`, `/services/google-ads/` (LP + Ads compound)

### Internal links IN

- `/learn/cro-and-automation/` pillar (Landing page H2), `/services/cro-and-automation/` (top 6), `/services/google-ads/` (cross-pillar), T14

### Schema

- **Article** + **FAQPage** + **BreadcrumbList**

### EEAT

- Byline, dates, first-person client 3x-improvement story with real before/after numbers, real client attribution

### Media

- Hero: 8-element landing page annotated visual
- Before/after landing page screenshots (real, anonymised)
- Author photo, OG image

### Notes

- Cross-pillar with Google Ads — LP is the compound story anchor.
- FAQ answers include "Contact for quote" at least once.

---

## Page 45 — T76: WhatsApp-first lead-capture funnel for a service business

| Field | Value |
|---|---|
| **URL** | `/learn/cro-and-automation/whatsapp-first-lead-capture-funnel/` |
| **Page type** | Cluster content — guide |
| **Primary keyword** | `whatsapp lead capture funnel service business` |
| **Secondary keywords** | whatsapp funnel india · click to whatsapp ad funnel · whatsapp lead automation small business |
| **Search intent** | Info-commercial |
| **H1** | The WhatsApp-First Lead-Capture Funnel That Actually Works for Indian Service Businesses |
| **Meta title** | WhatsApp-First Lead Funnel for Service Business — Vraj *(54 chars)* |
| **Meta description** | The provider-agnostic WhatsApp funnel — Click-to-WhatsApp or website button through qualification through human handoff — built from real Indian SMB deployments. *(160 chars)* |
| **Content format** | Guide |
| **Word count target** | 3,000–4,000 |
| **CTA** | Soft link → `/services/cro-and-automation/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why WhatsApp beats email as India's default lead channel
- H2 — The funnel shape (Ad or website → WhatsApp entry → qualification → human handoff → close)
- H2 — Entry points
  - H3 — Click-to-WhatsApp ads (Meta + Google)
  - H3 — Website button (floating + inline)
  - H3 — Instant Forms → WhatsApp routing
  - H3 — QR codes for offline entry
- H2 — The qualification message sequence (3 messages, 2 questions, 1 handoff)
- H2 — Human handoff protocol (response time, tone, next steps)
- H2 — When to use Business App vs API (link to T75 — Tranche 6)
- H2 — Tool-picking (provider-agnostic framework — AiSensy, WATI, Interakt, DoubleTick, etc.)
- H2 — Tracking WhatsApp conversions back to Ads / SEO
- H2 — In my client work — the WhatsApp funnel I ship for service businesses
- H2 — FAQ (8 items)
- Author bio card

### Internal links OUT

- T24 (Instant Forms vs LP — Tranche 6), T75 (Tranche 6), T77 (form routing — Tranche 7), T69 (landing page checklist)
- `/services/cro-and-automation/`, `/learn/cro-and-automation/`, `/services/google-ads/` (Click-to-WhatsApp)

### Internal links IN

- `/learn/cro-and-automation/` pillar (WhatsApp H2), `/services/cro-and-automation/` (top 6), `/services/google-ads/`, T69, sibling CRO clusters

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (funnel sequence)

### EEAT

- Byline, dates, first-person client funnel story with real message templates, provider-agnostic framing (no affiliate bias)

### Media

- Hero: WhatsApp funnel flow diagram
- Screenshot: sample qualification message thread
- Author photo, OG image

### Notes

- Provider-agnostic framing per Phase 1b — the ownable angle vs BSP-affiliated content.
- Cross-pillar with Google Ads (Click-to-WhatsApp ads).
- FAQ answers include "Contact for quote" at least once.

---

## Page 46 — T89: Google Ads for industrial exporters targeting overseas buyers

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/google-ads-for-industrial-exporters/` |
| **Page type** | Cluster content — guide (Zone 5.3 vertical, filed under Google Ads pillar) |
| **Primary keyword** | `google ads for industrial exporters india` |
| **Secondary keywords** | google ads for manufacturers india · b2b google ads india · export google ads india |
| **Search intent** | Info-commercial |
| **H1** | Google Ads for Indian Industrial Exporters Targeting Overseas Buyers |
| **Meta title** | Google Ads for Industrial Exporters India — Vraj Vithalani *(58 chars)* |
| **Meta description** | The RFQ funnel from an Indian exporter to an overseas buyer — geo targeting, keyword strategy, trust signals, and the campaign shape that survives first contact. *(161 → 158)* |
| **Content format** | Guide |
| **Word count target** | 3,500–4,500 |
| **CTA** | Soft link → `/services/google-ads/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why exporter Google Ads is a different playbook from local service or D2C
- H2 — The buyer journey — how an overseas buyer actually finds an Indian supplier
- H2 — Geo targeting — the country + region mix that produces qualified leads (not tire-kickers)
- H2 — Keyword strategy — product-family + buyer-intent + regional-language modifiers
- H2 — Ad copy that establishes credibility fast (certifications, capacity, MOQ, export experience)
- H2 — Landing page — the 8-page exporter site skeleton (link to T91 — Tranche 6)
- H2 — Inquiry-form vs Instant-Form for exporters (the WhatsApp handoff differs for overseas buyers)
- H2 — Lead-qualification flow (link to T92 — Tranche 7)
- H2 — Budget calibration for exporter campaigns (usually higher CPC, longer sales cycle — ROI reads differently)
- H2 — In my client work — VM Graphite Industries and Powercable (real exporter campaigns)
- H2 — Trust signals for overseas buyers (compliance, certifications, testimonials, factory imagery)
- H2 — FAQ (8 items)
- Author bio card

### Internal links OUT

- T90 (SEO for B2B manufacturing — sibling Zone 5.3), T91 (Tranche 6), T92 (Tranche 7), T14 (LP + QS), T21 (budget)
- `/services/google-ads/`, `/learn/google-ads/`, `/case-studies/vm-graphite/`, `/case-studies/powercable/`

### Internal links IN

- `/learn/google-ads/` pillar (Vertical H2), `/services/google-ads/` (top 6), VM Graphite + Powercable case studies, T90 (sibling)

### Schema

- **Article** + **FAQPage** + **BreadcrumbList**

### EEAT

- Byline, dates, first-person real exporter-campaign story, VM Graphite + Powercable named as working examples

### Media

- Hero: exporter Google Ads funnel visual
- Screenshot: real (anonymised) exporter ad + LP + inquiry form
- Country-targeting map
- Author photo, OG image

### Notes

- Zone 5.3 vertical filed under Google Ads pillar per Phase 1a rule.
- Working examples: VM Graphite + Powercable.
- FAQ answers include "Contact for quote" at least once.

---

## Page 47 — T90: SEO for B2B manufacturing — building international authority from India

| Field | Value |
|---|---|
| **URL** | `/learn/seo/seo-for-b2b-manufacturing-india-overseas/` |
| **Page type** | Cluster content — guide (Zone 5.3 vertical, filed under SEO pillar) |
| **Primary keyword** | `b2b manufacturing seo india international` |
| **Secondary keywords** | seo for industrial company · seo for manufacturers india · b2b industrial seo strategy |
| **Search intent** | Info-commercial |
| **H1** | SEO for Indian B2B Manufacturers — Building International Authority from India |
| **Meta title** | SEO for B2B Manufacturing India → Overseas — Vraj Vithalani *(59 chars)* |
| **Meta description** | The SEO stack for an Indian manufacturer courting overseas buyers — hreflang decisions, content depth, credibility signals, and the exporter site architecture. *(159 chars)* |
| **Content format** | Guide |
| **Word count target** | 3,500–4,500 |
| **CTA** | Soft link → `/services/seo/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why US/EU-focused SEO frameworks don't fit an Indian exporter
- H2 — The overseas-buyer search behaviour (informational → comparison → RFQ)
- H2 — Site architecture for an exporter (link to T91 — Tranche 6)
- H2 — hreflang — when to use it, when to skip (the honest answer for a small manufacturer)
- H2 — Content depth by product family (spec sheets, application content, certifications content)
- H2 — Credibility signals for an overseas buyer evaluating an Indian supplier
  - H3 — About/company page requirements
  - H3 — Certifications visibility (ISO, BIS, industry-specific)
  - H3 — Case studies from named export markets
  - H3 — Factory imagery + team photos
  - H3 — Compliance and trade documentation
- H2 — Technical SEO for exporter WordPress sites (link to T26)
- H2 — Off-site — building international authority from India (industry directories, guest posts, trade-show mentions)
- H2 — Local SEO for the manufacturer's Indian home city (still matters)
- H2 — In my client work — VM Graphite Industries + Powercable SEO
- H2 — FAQ (8 items)
- Author bio card

### Internal links OUT

- T89 (Google Ads for exporters — sibling), T91 (Tranche 6), T26, T34, T38, T43
- `/services/seo/`, `/learn/seo/`, `/case-studies/vm-graphite/`, `/case-studies/powercable/`

### Internal links IN

- `/learn/seo/` pillar (Vertical H2), `/services/seo/` (top 6), VM Graphite + Powercable case studies, T89 (sibling)

### Schema

- **Article** + **FAQPage** + **BreadcrumbList**

### EEAT

- Byline, dates, first-person exporter-SEO story, real client attribution, working knowledge of overseas-buyer behaviour

### Media

- Hero: India → world SEO visual
- Diagram: exporter site architecture (8-page skeleton)
- Screenshot: real exporter site (Powercable or VM Graphite)
- Author photo, OG image

### Notes

- Zone 5.3 vertical filed under SEO pillar per Phase 1a rule.
- Working examples: VM Graphite + Powercable.
- Cross-links with T89 (sibling vertical piece).
- FAQ answers include "Contact for quote" at least once.

## Page 48 — T100: Realistic digital-marketing budget expectations for an Indian SMB

| Field | Value |
|---|---|
| **URL** | `/learn/google-ads/digital-marketing-budget-indian-smb/` |
| **Page type** | Cluster content — framework (Zone 6 founder perspective — filed under Google Ads pillar per closest keyword intent) |
| **Primary keyword** | `digital marketing budget small business india` |
| **Secondary keywords** | how much to spend on digital marketing india · marketing budget for small business india · digital marketing cost india |
| **Search intent** | Info-commercial |
| **H1** | Realistic Digital-Marketing Budget Expectations for an Indian SMB in 2026 |
| **Meta title** | Digital Marketing Budget for Indian SMBs 2026 — Vraj *(52 chars)* |
| **Meta description** | The honest 5-tier digital-marketing budget guide for Indian SMBs — ad spend vs retainer spend, what each tier gets you, and when to jump tiers. *(148 chars → 156)* |
| **Content format** | Framework |
| **Word count target** | 3,500–4,500 |
| **CTA** | Soft link → `/services/` (hub — this piece is cross-service by nature) |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why most Indian budget guides mislead (retainer vs ad spend conflation)
- H2 — The 5 tiers by monthly total spend
  - H3 — Tier 1: ₹10k–₹25k/month (survival marketing — GBP + organic + one channel test)
  - H3 — Tier 2: ₹25k–₹60k/month (real Google Ads test + basic SEO + basic tracking)
  - H3 — Tier 3: ₹60k–₹1.5L/month (Ads + SEO + CRO working together)
  - H3 — Tier 4: ₹1.5L–₹4L/month (multi-channel + team + tools)
  - H3 — Tier 5: ₹4L+/month (full-stack retainer + significant ad spend + specialists)
- H2 — The ad-spend vs retainer split rule (why 70/30 or 80/20 is common)
- H2 — When to jump a tier vs when to hold
- H2 — What each tier actually delivers (lead volume, timeline, brand impact)
- H2 — Common mistakes at each tier
- H2 — In my client work — the tier conversations I have with founders
- H2 — FAQ (8 items)
- Author bio card

### Internal links OUT

- T21 (min Google Ads budget), T22 (₹15k test), T97 (Tranche 6 — hire GA consultant), T101 (Tranche 7 — cheap SEO), T100 self-context
- `/services/` (services hub — this piece spans all pillars), `/services/google-ads/`, `/services/seo/`, `/services/cro-and-automation/`, `/learn/google-ads/`, `/learn/seo/`, `/learn/cro-and-automation/`

### Internal links IN

- `/learn/google-ads/` pillar (Budget H2), `/services/` hub, `/services/google-ads/`, T21, T22, T125 (Tranche 7 — cost breakdown)

### Schema

- **Article** + **FAQPage** + **BreadcrumbList**

### EEAT

- Byline, dates, first-person founder-conversation block, real INR anchors across all 5 tiers, honest tier-jump signals

### Media

- Hero: 5-tier budget ladder visual (INR)
- Table: what each tier gets you (channels, deliverables, timeline)
- Author photo, OG image

### Notes

- Zone 6 (founder perspective) topic — filed under Google Ads pillar because budget queries map most closely to Ads keyword intent. Cross-links to all 4 service pillars because the topic spans them.
- INR-anchored per Phase 1b — the Indian SMB angle is loudest here.
- FAQ answers include "Contact for quote" at least once.

---

## Page 49 — T112: Landing-page speed and its impact on both SEO and Google Ads Quality Score

| Field | Value |
|---|---|
| **URL** | `/learn/cro-and-automation/landing-page-speed-quality-score-seo/` |
| **Page type** | Cluster content — teardown (cross-zone Zones 1+2+3) |
| **Primary keyword** | `landing page speed seo google ads quality score` |
| **Secondary keywords** | core web vitals ppc impact · page speed quality score · speed seo ppc impact |
| **Search intent** | Informational |
| **H1** | Landing-Page Speed × Google Ads Quality Score × SEO — The Compound Payoff |
| **Meta title** | Landing Page Speed × QS × SEO — Vraj Vithalani *(46 chars → expand: Landing Page Speed, QS & SEO Impact — Vraj Vithalani = 53 chars)* |
| **Meta description** | The dollar/rupee value of Core Web Vitals as reduced CPC AND higher rankings, with a real client example showing both effects from a single speed intervention. *(159 chars)* |
| **Content format** | Teardown |
| **Word count target** | 3,000–4,000 |
| **CTA** | Soft link → `/services/cro-and-automation/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why speed is the rare metric that pays back on 3 axes (CPC + rankings + conversion)
- H2 — The Core Web Vitals — LCP, CLS, INP (2026 targets, not 2022)
- H2 — How Google Ads Quality Score weighs page speed
- H2 — How Google organic ranking weighs page speed
- H2 — How conversion rate compounds from speed
- H2 — Diagnostic — where speed is usually lost (images, JS, third-party, host)
- H2 — Fix priority (server → images → JS → third-party → CDN)
- H2 — WordPress-specific fixes (link to T51 — Tranche 6)
- H2 — Next.js-specific fixes
- H2 — In my client work — a speed intervention that dropped CPC 22% and lifted rankings 4 positions
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T14 (LP + QS), T26 (WP audit), T51 (Tranche 6 — WP speed), T54 (Next.js build)
- `/services/cro-and-automation/`, `/services/google-ads/`, `/services/seo/`, `/services/web-development/`, `/learn/cro-and-automation/`, `/learn/google-ads/`, `/learn/seo/`

### Internal links IN

- `/learn/cro-and-automation/` pillar (Cross-zone H2), `/learn/google-ads/` (LP integration H2), `/learn/seo/` (Technical SEO H2), all 4 service pillars (this is a cross-zone piece)

### Schema

- **Article** + **FAQPage** + **BreadcrumbList**

### EEAT

- Byline, dates, first-person client-example block with real CPC drop + ranking lift numbers, before/after PageSpeed screenshots

### Media

- Hero: 3-axis payoff visual (CPC + rankings + CR)
- Before/after PageSpeed Insights screenshots
- Author photo, OG image

### Notes

- **Cross-zone piece** — filed under CRO pillar per Phase 1b assignment; also linked from Google Ads and SEO pillars because it lives at the intersection.
- Compound-skill signature — nobody who runs one channel alone can honestly report this compound payoff.
- FAQ answers include "Contact for quote" at least once.

---

## Page 50 — T113: The launch checklist for a new service-business site — SEO-ready and Ads-ready from day one

| Field | Value |
|---|---|
| **URL** | `/learn/web-development/service-business-site-launch-checklist/` |
| **Page type** | Cluster content — checklist (cross-zone Zones 1+2+3) |
| **Primary keyword** | `new website launch seo ppc checklist` |
| **Secondary keywords** | website launch checklist seo ads · pre-launch checklist small business site · launch service website checklist |
| **Search intent** | Informational |
| **H1** | The 50-Item Launch Checklist for a New Service-Business Site — SEO-Ready and Ads-Ready From Day One |
| **Meta title** | Service Business Site Launch Checklist — Vraj Vithalani *(55 chars)* |
| **Meta description** | The 50-item launch checklist covering SEO, GA4, Google Ads readiness, schema, and legal — everything a new service-business site needs live from day one. *(154 chars)* |
| **Content format** | Checklist |
| **Word count target** | 3,500–4,500 |
| **CTA** | Soft link → `/services/web-development/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why the SEO-only and Ads-only checklists both miss things
- H2 — The 50 items grouped by category
  - H3 — Technical SEO (10 items — HTTPS, canonical, sitemap, robots, hreflang, GSC + Bing verification, indexation, etc.)
  - H3 — On-page SEO (8 items — H1s, meta titles, meta descriptions, schema, internal linking, image alts)
  - H3 — Analytics + tracking (8 items — GA4 setup, GTM setup, Google Ads conversion actions, Search Console, event tracking)
  - H3 — Legal + trust (6 items — Privacy, Terms, Cookie banner, GDPR/DPDP, Contact, SSL)
  - H3 — Performance (6 items — Core Web Vitals baseline, image WebP/AVIF, lazy loading, CDN, cache)
  - H3 — Content + navigation (6 items — 404, breadcrumbs, header nav, footer nav, search, RSS)
  - H3 — Ads-readiness (6 items — landing page URLs live, conversion tracking verified, test conversions fired, Ads account linked, remarketing tags, negatives seeded)
- H2 — The launch-week sequence (order of operations across the checklist)
- H2 — The 24-hour post-launch monitoring checklist
- H2 — In my client work — the launch protocol I run
- H2 — Downloadable full checklist (PDF + Google Sheet)
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T1, T3, T26, T27, T34, T38, T41, T51 (Tranche 6), T62, T69, T112, T117
- `/services/web-development/`, `/services/google-ads/`, `/services/seo/`, `/services/cro-and-automation/`, `/learn/web-development/`

### Internal links IN

- `/learn/web-development/` pillar (Launch H2), all 4 service pillars (cross-zone piece), `/case-studies/drvishva/` (launching-soon example), `/case-studies/vitthalshringar/`

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (50-item sequence)

### EEAT

- Byline, dates, first-person client-launch story (drvishva/Vitthalshringar/Powercable/Trust NGO), downloadable checklist PDF + Google Sheet

### Media

- Hero: 50-item checklist visual
- Downloadable checklist card
- Timeline visual (launch-week sequence)
- Author photo, OG image

### Notes

- Cross-zone piece filed under Web Dev pillar (launch is a build activity); links from all 4 service pillars.
- Downloadable full checklist is the shareable artifact.
- FAQ answers include "Contact for quote" at least once.

---

## Page 51 — T117: Building a Next.js site engineered specifically for LLM citation

| Field | Value |
|---|---|
| **URL** | `/learn/web-development/nextjs-site-for-llm-citation/` |
| **Page type** | Cluster content — guide (cross-zone Zones 2+3) |
| **Primary keyword** | `nextjs site llm optimization` |
| **Secondary keywords** | nextjs for llm search · nextjs generative engine optimization · build website for chatgpt citation |
| **Search intent** | Informational |
| **H1** | Building a Next.js Site Engineered Specifically for LLM Citation |
| **Meta title** | Next.js Site for LLM Citation — Vraj Vithalani *(46 chars → expand: Next.js Site Engineered for LLM Citation — Vraj = 47 → 51 chars)* |
| **Meta description** | The exact Next.js build patterns that make a site LLM-extractable — component structure, schema, sitemap, and Bing setup — with live code from this site. *(155 chars)* |
| **Content format** | Guide + code walkthrough |
| **Word count target** | 3,500–4,500 |
| **CTA** | Soft link → `/services/web-development/` |

### Content structure

- H1, byline, short-answer block, TOC
- H2 — Why "LLM citation-optimised" is different from "SEO-optimised"
- H2 — The 5 patterns
  - H3 — Pattern 1: Short-answer block component (link to T46)
  - H3 — Pattern 2: JSON-LD site-wide layout (Person + Organization + Article per page)
  - H3 — Pattern 3: Semantic HTML5 landmarks (article, section, aside)
  - H3 — Pattern 4: Sitemap + Bing IndexNow (link to T128)
  - H3 — Pattern 5: Entity `@id` consistency across every schema block
- H2 — File-by-file walkthrough of this site's Next.js implementation
- H2 — The metadata API — canonical, OG, Twitter, JSON-LD in one place
- H2 — MDX components for authoring — short-answer, FAQ, table-of-contents
- H2 — Build-time vs runtime tradeoffs (SSG default, ISR for updated content)
- H2 — Testing — how to verify a page is LLM-extractable before publishing
- H2 — In my working example — vrajvithalani.com's build, laid open
- H2 — FAQ (7 items)
- Author bio card

### Internal links OUT

- T46, T47, T48, T54 (Next.js personal brand — closest sibling), T117 self-context, T128
- `/services/web-development/`, `/services/seo/`, `/learn/web-development/`, `/learn/seo/`

### Internal links IN

- `/learn/web-development/` pillar (LLM citation H2), `/services/web-development/` (top 6), `/services/seo/`, T54, T47

### Schema

- **Article** + **FAQPage** + **BreadcrumbList** + **HowTo** (build patterns)

### EEAT

- Byline, dates, working-example is this site, live code snippets from the same build, first-person "why I built it this way" block

### Media

- Hero: Next.js + LLM citation visual
- Annotated code screenshots
- Screenshot: real ChatGPT / Perplexity retrieval citing this site
- Author photo, OG image

### Notes

- Sibling to T54; T54 is the general Next.js personal-brand guide, T117 is the deeper "engineered for LLM citation" piece.
- Cross-pillar with SEO — the LLM-citation topic overlaps GEO cluster heavily.
- FAQ answers include "Contact for quote" at least once.

---

## Tranche 3 — Summary at a Glance

| # | URL | Type | Primary keyword | Word count | T# |
|---|---|---|---|---|---|
| 14 | `/learn/google-ads/` | Content pillar | google ads guide india | 5,000–7,000 | — |
| 15 | `/learn/seo/` | Content pillar | seo guide india | 5,000–7,000 | — |
| 16 | `/learn/web-development/` | Content pillar | web development guide india | 5,000–7,000 | — |
| 17 | `/learn/cro-and-automation/` | Content pillar | cro guide india | 5,000–7,000 | — |
| 18 | `/learn/seo/what-is-generative-engine-optimization/` | Cluster | what is generative engine optimization | 2,500–3,000 | T45 |
| 19 | `/learn/seo/short-answer-block-llm-extraction/` | Cluster | short answer block seo llm | 2,500–3,000 | T46 |
| 20 | `/learn/seo/appear-in-chatgpt-perplexity-ai-mode/` | Cluster | how to appear in chatgpt search results | 3,500–4,500 | T47 |
| 21 | `/learn/seo/entity-establishment-llm-era/` | Cluster | entity establishment seo person | 3,000–4,000 | T48 |
| 22 | `/learn/seo/llm-content-audit-website/` | Cluster | llm content audit website | 2,500–3,500 | T49 |
| 23 | `/learn/seo/ai-overviews-local-service-business/` | Cluster | ai overviews local service business | 2,500–3,500 | T127 |
| 24 | `/learn/seo/bing-indexing-chatgpt-visibility/` | Cluster | bing indexing chatgpt visibility | 2,500–3,000 | T128 |
| 25 | `/learn/seo/gbp-posting-frequency-2026/` | Cluster | gbp posting frequency 2026 | 2,500–3,000 | T129 |
| 26 | `/learn/google-ads/google-ads-account-structure-service-business/` | Cluster | how to structure google ads account for small business | 3,000–4,000 | T1 |
| 27 | `/learn/google-ads/minimum-tracking-stack-pre-launch/` | Cluster | google ads conversion tracking setup checklist | 2,500–3,500 | T3 |
| 28 | `/learn/google-ads/performance-max-without-creative-team/` | Cluster | performance max campaign structure small business | 3,000–3,500 | T5 |
| 29 | `/learn/google-ads/google-ads-clicks-no-conversions/` | Cluster | google ads clicks but no conversions | 3,000–4,000 | T13 |
| 30 | `/learn/google-ads/landing-page-elements-quality-score/` | Cluster | landing page quality score google ads | 3,000–4,000 | T14 |
| 31 | `/learn/google-ads/12-point-google-ads-audit/` | Cluster | google ads account audit checklist | 3,500–4,500 | T17 |
| 32 | `/learn/google-ads/minimum-google-ads-budget-that-works/` | Cluster | minimum google ads budget small business | 2,500–3,500 | T21 |
| 33 | `/learn/google-ads/google-ads-15000-rupees-test-protocol/` | Cluster | google ads budget 15000 rupees test | 3,000–4,000 | T22 |
| 34 | `/learn/google-ads/meta-ads-local-service-business/` | Cluster | meta ads for local service business | 2,500–3,500 | T25 |
| 35 | `/learn/seo/wordpress-technical-seo-audit-checklist/` | Cluster | wordpress technical seo audit checklist | 3,500–4,500 | T26 |
| 36 | `/learn/seo/wordpress-indexation-problems-fix/` | Cluster | wordpress indexation problems fix | 2,500–3,500 | T27 |
| 37 | `/learn/seo/schema-types-service-business-site/` | Cluster | schema markup for service business | 3,000–3,500 | T34 |
| 38 | `/learn/seo/hub-and-spoke-content-architecture/` | Cluster | hub and spoke content architecture seo | 3,000–4,000 | T38 |
| 39 | `/learn/seo/google-business-profile-solo-consultant/` | Cluster | google business profile setup solo consultant | 3,000–4,000 | T41 |
| 40 | `/learn/seo/location-pages-not-doorway-pages/` | Cluster | location pages seo doorway pages | 3,000–3,500 | T43 |
| 41 | `/learn/web-development/nextjs-personal-brand-google-llms/` | Cluster | nextjs personal brand website seo | 3,500–4,500 | T54 |
| 42 | `/learn/web-development/razorpay-checkout-wordpress/` | Cluster | razorpay woocommerce integration | 3,000–4,000 | T59 |
| 43 | `/learn/web-development/wordfence-2fa-hardening/` | Cluster | wordpress 2fa wordfence setup | 2,500–3,000 | T62 |
| 44 | `/learn/cro-and-automation/service-business-landing-page-checklist/` | Cluster | service business landing page checklist | 3,000–3,500 | T69 |
| 45 | `/learn/cro-and-automation/whatsapp-first-lead-capture-funnel/` | Cluster | whatsapp lead capture funnel service business | 3,000–4,000 | T76 |
| 46 | `/learn/google-ads/google-ads-for-industrial-exporters/` | Cluster · Zone 5.3 | google ads for industrial exporters india | 3,500–4,500 | T89 |
| 47 | `/learn/seo/seo-for-b2b-manufacturing-india-overseas/` | Cluster · Zone 5.3 | b2b manufacturing seo india international | 3,500–4,500 | T90 |
| 48 | `/learn/google-ads/digital-marketing-budget-indian-smb/` | Cluster · Zone 6 | digital marketing budget small business india | 3,500–4,500 | T100 |
| 49 | `/learn/cro-and-automation/landing-page-speed-quality-score-seo/` | Cluster · Cross-zone | landing page speed seo google ads quality score | 3,000–4,000 | T112 |
| 50 | `/learn/web-development/service-business-site-launch-checklist/` | Cluster · Cross-zone | new website launch seo ppc checklist | 3,500–4,500 | T113 |
| 51 | `/learn/web-development/nextjs-site-for-llm-citation/` | Cluster · Cross-zone | nextjs site llm optimization | 3,500–4,500 | T117 |

**Total pages in Tranche 3: 38** (4 pillars + 34 clusters). Total word-count target: ~130,000–170,000 words of published content.

**Zone distribution of clusters:**
- Zone 1 (Google Ads pillar): 11 clusters (T1, T3, T5, T13, T14, T17, T21, T22, T25, T89, T100)
- Zone 2 (SEO pillar): 12 clusters (T26, T27, T34, T38, T41, T43, T45, T46, T47, T48, T49, T90, T127, T128, T129) — 15 actually (miscounted above; verified list = 15)
- Zone 3 (Web Dev pillar): 5 clusters (T54, T59, T62, T113, T117)
- Zone 4 (CRO & Automation pillar): 3 clusters (T69, T76, T112)

Correction — SEO pillar carries the largest Tier 1 load because GEO topics (T45–T49 + T127–T128) all file under `/learn/seo/`. SEO cluster count = 15. Total clusters = 11 + 15 + 5 + 3 = 34. ✓

---

## Tranche 3 — Internal Linking Map (ASCII tree)

```
/learn/                                              (Learn hub — Tranche 1)
 │
 ├─→ /learn/google-ads/                              (Pillar — Page 14)
 │    │
 │    ├─→ Tier 1 clusters (Tranche 3):
 │    │    ├─→ T1  · account-structure-service-business
 │    │    ├─→ T3  · minimum-tracking-stack-pre-launch
 │    │    ├─→ T5  · performance-max-without-creative-team
 │    │    ├─→ T13 · google-ads-clicks-no-conversions
 │    │    ├─→ T14 · landing-page-elements-quality-score
 │    │    ├─→ T17 · 12-point-google-ads-audit
 │    │    ├─→ T21 · minimum-google-ads-budget-that-works
 │    │    ├─→ T22 · google-ads-15000-rupees-test-protocol
 │    │    ├─→ T25 · meta-ads-local-service-business
 │    │    ├─→ T89 · google-ads-for-industrial-exporters (Zone 5.3)
 │    │    └─→ T100· digital-marketing-budget-indian-smb (Zone 6)
 │    │
 │    ├─→ /services/google-ads/                      (upsell path)
 │    ├─→ Sibling pillars (/learn/seo/, /learn/web-development/, /learn/cro-and-automation/)
 │    └─→ Case studies (Powercable, Parv Travels, Synergy Tutorials, VM Graphite)
 │
 ├─→ /learn/seo/                                     (Pillar — Page 15)
 │    │
 │    ├─→ Tier 1 clusters (Tranche 3, 15 pieces):
 │    │    ├─→ T26 · wordpress-technical-seo-audit-checklist
 │    │    ├─→ T27 · wordpress-indexation-problems-fix
 │    │    ├─→ T34 · schema-types-service-business-site
 │    │    ├─→ T38 · hub-and-spoke-content-architecture
 │    │    ├─→ T41 · google-business-profile-solo-consultant
 │    │    ├─→ T43 · location-pages-not-doorway-pages
 │    │    │
 │    │    ├─→ GEO SUB-CLUSTER (published first — closing window):
 │    │    │    ├─→ T45 · what-is-generative-engine-optimization
 │    │    │    ├─→ T46 · short-answer-block-llm-extraction
 │    │    │    ├─→ T47 · appear-in-chatgpt-perplexity-ai-mode
 │    │    │    ├─→ T48 · entity-establishment-llm-era
 │    │    │    ├─→ T49 · llm-content-audit-website (Tier 2 pulled forward)
 │    │    │    ├─→ T127· ai-overviews-local-service-business (new)
 │    │    │    └─→ T128· bing-indexing-chatgpt-visibility (new)
 │    │    │
 │    │    ├─→ T129 · gbp-posting-frequency-2026 (new, Local SEO)
 │    │    └─→ T90  · seo-for-b2b-manufacturing-india-overseas (Zone 5.3)
 │    │
 │    ├─→ /services/seo/                             (upsell path)
 │    ├─→ Sibling pillars
 │    └─→ Case studies (drvishva, Powercable, Vitthalshringar, VM Graphite)
 │
 ├─→ /learn/web-development/                         (Pillar — Page 16)
 │    │
 │    ├─→ Tier 1 clusters (Tranche 3, 5 pieces):
 │    │    ├─→ T54  · nextjs-personal-brand-google-llms
 │    │    ├─→ T59  · razorpay-checkout-wordpress
 │    │    ├─→ T62  · wordfence-2fa-hardening
 │    │    ├─→ T113 · service-business-site-launch-checklist (Cross-zone)
 │    │    └─→ T117 · nextjs-site-for-llm-citation (Cross-zone 2+3)
 │    │
 │    ├─→ /services/web-development/                 (upsell path)
 │    ├─→ Sibling pillars
 │    └─→ Case studies (Powercable, drvishva, Vitthalshringar, Trust NGO, Dreams Astro, VM Graphite, IOTA overview)
 │
 └─→ /learn/cro-and-automation/                      (Pillar — Page 17)
      │
      ├─→ Tier 1 clusters (Tranche 3, 3 pieces):
      │    ├─→ T69  · service-business-landing-page-checklist
      │    ├─→ T76  · whatsapp-first-lead-capture-funnel
      │    └─→ T112 · landing-page-speed-quality-score-seo (Cross-zone 1+2+3)
      │
      ├─→ /services/cro-and-automation/              (upsell path)
      ├─→ Sibling pillars
      └─→ Case studies (Powercable, Vitthalshringar, drvishva, Parv Travels, Little Genius)
```

**Cross-cluster lateral links** (sibling cluster within same pillar): every cluster carries 2–3 lateral links to closely related sibling clusters. GEO cluster (T45–T49 + T127–T128) is densely cross-linked because the topics are highly interrelated.

**Cross-pillar cluster links** (cluster in one pillar linking to cluster in another): T14 ↔ T69 (LP compound); T14 ↔ T112 (speed compound); T112 ↔ everything (cross-zone by nature); T47 ↔ T128 (LLM citation via Bing); T54 ↔ T117 (Next.js sibling); T34 ↔ T48 (schema + entity).

**Upward links from every cluster:**
- Cluster → its Learn pillar (mandatory)
- Cluster → its Service pillar (via author bio card + explicit "Working with me" section on the pillar)

**Home page:** links to `/learn/` hub (via nav) + "recent articles" section featuring most recent 3–5 Learn cluster publications.

---

## Gaps observed

1. **T49 was pulled forward from Tier 2 to Tranche 3** per user's explicit "T45–T49 first" instruction (GEO window closing rationale). This changes Tranche 6's count from 37 → 36 pieces. Flagging so the count reconciles when Tranche 6 is produced.
2. **Tranche 3 total is 38 pages** (4 pillars + 34 clusters), which matches user's brief number of "~37" — the +1 comes from the T49 pull-forward. Everything reconciles.
3. **T100 filing decision**: I filed T100 (SMB marketing budget — Zone 6 founder perspective) under `/learn/google-ads/` because budget queries map most closely to Ads intent. Alternatives were `/learn/cro-and-automation/` (whole-stack budgeting) or a dedicated `/learn/founder/` pillar (which doesn't exist per Doc 03). If you'd prefer a different pillar for T100, flag before Phase 3 content writing starts.
4. **T113 filing decision**: I filed T113 (launch checklist SEO/Ads/CRO) under `/learn/web-development/` because a launch checklist is a build-adjacent activity. All 4 service pillars link to it. Flag if you'd prefer it under `/learn/seo/` instead.
5. **T112 filing decision**: kept per Phase 1b under `/learn/cro-and-automation/`; cross-linked from all 4 pillars per Phase 1b's compound-topic guidance.
6. **T22 in Google Ads pillar top-6 list**: current Tranche 2 pillar "Related guides" list is T1/T3/T13/T14/T17/T21. If you'd prefer T22 (the ₹15k test protocol) in that top-6 instead of T21 (the minimum-budget-that-works framework), swap. Flagged in Tranche 2's Gap #2 as well.
7. **T49 in SEO pillar top-6 list**: current Tranche 2 SEO pillar "Related guides" list is T26/T34/T38/T45/T46/T47. If T49 (now Tier 1 by pull-forward) deserves a slot, swap out T26 or T38. Recommendation: keep the Tranche 2 list unchanged, add T49 in the pillar-page article-index section (Tranche 3 Page 15 already includes it).
8. **NGO Tier 3 topics (T93–T96)** are NOT in Tranche 3 — they remain in Tier 3 per Phase 1b, `[VERIFY]` lifted, and land in Tranche 7. No physio Learn content anywhere per Doc 02 rule.
9. **Cross-pillar link density is deliberately moderate.** The 4×4 matrix from Tranche 2 (each pillar links to 2 of 3 others) is mirrored inside Tranche 3 at the cluster level — clusters carry 2–3 cross-pillar links maximum. Over-linking dilutes topical authority signals.
10. **First-person "In my client work" blocks appear in every cluster.** Where the specific client story is thin (T49 audit, T129 GBP posting), the first-person block references Vraj's own site as the working example instead. Both are legitimate EEAT signals; flagging so no one questions "why doesn't every article have a case study?"
11. **Downloadable artifacts (PDF checklists, Google Sheet templates, JSON-LD copy-blocks)** are referenced in 6 cluster pieces (T3, T17, T22, T26, T34, T113). These are Phase 4 assets — they need to be produced during content writing (Phase 3) or as part of the launch build. Flagging so they don't slip through.
12. **Cluster pages that reference vrajvithalani.com as the working example** are the strongest EEAT play in the tranche — T38 (hub-and-spoke), T43 (location pages), T46 (short-answer block), T47/T48/T49 (GEO), T54/T117 (Next.js builds), T127 (AI Overviews local via 3 city GBPs), T128 (Bing setup), T129 (GBP posting). These pieces should be written AFTER the site is live enough to link to real live examples. Sequencing note for Phase 3.
13. **The "3+ years running client campaigns" phrasing** carried from Tranche 2 continues here. Confirm the year Vraj first ran a paid Google Ads campaign (best guess: 2024 based on Doc 01's AADME timeline) so byline copy is honest.
14. **Update cadence**: every GEO cluster (T45–T49, T127, T128, T129) is flagged for quarterly review. Author bio card includes a "last-updated" claim; if quarterly review isn't operationally sustainable, tighten to semi-annual and adjust the promise on the pages.
15. **AI Overviews are appearing on ~40%+ of queries per Phase 1b.** Every Tier 1 cluster in this tranche carries a short-answer block near the top. Verify visually on QA that each short-answer block is boxed, above the fold on mobile, and third-person voiced. This is a launch-QA checklist item.

---

*End of Tranche 3. This is the largest tranche of the project by a wide margin. Awaiting review and approval or corrections before starting Tranche 4 (12 location pages).*

