# Data Schemas & Formulas

## capex.csv
- id, item, date (YYYY-MM), amount, useful_life_years, project_id
- Depreciation: straight-line = amount / useful_life_years (book value *not* a cash cost; we model cash at purchase).

## opex.csv
- id, item, start (YYYY-MM), end (YYYY-MM), amount, freq (monthly|quarterly|yearly), project_id, kind (subscription|headcount|support)

## projects.csv
- project_id, name, category (e.g., Zero Trust, SOC, OT), start_year, end_year, expected_annual_benefit

## config.yml
```yaml
horizon_years: 5
base_year: 2025
inflation_rate: 0.03
discount_rate: 0.08
apply_inflation_to_opex: true
apply_inflation_to_capex: false
scenarios:
  include_headcount: true
  include_tools: true
  include_projects: true
```

## Metrics
- TCO: sum of all cash outlays (inflated as configured)
- NPV: discount_rate applied to annual net cash flows: benefits - costs
- ROI: (Total Benefits - Total Costs) / Total Costs
- Payback: first year cumulative net cash >= 0
