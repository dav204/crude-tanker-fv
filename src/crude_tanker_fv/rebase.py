"""Watchlist pair rebase, anchor-preserving (2026-09-13 — the lane the owner's permission
change unlocked; the rule is the 2026-06-10 TEN precedent, applied by hand five times in the
last 60 days).

    python -m crude_tanker_fv.rebase TICKER            # draft: inputs/watchlist_rebase_<date>.yaml.draft
    python -m crude_tanker_fv.rebase TICKER --apply    # edit inputs/watchlist.yaml in place

A watchlist price never moves without consensus_pnav and consensus_fwd_pe from the SAME
vintage (CLAUDE.md: broker NAV = price/pnav would silently drift). The anchors of record are
preserved: implied broker NAV = old price / old pnav, the EPS basis = old price / old fwd_pe;
the new ratios are re-derived from the new close on those anchors. The close comes from
prices_daily.yaml (USD, already FX-converted at the daily's rate — never a price typed from
prose); as_of becomes the close's date. Edits are TEXTUAL: the value token on each of the four
lines is replaced and every comment survives; a dated marker is appended to the as_of line.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

import yaml

from .loaders import INPUTS_DIR

PRICE_FRESH_DAYS = 5


def _price(ticker: str, inputs_dir: Path, today: date | None = None) -> tuple[float, str]:
    d = yaml.safe_load((inputs_dir / "market_data" / "prices_daily.yaml").read_text()) or {}
    row = (d.get("prices") or {}).get(ticker)
    if not row or row.get("price") in (None, 0):
        raise SystemExit(f"no fresh price for {ticker} in prices_daily.yaml")
    asof = str(row.get("asof", ""))[:10]
    if not asof:
        raise SystemExit(f"prices_daily.yaml row for {ticker} carries no asof")
    if ((today or date.today()) - date.fromisoformat(asof)).days > PRICE_FRESH_DAYS:
        raise SystemExit(f"price vintage for {ticker} is {asof}: older than {PRICE_FRESH_DAYS} days — refresh first")
    if row.get("price_review"):
        raise SystemExit(f"{ticker} quote is flagged for review ({row.get('price_review')}); rebase by hand")
    return float(row["price"]), asof


def _block(text: str, ticker: str) -> tuple[int, int]:
    m = re.search(rf"^{re.escape(ticker)}:\n", text, flags=re.M)
    if not m:
        raise SystemExit(f"{ticker} not in watchlist.yaml")
    start = m.start()
    nxt = re.search(r"^[A-Z0-9]+:\n", text[m.end():], flags=re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return start, end


def _value(block: str, key: str) -> float | None:
    m = re.search(rf"^  {key}:\s*([-\d.]+)", block, flags=re.M)
    return float(m.group(1)) if m else None


def compute(ticker: str, inputs_dir: Path = INPUTS_DIR, *, price: float | None = None,
            asof: str | None = None, today: date | None = None) -> dict:
    text = (inputs_dir / "watchlist.yaml").read_text()
    s, e = _block(text, ticker)
    block = text[s:e]
    old_price = _value(block, "current_price")
    old_pnav = _value(block, "consensus_pnav")
    old_pe = _value(block, "consensus_fwd_pe")
    if old_price is None:
        raise SystemExit(f"{ticker}: no numeric current_price to rebase from")
    if price is None or asof is None:
        price, asof = _price(ticker, inputs_dir, today)
    out = {"ticker": ticker, "old_price": old_price, "price": round(price, 2), "as_of": asof,
           "implied_broker_nav": None, "eps_basis": None, "pnav": None, "fwd_pe": None}
    if old_pnav:
        out["implied_broker_nav"] = round(old_price / old_pnav, 2)
        out["pnav"] = round(price / (old_price / old_pnav), 2)
    if old_pe:
        out["eps_basis"] = round(old_price / old_pe, 2)
        out["fwd_pe"] = round(price / (old_price / old_pe), 1)
    return out


def apply(ticker: str, inputs_dir: Path = INPUTS_DIR, *, values: dict | None = None,
          today: date | None = None) -> dict:
    v = values or compute(ticker, inputs_dir)
    path = inputs_dir / "watchlist.yaml"
    text = path.read_text()
    s, e = _block(text, ticker)
    block = text[s:e]
    stamp = (today or date.today()).isoformat()

    def swap(b: str, key: str, new) -> str:
        if new is None:
            return b
        return re.sub(rf"^(  {key}:\s*)[-\d.]+", lambda m: f"{m.group(1)}{new}", b, count=1, flags=re.M)

    block = swap(block, "current_price", f"{v['price']:.2f}")
    block = swap(block, "consensus_pnav", f"{v['pnav']:.2f}" if v["pnav"] is not None else None)
    block = swap(block, "consensus_fwd_pe", f"{v['fwd_pe']:.1f}" if v["fwd_pe"] is not None else None)
    marker = (f"  # rebased {stamp} by crude_tanker_fv.rebase, anchor-preserving: implied broker NAV "
              f"{v['implied_broker_nav']} / EPS basis {v['eps_basis']} carried; one vintage {v['as_of']}")
    if re.search(r"^  as_of:", block, flags=re.M):
        block = re.sub(r"^  as_of:\s*\S+", f"  as_of: {v['as_of']}", block, count=1, flags=re.M)
        block = re.sub(r"(^  as_of:[^\n]*\n)", lambda m: m.group(1) + marker + "\n", block, count=1, flags=re.M)
    else:
        block = block.rstrip("\n") + f"\n  as_of: {v['as_of']}\n{marker}\n"
    path.write_text(text[:s] + block + text[e:])
    return v


def draft_path(ticker: str, inputs_dir: Path = INPUTS_DIR, today: date | None = None) -> Path:
    return inputs_dir / f"watchlist_rebase_{(today or date.today()).isoformat()}_{ticker.lower()}.yaml.draft"


def write_draft(ticker: str, inputs_dir: Path = INPUTS_DIR, *, values: dict | None = None,
                today: date | None = None) -> Path:
    v = values or compute(ticker, inputs_dir)
    p = draft_path(ticker, inputs_dir, today)
    p.write_text("# NOT-APPLIED — watchlist pair rebase draft (crude_tanker_fv.rebase); the promote consumes + deletes it\n"
                 + yaml.safe_dump({ticker: {"current_price": v["price"], "consensus_pnav": v["pnav"],
                                            "consensus_fwd_pe": v["fwd_pe"], "as_of": v["as_of"],
                                            "anchors": {"implied_broker_nav": v["implied_broker_nav"],
                                                        "eps_basis": v["eps_basis"], "old_price": v["old_price"]}}},
                                  sort_keys=False))
    return p


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="anchor-preserving watchlist pair rebase")
    ap.add_argument("ticker")
    ap.add_argument("--apply", action="store_true", help="edit inputs/watchlist.yaml (default: write a .draft)")
    args = ap.parse_args(argv)
    t = args.ticker.upper()
    v = compute(t)
    print(f"{t}: {v['old_price']} -> {v['price']} (as_of {v['as_of']}); pnav {v['pnav']} on implied NAV "
          f"{v['implied_broker_nav']}; fwd_pe {v['fwd_pe']} on EPS basis {v['eps_basis']}")
    if args.apply:
        apply(t, values=v)
        print(f"APPLIED to inputs/watchlist.yaml ({t} block; comments kept)")
    else:
        print(f"DRAFT {write_draft(t, values=v)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
