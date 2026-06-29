"""Committed, Pareto-free drift gate — METHODOLOGY Option B / PLAN.md Phase 2.

The problem this closes (audit A-2): after a sector launches, nothing
*automated* stops a drifted number from shipping on accuracy grounds. The
one-time calibration lock is manual and never auto-invoked; the >2pp drift
alert runs against a **gitignored, self-overwriting** snapshot
(`state/last_reconcile.json`), so it has no durable anchor and no teeth.

This module gives drift a durable, committed anchor and machine-enforces the
CLAUDE.md step-3 annotation discipline:

  baselines/reconcile_baseline.yaml   committed prior (per name: ev_pct /
                                      tool_nav / position_band / k_broker +
                                      ratifying commit + cause)
  tests/test_drift_gate.py            fails the build on an UNEXPLAINED move
  scripts/ratify_baseline.sh          deliberate re-ratify with mandatory cause

What it tracks, and why it never re-anchors to Pareto:

  * EV% / tool NAV / position_band  — the tool's **own** outputs vs its
    committed prior. Pareto-free: these never reference broker NAV. A move
    beyond threshold (or a band flip) needs a dated decision-log annotation.

  * k_broker on its **second difference** — k_broker is itself a first-order
    spread (the uniform mark premium that lifts the tool NAV onto the broker
    NAV, marks.solve_broker_premium). We gate on its *change* (Δk vs baseline),
    never its *level* — so a persistently-wide spread that is a documented §6
    call (INSW k≈1.64, NAT k≈2.16) sits green forever; only a *change* in the
    tool↔broker relationship trips it. The gate therefore never says "get
    closer to Pareto", only "your relationship to the tape moved — explain it."

  * APPROX names (reconcile.APPROX_PNAV_TICKERS) have a placeholder broker
    anchor, so k_broker is meaningless for them — they are tracked on
    **self-consistency only** (EV% / NAV / band vs their own prior; no Δk gate).

The annotation escape hatch: a breaching name passes if `decisions/<t>_log.md`
carries a human-authored dated entry (or a non-placeholder **Decision:** line)
dated on/after the baseline's `ratified_at`. Re-ratifying advances that date,
which resets the window — so accept a drift by re-ratifying (cause recorded),
not by leaving a stale annotation to cover future quarters.

Reuses the reconcile drift-delta pattern (reconcile.py:144-150) and its
single-sourced APPROX set; the baseline format is richer (committed YAML,
multi-field) than the reconcile snapshot, so the storage is separate.

Exit codes (CLI): 0 = no UNEXPLAINED drift · 1 = at least one UNEXPLAINED ·
2 = usage / missing data.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import yaml

from . import reconcile

ROOT = Path(__file__).resolve().parents[2]
BASELINE_PATH = ROOT / "baselines" / "reconcile_baseline.yaml"
STATE_PATH = ROOT / "state" / "last_run.json"
DECISIONS_DIR = ROOT / "decisions"

# Defaults — overridable per-baseline via the `thresholds:` block so the owner
# can tune without a code change. The EV% bar matches the CLAUDE.md >2pp drift
# discipline; NAV is the same bar in percent; Δk is the multiplier-space analog
# (~a 5% shift in tool↔broker alignment).
DEFAULT_THRESHOLDS = {
    "ev_pct_pp": 2.0,        # EV% move, percentage points
    "nav_pct": 2.0,          # tool NAV move, percent of baseline NAV
    "k_broker_delta": 0.05,  # k_broker second difference (Δ spread), multiplier points
}

APPROX = reconcile.APPROX_PNAV_TICKERS

_HEADER_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})[^\s]*\s*(.*)$")
_PLACEHOLDER = "pending annotation"
_AUTO_TITLE = "pipeline run (auto)"


# ---------------------------------------------------------------------------
# Baseline construction / IO
# ---------------------------------------------------------------------------

def _basis_for(ticker: str) -> str:
    return "approx" if ticker in APPROX else "pareto"


def baseline_record(t: dict) -> dict:
    """One name's committed record from a `last_run.json` ticker entry."""
    return {
        "ev_pct": round(float(t["ev_pct"]), 2),
        "tool_nav": round(float(t["nav_per_share"]), 2),
        "position_band": t["position"],
        "k_broker": round(float(t["k_broker"]), 3),
        "sector": t.get("sector", "?"),
    }


def build_baseline(state: dict, *, cause: str, ratified_commit: str) -> dict:
    names = {
        ticker: {"pnav_basis": _basis_for(ticker), **baseline_record(t)}
        for ticker, t in sorted(state.get("tickers", {}).items())
    }
    return {
        "meta": {
            "ratified_at": state.get("run_at"),
            "ratified_commit": ratified_commit,
            "quarter": state.get("quarter"),
            "cause": cause,
        },
        "thresholds": dict(DEFAULT_THRESHOLDS),
        "names": names,
    }


def load_baseline(path: Path = BASELINE_PATH) -> dict:
    return yaml.safe_load(path.read_text())


def load_state(path: Path = STATE_PATH) -> dict:
    return json.loads(path.read_text())


