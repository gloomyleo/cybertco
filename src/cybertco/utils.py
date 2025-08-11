from __future__ import annotations
import pandas as pd
from typing import Dict, List

def year_range(base_year:int, horizon:int) -> List[int]:
    return list(range(base_year, base_year + horizon))

def apply_inflation(amount: float, years_from_base: int, rate: float) -> float:
    return amount * ((1 + rate) ** years_from_base)

def discount(value: float, years_from_base: int, discount_rate: float) -> float:
    return value / ((1 + discount_rate) ** years_from_base)

def freq_to_per_year(freq: str) -> int:
    return {"monthly": 12, "quarterly": 4, "yearly": 1}.get(str(freq).lower(), 1)
