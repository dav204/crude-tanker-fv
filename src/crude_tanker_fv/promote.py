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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="the promoter (check-only for now)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="read-only: is the standing drift auto-absorbable?")
    c.add_argument("--json", action="store_true", help="machine-readable verdict")
    args = ap.parse_args(argv)

    if args.cmd == "check":
        v = evaluate_price_absorb()
        print(json.dumps(v.as_dict(), indent=1) if args.json else v.render())
        return 0 if v.ok else 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
