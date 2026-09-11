# Blueprint — Tranche 1: Site-Wide Standards + Fixed Pages

*Phase 2 blueprint · vrajvithalani.com · Tranche 1 of 7 · Covers 9 fixed pages plus site-wide standards, Person schema reference block, LocalBusiness schema reference block, and the service-area anchoring decision that governs Tranche 4 (location pages).*

*Format spec: every page carries all 18 fields from `05_example_blueprint_reference.md`. A short table opens each page for scan-value; the remaining fields are H3 subsections underneath.*

---

## Site-Wide Standards

### Domain and canonical

| Field | Value |
|---|---|
| Primary domain | `vrajvithalani.com` (repurchased, ready) |
| HTTPS | Required, always. HSTS to be enabled at Phase 4 launch |
| Canonical host | Non-`www` preferred (proposal) — `https://vrajvithalani.com/` [TO FINALIZE PHASE 4] |
| Trailing-slash policy | All URLs served with trailing slash. 301 redirect from non-trailing to trailing |
| International targeting | India (hreflang `en-IN` primary, `en` alternate). Australia is priority commercial market — targeted via content and location signals, not hreflang |

### Global head & meta

- `<html lang="en-IN">` on every page.
- `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1">` on every page.
- Every page carries: canonical URL, self-referential `<link rel="canonical">`, OpenGraph tags (og:title, og:description, og:image, og:url, og:type, og:locale=en_IN), Twitter card tags (`summary_large_image`).
- Favicon set: 16, 32, 48, 96, 192, 512, `apple-touch-icon.png` (180×180), `manifest.webmanifest`.
- OG image default: 1200×630 branded card with Vraj's headshot + primary keyword text. Per-page overrides where meaningful (case studies, cluster content).

### Global JSON-LD schema (present on every page)

- **Person** schema (Vraj as entity — see Person Schema Reference Block below). Rendered in a single site-wide `<script type="application/ld+json">` block, typically in the layout header.
- **Organization** schema (personal-brand solopreneur entity — legal name and `alternateName` capture consultancy identity). See Person block for values.
- **WebSite** schema with `potentialAction` (`SearchAction`) — enables a sitelinks search box.
- **BreadcrumbList** schema on every page except home.

Per-page schema layered on top of the global set is specified in each page's Schema Markup section.

### Global elements

- **Header**: minimal top nav — logo (wordmark "Vraj Vithalani" + soft-teal dot), primary nav (Services · Learn · Case Studies · About · Contact), mobile hamburger. Fixed on scroll with translucent white background (glassmorphism).
- **Footer**: three-column — (1) Vraj Vithalani NAP + WhatsApp + email, (2) primary nav mirror, (3) legal (Privacy, Terms) + last-updated of site + copyright.
- **WhatsApp floating CTA**: bottom-right on every page, `https://wa.me/918460474721?text=Hi%20Vraj%20—%20` (pre-filled greeting). Renders as circular button with WhatsApp glyph + subtle bounce on first visit, hidden on scroll-up on mobile to preserve reading space.
- **Cookie banner**: minimal, functional (GA4 opt-in), dismissible, link to `/privacy/`. Consent stored client-side.
- **Skip-to-content link**: visible on keyboard focus, accessibility default.

### Typography (proposed — [TO FINALIZE PHASE 4])

- **Body & UI**: Inter Variable (Google Fonts, self-hosted for speed). Weights loaded: 400, 500, 600, 700.
- **Display / H1s**: Inter Display (same family, tighter tracking) — or single-family Inter with letter-spacing tuning if the display variant is unavailable in the chosen stack.
- **Monospace (code blocks in Learn content)**: JetBrains Mono, weight 400.
- **Base font size**: 17px on desktop, 16px on mobile. Body line-height 1.6.
- **Heading scale**: H1 clamp(2.25rem, 4vw, 3.25rem); H2 clamp(1.75rem, 3vw, 2.25rem); H3 1.375rem; H4 1.125rem.
- Font loading: `font-display: swap`, preload the primary weight.

### Color palette (proposed — [TO FINALIZE PHASE 4])

Anchored to Doc 02: white base, black, soft-teal accent, glassmorphism-friendly. All values pass WCAG AA at intended usages.

| Token | Hex | Usage |
|---|---|---|
| `--ink` | `#0A0A0A` | Body text, primary headings |
| `--base` | `#FFFFFF` | Page background |
| `--teal-500` | `#14B8A6` | Primary accent — link text, primary buttons, focus rings |
| `--teal-300` | `#5EEAD4` | Highlight tint on glassmorphism surfaces |
| `--teal-700` | `#0F766E` | Interactive state (hover, active) |
| `--surface` | `#F8FAFC` | Off-white section backgrounds |
| `--muted` | `#6B7280` | Secondary text, captions |
| `--border` | `#E5E7EB` | Card borders, dividers |
| `--glass` | `rgba(255, 255, 255, 0.55)` + `backdrop-filter: blur(14px)` | Header, cards, testimonial surfaces |

### Accessibility

- WCAG 2.2 Level AA minimum on every page.
- Keyboard navigation complete: skip link, focus rings visible, no keyboard traps.
- Alt text on every non-decorative image (decorative images use `alt=""`).
- Form fields have visible labels, error messages announced via `aria-live`.
- Colour contrast checked at build time (Lighthouse + axe).
- Prefers-reduced-motion honoured (glassmorphism animations disable, transitions become instant).
- Semantic HTML5 landmarks (`header`, `nav`, `main`, `article`, `aside`, `footer`).

### Core Web Vitals targets

- **LCP** < 2.5s (75th percentile, mobile)
- **CLS** < 0.1
- **INP** < 200ms
- **FID** (legacy) — n/a in 2026, INP is the metric
- **Total page weight** target: < 1.5 MB on content pages, < 800 KB on fixed pages
- Images: WebP / AVIF preferred, `loading="lazy"` below-fold, explicit width/height to prevent CLS

### Tech stack

**[DEFERRED TO PHASE 4]** per Doc 02. What's locked in Doc 02 and safe to reference now:

- **Host**: Hostinger Managed WooCommerce Cloud Startup plan (10 Node.js app slots available).
- **Database**: MongoDB Atlas (external, connection string).
- **CDN**: included in Hostinger plan.
- **SSL**: included, auto-renewed.
- **Admin panel**: Vraj-only login, view contact form submissions, browser notifications only.

Frontend framework, backend framework, and rendering strategy (SSR / SSG / ISR) — all deferred to Phase 4 kickoff research per Doc 02.

### Content governance (locked, applies to every page in the blueprint)

- English only.
- No pricing shown publicly. "Contact for quote" pattern throughout.
- Single-actor framing: no named individuals other than Vraj. Companies as clients, collaborators, or context.
- Silent Indian SMB lens: never labeled as a series, framework, or brand.
- No AI-generated content on the final site.
- Every content page carries EEAT scaffolding (author byline, dates, first-person block, real data).
- Placeholders during build for photos; real Vraj photos integrated later.
- Physiotherapy is a vertical Vraj has worked in — not his identity. It appears only in the drvishva case study and as passing context in other pieces. Zero standalone physiotherapy Learn content.
- Contact page is intentionally underlinked. Only home footer, service pages, location pages, About bottom, and services hub bottom point to `/contact/`.

---

## Person Schema Reference Block

