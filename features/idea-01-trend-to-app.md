# Trend-to-App Builder

## Quick Stats

| Metric | Value |
|---|---|
| Difficulty | Intermediate |
| Estimated Build Time | 6-8 hours |
| Core Skill Feature | Signal Scanner + Landing Page Factory |
| API Keys Required | z.ai GLM API, Vercel Deployment Token |

---

## The Problem

Every day, thousands of pain points are expressed across Reddit, X (Twitter), TikTok, and niche forums. These are real people describing real frustrations — bugs they can't fix, workflows that waste hours, tools that are overpriced or overcomplicated. Yet the vast majority of these signals evaporate into the noise of the internet within hours. Indie developers and hackathon teams spend precious weekend hours brainstorming ideas from scratch, often landing on saturated markets or building solutions in search of problems. The gap between "someone is complaining about this right now" and "here's a working micro-app that solves it" is enormous. Traditional market research takes weeks, requires expensive tools, and still produces guesswork. Meanwhile, the window of opportunity for a trending pain point slams shut as competitors flood in or the conversation moves on. Hackathon participants especially suffer: they have 48-72 hours to ship something meaningful, but spend the first 12-24 hours just figuring out what to build. The fundamental inefficiency is that human trend-spotting cannot keep pace with the volume and velocity of online conversation, and even when a trend is spotted, the translation from "trending complaint" to "deployed solution" involves dozens of manual steps that drain creative energy and time.

---

## The Solution

The Trend-to-App Builder collapses the entire ideation-to-deployment pipeline into a single automated workflow powered by the last30days skill on chat.z.ai. It starts by running the signal scanner across Reddit, X, and TikTok to identify trending pain points with high engagement and low existing solutions. The scanner surfaces not just topics, but specific user quotes, engagement metrics, and competitive density scores. Once a high-signal pain point is identified, the system automatically feeds it into the z.ai GLM model to generate a complete vibe-coded micro-app — including UI components, API routes, and database schema. The generated app is then pushed through the Landing Page Factory to create a conversion-optimized landing page, and deployed to Vercel with a single command. The entire loop from "What are people complaining about?" to "Here's your live app" takes under 10 minutes. This means hackathon teams can run the scanner multiple times, test multiple ideas, and ship the one with the strongest signal — all before lunch on Saturday. The solution doesn't just save time; it fundamentally changes the strategy from "build and hope" to "scan, validate, and build with confidence."

---

## Architecture

The Trend-to-App Builder follows a pipeline architecture with five distinct stages: Signal Acquisition, Pain Point Extraction, App Generation, Landing Page Assembly, and Deployment. The Signal Acquisition stage uses the last30days skill's signal scanner to poll Reddit (via subreddit search), X (via keyword and hashtag search), and TikTok (via trend endpoint). Raw posts and comments are ingested into a processing queue. The Pain Point Extraction stage runs the skill's entity resolution and cluster merge algorithms to group related complaints, deduplicate across platforms, and score each cluster on engagement velocity, solution gap, and monetization potential. The App Generation stage sends the top-scored pain point to the z.ai GLM API with a structured prompt that includes the pain point description, target user persona, and desired feature set. GLM returns a complete Next.js project scaffold with Tailwind styling, shadcn/ui components, and API routes. The Landing Page Assembly stage takes the generated app metadata and feeds it through the Landing Page Factory module to produce a conversion-optimized page with hero section, feature list, pricing card, and CTA. The Deployment stage uses the Vercel CLI to push the project to a preview URL, with automatic environment variable injection for API keys.

```
[Reddit/X/TikTok] → Signal Scanner → Cluster Merge → Pain Point Ranker
                                                           ↓
[Vercel Deploy] ← Landing Page Factory ← GLM App Generator ←┘
```

---

## Data Flow

