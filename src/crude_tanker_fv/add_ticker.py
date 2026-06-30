"""Scaffold the YAML stubs, test file, and decision-log entry for a new ticker.

Removes the blank-page problem: every onboarding from here starts from a
known-good shape (METHODOLOGY §8.1) so the agent / user can focus on data
assembly, not file creation.

Usage:
    python -m crude_tanker_fv.add_ticker SBLK --sector dry_bulk
    python -m crude_tanker_fv.add_ticker GASS --sector lpg --quarter 2026-Q2
    python -m crude_tanker_fv.add_ticker DAC --sector containerships --dry-run

What it creates:
    inputs/fleet_manifests/<ticker>.yaml
    inputs/balance_sheets/<ticker>_<quarter>.yaml
    inputs/cost_structures/<ticker>.yaml
    inputs/dividend_policies/<ticker>.yaml
    tests/test_<ticker>.py            (pytest.mark.skip until data filled in)
    decisions/<ticker>_log.md         (header + intro; pipeline auto-prepends entries)

Appends to:
    inputs/watchlist.yaml             (text append — preserves comments)

What it does NOT do:
    - Pull IR PDFs or real data (next step for the agent/user).
    - Add the ticker to scenario_inputs.yaml for new sectors (methodology
      decision doc must come first — §11.4 / CLAUDE.md).
    - Run the pipeline.

Refuses to overwrite existing files. Use --force to override (rare; mostly
for re-scaffolding after a delete).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUTS = ROOT / "inputs"
TESTS = ROOT / "tests"
DECISIONS = ROOT / "decisions"
STATE_PATH = ROOT / "state" / "last_run.json"

# Sectors the scaffold offers as `--sector` choices. A sector is "live" if it
# actually has a `sectors.<name>` block in inputs/scenario_inputs.yaml — that's
# the canonical source of truth (looked up at runtime; survives sector landings
# without code edits). Sectors in this list that aren't yet in the YAML get a
# warning at scaffold time pointing the user at METHODOLOGY §11.x.
KNOWN_SECTORS = ("crude", "product", "lng", "dry_bulk",
                 "containerships", "lpg", "offshore_drilling")

# Sector-appropriate vessel class hints. Keep crude as the historical default
# (matches what the _template.yaml files ship with) so existing sectors get
# the same shape they always have.
SECTOR_CLASSES: dict[str, list[str]] = {
    "crude": ["VLCC", "Suezmax", "Aframax"],
    "product": ["MR", "LR1", "LR2", "Handysize", "Handymax"],
    "lng": ["LNGC", "MGC"],
    "dry_bulk": ["Cape", "Pana", "Supra", "Ultra"],
    "containerships": ["Containership"],
    "lpg": ["VLGC", "MGC"],
    "offshore_drilling": ["Drillship", "Semi", "Jackup"],
}


def _live_sectors() -> set[str]:
    """Return the set of sectors with a sectors.<name> block in
    inputs/scenario_inputs.yaml. Single source of truth — no hardcoded list."""
    import yaml
    path = INPUTS / "scenario_inputs.yaml"
    try:
        doc = yaml.safe_load(path.read_text())
        return set((doc.get("sectors") or {}).keys())
    except Exception:
        # Fallback to historical set if the file is unreadable for any reason.
        return {"crude", "product", "lng"}


def _quarter_from_state() -> str:
    """Default quarter is the last pipeline run's quarter; fall back to 2026-Q1."""
    if STATE_PATH.exists():
        try:
            q = json.loads(STATE_PATH.read_text()).get("quarter")
            if q:
                return q
        except Exception:
            pass
    return "2026-Q1"


def _read_template(path: Path) -> str:
    if not path.exists():
        sys.exit(f"Template missing: {path}")
    return path.read_text()


def _fleet_manifest_stub(ticker: str, quarter: str, classes: list[str]) -> str:
    classes_yaml = "\n".join(f"  {c}: null" for c in classes)
    summary_yaml = "\n".join(f"  {c}_count: null" for c in classes)
    return f"""# {ticker} fleet manifest — METHODOLOGY.md section 4.1
# FIXME: source from latest IR fleet page + cross-check against quarter-end
# report counts (CLAUDE.md: trust the report at quarter-end, not the live page).
ticker: {ticker}
report_date: {quarter}
vessels:
  # FIXME: one entry per vessel. Example:
  - id: PLACEHOLDER_001
    class: {classes[0]}
    dwt: null           # e.g. 300000
    age: null           # years (= 2026 - year built)
    scrubber: null      # true | false
    eco: null           # true | false (post-2014 fuel-efficient design)
    charter_status: null  # spot | time_charter
    charter_rate: null    # USD/day if time_charter, else null
    charter_end: null     # ISO date if time_charter, else null
spot_coverage_pct:      # share of fleet on spot, by class (0.0–1.0)
{classes_yaml}
fleet_summary:          # convenience totals, cross-check against vessels list
{summary_yaml}
  avg_age_{classes[0]}: null
"""