Single source of truth for the Person entity, referenced by every page's schema section. Rendered site-wide in the layout head.

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://vrajvithalani.com/#vraj",
  "name": "Vraj Vithalani",
  "url": "https://vrajvithalani.com/",
  "image": "https://vrajvithalani.com/img/vraj-vithalani-headshot.jpg",
  "jobTitle": "Google Ads, SEO, Web Development & CRO Specialist",
  "description": "Independent digital marketing and web development specialist based in Surat, India. Ships Google Ads, SEO, Next.js and WordPress builds, and CRO work for service businesses, D2C brands, industrial exporters, and NGOs.",
  "gender": "Male",
  "nationality": {"@type": "Country", "name": "India"},
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Surat",
    "addressRegion": "Gujarat",
    "addressCountry": "IN"
  },
  "email": "mailto:contact@vrajvithalani.com",
  "telephone": "+91-84604-74721",
  "alumniOf": {
    "@type": "EducationalOrganization",
    "name": "AADME — Academy of Advanced Digital Marketing Education"
  },
  "hasCredential": [
    {"@type": "EducationalOccupationalCredential", "name": "Diploma in Computer Engineering", "credentialCategory": "diploma"},
    {"@type": "EducationalOccupationalCredential", "name": "Google Digital Marketing Certificate (Coursera)", "credentialCategory": "certification"},
    {"@type": "EducationalOccupationalCredential", "name": "AADME Certified Digital Marketer", "credentialCategory": "certification"},
    {"@type": "EducationalOccupationalCredential", "name": "NIT-EDU Certified Digital Marketer", "credentialCategory": "certification"}
  ],
  "knowsAbout": [
    "Google Ads", "Performance Max Campaigns", "Meta Ads",
    "Search Engine Optimization", "Technical SEO", "Local SEO",
    "Generative Engine Optimization", "AI Search Visibility",
    "WordPress Development", "Next.js Development", "Node.js", "NestJS",
    "MongoDB", "Razorpay Integration", "Shopify",
    "Conversion Rate Optimization", "Landing Page Design",
    "WhatsApp Business Automation", "Google Analytics 4", "Google Tag Manager",
    "Schema Markup", "Site Speed Optimization", "WordFence Security"
  ],
  "sameAs": [
    "https://in.linkedin.com/in/vrajvithalani",
    "https://www.instagram.com/vrajvithalani/",
    "https://www.facebook.com/vraj.vithalani00/",
    "https://x.com/vrajvithalani"
  ],
  "worksFor": {"@id": "https://vrajvithalani.com/#org"}
}
```

Companion Organization block (for personal-brand entity resolution):

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://vrajvithalani.com/#org",
  "name": "Vraj Vithalani",
  "alternateName": "Vraj Vithalani Consulting",
  "url": "https://vrajvithalani.com/",
  "logo": "https://vrajvithalani.com/img/vraj-vithalani-logo.png",
  "founder": {"@id": "https://vrajvithalani.com/#vraj"},
  "email": "mailto:contact@vrajvithalani.com",
  "telephone": "+91-84604-74721",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Surat",
    "addressRegion": "Gujarat",
    "addressCountry": "IN"
  },
  "sameAs": [
    "https://in.linkedin.com/in/vrajvithalani",
    "https://www.instagram.com/vrajvithalani/",
    "https://www.facebook.com/vraj.vithalani00/",
    "https://x.com/vrajvithalani"
  ]
}
```

**Values to confirm during Phase 4**: exact headshot filename, exact logo filename, whether to add a Coursera / LinkedIn Learning URL under `hasCredential` when certificate IDs are re-verified. `contact@vrajvithalani.com` is the public professional email; the personal Gmail is used only for account creation and maintenance and never appears on-site.

---

## LocalBusiness Schema Reference Block

Vraj operates from Surat with no fixed office. LocalBusiness schema uses the **service-area business (SAB)** pattern — a `ProfessionalService` variant with `areaServed` rather than a street-address storefront. City-specific location pages (Tranche 4) inherit this pattern with their `areaServed` scoped to Surat / Ahmedabad / Bangalore respectively.

Base LocalBusiness block:

```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "https://vrajvithalani.com/#business",
  "name": "Vraj Vithalani — Digital Marketing & Web Development",
  "url": "https://vrajvithalani.com/",
  "image": "https://vrajvithalani.com/img/vraj-vithalani-headshot.jpg",
  "priceRange": "Contact for quote",
  "telephone": "+91-84604-74721",
  "email": "mailto:contact@vrajvithalani.com",
  "founder": {"@id": "https://vrajvithalani.com/#vraj"},
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Surat",
    "addressRegion": "Gujarat",
    "postalCode": "395007",
    "addressCountry": "IN"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 21.1702,
    "longitude": 72.8311
  },
  "areaServed": [
    {"@type": "City", "name": "Surat"},
    {"@type": "City", "name": "Ahmedabad"},
    {"@type": "City", "name": "Bangalore"},
    {"@type": "Country", "name": "India"},
    {"@type": "Country", "name": "Australia"}
  ],
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
    "opens": "10:00",
    "closes": "19:00"
  },
  "sameAs": [
    "https://in.linkedin.com/in/vrajvithalani",
    "https://www.instagram.com/vrajvithalani/",
    "https://www.facebook.com/vraj.vithalani00/",
    "https://x.com/vrajvithalani"
  ]
}
```