1. User invokes `/scan trending-pain-points` on chat.z.ai, specifying vertical (e.g., "developer tools", "productivity", "finance").
2. Signal Scanner queries Reddit (top 20 subreddits), X (trending hashtags), and TikTok (trending sounds/hashtags) for the past 30 days.
3. Raw posts and comments are normalized into a unified schema: `{ platform, author, content, engagement_score, timestamp, thread_url }`.
4. Entity Resolution groups mentions of the same pain point across platforms (e.g., "API rate limiting" on Reddit = "rate limit errors" on X).
5. Cluster Merge combines resolved entities into thematic clusters and assigns each a Signal Score (0-10) based on engagement velocity and solution gap.
6. Top 3 clusters are presented to the user with quotes, metrics, and competitive density.
7. User selects one cluster; the system sends the pain point metadata to the GLM API for app generation.
8. GLM returns a complete Next.js project (pages, components, API routes, schema.prisma).
9. Landing Page Factory generates a conversion-optimized landing page from the app metadata.
10. Project is deployed to Vercel via CLI, returning a live preview URL.

---

## Skill API Mapping

| Feature Step | Skill API / Command | Parameters |
|---|---|---|
| Signal Scan | `/scan <vertical>` | vertical, depth, time_range |
| Entity Resolution | Auto (built-in) | cluster_threshold, dedupe |
| Cluster Merge | Auto (built-in) | min_cluster_size, scoring_weights |
| Signal Score | `/validate <idea>` | idea_text, vertical |
| App Generation | GLM Chat API | prompt, model, max_tokens |
| Landing Page | `/landing-page-factory` | app_name, description, features |
| Deployment | Vercel CLI | project_path, env_vars |

---

## Tech Stack

- **Frontend**: Next.js 16 with App Router, TypeScript, Tailwind CSS 4, shadcn/ui
- **AI/Generation**: z.ai GLM API (chat completions with structured output)
- **Signal Processing**: last30days skill (signal scanner, entity resolution, cluster merge)
- **Deployment**: Vercel (preview deployments with automatic HTTPS)
- **Database**: Prisma ORM with SQLite (for app metadata and scan history)
- **Queue**: In-process job queue for scan pipeline orchestration
- **Monitoring**: Vercel Analytics + custom webhook for deployment status

---

## Implementation Steps

| Step | Task | Time Estimate |
|---|---|---|
| 1 | Set up Next.js project with App Router and Tailwind CSS | 30 min |
| 2 | Implement signal scanner integration with last30days skill API | 1.5 hours |
| 3 | Build pain point ranking UI with cluster visualization | 1 hour |
| 4 | Integrate GLM API for app generation with structured prompts | 1.5 hours |
| 5 | Build Landing Page Factory module with template system | 1 hour |
| 6 | Implement Vercel deployment pipeline with CLI integration | 45 min |
| 7 | Add scan history persistence with Prisma + SQLite | 30 min |
| 8 | Polish UI, add loading states, error handling, and demo data | 45 min |

**Total estimated time: ~7.5 hours**

---

## Demo Script (3-Minute Walkthrough)

**Minute 0:00-0:30 — Introduction & Problem Statement**
Open the Trend-to-App Builder dashboard. Show the empty state with a single search bar: "What vertical are you interested in?" Type "developer tools" and hit Enter. Explain that the system is about to scan Reddit, X, and TikTok for trending pain points in that space.

**Minute 0:30-1:30 — Signal Scanning & Pain Point Discovery**
Watch as the signal scanner progress bar fills. Three pain point clusters appear on screen, each with a Signal Score, user quotes, and engagement metrics. Hover over the top result — "API rate limiting is killing my workflow" (Signal Score: 8.7, 342 mentions across platforms, low competitive density). Explain how entity resolution grouped related complaints and the scoring system works.

**Minute 1:30-2:15 — App Generation**
Click "Build This" on the top pain point. The GLM API is invoked — show the generation progress with a live terminal view. Within seconds, a complete Next.js micro-app appears: a rate-limit monitor dashboard with alerting, pricing page, and onboarding flow. Show the file tree of the generated project.

**Minute 2:15-3:00 — Landing Page & Deployment**
The Landing Page Factory automatically generates a conversion-optimized landing page. Click "Deploy to Vercel" — watch the deployment progress. The live URL appears: `rate-limit-monitor.vercel.app`. Open it in a new tab to show the fully functional app. End by emphasizing that this entire pipeline — from trend discovery to live deployment — took under 10 minutes, turning a weekend hackathon strategy from "guess and build" into "scan, validate, and ship with confidence."
