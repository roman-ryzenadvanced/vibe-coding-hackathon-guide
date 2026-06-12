# AI Research Agent

## Quick Stats

| Metric | Value |
|---|---|
| Difficulty | Advanced |
| Estimated Build Time | 10-14 hours |
| Core Skill Feature | Agent Mode + Entity Resolution + Cluster Merge + HTML Brief |
| API Keys Required | z.ai GLM API |

---

## The Problem

Research is the invisible bottleneck of every knowledge-work project. Whether you're writing a market analysis, preparing an investor memo, evaluating a competitive landscape, or investigating a new technology, the process is painfully manual and time-consuming. You start with a question, open 50 browser tabs, read dozens of articles, take scattered notes, and then spend hours synthesizing everything into a coherent document. The problem isn't just the time — it's the fragmentation. Information is scattered across Reddit threads, Hacker News discussions, academic papers, blog posts, X threads, YouTube videos, and GitHub repos. Each source provides a piece of the puzzle, but assembling those pieces requires significant cognitive effort and domain expertise. Worse, the process is not reproducible: if you research the same topic a month later, you'll find different sources, draw different conclusions, and have no way to compare your findings over time. For teams, the problem multiplies — different team members research overlapping topics without coordination, producing redundant or contradictory findings. Traditional research tools like Google Scholar, PubMed, or even AI chatbots help with individual queries but can't orchestrate a multi-source, multi-step research workflow. They give you answers to questions, but they don't give you a structured, cited, reproducible research report. What's needed is an autonomous research agent that can take a research question, systematically explore relevant sources, resolve entities across fragmented data, merge related findings into coherent clusters, and produce a publication-ready HTML brief — all without human intervention beyond the initial question.

---

## The Solution

The AI Research Agent is an autonomous research agent that uses the last30days skill's Agent Mode, Entity Resolution, Cluster Merge, and HTML Brief Generation to produce comprehensive, cited research reports from a single research question. Unlike a simple chatbot that answers questions with a single response, the Research Agent operates in Agent Mode — a multi-step, self-directed workflow where it plans its research strategy, executes searches across multiple sources, evaluates and cross-references findings, identifies gaps in its knowledge, and iteratively refines its search until it has sufficient coverage. The Entity Resolution engine is critical: when the agent finds "React Server Components" mentioned in a blog post, "RSC" in a Reddit thread, and "server components" in a GitHub issue, it recognizes these as the same entity and merges the findings. The Cluster Merge algorithm then groups related entities into thematic clusters — for example, grouping all findings about React's rendering strategy into one cluster and all findings about its data-fetching approach into another. Finally, the HTML Brief Generator assembles all clusters into a beautifully formatted, citation-rich research report with a table of contents, executive summary, detailed sections with inline citations, and a methodology note. The entire process runs autonomously once the research question is submitted, with a live progress dashboard showing the agent's current activity, sources explored, and findings accumulated. For hackathon teams, this means you can submit a research question on Friday evening and have a comprehensive market research report ready by Saturday morning.

---

## Architecture

The AI Research Agent is built as an autonomous agent loop with five phases: Planning, Exploration, Resolution, Synthesis, and Publication. The Planning phase uses GLM to decompose the research question into sub-questions and determine which sources to search. The Exploration phase executes searches across Reddit, X, Hacker News, GitHub, arXiv, and blogs using the signal scanner, collecting raw findings. The Resolution phase runs Entity Resolution to merge duplicate entities across sources and Cluster Merge to group related findings into thematic clusters. The Synthesis phase uses GLM to generate narrative sections for each cluster, with inline citations linking back to source URLs. The Publication phase uses the HTML Brief module to assemble all sections into a formatted research report. The agent loop is iterative: after each cycle, the agent evaluates its coverage and decides whether additional searches are needed. A state machine tracks the agent's progress through the phases, and a live dashboard shows real-time status. The agent maintains a research log that records every search query, source visited, and finding extracted, making the entire process fully auditable and reproducible.

```
[Research Question] → Planning (GLM Decomposition) → Sub-Questions
                                                         ↓
[Findings Accumulator] ← Exploration (Signal Scanner) ← Search Queries
         ↓                                               ↑
Entity Resolution ← Raw Findings ←──────────────────────┘
         ↓
Cluster Merge → Thematic Clusters
         ↓
Synthesis (GLM Narrative Generation) → Sections with Citations
         ↓
Publication (HTML Brief) → Research Report
         ↓
[Coverage Check] → If insufficient → Loop back to Exploration
```

---

## Data Flow

1. User submits research question via web interface or `/research <question>` command.
2. Planning Phase: GLM decomposes the question into 5-10 sub-questions and identifies relevant sources.
3. Exploration Phase: Agent executes searches across Reddit, X, HN, GitHub, arXiv, blogs for each sub-question.
4. Raw findings are collected: `{ source, title, content, url, relevance_score, timestamp }`.
5. Entity Resolution merges duplicate entities across sources (e.g., "RSC" = "React Server Components").
6. Cluster Merge groups related entities into thematic clusters based on semantic similarity.
7. Coverage Check: Agent evaluates whether clusters sufficiently address all sub-questions.
8. If coverage is insufficient, agent generates new search queries and loops back to step 3.
9. Synthesis Phase: GLM generates narrative sections for each cluster with inline citations.
10. Publication Phase: HTML Brief Generator assembles all sections into a formatted research report.
11. Research report is delivered as an HTML page with table of contents, executive summary, detailed sections, citations, and methodology note.
12. Research log is persisted for auditability and reproducibility.

