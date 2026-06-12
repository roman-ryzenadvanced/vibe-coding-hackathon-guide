# Pivot Predictor

## Quick Stats

| Metric | Value |
|---|---|
| Difficulty | Advanced |
| Estimated Build Time | 10-12 hours |
| Core Skill Feature | Failure/Pivot Protocol + Signal Scanner |
| API Keys Required | z.ai GLM API, Monitoring Webhook URL |

---

## The Problem

Startups don't fail overnight — they fail gradually, then suddenly. The warning signs are always there: flatlined growth, rising churn, declining engagement, customer support tickets that reveal fundamental misalignment, and competitors gaining ground in your core market. Yet founders are notoriously bad at recognizing these signals in their own projects. Confirmation bias, sunk cost fallacy, and emotional attachment to the original vision create a powerful blind spot. By the time the data is undeniable, it's often too late — the runway is gone, the team is demoralized, and the pivot options have narrowed to zero. The problem is even more acute for indie hackers and small teams who lack the benefit of board meetings, investor check-ins, or executive teams providing alternative perspectives. They're flying solo, often staring at the same dashboards day after day, unable to see the forest for the trees. Even when founders do recognize that something is wrong, they rarely know what to do about it. Should they pivot the product, change the target market, adjust the pricing, or start over entirely? Each of these is a fundamentally different strategy with different risks and timelines. The lack of a systematic, data-driven framework for diagnosing failure modes and prescribing pivot actions means that most founders either stick with a failing idea too long (wasting months of runway) or pivot reactively without understanding why the original idea failed, repeating the same mistakes in a new domain. What's needed is an objective diagnostic tool that connects live metrics to known failure patterns and provides specific, actionable pivot prescriptions.

---

## The Solution

The Pivot Predictor is an interactive diagnostic tool that uses the last30days skill's Failure/Pivot Protocol to automatically detect failure modes in a live project and prescribe specific pivot actions. The tool ingests real-time metrics from your project (revenue, churn, user growth, engagement, support volume, competitive movements) and runs them through the Failure/Pivot Protocol — a structured diagnostic framework that maps metric patterns to known failure modes (Market Misfit, Feature Creep, Pricing Failure, Competitive Erosion, Channel Exhaustion, and Timing Miss). Each failure mode has a specific set of pivot prescriptions drawn from analysis of hundreds of startup pivots. For example, Market Misfit prescribes: "Narrow your target segment by 10x and revalidate," while Competitive Erosion prescribes: "Find an underserved adjacent niche using signal scanner." The tool also connects to live market signals via the Signal Scanner to detect emerging opportunities that align with your existing capabilities. The interface is designed as a "Health Dashboard" with a real-time Failure Risk Score (0-100), individual failure mode indicators, and a "Prescribe Pivot" button that generates a detailed pivot plan with timeline, resource requirements, and probability of success. For hackathon teams, the Pivot Predictor can be used proactively: input your hackathon project metrics and get an instant assessment of failure risk, along with recommendations for which aspects to prioritize during the remaining build time.

---

## Architecture

The Pivot Predictor is built as a three-layer system: Metric Ingestion, Diagnostic Engine, and Prescription Generator. The Metric Ingestion layer accepts data through three channels: API push (your app sends metrics via webhook), manual input (a form for entering key metrics), and automated integration (connects to Stripe for revenue, Mixpanel for engagement, and the last30days signal scanner for competitive movements). All metrics are normalized and stored in a time-series database. The Diagnostic Engine runs the Failure/Pivot Protocol on each metric refresh. The protocol consists of six failure mode detectors, each implemented as a rule-based classifier with tunable thresholds. Each detector outputs a Failure Mode Probability (0-1), and the composite Failure Risk Score is the weighted maximum. When a failure mode probability exceeds the alert threshold, the engine triggers the Prescription Generator. The Prescription Generator uses the GLM API to synthesize a pivot plan that is specific to the detected failure mode, the project's current metrics, and the available market signals. It also queries the Signal Scanner for adjacent opportunities that match the team's existing capabilities. The Health Dashboard presents all of this in a single view with real-time updates, historical trends, and a scenario modeling feature that lets you project outcomes of different pivot strategies.

```
[Live Metrics] → Metric Ingestion → Time-Series Store
                                        ↓
[Signal Scanner] → Competitive Data → Diagnostic Engine
                                        ↓
                              Failure/Pivot Protocol
                              (6 Failure Mode Detectors)
                                        ↓
[Health Dashboard] ← Prescription Generator ← Failure Mode + Market Signals
```

---

## Data Flow

1. User connects project metrics via API webhook, manual input, or integration (Stripe, Mixpanel, etc.).
2. Metrics are normalized and stored in time-series database with timestamps.
3. Signal Scanner runs competitive analysis on the project's market segment.
4. Diagnostic Engine runs Failure/Pivot Protocol on the latest metrics snapshot.
5. Each of 6 failure mode detectors produces a probability score (0-1).
6. Composite Failure Risk Score is calculated as the weighted maximum of individual probabilities.
7. If any failure mode exceeds the alert threshold, the engine flags it for prescription.
8. Prescription Generator queries GLM API with failure mode, current metrics, and market signal data.
9. GLM produces a structured pivot plan: diagnosis, prescription, timeline, resource requirements, success probability.
10. Signal Scanner identifies adjacent market opportunities aligned with the team's capabilities.
11. Health Dashboard updates in real-time with Failure Risk Score, individual indicators, and pivot plan.
12. User can run scenario models to project outcomes of different pivot strategies.

