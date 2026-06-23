"""Assemble Test-1 vintages from harvester marks + slow-rolled live inputs.

The factor->engine glue (DATA_CONTRACT_TEST1.md). Reads the harvester's resolved
marks (`_factor_marks.json`, exported from the .venv310 harvester) and writes a
`backtest/vintages/<YYYY-Qn>/` tree the engine can value as-of that quarter.

What's real vs slow-rolled in THIS pass (honest, partial MVP):
  * vessel_value_curves  — REAL, vintaged from the harvester (the win): class
    rename (Capesize->Cape, Kamsarmax->Pana, Ultramax->Supra-Ultra), resale->
    newbuild proxy, musd*1e6. MERGED over the live curves so classes the
    harvester doesn't cover (LR2, LNGC, ...) keep live marks and don't break NAV.
  * current_price        — REAL, vintaged: Sharadar raw close at the quarter-end.
  * scenario_inputs      — SYNTHESISED (the neutral mean-reversion forward,
    DATA_CONTRACT_TEST1.md): one neutral scenario per sector whose per-class
    forward glides the VINTAGED 12-month TC (xclusiv 1y-T/C prose) toward the
    through-cycle TC mean (±25% band). TC-consistent with the cycle-anchor means.
    Coverage: 2024-Q3 / 2025-Q1 / 2025-Q2 carry full tanker TC; xclusiv dropped
    the 1y-T/C prose after 2025-Q2, so 2025-Q3/Q4 fall back to the through-cycle
    mean (neutral, not spot).
  * balance-sheet CORE   — REAL, vintaged: cash, total_debt (Sharadar
    LongTermDebtNoncurrent + DebtCurrent) and diluted shares, point-in-time
    (datekey <= quarter-end). The shipping-specific lines (working capital,
    newbuild commitments, leases) stay slow-rolled from live.
  * FFA / means / fleet / cost / dividend — HELD from live (slow-roll).

=> The EV% is driven by REAL vintaged NAV marks + a REAL vintaged 12M-TC-anchored
forward + REAL vintaged price + point-in-time debt & share count. A legitimate
(small-n) read; residual held legs are cash, working capital, fleet ages, and the
newbuild/lease lines.

CLI: PYTHONPATH=. .venv/bin/python -m backtest.build_vintage 2024-Q3 2025-Q1 ...
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
from crude_tanker_fv.scenarios import quarter_keys, strip_start_from_asof  # noqa: E402

from .loaders_sharadar import SECTOR_OF, cache_dir  # noqa: E402

LIVE = REPO / "inputs"
VINTAGES = Path(__file__).resolve().parent / "vintages"
MARKS_JSON = VINTAGES / "_factor_marks.json"
_QEND = {1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)}

# harvester canonical class -> engine class
CLASS_MAP = {
    "Capesize": "Cape", "Kamsarmax": "Pana", "Panamax": "Pana",
    "Ultramax": "Supra-Ultra", "Supramax": "Supra-Ultra",
    "Handy": "Handysize", "Handysize": "Handysize",
    "VLCC": "VLCC", "Suezmax": "Suezmax", "Aframax": "Aframax",
    "MR": "MR", "MR2": "MR", "LR2": "LR2", "LR1": "LR1",
}
# harvester anchor -> engine curve key (resale is the newbuild proxy)
ANCHOR_MAP = {"newbuild": "newbuild", "resale": "newbuild",
              "five_year": "five_year_benchmark", "ten_year": "ten_year_benchmark",
              "scrap": "scrap_25yr"}


def _qkey(asof: str) -> str:                       # "2024-Q3" -> "2024Q3"
    return asof.replace("-", "")


def _qend(asof: str) -> dt.date:
    y, q = asof.split("-Q")
    m, d = _QEND[int(q)]
    return dt.date(int(y), m, d)


def factor_vessel_values(asof: str) -> dict:
    """engine_class -> {engine curve key: $value} from the harvester marks."""
    qk = _qkey(asof)
    marks = [m for m in json.loads(MARKS_JSON.read_text())
             if m["quarter"] == qk and m["field"] == "vessel_value"]
    out: dict[str, dict] = {}
    # explicit newbuild beats the resale proxy; otherwise first value per (class, key)
    for prefer in ("newbuild", "resale", "five_year", "ten_year", "scrap"):
        for m in marks:
            if m["anchor"] != prefer or m["value"] is None:
                continue
            ec = CLASS_MAP.get(m["vessel_class"])
            if not ec:
                continue
            cur = out.setdefault(ec, {})
            key = ANCHOR_MAP[prefer]
            cur.setdefault(key, float(m["value"]) * 1e6)
    return out


def merged_vessel_curves(asof: str) -> dict:
    """Live vessel_value_curves with the covered classes overwritten by harvester
    marks (dwt + uncovered classes preserved)."""
    live = yaml.safe_load((LIVE / "market_data" / "vessel_value_curves.yaml").read_text())
    classes = live["classes"]
    for ecls, curve in factor_vessel_values(asof).items():
        if ecls in classes:
            classes[ecls].update(curve)          # keep dwt + anchors the harvester lacks
        else:
            classes[ecls] = curve
    return live


def raw_close_at(ticker: str, asof: str) -> float | None:
    """Sharadar raw close at/<= the quarter-end (the EV% denominator)."""
    p = cache_dir() / f"prices_{ticker}.csv"
    if not p.exists():
        return None
    qend, best = _qend(asof), None
    with open(p) as fh:
        for row in csv.DictReader(fh):
            d = dt.date.fromisoformat(row["date"])
            if d > qend:
                break
            if row.get("close"):
                best = float(row["close"])
    return best


def _sharadar_field_at(ticker: str, field: str, asof: str):
    """Latest ARY value of `field` with filed-date <= the quarter-end (no
    look-ahead). Returns (period_end, value) or None."""
    sec = cache_dir() / f"sec_{ticker}.csv"
    if not sec.exists():
        return None
    qend = _qend(asof)
    avail = []
    with open(sec) as fh:
        for row in csv.DictReader(fh):
            if row.get("field") != field or row.get("dimension") != "ARY":
                continue
            try:
                filed = dt.date.fromisoformat(row["filed"])
                val = float(row["value"])
            except (ValueError, KeyError):
                continue
            if filed <= qend:
                avail.append((filed, row["period_end"], val))
    if not avail:
        return None
    avail.sort()
    return avail[-1][1], avail[-1][2]


def vintaged_bs_core(ticker: str, asof: str) -> dict:
    """Point-in-time balance-sheet core from Sharadar SF1 ARY (datekey<=q-end):
    cash, total_debt (LongTermDebtNoncurrent + DebtCurrent) and diluted shares.
    The shipping-specific lines (working capital, newbuild commitments, leases)
    stay slow-rolled from live."""
    out: dict = {}
    sh = _sharadar_field_at(ticker, "EntityCommonStockSharesOutstanding", asof)
    if sh:
        out["diluted_shares_outstanding"] = round(sh[1])
    cash = _sharadar_field_at(ticker, "CashAndCashEquivalentsAtCarryingValue", asof)
    if cash:
        out["cash_and_equivalents"] = cash[1]
    ltd = _sharadar_field_at(ticker, "LongTermDebtNoncurrent", asof)
    dc = _sharadar_field_at(ticker, "DebtCurrent", asof)
    if ltd:
        out["total_debt"] = ltd[1] + (dc[1] if dc and dc[0] == ltd[0] else 0.0)
    return out


# scenario-class key (== cycle_anchors key) -> harvester vessel_class
HARV_TC_KEY = {
    "vlcc": "VLCC", "suezmax": "Suezmax", "aframax_dirty": "Aframax", "lr2_clean": "LR2",
    "mr": "MR", "mr_clean": "MR",
    "cape": "Capesize", "pana": "Kamsarmax", "supra_ultra": "Ultramax",
}


def vintaged_tc(asof: str) -> dict:
    """{harvester_class: 12-month TC} for this quarter (xclusiv 1y-T/C prose)."""
    qk = _qkey(asof)
    return {m["vessel_class"]: float(m["value"]) for m in json.loads(MARKS_JSON.read_text())
            if m["quarter"] == qk and m["field"] == "twelve_month_tc" and m["value"] is not None}


def _synth_curve(anchor: float, mean: float, vk: list[str]) -> dict:
    """A neutral mean-reversion forward: glide from the as-of rate (`anchor`)
    toward the through-cycle `mean` over the horizon; ±25% low/high band."""
    h = len(vk)
    out = {}
    for i, q in enumerate(vk):
        base = anchor + (mean - anchor) * min(1.0, (i + 1) / h)
        out[q] = [round(base * 0.75), round(base), round(base * 1.25)]
    return out


def synthesize_scenarios(doc: dict, asof: str) -> dict:
    """Replace each sector's scenarios with ONE neutral scenario (weight 1.0)
    whose per-class forward mean-reverts the vintaged **12-month TC** toward the
    through-cycle TC mean (±25% band) — DATA_CONTRACT_TEST1.md's neutral forward.

    Anchored on 12M TC (xclusiv 1y-T/C prose), which is TC-consistent with the
    cycle-anchor means (vs the earlier spot anchor). Where a class has no
    vintaged TC for the quarter (xclusiv dropped the 1y-T/C prose after 2025-Q2,
    so 2025-Q3/Q4 have none), its forward sits flat at the through-cycle mean
    (neutral) — NOT spot, to avoid a TC-vs-spot level confound across quarters."""
    sq, sy = strip_start_from_asof(asof)
    tc = vintaged_tc(asof)
    for sec in doc["sectors"].values():
        vk = quarter_keys(int(sec.get("strip_horizon", 8)), sq, sy)
        scen = {"weight": 1.0, "description": "neutral mean-reversion (Test-1 vintage)"}
        for key, a in sec.get("cycle_anchors", {}).items():
            mean = float(a["ten_year_mean"])
            anchor = tc.get(HARV_TC_KEY.get(key, ""), mean)
            scen[key] = _synth_curve(anchor, mean, vk)
        sec["scenarios"] = {"neutral": scen}
    return doc


def assemble_vintage(asof: str, tickers: list[str]) -> Path:
    vd = VINTAGES / asof
    md = vd / "market_data"
    md.mkdir(parents=True, exist_ok=True)

    # market data: copy live, then overwrite vessel_value_curves with the merge
    for f in ("twelve_month_tc.yaml", "spot_tce.yaml", "ffa_forward_curve.yaml",
              "historical_tce_means.yaml"):
        shutil.copy(LIVE / "market_data" / f, md / f)
    shutil.copytree(LIVE / "market_data" / "transactions", md / "transactions",
                    dirs_exist_ok=True)
    (md / "vessel_value_curves.yaml").write_text(
        yaml.safe_dump(merged_vessel_curves(asof), sort_keys=False))

    # scenario_inputs: neutral mean-reversion forward synthesised from vintaged spot
    doc = yaml.safe_load((LIVE / "scenario_inputs.yaml").read_text())
    (vd / "scenario_inputs.yaml").write_text(
        yaml.safe_dump(synthesize_scenarios(doc, asof), sort_keys=False))

    # per-ticker: fleet/cost/dividend held (no quarter in name); balance sheet renamed
    for sub in ("fleet_manifests", "cost_structures", "dividend_policies"):
        (vd / sub).mkdir(exist_ok=True)
    (vd / "balance_sheets").mkdir(exist_ok=True)
    watch = yaml.safe_load((LIVE / "watchlist.yaml").read_text())
    out_watch: dict = {}
    for t in tickers:
        tl = t.lower()
        for sub in ("fleet_manifests", "cost_structures", "dividend_policies"):
            src = LIVE / sub / f"{tl}.yaml"
            if src.exists():
                shutil.copy(src, vd / sub / f"{tl}.yaml")
        bs_files = sorted((LIVE / "balance_sheets").glob(f"{tl}_*.yaml"))
        if bs_files:
            bs = yaml.safe_load(bs_files[-1].read_text())     # slow-roll base
            bs.update(vintaged_bs_core(t, asof))              # overwrite debt + shares, point-in-time
            bs["quarter"] = asof
            (vd / "balance_sheets" / f"{tl}_{asof}.yaml").write_text(
                yaml.safe_dump(bs, sort_keys=False))
        price = raw_close_at(t, asof)
        if price is None or t not in watch:
            continue
        out_watch[t] = {**watch[t], "current_price": round(price, 2),
                        "analyst_target": round(price, 2)}
    (vd / "watchlist.yaml").write_text(yaml.safe_dump(out_watch, sort_keys=False))
    return vd


def main(argv: list[str]) -> int:
    if not MARKS_JSON.exists():
        print(f"{MARKS_JSON} missing — export it from the harvester first.")
        return 2
    quarters = argv or ["2024-Q3", "2025-Q1", "2025-Q2", "2025-Q3", "2025-Q4"]
    tickers = [t for t in SECTOR_OF if (cache_dir() / f"prices_{t}.csv").exists()]
    for q in quarters:
        vd = assemble_vintage(q, tickers)
        nv = len(yaml.safe_load((vd / "watchlist.yaml").read_text()))
        print(f"  {q}: vintage assembled ({nv} names) -> {vd.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
