# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.2.0] - 2026-06-12

### Added — Agent Mode on chat.z.ai Instructions

This release adds comprehensive documentation for using the last30days skill in Agent Mode on chat.z.ai via the **"Please use this skill (skill URL) to..."** pattern — a zero-install, zero-config way to run the full research pipeline.

#### New Content

**README.md:**
- "Using Agent Mode on chat.z.ai (The Easy Way)" subsection in Step 6
- 4 ready-to-paste Agent mode prompts for chat.z.ai (find ideas, compare tools, validate demand, research pain points)
- "How the 'Please use this skill' Pattern Works" table with 7-step pipeline breakdown
- Pro tip on prompt specificity (Specificity = better entity resolution = higher signal)
- Weekend workflow table updated with chat.z.ai Agent mode alternatives for Friday 6 PM and Sunday AM

**guide.html:**
- New Page 7: "Use Agent Mode on chat.z.ai" — dedicated page with:
  - The "Please use this skill" pattern explanation card
  - 4 copy-paste Agent mode prompts (find ideas, compare tools, validate demand, research pain points)
  - 6-step pipeline visualization (Load → Decompose → Search → Score → Merge → Report)
  - Pro tip card on specificity
- Commands reference updated with `Please use this skill` pattern
- Page renumbered: Page 7→8 (Workflow & Tips), Page 8→9 (Resources + CTA)

**docs/how-to-use-30d-skill.md:**
- "Using Agent Mode on chat.z.ai (Zero Install)" section with:
  - The "Please use this skill" pattern explanation
  - 6 copy-paste prompts for different research tasks
  - "How the Pattern Works" table (7-step breakdown)
  - "Agent Mode Output Format" code block showing the structured report shape
  - "Tips for Better Agent Mode Results" — 5 actionable tips (be specific, include context, ask comparisons, chain queries, save findings)
- "The Method, Summarized" updated with item 8: Agent mode on chat.z.ai

**docs/skill-commands-reference.md:**
- New "Agent Mode on chat.z.ai (Zero Install)" section with:
  - Pattern syntax table
  - Copy-Paste Templates table (6 task types)
  - How the Pattern Works (5 steps)
  - Output Format code block
  - Tips for Better Results table (5 tips)
- Quick Reference updated with "Weekend Hackathon on chat.z.ai" and "Deep Research on chat.z.ai" workflows

**docs/hackathon-workflow.md:**
- New "Agent Mode Shortcut on chat.z.ai" section with:
  - Friday Evening prompts table (6 PM, 7 PM, 8 PM, 9 PM)
  - Saturday prompts table (Morning, Afternoon)
  - Sunday prompts table (Morning)
  - Note: Each prompt triggers Agent mode automatically
- Key Tips updated with chat.z.ai Agent mode tip

#### Tests
- `tests/test_guide_html.py`: Updated page count to >= 8, added `TestGuideAgentMode` class with 7 new tests
- `tests/test_agent_mode_docs.py`: New test file with 16 tests across 3 classes validating Agent mode content in README, docs/, and guide.html

### Design Decision
> The "Please use this skill" pattern is the lowest-friction path to using the last30days skill. No terminal, no install, no API keys. Just paste and get research. This makes the skill accessible to people who aren't developers or who want to try it before installing.

---

## [1.1.0] - 2026-06-12

### Changed — Repository Refocused as Tutorial

This release repositions the repository from a static "ideas guide" into a **hands-on tutorial** that teaches people how to use the last30days skill to research anything with real data, using hackathons as the example use case.

#### What Changed
- **README.md** — Completely rewritten as a step-by-step tutorial: "How to Find Hackathon Ideas Using Real Data." Now teaches the method, not just lists ideas.
- **docs/how-to-use-30d-skill.md** — Expanded into a comprehensive 8-step tutorial covering installation, first query, output modes, comparison mode, idea validation, agent mode, watchlist, and business launch tools.
- **Repository framing** — Changed from "10 ideas in a PDF" to "learn to research anything with the last30days skill, with hackathons as the example"

#### New Content in README
- "The Problem Every Hacker Faces" section — explains why guessing ideas fails
- "What You'll Learn" — 7 concrete learning outcomes
- "Quick Start: 3 Commands" — fastest path to first validated idea
- Step-by-step tutorial (7 steps) with exact commands and expected outputs
- "Real Example: Finding a Hackathon Idea" — full walkthrough from blank page to validated idea
- "The Same Method Works For Everything" — showing universal applicability beyond hackathons
- Data sources table with auth requirements
- Hackathon weekend workflow summary table

