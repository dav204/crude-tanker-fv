"""Pull quarterly (ARQ) balance-sheet core from Sharadar SF1 -> _bs_quarterly.csv.

The factor-portfolio cache holds only ANNUAL (ARY) balance-sheet fields, so a
mid-year vintage uses a balance sheet up to ~12 months stale. This pulls the
quarterly grain (cash / total debt / shares, point-in-time by `datekey`) so
`build_vintage.vintaged_bs_core` can prefer it. One-off enhancement; the output
CSV is gitignored (regenerable).

Run (needs the owner's Sharadar key + the factor-portfolio fetcher, 3.10+ env):
  set -a; source ~/.config/factor-portfolio.env; set +a
  PYTHONPATH=/Users/dan_personal/Projects/factor-portfolio/src \
      .venv310/bin/python backtest/pull_bs_quarterly.py
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, "/Users/dan_personal/Projects/factor-portfolio/src")
from factor_portfolio.fetch import sharadar as sh   # noqa: E402

NAMES = ["DHT", "FRO", "ECO", "INSW", "TNK", "NAT", "TEN", "STNG", "HAFN",
         "TRMD", "ASC", "FLNG", "CCEC", "SBLK", "GNK", "CMDB", "GSL"]
OUT = Path(__file__).resolve().parent / "vintages" / "_bs_quarterly.csv"
COLS = ["ticker", "datekey", "reportperiod", "cashneq", "debt", "sharesbas", "marketcap", "price"]


def main() -> int:
    rows = []
    for t in NAMES:
        data = sh._get("SF1", ticker=t, dimension="ARQ", columns=COLS)
        n = 0
        for r in data:
            filed, pe = r.get("datekey"), r.get("reportperiod")
            if not filed or not pe:
                continue
            shares = r.get("sharesbas")
            if not shares and r.get("marketcap") and r.get("price"):
                shares = r["marketcap"] / r["price"]
            rows.append({"ticker": t, "period_end": pe, "filed": filed,
                         "cash": r.get("cashneq"), "total_debt": r.get("debt"),
                         "shares": round(shares) if shares else None})
            n += 1
        print(f"  {t}: {n} ARQ rows")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["ticker", "period_end", "filed", "cash", "total_debt", "shares"])
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} ARQ BS rows -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
