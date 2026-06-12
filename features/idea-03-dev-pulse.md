# Developer Pulse Newsletter

## Quick Stats

| Metric | Value |
|---|---|
| Difficulty | Beginner-Intermediate |
| Estimated Build Time | 4-6 hours |
| Core Skill Feature | Briefing Engine + Watchlist |
| API Keys Required | z.ai GLM API, Email API (Resend/SendGrid) |

---

## The Problem

The developer ecosystem moves at a blistering pace. Every week, hundreds of significant events occur across open-source repositories, framework releases, security advisories, funding rounds, and community debates. For individual developers, staying informed is a part-time job in itself — endlessly scrolling Hacker News, subscribing to dozens of RSS feeds, monitoring GitHub trending repos, and still feeling like you're always behind. Teams face an even bigger challenge: knowledge silos form when only one person on the team follows a particular community or technology, and critical signals get missed entirely. Existing newsletters like TLDR, Hacker Newsletter, and Bytes do an excellent job, but they're generic — they cover the entire ecosystem and can't be personalized to your specific stack, interests, or business context. A React developer doesn't need to read about Rust compiler changes, and a fintech team doesn't need updates on game engine releases. The signal-to-noise ratio of generic developer news is simply too low for professionals who need actionable, relevant intelligence. Furthermore, creating a custom newsletter manually requires curating sources, writing summaries, designing templates, and managing distribution — a process that takes 4-6 hours per issue and is completely unsustainable for individuals or small teams. The result is that most developers either drown in irrelevant information or give up on staying current, both of which lead to suboptimal technical decisions and missed opportunities.

---

## The Solution

Developer Pulse Newsletter is an auto-generated weekly digest that uses the last30days skill's Briefing Engine, Watchlist, and HTML Brief output to produce a fully personalized, email-ready developer newsletter. Instead of manually curating content, you define your interests once — specific technologies, repositories, companies, or verticals — and the system does the rest. The Briefing Engine runs the signal scanner across your watchlisted entities, applies entity resolution to deduplicate across sources, and uses cluster merge to group related developments into coherent stories. The GLM API then generates concise, expert-level summaries of each story with context about why it matters. The HTML Brief module produces a beautifully formatted, email-ready output that works across all major email clients. The Watchlist system handles subscription management, delivery scheduling, and personalization. You can set up multiple "beats" — for example, a "Frontend" beat covering React, Next.js, and Tailwind, and a "DevOps" beat covering Kubernetes, Docker, and Terraform. Each beat produces its own section in the newsletter. The system also tracks what you've already been sent to avoid repetition. For hackathon teams, Developer Pulse can be set up in under an hour and immediately start delivering high-signal, relevant developer intelligence that informs build decisions throughout the weekend. It's like having a dedicated developer relations researcher who works 24/7 for free.

---

## Architecture

Developer Pulse follows a content pipeline architecture with four stages: Source Curation, Signal Processing, Content Generation, and Distribution. The Source Curation stage uses the Watchlist system to maintain a dynamic list of monitored entities (technologies, repos, people, companies). Each entity has associated source types and keywords. The Signal Processing stage runs the last30days signal scanner weekly (or on-demand), pulling from GitHub, Hacker News, Reddit, X, and official blogs. Raw signals pass through entity resolution and cluster merge to produce deduplicated, grouped story clusters. The Content Generation stage sends each cluster to the GLM API with a structured prompt that includes the cluster context, the subscriber's interest profile, and a style guide (tone, length, formatting). GLM returns a polished summary with a headline, body, and "Why It Matters" callout. The Distribution stage uses the HTML Brief module to assemble all summaries into a single email template, then delivers via Resend or SendGrid API. A scheduling layer (node-cron) triggers the full pipeline weekly, and a web dashboard shows upcoming issues, subscriber stats, and preview functionality.

```
[Watchlist Entities] → Signal Scanner → Entity Resolution → Cluster Merge
                                                              ↓
[Email Delivery] ← HTML Brief Assembler ← GLM Summarizer ← Story Ranker
     (Resend)           ↓
                  [Preview Dashboard]
```

---

## Data Flow