#### New Content in how-to-use-30d-skill.md
- "The Core Idea: Engagement Score > Search Ranking" philosophy section
- Detailed entity resolution explanation (what happens behind the scenes)
- Step-by-step walkthrough of the 5-stage research pipeline
- Idea validation decision rule (Signal Score >= 7/10 across 3+ sources)
- Business launch tools reference table
- Prompt variants guide with time estimates
- "The Method, Summarized" — 7-point checklist

### Design Philosophy
> This repository should teach, not just list. Every section answers "how do I do this myself?" not just "what ideas exist?" The hackathon context is the example, not the limit.

---

## [1.0.0] - 2026-06-12

### Added — Initial Release

#### Core Guide
- **Beautiful branded PDF guide** (14 pages) with Z.ai + rommark.dev dual branding
- **Cover page** with hero typography, brand logos, badge banner for 10% OFF Z.ai plans
- **10 hackathon project ideas** with difficulty ratings, descriptions, and tech stacks
- **Data sources overview** table showing 16+ platforms available through the skill
- **Step-by-step instructions** for using the last30days skill on chat.z.ai
- **Skill commands reference** with all major flags and modes
- **Hackathon weekend cheat sheet** with day-by-day workflow
- **Pro tips section** for winning strategies (research-backed presentations)
- **Essential resources** table with all key links
- **Discount banner** integration for Z.ai coding plan (code: ROK78RJKNW)

#### Ideas Documented
1. Trend-to-App Builder (Beginner)
2. Competitor Intelligence Dashboard (Intermediate)
3. Developer Pulse Newsletter (Beginner)
4. Niche Discovery Bot for Indie Hackers (Advanced)
5. Micro-SaaS Launch Pad (Intermediate)
6. Social Signal Validator (Beginner)
7. Pivot Predictor (Advanced)
8. Provider Marketplace Finder (Intermediate)
9. AI Research Agent for Hackathons (Advanced)
10. Vibe Coder Revenue Calculator (Intermediate)

#### Project Structure
- `README.md` — Full project documentation
- `CHANGELOG.md` — This file
- `LICENSE` — MIT License
- `FEATURES.md` — Feature documentation for all 10 ideas
- `CONTRIBUTING.md` — Contribution guidelines
- `guide.html` — Interactive web version of the guide
- `cover.html` — Standalone cover page
- `hackathon-ideas-guide.pdf` — Final branded PDF (14 pages)

#### Documentation
- `docs/how-to-use-30d-skill.md` — Detailed guide on using the skill with chat.z.ai
- `docs/hackathon-workflow.md` — Weekend workflow guide
- `docs/skill-commands-reference.md` — Full command reference

#### Feature Deep-Dives
- `features/idea-01-trend-to-app.md` through `features/idea-10-revenue-calculator.md`
- Each feature doc includes: concept, architecture, data flow, API mapping, and implementation notes

#### Tests
- `tests/test_guide_html.py` — Validates HTML guide structure and required elements
- `tests/test_cover_html.py` — Validates cover page layout and branding
- `tests/test_pdf_generation.py` — Validates PDF generation pipeline
- `tests/test_features_docs.py` — Validates all feature docs exist and have required sections
- `tests/test_links.py` — Validates all referenced URLs are accessible
- `tests/test_branding.py` — Validates Z.ai + rommark.dev branding consistency
- `tests/conftest.py` — Shared test fixtures and HTML parsing utilities

#### Scripts
- `scripts/build_guide.sh` — Automated build script for the PDF guide

#### Release Documentation
- `releases/v1.0.0.md` — Initial release notes with features, known issues, and upgrade notes

### Design Decisions

- **Dark mode design** chosen to align with developer/hackathon aesthetic
- **Dual branding** (Z.ai + rommark.dev) implemented as gradient text logos on cover
- **Badge banner** placed at top of cover page for maximum visibility of discount offer
- **Three difficulty tiers** (Beginner/Intermediate/Advanced) to serve all skill levels
- **Color coding** per idea card: purple (primary Z.ai), teal (accent), orange (rommark.dev)

### Bug Fixes During Development

#### Issue: Cover page absolute positioning in multi-page PDF
- **Root cause**: `html2pdf-next.js` converts `position: absolute` elements to static flow for multi-page documents, which broke the cover page layout
- **Fix**: Separated cover page into a standalone HTML file, rendered with `html2poster.js` (single-page renderer), then merged with content PDF using `pypdf`
- **Result**: Cover page now renders correctly with all elements in their intended positions

#### Issue: Footer overlap on content pages
- **Root cause**: `position: absolute; bottom: 20px` footers overlapped with content when page content varied in length
- **Fix**: Changed footer from absolute positioning to document flow (`padding-top`, `margin-top`, `border-top`) so it naturally follows content
- **Result**: Footers appear consistently after content without overlap

---

[1.0.0]: https://github.com/roman-ryzenadvanced/vibe-coding-hackathon-guide/releases/tag/v1.0.0
