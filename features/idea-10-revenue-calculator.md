# Vibe Coder Revenue Calculator

## Quick Stats

| Metric | Value |
|---|---|
| Difficulty | Beginner-Intermediate |
| Estimated Build Time | 4-6 hours |
| Core Skill Feature | break_even.py + niche_validator.py |
| API Keys Required | z.ai GLM API |

---

## The Problem

One of the most common reasons indie projects and micro-SaaS ventures fail is not technical failure but financial miscalculation. Founders build products without a clear understanding of whether the unit economics work — whether the cost of acquiring a customer is lower than the revenue that customer generates over their lifetime. They set prices based on gut feelings or competitor matching, estimate their market size from top-down guesses, and project revenue with wildly optimistic conversion rates. The result is a product that technically works but can never be profitable because the unit economics are fundamentally broken. Even founders who understand the importance of unit economics often lack the tools to calculate them properly. Spreadsheets are error-prone and hard to share. Financial modeling tools like Causal or Pry are designed for venture-scale startups with complex financial structures, not for indie hackers who need a simple answer to "If I charge $15/month and spend $50 to acquire each customer, how many do I need to break even?" The problem is compounded by the fact that unit economics don't exist in a vacuum — they depend on market conditions, competitive pricing, customer acquisition channels, and real-time demand signals that change constantly. A break-even calculation that assumes a $50 CAC is meaningless if the actual CAC for your niche turns out to be $200. Similarly, a $15/month price point might seem reasonable until you realize that the competitive average in your niche is $8 and your target customers have low willingness to pay. What's needed is a revenue calculator that doesn't just do the math — it pairs financial projections with real-time market signal data to give founders a reality-checked assessment of their business viability.

---

## The Solution

The Vibe Coder Revenue Calculator is a web tool that wraps the last30days skill's break_even.py and niche_validator.py into a visual, interactive calculator paired with real-time signal data. Instead of static spreadsheet calculations, the calculator provides a dynamic, visual interface where founders can adjust key parameters (price, CAC, churn rate, market size, conversion rate) and immediately see the impact on break-even timeline, MRR projections, and LTV:CAC ratio. What makes this tool unique is that it pairs these financial calculations with real-time signal data from the last30days signal scanner. When you enter your niche, the calculator automatically pulls competitive pricing data, estimated CAC ranges for your channel, typical churn rates for your vertical, and market size indicators — all from real social signals, not industry benchmarks from 2019. The calculator produces three core outputs: a Break-Even Timeline (visual chart showing month-by-month revenue vs. costs until profitability), a Unit Economics Scorecard (LTV, CAC, LTV:CAC ratio, payback period, margin), and a Viability Verdict (a plain-English assessment: "This niche has strong unit economics — break-even at month 5 with LTV:CAC of 4.2x" or "Warning: CAC likely exceeds LTV at current pricing — consider increasing price or narrowing niche"). The tool also provides sensitivity analysis: a tornado chart showing which parameter has the biggest impact on break-even, so founders know where to focus their optimization efforts. For hackathon teams, this means you can validate the financial viability of your idea in minutes and adjust your pricing and acquisition strategy before writing a single line of code.

---

## Architecture

The Vibe Coder Revenue Calculator is built as a single-page web application with a parameter input panel on the left, a visualization panel in the center, and a signal data panel on the right. The parameter input panel uses shadcn/ui form components with real-time validation and auto-suggestions from signal data. The visualization panel uses Recharts to render the break-even timeline, unit economics scorecard, and sensitivity analysis tornado chart. The signal data panel shows real-time market data pulled from the last30days signal scanner: competitive pricing distribution, estimated CAC ranges, typical churn rates, and market size indicators for the selected niche. The backend consists of two API routes: `/calculate` (runs break_even.py and niche_validator.py logic) and `/signals` (queries the signal scanner for niche-specific market data). When the user changes any parameter or selects a different niche, both routes are called in parallel and the UI updates in real-time. The calculation engine is deterministic and runs entirely on the server, with results cached by parameter hash for instant re-renders of previously calculated configurations.

```
[Niche + Parameters] → /calculate (break_even + niche_validator) → Financial Projections
         ↓                                                                    ↓
/signals (Signal Scanner) → Market Data → Auto-fill Suggestions       Visualization Panel
                                              ↓                          ↓
                                    Parameter Refinement ← User ← Interactive Charts
```

---

## Data Flow

