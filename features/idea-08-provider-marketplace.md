# Provider Marketplace Finder

## Quick Stats

| Metric | Value |
|---|---|
| Difficulty | Intermediate-Advanced |
| Estimated Build Time | 8-10 hours |
| Core Skill Feature | Data Reconnaissance + Provider Sourcing |
| API Keys Required | z.ai GLM API, Mapbox API (optional) |

---

## The Problem

Finding the right service provider — whether it's a plumber, a freelance designer, a SaaS consultant, or a legal advisor — remains one of the most frustrating and inefficient experiences in both consumer and business contexts. The existing solutions are fundamentally broken. Yelp and Google Reviews are gamed by businesses and cluttered with fake reviews. Thumbtack and TaskRabbit take massive commissions that inflate prices and incentivize providers to cut corners. Industry-specific directories are often outdated, unmaintained, and lack the depth needed for informed decisions. For niche or hyperlocal needs, the situation is even worse — there may be only a handful of qualified providers in a given area, but discovering them requires asking friends, posting in local Facebook groups, or cold-calling from a phone directory. The problem is particularly acute for business services where the stakes are higher: hiring the wrong consultant, agency, or contractor can cost thousands of dollars and months of wasted time. Meanwhile, the best providers are often the hardest to find because they're small operations that rely entirely on word-of-mouth and don't appear in any directory. There's a massive information asymmetry: providers who are great at their craft but terrible at marketing are invisible, while mediocre providers with big marketing budgets dominate search results. What's missing is a data-driven approach to provider discovery that uses real signals — social mentions, community recommendations, project portfolios, and engagement patterns — to surface the best providers regardless of their marketing spend or directory presence.

---

## The Solution

The Provider Marketplace Finder is a hyperlocal marketplace discovery tool that uses the last30days skill's Data Reconnaissance and Provider Sourcing capabilities to build real market maps with contactable providers. Instead of relying on traditional directories, the system scans social media, community forums, review sites, and professional networks to identify providers based on actual signals of quality: community recommendations, portfolio mentions, engagement patterns, and peer endorsements. The Data Reconnaissance module queries multiple sources to find providers in a given category and location, extracting names, specialties, contact information, and social proof signals. The Provider Sourcing module then enriches each provider profile with additional data: years of experience, project history, pricing indicators, availability signals, and review sentiment. The result is a dynamic market map — a visual and searchable directory of providers ranked by Signal Score (a composite of recommendation frequency, sentiment, portfolio strength, and community standing). Each provider card includes contact options (email, phone, social DM), a brief profile, and the supporting signals that determined their ranking. For hackathon teams, the Provider Marketplace Finder can be adapted to any vertical in minutes — from finding freelance React developers to sourcing local catering for an event — and the market map can be embedded as a widget on any website or exported as a shareable report.

---

## Architecture

The Provider Marketplace Finder is built as a three-stage pipeline: Reconnaissance, Enrichment, and Presentation. The Reconnaissance stage uses the last30days Data Reconnaissance module to scan Reddit (local subreddits, professional communities), X (service provider mentions), Facebook Groups (community recommendations), and review sites (Google, Clutch, G2). Each scan extracts raw provider mentions with context: who recommended them, what for, and what was said. The Enrichment stage uses the Provider Sourcing module to enhance each raw provider mention with structured data: business name, contact information, website URL, years in operation, project portfolio links, pricing signals, and availability indicators. Entity Resolution is critical here to merge multiple mentions of the same provider across sources (e.g., "Smith Plumbing" on Reddit = "J. Smith & Sons" on Yelp). The Presentation stage builds a market map using Mapbox (for geographic visualization) and a searchable directory with provider cards. Each card shows the provider's Signal Score, supporting evidence (quotes and links), and contact options. The system supports both web-based exploration and exportable reports (HTML brief format).

```
[Category + Location] → Data Reconnaissance → Raw Provider Mentions
                                                        ↓
                                            Entity Resolution + Dedup
                                                        ↓
                                              Provider Sourcing (Enrichment)
                                                        ↓
                                            Signal Score Calculation
                                                        ↓
[Market Map] ← Presentation Layer ← Ranked Provider Directory
```

---

## Data Flow