def _balance_sheet_stub(ticker: str, quarter: str) -> str:
    template = _read_template(INPUTS / "balance_sheets" / "_template.yaml")
    return (
        template
        .replace("ticker: null                      # e.g. DHT",
                 f"ticker: {ticker}")
        .replace("quarter: null                     # e.g. dht_2026-Q1.yaml",
                 f"quarter: {quarter}")
        .replace("quarter: null                     # e.g. 2026-Q1",
                 f"quarter: {quarter}")
        # Some templates may use a different placeholder — best-effort
        .replace("quarter: null", f"quarter: {quarter}")
    )


def _cost_structure_stub(ticker: str, classes: list[str]) -> str:
    classes_yaml = "\n".join(f"  {c}: null" for c in classes)
    return f"""# {ticker} cost structure — METHODOLOGY.md section 4.4
# FIXME: derive from latest quarterly results (USD).
ticker: {ticker}

opex_per_day:                 # daily operating cost per vessel, by class
{classes_yaml}

annual_G_and_A: null
annual_interest_expense: null
effective_tax_rate: null      # e.g. 0.02 (tonnage-tax regimes; verify per company)
"""


def _dividend_policy_stub(ticker: str) -> str:
    return f"""# {ticker} dividend policy — METHODOLOGY.md section 4.3
# FIXME: source from latest capital allocation policy / earnings release.
# Known v1 policies (METHODOLOGY §4.3):
#   FRO  — variable ~75–80% of net income, no fixed base
#   DHT  — variable 100% of net income, $0.025/qtr nominal floor
#   ECO  — variable, 75% of EPS above breakeven
#   INSW — $0.12/qtr base + supplemental variable on excess earnings
ticker: {ticker}
policy_type: null             # e.g. variable | base_plus_variable | fixed
payout_ratio: null            # fraction of net income (0–1)
base_dividend_per_share: null # fixed per-share base, 0 if none
floor: null                   # minimum quarterly payment, 0 if none
"""


def _watchlist_entry(ticker: str, sector: str) -> str:
    return f"""
# FIXME: filled in by /add-ticker scaffold {ticker}. Replace null values with real data,
# then re-order alphabetically if you care about list order.
{ticker}:
  current_price: null          # FIXME: latest close (Pareto Shipping Daily, dated)
  analyst_target: null         # FIXME: analyst / VIE target
  consensus_pnav: null         # FIXME: Pareto P/NAV (or APPROX if no Pareto coverage —
                               # see CLAUDE.md for the APPROX-anchored treatment)
  consensus_fwd_pe: null       # FIXME: Pareto consensus 1Y FWD P/E (or APPROX)
  sector: {sector}
  as_of: null                  # FIXME: YYYY-MM-DD
"""


def _test_stub(ticker: str, quarter: str) -> str:
    return f'''"""{ticker} tests — fill in data, then remove the skip marker.

When the four YAMLs under inputs/ are populated, delete the `pytestmark` line
below to activate the loads-cleanly assertion. Add per-name assertions
(fleet counts, NAV reconciliation band, position) as you understand the name."""

import pytest

from crude_tanker_fv.loaders import load_company_inputs

pytestmark = pytest.mark.skip(
    reason="{ticker} scaffolded by /add-ticker; data not yet filled in. "
           "Remove this marker when the four YAMLs are populated."
)


def test_inputs_load():
    """Sanity: company inputs load without schema error."""
    ci = load_company_inputs("{ticker}", "{quarter}")
    assert ci is not None
'''


def _decision_log_stub(ticker: str) -> str:
    return f"""# {ticker} — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

---

## Scaffolded — pending first pipeline run

**Confidence tier (governance handoff): PROVISIONAL** _(scaffold — every NAV-driving figure is
still a FIXME/estimate, so the FV is not handoff-ready by construction). Once filled + reconciled,
the tier is computed from the validation state by `crude_tanker_fv.provenance.confidence_tier` and
emitted in the scorecard. A PROVISIONAL name must NOT hand off a governed FV — flag, don't pass._

**Decision:** _[pending — fill in the four input YAMLs + watchlist row, then
run `python -m crude_tanker_fv.pipeline {{QUARTER}}`. After the first run, the
pipeline prepends a structured model-state entry above this line.]_
"""


