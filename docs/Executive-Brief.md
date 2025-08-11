# CyberTCO — Executive Brief

**Purpose:** Provide transparent, defensible cybersecurity budget planning and multi‑year forecasting, including CAPEX, OPEX, and total economics (TCO/ROI/NPV/Payback).

## What Leaders Get
- Clear year‑over‑year cost breakdown (CAPEX vs OPEX)
- Business‑value view via ROI, NPV, and Payback
- Scenario toggles (headcount, tools, program scope)
- Board‑ready charts and a one‑page summary (`outputs/report.md`)

## How It Works
1. **Inputs:** CSVs for CAPEX, OPEX, Projects; `config.yml` for horizon, inflation, discount.
2. **Compute:** `cybertco forecast` produces yearly totals & net cash flow.
3. **Communicate:** `cybertco report` generates charts and a concise summary for review.

## Typical Questions It Answers
- What’s our **TCO** across the program?
- How does **inflation** or **discount rate** change our spend picture?
- When do benefits exceed costs (**payback year**)?
- How do scenarios (e.g., **include headcount**) impact outcomes?

## Deliverables
- `outputs/forecast.csv` — Annual CAPEX/OPEX, benefits, net cash
- `outputs/metrics.json` — TCO, ROI, NPV, Payback
- `outputs/*.png` — Visuals for exec review
- `outputs/report.md` — One‑page, board‑ready summary

> **Presenting tip:** Start with the metrics line (TCO/ROI/NPV/Payback), then show the annual cost stack and the net cash flow trend. Close on the scenario sensitivity that leadership can choose today.
