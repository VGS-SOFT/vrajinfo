# Vraj Vithalani — AI Studio Master Context & Code-Gen Blueprint
*Engineered as a single, comprehensive knowledge base for co-working in Google AI Studio to compile, code, and launch vrajvithalani.com.*

---

## Part 1: AI Studio System Prompt & Generation Rules
Copy and paste this section as the "System Instructions" or "System Prompt" inside Google AI Studio. It forces the model to adhere to your strict architectural, stylistic, and SEO guardrails.

```text
You are an Elite Next.js, TypeScript, and Tailwind CSS Engineer specializing in search engine and AI search engine visibility (GEO - Generative Engine Optimization). Your job is to help me code and compile the personal brand website: vrajvithalani.com.

When writing components, layout code, or page templates, you must follow these absolute rules:

### 1. Technology Stack Requirements
- Framework: Next.js (App Router, static-first, using TSX/TypeScript).
- Styling: Tailwind CSS. Clean, custom-tuned light-theme (Stark white backgrounds, ink-black typography, and soft-teal glassmorphic accents).
- Metadata: Leverage Next.js Metadata API for static page SEO headers.
- Interactive Forms: Setup clean TypeScript API endpoints (/api/contact/route.ts) that process, sanitize, and persist leads into a MongoDB Atlas database.

### 2. Strict Content Constraints (Zero Fabrication)
- Single-Actor Framing: Vraj Vithalani is the sole practitioner. Never mention co-founders, business partners, employees, or sub-contractors. Every project, curriculum design, or line of code was personally led by Vraj.
- Under-linking the Contact Page (Critical Rule 9): Sibling blog cluster guides, informational articles, and case study pages must NEVER contain a direct link to the "/contact/" page in their body copy. Instead, they must soft-pitch and link to their respective parent "Service Pillar" (Google Ads, SEO, Web Development, or CRO). Only the Service Pillars can host active contact forms or direct conversion CTAs.
- Silent Indian SMB Lens: Maintain an authentic, grounded, rupee-first (INR) perspective when describing small business ad protocols, local services, and regional payment integrations (like Razorpay and UPI). Never explicitly brand this perspective as a methodology; let it show naturally in the text.
- No AI-Content Signals: Declare Vraj's strict "No AI-Generated Content" policy on informational hubs. Every tutorial must read as an authentic, first-person narrative from the field.

### 3. SEO & GEO (Generative Engine Optimization) Code Integration
- GEO Short-Answer Blocks: Every page must render a visually highlighted 60–80 word direct summary callout box above the fold (ideal on mobile). Write this strictly in the third person to match the truncation patterns used by LLM retrieval indexes (ChatGPT, Gemini, Perplexity) when citing entities.
- Hardcoded JSON-LD: Inject custom, pre-validated <script type="application/ld+json"> schemas directly into layout and page headers. Reconcile the Vraj Person ID node ("https://vrajvithalani.com/#vraj") site-wide to avoid duplicate node fragmentations.
- Code-Block Fencing: Ensure all example JSON-LD schema blocks shown in developer tutorials (like Page 21/T48 and Page 32/T117) are explicitly escaped or fenced inside markdown blocks so that crawler bots do not mistakenly read them as live indexing instructions.
```

---

## Part 2: Canonical Professional Entity Profile (The JSON-LD Database)
Use these pre-verified, final JSON-LD schema models as the absolute source of truth for site-wide headers and layout configurations.