---

## Skill API Mapping

| Feature Step | Skill API / Command | Parameters |
|---|---|---|
| Research Init | `/research <question>` | question, depth, time_range |
| Planning | GLM Chat API | question, decomposition_prompt |
| Exploration | `/scan <sub-question>` | query, sources, depth |
| Entity Resolution | Auto (built-in) | match_threshold, context_window |
| Cluster Merge | Auto (built-in) | similarity_threshold, min_cluster_size |
| Coverage Check | Built-in evaluator | sub_questions, cluster_coverage |
| Synthesis | GLM Chat API | cluster_data, citation_format, style_guide |
| HTML Brief | `/brief <research> --format html` | sections, template, citation_style |
| Research Log | Built-in logger | queries, sources, findings, timestamps |

---

## Tech Stack

- **Frontend**: Next.js 16, TypeScript, Tailwind CSS 4, shadcn/ui (research dashboard with live progress)
- **AI/Generation**: z.ai GLM API for planning, synthesis, and coverage evaluation
- **Agent Framework**: Custom agent loop with state machine and iterative refinement
- **Signal Processing**: last30days skill (agent mode, signal scanner, entity resolution, cluster merge, HTML brief)
- **Sources**: Reddit API, X API, Hacker News API, GitHub API, arXiv API, web scraping
- **Database**: Prisma ORM with PostgreSQL for research sessions, findings, and logs
- **Real-time**: Server-Sent Events (SSE) for live progress updates
- **Export**: HTML Brief module + PDF generation (via Puppeteer)
- **Deployment**: Vercel (dashboard) + Railway (agent worker process)

---

## Implementation Steps

| Step | Task | Time Estimate |
|---|---|---|
| 1 | Set up Next.js project with research dashboard layout | 1 hour |
| 2 | Build agent loop state machine with phase transitions | 2 hours |
| 3 | Implement Planning phase with GLM-based question decomposition | 1.5 hours |
| 4 | Build Exploration phase with multi-source signal scanner integration | 2 hours |
| 5 | Implement Entity Resolution and Cluster Merge pipeline | 1.5 hours |
| 6 | Build Coverage Check evaluator with loop-back logic | 1 hour |
| 7 | Implement Synthesis phase with GLM narrative generation and citations | 1.5 hours |
| 8 | Build HTML Brief publication module with formatted report output | 1 hour |
| 9 | Build live progress dashboard with SSE updates | 1 hour |
| 10 | Add research log persistence, auditability, and reproducibility | 1 hour |
| 11 | Polish UI, add demo data, and test end-to-end research flow | 1 hour |

**Total estimated time: ~13.5 hours**

---

## Demo Script (3-Minute Walkthrough)

**Minute 0:00-0:40 — Submitting a Research Question**
Open the AI Research Agent dashboard. Type a research question: "What are the emerging trends in AI-powered developer tools for 2025?" Click "Start Research." The agent immediately enters the Planning phase — show the sub-questions being generated: "1. What AI dev tools launched in Q4 2024? 2. What are developers saying about AI coding assistants? 3. Which AI dev tool startups raised funding recently?"

**Minute 0:40-1:30 — Live Exploration & Entity Resolution**
The agent enters the Exploration phase. A live activity feed shows searches being executed: "Scanning Reddit r/MachineLearning... 47 results. Scanning Hacker News... 83 results. Scanning GitHub trending... 29 results." Switch to the Entity Resolution view: show how "Copilot" and "GitHub Copilot" and "GH Copilot" are being merged into a single entity. The Cluster Merge view shows thematic clusters forming: "AI Code Generation," "AI Testing," "AI Documentation."

**Minute 1:30-2:15 — Synthesis & Coverage Check**
The agent enters the Synthesis phase. GLM generates narrative sections for each cluster. Show a section being written in real-time with inline citations: "GitHub Copilot has seen a 340% increase in adoption among enterprise teams [1], while Cursor has emerged as a strong alternative favored by startup developers [2]." The Coverage Check runs and shows: "4/5 sub-questions fully covered. Running additional search for: 'AI dev tool funding Q4 2024'."

**Minute 2:15-3:00 — Publication & Research Report**
The agent enters the Publication phase. The HTML Brief is generated and displayed as a fully formatted research report with: table of contents, executive summary, 5 detailed sections with 47 citations, and a methodology note. Show the "Export" options: HTML, PDF, Markdown. Click on a citation to see it link back to the original source. End by emphasizing: "A comprehensive, cited research report that would take a human researcher 8-10 hours — produced autonomously in under 10 minutes, with full auditability and reproducibility."
