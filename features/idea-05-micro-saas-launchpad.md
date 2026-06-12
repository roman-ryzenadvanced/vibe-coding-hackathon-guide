# Micro-SaaS Launch Pad

## Quick Stats

| Metric | Value |
|---|---|
| Difficulty | Advanced |
| Estimated Build Time | 10-14 hours |
| Core Skill Feature | Signal Scanner + Landing Page Factory + Ad Launch Playbook + Unit Economics |
| API Keys Required | z.ai GLM API, Vercel Token, Stripe Key, Ad Platform API |

---

## The Problem

Building a micro-SaaS product is deceptively complex. The coding part is often the easiest — the real challenges are scattered across a dozen disconnected domains: finding a validated idea, designing a conversion-optimized landing page, setting up payment infrastructure, launching acquisition channels, projecting unit economics, and creating a realistic timeline. Each of these domains requires specialized knowledge and tooling, and the switching cost between them destroys momentum. Most aspiring micro-SaaS founders follow a painfully sequential process: spend a week on ideation, another week on landing page design, a week on Stripe integration, then another week figuring out how to run their first ads — by which point they've burned through their motivation and their runway. The tools that exist for each step are siloed: Ahrefs for keyword research, Carrd for landing pages, Stripe for payments, Meta Ads Manager for acquisition, and spreadsheets for unit economics. There's no unified system that connects the signal (what to build) to the launch (how to sell it) to the economics (whether it's worth it). The result is that the vast majority of micro-SaaS attempts die in the "last mile" — the idea was good, the code worked, but the go-to-market execution fell apart because it was handled as an afterthought rather than an integrated first-class concern. For hackathon teams, this problem is existential: you have 48-72 hours to not just build but also validate and launch, and any time spent on manual infrastructure setup is time stolen from the product itself.

---

## The Solution

The Micro-SaaS Launch Pad is a one-click SaaS launcher that combines the last30days skill's Signal Scanner, Landing Page Factory, Ad Launch Playbook, Unit Economics Calculator, and 30-Day Timeline Generator into a single integrated workflow. Instead of navigating between a dozen disconnected tools, you run one command and the system produces everything you need to go from idea to live product with paying customers. The workflow starts with the Signal Scanner validating your idea — checking that real demand exists, quantifying the opportunity, and surfacing user quotes for marketing copy. Next, the Landing Page Factory generates a conversion-optimized page with hero section, feature showcase, pricing tiers, testimonials placeholder, and CTA — all deployed to Vercel. The Ad Launch Playbook creates platform-specific ad campaigns (Meta, Google, X) with targeting, creative, and budget recommendations based on the signal data. The Unit Economics Calculator (wrapping break_even.py and niche_validator.py) projects MRR, churn, CAC, LTV, and break-even timeline. Finally, the 30-Day Timeline Generator creates a week-by-week action plan with milestones, dependencies, and risk flags. The entire output is delivered as a "Launch Kit" — a single dashboard page with all resources, links, and next steps. For hackathon teams, this means you can have a validated idea, live landing page, ad campaigns, financial projections, and a 30-day plan — all before midnight on Friday.

---

## Architecture

The Micro-SaaS Launch Pad is built as a pipeline orchestrator that chains five independent modules into a sequential workflow with conditional branching. The Signal Scanner module validates the idea and produces a Market Report. The Landing Page Factory module consumes the Market Report (pain point, target persona, competitive positioning) and generates a Next.js landing page project. The Ad Launch Playbook module consumes the Market Report and Signal Scanner data to produce platform-specific campaign configurations. The Unit Economics module consumes the Market Report and Ad Launch data (projected CAC, conversion rates) to produce financial projections. The 30-Day Timeline module consumes all previous outputs to produce an actionable plan. The orchestrator manages data flow between modules, handles failures with retry logic, and provides a unified progress view. Each module can also be invoked independently for iterative refinement. The Launch Kit Dashboard assembles all outputs into a single view with live links, downloadable assets, and inline previews.

```
[Idea Input] → Signal Scanner → [Market Report]
                                    ↓              ↓              ↓
                          Landing Page     Ad Playbook    Unit Economics
                          Factory          Generator      Calculator
                              ↓              ↓              ↓
                              └──────────────┼──────────────┘
                                             ↓
                                      30-Day Timeline
                                             ↓
                                     Launch Kit Dashboard
```

---

## Data Flow

1. User enters idea description via `/launch <idea-description>` or web dashboard form.
2. Signal Scanner validates the idea: queries Reddit, X, TikTok for demand signals and competitive density.
3. Market Report is generated: Signal Score, user quotes, target persona, competitive positioning, pricing benchmarks.
4. Landing Page Factory receives Market Report and generates a complete Next.js landing page project.
5. Landing page is deployed to Vercel, returning a live URL.
6. Ad Launch Playbook receives Market Report and generates campaigns for Meta, Google, and X with targeting, creative briefs, and budget allocations.
7. Unit Economics Calculator receives Market Report and Ad data, projects MRR, CAC, LTV, churn, break-even month.
8. 30-Day Timeline Generator receives all outputs and produces a week-by-week action plan.
9. Launch Kit Dashboard assembles all resources: live URL, ad configs, financial projections, timeline.
10. User reviews Launch Kit, makes adjustments to any module, and re-runs affected downstream modules.

---

## Skill API Mapping

| Feature Step | Skill API / Command | Parameters |
|---|---|---|
| Idea Validation | `/scan <idea>` | idea_text, vertical, depth |
| Market Report | `/validate <idea>` | idea_text, competitive_set |
| Landing Page | `/landing-page-factory` | app_name, pain_point, persona, features |
| Deployment | Vercel CLI | project_path, env_vars |
| Ad Playbook | `/ad-launch <vertical>` | vertical, budget, platforms |
| Unit Economics | `/break-even` | price, cac, churn_rate, mrr_target |
| Niche Validation | `/niche-validator` | niche, competitive_density, demand_score |
| Timeline | `/timeline <idea>` | idea, launch_date, milestones |

---

## Tech Stack

- **Frontend**: Next.js 16, TypeScript, Tailwind CSS 4, shadcn/ui (Launch Kit Dashboard)
- **AI/Generation**: z.ai GLM API for landing page generation, ad copy, and financial narrative
- **Signal Processing**: last30days skill (signal scanner, landing page factory, ad launch playbook, unit economics, niche validator)
- **Payments**: Stripe API for checkout integration and subscription management
- **Deployment**: Vercel CLI for automated landing page deployment
- **Ad Platforms**: Meta Marketing API, Google Ads API, X Ads API (via ad launch playbook)
- **Database**: Prisma ORM with PostgreSQL for project persistence and economics data
- **Scheduling**: node-cron for timeline milestone reminders
- **Hosting**: Vercel (dashboard) + Railway (orchestrator worker)

---

## Implementation Steps

| Step | Task | Time Estimate |
|---|---|---|
| 1 | Set up Next.js project with Launch Kit Dashboard layout | 1 hour |
| 2 | Build idea input form with Signal Scanner integration | 1 hour |
| 3 | Implement Market Report generation and display | 1 hour |
| 4 | Build Landing Page Factory module with GLM integration | 2 hours |
| 5 | Implement Vercel deployment pipeline | 1 hour |
| 6 | Build Ad Launch Playbook generator with platform-specific configs | 1.5 hours |
| 7 | Integrate Unit Economics Calculator (break_even + niche_validator) | 1.5 hours |
| 8 | Build 30-Day Timeline Generator with milestone tracking | 1 hour |
| 9 | Assemble Launch Kit Dashboard with all module outputs | 1.5 hours |
| 10 | Add iterative refinement flow (re-run individual modules) | 1 hour |
| 11 | Polish UI, error handling, demo data, and end-to-end testing | 1 hour |

**Total estimated time: ~13 hours**

---

## Demo Script (3-Minute Walkthrough)

**Minute 0:00-0:40 — Idea Input & Validation**
Open the Micro-SaaS Launch Pad. Show the single input field: "Describe your micro-SaaS idea." Type: "An API uptime monitor that sends Slack alerts for small dev teams." Click "Launch." The Signal Scanner runs — show the progress. Results appear: Signal Score 8.2, 447 mentions of API monitoring pain points, low competitive density for small-team segment, user quotes from Reddit and X.

**Minute 0:40-1:40 — Landing Page & Deployment**
The Landing Page Factory kicks in. A preview of the generated landing page appears: hero section with the pain point quote, feature grid, pricing tiers ($9/mo, $29/mo, $79/mo), and CTA. Click "Deploy" — the page goes live on Vercel. Show the live URL opening in a new tab with a fully functional, professional landing page.

**Minute 1:40-2:30 — Ad Playbook & Unit Economics**
Switch to the Ad Launch Playbook tab. Three campaign cards appear: Meta ($500 budget, targeting dev team leads), Google Ads ($300 budget, search campaigns for "API monitoring"), X Ads ($200 budget, promoted tweets to dev community). Switch to Unit Economics: MRR projection hits $5K by month 6, CAC of $45, LTV of $540, break-even at month 4. Show the visual break-even chart.

**Minute 2:30-3:00 — 30-Day Timeline & Launch Kit**
Open the 30-Day Timeline: Week 1 (Build MVP + Ship landing page), Week 2 (Launch ads + First 10 users), Week 3 (Iterate on feedback), Week 4 (Optimize unit economics + Scale). Switch to the Launch Kit view — all resources in one place: live URL, ad configs, financial projections, timeline, and a "Share Kit" button. End by emphasizing: "From idea to complete launch kit in under 10 minutes — not 10 weeks."
