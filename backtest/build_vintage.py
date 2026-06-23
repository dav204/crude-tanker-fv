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
  * scenario_inputs      — live curves RE-KEYED to the vintage's strip quarters
    (so the as-of routing fires). Values held = the neutral mean-reversion forward
    is NOT yet synthesised, so the scenario LEVELS are live; flagged.
  * twelve_month_tc / spot / FFA / means / fleet / cost / dividend / balance sheet
                         — HELD from live (slow-roll). The harvester TC is still
    unreliable (Allied bug), so TC stays live this pass.

=> The resulting EV% is a PLUMBING-VALIDATION read (real vintaged NAV marks, but
held TC/scenario-levels/BS), not yet a valid Test-1 result. It proves the chain
end-to-end and surfaces glue/assembly issues. Marked as such in the report.

CLI: PYTHONPATH=. .venv/bin/python -m backtest.build_vintage 2024-Q3 2025-Q1 ...
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import re
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


def rekey_scenarios(doc: dict, asof: str) -> dict:
    """Relabel each scenario curve's quarter keys to the vintage's strip quarters
    (positional) so run_scenarios(asof_quarter) routes; values held."""
    sq, sy = strip_start_from_asof(asof)
    for sec in doc["sectors"].values():
        vk = quarter_keys(int(sec.get("strip_horizon", 8)), sq, sy)
        for scen in sec.get("scenarios", {}).values():
            for k, v in list(scen.items()):
                if isinstance(v, dict) and v and all(re.match(r"q[1-4]_\d{4}", kk) for kk in v):
                    vals = list(v.values())
                    scen[k] = {vk[i]: vals[i] for i in range(min(len(vk), len(vals)))}
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

    # scenario_inputs: re-keyed to this vintage's strip quarters
    doc = yaml.safe_load((LIVE / "scenario_inputs.yaml").read_text())
    (vd / "scenario_inputs.yaml").write_text(
        yaml.safe_dump(rekey_scenarios(doc, asof), sort_keys=False))

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
        bs = sorted((LIVE / "balance_sheets").glob(f"{tl}_*.yaml"))
        if bs:
            shutil.copy(bs[-1], vd / "balance_sheets" / f"{tl}_{asof}.yaml")
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
