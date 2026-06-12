"""Overlay ledger — the single registry of qualitative adjustments (§16).

The actionable view of a name = pipeline FV + the composition of active
overlays (§12 dividend-window, §14.4 MEG-lag, §14.6 attenuations, §15
haircuts, marks-vintage tilts). Each is documented in its own section;
this module renders the per-name composition so two readers land on the
same number and decision logs can cite it:

    "tool FV $X; active overlays per ledger net to ~$Y; acted at $Z."

Sources:
  - inputs/overlays.yaml — curated rows (everything except §15).
  - inputs/balance_sheets/*_<quarter>.yaml — §15 rows auto-populate from
    governance_discount_pct > 0 (the knob that actually drives the
    pipeline), latest quarter per ticker.

CLI:
    python -m crude_tanker_fv.overlay_ledger          # writes outputs/overlay_ledger.md
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OVERLAYS_YAML = ROOT / "inputs" / "overlays.yaml"
BALANCE_SHEETS = ROOT / "inputs" / "balance_sheets"
OUT_MD = ROOT / "outputs" / "overlay_ledger.md"

_BS_NAME = re.compile(r"^([a-z]+)_(\d{4}-Q[1-4])\.yaml$")


def curated_rows() -> list[dict]:
    doc = yaml.safe_load(OVERLAYS_YAML.read_text())
    return doc["overlays"]


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


def render(rows: list[dict]) -> str:
    by_name: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_name[r["name"]].append(r)
    lines = [
        "# Overlay ledger",
        "",
        "Single registry of active qualitative overlays (METHODOLOGY §16).",
        "Auto-generated — edit `inputs/overlays.yaml` (curated rows) or the",
        "balance-sheet `governance_discount_pct` (§15 rows), then re-render.",
        "",
        "| Name | Overlay | Dir | Magnitude | Applied | Retire trigger |",
        "|---|---|:---:|---|---|---|",
    ]
    for name in sorted(by_name, key=lambda n: (len(n) > 4, n)):  # tickers first, sector rows last
        for r in sorted(by_name[name], key=lambda r: r["overlay_id"]):
            arrow = "↑" if r["direction"] == "up" else "↓"
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


def main() -> None:
    rows = curated_rows() + governance_rows()
    OUT_MD.write_text(render(rows))
    auto = sum(1 for r in rows if r.get("_auto"))
    print(f"overlay ledger: {len(rows)} rows ({auto} auto-§15) -> {OUT_MD}")


if __name__ == "__main__":
    main()