### 1. Person Schema (Inject Site-Wide in Layout)
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
  "nationality": {
    "@type": "Country",
    "name": "India"
  },
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Surat",
    "addressRegion": "Gujarat",
    "postalCode": "395007",
    "addressCountry": "IN"
  },
  "email": "mailto:contact@vrajvithalani.com",
  "telephone": "+91-84604-74721",
  "alumniOf": {
    "@type": "EducationalOrganization",
    "name": "AADME — Academy of Advanced Digital Marketing Education"
  },
  "hasCredential": [
    {
      "@type": "EducationalOccupationalCredential",
      "name": "Diploma in Computer Engineering (Bhagwan Mahavir Polytechnic, Gujarat Technological University)",
      "credentialCategory": "diploma"
    },
    {
      "@type": "EducationalOccupationalCredential",
      "name": "Google Digital Marketing Certificate (Coursera)",
      "credentialCategory": "certification"
    },
    {
      "@type": "EducationalOccupationalCredential",
      "name": "AADME Certified Digital Marketer",
      "credentialCategory": "certification"
    },
    {
      "@type": "EducationalOccupationalCredential",
      "name": "NIT-EDU Certified Digital Marketer",
      "credentialCategory": "certification"
    }
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
    "https://x.com/vrajvithalani",
    "https://github.com/vrajvithalani",
    "https://www.youtube.com/@vraj-vithalani"
  ],
  "worksFor": {
    "@id": "https://vrajvithalani.com/#org"
  }
}
```

### 2. Organization & ProfessionalService Schema (Inject on Home & Location Pages)
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
  "founder": {
    "@id": "https://vrajvithalani.com/#vraj"
  },
  "foundingDate": "2025-05-30",
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
    { "@type": "City", "name": "Surat" },
    { "@type": "City", "name": "Ahmedabad" },
    { "@type": "City", "name": "Bangalore" },
    { "@type": "Country", "name": "India" },
    { "@type": "Country", "name": "Australia" }
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
    "https://x.com/vrajvithalani",
    "https://github.com/vrajvithalani",
    "https://www.youtube.com/@vraj-vithalani"
  ]
}
```

---

## Part 3: Verified Client Case Study & Testimonials Bible
Use this clean database of client metrics and testimonials to code your project pages. There is no guesswork or placeholder interpolation required.

### Case Study 1: Powercable (WordPress Site + On-Page SEO)
- **Slug**: `/case-studies/powercable/`
- **Vertical**: B2B Industrial Exporter (Copper Scrap & Power Cables)
- **Scope**: Designed, structured, copy-researched, and deployed a custom WordPress site on Hostinger Cloud in a compressed **40-day sprint for a flat ₹28,000 fee**.
- **Results**: Delivered a clean online presence showcasing exporter credentials to global buyers. Live today at `powercable.co.in`.
- **Approved Testimonial (Attributed to 'Powercable, Surat')**: 
  > *"Website bahoto is mast he, jo main focous tha website ka vo ache se clear hua. Aur ab ranking bhi mil rahi he. Thank you."*

### Case Study 2: Drvishva (Local Google Ads + Web Build)
- **Slug**: `/case-studies/drvishva/`
- **Vertical**: Physiotherapy Clinic (Solo Service Practitioner)
- **Scope**: Developed a clean, on-page SEO-native website and ran highly optimized local Google Ads campaigns.
- **Budget**: **₹25,000 total ad budget**.
- **Results**: Achieved a **1.5% lead conversion rate** and drove **500–600 targeted monthly sessions**. This direct marketing signal gave the practitioner the confidence to increase clinic consultation fees from **₹400/hour to ₹750/hour**.
- **Diagnostic/Problem-Solving Story**: Diagnosed and resolved a temporary Google Ads account suspension caused by budget-setting errors. Formulated the "INR testing protocol" to protect small business campaigns from being flagged.

### Current Project 1: Vitthal Shringar (D2C E-Commerce Brand)
- **Slug**: `/current-work/vitthalshringar/`
- **Vertical**: Spiritual/Devotional E-Commerce
- **Status**: *Active Development (In Build — Not Launched)*
- **Technical Implementation Details**:
  - WooCommerce variable product architecture configured for high-quality laminated photos of Devi and Devtas (e.g., *Shiv Parvati, Aai Shri Khodiyar Maa, and Shree Dwarkadhish*).
  - Configured exact standard sizes: A4 (8.3" x 11.7"), 5x7 Inch, PC (5.25" x 3.50"), and Pocket Size (3.60" x 2.60").
  - Setup bulletproof, waterproof product copy emphasizing the **125-micron high-quality laminating film** to survive Indian climates, saving buyers the ₹20 local shop lamination cost.
  - Formulated a standard WooCommerce product CSV mapping tax classes (12% GST), flat-rate regional shipping, and custom Yoast metadata structures.