---

## Skill API Mapping

| Feature Step | Skill API / Command | Parameters |
|---|---|---|
| Metric Ingestion | Webhook / Manual Form | metric_type, value, timestamp |
| Competitive Scan | `/scan competitors <vertical>` | vertical, depth |
| Failure Detection | Failure/Pivot Protocol (built-in) | metrics, thresholds |
| Signal Scan | `/scan <vertical>` | vertical, time_range |
| Pivot Prescription | GLM Chat API | failure_mode, metrics, signals |
| Scenario Modeling | GLM Chat API | current_state, pivot_strategy, time_horizon |
| Health Report | `/brief <project> --format html` | project, time_range, sections |

---

## Tech Stack

- **Frontend**: Next.js 16, TypeScript, Tailwind CSS 4, shadcn/ui, Recharts for health visualizations
- **AI/Generation**: z.ai GLM API for pivot prescription and scenario modeling
- **Signal Processing**: last30days skill (signal scanner, failure/pivot protocol, entity resolution)
- **Integrations**: Stripe API (revenue), Mixpanel API (engagement), custom webhook for arbitrary metrics
- **Database**: Prisma ORM with PostgreSQL for metrics storage and time-series data
- **Real-time**: Server-Sent Events (SSE) for live dashboard updates
- **Scheduling**: node-cron for periodic diagnostic runs
- **Deployment**: Vercel (dashboard) + Railway (diagnostic worker)

---

## Implementation Steps

| Step | Task | Time Estimate |
|---|---|---|
| 1 | Set up Next.js project with Health Dashboard layout | 1 hour |
| 2 | Build metric ingestion system (webhook + manual input + Stripe integration) | 2 hours |
| 3 | Implement Failure/Pivot Protocol with 6 failure mode detectors | 2 hours |
| 4 | Build composite Failure Risk Score calculator | 45 min |
| 5 | Integrate Signal Scanner for competitive and opportunity analysis | 1 hour |
| 6 | Build Prescription Generator with GLM API | 1.5 hours |
| 7 | Implement scenario modeling feature | 1 hour |
| 8 | Build Health Dashboard UI with real-time indicators and charts | 1.5 hours |
| 9 | Add alerting, notification system, and email reports | 1 hour |
| 10 | Polish UI, add demo data, and test end-to-end diagnostic flow | 45 min |

**Total estimated time: ~12 hours**

---

## Demo Script (3-Minute Walkthrough)

**Minute 0:00-0:40 — Connecting a Project & Initial Diagnosis**
Open the Pivot Predictor Health Dashboard. Click "Connect Project" and enter demo project: "TaskFlow, a project management tool for small teams." Connect Stripe — show 3 months of revenue data: $2.1K, $1.9K, $1.7K (declining). The dashboard immediately runs the Failure/Pivot Protocol and the Failure Risk Score appears: 72/100 (elevated risk). The top failure mode is highlighted: "Market Misfit — 78% probability."

**Minute 0:40-1:40 — Failure Mode Deep Dive & Signal Context**
Click into Market Misfit to see the detailed diagnosis: "Churn rate has increased 40% month-over-month while new user acquisition has plateaued. Customer support tickets reveal users want simpler workflows, not more features." The Signal Scanner panel shows competitive data: "3 new competitors entered the 'simple project management' segment in the last 30 days with lower-priced alternatives." A timeline chart shows the deterioration.

**Minute 1:40-2:30 — Pivot Prescription**
Click "Prescribe Pivot." The GLM API generates a structured pivot plan: "Diagnosis: TaskFlow is over-serving its market with feature complexity. Prescription: Pivot to 'TaskFlow Lite' — a minimalist task tracker for individual contributors, not teams. Timeline: 2-week MVP, 6-week relaunch. Success probability: 68%." The plan includes specific next steps: "1. Survey churned users about desired simplifications. 2. Build core-only MVP (tasks + deadlines + calendar). 3. Relaunch at $5/mo (down from $15)."

**Minute 2:30-3:00 — Scenario Modeling & Opportunity Signals**
Run a scenario model: "What if we pivot to TaskFlow Lite?" The dashboard shows projected outcomes: MRR at month 6 with the pivot ($4.2K) vs. without ($1.1K). Switch to the "Opportunity Signals" tab: the Signal Scanner has identified an adjacent niche — "freelance creatives who hate project management" — with a Signal Score of 8.3. End by emphasizing: "Instead of guessing why your project is struggling, the Pivot Predictor gives you a data-driven diagnosis and a specific, actionable pivot plan — turning failure from a surprise into a strategic decision."
