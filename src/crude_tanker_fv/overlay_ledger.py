"""Overlay ledger — the single registry of qualitative adjustments (§16).

The actionable view of a name = pipeline FV + the composition of active
overlays (§12 dividend-window, §14.4 MEG-lag, §14.6 attenuations, §15
haircuts, marks-vintage tilts). Each is documented in its own section;
this module renders the per-name composition so two readers land on the
same number and decision logs can cite it:

    "tool FV $X; active overlays per ledger net to ~$Y; acted at $Z."

Sources:
  - inputs/overlays.yaml — curated rows (everything except §15 and §12.6).
  - inputs/balance_sheets/*_<quarter>.yaml — §15 rows auto-populate from
    governance_discount_pct > 0 (the knob that actually drives the
    pipeline), latest quarter per ticker.
  - the §12.5–§12.7 dividend-window test — §12.6 rows auto-populate from the
    COMPUTED classification (`dividend_window.build_rows`), so the ledger row
    can never contradict the diagnostic (closes audit E-2 "ledger is
    documentation, not a control" for this overlay type — the prior hand-written
    NAT "treat FV as a NAV floor" §12 row was the exact drift this removes).

CLI:
    python -m crude_tanker_fv.overlay_ledger              # latest quarter
    python -m crude_tanker_fv.overlay_ledger --quarter 2026-Q1
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OVERLAYS_YAML = ROOT / "inputs" / "overlays.yaml"
BALANCE_SHEETS = ROOT / "inputs" / "balance_sheets"
OUT_MD = ROOT / "outputs" / "overlay_ledger.md"

_BS_NAME = re.compile(r"^([a-z]+)_(\d{4}-Q[1-4])\.yaml$")
_ARROW = {"up": "↑", "down": "↓", "none": "·"}


def curated_rows() -> list[dict]:
    doc = yaml.safe_load(OVERLAYS_YAML.read_text())
    return doc["overlays"]


def _latest_quarter() -> str:
    quarters = [m.group(2) for p in BALANCE_SHEETS.glob("*.yaml")
                if (m := _BS_NAME.match(p.name))]
    return max(quarters) if quarters else "2026-Q1"


def governance_rows() -> list[dict]:
    """§15 rows from the latest balance sheet per ticker."""
    latest: dict[str, tuple[str, Path]] = {}
    for p in BALANCE_SHEETS.glob("*.yaml"):
        m = _BS_NAME.match(p.name)
        if not m:
            continue
        ticker, quarter = m.group(1).upper(), m.group(2)
        if ticker not in latest or quarter > latest[ticker][0]:
            latest[ticker] = (quarter, p)
    rows = []
    for ticker, (quarter, p) in sorted(latest.items()):
        pct = yaml.safe_load(p.read_text()).get("governance_discount_pct") or 0
        if pct > 0:
            rows.append({
                "name": ticker,
                "overlay_id": "§15",
                "direction": "down",
                "magnitude": f"{pct:.0%} haircut (blend layer + strip terminal; NAV untouched)",
                "applied": "per decision log",
                "retire_trigger": f"reopen triggers in decisions/{ticker.lower()}_log.md",
                "note": f"Auto-populated from balance_sheets/{p.name} governance_discount_pct.",
                "_auto": True,
            })
    return rows


def dividend_window_overlay(r) -> dict | None:
    """Map one §12 dividend-window classification (a DividendWindowRow) to a
    ledger row. Only GATED names carry a §12.6 overlay; a gate-pass that resolves
    to TRIM-stands is recorded as a *neutral* row (no FV change) so the ledger
    documents that the override was evaluated and explicitly did NOT fire."""
    if not r.gated:
        return None
    qs = ">strip" if r.q_star is None else f"{r.q_star:.0f}"
    if r.classification == "undervaluation":
        direction = "up"
        magnitude = (f"§12 undervaluation — premium rate-supported "
                     f"(Q*={qs} ≤ H={r.supported_horizon:.1f}); floor framing applies")
    else:  # TRIM-stands (value trap)
        direction = "none"
        magnitude = (f"TRIM stands (value trap) — premium NOT rate-supported "
                     f"(Q*={qs} > H={r.supported_horizon:.1f}); no floor, no FV change")
    return {
        "name": r.ticker,
        "overlay_id": "§12.6",
        "direction": direction,
        "magnitude": magnitude,
        "applied": "diagnostic-only (no FV change)",
        "retire_trigger": ("reclassifies to undervaluation if Q* ≤ H — FFA horizon extends "
                           "above the through-cycle mean, or the premium compresses"),
        "note": (f"Auto-derived from the §12.5–§12.7 dividend-window test "
                 f"(outputs/dividend_window_test.md): gated at {r.premium_x:.2f}× price/NAV, "
                 f"payout {r.payout_ratio:.0%}, cycle {r.cycle_position:.2f}×."),
        "_auto": True,
    }


def dividend_window_rows(quarter: str) -> list[dict]:
    """§12.6 rows from the computed dividend-window classification (gated names)."""
    from .dividend_window import build_rows
    rows = []
    for r in build_rows(quarter):
        overlay = dividend_window_overlay(r)
        if overlay is not None:
            rows.append(overlay)
    return rows


def render(rows: list[dict]) -> str:
    by_name: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_name[r["name"]].append(r)
    lines = [
        "# Overlay ledger",
        "",
        "Single registry of active qualitative overlays (METHODOLOGY §16).",
        "Auto-generated — edit `inputs/overlays.yaml` (curated rows), the",
        "balance-sheet `governance_discount_pct` (§15 rows), or the §12 inputs",
        "(§12.6 rows auto-derive from the dividend-window test), then re-render.",
        "",
        "| Name | Overlay | Dir | Magnitude | Applied | Retire trigger |",
        "|---|---|:---:|---|---|---|",
    ]
    for name in sorted(by_name, key=lambda n: (len(n) > 4, n)):  # tickers first, sector rows last
        for r in sorted(by_name[name], key=lambda r: r["overlay_id"]):
            arrow = _ARROW.get(r["direction"], "·")
            lines.append(
                f"| {name} | {r['overlay_id']} | {arrow} | {r['magnitude']} "
                f"| {r['applied']} | {r['retire_trigger']} |"
            )
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    for name in sorted(by_name, key=lambda n: (len(n) > 4, n)):
        for r in by_name[name]:
            if r.get("note"):
                lines.append(f"- **{name} {r['overlay_id']}** — {r['note']}")
    lines.append("")
    return "\n".join(lines)


def main(quarter: str | None = None) -> None:
    quarter = quarter or _latest_quarter()
    rows = curated_rows() + governance_rows() + dividend_window_rows(quarter)
    OUT_MD.write_text(render(rows))
    auto = sum(1 for r in rows if r.get("_auto"))
    print(f"overlay ledger ({quarter}): {len(rows)} rows ({auto} auto §15/§12.6) -> {OUT_MD}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(prog="crude_tanker_fv.overlay_ledger")
    ap.add_argument("--quarter", help="quarter for the §12.6 dividend-window rows (default: latest)")
    main(ap.parse_args().quarter)
