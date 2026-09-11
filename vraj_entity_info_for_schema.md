# Vraj Vithalani — Entity Information for JSON-LD Schema

*Compiled from master narrative, substrate document, screenshots shared during planning, blueprint entries, and prior discussion. Everything below is either confirmed factual or marked with a source note.*

---

## Confirmed real values — safe to use in schema

### Identity

| Field | Value | Source |
|---|---|---|
| Full name | Vraj Vithalani | Master narrative, substrate, all screenshots |
| Primary location | Surat, Gujarat, India | Master narrative, screenshots (AI Mode result "Based in Surat, Gujarat, India") |
| Country | India | Confirmed |
| Job title / positioning | Google Ads, SEO, Web Development & CRO Specialist | Locked H1 decision |
| Alternate description | Digital marketing specialist and full-stack developer | Master narrative |
| Domain | vrajvithalani.com | Repurchased, confirmed |
| Nationality | Indian | Confirmed |
| Language | English (primary), Hindi and Gujarati (regional) | Substrate + locked English-only site rule |

### Contact channels

| Field | Value | Source |
|---|---|---|
| WhatsApp | +91 8460474721 | Tranche 1 blueprint global elements — floating CTA link |
| Instagram | https://www.instagram.com/vrajvithalani/ | Confirmed via AI Mode screenshot showing "@vrajvithalani" |
| LinkedIn | https://www.linkedin.com/in/vrajvithalani/ *(likely — verify with Vraj)* | AI Mode screenshots cite "LinkedIn India · Vraj Vithalani" but full URL not captured |
| GitHub | https://github.com/vrajvithalani *(inferred — verify with Vraj)* | Earlier screenshot showed browser tab `vrajvithalani/physiotherapist` which is a repo path |

### Professional background

| Field | Value | Source |
|---|---|---|
| Company (founded, past) | VGS IT Solution | Master narrative |
| VGS founded date | December 14, 2023 | Master narrative |
| VGS transition date | May 30, 2025 | Master narrative |
| VGS duration | 18 months | Master narrative |
| Current status | Independent consultant | Master narrative (transitioned mid-2025) |
| Educational background | Diploma in Computer Engineering | Master narrative |
| Founded VGS in | First semester of his diploma | Master narrative |
| Years of experience | Roughly 3+ years professional work (started with VGS Dec 2023, marketing work since) | Inferred from master narrative timeline |

### Skills and expertise (for `knowsAbout` schema property)

Confirmed from master narrative + Phase 1a + substrate:

- Google Ads (Performance Max, Search, remarketing)
- Meta Ads (via delivery partnership — NOT to be surfaced on site)
- SEO (technical, on-page, local, content strategy)
- Generative Engine Optimization (GEO / LLM search optimization)
- Web development — Next.js, WordPress, NestJS, Node.js, React
- CRO (Conversion Rate Optimization)
- Marketing automation
- WhatsApp automation for lead capture
- Analytics (GA4, Google Search Console, Google Tag Manager)
- Schema markup implementation
- Razorpay integration
- WordFence security
- Hostinger deployment
- MongoDB, Supabase, MySQL databases
- Computer vision (Raspberry Pi, ANPR — conceptual only, IOTA NDA)
- Python for marketing automation

### Verticals worked in (for `alumniOf` or context)

- Physiotherapy (Drvishva)
- Copper cables / industrial B2B (Powercable)
- Graphite exports (VM Graphite)
- E-commerce / D2C jewellery (Vitthalshringar — in progress)
- NGO / charitable trust (Devkunvarben Vithalani Charitable Trust — in progress)
- Astrology / spiritual services (Dreams Astro)
- Education / coaching (Synergy Tutorials, Soni Classes)
- Pre-schools (Little Genius)
- Tours & travel (Parv Travels)

### Family trust (special reference)

| Field | Value |
|---|---|
| Trust legal name | Devkunvarben Kevsavlal Bhanaji Vithalani Charitable Trust |
| Trust cause | Medical help, education, disaster relief (planned wheelchair rental program) |
| Vraj's role | Manages the trust pro bono |
| Certificates held | 80G, 12A |
| FCRA status | Pending |
| Amount raised so far | ₹25,000 |

---

## Values marked as `[TO CONFIRM AT PHASE 4 BUILD]` — Cowork should placeholder these

The following values were not surfaced during any of our conversations. Cowork should mark these as `[TO CONFIRM AT PHASE 4 BUILD]` in schema — user (Ansh) will collect from Vraj closer to launch:

- **Contact email address** — never disclosed to me
- **Date of birth / exact age** — for schema `birthDate` if desired (optional field, can be omitted safely)
- **Full postal address** — for LocalBusiness schema; substrate shows Surat-based but no street address. Recommended handling per Tranche 4 blueprint: for Surat pages use full address once collected; for Ahmedabad/Bangalore pages, use `areaServed` schema pattern instead of fake address (this was Cowork's own smart recommendation and it's correct)
- **X (Twitter) URL** — never mentioned
- **Facebook profile URL** — mentioned as "will be reframed post-launch" but URL not provided
- **YouTube channel URL** — not confirmed to exist
- **Personal Google Business Profile** — confirmed does NOT exist yet, planned as post-launch trust signal task
- **Professional photo URLs** — using placeholders; two headshots exist and will be provided during Phase 4 build
- **Any professional certifications** (Google Ads certification, GA4 certification, etc.) — if Vraj holds any, they'd strengthen `hasCredential` schema

---

## Schema.org type recommendation

For Vraj's Person schema, the recommended type stack:

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Vraj Vithalani",
  "givenName": "Vraj",
  "familyName": "Vithalani",
  "jobTitle": "Google Ads, SEO, Web Development & CRO Specialist",
  "description": "Google Ads, SEO, web development and CRO specialist based in Surat, India. Independent consultant serving businesses in India and internationally.",
  "url": "https://vrajvithalani.com/",
  "image": "[TO CONFIRM AT PHASE 4 BUILD — Vraj headshot URL]",
  "sameAs": [
    "https://www.instagram.com/vrajvithalani/",
    "https://www.linkedin.com/in/vrajvithalani/",
    "https://github.com/vrajvithalani"
  ],
  "worksFor": {
    "@type": "Organization",
    "name": "Vraj Vithalani (Independent Consultancy)",
    "url": "https://vrajvithalani.com/"
  },
  "knowsAbout": [
    "Google Ads",
    "Search Engine Optimization",
    "Generative Engine Optimization",
    "Web Development",
    "Next.js",
    "WordPress",
    "Conversion Rate Optimization",
    "Marketing Automation",
    "Local SEO",
    "Technical SEO"
  ],
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Surat",
    "addressRegion": "Gujarat",
    "addressCountry": "IN"
  },
  "nationality": {
    "@type": "Country",
    "name": "India"
  }
}
```

For the Organization / LocalBusiness schema on the site (since Vraj is a solopreneur, this represents the consultancy):

```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Vraj Vithalani",
  "alternateName": "Vraj Vithalani Digital Marketing Consultancy",
  "description": "Independent Google Ads, SEO, web development and CRO consultancy based in Surat, India.",
  "url": "https://vrajvithalani.com/",
  "founder": {
    "@type": "Person",
    "name": "Vraj Vithalani"
  },
  "foundingDate": "2025-05-30",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Surat",
    "addressRegion": "Gujarat",
    "addressCountry": "IN"
  },
  "areaServed": [
    { "@type": "City", "name": "Surat" },
    { "@type": "City", "name": "Ahmedabad" },
    { "@type": "City", "name": "Bangalore" },
    { "@type": "Country", "name": "India" },
    { "@type": "Country", "name": "Australia" }
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+91-8460474721",
    "contactType": "customer service",
    "availableLanguage": ["English", "Hindi", "Gujarati"]
  },
  "sameAs": [
    "https://www.instagram.com/vrajvithalani/",
    "https://www.linkedin.com/in/vrajvithalani/",
    "https://github.com/vrajvithalani"
  ]
}
```

---

## Instructions for Cowork on using this document

1. **Use everything in the "Confirmed" section as real values in schema markup.**
2. **For anything in the "TO CONFIRM AT PHASE 4 BUILD" section, use placeholder text with that exact label** so it's clearly visible during Phase 4 build review.
3. **The two schema blocks at the bottom are starting templates** — extend them per page-specific schema requirements (Article, Service, LocalBusiness variants, FAQPage, Review, VideoObject, BreadcrumbList, etc.) as each page's blueprint spec dictates.
4. **The Person schema goes site-wide** (header layout). The Organization / ProfessionalService schema goes on Home, About, Contact, and location pages (per Tranche 1 blueprint's global schema strategy).
5. **Update `foundingDate` on the ProfessionalService schema** if Vraj considers the consultancy to have started earlier than the VGS transition date. Current value (2025-05-30) uses the master narrative's VGS-transition date.