def _next_steps(ticker: str, sector: str, quarter: str, files: list[Path]) -> str:
    lines = [
        "",
        "=" * 60,
        f"Scaffolded {ticker} ({sector}, {quarter}). Files created:",
        "=" * 60,
    ]
    for f in files:
        lines.append(f"  - {f.relative_to(ROOT)}")
    lines.extend([
        "",
        "Next steps (CLAUDE.md onboarding workflow):",
        "  1. Pull the latest quarterly results (6-K / 20-F / press release).",
        "     Trust the report at quarter-end, not the live IR fleet page.",
        "  2. Fill in the four YAMLs. Use DHT as a minimal-shape reference.",
        "  3. Fill in the watchlist row's FIXME values.",
        "  4. Remove the pytest.mark.skip from tests/test_" + ticker.lower() + ".py.",
        f"  5. Run: python -m crude_tanker_fv.pipeline {quarter}",
        f"  6. Run: /reconcile {ticker}   (must report SANITY = OK)",
        "  7. Close the decision log entry with the reconciliation gap as",
        "     baseline for future drift detection.",
        "  8. CONFIDENCE TIER (governance handoff): the scorecard computes it from the",
        "     validation state (provenance.confidence_tier). The name starts PROVISIONAL",
        "     (uncited figures) and MUST clear to VALIDATED-TIGHT / GOVERNED-WIDE before",
        "     handing off a governed FV — a PROVISIONAL name is NOT handoff-ready; flag,",
        "     don't pass. Get its newbuild commitment/advances CITED (not '~estimate').",
        "",
    ])
    return "\n".join(lines)


def scaffold(ticker: str, sector: str, quarter: str, force: bool, dry_run: bool) -> int:
    ticker = ticker.upper()
    sector = sector.lower()
    lowercase = ticker.lower()

    live = _live_sectors()
    if sector not in live:
        print(f"WARNING: sector {sector!r} is not in scenario_inputs.yaml yet.")
        print(f"         (live sectors: {sorted(live)})")
        print("         A methodology decision doc (METHODOLOGY §11.x) must land BEFORE")
        print("         this ticker can be valued. Scaffolding the files anyway.")
        print()

    classes = SECTOR_CLASSES.get(sector, ["Placeholder"])

    targets = [
        (INPUTS / "fleet_manifests" / f"{lowercase}.yaml",
         _fleet_manifest_stub(ticker, quarter, classes)),
        (INPUTS / "balance_sheets" / f"{lowercase}_{quarter}.yaml",
         _balance_sheet_stub(ticker, quarter)),
        (INPUTS / "cost_structures" / f"{lowercase}.yaml",
         _cost_structure_stub(ticker, classes)),
        (INPUTS / "dividend_policies" / f"{lowercase}.yaml",
         _dividend_policy_stub(ticker)),
        (TESTS / f"test_{lowercase}.py",
         _test_stub(ticker, quarter)),
        (DECISIONS / f"{lowercase}_log.md",
         _decision_log_stub(ticker)),
    ]

    # Refuse-to-overwrite check FIRST, before any side effects.
    if not force:
        existing = [t.relative_to(ROOT) for t, _ in targets if t.exists()]
        if existing:
            sys.stderr.write(
                f"Refusing to overwrite existing files (use --force to override):\n"
            )
            for p in existing:
                sys.stderr.write(f"  - {p}\n")
            return 1

    # Watchlist append needs special handling (preserve comments).
    watchlist_path = INPUTS / "watchlist.yaml"
    watchlist_entry = _watchlist_entry(ticker, sector)
    watchlist_text = watchlist_path.read_text()
    if f"\n{ticker}:" in watchlist_text or watchlist_text.startswith(f"{ticker}:"):
        if not force:
            sys.stderr.write(
                f"Refusing to add duplicate watchlist entry for {ticker} "
                f"(use --force to override).\n"
            )
            return 1

    if dry_run:
        print(f"DRY RUN — would create {len(targets)} files + append watchlist row.")
        for path, _ in targets:
            print(f"  + {path.relative_to(ROOT)}")
        print(f"  ~ inputs/watchlist.yaml (append {ticker} stanza)")
        return 0

    for path, content in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    watchlist_path.write_text(watchlist_text.rstrip() + "\n" + watchlist_entry)

    print(_next_steps(ticker, sector, quarter, [p for p, _ in targets]))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="crude_tanker_fv.add_ticker",
        description="Scaffold YAML stubs + test + decision log for a new ticker.",
    )
    parser.add_argument("ticker", help="ticker symbol (e.g. SBLK)")
    parser.add_argument(
        "--sector", required=True,
        choices=sorted(KNOWN_SECTORS),
        help="sector (existing: crude/product/lng; new sectors warn)",
    )
    parser.add_argument(
        "--quarter", default=None,
        help="balance-sheet quarter (default: from last pipeline run)",
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="show what would be created without writing")
    parser.add_argument("--force", action="store_true",
                        help="overwrite existing files / duplicate watchlist entries")
    args = parser.parse_args(argv)
    quarter = args.quarter or _quarter_from_state()
    return scaffold(args.ticker, args.sector, quarter, args.force, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