def _git_short_head() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def write_baseline(cause: str, *, state: Optional[dict] = None,
                   path: Path = BASELINE_PATH) -> dict:
    """Rewrite the committed baseline from the current pipeline state."""
    state = state if state is not None else load_state()
    baseline = build_baseline(state, cause=cause, ratified_commit=_git_short_head())
    path.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# Committed drift-gate baseline (METHODOLOGY Option B / PLAN.md Phase 2).\n"
        "# Pareto-free reference for tests/test_drift_gate.py. Re-ratify deliberately\n"
        "# via scripts/ratify_baseline.sh \"<cause>\" — never hand-edit the numbers.\n"
    )
    path.write_text(header + yaml.safe_dump(baseline, sort_keys=False, width=100,
                                            allow_unicode=True))
    return baseline


# ---------------------------------------------------------------------------
# Decision-log annotation grep
# ---------------------------------------------------------------------------

def decision_log_annotated_since(
    ticker: str, since: str, decisions_dir: Path = DECISIONS_DIR
) -> bool:
    """True iff the MOST-RECENT decision-log entry for `ticker` is a human
    annotation dated on/after `since`.

    Only the top (newest) entry counts. Every pipeline run prepends a fresh
    ``Pipeline run (auto)`` entry whose ``**Decision:**`` line is the
    ``_[pending annotation]_`` placeholder, so a breach is "explained" only when
    a human has annotated *that* run — either by prepending a dated non-auto
    header or by replacing the placeholder under the latest auto entry.

    This closes the auto-explain hole: a real annotation buried under an *older*
    entry (e.g. a prior move's note that still sits inside the ratification
    window) no longer blesses a fresh, unreviewed move. The pipeline writing the
    log quietly cannot self-explain — the newest entry it writes carries the
    placeholder, and a stale lower entry is not consulted.
    """
    path = decisions_dir / f"{ticker.lower()}_log.md"
    if not path.exists():
        return False
    since_day = since[:10]
    lines = path.read_text().splitlines()

    # Locate the first (most-recent) dated entry header; skip any file preamble.
    idx = next((i for i, ln in enumerate(lines) if _HEADER_RE.match(ln)), None)
    if idx is None:
        return False
    m = _HEADER_RE.match(lines[idx])
    day, title = m.group(1), m.group(2).lstrip("—- ").strip()
    if day < since_day:
        return False  # the newest entry predates the ratification window
    if title and not title.lower().startswith(_AUTO_TITLE):
        return True   # a human-authored header sits on top

    # Auto header on top: explained only if a human replaced its placeholder.
    # Scan its body up to (but not into) the next, older entry.
    for line in lines[idx + 1:]:
        if _HEADER_RE.match(line):
            break
        s = line.strip()
        if s.startswith("**Decision:**"):
            body = s[len("**Decision:**"):].strip().strip("*_ ").strip()
            if body and _PLACEHOLDER not in body.lower():
                return True
    return False


# ---------------------------------------------------------------------------
# Drift evaluation
# ---------------------------------------------------------------------------

@dataclass
class DriftRow:
    ticker: str
    pnav_basis: str
    status: str                       # stable / explained / UNEXPLAINED / new / missing
    breaches: list[str] = field(default_factory=list)
    d_ev: Optional[float] = None      # pp
    d_nav_pct: Optional[float] = None # percent
    band_from: Optional[str] = None
    band_to: Optional[str] = None
    d_k: Optional[float] = None
    annotated: bool = False


def _thresholds(baseline: dict) -> dict:
    th = dict(DEFAULT_THRESHOLDS)
    th.update(baseline.get("thresholds") or {})
    return th


def evaluate(baseline: dict, state: dict,
             decisions_dir: Path = DECISIONS_DIR) -> list[DriftRow]:
    """Compare current state against the committed baseline; classify each name."""
    th = _thresholds(baseline)
    ratified_at = (baseline.get("meta") or {}).get("ratified_at") or "0000-00-00"
    names = baseline.get("names") or {}
    tickers = state.get("tickers", {})
    rows: list[DriftRow] = []

    for ticker in sorted(names):
        base = names[ticker]
        basis = base.get("pnav_basis", _basis_for(ticker))
        t = tickers.get(ticker)
        if t is None:
            rows.append(DriftRow(ticker, basis, "missing"))
            continue

        cur = baseline_record(t)
        d_ev = round(cur["ev_pct"] - float(base["ev_pct"]), 2)
        base_nav = float(base["tool_nav"])
        d_nav_pct = round((cur["tool_nav"] - base_nav) / base_nav * 100.0, 2) if base_nav else 0.0
        band_from, band_to = base["position_band"], cur["position_band"]
        d_k = round(cur["k_broker"] - float(base["k_broker"]), 3)

        breaches: list[str] = []
        if abs(d_ev) > th["ev_pct_pp"]:
            breaches.append("EV%")
        if abs(d_nav_pct) > th["nav_pct"]:
            breaches.append("NAV")
        if band_from != band_to:
            breaches.append("band")
        if basis != "approx" and abs(d_k) > th["k_broker_delta"]:
            breaches.append("k_broker")

        annotated = False
        if breaches:
            annotated = decision_log_annotated_since(ticker, ratified_at, decisions_dir)
            status = "explained" if annotated else "UNEXPLAINED"
        else:
            status = "stable"

        rows.append(DriftRow(
            ticker=ticker, pnav_basis=basis, status=status, breaches=breaches,
            d_ev=d_ev, d_nav_pct=d_nav_pct, band_from=band_from, band_to=band_to,
            d_k=d_k, annotated=annotated,
        ))

    # Names present in state but not yet in the baseline (newly onboarded):
    # report so they get ratified, but do not fail the gate.
    for ticker in sorted(tickers):
        if ticker not in names:
            rows.append(DriftRow(ticker, _basis_for(ticker), "new"))
    return rows


