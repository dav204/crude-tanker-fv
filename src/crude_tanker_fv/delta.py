"""Delta report + decision log (METHODOLOGY §7.7, §7.8).

After every pipeline run, this module:
  1. Snapshots the model state (per-ticker FV / NAV / position / broker spread)
     and a hash of every input YAML, into ``state/last_run.json``.
  2. Compares the new snapshot to the previous one and writes
     ``outputs/delta_report.md`` — headline material changes, which input files
     changed, and the full per-ticker delta table.
  3. Prepends a structured "model state" entry to ``decisions/{ticker}_log.md``
     for every ticker — newest entry at the top, user annotates with the
     `**Decision:**` line afterward. Existing content below the new entry is
     left untouched.

Design choices locked 2026-06-01 (see chat log + AskUserQuestion):
  - **Auto-prepend frequency:** every pipeline run (no rate-limiting or dedup).
  - **Material-change thresholds:** position flip (always), |ΔFV%| > 10%,
    |Δbroker_spread| > 5pp, |ΔNAV%| > 5%.
  - **State tracking:** ``state/last_run.json`` is gitignored — machine-local;
    decision logs ARE git-tracked (durable history lives in those files).
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from .price_refresh import PRICE_FRESH_DAYS, STALE_PRICE_ALERT_MIN_NAMES
from .scenarios import detect_mixed_anchor_basis, format_mixed_anchor_basis

# Project root resolved relative to this file (src/crude_tanker_fv/delta.py)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
STATE_DIR = PROJECT_ROOT / "state"
DECISIONS_DIR = PROJECT_ROOT / "decisions"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
INPUTS_DIR = PROJECT_ROOT / "inputs"
SNAPSHOT_PATH = STATE_DIR / "last_run.json"

# ----------------------------------------------------------------------------
# Material-change thresholds (locked 2026-06-01 — "standard" sensitivity)
# ----------------------------------------------------------------------------
MATERIAL_FV_PCT = 10.0        # |ΔFV%| > 10% is material
MATERIAL_SPREAD_PP = 5.0      # |Δbroker_spread_pp| > 5 is material
MATERIAL_NAV_PCT = 5.0        # |ΔNAV/sh %| > 5% is material


# ----------------------------------------------------------------------------
# Snapshot schema
# ----------------------------------------------------------------------------
@dataclass
class TickerSnapshot:
    """The minimal state per ticker needed to compute next-run deltas.

    Kept deliberately narrow: extending this is cheap, shrinking it later means
    backfilling missing fields in old snapshots, which is the wrong direction.
    """
    current_price: float
    single_point_fv: float       # the run_watchlist blended.fair_value_per_share headline
    scenario_pw_fv: float        # run_scenarios_watchlist probability_weighted_fv
    nav_per_share: float         # ScenarioReport.base_nav_per_share (unflexed reference)
    ev_pct: float                # scenario EV% vs current_price
    position: str                # scenario_report.position_recommendation
    breakeven_tce: float         # scenario-invariant breakeven (blended)
    broker_spread_pp: float      # BrokerSweepRow.spread (broker - tool EV%)
    k_broker: float              # mark premium that lifts tool NAV to broker NAV
    sector: str                  # routing sector (crude / lng / product)
    # D-M5 (ruled 2026-07-15): the scenario FV interval — min/max scenario FV over
    # WEIGHT>0 scenarios (0-mass structural tails excluded; they carry no probability
    # and would swamp the low end). Feeds the drift gate's interval flip-triage rule.
    # Defaults keep pre-2.4 snapshots loadable (TickerSnapshot(**s) is strict-keys).
    fv_low: float = float("nan")
    fv_high: float = float("nan")


@dataclass
class RunSnapshot:
    """Full state captured at the end of a pipeline run.

    Persisted as ``state/last_run.json``. The ``input_file_hashes`` map drives
    the "which inputs changed since last run" section of the delta report —
    SHA-256 of every YAML file under ``inputs/``.
    """
    run_at: str                                  # ISO-8601 UTC timestamp
    quarter: str
    tickers: dict[str, TickerSnapshot]
    input_file_hashes: dict[str, str]            # path-relative-to-project-root → sha256


# ----------------------------------------------------------------------------
# Snapshot capture from pipeline objects
# ----------------------------------------------------------------------------
def snapshot_current_run(
    quarter: str,
    fv_reports: list,                # list[CompanyReport]
    scenario_reports: list,          # list[ScenarioReport]
    broker_rows: list,               # list[BrokerSweepRow]
    inputs_dir: Path = INPUTS_DIR,
) -> RunSnapshot:
    """Build a ``RunSnapshot`` from the three pipeline result lists.

    Cross-indexes by ticker. Tickers missing from any of the three sources are
    skipped silently (e.g. a transaction-anchor toggle that valuates fewer
    names). The merged set is whatever's present in ``scenario_reports`` — that
    list is canonical because every watchlist name produces a scenario report.
    """
    fv_by = {r.ticker: r for r in fv_reports}
    bsw_by = {r.ticker: r for r in broker_rows}

    tickers: dict[str, TickerSnapshot] = {}
    for sr in scenario_reports:
        fv = fv_by.get(sr.ticker)
        bsw = bsw_by.get(sr.ticker)
        active_fvs = [sc.fair_value for sc in (getattr(sr, "scenarios", None) or []) if sc.weight > 0]
        tickers[sr.ticker] = TickerSnapshot(
            current_price=round(sr.current_price, 2),
            single_point_fv=round(fv.blended.fair_value_per_share, 2) if fv else float("nan"),
            scenario_pw_fv=round(sr.probability_weighted_fv, 2),
            nav_per_share=round(sr.base_nav_per_share, 2),
            ev_pct=round(sr.expected_value_vs_current / sr.current_price * 100.0, 2),
            position=sr.position_recommendation,
            breakeven_tce=round(sr.breakeven_tce, 0),
            broker_spread_pp=round(bsw.spread, 1) if bsw else 0.0,
            k_broker=round(bsw.k_broker, 2) if bsw else 1.0,
            sector=sr.sector or "crude",
            fv_low=round(min(active_fvs), 2) if active_fvs else float("nan"),
            fv_high=round(max(active_fvs), 2) if active_fvs else float("nan"),
        )

    return RunSnapshot(
        run_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        quarter=quarter,
        tickers=tickers,
        input_file_hashes=_hash_input_files(inputs_dir),
    )


def _hash_input_files(inputs_dir: Path) -> dict[str, str]:
    """SHA-256 every YAML under inputs/, keyed by path relative to project root.

    Skips _template.yaml files (they're scaffolding, not real inputs) and
    anything under hidden directories. Sorted output for determinism.
    """
    hashes: dict[str, str] = {}
    for p in sorted(inputs_dir.rglob("*.yaml")):
        if p.name.startswith("_template"):
            continue
        if any(part.startswith(".") for part in p.parts):
            continue
        rel = p.relative_to(PROJECT_ROOT).as_posix()
        hashes[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return hashes


# ----------------------------------------------------------------------------
# Persistence
# ----------------------------------------------------------------------------
def save_snapshot(snap: RunSnapshot, path: Path = SNAPSHOT_PATH) -> None:
    """Persist a snapshot to ``state/last_run.json``."""
    path.parent.mkdir(parents=True, exist_ok=True)
    # Dataclass → dict (the nested TickerSnapshot map needs explicit handling)
    data = {
        "run_at": snap.run_at,
        "quarter": snap.quarter,
        "tickers": {t: asdict(s) for t, s in snap.tickers.items()},
        "input_file_hashes": snap.input_file_hashes,
    }
    path.write_text(json.dumps(data, indent=2))


def load_previous_snapshot(path: Path = SNAPSHOT_PATH) -> Optional[RunSnapshot]:
    """Load the previous ``state/last_run.json`` or return None if absent."""
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    return RunSnapshot(
        run_at=data["run_at"],
        quarter=data["quarter"],
        tickers={t: TickerSnapshot(**s) for t, s in data["tickers"].items()},
        input_file_hashes=data.get("input_file_hashes", {}),
    )


# ----------------------------------------------------------------------------
# Delta computation
# ----------------------------------------------------------------------------
@dataclass
class TickerDelta:
    """Per-ticker change between two runs. Bottom-half fields are nullable so
    a brand-new ticker (no previous snapshot) renders cleanly with em-dashes."""
    ticker: str
    is_new: bool                                  # not in previous snapshot
    current: TickerSnapshot
    previous: Optional[TickerSnapshot] = None
    # Computed deltas (None when previous is None)
    delta_price: Optional[float] = None
    delta_fv: Optional[float] = None
    delta_fv_pct: Optional[float] = None
    delta_pw_fv: Optional[float] = None
    delta_pw_fv_pct: Optional[float] = None
    delta_nav: Optional[float] = None
    delta_nav_pct: Optional[float] = None
    delta_spread_pp: Optional[float] = None
    position_changed: bool = False
    material: bool = False
    material_reasons: list[str] = field(default_factory=list)


@dataclass
class DeltaReport:
    """Result of comparing the current snapshot to the previous one."""
    is_first_run: bool
    current_run_at: str
    previous_run_at: Optional[str]
    deltas: list[TickerDelta]
    dropped_tickers: list[str]                    # in previous but not current
    changed_input_files: list[str]                # path strings, sorted
    new_input_files: list[str]
    removed_input_files: list[str]


def compute_deltas(current: RunSnapshot, previous: Optional[RunSnapshot]) -> DeltaReport:
    """Diff two snapshots into a structured ``DeltaReport``.

    First-run case: every ticker is flagged ``is_new=True``, no per-field
    deltas are populated, ``is_first_run`` is True. The delta report renders
    cleanly with em-dashes in delta columns.
    """
    if previous is None:
        return DeltaReport(
            is_first_run=True,
            current_run_at=current.run_at,
            previous_run_at=None,
            deltas=[TickerDelta(ticker=t, is_new=True, current=s)
                    for t, s in current.tickers.items()],
            dropped_tickers=[],
            changed_input_files=sorted(current.input_file_hashes.keys()),
            new_input_files=sorted(current.input_file_hashes.keys()),
            removed_input_files=[],
        )

    deltas: list[TickerDelta] = []
    for t, cur in current.tickers.items():
        prev = previous.tickers.get(t)
        if prev is None:
            deltas.append(TickerDelta(ticker=t, is_new=True, current=cur))
            continue
        d = TickerDelta(
            ticker=t,
            is_new=False,
            current=cur,
            previous=prev,
            delta_price=round(cur.current_price - prev.current_price, 2),
            delta_fv=round(cur.single_point_fv - prev.single_point_fv, 2),
            delta_fv_pct=_pct_delta(cur.single_point_fv, prev.single_point_fv),
            delta_pw_fv=round(cur.scenario_pw_fv - prev.scenario_pw_fv, 2),
            delta_pw_fv_pct=_pct_delta(cur.scenario_pw_fv, prev.scenario_pw_fv),
            delta_nav=round(cur.nav_per_share - prev.nav_per_share, 2),
            delta_nav_pct=_pct_delta(cur.nav_per_share, prev.nav_per_share),
            delta_spread_pp=round(cur.broker_spread_pp - prev.broker_spread_pp, 1),
            position_changed=(cur.position != prev.position),
        )
        d.material, d.material_reasons = _classify_material(d)
        deltas.append(d)

    dropped = sorted(set(previous.tickers.keys()) - set(current.tickers.keys()))

    prev_hashes = previous.input_file_hashes
    cur_hashes = current.input_file_hashes
    prev_paths = set(prev_hashes.keys())
    cur_paths = set(cur_hashes.keys())
    new_files = sorted(cur_paths - prev_paths)
    removed_files = sorted(prev_paths - cur_paths)
    changed = sorted(p for p in cur_paths & prev_paths if cur_hashes[p] != prev_hashes[p])

    return DeltaReport(
        is_first_run=False,
        current_run_at=current.run_at,
        previous_run_at=previous.run_at,
        deltas=deltas,
        dropped_tickers=dropped,
        changed_input_files=changed,
        new_input_files=new_files,
        removed_input_files=removed_files,
    )


def _pct_delta(cur: float, prev: float) -> Optional[float]:
    """Percentage change, guarded against zero/NaN previous values."""
    if prev is None or prev == 0 or prev != prev:
        return None
    return round((cur - prev) / prev * 100.0, 1)


def _classify_material(d: TickerDelta) -> tuple[bool, list[str]]:
    """Apply the material-change rules — position flip (always), |ΔFV%| > 10%,
    |Δspread| > 5pp, |ΔNAV%| > 5%. Returns (is_material, list_of_reasons)."""
    reasons: list[str] = []
    if d.position_changed:
        reasons.append(f"position {d.previous.position} → {d.current.position}")
    if d.delta_fv_pct is not None and abs(d.delta_fv_pct) > MATERIAL_FV_PCT:
        reasons.append(f"single-point FV {d.delta_fv_pct:+.1f}%")
    if d.delta_pw_fv_pct is not None and abs(d.delta_pw_fv_pct) > MATERIAL_FV_PCT:
        reasons.append(f"scenario PW FV {d.delta_pw_fv_pct:+.1f}%")
    if d.delta_spread_pp is not None and abs(d.delta_spread_pp) > MATERIAL_SPREAD_PP:
        reasons.append(f"broker spread {d.delta_spread_pp:+.1f}pp")
    if d.delta_nav_pct is not None and abs(d.delta_nav_pct) > MATERIAL_NAV_PCT:
        reasons.append(f"NAV/sh {d.delta_nav_pct:+.1f}%")
    return (len(reasons) > 0, reasons)


# ----------------------------------------------------------------------------
# Markdown rendering — delta report
# ----------------------------------------------------------------------------
def write_delta_report(report: DeltaReport, outputs_dir: Path = OUTPUTS_DIR,
                       stale_prices: Optional[dict[str, str]] = None) -> Path:
    """Render the delta report to ``outputs/delta_report.md`` and return path.

    ``stale_prices`` is ``loaders.stale_price_fallbacks(...)`` for the run —
    at ``STALE_PRICE_ALERT_MIN_NAMES`` names the report leads with a banner:
    that many freshness-gate fallbacks means the overlay vintage itself aged
    out, and every flip below may be a phantom on month-old statics
    (2026-07-31 — the delta report said nothing while TNK/STNG/ASC flipped)."""
    outputs_dir.mkdir(parents=True, exist_ok=True)
    path = outputs_dir / "delta_report.md"
    path.write_text(_render_delta_md(report, stale_prices))
    return path


def _render_delta_md(r: DeltaReport, stale_prices: Optional[dict[str, str]] = None) -> str:
    lines: list[str] = []
    lines.append("# Pipeline Delta Report\n")
    if stale_prices and len(stale_prices) >= STALE_PRICE_ALERT_MIN_NAMES:
        names = ", ".join(sorted(stale_prices))
        lines.append(f"> ## ⚠️ STALE-PRICE RUN — price basis is NOT the tape\n"
                     f">\n"
                     f"> **{len(stale_prices)} names fell back past the freshness gate: {names}.** "
                     f"The `prices_daily.yaml` overlay is older than {PRICE_FRESH_DAYS} days, so "
                     f"these rows are priced on watchlist statics. Every position flip and Δprice "
                     f"below is SUSPECT until prices are re-fetched "
                     f"(`python -m crude_tanker_fv.price_refresh`), the vintage committed, and the "
                     f"pipeline re-run.\n")
    lines.append(f"- **This run:** {r.current_run_at}")
    if r.is_first_run:
        lines.append("- **Previous run:** _(none — first snapshot)_\n")
        lines.append("## Headline changes\n")
        lines.append(f"- **First run.** {len(r.deltas)} tickers captured; no deltas computed yet.")
        lines.append("- Future runs will surface position flips, FV moves > 10%, "
                     "broker spread shifts > 5pp, and NAV moves > 5% here.\n")
        lines.append("## Input files captured this run\n")
        for p in r.new_input_files:
            lines.append(f"- `{p}` (new)")
        lines.append("")
        lines.append(_render_full_table(r))
        return "\n".join(lines)

    lines.append(f"- **Previous run:** {r.previous_run_at}\n")

    # --- Headline section ---
    lines.append("## Headline changes (material moves)\n")
    material = [d for d in r.deltas if d.material]
    new = [d for d in r.deltas if d.is_new]
    if not material and not new and not r.dropped_tickers:
        lines.append("- **No material changes.** All tickers within "
                     f"thresholds (|ΔFV%|≤{MATERIAL_FV_PCT:.0f}%, "
                     f"|Δspread|≤{MATERIAL_SPREAD_PP:.0f}pp, "
                     f"|ΔNAV%|≤{MATERIAL_NAV_PCT:.0f}%) and no position flips.")
    else:
        for d in new:
            lines.append(f"- **{d.ticker}: new to watchlist** "
                         f"(price ${d.current.current_price:.2f}, "
                         f"position {d.current.position})")
        for t in r.dropped_tickers:
            lines.append(f"- **{t}: dropped from watchlist** since last run")
        for d in material:
            reasons = "; ".join(d.material_reasons)
            lines.append(f"- **{d.ticker}:** {reasons}")
    lines.append("")

    # --- Input file changes ---
    lines.append("## Input files changed since last run\n")
    if not (r.changed_input_files or r.new_input_files or r.removed_input_files):
        lines.append("- _(no input file changes detected — hashes match)_")
    else:
        for p in r.new_input_files:
            lines.append(f"- `{p}` (new)")
        for p in r.changed_input_files:
            lines.append(f"- `{p}` (modified)")
        for p in r.removed_input_files:
            lines.append(f"- `{p}` (removed)")
    lines.append("")

    # --- Full per-ticker table ---
    lines.append(_render_full_table(r))
    return "\n".join(lines)


def _render_full_table(r: DeltaReport) -> str:
    lines: list[str] = []
    lines.append("## Full per-ticker deltas\n")
    lines.append("| Ticker | Price | Single-point FV | Scenario PW FV | "
                 "NAV/sh | Position | Broker spread |")
    lines.append("|---|---|---|---|---|---|---|")
    for d in r.deltas:
        cur = d.current
        if d.is_new:
            lines.append(
                f"| **{d.ticker}** (new) | ${cur.current_price:.2f} | "
                f"${cur.single_point_fv:.2f} | ${cur.scenario_pw_fv:.2f} | "
                f"${cur.nav_per_share:.2f} | {cur.position} | "
                f"{cur.broker_spread_pp:+.1f}pp |"
            )
        else:
            star = " ⚑" if d.material else ""
            lines.append(
                f"| {d.ticker}{star} | "
                f"${cur.current_price:.2f} ({_signed(d.delta_price)}) | "
                f"${cur.single_point_fv:.2f} ({_signed_pct(d.delta_fv_pct)}) | "
                f"${cur.scenario_pw_fv:.2f} ({_signed_pct(d.delta_pw_fv_pct)}) | "
                f"${cur.nav_per_share:.2f} ({_signed_pct(d.delta_nav_pct)}) | "
                f"{cur.position}{' ⟵' if d.position_changed else ''} | "
                f"{cur.broker_spread_pp:+.1f}pp ({_signed_pp(d.delta_spread_pp)}) |"
            )
    lines.append("")
    lines.append("_⚑ flags a material change (position flip, |ΔFV%| > 10%, "
                 "|Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._")

    # MIXED-ANCHOR-BASIS flag (B5 — METHODOLOGY §10): the table mixes sectors,
    # whose cycle anchors use incompatible bases. Cycle-position reads are only
    # comparable within a basis, never across — surface that here.
    mix = detect_mixed_anchor_basis(d.current.sector for d in r.deltas)
    if mix:
        lines.append("")
        lines.append(
            f"_⚠ MIXED-ANCHOR-BASIS: this table spans {len(mix)} incompatible "
            "cycle-anchor bases — cycle-position ratios are NOT comparable across "
            f"them (METHODOLOGY §10): {format_mixed_anchor_basis(mix)}._"
        )
    return "\n".join(lines)


def _signed(v: Optional[float]) -> str:
    if v is None:
        return "—"
    if v == 0:
        return "no change"
    return f"{v:+.2f}"


def _signed_pct(v: Optional[float]) -> str:
    if v is None:
        return "—"
    if v == 0:
        return "no change"
    return f"{v:+.1f}%"


def _signed_pp(v: Optional[float]) -> str:
    if v is None:
        return "—"
    if v == 0:
        return "no change"
    return f"{v:+.1f}pp"


# ----------------------------------------------------------------------------
# Decision-log prepend
# ----------------------------------------------------------------------------
# The decision log is the user-curated counterpart to the delta report. Each
# pipeline run prepends a structured entry to ``decisions/{ticker}_log.md``.
# Existing content (below the new entry) is preserved verbatim — user
# annotations live forever. If the file doesn't exist, it's created with a
# brief header.

# A dated entry header. This module writes them; drift_gate reads only the
# first one (newest-first contract), so the prepend anchor and the gate parser
# must share this definition.
DECISION_LOG_HEADER_RE = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})[^\s]*\s*(.*)$")

_DECISION_LOG_HEADER = """# {ticker} — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

---
"""


def prepend_decision_log_entries(
    report: DeltaReport, decisions_dir: Path = DECISIONS_DIR,
) -> list[Path]:
    """Prepend a model-state entry to each ticker's decision log.

    Returns the list of file paths touched (for reporting). Files are created
    on first encounter with ``_DECISION_LOG_HEADER`` + the first entry.
    """
    decisions_dir.mkdir(parents=True, exist_ok=True)
    touched: list[Path] = []
    for d in report.deltas:
        path = decisions_dir / f"{d.ticker.lower()}_log.md"
        entry = _render_decision_log_entry(d, report)
        if path.exists():
            existing = path.read_text()
            # Insert the new entry immediately above the first dated entry
            # header — newest-first must hold even for logs founded manually,
            # whose top entry sits above any "---" preamble separator.
            lines = existing.splitlines(keepends=True)
            idx = next(
                (i for i, ln in enumerate(lines)
                 if DECISION_LOG_HEADER_RE.match(ln)),
                None,
            )
            if idx is None:
                new_content = f"{existing.rstrip()}\n\n{entry}\n"
            else:
                preamble = "".join(lines[:idx])
                if preamble:
                    preamble = preamble.rstrip("\n") + "\n\n"
                new_content = f"{preamble}{entry}\n{''.join(lines[idx:])}"
        else:
            header = _DECISION_LOG_HEADER.format(ticker=d.ticker)
            new_content = f"{header}\n{entry}\n"
        path.write_text(new_content)
        touched.append(path)
    return touched


def _render_decision_log_entry(d: TickerDelta, report: DeltaReport) -> str:
    """Markdown for one decision-log entry. Compact, scannable, copy-pasteable."""
    cur = d.current
    ts = report.current_run_at
    lines: list[str] = [f"## {ts} — Pipeline run (auto)\n"]
    lines.append("**Model state:**")
    lines.append(f"- Current price: ${cur.current_price:.2f}")
    lines.append(f"- Single-point FV: ${cur.single_point_fv:.2f}")
    lines.append(f"- Scenario PW FV: ${cur.scenario_pw_fv:.2f} (EV {cur.ev_pct:+.1f}%)")
    lines.append(f"- NAV / share: ${cur.nav_per_share:.2f}")
    lines.append(f"- Position: **{cur.position}**")
    lines.append(f"- Broker spread: {cur.broker_spread_pp:+.1f}pp "
                 f"(k_broker {cur.k_broker:.2f})")
    lines.append(f"- Sector: {cur.sector}")
    lines.append("")

    if d.is_new:
        lines.append("**Status:** _First snapshot — no prior state to compare._\n")
    elif d.material:
        lines.append("**Material deltas since last run:**")
        for r in d.material_reasons:
            lines.append(f"- ⚑ {r}")
        # Always include the numeric context so the entry is self-contained.
        lines.append(f"- Δprice: {_signed(d.delta_price)} "
                     f"| Δsingle FV: {_signed_pct(d.delta_fv_pct)} "
                     f"| Δscenario FV: {_signed_pct(d.delta_pw_fv_pct)} "
                     f"| ΔNAV: {_signed_pct(d.delta_nav_pct)} "
                     f"| Δspread: {_signed_pp(d.delta_spread_pp)}")
        lines.append("")
    else:
        lines.append("**Deltas since last run:** _(no material moves)_")
        lines.append(f"- Δprice: {_signed(d.delta_price)} "
                     f"| Δsingle FV: {_signed_pct(d.delta_fv_pct)} "
                     f"| Δscenario FV: {_signed_pct(d.delta_pw_fv_pct)} "
                     f"| ΔNAV: {_signed_pct(d.delta_nav_pct)} "
                     f"| Δspread: {_signed_pp(d.delta_spread_pp)}")
        lines.append("")

    lines.append("**Decision:** _[pending annotation]_")
    lines.append("")
    lines.append("---\n")
    return "\n".join(lines)
