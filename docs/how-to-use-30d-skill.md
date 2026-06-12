# How to Use the last30days Skill on chat.z.ai

## Installation & Access

The last30days skill is available directly on chat.z.ai — no installation required. Simply navigate to chat.z.ai and start a new conversation. The skill is pre-loaded and accessible through natural language prompts or explicit command syntax. If you're using the skill for the first time, type `hello` or `what can you do?` to see a quick overview of capabilities. The skill runs entirely within the chat interface, so there's nothing to download, configure, or deploy on your end.

## Basic Commands

The skill responds to both natural language and structured commands. Here are the fundamental operations:

- **Scan a topic**: `/scan <topic>` — Runs a signal scan across Reddit, X, TikTok, and other sources for the specified topic. Example: `/scan developer tools`
- **Validate an idea**: `/validate <idea description>` — Quick validation of a business or project idea, returning a Signal Score (0-10) with supporting evidence.
- **Compare entities**: `/compare A vs B vs C` — Side-by-side comparison of competitors, tools, or concepts with structured output.
- **Generate brief**: `/brief <topic>` — Creates an HTML-formatted research brief on the specified topic.

## Prompt Variants

The skill is flexible in how you phrase your requests. Here are effective prompt patterns:

- **Exploratory**: "What's trending in the fintech space right now?"
- **Specific**: "Find pain points related to API rate limiting on Reddit and X"
- **Comparative**: "Compare Vercel vs Netlify vs Cloudflare Pages for Next.js hosting"
- **Validating**: "Is there real demand for a time-tracking app for freelance designers?"
- **Actionable**: "Give me a 30-day launch plan for a micro-SaaS that monitors API uptime"

The key is to be specific about your vertical, intent, and desired output format. Vague prompts like "tell me about tech" produce broad, less useful results. Specific prompts like "find trending pain points in the React ecosystem with high engagement and low competitive density" produce focused, actionable intelligence.

## Comparison Mode

Comparison Mode is one of the most powerful features of the last30days skill. It enables structured A/B/C comparison of any set of entities — competitors, tools, frameworks, companies, or products. To activate it, use the `/compare` command with the entities you want to compare, separated by "vs." For example:

```
/compare Notion vs Obsidian vs Roam Research
```

The skill will return a structured comparison table covering dimensions like features, pricing, community size, sentiment, velocity of development, and market positioning. You can also specify comparison dimensions:

```
/compare Notion vs Obsidian vs Roam --dimensions pricing,api,community
```

Comparison Mode is especially valuable for competitive analysis, tool selection, and market positioning. The data is drawn from real social signals, not marketing pages — so you'll see what actual users say, not what companies claim.

## Watchlist Setup

The Watchlist feature enables persistent monitoring of specific topics, competitors, or verticals. Instead of running one-off scans, you add entities to your watchlist and receive periodic digests automatically.

- **Add to watchlist**: `/watch add <entity>` — Example: `/watch add Vercel` or `/watch add React ecosystem`
- **View watchlist**: `/watch list` — Shows all currently monitored entities.
- **Remove from watchlist**: `/watch remove <entity>` — Stops monitoring an entity.
- **Subscribe to digests**: `/watch subscribe --channel slack --frequency daily` — Configures digest delivery to Slack, email, or webhook.
- **Run watchlist scan**: `/watch scan` — Manually triggers a scan of all watchlisted entities.

Watchlist is ideal for ongoing competitive monitoring, market tracking, and trend spotting. Set it up once and let the skill do the work.

## Business Launch Workflow

The last30days skill includes a complete business launch workflow that takes you from idea to market in a structured, data-driven process. The workflow follows these steps:

1. **Idea Validation**: Run `/validate <your idea>` to get a Signal Score and supporting evidence.
2. **Market Scanning**: Run `/scan <your vertical>` to understand the competitive landscape and identify gaps.
3. **Competitive Analysis**: Run `/compare <your top 3 competitors>` to position your product.
4. **Landing Page**: Use the landing page factory to generate a conversion-optimized page.
5. **Unit Economics**: Run `/break-even` with your pricing and cost assumptions to validate financials.
6. **Launch Plan**: Generate a 30-day timeline with milestones and action items.

Each step produces structured output that feeds into the next, creating a coherent launch strategy backed by real data.

## ELI5 Mode

ELI5 (Explain Like I'm 5) mode simplifies the skill's output for non-technical users or quick overviews. Append `--eli5` to any command:

```
/scan Kubernetes trends --eli5
```

The skill will return a simplified, jargon-free summary with plain-language explanations of technical concepts. This is perfect for sharing findings with non-technical stakeholders, investors, or teammates who need the gist without the depth.

## Agent Mode

Agent Mode enables autonomous, multi-step research workflows. Instead of running individual commands, you give the agent a research question and it plans, executes, and synthesizes a complete research report. Activate it with:

```
/research What are the emerging trends in AI-powered developer tools for 2025?
```

The agent will decompose your question into sub-questions, execute searches across multiple sources, resolve and merge entities, evaluate coverage, and produce a comprehensive HTML brief — all autonomously. You can monitor progress in real-time and the final report includes full citations and methodology notes.

## HTML Briefs

HTML Briefs are the skill's formatted output format for research reports, market analyses, and competitive intelligence. Generate one with:

```
/brief <topic> --format html
```

HTML Briefs are email-ready, print-friendly, and include: table of contents, executive summary, detailed sections with inline citations, and methodology notes. They can be exported directly or embedded in emails, Slack messages, or web pages.

## Troubleshooting

**"No signals found"**: Your query may be too narrow or too specific. Try broadening the topic or using more common terminology. For example, instead of "GPT-4 fine-tuning for medical imaging," try "AI model customization in healthcare."

**Slow responses**: Deep scans (depth 3+) can take 30-60 seconds. Use `--depth 1` for quick results. Agent mode research can take 5-10 minutes for complex questions.

**Inconsistent scores**: Signal Scores are based on the most recent 30 days of data and can fluctuate as new signals emerge. Re-run scans periodically for updated scores.

**Watchlist not delivering**: Check that your webhook URL is correct and that the frequency is set properly. Use `/watch test` to verify delivery.

**Entity resolution errors**: If the skill is merging or splitting entities incorrectly, use more specific entity names in your queries. For example, use "Apple (company)" instead of just "Apple" to avoid confusion with the fruit.
