# Social Signal Validator

## Quick Stats

| Metric | Value |
|---|---|
| Difficulty | Beginner |
| Estimated Build Time | 3-4 hours |
| Core Skill Feature | Quick Scan Mode + Signal Score |
| API Keys Required | z.ai GLM API |

---

## The Problem

Hackathons are won and lost in the first two hours — the ideation phase. Teams that pick a strong, validated idea build with confidence and ship polished products. Teams that guess wrong spend the entire weekend pivoting, refactoring, and ultimately presenting something half-baked. Yet the ideation process at most hackathons is embarrassingly unscientific: someone suggests an idea they thought of in the shower, the team debates it based on gut feelings and anecdotal evidence, and they commit based on enthusiasm rather than data. The problem is that there's no quick, reliable way to validate a hackathon idea against real market signals. Traditional validation requires customer interviews, landing page tests, and competitive analysis — processes that take days or weeks, not the 60 seconds you have before the team starts coding. Even experienced founders fall into the trap of building products for imagined audiences. They see a pain point in their own lives and generalize it to millions of potential users, only to discover post-launch that the market is tiny, the willingness to pay is zero, or three well-funded competitors already exist. The cost of a bad idea at a hackathon isn't just a lost weekend — it's a missed opportunity to build something that could have been the start of a real business. What's needed is a rapid validation tool that takes an idea description as input and returns a quantified Signal Score with supporting evidence in under 60 seconds, giving teams the confidence to commit or the data to pivot before they write a single line of code.

---

## The Solution

The Social Signal Validator is a lightning-fast idea validation tool that uses the last30days skill's Quick Scan Mode to return a Signal Score (0-10) with supporting quotes and engagement metrics in under 60 seconds. You simply describe your idea in plain English — "A time-tracking app for freelance designers" — and the validator immediately scans Reddit, X, TikTok, and relevant forums for signals of demand, competition, and monetization potential. The output is a single, scannable card with three sections: Signal Score (a 0-10 composite of demand, competition, and timing), Evidence (real user quotes expressing the pain point, with engagement metrics and source links), and Verdict (a one-sentence recommendation: "Build it," "Pivot to X," or "Skip — saturated market"). The Signal Score is calculated from four weighted factors: Demand Volume (how many people are expressing this need), Engagement Intensity (how strongly they feel about it — measured by upvotes, retweets, comment depth), Competitive Density (how many existing solutions are mentioned), and Timing Signal (whether the trend is growing, stable, or declining). The validator also surfaces "pivot hints" — adjacent ideas with higher signal scores that the team might not have considered. For hackathon teams, this means you can validate five ideas in five minutes and commit to the best one with data-backed confidence, turning the ideation phase from a debate into a data-driven decision.

---

## Architecture

The Social Signal Validator is built as a single-page web application with a lightweight API backend. The frontend is a Next.js page with a centered input field and a results card. The backend exposes a single `/validate` endpoint that orchestrates the validation pipeline. When a request comes in, the backend invokes the last30days Quick Scan Mode with the idea description as the query. Quick Scan runs a focused, shallow scan (depth=1) across Reddit, X, and TikTok, returning a condensed set of top signals. The backend then calculates the Signal Score using a weighted composite of demand volume, engagement intensity, competitive density, and timing trend. Supporting quotes are extracted from the scan results and ranked by relevance and engagement. The GLM API generates the Verdict sentence and any pivot hints based on the scored data. The entire pipeline is optimized for speed: Quick Scan uses cached results where possible, the scoring algorithm is deterministic, and the GLM call uses a short max_tokens limit. The target end-to-end latency is under 60 seconds for any idea.

```
[Idea Description] → Quick Scan Mode → Raw Signals
                                              ↓
                                    Signal Score Calculator
                                    (Demand + Engagement + 
                                     Competition + Timing)
                                              ↓
[Results Card] ← Verdict Generator (GLM) ← Scored Signals + Top Quotes
```

---

## Data Flow

