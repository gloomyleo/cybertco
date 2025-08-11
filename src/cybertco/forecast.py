from __future__ import annotations
import pandas as pd
import yaml
from pathlib import Path
from typing import Dict, Tuple
from .utils import year_range, apply_inflation, discount, freq_to_per_year

def load_inputs(base: Path) -> Tuple[dict, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    config = yaml.safe_load((base / "config.yml").read_text())
    capex = pd.read_csv(base / "data" / "capex.csv")
    opex = pd.read_csv(base / "data" / "opex.csv")
    projects = pd.read_csv(base / "data" / "projects.csv")
    return config, capex, opex, projects

def _inflate_cost(amount, y, base_year, rate, enabled) -> float:
    if not enabled:
        return amount
    years_from_base = y - base_year
    return amount * ((1 + rate) ** max(0, years_from_base))

def compute_forecast(base: Path) -> Dict:
    config, capex, opex, projects = load_inputs(base)
    horizon = config["horizon_years"]
    base_year = config["base_year"]
    years = year_range(base_year, horizon)

    capex["purchase_year"] = capex["date"].str.slice(0,4).astype(int)

    annual = pd.DataFrame({"year": years})
    annual["capex_cash"] = 0.0
    annual["opex_cash"] = 0.0
    annual["benefit"] = 0.0

    for _, r in capex.iterrows():
        if r["purchase_year"] in years:
            idx = annual.index[annual["year"] == r["purchase_year"]][0]
            amt = _inflate_cost(
                r["amount"], r["purchase_year"], base_year,
                config["inflation_rate"], config.get("apply_inflation_to_capex", False)
            )
            annual.at[idx, "capex_cash"] += float(amt)

    opex["start_year"] = opex["start"].str.slice(0,4).astype(int)
    opex["end_year"] = opex["end"].str.slice(0,4).astype(int)
    for _, r in opex.iterrows():
        per_year_times = freq_to_per_year(r["freq"])
        for y in years:
            if y >= r["start_year"] and y <= r["end_year"]:
                amt = float(r["amount"]) * per_year_times
                amt = _inflate_cost(
                    amt, y, base_year,
                    config["inflation_rate"], config.get("apply_inflation_to_opex", True)
                )
                annual.loc[annual["year"]==y, "opex_cash"] += amt

    for _, r in projects.iterrows():
        for y in years:
            if y >= int(r["start_year"]) and y <= int(r["end_year"]):
                annual.loc[annual["year"]==y, "benefit"] += float(r["expected_annual_benefit"])

    annual["total_cost"] = annual["capex_cash"] + annual["opex_cash"]
    annual["net_cash_flow"] = annual["benefit"] - annual["total_cost"]

    dr = config["discount_rate"]
    annual["discounted_net"] = [ (v / ((1+dr)**(i))) for i, v in enumerate(annual["net_cash_flow"]) ]
    npv = annual["discounted_net"].sum()

    tco = annual["total_cost"].sum()
    total_benefit = annual["benefit"].sum()
    roi = (total_benefit - tco) / tco if tco else 0.0

    cum = 0.0
    payback_year = None
    for y, v in zip(annual["year"], annual["net_cash_flow"]):
        cum += v
        if cum >= 0 and payback_year is None:
            payback_year = int(y)

    outputs = base / "outputs"
    outputs.mkdir(exist_ok=True)
    annual.to_csv(outputs / "forecast.csv", index=False)

    metrics = {
        "base_year": base_year,
        "horizon_years": horizon,
        "tco": round(float(tco),2),
        "total_benefit": round(float(total_benefit),2),
        "npv": round(float(npv),2),
        "roi": round(float(roi),4),
        "payback_year": payback_year
    }
    (outputs / "metrics.json").write_text(__import__("json").dumps(metrics, indent=2))

    return {"annual": annual, "metrics": metrics}
