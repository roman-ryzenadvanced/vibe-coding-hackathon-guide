# Features

Complete feature documentation for the **Vibe Coding Builders Hackathon Ideas Guide**, a Z.ai + rommark.dev partnered project. Each of the 10 ideas maps to specific capabilities of the last30days-skill.

## Feature Overview

| # | Feature | Skill Module | Difficulty | Time to Build |
|---|---------|-------------|-----------|---------------|
| 1 | Trend-to-App Builder | Signal Scanner | Beginner | 1-2 days |
| 2 | Competitor Intelligence Dashboard | Comparison Mode | Intermediate | 2-3 days |
| 3 | Developer Pulse Newsletter | Briefing Engine | Beginner | 1 day |
| 4 | Niche Discovery Bot | Interactive Gate + Full Workflow | Advanced | 3-5 days |
| 5 | Micro-SaaS Launch Pad | Landing Page Factory + Unit Economics | Intermediate | 2-3 days |
| 6 | Social Signal Validator | Quick Scan Mode | Beginner | 1 day |
| 7 | Pivot Predictor | Failure/Pivot Protocol | Advanced | 3-5 days |
| 8 | Provider Marketplace Finder | Data Recon + Provider Sourcing | Intermediate | 2-3 days |
| 9 | AI Research Agent | Agent Mode + Entity Resolution | Advanced | 3-5 days |
| 10 | Vibe Coder Revenue Calculator | break_even.py + niche_validator.py | Intermediate | 2-3 days |

## How Features Connect to the Skill

```
last30days-skill (v3.3.2)
├── Research Engine
│   ├── Signal Scanner ──────── Ideas 1, 6
│   ├── Comparison Mode ─────── Idea 2
│   ├── Briefing Engine ─────── Idea 3
│   ├── Agent Mode ──────────── Idea 9
│   ├── Entity Resolution ───── Idea 9
│   └── HTML Briefs ─────────── Ideas 3, 9
│
└── Business Launch System
    ├── Interactive Gate ─────── Idea 4
    ├── Landing Page Factory ── Idea 5
    ├── Unit Economics ──────── Idea 10
    ├── Quick Scan ──────────── Idea 6
    ├── Failure/Pivot ───────── Idea 7
    ├── Data Reconnaissance ─── Idea 8
    ├── Provider Sourcing ───── Idea 8
    └── 30-Day Timeline ─────── Ideas 4, 5
```

## Quick Start by Goal

| I want to... | Start with... | Then read... |
|--------------|---------------|-------------|
| Build a simple project this weekend | Idea 6 (Signal Validator) | `features/idea-06-signal-validator.md` |
| Win the hackathon | Idea 1 (Trend-to-App) | `features/idea-01-trend-to-app.md` |
| Build a real product after the hackathon | Idea 5 (Micro-SaaS Launch Pad) | `features/idea-05-micro-saas-launchpad.md` |
| Create an AI agent | Idea 9 (Research Agent) | `features/idea-09-research-agent.md` |
| Help indie hackers find niches | Idea 4 (Niche Discovery Bot) | `features/idea-04-niche-discovery-bot.md` |
| Just explore ideas fast | Idea 6 (Signal Validator) | `docs/how-to-use-30d-skill.md` |

## Skill Feature Mapping

### Research Engine Features Used

| Skill Feature | Ideas Using It | What It Provides |
|---------------|---------------|-----------------|
| Multi-source parallel search | 1, 2, 3, 6, 9 | 16+ platform search at once |
| Cross-source cluster merging | 2, 9 | Same story merged across platforms |
| Comparison mode | 2 | Head-to-head A/B/C tables |
| Competitor auto-discovery | 2, 6 | `--competitors` flag finds top peers |
| GitHub person/project mode | 3, 9 | PR velocity, stars, release notes |
| Shareable HTML briefs | 3, 9 | `--emit=html` for Slack/email |
| Best Takes scoring | 1, 6 | Virality/humor scoring on quotes |
| Query quality pre-flight | 6, 9 | Detects keyword-trap topics |
| Category-peer expansion | 1, 6 | Auto-expands to cross-product communities |
| ELI5 mode | 6 | Plain-language synthesis |
| Watchlist & briefings | 2, 3 | `--store`, `watchlist.py`, `briefing.py` |
| Agent mode | 9 | Non-interactive autonomous research |

### Business Launch Features Used

| Skill Feature | Ideas Using It | What It Provides |
|---------------|---------------|-----------------|
| Signal Scanner | 1, 4, 5, 6 | Scores topics by engagement (0-10) |
| Interactive Gate | 4 | AI waits for YOUR decision |
| Unit Economics Calculator | 5, 10 | Break-even, margin, runway |
| Provider Sourcing | 8 | 4-phase vetting system |
| Landing Page Factory | 5 | Mobile-first HTML landing pages |
| Local Channel Mapper | 8 | Geo-specific Reddit/FB/classifieds |
| Regulatory Check | 5, 8 | Compliance checklist |
| Ad Launch Playbook | 5 | Keywords, targeting, budget rules |
| 30-Day Timeline System | 4, 5 | Day-by-day launch checklist |
| Prompt Variants | 6 | 5 modes: Quick Scan, Deep Dive, Pivot, Scale, Workshop |
| Failure/Pivot Protocol | 7 | 6 failure modes with detection triggers |
| Data Reconnaissance | 8 | Build real market map before vetting |

## No-API-Key Features

These ideas work with **zero API keys** using the skill's free-tier capabilities:

| Idea | Free Sources | No API Key Needed |
|------|-------------|------------------|
| 1 | Reddit + HN + Polymarket + GitHub | Yes |
| 3 | Hacker News + GitHub | Yes |
| 5 | All business features | Yes |
| 6 | Reddit + HN (quick scan) | Yes |
| 7 | Business logic only | Yes |
| 8 | Reddit + local channels | Yes |
| 10 | Python stdlib scripts | Yes |