**Postal code**: `395007` is a Surat central-area placeholder [TO CONFIRM — replace with the actual PIN of Vraj's operating locality]. Coordinates `21.1702, 72.8311` correspond to Surat city centre; refine to the actual operating neighbourhood before Phase 4 for accurate map pinning.

---

## Location-Page Anchoring Decision (governs Tranche 4)

Vraj has one operating base (Surat). Ahmedabad and Bangalore are served remotely with occasional in-person visits. The blueprint uses the following pattern for the 12 location pages:

- **Surat pages** — full LocalBusiness with the Surat address + geo coordinates. This is the primary local entity for Google Business Profile anchoring.
- **Ahmedabad pages** — LocalBusiness of subtype `ProfessionalService` with `address` still Surat, `areaServed` scoped to `{City: Ahmedabad}`, and explicit on-page copy stating "remote-first delivery with occasional in-person visits for local clients." This is the honest service-area framing that Google penalises spun/doorway pages for missing.
- **Bangalore pages** — same pattern as Ahmedabad, scoped to `{City: Bangalore}`.

This avoids fake-office LocalBusiness schema (which is a Google penalty vector), and matches the actual delivery model. Each of the 12 location pages will still carry genuinely local content per Doc 03 (real landmarks, real local FAQ, real client references where any exist in that city).

---

## Page 1 — Home

| Field | Value |
|---|---|
| **URL** | `/` |
| **Page type** | Home (entity establishment + service overview + credibility) |
| **Primary keyword** | `vraj vithalani` (branded — highest priority for entity re-anchoring against current LinkedIn/AI-Mode physio misclassification) |
| **Secondary keywords** | google ads specialist india · seo consultant india · web developer surat · cro consultant india · digital marketing consultant surat |
| **Search intent** | Navigational (branded) + Commercial (four service pillars, hire intent) |
| **H1** | Vraj Vithalani — Google Ads, SEO, Web Development & CRO Specialist |
| **Meta title** | Vraj Vithalani — Google Ads, SEO, Web Dev & CRO Specialist *(58 chars)* |
| **Meta description** | Google Ads, SEO, web development and CRO consulting for service businesses and D2C brands. Independent specialist based in Surat, India. Contact for quote. *(156 chars)* |
| **Content format** | Landing page — hero + short-answer block + four pillar tiles + featured case studies + credibility + FAQ + soft CTA |
| **Word count target** | 1,200–1,500 |

### Content structure (H2 / H3 outline)

- H1 — Vraj Vithalani — Google Ads, SEO, Web Development & CRO Specialist
- Hero paragraph — 50-word positioning statement. First sentence must contain full name + all four pillars + "specialist" + "Surat" / "India". Written third person for LLM-friendly entity extraction.
- **Short-answer block** — 60–80 words, boxed visually. Third person. Loaded with entity signals: full name, four services, base city, years operating, ideal client types. This is the block that gets pulled into AI Overviews / ChatGPT.
- H2 — Four things I help you do
  - H3 — Run Google Ads that pay back (2 sentences + tile CTA → `/services/google-ads/`)
  - H3 — Rank in Google and AI search (2 sentences + tile CTA → `/services/seo/`)
  - H3 — Build websites that convert (2 sentences + tile CTA → `/services/web-development/`)
  - H3 — Automate the lead funnel (2 sentences + tile CTA → `/services/cro-and-automation/`)
- H2 — About Vraj (200-word excerpt from `/about/`, ends with "Read the full story →" link)
- H2 — Recent work (3 large case-study cards)
  - Powercable card (industrial exporter, ~40-day cold-call-to-deployment build)
  - Drvishva card (physiotherapy website, Next.js, launching soon)
  - Vitthalshringar card (D2C e-commerce, in progress)
  - Plus "See all case studies →" link
- H2 — Working from Surat, serving India and international clients (short paragraph — 60 words — mentions Surat base + India-wide remote delivery + international including Australia)
- H2 — What clients say (2–3 testimonial cards — attributed to companies, not individuals per single-actor rule)
- H2 — Frequently asked questions (5 items — see below)
  - How do I work with clients?
  - Do you work with international clients?
  - Do you have pricing on the site?
  - Are you a solo consultant or an agency?
  - How do I get started?
- H2 — Let's talk about your project (soft CTA block — two buttons: "See what I do" → `/services/`, "WhatsApp me" → wa.me link)
- Footer (site-wide)

### Internal links OUT

- `/services/google-ads/` · `/services/seo/` · `/services/web-development/` · `/services/cro-and-automation/` (4 pillar tiles, primary conversion paths)
- `/services/` (from "See all services" and final CTA)
- `/about/` (from "Read the full story" and secondary hero CTA)
- `/case-studies/powercable/` · `/case-studies/drvishva/` · `/case-studies/vitthalshringar/` (3 featured cards)
- `/case-studies/` (from "See all case studies")
- `/locations/` (from "Working from Surat" section)
- `/learn/` (via header nav + optional "recent articles" strip once Learn content is live; placeholder pre-launch)
- `/contact/` (footer only — home hero does NOT primary-CTA to contact; sends to `/services/` per Doc 03)

### Internal links IN

- Every other page on the site (via header logo + footer nav — this is the universal inbound pattern).

### Schema markup required

- **Person** (from Person Schema Reference Block — site-wide)
- **Organization** (from Reference Block — site-wide)
- **WebSite** with `SearchAction` (home is the natural host for the site-search entity)
- **FAQPage** (5 FAQ items from the on-page FAQ section)
- No `BreadcrumbList` on home (home is the root — schema-guideline exception)

### EEAT elements required

- Author byline strip below hero: circular headshot + "Vraj Vithalani · Google Ads, SEO, Web Dev & CRO Specialist · Based in Surat, India" + published date + last-updated date.
- Credentials line visible in About section: "Diploma in Computer Engineering · Certified Digital Marketer (AADME, Coursera, NIT-EDU) · 3+ years shipping client campaigns."
- 4-logo "worked with" row (Powercable, Vitthalshringar, Drvishva parent brand, IOTA — real, not stock).
- 2–3 testimonial cards with client-company attribution (per single-actor rule, no named individuals other than Vraj — testimonial cards say e.g. "Powercable, Surat" not "[Person Name], CEO").
- Real WhatsApp number + real email visible in footer.
- Last-updated date visible on page (footer or below hero byline).
- Real headshot (placeholder pre-launch — final headshot integrated per Doc 02 plan).

### CTA specification

- **Primary CTA** (hero right side): "See what I do" → `/services/` — soft, non-transactional, per critical rule 9 (home CTA goes to services, not contact).
- **Secondary CTA** (hero left, less prominent): "Talk on WhatsApp" → `wa.me/918460474721?text=Hi%20Vraj%20—%20`.
- **Floating CTA** (bottom-right, site-wide): WhatsApp glyph button.
- **Final block CTA** (bottom of page): two buttons — "See services" and "WhatsApp me". No contact-form CTA on home.

### Media requirements

- **Hero image**: professional Vraj headshot, medium-wide framing, white or subtle glassmorphism background, soft-teal accent lighting. 1920×1080, WebP + AVIF. Placeholder pre-launch.
- **4 pillar tile icons**: custom SVG, monochrome soft-teal, consistent line-weight. Reused on Services hub and About page for visual continuity.
- **3 case study card images**: real project screenshots or hero images from Powercable / Drvishva / Vitthalshringar sites. Not stock photography.
- **4 client logos or wordmarks**: monochrome grey to keep the visual quiet, teal on hover.
- **2–3 testimonial card avatars**: company logos, not individual photos (single-actor rule).
- **OG image**: dedicated 1200×630 branded card — headshot + name + role + soft-teal background.
- **Favicon set**: as specified in Site-Wide Standards.

### Notes

- **Home's primary job is entity re-establishment.** The current AI-Mode/ChatGPT skew describing Vraj as a "physiotherapy marketing specialist" is caused by LinkedIn's recent post frequency. The first 100 words of the page must contain, in one clean sequence: full name, all four service pillars, the word "specialist", and "Surat" / "India". This is what LLMs extract when re-indexing the entity.
- **Short-answer block placement** is above-the-fold on mobile (immediately after hero paragraph). Third-person voice for LLM extraction; first-person voice reserved for About and Learn content.
- Do NOT primary-CTA to `/contact/` per Doc 03 internal linking strategy. Home CTAs route to `/services/` to keep link equity on the money pages.
- FAQ answers should include the phrase "Contact for quote" at least once — this is a locked content-governance rule, and the FAQ is the natural place to bake it in.
- Testimonial attribution: single-actor rule extends to testimonial cards. Attribute to the company ("Powercable, Surat") not to a named individual within the company. If a testimonial reads well only with an individual's name, either request the client's approval to attribute to the company or omit the name.
- Physiotherapy: on the home page, physio appears at most as a listed vertical among others in the "who I work with" copy on the Services hub — not on home. Zero physio-forward language on home.

---

## Page 2 — About

| Field | Value |
|---|---|
| **URL** | `/about/` |
| **Page type** | About (personal biography + EEAT authority hub) |
| **Primary keyword** | `vraj vithalani about` (branded) |
| **Secondary keywords** | vraj vithalani founder · vraj vithalani surat · full stack developer digital marketer · independent digital marketing consultant india · ex vgs it solution |
| **Search intent** | Navigational (branded) + Evaluation (trust-building for prospects and LLMs) |
| **H1** | About Vraj Vithalani |
| **Meta title** | About Vraj Vithalani — Story, Stack & How I Actually Work *(57 chars)* |
| **Meta description** | Full-stack developer, digital marketer, founder based in Surat. My work across Google Ads, SEO, Next.js and Razorpay for Indian and international clients. *(155 chars)* |
| **Content format** | Long-form biographical page — first-person narrative with timeline anchors, tech stack disclosure, verticals worked in, and how-I-work section |
| **Word count target** | 1,800–2,400 |

### Content structure

- H1 — About Vraj Vithalani
- Hero paragraph (first-person, 60–80 words). First sentence: "I'm Vraj Vithalani. I run Google Ads, build websites, and ship SEO and CRO work for service businesses, D2C brands, industrial exporters, and NGOs."
- **Short-answer block** (60 words, third person for LLM extraction — this is the entity summary that gets pulled into AI Overviews)
- H2 — The short version (4-sentence positioning summary)
- H2 — How I got here (narrative)
  - H3 — Starting out: a computer engineering diploma and a WordPress obsession
  - H3 — Founding VGS IT Solution (14 December 2023 — 18 months running end-to-end)
  - H3 — Learning digital marketing from the ground up (AADME + client fieldwork)
  - H3 — Teaching digital marketing at Soni Computer Institute
  - H3 — Transitioning to independent consulting (mid-2025)
- H2 — The four things I do
  - H3 — Google Ads (2 sentences + link to `/services/google-ads/`)
  - H3 — SEO, including GEO / AI search (2 sentences + link to `/services/seo/`)
  - H3 — Web development (2 sentences + link to `/services/web-development/`)
  - H3 — CRO and automation (2 sentences + link to `/services/cro-and-automation/`)
- H2 — The tech stack I actually ship on (WordPress, Next.js, Node/NestJS, MongoDB, Hostinger, Razorpay, WordFence, Shopify, Python — anchored to real project experience)
- H2 — The verticals I've worked deeply in
  - Industrial exporters and B2B manufacturing (VM Graphite, Powercable)
  - Education and coaching institutes (Synergy Tutorials, Soni Classes teaching engagement)
  - E-commerce and D2C brands (Vitthalshringar, VGS Store)
  - Physiotherapy clinics (drvishva — case study)
  - NGOs and non-profits (Trust project — pro bono)
  - Marginal verticals covered as case studies only: pre-schools, astrology, tours & travel
- H2 — A note on how I write
- H2 — Certifications and training (list — AADME, Coursera Google Digital Marketing, NIT-EDU Digital Marketing, plus diploma in Computer Engineering)
- H2 — Where I work from and who I work with (Surat home base, India + international, quiet nod to Australia priority)
- H2 — Talk soon (soft CTA to `/services/` + WhatsApp)

### Internal links OUT

- All 4 service pillars (from "The four things I do" section)
- 4–5 featured case studies (Powercable, Drvishva, Vitthalshringar, Trust NGO, IOTA ANPR)
- `/case-studies/` (from "verticals" section — "See all case studies")
- `/learn/` (from "how I write" note — link to content pillars)
- `/locations/` (from "Where I work from" section)
- `/contact/` (single link in the "Talk soon" CTA — one of the deliberately few contact-linking nodes site-wide)
- `/services/` (final CTA)

### Internal links IN

- Home ("About Vraj" section + author byline)
- Every service pillar (author bio block linking to About)
- Every case study (author byline)
- Every Learn cluster article (author byline)
- Header nav (every page)
- Footer nav (every page)

### Schema markup required

- **Person** (extended — this is the canonical Person entity page; add `birthDate` if provided, `hasOccupation` array, `subjectOf` links back to social profiles)
- **AboutPage** wrapping the Person entity
- **BreadcrumbList** (Home → About)

### EEAT elements required

- Author byline at top: headshot + name + role + published date + last-updated date.
- First-person narrative throughout — this page is the EEAT gold that every content page's author byline links back to.
- Real dates: VGS IT Solution founded 14 December 2023, transitioned mid-2025.
- Real client references: Powercable, VM Graphite, Vitthalshringar, drvishva, IOTA, Trust NGO, Dreams Astro Numero, Little Genius, Parv Travels, Synergy Tutorials, Soni Classes.
- Certifications block with issuing body + credential type.
- Location transparency: "based in Surat, Gujarat, India."
- Optional: workspace / at-work photo (placeholder pre-launch).
- Explicit AI-content statement: "No content on this site is AI-generated. Every guide comes from real client work."

### CTA specification

- Soft CTA to `/services/` at bottom (primary).
- Secondary link to WhatsApp in the "Talk soon" block.
- WhatsApp floating button (site-wide).
- One link to `/contact/` from the "Talk soon" block — this is the About page's one contact-outbound link (in Doc 03's "About links to featured case studies, service pillars" pattern the contact link is optional; adding it here because About visitors are high-intent).