def unexplained(rows: list[DriftRow]) -> list[DriftRow]:
    return [r for r in rows if r.status == "UNEXPLAINED"]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _fmt_band(r: DriftRow) -> str:
    if r.band_from is None:
        return "—"
    if r.band_from == r.band_to:
        return r.band_from.split()[0]
    return f"{r.band_from.split()[0]}→{r.band_to.split()[0]}"


def _print_report(baseline: dict, rows: list[DriftRow]) -> None:
    meta = baseline.get("meta") or {}
    print(f"DRIFT GATE — baseline ratified {(meta.get('ratified_at') or '?')[:10]} "
          f"(commit {meta.get('ratified_commit', '?')}, {meta.get('quarter', '?')})")
    th = _thresholds(baseline)
    print(f"  thresholds: ΔEV>{th['ev_pct_pp']}pp · ΔNAV>{th['nav_pct']}% · "
          f"Δk>{th['k_broker_delta']} (k on its second difference; APPROX = self-consistency only)")
    header = f"{'TICKER':<8}{'BASIS':<8}{'ΔEV':>8}{'ΔNAV':>8}  {'BAND':<14}{'Δk':>8}  {'STATUS':<12}{'BREACH'}"
    print(header)
    print("-" * (len(header) + 6))
    for r in rows:
        d_ev = "—" if r.d_ev is None else f"{r.d_ev:+.1f}pp"
        d_nav = "—" if r.d_nav_pct is None else f"{r.d_nav_pct:+.1f}%"
        d_k = "—" if (r.d_k is None or r.pnav_basis == "approx") else f"{r.d_k:+.3f}"
        print(f"{r.ticker:<8}{r.pnav_basis:<8}{d_ev:>8}{d_nav:>8}  {_fmt_band(r):<14}{d_k:>8}  "
              f"{r.status:<12}{','.join(r.breaches)}")
    bad = unexplained(rows)
    expl = [r for r in rows if r.status == "explained"]
    new = [r for r in rows if r.status == "new"]
    missing = [r for r in rows if r.status == "missing"]
    print()
    print(f"  {len(rows)} rows: {len(bad)} UNEXPLAINED, {len(expl)} explained, "
          f"{len(new)} new, {len(missing)} missing-from-state.")
    if bad:
        print("  UNEXPLAINED (annotate decisions/<t>_log.md or re-ratify with cause): "
              + ", ".join(r.ticker for r in bad))
    if new:
        print("  New (run scripts/ratify_baseline.sh to start tracking): "
              + ", ".join(r.ticker for r in new))


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="crude_tanker_fv.drift_gate",
        description="Committed Pareto-free drift gate (report, or re-ratify the baseline).",
    )
    parser.add_argument("--ratify", action="store_true",
                        help="rewrite baselines/reconcile_baseline.yaml from current state")
    parser.add_argument("--cause", help="mandatory cause when --ratify is used")
    args = parser.parse_args(argv)

    if args.ratify:
        if not args.cause or not args.cause.strip():
            sys.stderr.write("--ratify requires a non-empty --cause.\n")
            return 2
        if not STATE_PATH.exists():
            sys.stderr.write("state/last_run.json not found — run the pipeline first.\n")
            return 2
        baseline = write_baseline(args.cause.strip())
        n = len(baseline["names"])
        print(f"Ratified {n} names @ commit {baseline['meta']['ratified_commit']} "
              f"({baseline['meta']['quarter']}). Cause: {args.cause.strip()}")
        print(f"Wrote {BASELINE_PATH.relative_to(ROOT)}")
        return 0

    if not BASELINE_PATH.exists():
        sys.stderr.write(
            "baselines/reconcile_baseline.yaml not found — ratify it first:\n"
            "  scripts/ratify_baseline.sh \"initial ratification\"\n"
        )
        return 2
    if not STATE_PATH.exists():
        sys.stderr.write("state/last_run.json not found — run the pipeline first.\n")
        return 2
    baseline = load_baseline()
    state = load_state()
    rows = evaluate(baseline, state)
    _print_report(baseline, rows)
    return 1 if unexplained(rows) else 0


if __name__ == "__main__":
    sys.exit(main())