1. User enters niche description and key parameters (price, CAC estimate, churn rate, market size, conversion rate).
2. Alternatively, user selects a niche and the system auto-fills parameters from signal data.
3. Frontend sends parameters to `/calculate` endpoint in real-time as values change.
4. Backend runs break_even.py logic: calculates month-by-month revenue, costs, and cumulative profit/loss.
5. Backend runs niche_validator.py logic: scores the niche on demand, competition, pricing viability, and timing.
6. `/signals` endpoint queries signal scanner for the niche: competitive pricing distribution, CAC estimates, churn benchmarks.
7. Financial projections are returned: break-even month, MRR trajectory, LTV, CAC, LTV:CAC ratio, payback period.
8. Signal data is returned: pricing distribution, CAC ranges, churn benchmarks, market size indicators.
9. Frontend renders break-even timeline chart, unit economics scorecard, and sensitivity tornado chart.
10. Frontend also renders signal data panel with market context and auto-fill suggestions.
11. User adjusts parameters and sees real-time impact on all visualizations.
12. User can export the complete analysis as an HTML brief or PDF.

---

## Skill API Mapping

| Feature Step | Skill API / Command | Parameters |
|---|---|---|
| Niche Scan | `/scan <niche>` | niche, depth, time_range |
| Break-Even Calc | `break_even.py` logic | price, cac, churn, market_size, conversion |
| Niche Validation | `niche_validator.py` logic | niche, demand_score, competition_score |
| Signal Data | `/signals <niche>` | niche, data_types (pricing, cac, churn) |
| Sensitivity Analysis | Built-in calculator | base_params, sensitivity_range |
| Viability Verdict | GLM Chat API | financial_data, signal_data, max_tokens=150 |
| HTML Brief | `/brief <analysis> --format html` | niche, calculations, signals |

---

## Tech Stack

- **Frontend**: Next.js 16, TypeScript, Tailwind CSS 4, shadcn/ui, Recharts for interactive visualizations
- **API Backend**: Next.js API Routes (`/calculate`, `/signals`)
- **AI/Generation**: z.ai GLM API for viability verdict and narrative generation
- **Calculation Engine**: Server-side break_even.py and niche_validator.py logic (ported to TypeScript)
- **Signal Processing**: last30days skill (signal scanner for market data, niche validator)
- **Caching**: In-memory LRU cache for calculation results (keyed by parameter hash)
- **Export**: HTML Brief module for shareable reports
- **Deployment**: Vercel (serverless functions)

---

## Implementation Steps

| Step | Task | Time Estimate |
|---|---|---|
| 1 | Set up Next.js project with three-panel layout | 30 min |
| 2 | Build parameter input form with real-time validation and auto-fill | 1 hour |
| 3 | Port break_even.py logic to TypeScript and build `/calculate` endpoint | 1 hour |
| 4 | Port niche_validator.py logic to TypeScript and integrate | 45 min |
| 5 | Build `/signals` endpoint with signal scanner integration | 45 min |
| 6 | Implement break-even timeline chart with Recharts | 45 min |
| 7 | Build unit economics scorecard UI | 30 min |
| 8 | Implement sensitivity analysis tornado chart | 45 min |
| 9 | Build signal data panel with market context and auto-fill | 45 min |
| 10 | Add export functionality (HTML brief) and polish UI | 30 min |

**Total estimated time: ~6 hours**

---

## Demo Script (3-Minute Walkthrough)

**Minute 0:00-0:40 — Niche Selection & Auto-Fill**
Open the Vibe Coder Revenue Calculator. Type "API monitoring for small dev teams" in the niche field. The signal scanner auto-fills parameters: "Average competitor price: $12-29/month. Estimated CAC: $30-60. Typical churn: 4-6%/month. Market size signal: Strong." Explain that these aren't guesses — they're derived from real social signals and competitive data.

**Minute 0:40-1:30 — Interactive Calculations**
Adjust the price slider to $19/month. The break-even timeline chart updates instantly: the line crosses zero at month 5. The unit economics scorecard shows: LTV $380, CAC $45, LTV:CAC ratio 8.4x, payback period 2.4 months. The viability verdict appears: "Strong unit economics — break-even at month 5 with excellent LTV:CAC ratio. This niche is financially viable at current pricing."

**Minute 1:30-2:15 — Sensitivity Analysis & What-If**
Switch to the sensitivity analysis view. The tornado chart shows that CAC has the biggest impact on break-even timeline, followed by price, then churn. Drag the CAC slider from $45 to $120 (simulating paid advertising). Break-even shifts from month 5 to month 11. The verdict updates: "Warning: at CAC $120, break-even extends to 11 months. Consider organic channels or increasing price to $29/month."

**Minute 2:15-3:00 — Price Optimization & Export**
Adjust price to $29/month with the higher CAC of $120. Break-even improves to month 7. The signal data panel shows: "Competitors at $29/month: 3 (low density). Market accepts this price point — 67% of users in signal data pay $20+/month." Click "Export Analysis" to generate an HTML brief with all calculations, charts, and signal data. End by emphasizing: "Financial viability isn't a guessing game — it's a calculation. The Revenue Calculator pairs your assumptions with real market data to give you a reality-checked assessment before you invest a single hour of development time."