1. User types idea description into the web input field (e.g., "Time-tracking app for freelance designers").
2. Frontend sends POST request to `/validate` endpoint with the idea text.
3. Backend invokes last30days Quick Scan Mode with `depth=1` and the idea as query.
4. Quick Scan returns top signals from Reddit, X, and TikTok (typically 20-50 results).
5. Backend extracts demand volume (mention count), engagement intensity (upvotes, retweets, comment depth).
6. Backend runs competitive density analysis: counts mentions of existing solutions in the signal set.
7. Backend calculates timing trend: compares mention volume in last 7 days vs. previous 23 days.
8. Composite Signal Score is calculated: `0.3*demand + 0.3*engagement + 0.25*(10-competition) + 0.15*timing`.
9. Top 5 user quotes are extracted and ranked by relevance + engagement.
10. GLM API generates Verdict sentence and pivot hints from scored data.
11. Results card is returned to frontend: Signal Score, Evidence (quotes with metrics), Verdict, Pivot Hints.

---

## Skill API Mapping

| Feature Step | Skill API / Command | Parameters |
|---|---|---|
| Quick Scan | `/scan <idea> --depth 1` | query, depth, time_range |
| Signal Score | Built-in calculator | demand, engagement, competition, timing |
| Quote Extraction | Auto (built-in) | relevance_threshold, max_quotes |
| Competitive Density | `/compare <idea>` | idea_text, depth |
| Verdict Generation | GLM Chat API | score, evidence, max_tokens=100 |
| Pivot Hints | GLM Chat API | idea_text, signal_data, adjacent_niches |

---

## Tech Stack

- **Frontend**: Next.js 16, TypeScript, Tailwind CSS 4, shadcn/ui (input + results card)
- **API Backend**: Next.js API Routes (single `/validate` endpoint)
- **AI/Generation**: z.ai GLM API for verdict and pivot hint generation
- **Signal Processing**: last30days skill (Quick Scan Mode, signal scoring)
- **Caching**: In-memory LRU cache for repeated idea validations
- **Analytics**: Vercel Analytics for tracking validation volume and score distributions
- **Deployment**: Vercel (serverless functions for API)

---

## Implementation Steps

| Step | Task | Time Estimate |
|---|---|---|
| 1 | Set up Next.js project with single-page layout | 20 min |
| 2 | Build idea input UI with loading states and animations | 30 min |
| 3 | Implement `/validate` API endpoint with Quick Scan integration | 1 hour |
| 4 | Build Signal Score calculator with weighted composite algorithm | 45 min |
| 5 | Implement quote extraction and ranking logic | 30 min |
| 6 | Integrate GLM API for verdict and pivot hint generation | 30 min |
| 7 | Build results card UI (Signal Score gauge, quotes, verdict, pivots) | 45 min |
| 8 | Add caching, error handling, and edge cases | 20 min |
| 9 | Polish animations, add demo data, test end-to-end latency | 15 min |

**Total estimated time: ~4 hours**

---

## Demo Script (3-Minute Walkthrough)

**Minute 0:00-0:30 — The Problem & First Validation**
Open the Social Signal Validator. The page is minimal: a single input field with the placeholder "Describe your hackathon idea..." Type "A time-tracking app for freelance designers" and hit Enter. A sleek loading animation appears with the text "Scanning social signals..."

**Minute 0:30-1:15 — Signal Score & Evidence**
The results card appears in under 60 seconds. A large circular gauge shows the Signal Score: 6.4/10. Below it, three sub-scores: Demand 8.2, Engagement 7.1, Competition 3.8 (high = bad), Timing 5.9. Scroll to the Evidence section: five real user quotes from Reddit and X, each with engagement metrics — "I've tried 5 time trackers and none work for freelance project switching" (347 upvotes, r/freelance).

**Minute 1:15-2:00 — Verdict & Pivot Hints**
The Verdict section: "Moderate signal — demand exists but competition is significant. Consider narrowing to a specific freelance niche." Pivot Hints appear: "Time-tracking for freelance developers (Signal Score: 8.1)" and "Invoice + time-tracking combo for EU freelancers (Signal Score: 7.6)."

**Minute 2:00-2:45 — Rapid Validation Loop**
Click "Validate another idea" and type "AI-powered recipe generator from fridge photos." Score: 4.2/10. Verdict: "Skip — saturated market with low willingness to pay." Try a third: "Slack bot that summarizes long threads for managers." Score: 8.7/10. Verdict: "Build it — strong demand, low competition, growing trend."

**Minute 2:45-3:00 — Confidence & Commitment**
Show the contrast between the three ideas. Emphasize that in under 3 minutes, you validated three ideas and identified the clear winner — a process that would normally take days of manual research. The team can now commit to building the Slack thread summarizer with data-backed confidence, knowing the market signal is real and the opportunity is validated.