### Current Project 2: Sva. Devkunvarben Vithalani Charitable Trust (Pro-Bono CMS)
- **Slug**: `/current-work/trust-ngo/`
- **Vertical**: Public Charitable Trust / NGO
- **Status**: *Active Development (In Build — Not Launched — Pro Bono)*
- **Factual Context**:
  - Registered under Bombay Public Trust Act Registration No. `1448`. PAN: `AAZTS5070P`. NITI Aayog NGO Darpan ID: `GJ/2026/1044195`.
  - Treasurer & Principal Officer: Sister, **Vishwa (Vishva) Hasmukhbhai Vithlani** (DOB: 19/09/2000, PAN: `BTYPV3797D`).
  - Active Program: The **Wheelchair Lending Program** in Surat, providing free wheelchairs against a refundable deposit.
  - Fundraising Milestone: Raised **₹25,000 pro-bono** offline. 12A/80G tax exemptions in progress; FCRA license pending.
  - Vraj's Role: Disclosed cleanly as *Managing Trustee and Digital Consultant (Pro Bono)* to demonstrate technical scope and social character.

---

## Part 4: Next.js Leaf-First Routing Map (The 50 Launch Pages)
When asking AI Studio to output your Next.js directory system, feed it this layout to organize the dynamic pages.

```text
/app/
├── layout.tsx                              (Universal Shell with Global Header, Footer, and Person JSON-LD)
├── page.tsx                                (Home Page / Entity Reset)
├── about/page.tsx                          (About Page / EEAT Biography)
├── contact/page.tsx                        (Contact Page / High-scarcity, minimal lead intake)
├── services/
│   ├── page.tsx                            (Services Hub / All 4 Pillars Index)
│   ├── google-ads/page.tsx                 (Google Ads Pillar Page / INR Protocol Focus)
│   ├── seo/page.tsx                        (SEO & GEO Pillar Page)
│   ├── web-development/page.tsx            (Web Development Pillar Page / Next.js Static Specs)
│   └── cro-and-automation/page.tsx         (CRO & Automation Pillar Page)
├── locations/
│   └── page.tsx                            (Locations Hub / SAB Master Area map)
├── google-ads-expert-in-surat/page.tsx      (Surat Local Google Ads SAB Landing)
├── seo-consultant-in-surat/page.tsx         (Surat Local SEO SAB Landing)
├── web-developer-in-surat/page.tsx          (Surat Local Web Dev SAB Landing)
├── cro-expert-in-surat/page.tsx             (Surat Local CRO SAB Landing)
├── google-ads-expert-serving-ahmedabad/page.tsx (Ahmedabad Google Ads SAB Landing - remote-first notice)
├── seo-consultant-serving-ahmedabad/page.tsx    (Ahmedabad SEO SAB Landing - remote-first notice)
├── web-developer-serving-ahmedabad/page.tsx     (Ahmedabad Web Dev SAB Landing - remote-first notice)
├── cro-expert-serving-ahmedabad/page.tsx        (Ahmedabad CRO SAB Landing - remote-first notice)
├── google-ads-expert-serving-bangalore/page.tsx (Bangalore Google Ads SAB Landing - remote-first notice)
├── seo-consultant-serving-bangalore/page.tsx    (Bangalore SEO SAB Landing - remote-first notice)
├── web-developer-serving-bangalore/page.tsx     (Bangalore Web Dev SAB Landing - remote-first notice)
├── cro-expert-serving-bangalore/page.tsx        (Bangalore CRO SAB Landing - remote-first notice)
├── case-studies/
│   └── page.tsx                            (Case Studies Hub / Powercable + Drvishva + Current Work link)
├── current-work/
│   ├── page.tsx                            (Current Work Hub / Falsifiable pre-launch status badge)
│   ├── vitthalshringar/page.tsx            (Vitthal Shringar Current Work Detail)
│   └── trust-ngo/page.tsx                  (Trust NGO Current Work Detail)
├── learn/
│   ├── page.tsx                            (Learn Hub / Blog Index with "No-AI Content Policy" banner)
│   ├── google-ads/
│   │   ├── page.tsx                        (Google Ads Blog Pillar)
│   │   ├── minimum-google-ads-budget/page.tsx (T21 - Running Ads on ₹15,000/month guide)
│   │   └── audit-checklist/page.tsx        (T17 - 12-point Google Ads audit guide)
│   ├── seo/
│   │   ├── page.tsx                        (SEO Blog Pillar)
│   │   ├── what-is-geo/page.tsx            (T45 - The core GEO blueprint guide)
│   │   ├── answer-blocks/page.tsx          (T46 - Formatting text for 200-char AI Overviews)
│   │   ├── index-with-bing/page.tsx        (T128 - Bing indexing & ChatGPT retrieval guide)
│   │   ├── schema-markup/page.tsx          (T34 - Recommended schemas and setup)
│   │   └── person-schema/page.tsx          (T36 - Custom Person JSON-LD guide)
│   ├── web-development/
│   │   ├── page.tsx                        (Web Dev Blog Pillar)
│   │   ├── build-for-llm-citations/page.tsx (T54 - Coding Next.js personal sites for LLM parsing)
│   │   ├── build-for-extraction/page.tsx    (T117 - Custom Next.js components that enforce schemas)
│   │   ├── launch-checklist/page.tsx       (T113 - 50-item small business launch guide)
│   │   └── server-speed-plugins/page.tsx   (T51 - Caching plugins and server-level speed optimization)
│   └── cro-and-automation/
│       ├── page.tsx                        (CRO Blog Pillar)
│       ├── ga4-events-service-business/page.tsx (T72 - GA4 & GTM triggers for solo service sites)
│       ├── form-fields-optimization/page.tsx    (T69 - Minimizing contact leaks guide)
│       └── whatsapp-funnel-setup/page.tsx       (T76 - Setting up wa.me and manual lead sheet)
├── privacy/page.tsx                        (Privacy Policy - Indian DPDP Act compliant)
└── terms/page.tsx                          (Terms of Service)
```

