from __future__ import annotations
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import json

def make_charts(base: Path):
    out = base / "outputs"
    df = pd.read_csv(out / "forecast.csv")

    plt.figure()
    df.plot(x="year", y=["capex_cash", "opex_cash"], kind="bar", stacked=True)
    plt.title("Annual Cost Breakdown")
    plt.xlabel("Year")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.savefig(out / "annual_cost_breakdown.png")
    plt.close()

    plt.figure()
    df.plot(x="year", y="net_cash_flow", kind="line", marker="o")
    plt.title("Net Cash Flow by Year")
    plt.xlabel("Year")
    plt.ylabel("Net Cash Flow")
    plt.tight_layout()
    plt.savefig(out / "net_cash_flow.png")
    plt.close()

def write_report(base: Path):
    out = base / "outputs"
    df = pd.read_csv(out / "forecast.csv")
    metrics = json.loads((out / "metrics.json").read_text())

    lines = []
    lines.append("# CyberTCO — Summary\n")
    lines.append(f"- Base Year: {metrics['base_year']}")
    lines.append(f"- Horizon: {metrics['horizon_years']} years")
    lines.append(f"- TCO: {metrics['tco']:,}")
    lines.append(f"- Total Benefit: {metrics['total_benefit']:,}")
    lines.append(f"- NPV: {metrics['npv']:,}")
    lines.append(f"- ROI: {metrics['roi']*100:.2f}%")
    lines.append(f"- Payback Year: {metrics['payback_year']}\n")
    lines.append("## Annual View\n")
    lines.append(df.to_markdown(index=False))
    lines.append("\n## Charts\n")
    lines.append("![Annual Cost Breakdown](annual_cost_breakdown.png)")
    lines.append("![Net Cash Flow](net_cash_flow.png)\n")

    (out / "report.md").write_text("\n".join(lines))

def build(base: Path):
    make_charts(base)
    write_report(base)
