"""Pre-flight quarterly refresh checklist (METHODOLOGY §8).

Run at the start of a refresh cycle BEFORE the main pipeline:

    python -m crude_tanker_fv.refresh           # auto-infer target quarter
    python -m crude_tanker_fv.refresh 2026-Q2   # explicit target

Emits ``outputs/refresh_checklist.md`` flagging:
  - Missing quarterly balance sheets (with per-ticker IR URLs to pull from)
  - Stale market data files (> 30 days)
  - Stale watchlist prices / APPROX consensus_pnav entries
  - Per-ticker file age table (fleet / cost / dividend drift)
  - Full IR URL playbook for ad-hoc lookups

The checklist answers "what do I need to gather before I can run the full
pipeline this quarter?" — turning the start of a refresh from a half-day
of remembering what to update into a 5-minute review.

Design choices (locked 2026-06-01):
  - Default target quarter = quarter just completed as of today (today 2026-06-01
    → Q1 2026). User can override with CLI arg.
  - Market-data staleness threshold: 30 days. Watchlist as_of: 14 days.
    Fleet manifest: 90 days. Cost / dividend: 180 days (rarely change).
  - Separate workflow from the main pipeline — not wired into pipeline.main()
    on purpose. The pipeline is the "I'm running with the data I have" loop;
    this is the "do I have the data I need?" loop.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUTS_DIR = PROJECT_ROOT / "inputs"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
DATA_SOURCES_PATH = INPUTS_DIR / "data_sources.yaml"

# ----------------------------------------------------------------------------
# Staleness thresholds (locked 2026-06-01)
# ----------------------------------------------------------------------------
MARKET_DATA_STALE_DAYS = 30      # spot / 12M TC / FFA / vessel value curves
WATCHLIST_STALE_DAYS = 42        # consensus-pair vintage (owner 2026-07-06 at the
                                 # first recapture sitting: 14d guaranteed standing
                                 # flags between sittings; 42d = monthly rhythm +
                                 # slack, with the quarterly recapture trigger and
                                 # the staleness-floor trigger as hard backstops)
FLEET_STALE_DAYS = 90            # fleet manifest (vessels enter / exit)
COST_DIVIDEND_STALE_DAYS = 180   # cost structure / dividend policy

# Market data files to monitor (relative to inputs/market_data/)
MARKET_DATA_FILES = [
    "vessel_value_curves.yaml",
    "spot_tce.yaml",
    "twelve_month_tc.yaml",
    "ffa_forward_curve.yaml",
    "historical_tce_means.yaml",
]


# ----------------------------------------------------------------------------
# Target-quarter inference
# ----------------------------------------------------------------------------
def infer_target_quarter(today: date | None = None) -> str:
    """Return the quarter just completed as of ``today`` (default: real today).

    Convention: ``2026-Q1`` = Jan-Mar 2026. The refresh workflow runs AFTER
    quarter-end results land — i.e. the quarter you're refreshing is the one
    most recently CLOSED, not the one currently in progress.

    Examples (today → target):
        2026-04-15 → 2026-Q1  (Q1 just closed end-March)
        2026-06-01 → 2026-Q1  (Q2 in progress; Q1 results released ~May)
        2026-08-01 → 2026-Q2  (Q2 closed end-June; results released July-Aug)
        2026-01-15 → 2025-Q4  (year-end rollover)
    """
    today = today or date.today()
    year, month = today.year, today.month
    current_q = (month - 1) // 3 + 1   # 1..4
    if current_q == 1:
        return f"{year - 1}-Q4"
    return f"{year}-Q{current_q - 1}"


# ----------------------------------------------------------------------------
# CheckItem + Checklist data structures
# ----------------------------------------------------------------------------
@dataclass
class CheckItem:
    """One row of the checklist — a thing to look at, with a verdict."""
    label: str
    status: str          # "ok" / "stale" / "missing" / "approx" / "warn"
    detail: str = ""     # free-form: file path, days old, source URL, etc.


@dataclass
class TickerFileAges:
    """Per-ticker file-modification snapshot."""
    ticker: str
    fleet_days: int | None = None
    balance_sheet_days: int | None = None
    balance_sheet_present: bool = False
    cost_days: int | None = None
    dividend_days: int | None = None


@dataclass
class Checklist:
    """Full refresh checklist, ready to render."""
    today: str
    target_quarter: str
    balance_sheets: list[CheckItem] = field(default_factory=list)
    market_data: list[CheckItem] = field(default_factory=list)
    watchlist: list[CheckItem] = field(default_factory=list)
    earnings: list[CheckItem] = field(default_factory=list)
    reweight_triggers: list[CheckItem] = field(default_factory=list)
    per_ticker_ages: list[TickerFileAges] = field(default_factory=list)
    data_sources: dict = field(default_factory=dict)

    @property
    def missing_bs_count(self) -> int:
        return sum(1 for c in self.balance_sheets if c.status == "missing")

    @property
    def stale_md_count(self) -> int:
        return sum(1 for c in self.market_data if c.status == "stale")

    @property
    def approx_watchlist_count(self) -> int:
        return sum(1 for c in self.watchlist if c.status == "approx")

    @property
    def stale_watchlist_count(self) -> int:
        return sum(1 for c in self.watchlist if c.status == "stale")

    @property
    def earnings_due_count(self) -> int:
        return sum(1 for c in self.earnings if c.status == "missing")

    @property
    def triggers_due_count(self) -> int:
        return sum(1 for c in self.reweight_triggers if c.status == "missing")


# ----------------------------------------------------------------------------
# File-age helpers
# ----------------------------------------------------------------------------
def _days_since(path: Path, today: date) -> int | None:
    """Days since the file was last modified, or None if the file is absent."""
    if not path.exists():
        return None
    mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).date()
    return (today - mtime).days


EARNINGS_UPCOMING_DAYS = 14      # "reports soon" warning horizon
EARNINGS_CALENDAR_PATH = INPUTS_DIR / "earnings_calendar.yaml"

TRIGGER_UPCOMING_DAYS = 14       # "trigger due soon" warning horizon
REWEIGHT_TRIGGERS_PATH = INPUTS_DIR / "reweight_triggers.yaml"


# ----------------------------------------------------------------------------
# Per-section checks
# ----------------------------------------------------------------------------
def load_earnings_calendar(inputs_dir: Path = INPUTS_DIR) -> "tuple[dict, dict]":
    """THE calendar reader (WO2 2.1/R-5) — every consumer goes through here;
    nobody special-cases the quarter key anymore. Returns (meta, names);
    missing file -> ({}, {})."""
    path = inputs_dir / "earnings_calendar.yaml"
    if not path.exists():
        return {}, {}
    doc = yaml.safe_load(path.read_text()) or {}
    return doc.get("meta") or {}, doc.get("names") or {}


def check_earnings_calendar(
    target_quarter: str, watchlist: dict, inputs_dir: Path = INPUTS_DIR,
    today: date | None = None,
) -> list[CheckItem]:
    """One CheckItem per watchlist ticker against inputs/earnings_calendar.yaml.

    Statuses: "missing" = report window has opened/passed but the calendar
    quarter's balance sheet is absent (REPORT OUT — refresh due NOW);
    "warn" = reports within EARNINGS_UPCOMING_DAYS, or no calendar entry,
    or the calendar covers a different quarter than it should; "ok" = dated,
    in the future, nothing to do yet.
    """
    today = today or date.today()
    meta, cal = load_earnings_calendar(inputs_dir)
    if not meta and not cal:
        return [CheckItem(label="(calendar)", status="warn",
                          detail="inputs/earnings_calendar.yaml missing — "
                                 "build it before earnings season")]
    cal_quarter = meta.get("quarter")
    items: list[CheckItem] = []
    for ticker in watchlist:
        entry = cal.get(ticker)
        if not isinstance(entry, dict):
            items.append(CheckItem(label=ticker, status="warn",
                                   detail="no earnings date on file"))
            continue
        start = entry.get("window_start")
        end = entry.get("window_end") or start
        status_word = entry.get("status", "expected")
        basis = entry.get("basis", "")
        bs_path = (inputs_dir / "balance_sheets"
                   / f"{ticker.lower()}_{cal_quarter}.yaml")
        when = f"{start} → {end}" if start != end else f"{start}"
        if start and today >= start and not bs_path.exists():
            verb = ("report window open" if end and today <= end
                    else "report OUT")
            items.append(CheckItem(
                label=ticker, status="missing",
                detail=f"{verb} ({when}, {status_word}) and no "
                       f"{cal_quarter} balance sheet on file — refresh due. {basis}"))
        elif start and 0 <= (start - today).days <= EARNINGS_UPCOMING_DAYS:
            items.append(CheckItem(
                label=ticker, status="warn",
                detail=f"reports in {(start - today).days}d "
                       f"({when}, {status_word}). {basis}"))
        else:
            items.append(CheckItem(
                label=ticker, status="ok",
                detail=f"{when} ({status_word}). {basis}"))
    return items


def check_reweight_triggers(
    inputs_dir: Path = INPUTS_DIR, today: date | None = None,
) -> list[CheckItem]:
    """One CheckItem per trigger in inputs/reweight_triggers.yaml (§13.3
    operationalized — audit F-2: the prose trigger fired Jun-17 and sat 15 days).

    Statuses: "missing" = trigger DUE/overdue or FIRED (a §13.3 decision is
    owed NOW); "warn" = due within TRIGGER_UPCOMING_DAYS; "ok" = armed with a
    future date, a standing event-watch, or done/retired.
    """
    today = today or date.today()
    path = inputs_dir / "reweight_triggers.yaml"
    if not path.exists():
        return [CheckItem(label="(triggers)", status="warn",
                          detail="inputs/reweight_triggers.yaml missing — the §13.3 "
                                 "triggers are unwatched (the Jun-17 miss, again)")]
    doc = yaml.safe_load(path.read_text()) or {}
    items: list[CheckItem] = []
    for name, entry in doc.items():
        if not isinstance(entry, dict):
            continue
        status = entry.get("status", "armed")
        due = entry.get("due")
        sector = entry.get("sector", "?")
        obs = " ".join(str(entry.get("observable", "")).split())[:140]
        if status == "fired":
            items.append(CheckItem(label=name, status="missing",
                                   detail=f"[{sector}] FIRED — §13.3 reweight decision OWED. {obs}"))
        elif status in ("done", "retired"):
            items.append(CheckItem(label=name, status="ok",
                                   detail=f"[{sector}] {status}"))
        elif due and today >= due:
            items.append(CheckItem(label=name, status="missing",
                                   detail=f"[{sector}] DUE {due} — check the observable and "
                                          f"record the outcome. {obs}"))
        elif due and 0 <= (due - today).days <= TRIGGER_UPCOMING_DAYS:
            items.append(CheckItem(label=name, status="warn",
                                   detail=f"[{sector}] due in {(due - today).days}d ({due}). {obs}"))
        else:
            when = f"due {due}" if due else "standing event-watch"
            items.append(CheckItem(label=name, status="ok",
                                   detail=f"[{sector}] {when}. {obs}"))
    return items


def check_balance_sheets(
    target_quarter: str, watchlist: dict, inputs_dir: Path = INPUTS_DIR,
    today: date | None = None,
) -> list[CheckItem]:
    """One CheckItem per watchlist ticker: balance sheet present for the target
    quarter or missing. Missing items carry a "pull from {ir_url}" hint.
    """
    today = today or date.today()
    items: list[CheckItem] = []
    for ticker in watchlist:
        bs_path = inputs_dir / "balance_sheets" / f"{ticker.lower()}_{target_quarter}.yaml"
        if bs_path.exists():
            days = _days_since(bs_path, today)
            items.append(CheckItem(
                label=ticker, status="ok",
                detail=f"balance_sheets/{bs_path.name} (modified {days}d ago)",
            ))
        else:
            items.append(CheckItem(
                label=ticker, status="missing",
                detail=f"expected balance_sheets/{bs_path.name}",
            ))
    return items


def check_market_data(
    inputs_dir: Path = INPUTS_DIR, today: date | None = None,
    threshold_days: int = MARKET_DATA_STALE_DAYS,
) -> list[CheckItem]:
    """One CheckItem per monitored market_data file."""
    today = today or date.today()
    items: list[CheckItem] = []
    for fname in MARKET_DATA_FILES:
        path = inputs_dir / "market_data" / fname
        days = _days_since(path, today)
        if days is None:
            items.append(CheckItem(
                label=fname, status="missing",
                detail=f"expected market_data/{fname}",
            ))
        elif days > threshold_days:
            items.append(CheckItem(
                label=fname, status="stale",
                detail=f"market_data/{fname} ({days}d old, threshold {threshold_days}d)",
            ))
        else:
            items.append(CheckItem(
                label=fname, status="ok",
                detail=f"market_data/{fname} ({days}d old)",
            ))
    return items


def check_watchlist_freshness(
    watchlist: dict, today: date | None = None,
    threshold_days: int = WATCHLIST_STALE_DAYS,
) -> list[CheckItem]:
    """Per-ticker as_of freshness and APPROX consensus_pnav flags.

    The watchlist YAML stores ``as_of: 2026-05-29`` per ticker; this surfaces
    the days-since-as_of figure. Additionally, the loader's convention is that
    APPROX consensus_pnav entries are flagged in the YAML comments (e.g.
    ``consensus_pnav: 0.75     # APPROX -- replace with Pareto figure``). We
    detect those by scanning the raw YAML text — imperfect (depends on the
    ``APPROX`` token in comments) but cheap and reliable in practice.
    """
    today = today or date.today()
    items: list[CheckItem] = []

    # Re-read the raw YAML to scan for "APPROX" annotations in comments.
    watchlist_text = (INPUTS_DIR / "watchlist.yaml").read_text()

    for ticker, entry in watchlist.items():
        as_of = entry.get("as_of")
        if isinstance(as_of, date):
            days = (today - as_of).days
        elif isinstance(as_of, str):
            try:
                days = (today - date.fromisoformat(as_of)).days
            except ValueError:
                days = None
        else:
            days = None

        # APPROX detection: scan the per-ticker block of the YAML for the
        # token. The watchlist block is small enough that we can isolate the
        # ticker's lines by splitting on "{TICKER}:" and taking the next block
        # until the next top-level key.
        approx = _ticker_block_contains_approx(watchlist_text, ticker)

        # Combine: stale if days > threshold; approx if APPROX flagged
        # (regardless of staleness, since APPROX is a separate dimension).
        if approx:
            status = "approx"
            detail = f"as_of {as_of} ({days}d ago); consensus_pnav flagged APPROX in comment — replace with Pareto / broker figure"
        elif days is None:
            status = "warn"
            detail = "as_of missing or unparseable"
        elif days > threshold_days:
            status = "stale"
            detail = f"as_of {as_of} ({days}d ago, threshold {threshold_days}d)"
        else:
            status = "ok"
            detail = f"as_of {as_of} ({days}d ago)"
        items.append(CheckItem(label=ticker, status=status, detail=detail))
    return items


def _ticker_block_contains_approx(text: str, ticker: str) -> bool:
    """True if the per-ticker watchlist block contains the ``APPROX`` token.

    The watchlist YAML format is:
        TICKER:
          current_price: X     # comment may include APPROX
          analyst_target: Y
          consensus_pnav: Z    # comment may include APPROX
          ...
    A block ends at the next top-level key (a line starting at column 0 that
    isn't a comment or blank). We slice the text between the ticker's header
    line and the next top-level key, then look for ``APPROX``.
    """
    import re
    pattern = re.compile(rf"^{re.escape(ticker)}:\s*$", re.MULTILINE)
    m = pattern.search(text)
    if not m:
        return False
    start = m.end()
    # Find next top-level key: a line at col 0 that's alphanumeric (not " " or "#")
    # and ends with ":". Includes the ticker itself if there's repetition — handled.
    rest = text[start:]
    next_match = re.search(r"^\S", rest, re.MULTILINE)
    block = rest[:next_match.start()] if next_match else rest
    return "APPROX" in block


def collect_per_ticker_ages(
    watchlist: dict, target_quarter: str,
    inputs_dir: Path = INPUTS_DIR, today: date | None = None,
) -> list[TickerFileAges]:
    """Per-ticker file modification ages across fleet / BS / cost / dividend."""
    today = today or date.today()
    out: list[TickerFileAges] = []
    for ticker in watchlist:
        t = ticker.lower()
        bs_path = inputs_dir / "balance_sheets" / f"{t}_{target_quarter}.yaml"
        out.append(TickerFileAges(
            ticker=ticker,
            fleet_days=_days_since(inputs_dir / "fleet_manifests" / f"{t}.yaml", today),
            balance_sheet_days=_days_since(bs_path, today),
            balance_sheet_present=bs_path.exists(),
            cost_days=_days_since(inputs_dir / "cost_structures" / f"{t}.yaml", today),
            dividend_days=_days_since(inputs_dir / "dividend_policies" / f"{t}.yaml", today),
        ))
    return out


def load_data_sources(path: Path = DATA_SOURCES_PATH) -> dict:
    """Load inputs/data_sources.yaml — per-ticker IR URLs + reporting pattern."""
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text()) or {}


# ----------------------------------------------------------------------------
# Assembly
# ----------------------------------------------------------------------------
def build_checklist(
    target_quarter: str | None = None,
    today: date | None = None,
    inputs_dir: Path = INPUTS_DIR,
) -> Checklist:
    """Assemble the full checklist from the input file tree + data sources."""
    from crude_tanker_fv.loaders import load_watchlist

    today = today or date.today()
    target_quarter = target_quarter or infer_target_quarter(today)
    watchlist = load_watchlist(inputs_dir)
    sources = load_data_sources()

    return Checklist(
        today=today.isoformat(),
        target_quarter=target_quarter,
        balance_sheets=check_balance_sheets(target_quarter, watchlist, inputs_dir, today),
        market_data=check_market_data(inputs_dir, today),
        watchlist=check_watchlist_freshness(watchlist, today),
        earnings=check_earnings_calendar(target_quarter, watchlist, inputs_dir, today),
        reweight_triggers=check_reweight_triggers(inputs_dir, today),
        per_ticker_ages=collect_per_ticker_ages(watchlist, target_quarter, inputs_dir, today),
        data_sources=sources,
    )


# ----------------------------------------------------------------------------
# Markdown rendering
# ----------------------------------------------------------------------------
def write_checklist(checklist: Checklist, outputs_dir: Path = OUTPUTS_DIR) -> Path:
    """Render the checklist to outputs/refresh_checklist.md and return path."""
    outputs_dir.mkdir(parents=True, exist_ok=True)
    path = outputs_dir / "refresh_checklist.md"
    path.write_text(_render_checklist_md(checklist))
    return path


def _render_checklist_md(c: Checklist) -> str:
    lines: list[str] = []
    lines.append(f"# Refresh Checklist — {c.target_quarter} (target quarter)\n")
    lines.append(f"- **Today:** {c.today}")
    lines.append(f"- **Target quarter:** {c.target_quarter}")
    lines.append("- **Workflow:** work through the sections below, then run "
                 "`python -m crude_tanker_fv.pipeline` to refresh outputs.\n")

    # --- Status summary ---
    lines.append("## Status summary\n")
    bs_total = len(c.balance_sheets)
    bs_present = bs_total - c.missing_bs_count
    md_total = len(c.market_data)
    md_ok = md_total - c.stale_md_count
    wl_total = len(c.watchlist)
    wl_clean = sum(1 for w in c.watchlist if w.status == "ok")
    lines.append(f"- {_check(bs_present == bs_total)} **Balance sheets:** "
                 f"{bs_present} of {bs_total} present for {c.target_quarter}"
                 + (f" — missing: {', '.join(c.label for c in c.balance_sheets if c.status == 'missing')}"
                    if c.missing_bs_count else ""))
    lines.append(f"- {_check(c.stale_md_count == 0)} **Market data:** "
                 f"{md_ok} of {md_total} fresh (< {MARKET_DATA_STALE_DAYS} days)"
                 + (f" — stale: {', '.join(it.label for it in c.market_data if it.status == 'stale')}"
                    if c.stale_md_count else ""))
    lines.append(f"- {_check(wl_clean == wl_total)} **Watchlist:** "
                 f"{wl_clean} of {wl_total} clean"
                 + (f" — {c.stale_watchlist_count} stale, {c.approx_watchlist_count} APPROX consensus_pnav"
                    if (c.stale_watchlist_count + c.approx_watchlist_count) else ""))
    due = [it.label for it in c.earnings if it.status == "missing"]
    soon = [it.label for it in c.earnings if it.status == "warn"]
    lines.append(f"- {_check(not due)} **Earnings:** "
                 + (f"REFRESH DUE: {', '.join(due)}" if due else "no reports outstanding")
                 + (f" — upcoming/check: {', '.join(soon)}" if soon else ""))
    t_due = [it.label for it in c.reweight_triggers if it.status == "missing"]
    t_soon = [it.label for it in c.reweight_triggers if it.status == "warn"]
    lines.append(f"- {_check(not t_due)} **§13.3 reweight triggers:** "
                 + (f"DUE/FIRED: {', '.join(t_due)}" if t_due
                    else "none due")
                 + (f" — upcoming: {', '.join(t_soon)}" if t_soon else ""))
    lines.append("")

    # --- Section 0a: Scenario-weight triggers (§13.3 — audit F-2) ---
    lines.append("## 0a. Scenario-weight re-evaluation triggers "
                 "(`inputs/reweight_triggers.yaml`)\n")
    lines.append("| Trigger | Status | Detail |")
    lines.append("|---|---|---|")
    torder = {"missing": 0, "warn": 1, "ok": 2}
    for it in sorted(c.reweight_triggers, key=lambda i: (torder.get(i.status, 3), i.label)):
        flag = {"missing": "🔴 DUE", "warn": "🟡", "ok": "—"}.get(it.status, "?")
        lines.append(f"| {it.label} | {flag} | {it.detail} |")
    lines.append("")

    # --- Section 0: Earnings calendar ---
    lines.append("## 0. Earnings calendar (report-day refresh runbook in CLAUDE.md)\n")
    lines.append("| Ticker | Status | Detail |")
    lines.append("|---|---|---|")
    order = {"missing": 0, "warn": 1, "ok": 2}
    for it in sorted(c.earnings, key=lambda i: (order.get(i.status, 3), i.label)):
        flag = {"missing": "🔴 DUE", "warn": "🟡", "ok": "—"}.get(it.status, "?")
        lines.append(f"| {it.label} | {flag} | {it.detail} |")
    lines.append("")

    # --- Section 1: Missing balance sheets + IR playbook ---
    lines.append("## 1. Missing quarterly balance sheets\n")
    missing = [it for it in c.balance_sheets if it.status == "missing"]
    if not missing:
        lines.append(f"_All watchlist tickers have a balance sheet on file for "
                     f"{c.target_quarter}. ✓_\n")
    else:
        lines.append(f"For each missing name below, pull the {c.target_quarter} "
                     f"results from the listed IR URLs and populate "
                     f"`inputs/balance_sheets/{{ticker}}_{c.target_quarter}.yaml`:\n")
        for it in missing:
            src = c.data_sources.get(it.label, {})
            lines.append(f"### {it.label}")
            if src.get("press_releases"):
                lines.append(f"- **Press releases:** {src['press_releases']}")
            if src.get("sec_edgar"):
                lines.append(f"- **SEC EDGAR filings:** {src['sec_edgar']}")
            if src.get("fleet_page"):
                lines.append(f"- **Fleet page:** {src['fleet_page']}")
            if src.get("reporting_pattern"):
                lines.append(f"- **Reporting pattern:** {src['reporting_pattern']}")
            if src.get("notes"):
                lines.append(f"- **Notes:** {src['notes']}")
            if not src:
                lines.append("- _(no data_sources.yaml entry — add one to populate IR URLs)_")
            lines.append("")

    # --- Section 2: Stale market data ---
    lines.append("## 2. Stale market data\n")
    stale_md = [it for it in c.market_data if it.status == "stale"]
    missing_md = [it for it in c.market_data if it.status == "missing"]
    if not stale_md and not missing_md:
        lines.append(f"_All market data files were updated within "
                     f"{MARKET_DATA_STALE_DAYS} days. ✓_\n")
    else:
        lines.append("| File | Status | Detail |")
        lines.append("|---|---|---|")
        for it in stale_md + missing_md:
            badge = "⚠ stale" if it.status == "stale" else "✗ missing"
            lines.append(f"| `{it.label}` | {badge} | {it.detail} |")
        lines.append("")
        lines.append("Refresh sources: spot TCE + 12M TC + FFA from Pareto "
                     "Shipping Daily / Baltic Exchange / Clarksons; vessel "
                     "value curves from VesselsValue / Clarksons SIN.\n")

    # --- Section 3: Watchlist freshness ---
    lines.append("## 3. Watchlist freshness\n")
    lines.append("| Ticker | as_of status | Detail |")
    lines.append("|---|---|---|")
    for it in c.watchlist:
        badge = {
            "ok": "✓", "stale": "⚠ stale", "approx": "⚠ APPROX",
            "warn": "⚠ missing", "missing": "✗ missing",
        }.get(it.status, it.status)
        lines.append(f"| {it.label} | {badge} | {it.detail} |")
    lines.append("")
    if c.approx_watchlist_count:
        lines.append(f"_{c.approx_watchlist_count} ticker(s) carry APPROX "
                     "consensus_pnav comments — replace with authoritative "
                     "broker NAV print (Pareto / Cleaves / Clarksons) when the "
                     "Q-end research notes land._\n")

    # --- Section 4: Per-ticker file ages ---
    lines.append("## 4. Per-ticker file age table\n")
    lines.append("| Ticker | Fleet (≤90d) | BS for " + c.target_quarter + " | Cost (≤180d) | Dividend (≤180d) |")
    lines.append("|---|---|---|---|---|")
    for t in c.per_ticker_ages:
        fleet = _age_cell(t.fleet_days, FLEET_STALE_DAYS)
        bs = "✓ present" if t.balance_sheet_present else "✗ missing"
        if t.balance_sheet_present and t.balance_sheet_days is not None:
            bs = f"✓ {t.balance_sheet_days}d ago"
        cost = _age_cell(t.cost_days, COST_DIVIDEND_STALE_DAYS)
        div = _age_cell(t.dividend_days, COST_DIVIDEND_STALE_DAYS)
        lines.append(f"| {t.ticker} | {fleet} | {bs} | {cost} | {div} |")
    lines.append("")
    lines.append(f"_Thresholds: fleet manifest {FLEET_STALE_DAYS}d (vessel "
                 f"sales/purchases happen quarterly); cost + dividend "
                 f"{COST_DIVIDEND_STALE_DAYS}d (rarely change but should "
                 f"be re-validated annually)._\n")

    # --- Section 5: Full IR URL playbook ---
    lines.append("## 5. IR URL playbook (all watchlist)\n")
    lines.append("For ad-hoc lookups outside the refresh cycle:\n")
    lines.append("| Ticker | IR home | Press releases | SEC EDGAR | Fleet page |")
    lines.append("|---|---|---|---|---|")
    for it in c.balance_sheets:
        src = c.data_sources.get(it.label, {})
        ir_home = src.get("ir_home") or "—"
        pr = src.get("press_releases") or "—"
        edgar = src.get("sec_edgar") or "—"
        fleet = src.get("fleet_page") or "—"
        # Shorten cell rendering — for URLs use bare links so markdown stays scannable
        lines.append(f"| {it.label} | {ir_home} | {pr} | {edgar} | {fleet} |")
    lines.append("")

    return "\n".join(lines)


def _check(ok: bool) -> str:
    return "✓" if ok else "⚠"


def _age_cell(days: int | None, threshold: int) -> str:
    if days is None:
        return "✗ missing"
    if days > threshold:
        return f"⚠ {days}d"
    return f"✓ {days}d"


# ----------------------------------------------------------------------------
# CLI entry
# ----------------------------------------------------------------------------
def main() -> None:
    """``python -m crude_tanker_fv.refresh [quarter]`` — write the checklist."""
    target_quarter = sys.argv[1] if len(sys.argv) > 1 else None
    today = date.today()
    checklist = build_checklist(target_quarter=target_quarter, today=today)
    path = write_checklist(checklist)
    # Print a one-line summary for terminal scanning.
    print(f"refresh checklist for {checklist.target_quarter} -> {path}")
    print(f"  balance sheets:    {len(checklist.balance_sheets) - checklist.missing_bs_count}/{len(checklist.balance_sheets)} present")
    print(f"  market data:       {len(checklist.market_data) - checklist.stale_md_count}/{len(checklist.market_data)} fresh (<{MARKET_DATA_STALE_DAYS}d)")
    print(f"  watchlist clean:   {sum(1 for w in checklist.watchlist if w.status == 'ok')}/{len(checklist.watchlist)}")


if __name__ == "__main__":
    main()