### Media requirements

- **Hero image**: Vraj headshot, medium-wide, professional (placeholder pre-launch). 1600×900.
- **Optional timeline visual**: horizontal timeline SVG — Dec 2023 (VGS founded) → mid-2025 (transitioned) → present (independent consulting). Minimal, soft-teal accents.
- **4 pillar icons**: same set as Home for visual continuity.
- **Verticals visual (optional)**: 5-tile grid with vertical icons.
- **Workspace photo (optional)**: candid at-desk shot — placeholder pre-launch.
- **OG image**: About-page-specific 1200×630 with "About Vraj Vithalani" + headshot.

### Notes

- **Single-actor framing is critical on this page above all others.** Every action in the story is Vraj's own. No partnership language for VGS. ANPR/IOTA framed as "delivered in collaboration with IOTA, a Kerala-based industrial systems company" (company-to-company, no individuals).
- **Silent Indian SMB angle** appears in specific mentions (INR budgets in client stories, WhatsApp as lead channel, Razorpay for payments) — never labeled as a framework or series.
- **VGS IT Solution dates** are load-bearing for entity credibility. Founded 14 December 2023, transitioned mid-2025 — state both dates explicitly.
- **Physiotherapy** appears once, listed among five verticals — never as identity. Drvishva is referenced as one case study among many.
- **Certifications list** should use full names of issuing bodies as they appear on the certificates. Coursera → "Google Digital Marketing Certificate (Coursera)". NIT-EDU → confirm the exact issuing entity name at Phase 4.
- The "A note on how I write" section is a deliberate GEO play — LLMs can extract editorial standards, and this differentiates the site from AI-content farms.
- The tech stack disclosure section pulls double duty: entity credibility for LLMs (Vraj *does* the tech) and self-qualification for prospects.

---

## Page 3 — Contact

| Field | Value |
|---|---|
| **URL** | `/contact/` |
| **Page type** | Contact / functional (form-first) |
| **Primary keyword** | `contact vraj vithalani` (branded) |
| **Secondary keywords** | hire vraj vithalani · vraj vithalani whatsapp · vraj vithalani email · google ads consultant contact surat |
| **Search intent** | Transactional (submit an inquiry) |
| **H1** | Contact Vraj Vithalani |
| **Meta title** | Contact Vraj Vithalani — Get a Quote for Your Project *(53 chars)* |
| **Meta description** | Get in touch with Vraj Vithalani for Google Ads, SEO, web development or CRO consulting. Response within 24 business hours via WhatsApp, email, or form. *(152 chars)* |
| **Content format** | Short, functional form-first page with WhatsApp + email alternates |
| **Word count target** | 400–600 (intentionally short — the page is the CTA, not a reading experience) |

### Content structure

- H1 — Contact Vraj Vithalani
- Sub-heading (one sentence) — "Tell me about your project. I'll reply within 24 business hours (IST)."
- H2 — Send a project inquiry
  - The form. Fields: Name (required), Email (required), WhatsApp number (optional), Company or website (optional), What are you looking for (multi-select: Google Ads / SEO / Web Development / CRO / Not sure yet), Project stage (dropdown: Exploring options / Ready to hire / Already running something), Message (textarea, required), honeypot (hidden). Submit button: "Send inquiry".