1. User specifies category and location (e.g., "freelance React developers in Austin, TX" or "plumbers in Brooklyn").
2. Data Reconnaissance scans Reddit (relevant subreddits), X (mentions and recommendations), review sites, and professional networks.
3. Raw provider mentions are extracted: `{ name, source, context, sentiment, url, timestamp }`.
4. Entity Resolution merges mentions of the same provider across sources using name matching and contextual signals.
5. Provider Sourcing enriches each unique provider with contact info, website, portfolio, pricing indicators.
6. Signal Score is calculated for each provider: weighted composite of recommendation frequency, sentiment, portfolio strength, community standing.
7. Providers are ranked by Signal Score and grouped by sub-specialty and availability.
8. Market Map is rendered with geographic visualization (Mapbox) and searchable directory.
9. Provider cards are generated with contact options, profile summary, and supporting evidence.
10. User can filter, search, and export results as HTML brief or JSON.

---

## Skill API Mapping

| Feature Step | Skill API / Command | Parameters |
|---|---|---|
| Category Scan | `/scan <category> --location <loc>` | category, location, depth |
| Data Reconnaissance | Built-in module | sources, keywords, location |
| Entity Resolution | Auto (built-in) | match_threshold |
| Provider Sourcing | Built-in module | provider_name, enrichment_fields |
| Signal Score | Built-in calculator | recommendation_freq, sentiment, portfolio, community |
| Market Map | Mapbox API + custom renderer | providers, location, zoom |
| HTML Brief | `/brief <market> --format html` | category, location, top_n |
| Export | Custom endpoint | format (html, json, csv), filters |

---

## Tech Stack

- **Frontend**: Next.js 16, TypeScript, Tailwind CSS 4, shadcn/ui, Mapbox GL JS for geographic visualization
- **AI/Generation**: z.ai GLM API for provider profile summarization and enrichment narratives
- **Signal Processing**: last30days skill (data reconnaissance, provider sourcing, entity resolution, cluster merge)
- **Geographic**: Mapbox API for market map rendering and geocoding
- **Database**: Prisma ORM with PostgreSQL for provider profiles and scan history
- **Export**: Custom HTML Brief module + JSON/CSV export endpoints
- **Deployment**: Vercel (frontend + API routes)

---

## Implementation Steps

| Step | Task | Time Estimate |
|---|---|---|
| 1 | Set up Next.js project with marketplace layout and search UI | 1 hour |
| 2 | Build category + location input form with autocomplete | 45 min |
| 3 | Implement Data Reconnaissance integration | 1.5 hours |
| 4 | Build Entity Resolution and deduplication pipeline | 1 hour |
| 5 | Implement Provider Sourcing enrichment module | 1.5 hours |
| 6 | Build Signal Score calculator and provider ranking | 45 min |
| 7 | Implement Mapbox market map visualization | 1.5 hours |
| 8 | Build provider cards with contact options and evidence | 1 hour |
| 9 | Add filtering, search, and export functionality | 1 hour |
| 10 | Polish UI, add demo data, and test end-to-end flow | 45 min |

**Total estimated time: ~10 hours**

---

## Demo Script (3-Minute Walkthrough)

**Minute 0:00-0:40 — Search & Reconnaissance**
Open the Provider Marketplace Finder. Enter category: "Freelance React Developers" and location: "Austin, TX." Click "Find Providers." A loading animation shows the Data Reconnaissance progress: "Scanning Reddit... Scanning X... Scanning professional networks..." Raw mentions stream in on the left side of the screen.

**Minute 0:40-1:30 — Market Map & Provider Discovery**
The results appear as a Mapbox market map with provider pins clustered by neighborhood. Each pin shows the provider's Signal Score. Zoom into East Austin — three high-scoring providers are clustered near the tech corridor. Click a pin to see a preview card: "Sarah Chen — Signal Score: 8.9. Recommended 12x in r/Austin. Portfolio: 3 SaaS products. Availability: Open to new projects."

**Minute 1:30-2:15 — Provider Card & Evidence**
Click into Sarah Chen's full profile card. See the supporting evidence: 5 Reddit recommendations with quotes, 3 X endorsements, a portfolio link to her GitHub, and pricing indicators ("mid-range, project-based"). Contact options: email, Calendly link, X DM. Explain how the Signal Score is calculated from these real community signals, not paid placements.

**Minute 2:15-3:00 — Export & Embedding**
Click "Export Market Map" to generate an HTML Brief with the top 10 providers, their Signal Scores, and contact information. Show the beautifully formatted output suitable for sharing with a team. Alternatively, show the embed widget code for adding the market map to any website. End by emphasizing: "The best providers aren't the ones with the biggest ad budgets — they're the ones with the strongest community signals. The Provider Marketplace Finder surfaces them using real data, not paid placements."
