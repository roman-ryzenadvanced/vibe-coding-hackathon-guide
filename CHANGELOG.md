# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
