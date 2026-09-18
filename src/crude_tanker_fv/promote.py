"""The promoter — bounded, predicate-gated absorption of routine drift.

    python -m crude_tanker_fv.promote check          # read-only verdict, exit 0/1
    python -m crude_tanker_fv.promote check --json   # machine form (the report reads this)

STATUS: `check` only. It evaluates, it never writes and never lands. Landing (worktree →
commit-inputs-first → regen → comparator → gate → bounded ratify → suite → ff-merge) is the
next build; the predicate below is deliberately the SAME code both will use, so the day
authority is granted nothing about the decision changes except who executes it.

THE ONE QUESTION IT ANSWERS — "is the standing drift a one-word ratify, or does it need the
owner's eye?" That question is asked at every sitting, and answering it by hand means reading
the whole gate table. The predicate is the repo's own written rules, not a new judgment:

  LANE D (price-vintage absorb), all conjuncts required —
    1. every drift-gate row is `stable`, or its breaches are EV%-ONLY with ΔNAV exactly 0.0
       (the price leg moves the denominator, never the asset value — the shape every
       price-vintage ratify in RATIFY_LOG.md has taken since 2026-07-10)
    2. no band EXIT — a band flip whose price sits OUTSIDE the fv_low/fv_high interval is a
       real re-read, not a mechanical crossing (D-M5, 2026-07-15)
    3. no flip TOWARD BUY — the standing halt-and-investigate rule; a machine may never walk
       a name into the actionable set
    4. |Δk_broker| ≤ the baseline's own threshold (the second-difference gate)
    5. the tree carries no NON-drift dirt (the owner is not mid-surgery)

  Anything else FREEZES to the owner, with the reason named. A freeze is the design working,
  not a failure.

Read-only by construction: it opens the committed baseline, `state/last_run.json` and
`git status`, and writes nothing at all.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


@dataclass
class Verdict:
    lane: str
    ok: bool
    conjuncts: list[tuple[str, bool, str]] = field(default_factory=list)
    freeze_reasons: list[str] = field(default_factory=list)
    rows_considered: int = 0
    buyward: list = field(default_factory=list)   # (ticker, band_to) flips awaiting a fork

    def as_dict(self) -> dict:
        return {"lane": self.lane, "ok": self.ok, "rows_considered": self.rows_considered,
                "conjuncts": [{"name": n, "passed": p, "detail": d} for n, p, d in self.conjuncts],
                "freeze_reasons": self.freeze_reasons}

    def render(self) -> str:
        head = (f"LANE {self.lane}: {'AUTO-ABSORBABLE' if self.ok else 'FREEZE — owner word needed'}"
                f"  ({self.rows_considered} gate row(s))")
        lines = [head, ""]
        for name, passed, detail in self.conjuncts:
            lines.append(f"  [{'PASS' if passed else 'FAIL'}] {name}: {detail}")
        if self.freeze_reasons:
            lines += ["", "  Why it stops here:"]
            lines += [f"    - {r}" for r in self.freeze_reasons]
        return "\n".join(lines)


def _non_drift_dirt(root: Path = ROOT) -> list[str]:
    """Working-tree paths that are NOT on the automation-drift list."""
    allowed = set()
    dl = root / "scripts" / "drift_files.txt"
    if dl.exists():
        allowed = {ln.strip() for ln in dl.read_text().splitlines()
                   if ln.strip() and not ln.startswith("#")}
    try:
        out = subprocess.run(["git", "status", "--porcelain"], cwd=root,
                             capture_output=True, text=True, check=True).stdout
    except Exception:
        return ["git status unavailable"]
    dirt = []
    for line in out.splitlines():
        if not line.strip():
            continue
        path = line[3:].strip()
        if path not in allowed:
            dirt.append(path)
    return dirt


def evaluate_price_absorb(root: Path = ROOT) -> Verdict:
    from . import drift_gate

    v = Verdict(lane="D (price-vintage absorb)", ok=False)
    baseline_path = root / "baselines" / "reconcile_baseline.yaml"
    state_path = root / "state" / "last_run.json"
    if not baseline_path.exists() or not state_path.exists():
        v.conjuncts.append(("inputs present", False,
                            "baseline or state/last_run.json missing — run the pipeline first"))
        v.freeze_reasons.append("cannot evaluate: no committed baseline or no run state")
        return v

    baseline = drift_gate.load_baseline(baseline_path)
    state = json.loads(state_path.read_text())
    rows = drift_gate.evaluate(baseline, state)
    v.rows_considered = len(rows)
    thresholds = baseline.get("thresholds") or drift_gate.DEFAULT_THRESHOLDS

    # A name whose DISPLAYED position is a governed relabel never counts as BUY-ward: its
    # raw band is not what the book acts on (POSITION_UNRELIABLE / POSITION_CYCLE_RELABEL,
    # provenance.py). Reading the raw band instead would freeze this lane forever on
    # CAPT/BRUT/TNK/MPCC — safe, but permanently useless.
    from .provenance import POSITION_CYCLE_RELABEL, POSITION_UNRELIABLE
    relabelled = set(POSITION_CYCLE_RELABEL) | set(POSITION_UNRELIABLE)

    moved = [r for r in rows if r.status != "stable"]
    ev_only, nav_movers, band_exits, buyward, k_breaches = [], [], [], [], []
    for r in moved:
        breaches = set(r.breaches or [])
        if r.d_nav_pct is not None and abs(r.d_nav_pct) > 0.0:
            nav_movers.append(f"{r.ticker} ΔNAV {r.d_nav_pct:+.2f}%")
        if breaches and breaches <= {"ev_pct"}:
            ev_only.append(r.ticker)
        if r.band_from and r.band_to and r.band_from != r.band_to:
            if "band-mech" not in " ".join(r.breaches or []):
                band_exits.append(f"{r.ticker} {r.band_from} → {r.band_to}")
            if str(r.band_to).upper().startswith("BUY") and r.ticker not in relabelled:
                buyward.append(f"{r.ticker} → {r.band_to}")
        if r.d_k is not None and abs(r.d_k) > float(thresholds.get("k_broker", 0.05)):
            k_breaches.append(f"{r.ticker} Δk {r.d_k:+.3f}")

    c1 = not nav_movers
    v.conjuncts.append(("EV-only (ΔNAV exactly 0.0 on every row)", c1,
                        "no row moved NAV" if c1 else "; ".join(nav_movers)))
    if not c1:
        v.freeze_reasons.append("a NAV move is a SOURCING event, not a price vintage — it needs "
                                "its own cause and an owner ratify")

    c2 = not band_exits
    v.conjuncts.append(("no band EXIT", c2,
                        "no band crossing outside its interval" if c2 else "; ".join(band_exits)))
    if not c2:
        v.freeze_reasons.append("a band EXIT is a real re-read (D-M5), not a mechanical crossing")

    c3 = not buyward
    v.conjuncts.append(("no flip toward BUY (displayed position, relabels excluded)", c3,
                        "nothing walked into the actionable set" if c3 else "; ".join(buyward)))
    if not c3:
        v.freeze_reasons.append("flip toward BUY — standing halt-and-investigate rule; a machine "
                                "never walks a name into the long set")

    c4 = not k_breaches
    v.conjuncts.append((f"|Δk| ≤ {thresholds.get('k_broker', 0.05)}", c4,
                        "tool↔broker relationship unchanged" if c4 else "; ".join(k_breaches)))
    if not c4:
        v.freeze_reasons.append("a k_broker second-difference breach means the relationship to the "
                                "tape moved — explain it, don't absorb it")

    dirt = _non_drift_dirt(root)
    c5 = not dirt
    v.conjuncts.append(("tree carries only automation drift", c5,
                        "clean apart from the drift list" if c5 else f"non-drift dirt: {', '.join(dirt[:5])}"))
    if not c5:
        v.freeze_reasons.append("the working tree is mid-surgery — automation never runs through it")

    unexplained = [r.ticker for r in rows if r.status == "UNEXPLAINED"]
    v.conjuncts.append(("gate rows accounted for", True,
                        f"{len(moved)} moved, {len(ev_only)} EV-only, "
                        f"{len(unexplained)} UNEXPLAINED"))

    v.ok = c1 and c2 and c3 and c4 and c5
    if v.ok and not moved:
        v.freeze_reasons.append("(nothing to absorb — the gate is quiet)")
    return v


# --------------------------------------------------------------------------------------
# LANE LAND — auto-ratify (owner ruling 2026-09-10: "go build the rest"; the landing lane
# of decisions/autopilot_authority_2026-09-02.md §6). Advances the committed baseline through
# scripts/ratify_baseline.sh when, and ONLY when, the standing drift is fully explained:
#
#   (a) the drift gate reads 0 UNEXPLAINED;
#   (b) every non-stable row's decision log carries a HUMAN annotation dated on/after the
#       baseline's ratified date (drift_gate.decision_log_annotated_since — the same reader
#       the gate uses, so the lane cannot "explain" what the gate would not);
#   (c) the working tree carries only automation-drift paths (_non_drift_dirt);
#   (d) no row flipped TOWARD BUY vs the baseline (relabels excluded, as in Lane D);
#   (e) the committed surface IS the surface being ratified: outputs/book_scorecard.json's
#       source_commit equals HEAD, and state/last_run.json is younger than 24h.
#
# The CAUSE is composed from the record, never typed: the first sentence of each explained
# row's top Decision line, deduplicated, capped, pointing at the logs. Placeholders never
# reach the cause (a row with one is UNEXPLAINED, so (a) already refuses it).
#
# `land --dry-run` prints the verdict, the cause and the would-run command, exits 0, runs
# nothing. `land` runs the ratify script and commits its two files. Not wired into cron —
# that is an owner-visible step.
# --------------------------------------------------------------------------------------

CAUSE_CAP = 400
STATE_MAX_AGE_HOURS = 24


def _git(root: Path, *args: str) -> str:
    try:
        return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return ""


def _git_ok(root: Path, *args: str) -> bool:
    try:
        return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True).returncode == 0
    except Exception:
        return False


# Source ARCHIVES under inputs/ (staged filings, issuer/broker research) are read by agents,
# never by the pipeline — a saved press release must not freeze the lane. PROCESS files under
# inputs/ are likewise not determinants (2026-09-15): the fork registry, the notify routing table,
# the trigger cards, the source/coverage config, the earnings calendar and the duty roster change
# no number the pipeline computes. Executing a fork writes forks.yaml, which froze this lane the
# moment the executor did its job. The test of a determinant is whether the pipeline reads it into
# a valuation. ONE list, two readers: annotate.determinant_changes measures its price-leg proof
# over the same window this exclusion defines (guarded by tests/test_annotate.py).
DETERMINANT_EXCLUDES = (
    ":(exclude)inputs/filings", ":(exclude)inputs/research_issuer",
    ":(exclude)inputs/research_pareto", ":(exclude)inputs/research_pareto_other",
    ":(exclude)inputs/research_mb", ":(exclude)inputs/ffa_drybulk",
    ":(exclude)inputs/forks.yaml", ":(exclude)inputs/notify.yaml",
    ":(exclude)inputs/reweight_triggers.yaml", ":(exclude)inputs/data_sources.yaml",
    ":(exclude)inputs/rocketchat_sources.yaml", ":(exclude)inputs/archive_gaps.yaml",
    ":(exclude)inputs/earnings_calendar.yaml", ":(exclude)inputs/agent_duties.yaml",
)

# Paths under inputs/ that feed NO valuation and cannot be excluded by pathspec: the sp_scan
# cursor (sp_scan + the sentinel staleness check read it, the pipeline does not) and the
# shadow-build / rebase drafts (CLAUDE.md drafts-only — the pipeline reads the .yaml, never the
# .yaml.draft, and a draft may sit anywhere under inputs/).
NON_DETERMINANT_INPUTS = ("inputs/market_data/transactions/_scan_state.json",)
NON_DETERMINANT_SUFFIX = ".yaml.draft"


def is_non_determinant(path: str) -> bool:
    return path.endswith(NON_DETERMINANT_SUFFIX) or path in NON_DETERMINANT_INPUTS


def determinant_paths(root: Path, frm: str, to: str = "HEAD") -> "list[str]":
    """The determinant paths that moved between two commits — THE definition, THREE readers:
    (e) below, the annotator's price-leg proof, and the cron's regen trigger. A reader that
    builds its own copy can call a morning current that another calls contaminated (2026-09-18:
    a shadow build's *.yaml.draft froze (e) while the annotator ignored it)."""
    out = _git(root, "diff", "--name-only", frm, to, "--", "src", "inputs", *DETERMINANT_EXCLUDES)
    return [q for q in (ln.strip() for ln in out.splitlines()) if q and not is_non_determinant(q)]


def _surface_matches_head(root: Path) -> "tuple[bool, str]":
    """(e): the committed decision surface must be CURRENT for HEAD.

    The repo's own pattern is inputs commit -> regen -> outputs commit, so the surface's
    source_commit is normally an ANCESTOR of HEAD, not HEAD itself. Current means: the stamp
    is clean, it is reachable from HEAD, and no determinant (src/, inputs/) changed between
    the stamp and HEAD — anything else would ratify numbers the tree no longer produces.
    """
    sc = root / "outputs" / "book_scorecard.json"
    if not sc.exists():
        return False, "outputs/book_scorecard.json missing"
    stamp = str(json.loads(sc.read_text()).get("source_commit") or "")
    head = _git(root, "rev-parse", "--short", "HEAD")
    if not stamp or not head:
        return False, f"stamp={stamp!r} head={head!r}"
    if stamp.endswith("-dirty"):
        return False, f"surface stamped dirty ({stamp})"
    if not _git_ok(root, "merge-base", "--is-ancestor", stamp, "HEAD"):
        return False, f"surface {stamp} is not an ancestor of HEAD {head}"
    changed = determinant_paths(root, stamp, "HEAD")
    if changed:
        return False, (f"determinants changed since the surface {stamp}: "
                       + ", ".join(changed[:6])
                       + (f" (+{len(changed) - 6} more)" if len(changed) > 6 else ""))
    return True, f"surface {stamp} current for HEAD {head}"


def _state_is_fresh(root: Path, now=None) -> "tuple[bool, str]":
    from datetime import datetime, timedelta, timezone

    p = root / "state" / "last_run.json"
    if not p.exists():
        return False, "state/last_run.json missing"
    run_at = str(json.loads(p.read_text()).get("run_at") or "")
    try:
        ts = datetime.fromisoformat(run_at)
    except ValueError:
        return False, f"unparseable run_at {run_at!r}"
    if ts.tzinfo is None:
        ts = ts.replace(tzinfo=timezone.utc)
    now = now or datetime.now(timezone.utc)
    age = now - ts
    return age <= timedelta(hours=STATE_MAX_AGE_HOURS), f"last run {run_at} ({age.total_seconds()/3600:.1f}h old)"


def _first_decision_sentence(ticker: str, decisions_dir: Path) -> str:
    """The first sentence of the TOP entry's Decision line — the record's own words."""
    from . import drift_gate

    path = decisions_dir / f"{ticker.lower()}_log.md"
    if not path.exists():
        return ""
    lines = path.read_text().splitlines()
    idx = next((i for i, ln in enumerate(lines) if drift_gate._HEADER_RE.match(ln)), None)
    if idx is None:
        return ""
    for ln in lines[idx + 1:]:
        if drift_gate._HEADER_RE.match(ln):
            break
        s = ln.strip()
        if s.startswith("**Decision:**"):
            body = s[len("**Decision:**"):].strip().strip("*_ ").strip()
            if not body or drift_gate._PLACEHOLDER in body.lower():
                return ""
            cut = body.find(". ")
            return (body[:cut + 1] if 0 < cut < 200 else body[:200]).strip()
    return ""


def compose_cause(rows, decisions_dir: Path, today=None) -> str:
    from datetime import date as _date

    today = today or _date.today()
    seen, parts = set(), []
    for r in rows:
        if r.status != "explained":
            continue
        s = _first_decision_sentence(r.ticker, decisions_dir)
        if s and s not in seen:
            seen.add(s)
            parts.append(s)
    head = f"auto-land {today.isoformat()}: "
    tail = " — full record in decisions/*_log.md"
    body = " · ".join(parts) if parts else "no explained rows (gate quiet)"
    room = CAUSE_CAP - len(head) - len(tail)
    if len(body) > room:
        body = body[:max(0, room - 1)].rstrip() + "…"
    return head + body + tail


def evaluate_land(root: Path = ROOT, now=None) -> "tuple[Verdict, str]":
    from . import drift_gate
    from .provenance import POSITION_CYCLE_RELABEL, POSITION_UNRELIABLE

    v = Verdict(lane="LAND (auto-ratify)", ok=False)
    baseline_path = root / "baselines" / "reconcile_baseline.yaml"
    state_path = root / "state" / "last_run.json"
    if not baseline_path.exists() or not state_path.exists():
        v.conjuncts.append(("inputs present", False, "baseline or state/last_run.json missing"))
        v.freeze_reasons.append("cannot evaluate: no committed baseline or no run state")
        return v, ""
    baseline = drift_gate.load_baseline(baseline_path)
    state = json.loads(state_path.read_text())
    rows = drift_gate.evaluate(baseline, state)
    v.rows_considered = len(rows)
    since = str((baseline.get("meta") or {}).get("ratified_at") or "")[:10]
    decisions_dir = root / "decisions"

    unexplained = [r.ticker for r in rows if r.status == "UNEXPLAINED"]
    a = not unexplained
    v.conjuncts.append(("(a) gate reads 0 UNEXPLAINED", a,
                        "0 UNEXPLAINED" if a else "UNEXPLAINED: " + ", ".join(unexplained)))

    unannotated = [r.ticker for r in rows if r.status != "stable"
                   and not drift_gate.decision_log_annotated_since(r.ticker, since, decisions_dir)]
    b = not unannotated
    v.conjuncts.append((f"(b) every moved row annotated since {since or '?'}", b,
                        "all annotated" if b else "unannotated: " + ", ".join(unannotated)))

    dirt = _non_drift_dirt(root)
    c = not dirt
    v.conjuncts.append(("(c) tree carries only automation drift", c,
                        "clean apart from the drift list" if c else "non-drift dirt: " + ", ".join(dirt[:5])))

    relabelled = set(POSITION_CYCLE_RELABEL) | set(POSITION_UNRELIABLE)
    flips = [(r.ticker, str(r.band_to)) for r in rows
             if r.band_from and r.band_to and r.band_from != r.band_to
             and str(r.band_to).upper().startswith("BUY") and r.ticker not in relabelled]
    # 2026-09-13 (owner: the BUY-flip ratify was the last human ratify): a flip toward BUY
    # is no longer a permanent freeze. The land lane registers a `buyflip_<ticker>_<date>`
    # fork (3 business days, the sentinel pages FORK-EXECUTABLE) and lands once the fork is
    # executed by silence — the halt-and-investigate becomes an objection window.
    executed = _executed_buyflips(root)
    waiting = [(t, b) for t, b in flips if t not in executed]
    buyward = [f"{t} → {b}" for t, b in waiting]
    d = not buyward
    v.buyward = waiting
    covered = [f"{t} → {b} (fork executed)" for t, b in flips if t in executed]
    v.conjuncts.append(("(d) no flip toward BUY without an executed buyflip fork", d,
                        ("none" if not covered else "; ".join(covered)) if d else "; ".join(buyward)))

    e1, e1d = _surface_matches_head(root)
    e2, e2d = _state_is_fresh(root, now)
    e = e1 and e2
    v.conjuncts.append(("(e) committed surface is HEAD's and the run is fresh", e, f"{e1d}; {e2d}"))

    for passed, why in ((a, "an UNEXPLAINED row is exactly what a ratify must never absorb"),
                        (b, "an annotation is the record the cause is composed from"),
                        (c, "the working tree is mid-surgery — automation never lands through it"),
                        (d, "a flip toward BUY waits for its buyflip fork (3 business days of silence)"),
                        (e, "ratifying a surface HEAD did not produce, or a stale one, anchors the wrong numbers")):
        if not passed:
            v.freeze_reasons.append(why)
    v.ok = a and b and c and d and e
    cause = compose_cause(rows, decisions_dir) if v.ok else ""
    return v, cause


def _executed_buyflips(root: Path) -> set:
    """Tickers whose `buyflip_<ticker>_<date>` fork has been executed (silence ran out)."""
    from . import forks as _forks
    path = root / "inputs" / "forks.yaml"
    if not path.exists():
        return set()
    out = set()
    for f in _forks.load(path).get("forks") or []:
        fid = str(f.get("id", ""))
        if fid.startswith("buyflip_") and str(f.get("status")) == "executed":
            out.add(fid.split("_")[1].upper())
    return out


def _register_buyflip(root: Path, ticker: str, band_to: str, *, dry_run: bool) -> str:
    """One fork per ticker flip; idempotent across mornings (an open one is left alone)."""
    from datetime import date as _date
    from . import forks as _forks
    path = root / "inputs" / "forks.yaml"
    if not path.exists():
        return ""
    for f in _forks.load(path).get("forks") or []:
        fid = str(f.get("id", ""))
        if fid.startswith(f"buyflip_{ticker.lower()}_") and str(f.get("status")) in ("open", "executed"):
            return ""
    fid = f"buyflip_{ticker.lower()}_{_date.today().isoformat()}"
    if not dry_run:
        _forks.open_fork(fid, kind="judgment", doc=f"decisions/{ticker.lower()}_log.md",
                         recommendation=(f"land the flip toward {band_to} on {ticker} as the surface computes it "
                                         f"(the drift gate explains it; the standing halt-and-investigate is now "
                                         f"this 3-business-day objection window). Executing = marking this fork "
                                         f"executed; the next auto-land ratifies."),
                         path=path)
    return fid


def land(root: Path = ROOT, dry_run: bool = True, runner=None) -> int:
    """Exit codes for the cron: 0 = landed, or nothing to land; 1 = FREEZE (a precondition
    failed — the normal state while a move awaits its annotation); never anything else."""
    runner = runner or subprocess.run
    v, cause = evaluate_land(root)
    print(v.render())
    if not v.ok:
        for ticker, band_to in v.buyward:
            fid = _register_buyflip(root, ticker, band_to, dry_run=dry_run)
            if fid:
                print(f"FORK {'would be ' if dry_run else ''}REGISTERED: {fid} — lands after 3 business days of silence")
        return 1
    # A quiet gate is not a landing: re-ratifying an unchanged baseline every morning would
    # be a daily noise commit with an empty cause (wired into cron 2026-09-10, owner's word).
    if "no explained rows (gate quiet)" in cause:
        print("NOTHING TO LAND — the gate is quiet; the baseline already describes this surface")
        return 0
    argv = ["scripts/ratify_baseline.sh", cause]
    print()
    print("cause:", cause)
    if dry_run:
        print("DRY RUN — would run:", argv[0], "<cause>")
        return 0
    runner(argv, cwd=root, check=True)
    runner(["git", "add", "baselines/reconcile_baseline.yaml", "RATIFY_LOG.md"], cwd=root, check=True)
    runner(["git", "commit", "-q", "-m", f"baseline: auto-land — {cause}"], cwd=root, check=True)
    print("LANDED — baseline re-ratified and committed")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="the promoter: check (read-only) and land (auto-ratify)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="read-only: is the standing drift auto-absorbable?")
    c.add_argument("--json", action="store_true", help="machine-readable verdict")
    ld = sub.add_parser("land", help="auto-ratify the baseline when every precondition holds")
    ld.add_argument("--dry-run", action="store_true",
                    help="print the verdict, the composed cause and the would-run command; run nothing")
    dt = sub.add_parser("determinants", help="determinant paths that moved between two commits")
    dt.add_argument("frm")
    dt.add_argument("to", nargs="?", default="HEAD")
    args = ap.parse_args(argv)

    if args.cmd == "check":
        v = evaluate_price_absorb()
        print(json.dumps(v.as_dict(), indent=1) if args.json else v.render())
        return 0 if v.ok else 1
    if args.cmd == "land":
        return land(dry_run=args.dry_run)
    if args.cmd == "determinants":
        for path in determinant_paths(ROOT, args.frm, args.to):
            print(path)
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