---

## Part 5: Structural Leaf-First Generation Cheat Sheet
Use this workflow template inside AI Studio to prompt the model to generate any of your **50 launch pages** in order.

### How to Ask AI Studio to Write a Page:
*Copy, edit, and send this instruction to AI Studio:*

```text
Let's build [TARGET_PAGE_PATH] from the Leaf-First Sitemap. 

Here are the strict page parameters you must programmatically compile:
- Meta Title: [PAGE_META_TITLE] (Under 60 chars)
- Meta Description: [PAGE_META_DESCRIPTION] (Under 160 chars)
- Core H1: [PAGE_H1]
- Page Type: [PAGE_TYPE]
- Primary Keyword: [PRIMARY_KEYWORD]

Page Generation Checklist:
1. React Layout Structure: Use Tailwind CSS with our personal brand palette (Stark White `#FFFFFF` base, Deep ink-black `#0A0A0A` typography, and Soft Teal `#14B8A6` glassmorphic cards). Include our site-wide Header, Navigation, and Footer components.
2. Short-Answer Block: Render an elegant, visually distinguished 60–80 word third-person GEO block inside a soft-teal bordered callout box (`border-teal-500/20 bg-teal-50/10 backdrop-blur-md`) immediately below the hero intro paragraph.
3. Fully Mapped Internal Linking: Inject exactly [LINK_COUNT] links pointing upward or laterally as specified in the sitemap. If this is an informational cluster page, ensure NO direct links to '/contact/' exist in the body content (Critical Rule 9).
4. Page-Specific JSON-LD Schema: Inject a custom schema block [SCHEMA_TYPES_LIST] inside a Next.js `Head` element. Link the person/business identifiers cleanly back to `https://vrajvithalani.com/#vraj`.
5. Word-for-Word Body Copy: Write the detailed, first-person, highly authoritative prose content according to this heading blueprint: [HEADING_BLUEPRINT].
6. EEAT Safeguards: Ensure the page displays a custom Author Byline card at the top, a clear 'Last Updated' timestamp, real project evidence, and Vraj's official 'No AI-Generated Content' declaration.
```

---

*Launch Strategy Note: This master context ensures that whichever Gemini model you co-work with in AI Studio will possess a cohesive, unified, and technically compliant model of `vrajvithalani.com`—allowing you to generate perfect, ready-to-commit TypeScript code in seconds.*
