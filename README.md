![CyberTCO](assets/cybertco-banner.png)

# CyberTCO — Cybersecurity Budgeting, Costing & Forecast

A GitHub-ready package to plan **CAPEX/OPEX**, forecast multi-year spend, compute **TCO/NPV/ROI**, and generate reports & charts for a cybersecurity program.

## ✨ Features
- CAPEX & OPEX modeling with inflation and depreciation (straight-line).
- Multi-year forecasts with scenario toggles.
- Metrics: TCO, NPV, ROI, Payback.
- Reports: CSV outputs and Matplotlib charts.
- CLI: `cybertco` for one-command forecasting & reporting.
- Ready for GitHub Actions CI and community contributions.

## Quickstart
```bash
# 1) Create venv & install
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

pip install -e .

# 2) Run a forecast (uses data/*.csv and config.yml)
cybertco forecast --config config.yml

# 3) Generate charts and a markdown report in outputs/
cybertco report
```

## Inputs
- `data/capex.csv` — one-time asset purchases.
- `data/opex.csv` — recurring costs (tools, subscriptions, headcount).
- `data/projects.csv` — projects/initiatives mapping to costs.
- `config.yml` — planning horizon, inflation, discount rate, scenario flags.

## Outputs
- `outputs/forecast.csv` — per-year, per-category totals.
- `outputs/metrics.json` — TCO/NPV/ROI/Payback summary.
- `outputs/*.png` — charts.
- `outputs/report.md` — concise report.

## Example Metrics
- **TCO** (total cash outlay)
- **NPV** (discounted cash flows)
- **ROI** = (Benefits − Cost) / Cost  (benefit modeled per project in `projects.csv`)
- **Payback**: first year when cumulative benefits exceed cost

## Data Schemas
See [`docs/metrics.md`](docs/metrics.md) for column details & formulas.

## License
MIT