- H2 — Prefer WhatsApp? (button — `https://wa.me/918460474721?text=Hi%20Vraj%20—%20I'm%20looking%20for%20help%20with%20`)
- H2 — Prefer email? (mailto link — `contact@vrajvithalani.com`)
- H2 — What to include in your first message (3-sentence paragraph — current situation, what you've tried, budget range if known, deadline if any)
- H2 — Response times and what to expect (2 sentences — response window, next steps after reply)
- H2 — Not sure what you need yet? (soft link back to `/services/` and `/learn/`)

### Internal links OUT

- `/services/` (for visitors not ready to submit)
- `/learn/` (for research-mode visitors)
- `/privacy/` (linked near submit button)
- `/terms/` (linked near submit button)

Deliberately minimal — Contact does not push visitors elsewhere once they've landed.

### Internal links IN

- Header nav (every page)
- Footer nav (every page)
- Home footer CTA
- About page "Talk soon" block
- Every service pillar (embedded form on pillar + explicit contact link)
- Every location page (embedded form + WhatsApp CTA)
- Services hub bottom CTA

NOT linked from: case studies (soft-CTA to service pillar per Doc 03), cluster content (soft-CTA to service pillar per Doc 03), Learn hub (soft-CTA to service pillar).

### Schema markup required

- **ContactPage**
- **LocalBusiness** (Surat address + geo, from LocalBusiness Reference Block)
- **BreadcrumbList** (Home → Contact)

### EEAT elements required

- Explicit response window ("within 24 business hours, IST") — sets a trust anchor.
- Real WhatsApp number visible + clickable.
- Real email visible + clickable.
- Business hours stated (Mon–Sat 10:00–19:00 IST) — matches openingHoursSpecification in LocalBusiness schema.
- No CAPTCHA friction — honeypot only. This is a UX/CRO decision (friction cost > spam cost at SMB volume).
- Form submits to `/api/contact/`, stored in MongoDB Atlas, viewable in `/admin/` per Doc 02.

### CTA specification

- The page IS the CTA target. No secondary exit CTAs beyond the "Not sure what you need yet?" fallback.
- Primary action: form submission.
- Equal-weight alternates: WhatsApp button (green, brand-colour) and email link.
- WhatsApp floating button (site-wide) still present.

### Media requirements

- Minimal — no hero image beyond a light background.
- WhatsApp glyph (SVG, brand green).
- Email glyph (SVG, monochrome ink).
- Optional: small Surat map with pin (Google Maps embed) — decision [TO CONFIRM]. Embedding adds 200 KB+ of third-party JS; consider linking to Google Maps instead of embedding.

### Notes

- **Underlinked by design.** Per Doc 03 internal linking strategy, `/contact/` is deliberately underlinked to prevent it absorbing link equity that should concentrate on service pillars. This page ranks for its own branded terms only.
- **Form endpoint**: `POST /api/contact/` → MongoDB Atlas → visible only at `/admin/` (Vraj-only login, browser notifications). No email/WhatsApp forwarding, no CRM integration in Phase 4 launch per Doc 02.
- **WhatsApp pre-fill**: use `?text=` query parameter to seed conversation with "Hi Vraj — I'm looking for help with " so the visitor lands mid-sentence and the ice is broken.
- **Response window**: 24 business hours = the promise. If Vraj can consistently do 12, tighten later. Under-promise, over-deliver.
- **Privacy link near submit button**: legally required and improves conversion by pre-empting the "what happens to my data" question.
- **Currency of any pricing question in the form**: none. The form never asks budget in INR/USD explicitly (that's for the first reply conversation). Optional "budget range if known" hint appears only in the "What to include in your first message" paragraph.
- **Language**: English only. Time zone: IST (India Standard Time) — stated explicitly for international (esp. Australian) prospects.
- **Google Maps embed decision**: default to a static Google Maps *link* (not embed) to avoid the third-party JS payload. Revisit in Phase 4 if a visual map materially improves trust.

---

## Page 4 — Services hub

| Field | Value |
|---|---|
| **URL** | `/services/` |
| **Page type** | Services hub (index of 4 service pillars) |
| **Primary keyword** | `digital marketing services surat` (secondary commercial) + branded `vraj vithalani services` |
| **Secondary keywords** | google ads seo web development cro services india · independent digital marketing consultant · digital marketing consultant surat · hire digital marketing specialist india |
| **Search intent** | Commercial + Navigational (users comparing service pillars) |
| **H1** | Services — Google Ads, SEO, Web Development & CRO |
| **Meta title** | Services — Google Ads, SEO, Web Dev & CRO by Vraj Vithalani *(60 chars)* |
| **Meta description** | Four service pillars for service businesses and D2C brands: Google Ads, SEO, web development, and CRO & automation from an independent Surat-based specialist. *(159 chars)* |
| **Content format** | Hub page — intro + short-answer block + 4 pillar tiles with 150-word summaries + how-I-work + who-I-work-with + hiring FAQ + soft CTA |
| **Word count target** | 1,200–1,800 |

### Content structure

- H1 — Services — Google Ads, SEO, Web Development & CRO
- Intro paragraph (60–80 words) explaining how the four pillars compound (landing page × Ads × SEO × tracking = one system, not four vendors).
- **Short-answer block** (60 words listing all four services with a one-line descriptor each — this is what LLMs pull when asked "what does Vraj Vithalani do?")
- H2 — The four pillars
  - H3 — Google Ads (150-word summary + tile CTA "See Google Ads services →" linking to `/services/google-ads/`)
  - H3 — SEO (150-word summary + tile CTA linking to `/services/seo/`)
  - H3 — Web Development (150-word summary + tile CTA linking to `/services/web-development/`)
  - H3 — CRO & Automation (150-word summary + tile CTA linking to `/services/cro-and-automation/`)
- H2 — How I work (5-step process)
  - H3 — 1. Discovery call
  - H3 — 2. Scope and proposal
  - H3 — 3. Sprint plan
  - H3 — 4. Build and ship
  - H3 — 5. Handover and follow-up
- H2 — Who I work with (types of clients — service businesses, D2C brands, industrial exporters, NGOs, coaching institutes, physiotherapy clinics as one of many verticals)
- H2 — Where I work from and who I serve geographically (Surat base, India + international, Australia priority quietly noted)
- H2 — Frequently asked questions about hiring me (7 items)
  - Do you have fixed pricing or is every project custom?
  - Do you work retainer or project-based?
  - Do you work with international clients?
  - Do you subcontract work to others?
  - How long does a typical engagement take?
  - Do you work with pre-revenue businesses?
  - Do you offer training or workshops?
- H2 — Ready to talk? (final CTA — two buttons: WhatsApp + Contact form)

### Internal links OUT

- `/services/google-ads/`, `/services/seo/`, `/services/web-development/`, `/services/cro-and-automation/` (4 pillar tiles — primary conversion paths)
- `/locations/` (from "Where I work from" section)
- `/case-studies/` ("worked with" section)
- `/about/` (author bio link)
- `/contact/` (final CTA — one of the deliberately-few contact-linking nodes)

### Internal links IN

- Home (nav + services section)
- Header nav (every page)
- Footer nav (every page)
- About page (from "The four things I do" section)
- Every service pillar page (breadcrumb parent + "back to services" link)
- Every location page (breadcrumb via `/services/` if location page mentions the service hub — actually location pages sit at root, so their breadcrumb goes Home → Locations → City-Service, and Services hub is not a breadcrumb ancestor; it is however linked contextually where relevant)

### Schema markup required

- **CollectionPage**
- **ItemList** (4 Service entities, ordered)
- **BreadcrumbList** (Home → Services)
- **FAQPage** (7 hiring FAQs)
- Each service tile also carries a `Service` reference schema linking to the pillar page

### EEAT elements required

- Author byline at top and bottom.
- Explicit statement that Vraj personally delivers all work — no subcontracting (this is a real differentiator against agencies and worth stating clearly).
- Real client mentions (Powercable, Drvishva, Vitthalshringar, VM Graphite) in the "how I work" or "who I work with" sections.
- Certifications badge strip (optional visual — Google, AADME, NIT-EDU).

### CTA specification

- Per-tile CTA buttons on each of the 4 pillar summaries (primary in-page conversion driver).
- Embedded WhatsApp CTA in each pillar tile.
- Final block CTA linking to `/contact/` (one of the few contact-outbound links) plus WhatsApp button.
- Floating WhatsApp button (site-wide).

### Media requirements

- 4 pillar tile illustrations (same set as Home — visual continuity).
- Optional process diagram (5 steps of "how I work") — horizontal SVG, soft-teal accents.
- Author bio card at bottom (headshot + credentials).
- Client-logo strip (Powercable, Drvishva, Vitthalshringar, VM Graphite parent brand, Trust NGO).
- OG image: Services-hub-specific 1200×630.

### Notes

- **This is a hub, not a pillar.** Real conversion depth happens on the 4 individual pillar pages (Tranche 2). Keep this hub crisp — a routing page with enough substance to rank for the secondary commercial keyword.
- **Ranks for** the branded `vraj vithalani services` query plus the softer `digital marketing services surat` — the individual pillar pages carry the harder commercial keywords.
- **FAQ answers** must include the "Contact for quote" phrasing at least once (locked content-governance rule).
- **"Do you subcontract?"** answer: "No — I personally deliver every engagement. This is a solo consultancy by design, not an agency-in-training." This is the single biggest differentiator against agency competitors.
- **Australia priority** stays quiet — one sentence in the geographic section. Doc 02 rule: "Australia is the priority market but never over-emphasized."
- **Physiotherapy** in the "who I work with" list appears among others; not surfaced as a headline vertical.

---

## Page 5 — Locations hub

| Field | Value |
|---|---|
| **URL** | `/locations/` |
| **Page type** | Locations hub (index of 12 location pages) |
| **Primary keyword** | `digital marketing consultant surat ahmedabad bangalore` (soft — the real value is in the 12 individual pages) |
| **Secondary keywords** | google ads consultant surat ahmedabad bangalore · seo consultant across india · web developer india cities · remote digital marketing india |
| **Search intent** | Navigational + Local commercial (users choosing their city) |
| **H1** | Where I Work — Surat, Ahmedabad, Bangalore & Remote |
| **Meta title** | Locations — Google Ads, SEO, Web Dev & CRO Across India *(56 chars)* |
| **Meta description** | Serving clients in Surat, Ahmedabad, Bangalore, and remotely across India and internationally. Local Google Ads, SEO, web development, and CRO consulting. *(155 chars)* |
| **Content format** | Hub — city intros + 3×4 city-service matrix + remote-service statement + FAQ |
| **Word count target** | 800–1,200 (compact — this is a routing page, not a ranking page) |

### Content structure

- H1 — Where I Work — Surat, Ahmedabad, Bangalore & Remote
- Intro paragraph (60 words) — Surat home base, serving India, international including Australia, remote-first delivery.
- H2 — The three cities I focus on locally
  - H3 — Surat, Gujarat — my home base (short paragraph: local landmarks — Adajan, Vesu, Athwa, Ring Road; local client mentions — Powercable, Vitthalshringar)
  - H3 — Ahmedabad, Gujarat — the neighbour city (short paragraph: Satellite, SG Highway, Bodakdev context; remote-first framing)
  - H3 — Bangalore, Karnataka — India's tech corridor (short paragraph: Whitefield, Koramangala, Indiranagar context; remote-first framing)
- H2 — All 12 city-service pages (matrix — visual grid of 12 links)
  - Google Ads Expert in Surat / Ahmedabad / Bangalore
  - SEO Consultant in Surat / Ahmedabad / Bangalore
  - Web Developer in Surat / Ahmedabad / Bangalore
  - CRO Expert in Surat / Ahmedabad / Bangalore
- H2 — Remote work across India and internationally (paragraph — India-wide remote delivery + Australia + global; note that in-person meetings happen when logistics allow)
- H2 — Frequently asked questions (4 items)
  - Do you travel to client sites?
  - Do you work with clients outside these three cities?
  - What time zone do you work in?
  - Can we meet in person if I'm in Surat?
- H2 — Talk about your project (soft CTA — WhatsApp + link back to `/services/`)

### Internal links OUT

- All 12 location pages (via matrix + inline in city intro paragraphs)
- `/services/` (soft CTA at bottom)
- `/contact/` (final CTA — one of the deliberately-few contact links)

### Internal links IN

- Home (nav + "Working from Surat" section)
- Header nav (every page)
- Footer nav (every page)
- About page ("Where I work from" section)
- Every location page (breadcrumb via `/locations/`)

### Schema markup required

- **CollectionPage**
- **ItemList** (12 Place / LocalBusiness references — with each item pointing to its individual location page for full LocalBusiness detail)
- **BreadcrumbList** (Home → Locations)
- **FAQPage** (4 FAQs)

### EEAT elements required

- Honesty about Surat home base + remote delivery for Ahmedabad and Bangalore. No fake "office in Bangalore" claims.
- Real local landmarks in city intros (this signals genuine local knowledge to both readers and Google).
- Client mentions where applicable (Powercable + Vitthalshringar tie Vraj to Surat directly).
- Time-zone transparency (IST) in the FAQ.

### CTA specification

- Floating WhatsApp button (site-wide).
- Final soft CTA to `/services/` + WhatsApp button.
- Each city-service tile in the matrix acts as a routing CTA to the individual location page.

### Media requirements

- Optional: India map with 3 pins (Surat, Ahmedabad, Bangalore) + subtle global reach glow. SVG, monochrome + soft teal.
- 12 city-service tile chips (visual matrix — 4 columns × 3 rows). Minimal typography, teal accent on hover.
- OG image: Locations-hub 1200×630.

### Notes

- **This hub is a routing page.** Real ranking value sits in the 12 individual location pages (Tranche 4). Keep this hub short and clean; do not repeat 12 pages' worth of local content here.
- **Service-area business framing** (from LocalBusiness Reference Block above) is baked into the intro: "Surat home base + remote-first delivery to Ahmedabad, Bangalore, and beyond." This is the honest anchor that lets the 11 non-Surat pages carry SAB LocalBusiness schema without penalty.
- **Local landmarks** in city intros are important — they distinguish real local knowledge from doorway-page copy. Adajan / Vesu / Athwa for Surat; Satellite / SG Highway for Ahmedabad; Whitefield / Koramangala for Bangalore.
- **Australia** appears quietly in the "remote and internationally" paragraph — not headlined per Doc 02 rule.
- **Time-zone FAQ** answer: "I operate in IST. For Australian clients, that's a ~4.5-hour offset from AEST — mornings in India overlap with your working day well." Sets expectation without being intrusive.

---

## Page 6 — Case studies hub

| Field | Value |
|---|---|
| **URL** | `/case-studies/` |
| **Page type** | Case studies hub (index of 13 case study pages) |
| **Primary keyword** | `vraj vithalani case studies` (branded) + `digital marketing case studies india` (secondary) |
| **Secondary keywords** | google ads case study india · seo case study india · wordpress case study · d2c ecommerce case study india · industrial exporter website case study |
| **Search intent** | Trust-building / Evaluation (prospects vetting the consultant) |
| **H1** | Case Studies — Real Client Work |
| **Meta title** | Case Studies — Real Google Ads, SEO, Web Dev & CRO Work *(55 chars)* |
| **Meta description** | Real client work across Google Ads, SEO, web development, and CRO — from industrial exporters to physiotherapy clinics, D2C brands, coaching, and NGOs. *(152 chars)* |
| **Content format** | Hub — 4 featured cards + 9 earlier-work cards + service filter + vertical filter + how-to-read-a-case-study note + soft CTA |
| **Word count target** | 1,000–1,500 |

### Content structure

- H1 — Case Studies — Real Client Work
- Intro paragraph (60 words) — client range, honest depth statement, single-actor framing baked in ("Every project below is work I personally led — no subcontracting").
- **Short-answer block** (60 words listing verticals + result types)
- H2 — Featured work (live or launching soon — 4 large cards)
  - Card 1 — Powercable (industrial exporter, ~40-day cold-call-to-deployment, live at powercable.co.in)
  - Card 2 — Drvishva (physiotherapy website, Next.js, launching soon)
  - Card 3 — Vitthalshringar (D2C e-commerce, in progress, launching soon)
  - Card 4 — Trust NGO (custom donation & beneficiary CMS + fundraising + on-ground volunteering coordination, pro bono, launching soon)
- H2 — Earlier client work (9 smaller cards, from VGS era)
  - Dreams Astro Numero Foundation (WordPress + Razorpay + course platform)
  - VM Graphite Industries (exporter website + campaign work)
  - Little Genius Pre School (social media management — with the ~10x brand awareness lift: 500–600 → 5,500–6,000 monthly views)
  - Parv Travels (Meta Ads + Google Ads — 3-month engagement)
  - Synergy Tutorials (coaching-institute campaigns for admissions footfall)
  - Soni Classes (WordPress website + teaching engagement context)
  - VGS IT Solution (own company site — case study of building a service business)
  - VGS Store (Shopify dropshipping demo — capability showcase)
  - IOTA ANPR (production-grade Automatic Number Plate Recognition system — overview only, no implementation detail)
- H2 — Filter by service (Google Ads / SEO / Web Development / CRO) — visual filter chips
- H2 — Filter by vertical (Industrial exporters / D2C / Education / Physiotherapy / NGO / Astrology / Travel / Pre-school)
- H2 — How to read a case study on this site (short paragraph — every case study follows the same template: challenge → approach → what I did → results → tech/tools → lessons)
- H2 — Have a similar project? (soft CTA to `/services/` — NOT to `/contact/` per Doc 03 critical rule 9)

### Internal links OUT

- All 13 individual case study pages (from feature + earlier cards)
- `/services/` (soft CTA at bottom)
- 4 service pillars (via contextual links in "filter by service" chips)

### Internal links IN

- Home ("recent work" section — "See all case studies")
- Header nav (every page)
- Footer nav (every page)
- Every service pillar ("Case studies" section)
- Every individual case study page (sibling "See all case studies" link)
- About page ("verticals I've worked deeply in" section)

### Schema markup required

- **CollectionPage**
- **ItemList** (13 Article items, ordered — featured first)
- **BreadcrumbList** (Home → Case Studies)

### EEAT elements required

- Every card carries: client name, vertical tag, dominant service tag, one-line headline result.
- Featured cards have 4× visual weight vs earlier cards (visitors should feel the distinction).
- Single-actor framing throughout: "I built...", "I ran the campaigns...", "I designed and shipped..." — never "our team".
- IOTA ANPR card visually flagged "overview only" so visitors don't expect implementation detail.
- Little Genius card should surface the 10x brand awareness lift metric (500–600 → 5,500–6,000 monthly views).
- Powercable card should surface the ~40-day cold-call-to-deployment timeline.

### CTA specification

- Soft final CTA to `/services/` per critical rule 9 (cluster and case-study CTAs go to service pillars, NOT to contact).
- Each card acts as a routing CTA to its individual case study.
- Floating WhatsApp button (site-wide).

### Media requirements

- **4 featured card images**: real project hero shots or screenshots (Powercable, Drvishva, Vitthalshringar, Trust NGO). Not stock.
- **9 earlier-work thumbnails**: smaller cards, project thumbnails or wordmarks. Historic screenshots where available; wordmarks where sites are dead.
- **Filter chip UI**: minimal, teal accent on active state.
- **OG image**: case-studies-hub 1200×630.

### Notes

- **Featured vs earlier weighting** is the honest recency framing. Powercable is live now; older VGS-era work is legitimate but dated. Both matter; the visual weight communicates the difference.
- **IOTA ANPR** must be labeled overview-only. Per Doc 02, implementation details stay confidential. Card copy: "IOTA ANPR — overview-only case study of a production-grade Automatic Number Plate Recognition system built in collaboration with IOTA, a Kerala-based industrial systems company."
- **VGS IT Solution** as its own case study: single-actor framing. Card copy: "VGS IT Solution — founded and ran end-to-end for 18 months. A case study of building a service business from cold call to client delivery." No partnership language.
- **Little Genius** is the strongest older-work metric. Feature the 10x lift prominently on the card even though the engagement itself ended when the client moved to another agency (both parts of the story are told inside the case study; the metric alone on the card is fair).
- **Cluster and case-study CTA rule (critical rule 9)**: soft CTA to `/services/`, NOT `/contact/`. This preserves contact-link scarcity.
- **Filter functionality**: nice-to-have for launch. If dev time is tight in Phase 4, ship the hub without filters and add them post-launch.

---

## Page 7 — Learn hub

| Field | Value |
|---|---|
| **URL** | `/learn/` |
| **Page type** | Learn hub (index of 4 content pillars + recent articles) |
| **Primary keyword** | `vraj vithalani learn` / `vraj vithalani blog` (branded) |
| **Secondary keywords** | digital marketing blog india · google ads guides india · seo guides india · wordpress guides india · geo ai search guides india |
| **Search intent** | Informational + Navigational (users browsing the content library) |
| **H1** | Learn — Google Ads, SEO, Web Dev & CRO |
| **Meta title** | Learn — Google Ads, SEO, Web Dev & CRO Guides by Vraj *(53 chars)* |
| **Meta description** | In-depth guides on Google Ads, SEO, web development, and CRO for Indian service businesses, D2C brands, exporters, and NGOs. Written from real client work. *(156 chars)* |
| **Content format** | Content hub — intro + short-answer block + 4 pillar tiles + recent articles + all-topics filter + how-to-use + soft CTA |
| **Word count target** | 1,200–1,800 |

### Content structure

- H1 — Learn — Google Ads, SEO, Web Dev & CRO
- Intro paragraph (60 words) — what this hub is, sourced from real client work, no AI content, silent Indian SMB lens.
- **Short-answer block** (60 words summarising the four pillars for LLM extraction — "Vrajvithalani.com/learn hosts long-form guides on...")
- H2 — The four content pillars
  - H3 — Google Ads (2 sentences + tile link to `/learn/google-ads/`)
  - H3 — SEO, including GEO and AI search (2 sentences + tile link to `/learn/seo/`)
  - H3 — Web Development (2 sentences + tile link to `/learn/web-development/`)
  - H3 — CRO & Automation (2 sentences + tile link to `/learn/cro-and-automation/`)
- H2 — Recent articles (10 most recent — dynamically populated, article thumbnails + title + one-line excerpt + link)
- H2 — All topics by vertical (optional secondary index — Education / D2C / Industrial exporters / NGO / Physiotherapy [with note: "Physio content lives in the drvishva case study, not as standalone Learn articles"])
- H2 — Who these guides are for (short — Indian SMB owners, service-business operators, D2C founders, consultants)
- H2 — How I write these (short — no AI, real client work, first-person experience blocks, honest angles)
- H2 — Talk about your project (soft CTA to `/services/`)

### Internal links OUT

- 4 content pillar pages (`/learn/google-ads/`, `/learn/seo/`, `/learn/web-development/`, `/learn/cro-and-automation/`)
- 10 recent Learn articles (dynamic)
- `/services/` (soft CTA at bottom)
- `/case-studies/` (contextual — "see how this applied in real client work")

### Internal links IN

- Home (nav + "recent articles" section once populated)
- Header nav (every page)
- Footer nav (every page)
- Every content pillar (breadcrumb parent link)
- Every cluster article (breadcrumb via pillar → Learn hub → Home)
- Every service pillar ("Further reading" section)
- About page (from "How I write" reference)

### Schema markup required

- **CollectionPage**
- **ItemList** (4 content-pillar CreativeWork references)
- **BreadcrumbList** (Home → Learn)

### EEAT elements required

- Author byline at top (Vraj — headshot + credentials + link to `/about/`).
- Explicit "no AI-generated content" statement in the "How I write" section — this differentiates the site strongly in the 2026 content-farm landscape.
- Real client references in the how-I-write section (drvishva, Powercable, Vitthalshringar as examples of "the source material").

### CTA specification

- Soft final CTA to `/services/` per critical rule 9.
- Floating WhatsApp button (site-wide).
- No contact-form CTA on Learn hub or on cluster content — this is the intentional restraint.

### Media requirements

- 4 pillar tile illustrations (matching Home + About).
- Recent-article thumbnails (dynamic — 10 cards with hero images).
- Author bio card (headshot + credentials).
- OG image: Learn-hub 1200×630.

### Notes

- **Distinct from `/services/`.** Learn is informational; Services is commercial. Users may enter either funnel and cross via internal links, but the intent split must stay clean.
- **Naming**: "Learn" per Doc 02 (not Blog, not Insights, not Resources). Header nav shows "Learn".
- **"No AI-generated content" declaration** is a real GEO / trust play — LLMs can extract editorial policy, and this differentiates the site from AI-generated content farms that increasingly fill informational SERPs.
- **Physiotherapy note in "All topics by vertical"**: explicitly state that physio content is case-study-only, no standalone Learn articles. This handles the intent of a visitor arriving via LinkedIn who expects physio content, and reroutes them to the drvishva case study instead. It also documents the strategic decision on-page for LLM visibility.
- **Recent articles** section is dynamic — 10 most recent published cluster pieces. Populated as Tranches 3, 6, 7 pages go live.
- **Pillar-page word counts**: 5,000+ each (Tranche 3 spec). Long-form authoritative resources that host cluster content beneath them.

---

## Page 8 — Privacy

| Field | Value |
|---|---|
| **URL** | `/privacy/` |
| **Page type** | Static / legal |
| **Primary keyword** | N/A (not for ranking) |
| **Secondary keywords** | N/A |
| **Search intent** | Legal / trust / compliance |
| **H1** | Privacy Policy |
| **Meta title** | Privacy Policy — Vraj Vithalani (vrajvithalani.com) *(51 chars)* |
| **Meta description** | How Vraj Vithalani collects, uses, and protects your data when you contact via this website. GDPR-aware and India IT Act 2000 Section 43A compliant. *(149 chars)* |
| **Content format** | Static legal page — structured privacy policy |
| **Word count target** | 1,000–1,500 |

### Content structure

- H1 — Privacy Policy
- Effective date + last-updated date (both visible at top)
- Introductory paragraph (2 sentences — who this policy covers, scope of the site)
- H2 — What data I collect
  - H3 — Contact form submissions (name, email, WhatsApp number, company, message)
  - H3 — Analytics data (GA4 events, IP address anonymized)
  - H3 — Cookies (functional + analytics — opt-in)
- H2 — Why I collect it (respond to inquiries, understand site usage, improve content)
- H2 — Where I store it (MongoDB Atlas, encrypted at rest and in transit; GA4 in Google's systems)
- H2 — Who has access (only Vraj Vithalani — no team, no third-party processors beyond the storage providers named)
- H2 — How long I keep it (form submissions: 24 months from last contact; analytics data: 14 months per GA4 default; you may request deletion earlier)
- H2 — Third-party services used
  - Google Analytics 4 (analytics)
  - Google Search Console (SEO monitoring, no user data)
  - Hostinger (hosting)
  - MongoDB Atlas (form data storage)
  - WhatsApp Business (if you choose to contact via WhatsApp)
- H2 — Cookies and tracking (list of cookies, purpose, opt-out method)
- H2 — Your rights (access, deletion, portability, objection — GDPR-aligned; complaint-lodging procedure)
- H2 — Data transfers (if data leaves India — GA4 processes in Google's global infrastructure; disclose)
- H2 — Security measures (HTTPS, encryption at rest, 2FA on admin, WordFence on any WordPress infrastructure)
- H2 — How to reach me about your data (contact@vrajvithalani.com)
- H2 — Changes to this policy (versioning + notification method)

### Internal links OUT

- `/terms/`
- `/contact/` (for data-request submissions)

### Internal links IN

- Footer (every page)
- Cookie banner
- Contact form (link near submit button)

### Schema markup required

- **WebPage** (basic)
- **BreadcrumbList** (Home → Privacy)

### EEAT elements required

- Real contact email for data requests (contact@vrajvithalani.com)
- Effective date + last-updated date visible at top and footer of policy
- Specific data-handling commitments (retention periods, storage locations, security measures)
- Explicit named third-party processors

### CTA specification

- None (legal page — no promotional CTAs).

### Media requirements

- None.

### Notes

- **Legal review recommended before launch** [TO CONFIRM PHASE 4]. Draft this policy accurately, then have a lawyer familiar with Indian IT Act 2000 Section 43A and (if serving EU/UK/Australian clients) GDPR/UK-GDPR/Australian Privacy Act 1988 review it before publishing.
- **PCI-DSS not applicable in Phase 1** — the site does not accept payments. If payments are added later (Razorpay for consulting deposits, say), add a Payments section covering PCI-DSS scope.
- **India IT Act 2000 Section 43A** is the operative Indian data-protection reference in July 2026; the Digital Personal Data Protection Act 2023 (DPDP Act) is the newer framework and its rules should be checked at Phase 4 for what's actually enforceable at launch.
- **GDPR alignment** matters for European visitors and any Australian client whose contracts require GDPR-style handling.
- The policy is user-friendly by design — avoid the wall-of-text legalese pattern. Short H2s, plain-language explanations, real dates.

---

## Page 9 — Terms of Service

| Field | Value |
|---|---|
| **URL** | `/terms/` |
| **Page type** | Static / legal |
| **Primary keyword** | N/A |
| **Secondary keywords** | N/A |
| **Search intent** | Legal / trust / compliance |
| **H1** | Terms of Service |
| **Meta title** | Terms of Service — Vraj Vithalani (vrajvithalani.com) *(53 chars)* |
| **Meta description** | Terms governing use of vrajvithalani.com and inquiries submitted through the contact form. Governing law: India (Gujarat). Read before submitting an inquiry. *(158 chars)* |
| **Content format** | Static legal page — terms of service |
| **Word count target** | 1,000–1,500 |

### Content structure

- H1 — Terms of Service
- Effective date + last-updated date (both visible at top)
- Introductory paragraph (2 sentences — scope of these terms)
- H2 — Who I am and what this site is (independent consultancy operated by Vraj Vithalani, based in Surat, India)
- H2 — Use of this website
  - H3 — Acceptable use
  - H3 — Intellectual property (content on the site is Vraj's original work unless credited; no republication without written permission)
- H2 — The contact form and what happens after you submit
  - H3 — What submitting means (no obligation on either party until a written scope agreement is signed)
  - H3 — Response times (24 business hours IST, no legal commitment)
- H2 — No professional-services contract until scope is signed
- H2 — Content on this site (accuracy of guides, no warranty of results if you follow advice yourself, no substitute for tailored consulting)
- H2 — Third-party links (no responsibility for external content)
- H2 — Limitation of liability (standard clause — no consequential damages, cap at inquiry-response scope)
- H2 — Indemnification (limited)
- H2 — Governing law and jurisdiction (Indian law; Gujarat courts of exclusive jurisdiction)
- H2 — Changes to these terms (versioning + notification method)
- H2 — Contact for questions (contact@vrajvithalani.com)

### Internal links OUT

- `/privacy/`
- `/contact/`

### Internal links IN

- Footer (every page)
- Contact form (link near submit button)

### Schema markup required

- **WebPage** (basic)
- **BreadcrumbList** (Home → Terms)

### EEAT elements required

- Real contact email for terms questions
- Effective + last-updated dates visible
- Explicit governing law (India — Gujarat) — sets clear jurisdictional expectation for international clients
- Named entity (Vraj Vithalani, Surat, India)

### CTA specification

- None (legal page).

### Media requirements

- None.

### Notes

- **Legal review before launch** [TO CONFIRM PHASE 4]. Standard consulting-services terms with jurisdiction clause. Have a lawyer review before publishing.
- **Governing law clause** protects both parties and sets clear expectations for the ~10% of prospects who will read this before inquiring.
- **No sales/services contract in these terms** — this page covers site usage. Actual services engagements are covered by a separate scope-of-work document signed before each engagement.
- **International clients (Australia, EU, UK)** may want their own governing-law clauses in the eventual scope-of-work — that's out of scope for the terms page but worth noting for Phase 4 process.

---

## Tranche 1 — Summary at a Glance

| # | URL | Page type | Primary keyword | Word count | Ranking priority |
|---|---|---|---|---|---|
| 1 | `/` | Home | vraj vithalani (branded) | 1,200–1,500 | Entity re-establishment (top priority) |
| 2 | `/about/` | About | vraj vithalani about | 1,800–2,400 | EEAT authority hub |
| 3 | `/contact/` | Contact | contact vraj vithalani | 400–600 | Functional conversion page |
| 4 | `/services/` | Services hub | digital marketing services surat | 1,200–1,800 | Routing hub + soft commercial |
| 5 | `/locations/` | Locations hub | digital marketing consultant surat ahmedabad bangalore | 800–1,200 | Routing hub for 12 location pages |
| 6 | `/case-studies/` | Case studies hub | vraj vithalani case studies | 1,000–1,500 | Trust/evaluation index |
| 7 | `/learn/` | Learn hub | vraj vithalani learn | 1,200–1,800 | Content library index |
| 8 | `/privacy/` | Static legal | N/A | 1,000–1,500 | Compliance |
| 9 | `/terms/` | Static legal | N/A | 1,000–1,500 | Compliance |

**Total word count for Tranche 1 pages: ~10,000–13,000 words.**

---

## Tranche 1 — Internal Linking Map (ASCII tree)

```
/                                     (Home — root hub)
 │
 ├─→ /about/                          (from Home "About Vraj" section + secondary hero link)
 │    ├─→ /services/                  (from "The four things I do" recap)
 │    ├─→ /services/google-ads/       (from pillar tile — Tranche 2)
 │    ├─→ /services/seo/              (Tranche 2)
 │    ├─→ /services/web-development/  (Tranche 2)
 │    ├─→ /services/cro-and-automation/  (Tranche 2)
 │    ├─→ /case-studies/              (from "verticals" section)
 │    ├─→ /learn/                     (from "how I write" note)
 │    ├─→ /locations/                 (from "where I work from")
 │    └─→ /contact/                   (from "Talk soon" CTA — one of the few allowed contact links)
 │
 ├─→ /services/                       (from Home 4 pillar tiles + nav + "See all services")
 │    ├─→ /services/google-ads/       (pillar — Tranche 2)
 │    ├─→ /services/seo/              (Tranche 2)
 │    ├─→ /services/web-development/  (Tranche 2)
 │    ├─→ /services/cro-and-automation/  (Tranche 2)
 │    ├─→ /locations/                 (from "where I work from")
 │    ├─→ /case-studies/              (from "worked with")
 │    ├─→ /about/                     (author bio link)
 │    └─→ /contact/                   (final CTA — one of the few allowed contact links)
 │
 ├─→ /locations/                      (from Home "Working from Surat" + nav)
 │    ├─→ 12 city-service location pages  (Tranche 4)
 │    ├─→ /services/                   (soft CTA)
 │    └─→ /contact/                    (final CTA — one of the few allowed contact links)
 │
 ├─→ /case-studies/                   (from Home "recent work" section + nav)
 │    ├─→ 13 individual case study pages  (Tranche 5)
 │    ├─→ /services/                   (soft CTA — critical rule 9)
 │    └─→ 4 service pillars           (via filter chips — Tranche 2)
 │
 ├─→ /learn/                          (from Home nav + "recent articles" section)
 │    ├─→ 4 content pillar pages      (Tranche 3)
 │    ├─→ Recent Learn articles       (Tranches 3, 6, 7 populate)
 │    ├─→ /services/                   (soft CTA — critical rule 9)
 │    └─→ /case-studies/               (contextual link)
 │
 ├─→ /contact/                        (footer only from Home — deliberately underlinked)
 │    ├─→ /services/                   (fallback link)
 │    ├─→ /learn/                      (fallback link)
 │    ├─→ /privacy/                    (near submit button)
 │    └─→ /terms/                      (near submit button)
 │
 ├─→ /privacy/                        (footer only + cookie banner)
 │    ├─→ /terms/
 │    └─→ /contact/
 │
 └─→ /terms/                          (footer only + contact form)
      ├─→ /privacy/
      └─→ /contact/

Header nav (every page): Services · Learn · Case Studies · About · Contact
Footer nav (every page): Home · About · Services · Learn · Case Studies · Locations · Contact · Privacy · Terms
```

**Contact-page inbound scarcity summary** (this is the load-bearing detail of Doc 03):

| Page linking to `/contact/` | Link source |
|---|---|
| Home | Footer only |
| About | "Talk soon" bottom CTA |
| Services hub | Final CTA block |
| Locations hub | Final CTA block |
| 4 Service pillars | Embedded form + explicit contact link (Tranche 2) |
| 12 Location pages | Embedded form + WhatsApp (Tranche 4) |
| Header nav | Every page |
| Footer nav | Every page |
| Cookie banner + form legal links | Every page |

**Case studies and Learn cluster content do NOT contact-link in body copy** — they soft-CTA to service pillars only. This is what preserves the "money page" concentration.

---

## Gaps observed

1. **404 page** — Doc 03 mentions the 404 is "designed but not a URL-addressable page." Not included in this tranche per your 9-page list. Flagging for Phase 4 design: 404 should carry the site-wide header/footer, a short apology, a search box, and links to the 4 service pillars + case studies + learn hub. It carries no schema and no crawl-relevant content.
2. **robots.txt** — technical file, not a page. Flagging for Phase 4: default should Allow all, Sitemap directive pointing to `/sitemap.xml`, plus `Allow: /` for GPTBot / OAI-SearchBot / PerplexityBot / Google-Extended (relevant per Phase 1b GEO topics — these are the LLM crawlers we want indexing us).
3. **sitemap.xml** — flagging for Phase 4: auto-generated, updated on publish. Include priority weighting (Home 1.0, pillars 0.9, hubs 0.8, cluster content 0.7, static 0.5).
4. **RSS / Atom feed for Learn hub** — worth adding for Phase 4 GEO signal + traditional feed-reader visibility. Not in scope for Tranche 1 spec.
5. **HTML sitemap page** (`/sitemap/`) — not planned in Doc 03. Consider adding as a small usability aid + additional internal-linking surface for the crawler. Not adding without your approval.
6. **Cookie banner text** — mentioned in Site-Wide Standards; exact wording is a Phase 4 legal-review deliverable, not blueprint work.
7. **`/admin/` page** — Vraj-only login per Doc 02, not URL-addressable in the public site map. Not part of Tranche 1 blueprint; will be built in Phase 4.
8. **404 for `/case-studies/[old-domain-name]/` redirects** — some old VGS-era domains (`vgsitsolution.com`, `dreamsastronumero.com`, etc.) may still have inbound links. If any real inbound authority exists to those old URLs, consider 301 redirects to `/case-studies/[slug]/` on the new site. Requires an inbound-links audit at Phase 4.
9. **Traceability note for topics cut from Phase 1b**: T50 (Choosing a WordPress theme 2026) and T111 (Simple data pipelines for a solo marketer) — both existed in Phase 1a but were cut in Phase 1b. Neither will be blueprint entries in Tranches 3/6/7. Flagging here so no one asks later "where did T50 go?"
10. **Postal code `395007`** for Surat used in the LocalBusiness Reference Block is a central-area placeholder — please confirm the actual PIN of Vraj's operating locality before Phase 4. Same for the exact geo coordinates (currently Surat city centre).
11. **Font stack and colour palette** proposals are [TO FINALIZE PHASE 4] — every value carried here is grounded in Doc 02's brand statement (white/black/soft teal, minimal typography, glassmorphism) but the exact font family and hex codes may shift during Phase 4 design refinement.

---

*End of Tranche 1. Awaiting review and approval or corrections before starting Tranche 2 (service pillar pages).*
