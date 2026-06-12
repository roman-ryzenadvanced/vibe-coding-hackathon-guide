# Skill Commands Reference

Complete reference for all last30days-skill flags, modes, and commands with examples.

---

## Basic Research Commands

| Command | Flags | Description | Example |
|---|---|---|---|
| `/scan` | `--depth`, `--time-range`, `--sources` | Run a signal scan across social platforms for a topic | `/scan developer tools --depth 2 --time-range 7d` |
| `/validate` | `--depth`, `--vertical` | Validate an idea and return Signal Score (0-10) | `/validate time-tracking app for freelancers` |
| `/brief` | `--format`, `--sections`, `--time-range` | Generate a formatted research brief | `/brief AI coding assistants --format html` |
| `/research` | `--depth`, `--sources`, `--max-iterations` | Launch autonomous research agent for complex questions | `/research What are the top emerging fintech trends?` |

---

## Output Modes

| Flag | Values | Description | Example |
|---|---|---|---|
| `--format` | `html`, `markdown`, `json`, `text` | Output format for results | `/brief React ecosystem --format html` |
| `--depth` | `1` (quick), `2` (standard), `3` (deep) | Scan depth level — higher = more thorough but slower | `/scan DevOps tools --depth 3` |
| `--eli5` | (none — flag only) | Simplify output for non-technical audiences | `/scan Kubernetes --eli5` |
| `--time-range` | `7d`, `14d`, `30d` | Time window for signal data | `/scan fintech --time-range 7d` |
| `--sources` | `reddit`, `x`, `tiktok`, `hn`, `github`, `all` | Filter which sources to scan | `/scan React --sources reddit,x` |
| `--sections` | Comma-separated list | Include only specific sections in output | `/brief AI tools --sections summary,quotes` |

---

## Comparison Mode

| Command | Flags | Description | Example |
|---|---|---|---|
| `/compare` | `--dimensions` | Structured A/B/C comparison of entities | `/compare Notion vs Obsidian vs Roam` |
| `--dimensions` | `features`, `pricing`, `community`, `sentiment`, `velocity`, `all` | Specify comparison dimensions | `/compare Vercel vs Netlify --dimensions pricing,features` |
| `--time-range` | `7d`, `14d`, `30d` | Time window for comparison data | `/compare React vs Vue --time-range 30d` |

---

## Competitor & Market Analysis

| Command | Flags | Description | Example |
|---|---|---|---|
| `/scan competitors` | `--vertical`, `--depth` | Scan for competitors in a vertical | `/scan competitors --vertical project-management` |
| `/compare` | (see above) | Direct competitor comparison | `/compare Stripe vs Braintree vs Square` |
| `/watch add` | `--beat` | Add competitor to watchlist for ongoing monitoring | `/watch add Vercel --beat hosting` |
| `/watch scan` | (none) | Trigger manual scan of all watchlisted entities | `/watch scan` |
| `/validate` | `--vertical`, `--depth` | Validate idea within competitive context | `/validate API monitoring tool --vertical dev-tools` |

---

## Agent Mode

| Command | Flags | Description | Example |
|---|---|---|---|
| `/research` | `--depth`, `--max-iterations`, `--sources` | Launch autonomous research agent | `/research AI dev tools market landscape 2025` |
| `--max-iterations` | Integer (default: 3) | Maximum research iteration cycles | `/research fintech trends --max-iterations 5` |
| `--sources` | (see output modes) | Restrict agent's source pool | `/research Rust adoption --sources reddit,hn,github` |
| `--depth` | `1`, `2`, `3` | Depth of each iteration's scans | `/research cloud computing --depth 2` |

**Agent Mode Workflow**: The agent automatically decomposes the question → runs scans → resolves entities → merges clusters → evaluates coverage → loops if insufficient → synthesizes narrative → generates HTML brief.

---

## ELI5 Mode

| Flag | Applies To | Description | Example |
|---|---|---|---|
| `--eli5` | `/scan`, `/brief`, `/validate`, `/compare` | Simplify output to plain language | `/scan Kubernetes --eli5` |
| `--eli5` | `/research` | Agent produces simplified final report | `/research quantum computing --eli5` |

ELI5 mode removes jargon, uses analogies, and provides brief contextual explanations for technical terms. Ideal for sharing findings with non-technical stakeholders.

---

## Store & Watchlist

| Command | Flags | Description | Example |
|---|---|---|---|
| `/watch add` | `--beat` | Add entity to watchlist | `/watch add React --beat frontend` |
| `/watch remove` | (none) | Remove entity from watchlist | `/watch remove Angular` |
| `/watch list` | (none) | View all watchlisted entities | `/watch list` |
| `/watch scan` | (none) | Manually trigger watchlist scan | `/watch scan` |
| `/watch subscribe` | `--channel`, `--frequency`, `--webhook` | Subscribe to watchlist digests | `/watch subscribe --channel slack --frequency daily --webhook https://hooks.slack.com/...` |
| `/watch test` | (none) | Test watchlist delivery configuration | `/watch test` |
| `--beat` | String | Group watchlist entities into thematic beats | `/watch add Next.js --beat frontend` |
| `--frequency` | `hourly`, `daily`, `weekly` | Digest delivery frequency | `/watch subscribe --frequency daily` |

---

## Business Tools

| Command | Flags | Description | Example |
|---|---|---|---|
| `/validate` | `--vertical`, `--depth` | Validate business idea with Signal Score | `/validate SaaS uptime monitor for startups` |
| `/break-even` | `--price`, `--cac`, `--churn`, `--market-size`, `--conversion` | Calculate break-even timeline and unit economics | `/break-even --price 19 --cac 50 --churn 0.05` |
| `/niche-validator` | `--depth` | Score niche on demand, competition, and viability | `/niche-validator freelance designer tools` |
| `/landing-page-factory` | `--pain-point`, `--features`, `--pricing` | Generate a conversion-optimized landing page | `/landing-page-factory TaskMonitor --pain-point "API downtime costs money" --features alerts,dashboard,integrations` |
| `/ad-launch` | `--vertical`, `--budget`, `--platforms` | Generate ad campaign playbook | `/ad-launch --vertical dev-tools --budget 1000 --platforms meta,google,x` |
| `/timeline` | `--launch-date`, `--milestones` | Generate 30-day launch timeline | `/timeline API monitor --launch-date 2025-04-01 --milestones mvp,landing-page,launch` |
| `/brief` | `--format html` | Generate formatted business intelligence brief | `/brief competitive landscape for API monitoring --format html` |

---

## Quick Reference: Common Workflows

### Weekend Hackathon (3 steps)
```
1. /validate <your idea>
2. /scan <your vertical> --depth 2
3. /compare <competitor 1> vs <competitor 2> vs <competitor 3>
```

### Business Launch (6 steps)
```
1. /validate <idea>
2. /scan <vertical> --depth 3
3. /compare <top 3 competitors>
4. /break-even --price <price> --cac <cac> --churn <churn>
5. /landing-page-factory <app name> --pain-point <pain point>
6. /timeline <idea> --launch-date <date>
```

### Competitive Monitoring (ongoing)
```
1. /watch add <competitor 1> <competitor 2> <competitor 3>
2. /watch subscribe --channel slack --frequency daily
3. /watch scan  (run periodically)
```

### Deep Research (1 command)
```
/research <your research question> --depth 3 --max-iterations 5
```
