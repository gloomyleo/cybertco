from __future__ import annotations
import argparse
from pathlib import Path
from .forecast import compute_forecast
from .report import build as build_report

def main():
    parser = argparse.ArgumentParser(prog="cybertco", description="Cybersecurity budgeting & TCO/ROI forecasting")
    sub = parser.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("forecast", help="Run forecast and compute metrics")
    f.add_argument("--config", default="config.yml", help="Path to config.yml (for validation only)")

    r = sub.add_parser("report", help="Generate charts and markdown report")

    args = parser.parse_args()
    base = Path(".").resolve()

    if args.cmd == "forecast":
        compute_forecast(base)
        print("Wrote:", base / "outputs" / "forecast.csv")
        print("Wrote:", base / "outputs" / "metrics.json")
    elif args.cmd == "report":
        build_report(base)
        print("Wrote:", base / "outputs" / "annual_cost_breakdown.png")
        print("Wrote:", base / "outputs" / "net_cash_flow.png")
        print("Wrote:", base / "outputs" / "report.md")