1. User defines interest beats via `/watch add` commands (e.g., `/watch add react nextjs tailwindcss --beat frontend`).
2. Scheduler triggers weekly scan (or user invokes `/scan developer-pulse --beat all`).
3. Signal Scanner queries GitHub trending, Hacker News, Reddit r/programming, X developer accounts.
4. Raw signals are normalized: `{ entity, source, title, content, url, engagement, timestamp }`.
5. Entity Resolution maps signals to watchlisted entities with fuzzy matching.
6. Cluster Merge groups related signals into story clusters (e.g., "React 19 RC released" + "React team AMA" = one story).
7. Story Ranker scores clusters by relevance to subscriber interests and engagement metrics.
8. GLM API generates summary for each cluster with headline, body, and "Why It Matters" callout.
9. HTML Brief Assembler combines all summaries into a responsive email template.
10. Email API delivers the newsletter to all subscribers; preview is available on the web dashboard.

---

## Skill API Mapping

| Feature Step | Skill API / Command | Parameters |
|---|---|---|
| Define Beats | `/watch add <entities> --beat <name>` | entity_list, beat_name |
| Signal Scan | `/scan developer-pulse --beat <name>` | beat, time_range, depth |
| Entity Resolution | Auto (built-in) | match_threshold |
| Cluster Merge | Auto (built-in) | min_cluster_size |
| Story Summarization | GLM Chat API | prompt, cluster_data, style_guide |
| HTML Brief | `/brief <beat> --format html` | beat, sections, template |
| Watchlist Subscribe | `/watch subscribe --email <addr>` | email, beats, frequency |
| Email Delivery | Resend/SendGrid API | to, subject, html_body |

---

## Tech Stack

- **Frontend**: Next.js 16, TypeScript, Tailwind CSS 4, shadcn/ui (for preview dashboard)
- **AI/Generation**: z.ai GLM API for story summarization and headline generation
- **Signal Processing**: last30days skill (signal scanner, briefing engine, watchlist, entity resolution, cluster merge, HTML brief)
- **Email Delivery**: Resend API (primary) or SendGrid (fallback)
- **Scheduling**: node-cron for weekly pipeline triggers
- **Database**: Prisma ORM with SQLite for subscriber management and issue history
- **Template Engine**: Custom HTML Brief module with MJML for email-compatible markup
- **Deployment**: Vercel with cron jobs for scheduled execution

---

## Implementation Steps

| Step | Task | Time Estimate |
|---|---|---|
| 1 | Set up Next.js project with dashboard and newsletter preview UI | 45 min |
| 2 | Implement beat/watchlist management (create, edit, delete beats) | 1 hour |
| 3 | Integrate signal scanner for weekly content discovery | 1 hour |
| 4 | Build story cluster ranking and selection logic | 45 min |
| 5 | Integrate GLM API for automated story summarization | 1 hour |
| 6 | Build HTML Brief email template with MJML | 45 min |
| 7 | Implement email delivery via Resend API | 30 min |
| 8 | Add scheduling, subscriber management, and issue history | 45 min |
| 9 | Polish preview dashboard, add demo data, and test email rendering | 30 min |

**Total estimated time: ~6 hours**

---

## Demo Script (3-Minute Walkthrough)

**Minute 0:00-0:40 — Beat Setup & Source Curation**
Open the Developer Pulse dashboard. Show the "Create New Beat" form. Enter beat name: "Frontend Ecosystem." Add entities: "React, Next.js, Tailwind CSS, Vite, Remix." Click "Create Beat." Explain that the system will now monitor all relevant sources for these technologies.

**Minute 0:40-1:40 — Signal Scanning & Story Generation**
Click "Run Scan Now" to trigger an immediate scan. Watch the progress indicator as the signal scanner queries GitHub, Hacker News, Reddit, and X. Story clusters appear on screen: "React 19 Compiler Ships to Stable," "Vite 6 Bundles 40% Faster," "Tailwind CSS v4.0 Launches." Click into the React story to show the GLM-generated summary with headline, body, and "Why It Matters" callout.

**Minute 1:40-2:20 — HTML Brief Preview & Assembly**
Switch to the "Preview Issue" tab to see the assembled HTML Brief. Show how stories are organized by beat, with a clean table of contents and responsive layout. Explain that this exact HTML is what will be delivered to subscribers' inboxes. Point out the personalization: no Rust or Go stories — only Frontend content.

**Minute 2:20-3:00 — Delivery & History**
Click "Send Test Email" and show the email arriving in a test inbox. Switch to the "Subscribers" tab to show the watchlist management. Switch to "Issue History" to show previous issues with open rates. End by emphasizing that this entire pipeline runs on autopilot every week, delivering personalized developer intelligence without any manual curation — a self-sustaining newsletter in a box.
