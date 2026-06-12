# How to Use the last30days Skill to Research Anything

This is the complete tutorial for using the [last30days-skill](https://github.com/roman-ryzenadvanced/last30days-skill) to research any topic with real engagement data. Whether you're preparing for a hackathon, validating a business idea, doing market research, or just curious about what people think — this guide teaches you the method.

---

## The Core Idea: Engagement Score > Search Ranking

Traditional search gives you what's SEO-optimized. The last30days skill gives you what people actually care about — measured by upvotes, likes, views, real money odds, and comment depth across 16+ platforms.

**This is social relevancy, not SEO relevancy.**

When you research "AI code editors," you don't get marketing pages from the tool makers. You get Reddit threads where developers argue about which one actually saves time. You get TikTok videos going viral about the one feature that changed someone's workflow. You get Hacker News threads with 400 upvotes dissecting the pros and cons. That's signal. Everything else is noise.

---

## Step 1: Install the Skill

### Option A: As an AI Skill (Recommended)

This is the easiest way. The skill works with every major AI agent host.

```bash
# Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and 50+ others
npx skills add roman-ryzenadvanced/last30days-skill -g

# Claude Code specifically
npx skills add roman-ryzenadvanced/last30days-skill -g -a claude-code
```

After installation, the skill is available as `/last30days` in your agent. Open chat.z.ai and start researching.

### Option B: Standalone (Just the Research Engine)

If you don't use an AI agent host, you can run the engine directly:

```bash
git clone https://github.com/roman-ryzenadvanced/last30days-skill.git
cd last30days-skill

# Run your first research
python3 scripts/last30days.py "your topic" --emit=compact
```

Requires Python 3.12+ and Node.js (for X/Twitter search).

### No API Keys Needed to Start

Reddit, Hacker News, Polymarket, and GitHub work immediately with zero configuration. Unlock more sources with optional keys:

| Sources | What You Need | Cost |
|---------|---------------|------|
| Reddit + HN + Polymarket + GitHub | Nothing | Free |
| X / Twitter | Browser cookies or xAI API key | Free |
| YouTube | `brew install yt-dlp` | Free |
| Bluesky | App password from bsky.app | Free |
| TikTok + Instagram + Threads + Pinterest | ScrapeCreators API key | 100 free credits |
| Perplexity Sonar | OpenRouter API key | Pay as you go |
| Web search (Brave) | Brave Search API key | 2,000 free queries/month |

See [CONFIGURATION.md](https://github.com/roman-ryzenadvanced/last30days-skill/blob/main/CONFIGURATION.md) for the full setup guide.

---

## Step 2: Your First Research Query

Open chat.z.ai and type:

```
/last30days AI code editors
```

**What happens behind the scenes:**

1. **Entity Resolution** — The skill figures out who matters for "AI code editors." It finds r/cursor, r/ChatGPTCoding, @cursor_ai on X, the right YouTube channels, and relevant TikTok hashtags. Product-to-community, person-to-company, name-to-GitHub-profile — all resolved automatically before a single API call fires.

2. **Parallel Source Search** — All 16+ sources are searched simultaneously. Reddit, X, YouTube, TikTok, Instagram, Hacker News, Polymarket, GitHub, Bluesky, Truth Social, Threads, Pinterest, Digg, Perplexity, and the web — all at once.

3. **Engagement Scoring** — Every result is scored by real engagement metrics: upvotes on Reddit, likes on X, views on TikTok, real money odds on Polymarket, stars on GitHub. Not keyword matches. Real human signals.

4. **Cross-Source Cluster Merging** — The same story appearing on Reddit, X, and YouTube is merged into one cluster, not three separate items. You see the story once, with all its evidence attached.

5. **Ranked Brief** — You get a synthesized brief with evidence clusters sorted by signal strength, inline citations, and a badge line showing the engine version and source count.

**Try it now with your own topic:**

```
/last30days nvidia earnings reaction
/last30days freelance designer pain points
/last30days Rust vs Go performance 2026
/last30days best neighborhoods in Tbilisi for expats
```

---

## Step 3: Output Modes

The skill supports multiple output formats depending on your needs:

### Compact Mode (Fast, Scannable)

```
/last30days "your topic" --emit=compact
```

Best for: Quick scans, initial exploration, comparing multiple topics fast. Shows ranked results with key metrics, stripped of narrative fluff.

### HTML Brief (Shareable, Beautiful)

```
/last30days "your topic" --emit=html
```

Best for: Sharing with teammates, presenting to judges, sending in Slack/email. Generates a self-contained dark-mode HTML file with all citations, engagement metrics, and evidence. Print it, share it, embed it.

### Standard Mode (Default)

```
/last30days "your topic"
```

Best for: Deep reading. Full narrative synthesis with inline citations, evidence clusters, and "Best Takes" (the wittiest community quotes scored by humor/virality).

---

## Step 4: Comparison Mode

One of the most powerful features. Compare any entities head-to-head:

```
/last30days Cursor vs Windsurf vs Bolt
```

This runs a separate pipeline for each entity:
- **Per-entity resolution** — Finds the right communities, handles, and channels for each
- **Parallel research** — All entities researched simultaneously
- **Head-to-head table** — Structured comparison with per-entity scoring
- **Gap identification** — Where are users frustrated? Those gaps are your opportunities

### Auto-Discover Competitors

Don't know who the competitors are? Let the skill find them:

```
/last30days "AI code editors" --competitors
```

The `--competitors` flag uses WebSearch to auto-discover the top 2 peers, then runs a full 3-way comparison. You see the whole landscape in one command.

**Use this for:** Competitive analysis, tool selection, market positioning, and finding gaps in existing products that your hackathon project can fill.

---

## Step 5: Validating a Hackathon Idea

Got an idea? Here's how to validate it with data in 60 seconds:

```
/last30days "AI code review tools" --emit=compact
```

Look at the output and ask yourself:

1. **Are people actively discussing this problem?** Check the source count and engagement metrics.
2. **Is there emotional urgency?** Look for words like "frustrating," "desperate," "wish there was." The skill surfaces these from comment sentiment.
3. **Is the problem recurring?** Cross-source repetition (same complaint on Reddit, X, and HN) = high signal.
4. **Are there gaps in existing solutions?** Comparison mode reveals where users are unhappy with current options.

**Decision rule:** If Signal Score >= 7/10 across 3+ sources, you have a validated idea. Build it. If Score < 5/10, kill it and try another. The 30 minutes you spend validating saves 10 hours of wasted building.

---

## Step 6: Agent Mode for Deep Research

For complex questions that need multi-step investigation:

```
/last30days "emerging trends in AI-powered developer tools" --agent
```

Agent mode runs autonomously through this workflow:
1. **Decompose** your question into sub-questions
2. **Search** all sources for each sub-question
3. **Resolve** entities (people, products, companies)
4. **Merge** cross-source clusters
5. **Evaluate** coverage — if insufficient, loop back
6. **Synthesize** into a comprehensive narrative
7. **Generate** HTML brief with full citations

You can step away and come back to a complete research report. Perfect for pre-hackathon preparation.

---

## Step 7: Watchlist for Ongoing Monitoring

If you want to track a topic over time (like monitoring competitor moves during a hackathon weekend):

```bash
# Add entities to watchlist
python3 scripts/last30days.py "your topic" --store

# Check for changes
python3 scripts/watchlist.py scan

# Generate a digest
python3 scripts/briefing.py --frequency daily
```

The watchlist persists to SQLite, monitors for changes, and can deliver digests to Slack. Set it up before your hackathon and you'll catch competitor moves in real-time.

---

## Step 8: Business Launch Tools

The skill includes a complete business launch system that takes you from validated idea to launched product. All tools work without API keys:

| Tool | Command | What It Does |
|------|---------|-------------|
| **Break-even Calculator** | `python3 scripts/break_even.py --avg-job 25 --profit 10` | Calculate break-even volume, margin, runway |
| **Niche Validator** | `python3 scripts/niche_validator.py --niche "Airbnb cleaning"` | Score niche viability on 12 criteria |
| **Signal Score Helper** | `python3 scripts/signal_score.py` | Engagement scoring reference and demo |
| **Landing Page Factory** | Use `templates/landing-page.html` | Mobile-first HTML template with dark theme |
| **30-Day Timeline** | Use `templates/30-day-calendar.md` | Day-by-day launch checklist |

These tools pair perfectly with the research engine: use signals to find your idea, then use the business tools to plan your launch.

---

## Prompt Variants: 5 Modes for Different Situations

The skill ships with 5 ready-to-use prompt templates in the `templates/` directory:

| Mode | Template | When to Use | Time |
|------|----------|-------------|------|
| **Quick Scan** | `templates/quick-scan.txt` | Top 5 opportunities, fast overview | 5 min |
| **Deep Dive** | `templates/deep-dive.txt` | Full analysis of one niche | 20 min |
| **Pivot** | `templates/pivot.txt` | Diagnose and fix a failing idea | 15 min |
| **Scale** | `templates/scale.txt` | Growth path for a working idea | 20 min |
| **Workshop** | `templates/workshop.txt` | 20-minute teaching script | 20 min |

**For hackathons**, start with Quick Scan to find ideas fast, then switch to Deep Dive on your top choice.

---

## ELI5 Mode

Need to explain your research to non-technical teammates or stakeholders? Add `--eli5` to any command:

```
/last30days "Kubernetes trends" --eli5
```

The skill returns the same data, same sources, just in plain language with contextual explanations. No jargon. Perfect for sharing with judges who aren't deeply technical.

---

## Troubleshooting

**"No signals found"**: Your query may be too narrow. Try broadening the topic or using more common terminology. Instead of "GPT-4 fine-tuning for medical imaging," try "AI model customization in healthcare."

**Slow responses**: Deep scans can take 30-60 seconds. Use `--emit=compact` for faster results. Agent mode can take 5-10 minutes for complex questions — that's normal for autonomous multi-step research.

**Entity resolution errors**: If the skill merges or splits entities incorrectly, use more specific names. "Apple (company)" instead of just "Apple" avoids confusion with the fruit.

**Missing sources**: Some sources require API keys. Check [CONFIGURATION.md](https://github.com/roman-ryzenadvanced/last30days-skill/blob/main/CONFIGURATION.md) for the full key matrix. Reddit, HN, Polymarket, and GitHub always work for free.

---

## The Method, Summarized

1. **Research first, build second** — Use `/last30days` to scan any topic before you commit
2. **Score by engagement** — Signal Scores (0-10) based on real human behavior
3. **Compare alternatives** — `A vs B vs C` reveals gaps and opportunities
4. **Validate fast** — 60 seconds to know if your idea has real demand
5. **Share your research** — `--emit=html` generates judge-ready briefs
6. **Monitor continuously** — Watchlist catches changes while you build
7. **Apply to anything** — Not just hackathons. Any topic. Any question.

**The interactive gate is sacred.** The skill presents data and waits for YOUR decision. You choose the niche. You choose what to build. The AI executes, you decide.
