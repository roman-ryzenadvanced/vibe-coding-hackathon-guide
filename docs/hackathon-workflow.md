# Hackathon Weekend Workflow Guide

## Overview

This guide provides a structured Friday-to-Sunday workflow for using the last30days skill during a hackathon. Each day has specific goals, commands to run, and expected outputs. Follow this workflow to maximize your hackathon weekend and ship a validated, data-backed product.

---

## Friday Evening: Ideation & Validation (6 PM - Midnight)

**Goal**: Identify and validate your hackathon idea using real market signals.

### 6:00 PM — Kickoff & Brainstorming
Start by listing 3-5 ideas you're considering. Don't filter yet — just get them on paper.

**Command**: For each idea, run a quick validation:
```
/validate <idea 1>
/validate <idea 2>
/validate <idea 3>
```

**Expected Output**: Signal Scores (0-10) for each idea with user quotes, engagement metrics, and competitive density. Compare the scores and eliminate any idea below 6.0.

### 7:00 PM — Deep Dive on Top 2 Ideas
Take your top 2 scoring ideas and run deeper scans.

**Commands**:
```
/scan <idea 1 vertical> --depth 2
/scan <idea 2 vertical> --depth 2
/compare <top competitors for idea 1>
/compare <top competitors for idea 2>
```

**Expected Output**: Detailed signal reports with trending pain points, competitive landscape, and gap analysis. The comparison output will show you where competitors are weak and where opportunities exist.

### 8:00 PM — Final Decision & Market Mapping
By now, one idea should clearly outperform the other. Commit to it.

**Commands**:
```
/validate <chosen idea> --depth 3
/compare <top 3 competitors> --dimensions features,pricing,gaps
/watch add <competitor 1> <competitor 2> <competitor 3>
```

**Expected Output**: A comprehensive validation report with high-confidence Signal Score, detailed competitive comparison, and active watchlist monitoring for the weekend.

### 9:00 PM - Midnight — Unit Economics & Architecture Planning
Validate the financials before you start building.

**Commands**:
```
/break-even --price <proposed price> --cac <estimated cac> --churn <estimated churn>
/niche-validator <your niche>
```

**Expected Output**: Break-even timeline, LTV:CAC ratio, payback period, and niche viability assessment. If the economics don't work at your proposed pricing, adjust now — not after you've built the product.

Also use this time to generate a launch plan:
```
/timeline <your idea> --launch-date Sunday --milestones mvp,landing-page,demo
```

**Expected Output**: A structured timeline with Friday night through Sunday milestones. Print this and tape it to your monitor.

---

## Saturday: Build & Iterate (9 AM - Midnight)

**Goal**: Build the MVP, deploy the landing page, and iterate based on signal data.

### 9:00 AM — Landing Page First
Before writing application code, deploy your landing page. This gives you a URL to share and starts collecting interest.

**Commands**:
```
/landing-page-factory <app name> --pain-point <validated pain point> --features <top 3 features>
```

**Expected Output**: A complete landing page project (Next.js + Tailwind) with hero, features, pricing, and CTA. Deploy to Vercel immediately.

### 10:00 AM - 6:00 PM — Core Build Sprint
Focus on building the core product. Periodically check your watchlist for any competitive movements or new signals that might affect your approach.

**Periodic Commands** (run every 2-3 hours):
```
/watch scan
```

**Expected Output**: Updates on any competitor movements or new market signals. If a competitor launches a similar feature, you'll know immediately and can adjust.

### 6:00 PM — Midpoint Check-In
Run a quick validation refresh to make sure your build direction still aligns with market signals.

**Commands**:
```
/validate <your idea as currently scoped>
/scan <your vertical> --depth 1
```

**Expected Output**: Updated Signal Score for your refined idea. If the score has dropped, consider whether you've drifted from the original validated pain point. If it's improved, you're on the right track.

### 7:00 PM - Midnight — Polish & Prepare Demo
Focus on polish, error handling, and demo preparation. Generate an HTML brief of your competitive landscape for the demo.

**Commands**:
```
/brief <your market> --format html
```

**Expected Output**: A formatted competitive landscape brief you can reference during your demo to show judges you built with market awareness.

---

## Sunday: Ship & Present (9 AM - 5 PM)

**Goal**: Final polish, ship to production, and present a data-backed demo.

### 9:00 AM — Final Deployment
Deploy your final build to production. Run one last competitive check.

**Commands**:
```
/watch scan
/compare <your product> vs <top competitors> --dimensions features,pricing
```

**Expected Output**: Confirmation that your competitive positioning is solid and no new threats have emerged over the weekend.

### 10:00 AM - 1:00 PM — Demo Preparation
Prepare your 3-minute demo. Use the HTML brief from Saturday as a reference for market context. Practice your narrative: problem → signal validation → solution → live demo → unit economics.

### 1:00 PM - 3:00 PM — Final Testing & Buffer
Last-minute bug fixes and testing. Generate a final validation report to include in your submission.

**Commands**:
```
/validate <your idea> --depth 2
/break-even --price <final price> --cac <final cac estimate> --churn <final churn estimate>
```

**Expected Output**: Final Signal Score and unit economics that you can present to judges as evidence of market validation.

### 3:00 PM - 5:00 PM — Present & Submit
Present your project with confidence, backed by 48 hours of data-driven decision-making. Show judges not just what you built, but why you built it — with Signal Scores, competitive comparisons, and validated unit economics.

---

## Key Tips

- **Validate before you build**: The 30 minutes spent validating on Friday evening saves 10 hours of wasted building on Saturday.
- **Check your watchlist**: Competitive landscapes change fast. A Saturday morning scan might reveal a competitor launch you didn't know about.
- **Trust the data, not your gut**: If the Signal Score says pivot, pivot. The data has no emotional attachment to your idea.
- **Use ELI5 mode for teammates**: Not everyone on your team needs the deep analysis. `--eli5` gives them the gist.
- **Generate HTML briefs for judges**: A formatted market research brief sets your project apart from teams that just built something cool without validating demand.
