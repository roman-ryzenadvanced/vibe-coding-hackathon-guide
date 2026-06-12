# How to Find Hackathon Ideas Using Real Data — A last30days Skill Tutorial

[![Get 10% OFF on Z.ai Coding Plans](https://img.shields.io/badge/Get_10%25_OFF-Z.ai_Coding_Plans-FF6B35?style=for-the-badge)](https://z.ai/subscribe?ic=ROK78RJKNW)

> **Stop guessing what to build.** This tutorial teaches you how to use the [last30days-skill](https://github.com/roman-ryzenadvanced/last30days-skill) to research any topic with real engagement data from 16+ platforms — and find validated hackathon ideas people actually want.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Z.ai Partner](https://img.shields.io/badge/Partner-Z.ai-6C5CE7)](https://z.ai)
[![rommark.dev](https://img.shields.io/badge/Partner-rommark.dev-FF6B35)](https://rommark.dev)

---

## The Problem Every Hacker Faces

You walk into a hackathon. You have 48 hours. You need an idea. So you brainstorm, pick something that sounds cool, and start coding. Sunday comes — you demo something shiny but the judges ask: *"Who actually needs this?"*

You don't have an answer. Because you guessed.

**There's a better way.** Use real data from real people to find out what they're actually complaining about, asking for, and wishing existed — *before* you write a single line of code.

That's what this tutorial teaches.

---

## What You'll Learn

By the end of this tutorial you will be able to:

1. **Install and use** the last30days research skill on chat.z.ai
2. **Scan any topic** across 16+ platforms (Reddit, X, YouTube, TikTok, Hacker News, GitHub, and more) in seconds
3. **Score ideas** with engagement-weighted Signal Scores — not opinions, but data
4. **Compare tools, frameworks, or competitors** head-to-head with real user sentiment
5. **Validate your hackathon idea** in under 60 seconds
6. **Generate a complete research brief** you can show judges
7. **Apply the same method** to research literally anything — not just hackathons

---

## Quick Start: 3 Commands to Your First Validated Idea

```bash
# Step 1: Install the skill
npx skills add roman-ryzenadvanced/last30days-skill -g

# Step 2: Open chat.z.ai and run your first research
/last30days vibe coding tools

# Step 3: Compare alternatives
/last30days Cursor vs Windsurf vs Bolt
```

That's it. You just pulled real engagement data from Reddit, X, YouTube, Hacker News, and 12+ other platforms. The skill scored every result by upvotes, likes, views, and real money odds — not SEO rankings.

---

## Tutorial: Step-by-Step

### Step 1: Install the Skill

The last30days skill works with any AI agent host — Claude Code, Codex, Cursor, Copilot, Gemini CLI, or directly on chat.z.ai.

```bash
# Install for any agent host
npx skills add roman-ryzenadvanced/last30days-skill -g

# Or install for Claude Code specifically
npx skills add roman-ryzenadvanced/last30days-skill -g -a claude-code

# Or clone standalone
git clone https://github.com/roman-ryzenadvanced/last30days-skill.git
```

No API keys required to start. Reddit, Hacker News, Polymarket, and GitHub work immediately for free. Unlock more sources (X, YouTube, TikTok, Instagram) with optional keys — see [CONFIGURATION.md](https://github.com/roman-ryzenadvanced/last30days-skill/blob/main/CONFIGURATION.md).

### Step 2: Research Any Topic

Open chat.z.ai and type:

```
/last30days AI code editors
```

The skill will:
1. **Resolve who matters** — find the right subreddits, X handles, YouTube channels, and TikTok hashtags
2. **Search all sources in parallel** — Reddit + X + YouTube + TikTok + Hacker News + GitHub + more, all at once
3. **Score by real engagement** — upvotes, likes, views, and real money odds (Polymarket), not keyword matches
4. **Merge cross-source clusters** — the same story on Reddit, X, and YouTube becomes one item, not three
5. **Return a ranked brief** — evidence clusters sorted by signal strength

**Try it with any topic:**

```
/last30days nvidia earnings reaction
/last30days freelance designer pain points
/last30days Rust adoption in 2026
```

### Step 3: Validate Your Hackathon Idea

Got an idea? Test it in 60 seconds:

```
/last30days "AI code review tools" --emit=compact
```

Look at the output. Are people actively complaining about the problem you're solving? Are there upvoted Reddit threads, viral TikToks, or trending HN posts about it? If the engagement signals are strong, you've got a validated idea. If not — kill it and try another one.

**The fastest way to scan for opportunities:**

```
/last30days "developer pain points" --competitors --emit=compact
```

The `--competitors` flag auto-discovers the top 2 competitors and runs a 3-way comparison. You see the whole landscape in one command.

### Step 4: Compare Alternatives Head-to-Head

Not sure which tool or framework to use? Or want to find gaps in existing products?

```
/last30days Cursor vs Windsurf vs Bolt
```

This returns a structured comparison table with per-entity resolution, parallel pipeline, and head-to-head scoring. You'll see exactly where each tool is strong and where users are frustrated — those frustrations are your hackathon opportunity.

### Step 5: Generate a Shareable Research Brief

When you need to show your research to teammates or judges:

```
/last30days "your topic" --emit=html
```

This generates a self-contained dark-mode HTML file you can share in Slack, email, or Notion. It includes all citations, engagement metrics, and evidence clusters. Judges love data-backed decisions.

### Step 6: Use Agent Mode for Deep Research

For complex questions that need multi-step investigation:

```
/last30days "emerging trends in AI-powered developer tools" --agent
```

Agent mode runs autonomously: it decomposes your question, searches all sources, resolves entities, merges clusters, evaluates coverage, and produces a comprehensive brief — without you pressing enter again.

#### Using Agent Mode on chat.z.ai (The Easy Way)

You don't need to install anything locally to use Agent mode. **chat.z.ai** has the skill built in. Just tell the Z.ai agent to use it with the "Please use this skill" pattern:

```
Please use this skill https://github.com/roman-ryzenadvanced/last30days-skill to find hackathon ideas about AI developer tools
```

That's it. The Z.ai agent will:
1. **Load the skill** automatically from the GitHub URL
2. **Run Agent mode** autonomously — decompose, search, resolve, merge, score
3. **Return a complete research report** with Key Findings, synthesis, and stats

**More Agent mode prompts for chat.z.ai:**

```
Please use this skill https://github.com/roman-ryzenadvanced/last30days-skill to compare Cursor vs Windsurf vs Bolt for hackathon builders
```

```
Please use this skill https://github.com/roman-ryzenadvanced/last30days-skill to validate if there is real demand for an AI code review tool with fewer false positives
```

```
Please use this skill https://github.com/roman-ryzenadvanced/last30days-skill to research what indie hackers are struggling with in 2026 and find hackathon-worthy problems
```

```
Please use this skill https://github.com/roman-ryzenadvanced/last30days-skill to find trending developer pain points on Reddit and Hacker News that could become hackathon projects
```

#### How the "Please use this skill" Pattern Works

| Step | What Happens | You See |
|------|-------------|---------|
| **1** | You paste the prompt into chat.z.ai | Your message in the chat |
| **2** | Z.ai agent loads the skill from the GitHub URL | Agent starts working |
| **3** | Agent mode runs autonomously — no follow-up needed | Progress indicators |
| **4** | Agent decomposes your question into sub-queries | Entity resolution |
| **5** | Searches all 16+ sources in parallel | Source scanning |
| **6** | Merges cross-source clusters, scores by engagement | Cluster merging |
| **7** | Returns complete research report | **Key Findings + What I learned + Stats** |

**Pro tip:** The more specific your prompt, the better the research. Instead of "find ideas about AI," say "find hackathon ideas about AI tools that solve developer pain points with code review." Specificity = better entity resolution = higher signal.

### Step 7: Explore 5 Prompt Modes

The skill ships with 5 specialized prompt variants for different situations:

| Mode | Template | When to Use |
|------|----------|-------------|
| **Quick Scan** | `templates/quick-scan.txt` | Top 5 opportunities in 5 minutes |
| **Deep Dive** | `templates/deep-dive.txt` | Full analysis of one niche |
| **Pivot** | `templates/pivot.txt` | Diagnose and fix a failing idea |
| **Scale** | `templates/scale.txt` | Growth path for a working idea |
| **Workshop** | `templates/workshop.txt` | 20-minute teaching script |

---

## Real Example: Finding a Hackathon Idea

Let's walk through the exact process from blank page to validated idea.

### Friday 6 PM — You Have No Idea

```
/last30days "what developers struggle with in 2026" --emit=compact
```

**What you get back:** A ranked list of trending pain points across Reddit, X, Hacker News, and GitHub. Each item has an engagement score, source citations, and user quotes. You see that "AI code review is unreliable" has 8.2/10 signal strength with 3 trending Reddit threads and 2 viral X posts.

### Friday 7 PM — Validate the Top Idea

```
/last30days "AI code review tools" --competitors --emit=compact
```

**What you get back:** A 3-way comparison of the top AI code review tools. You see that users love the speed but hate the false positives. That's your gap — "AI code review with fewer false positives."

### Friday 8 PM — Check the Competitive Landscape

```
/last30days "CodeRabbit vs Codacy vs SonarQube AI"
```

**What you get back:** Head-to-head comparison with real user sentiment. You see that CodeRabbit has the most positive sentiment but users complain about language support. Your hackathon project: "AI code review with better multi-language support."

### Friday 9 PM — Generate the Research Brief

```
/last30days "AI code review" --emit=html
```

**What you get back:** A shareable HTML brief with all your research. You now have data-backed evidence that your idea solves a real problem. Print it. Pin it. Show it to judges on Sunday.

---

## The Same Method Works for Everything

This tutorial uses hackathons as the example, but the method is universal. Use the last30days skill to research:

| Use Case | Command |
|----------|---------|
| **Market research** | `/last30days "fintech for Gen Z"` |
| **Product validation** | `/last30days "time tracking for freelancers"` |
| **Competitive analysis** | `/last30days "Notion vs Obsidian vs Roam"` |
| **Trend spotting** | `/last30days "Rust adoption trends"` |
| **Investment research** | `/last30days "nvidia earnings reaction"` |
| **Job market analysis** | `/last30days "AI engineer hiring trends 2026"` |
| **Community research** | `/last30days "expat life in Batumi"` |
| **Academic research** | `/last30days "LLM hallucination mitigation"` |

Any topic. Any question. The same pipeline: resolve entities, search 16+ sources in parallel, score by engagement, merge clusters, return a ranked brief.

---

## 16+ Data Sources at Your Fingertips

| Source | What You Get | Auth Needed |
|--------|-------------|-------------|
| **Reddit** | Top comments with upvote counts | None — free |
| **X / Twitter** | Hot takes, expert threads, breaking reactions | Cookies or xAI API |
| **YouTube** | Full transcripts, top comments with likes | yt-dlp (free) |
| **TikTok** | Viral engagement — views, likes, captions | ScrapeCreators API |
| **Instagram Reels** | Influencer transcripts | ScrapeCreators API |
| **Hacker News** | Developer consensus via Algolia | None — free |
| **Polymarket** | Real-money odds, not opinions | None — free |
| **GitHub** | Stars, PRs, release velocity, READMEs | None — free |
| **Bluesky** | Decentralized social via AT Protocol | App password |
| **Truth Social** | Political/social signal | Auth token |
| **Threads** | Creator and brand conversations | ScrapeCreators API |
| **Pinterest** | Visual discovery, saves, comments | ScrapeCreators API |
| **Digg** | Curated AI story clusters | digg-pp-cli (free) |
| **Perplexity** | Grounded web search with citations | OpenRouter API |
| **Xiaohongshu** | Chinese social commerce | ScrapeCreators API |
| **Web** | Editorial, blogs, tutorials | Brave API (2K free/mo) |

---

## 10 Hackathon Ideas Found With This Method

These are real project ideas you can build using the skill. Each was found by scanning engagement signals across multiple platforms.

| # | Project | Difficulty | Core Skill Feature | Deep Dive |
|---|---------|-----------|-------------------|-----------|
| 01 | **Trend-to-App Builder** | Beginner | Signal Scanner | [idea-01-trend-to-app.md](features/idea-01-trend-to-app.md) |
| 02 | **Competitor Intelligence Dashboard** | Intermediate | Comparison Mode | [idea-02-competitor-dashboard.md](features/idea-02-competitor-dashboard.md) |
| 03 | **Developer Pulse Newsletter** | Beginner | Briefing Engine | [idea-03-dev-pulse.md](features/idea-03-dev-pulse.md) |
| 04 | **Niche Discovery Bot** | Advanced | Interactive Gate | [idea-04-niche-discovery-bot.md](features/idea-04-niche-discovery-bot.md) |
| 05 | **Micro-SaaS Launch Pad** | Intermediate | Landing Page Factory | [idea-05-micro-saas-launchpad.md](features/idea-05-micro-saas-launchpad.md) |
| 06 | **Social Signal Validator** | Beginner | Quick Scan | [idea-06-signal-validator.md](features/idea-06-signal-validator.md) |
| 07 | **Pivot Predictor** | Advanced | Failure/Pivot Protocol | [idea-07-pivot-predictor.md](features/idea-07-pivot-predictor.md) |
| 08 | **Provider Marketplace Finder** | Intermediate | Data Reconnaissance | [idea-08-provider-marketplace.md](features/idea-08-provider-marketplace.md) |
| 09 | **AI Research Agent** | Advanced | Agent Mode | [idea-09-research-agent.md](features/idea-09-research-agent.md) |
| 10 | **Vibe Coder Revenue Calculator** | Intermediate | Unit Economics | [idea-10-revenue-calculator.md](features/idea-10-revenue-calculator.md) |

---

## Hackathon Weekend Workflow

For the full Friday-to-Sunday breakdown with exact commands and expected outputs, see [docs/hackathon-workflow.md](docs/hackathon-workflow.md).

**TL;DR:**

| Time | What | Command |
|------|------|---------|
| **Friday 6 PM** | Scan for trending pain points | `/last30days "developer pain points" --emit=compact` *or* `Please use this skill https://github.com/roman-ryzenadvanced/last30days-skill to find trending developer pain points` on chat.z.ai |
| **Friday 7 PM** | Validate top 2 ideas | `/last30days "your idea" --competitors` |
| **Friday 9 PM** | Check economics | `python3 scripts/break_even.py --avg-job 25 --profit 10` |
| **Saturday** | Build, check watchlist every 2h | `watchlist.py scan` |
| **Sunday AM** | Generate research brief for judges | `/last30days "your topic" --emit=html` *or* `Please use this skill https://github.com/roman-ryzenadvanced/last30days-skill to research your topic and generate a brief` on chat.z.ai |
| **Sunday PM** | Present with data backing | Show Signal Scores + HTML brief |

---

## Complete Command Reference

For all flags, modes, and commands with examples, see [docs/skill-commands-reference.md](docs/skill-commands-reference.md).

**Most-used commands cheat sheet:**

```bash
# Basic research
/last30days "topic here"

# Compact output (fast)
/last30days "topic" --emit=compact

# Full HTML brief (shareable)
/last30days "topic" --emit=html

# Compare 3+ entities
/last30days "A vs B vs C"

# Auto-discover competitors
/last30days "topic" --competitors

# Agent mode (autonomous deep research)
/last30days "topic" --agent

# Plain-language mode
/last30days "topic" --eli5
```

---

## Repository Structure

```
vibe-coding-hackathon-guide/
├── README.md                          # This tutorial
├── CHANGELOG.md                       # Version history
├── LICENSE                            # MIT License
├── FEATURES.md                        # Feature-to-skill mapping
├── CONTRIBUTING.md                    # Contribution guidelines
│
├── guide.html                         # Branded web guide
├── cover.html                         # Cover page (standalone)
├── hackathon-ideas-guide.pdf          # Full branded PDF guide
│
├── docs/                              # Deep-dive documentation
│   ├── how-to-use-30d-skill.md        # Detailed skill usage tutorial
│   ├── hackathon-workflow.md          # Friday-Sunday weekend workflow
│   └── skill-commands-reference.md    # Complete command reference
│
├── features/                          # 10 idea deep-dives
│   ├── idea-01-trend-to-app.md
│   ├── idea-02-competitor-dashboard.md
│   ├── idea-03-dev-pulse.md
│   ├── idea-04-niche-discovery-bot.md
│   ├── idea-05-micro-saas-launchpad.md
│   ├── idea-06-signal-validator.md
│   ├── idea-07-pivot-predictor.md
│   ├── idea-08-provider-marketplace.md
│   ├── idea-09-research-agent.md
│   └── idea-10-revenue-calculator.md
│
├── tests/                             # 279 passing tests
├── scripts/                           # Build scripts
└── releases/                          # Release notes
```

---

## Key Links

| Resource | URL |
|----------|-----|
| last30days-skill | [github.com/roman-ryzenadvanced/last30days-skill](https://github.com/roman-ryzenadvanced/last30days-skill) |
| Z.ai Chat | [chat.z.ai](https://chat.z.ai) |
| Z.ai Coding Plans | [z.ai/subscribe?ic=ROK78RJKNW](https://z.ai/subscribe?ic=ROK78RJKNW) |
| rommark.dev | [rommark.dev](https://rommark.dev) |

---

## Acknowledgments

- **last30days-skill** by [@mvanhorn](https://github.com/mvanhorn) with v3 architecture by [@j-sperling](https://github.com/j-sperling)
- **Business launch system** original concept by Roman (z.ai GLM Workshop)
- **Z.ai** — AI-powered coding platform
- **rommark.dev** — Hackathon partner and community builder

---

## License

MIT License — see [LICENSE](LICENSE) file.
