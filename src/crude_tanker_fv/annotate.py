"""Deterministic price-attribution annotator — the missing half of the daily land lane.

    python -m crude_tanker_fv.annotate            # report what it WOULD write, write nothing
    python -m crude_tanker_fv.annotate --apply    # write the entries

THE PROBLEM IT CLOSES (2026-09-15). The nightly price refresh writes a determinant, the
morning regen re-reads it, and every name whose EV moved >2pp lands in the drift gate as
UNEXPLAINED carrying the pipeline's `_[pending annotation]_` placeholder. Precondition (a) of
`promote.land` needs 0 UNEXPLAINED, so the committed baseline anchor cannot advance until a
human writes attribution prose — thirteen times in three days, always the same sentence.

WHAT IT IS ALLOWED TO SAY. Exactly one thing: *the tape moved, the valuation did not*. It
annotates a gate row only when the move is PURE PRICE, and REFUSES everything else with the
reason named. A refusal is the design working: the row stays UNEXPLAINED, auto-land freezes on
(a), and a human writes the cause. A machine may never invent one.

THE PREDICATE (all conjuncts required; any failure refuses the row, or the run).

  Run level — measured over the SAME window the gate measures, the baseline anchor to now:
    R1  state/last_run.json's run_at == the surface's generated_at (one run, two files).
    R2  the anchor surface is `git show <baseline.meta.ratified_commit>:outputs/book_scorecard.json`
        and its generated_at == baseline.meta.ratified_at. Anything else is a different window
        than the gate's, so every delta below would describe the wrong number.
    R3  DETERMINANT PROOF — `git diff` from the anchor surface's stamp to this one, over src/
        and inputs/ with promote's own archive/process excludes, touches nothing but the price
        vintage (plus paths no valuation reads: the sp_scan cursor and *.yaml.draft). This is
        structural, not a float comparison, and it is what refuses a curve-promote morning.

  Row level — only rows the gate itself calls UNEXPLAINED:
    P1  breaches ⊆ {EV%, k_broker, band-mech}. A NAV / band / band-EXIT breach is a re-read.
    P2  ΔNAV exactly 0.0 (necessary, nowhere near sufficient — a rate-only or weight-only leg
        also reads 0.0: see decisions/dht_log.md 2026-09-09 and 2026-09-10).
    P3  fair value unchanged to the cent between the two surfaces.
    P4  the price actually moved (EV ≡ fv/price − 1, so EV movement on a frozen price IS a
        fair-value move).
    P5  EV IDENTITY — the whole ΔEV must reproduce from the held fv against the anchor price,
        inside the propagated cent-rounding budget.
    P6  PRECISION FLOOR — refuse when that budget exceeds 0.5pp (a quarter of the 2pp gate).
        On a sub-$2 name cent rounding cannot tell a tape move from a curve move, so the
        machine must not claim it did (2343 round-tripped 0.38 -> 0.37 -> 0.38 across the
        2026-09-15 dry-FFA promote with a +0.66pp residual hidden inside the rounding).
    P7  a k_broker breach additionally needs the broker-NAV ratio to track the price ratio —
        broker_nav = price / consensus_pnav, so that identity proves consensus_pnav did not
        move, which is the only way a k breach is mechanical. (k itself is AFFINE in price,
        not proportional — never test k against the price ratio.)
    P8  no flip toward BUY, ever, relabel or not. That flip is the buyflip fork's business
        (promote.land (d)); annotating it into silence would walk a name into the actionable
        set without the objection window.
    P9  the name is not on a static / stale price fallback and is not void or SANITY=FAIL.

WHAT IT WRITES. One dated entry at the top of decisions/<ticker>_log.md, in the existing
convention, carrying a machine marker for idempotency. The FIRST SENTENCE of its `**Decision:**`
line is load-bearing beyond prose: `promote.compose_cause` builds the ratify cause from the
first sentence of every explained row, so it is short, self-describing and carries the numbers.

Touches nothing but decisions/*_log.md. Never ratifies, never runs the pipeline, never writes
inputs/ or outputs/.

Exit codes: 0 = wrote, or nothing to do (a refusal is a normal outcome) · 2 = missing data.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import yaml

from . import drift_gate, promote
from .delta import DECISION_LOG_HEADER_RE

ROOT = Path(__file__).resolve().parents[2]
DECISIONS_DIR = ROOT / "decisions"
SCORECARD_REL = "outputs/book_scorecard.json"
PRICES_REL = "inputs/market_data/prices_daily.yaml"

MARKER_VERSION = 1

# The ONLY determinant allowed to have moved. Everything else under src/ + inputs/ (archives
# and process files already excluded, promote.DETERMINANT_EXCLUDES) refuses the whole run.
PRICE_LEG_PATH = PRICES_REL


# Breaches a pure-price move can produce. band-mech is the D-M5 auto-classified price crossing;
# NAV / band / band-EXIT are re-reads and refuse.
ANNOTATABLE_BREACHES = {"EV%", "k_broker", "band-mech"}

# EV rounding budget, percentage points. The published fv is round(raw, 2), so each end of the
# comparison carries up to half a cent; the constant absorbs the baseline's own 0.01pp rounding
# at both ends with slack.
EV_TOL_CONST_PP = 0.02
PRECISION_FLOOR_PP = 0.5


# ---------------------------------------------------------------------------
# git / surface IO
# ---------------------------------------------------------------------------

def _git(root: Path, *args: str) -> "tuple[int, str]":
    p = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)
    return p.returncode, p.stdout


def current_surface(root: Path = ROOT) -> dict:
    return json.loads((root / SCORECARD_REL).read_text(encoding="utf-8"))


def surface_at(root: Path, commit: str) -> Optional[dict]:
    rc, out = _git(root, "show", f"{commit}:{SCORECARD_REL}")
    if rc != 0 or not out.strip():
        return None
    return json.loads(out)


def by_ticker(surface: dict) -> dict:
    return {str(n["ticker"]): n for n in (surface.get("names") or [])}


def determinant_changes(root: Path, frm: str, to: str) -> "list[str]":
    """Determinants that moved between two surface stamps. promote.determinant_paths is THE
    definition: this lane's price-leg proof must measure exactly the window (e) measures."""
    return promote.determinant_paths(root, frm, to)


# ---------------------------------------------------------------------------
# The predicate
# ---------------------------------------------------------------------------

@dataclass
class RunContext:
    baseline: dict
    state: dict
    current: dict
    anchor: dict
    prices: dict
    anchor_commit: str
    anchor_stamp: str
    current_stamp: str
    day: str
    moved: "list[str]" = field(default_factory=list)


@dataclass
class Outcome:
    ticker: str
    ok: bool
    reason: str = ""
    sentence: str = ""
    entry: str = ""
    path: Optional[Path] = None
    already: bool = False


class Refusal(Exception):
    """The whole run is refused — every row would be described over the wrong window."""


def build_context(root: Path = ROOT) -> RunContext:
    baseline = drift_gate.load_baseline(root / "baselines" / "reconcile_baseline.yaml")
    state = json.loads((root / "state" / "last_run.json").read_text(encoding="utf-8"))
    current = current_surface(root)
    meta = baseline.get("meta") or {}

    run_at = str(state.get("run_at") or "")
    generated_at = str(current.get("generated_at") or "")
    if run_at != generated_at:
        raise Refusal(f"state/last_run.json run_at {run_at!r} != surface generated_at "
                      f"{generated_at!r} — the state and the surface came from different runs")

    current_stamp = str(current.get("source_commit") or "")
    if not current_stamp or current_stamp.endswith("-dirty"):
        raise Refusal(f"surface stamp {current_stamp!r} is empty or dirty — the determinants "
                      f"the surface was built from are not a commit")

    anchor_commit = str(meta.get("ratified_commit") or "")
    anchor = surface_at(root, anchor_commit) if anchor_commit else None
    if anchor is None:
        raise Refusal(f"no committed surface at the baseline anchor {anchor_commit!r} — "
                      f"cannot measure the gate's own window")
    if str(anchor.get("generated_at") or "") != str(meta.get("ratified_at") or ""):
        raise Refusal(f"the surface at {anchor_commit} was generated "
                      f"{anchor.get('generated_at')!r}, but the baseline was ratified "
                      f"{meta.get('ratified_at')!r} — it is not the anchored surface")

    anchor_stamp = str(anchor.get("source_commit") or "")
    moved = determinant_changes(root, anchor_stamp, current_stamp)
    offenders = [p for p in moved if p != PRICE_LEG_PATH]
    if offenders:
        raise Refusal("a determinant other than the price vintage moved between the anchor "
                      f"surface {anchor_stamp} and this one {current_stamp}: "
                      + ", ".join(offenders[:6])
                      + (f" (+{len(offenders) - 6} more)" if len(offenders) > 6 else "")
                      + " — a sourcing event needs its own cause")

    prices = (yaml.safe_load((root / PRICES_REL).read_text(encoding="utf-8")) or {}).get("prices") or {}
    return RunContext(baseline=baseline, state=state, current=current, anchor=anchor,
                      prices=prices, anchor_commit=anchor_commit, anchor_stamp=anchor_stamp,
                      current_stamp=current_stamp, day=run_at[:10], moved=moved)


def ev_tolerance_pp(price_anchor: float, price_now: float) -> float:
    """Propagated half-cent fv rounding at both ends of the comparison, in percentage points."""
    return 0.5 / price_anchor + 0.5 / price_now + EV_TOL_CONST_PP


def pure_price(row, ctx: RunContext) -> "tuple[bool, str, dict]":
    """(ok, reason-if-not, facts). The whole predicate, one row."""
    t = row.ticker
    base = (ctx.baseline.get("names") or {}).get(t) or {}
    cur_state = (ctx.state.get("tickers") or {}).get(t) or {}
    a = by_ticker(ctx.anchor).get(t)
    c = by_ticker(ctx.current).get(t)

    if a is None or c is None:
        return False, "absent from the anchor or the current surface — nothing to compare", {}

    # P9 — a basis change is not a tape move, and a broken construction is not a move at all.
    pb = ctx.current.get("price_basis") or {}
    for key in ("static_fallback", "stale_fallback"):
        if t in (pb.get(key) or {}):
            return False, f"the price is a {key.replace('_', ' ')} — the BASIS changed, not the tape", {}
    if c.get("void") or str(c.get("sanity") or "") == "FAIL":
        return False, (f"void={bool(c.get('void'))} sanity={c.get('sanity')!r} — a construction "
                       f"problem, not a tape move"), {}

    # P1 — the breach shape.
    extra = sorted(set(row.breaches or []) - ANNOTATABLE_BREACHES)
    if extra:
        return False, f"breach {','.join(extra)} is a re-read, not a price move", {}

    # P8 — a flip toward BUY is the buyflip fork's, never a silent annotation.
    band_from, band_to = str(row.band_from or ""), str(row.band_to or "")
    flipped = bool(band_from and band_to and band_from != band_to)
    if flipped and band_to.upper().startswith("BUY"):
        return False, (f"band flip toward BUY ({band_from} -> {band_to}) — that is the buyflip "
                       f"fork's objection window, never a machine annotation"), {}

    # P2 — ΔNAV exactly 0.0.
    if row.d_nav_pct is None or abs(row.d_nav_pct) != 0.0:
        return False, f"ΔNAV {row.d_nav_pct}% is not exactly 0.0", {}

    fv_a, fv_c = float(a["fv"]), float(c["fv"])
    p_a, p_c = float(a["price"]), float(c["price"])

    # P3 — fair value held to the cent.
    if round(fv_a, 2) != round(fv_c, 2):
        return False, (f"fair value moved {fv_a:.2f} -> {fv_c:.2f} — a cause is needed and a "
                       f"machine must not invent one"), {}

    # P4 — the tape actually moved.
    if p_a == p_c:
        return False, f"the price is unchanged at {p_c:.2f} — an EV move here is a fair-value move", {}

    # P6 — precision floor before P5, so the reason names the real problem on a penny name.
    tol = ev_tolerance_pp(p_a, p_c)
    if tol > PRECISION_FLOOR_PP:
        return False, (f"cent rounding on a {p_c:.2f} share is worth ±{tol:.2f}pp of EV — too "
                       f"coarse to tell a tape move from a curve move"), {}

    # P5 — the EV identity, measured over the gate's own window.
    base_ev = float(base.get("ev_pct", cur_state.get("ev_pct", 0.0)))
    resid = (fv_c / p_a - 1.0) * 100.0 - base_ev
    if abs(resid) > tol:
        return False, (f"{abs(resid):.2f}pp of the ΔEV does not come from the price (budget "
                       f"±{tol:.2f}pp) — something other than the tape moved"), {}

    facts = {
        "ticker": t, "fv": fv_c, "price_anchor": p_a, "price_now": p_c,
        "ev_from": base_ev, "ev_to": float(cur_state.get("ev_pct", c.get("ev_pct", 0.0))),
        "d_nav_pct": float(row.d_nav_pct), "d_k": row.d_k,
        "position": str(c.get("position") or ""), "band_from": band_from, "band_to": band_to,
        "flipped": flipped, "resid_pp": resid, "tol_pp": tol,
    }

    # P7 — a k breach needs the broker-NAV ratio to track the tape.
    if "k_broker" in (row.breaches or []):
        bn_a, bn_c = a.get("broker_nav"), c.get("broker_nav")
        if not bn_a or not bn_c:
            return False, "a k_broker breach with no broker NAV on both surfaces to prove it mechanical", {}
        bn_a, bn_c = float(bn_a), float(bn_c)
        k_tol = 0.005 * (1 / bn_a + 1 / bn_c + 1 / p_a + 1 / p_c) * (bn_c / bn_a)
        k_resid = bn_c / bn_a - p_c / p_a
        if abs(k_resid) > k_tol:
            return False, (f"broker NAV moved {bn_c / bn_a:.4f}x against a {p_c / p_a:.4f}x tape "
                           f"(budget ±{k_tol:.4f}) — consensus_pnav moved, so the tool↔broker "
                           f"relationship changed"), {}
        facts["broker_nav_anchor"], facts["broker_nav_now"] = bn_a, bn_c

    asof = str((ctx.prices.get(t) or {}).get("asof") or "")
    if not asof:
        return False, f"no dated quote for {t} in {PRICES_REL} — cannot say when the tape moved", {}
    facts["asof"] = asof[:10]
    return True, "", facts


# ---------------------------------------------------------------------------
# The entry
# ---------------------------------------------------------------------------

def marker(ctx: RunContext, f: dict) -> str:
    return (f"<!-- annotate.py/{MARKER_VERSION} ticker={f['ticker']} run={ctx.state['run_at']} "
            f"anchor={ctx.anchor_commit} ev={f['ev_to']:.2f} px={f['price_now']:.2f} -->")


def first_sentence(f: dict) -> str:
    """Load-bearing: promote.compose_cause builds the ratify cause from this, cut at the first
    ". ", capped at 200 chars and joined with every other explained row's. Short, ASCII, no
    abbreviation-period, and it carries the numbers.

    A FLIPPED row names the band move (2026-09-18): the cause is the only place a reader sees
    what the anchor absorbed, and a band change absorbed silently is the one thing the owner
    said they must not lose when the executor started landing the tape itself. The parenthetical
    ("(undervalued)") is dropped — the cause is capped and the band word carries the meaning."""
    band = ""
    if f.get("flipped"):
        band = (f" band {str(f['band_from']).split(' (')[0]} -> "
                f"{str(f['band_to']).split(' (')[0]},")
    return (f"{f['ticker']} tape-only:{band} EV {f['ev_from']:+.1f}->{f['ev_to']:+.1f}pp, "
            f"fv held {f['fv']:.2f}.")


def render_entry(ctx: RunContext, f: dict) -> str:
    pct = (f["price_now"] / f["price_anchor"] - 1.0) * 100.0
    body = [first_sentence(f)]
    body.append(f"The quote stamped {f['asof']} took the share {f['price_anchor']:.2f} -> "
                f"{f['price_now']:.2f} ({pct:+.2f}%) while fair value held at {f['fv']:.2f} to "
                f"the cent, so the whole EV move is the denominator.")
    body.append(f"Determinant proof: {PRICE_LEG_PATH} is the only valuation determinant that "
                f"moved between the anchor surface {ctx.anchor_stamp} and this one "
                f"{ctx.current_stamp}; the unexplained residual is {abs(f['resid_pp']):.2f}pp "
                f"against a ±{f['tol_pp']:.2f}pp cent-rounding budget.")
    if "broker_nav_now" in f:
        body.append(f"Δk {f['d_k']:+.3f} rides the same tape: broker NAV "
                    f"{f['broker_nav_anchor']:.2f} -> {f['broker_nav_now']:.2f} tracks the price "
                    f"one-for-one, so consensus_pnav is a fixed ratio and the tool↔broker "
                    f"relationship did not move.")
    if f["flipped"]:
        body.append(f"The band reads {f['band_from']} -> {f['band_to']} — a price crossing with "
                    f"the share still inside the scenario FV interval (band-mech, D-M5), not a re-read.")
    body.append(f"The read stays '{f['position']}'.")
    body.append(f"Baseline anchor: the {str((ctx.baseline.get('meta') or {}).get('ratified_at'))[:10]} "
                f"ratify ({ctx.anchor_commit}). Gate row ΔNAV {f['d_nav_pct']:+.1f}%.")
    body.append("Written by crude_tanker_fv.annotate — deterministic price attribution only; a "
                "fair-value move is refused, never described.")

    title = (f"{f['ticker']} TAPE ONLY: EV {f['ev_from']:+.1f}pp -> {f['ev_to']:+.1f}pp, "
             f"fair value unchanged to the cent")
    return (f"## {ctx.day} — {title}\n\n"
            f"{marker(ctx, f)}\n\n"
            f"**Decision:** {' '.join(body)}\n\n"
            f"---\n")


def prepend_entry(path: Path, entry: str) -> None:
    """Insert above the first dated header, preserving any preamble — delta.py's own rule, so
    newest-first holds and drift_gate reads THIS entry."""
    if not path.exists():
        path.write_text(f"# {path.stem.split('_')[0].upper()} — Decision Log\n\n{entry}",
                        encoding="utf-8")
        return
    existing = path.read_text(encoding="utf-8")
    lines = existing.splitlines(keepends=True)
    idx = next((i for i, ln in enumerate(lines) if DECISION_LOG_HEADER_RE.match(ln)), None)
    if idx is None:
        path.write_text(f"{existing.rstrip()}\n\n{entry}", encoding="utf-8")
        return
    preamble = "".join(lines[:idx])
    if preamble:
        preamble = preamble.rstrip("\n") + "\n\n"
    path.write_text(f"{preamble}{entry}\n{''.join(lines[idx:])}", encoding="utf-8")


# ---------------------------------------------------------------------------
# Plan / apply
# ---------------------------------------------------------------------------

def plan(root: Path = ROOT, decisions_dir: Optional[Path] = None) -> "tuple[list[Outcome], str]":
    """(outcomes, run-level note). Raises Refusal when the whole run is off-window."""
    decisions_dir = decisions_dir or (root / "decisions")
    baseline = drift_gate.load_baseline(root / "baselines" / "reconcile_baseline.yaml")
    state = json.loads((root / "state" / "last_run.json").read_text(encoding="utf-8"))
    rows = drift_gate.evaluate(baseline, state, decisions_dir)
    todo = [r for r in rows if r.status == "UNEXPLAINED"]
    if not todo:
        return [], "0 UNEXPLAINED gate row(s) — nothing to do."

    ctx = build_context(root)
    out: list[Outcome] = []
    for row in todo:
        ok, reason, f = pure_price(row, ctx)
        if not ok:
            out.append(Outcome(row.ticker, False, reason))
            continue
        path = decisions_dir / f"{row.ticker.lower()}_log.md"
        entry = render_entry(ctx, f)
        already = path.exists() and marker(ctx, f) in path.read_text(encoding="utf-8")
        out.append(Outcome(row.ticker, True, sentence=first_sentence(f), entry=entry,
                           path=path, already=already))
    return out, f"{len(todo)} UNEXPLAINED gate row(s) considered."


def main(argv: "list[str] | None" = None) -> int:
    ap = argparse.ArgumentParser(
        prog="crude_tanker_fv.annotate",
        description="write the price-attribution annotation for PURE-PRICE gate rows; refuse the rest")
    ap.add_argument("--apply", action="store_true", help="write the entries (default: report only)")
    args = ap.parse_args(argv)

    for p in ("baselines/reconcile_baseline.yaml", "state/last_run.json", SCORECARD_REL):
        if not (ROOT / p).exists():
            sys.stderr.write(f"{p} not found — run the pipeline first.\n")
            return 2

    baseline_meta = (drift_gate.load_baseline().get("meta") or {})
    try:
        outcomes, note = plan(ROOT)
    except Refusal as exc:
        print(f"ANNOTATE — baseline anchor {str(baseline_meta.get('ratified_at'))[:10]} "
              f"({baseline_meta.get('ratified_commit')})")
        print(f"  RUN REFUSED: {exc}")
        return 0

    print(f"ANNOTATE — baseline anchor {str(baseline_meta.get('ratified_at'))[:10]} "
          f"({baseline_meta.get('ratified_commit')})")
    print(f"  {note}")
    wrote = refused = already = 0
    for o in outcomes:
        if not o.ok:
            refused += 1
            print(f"  REFUSED {o.ticker}: {o.reason}")
        elif o.already:
            already += 1
            print(f"  ALREADY ANNOTATED {o.ticker} — this run's entry is in {o.path.name}")
        elif args.apply:
            prepend_entry(o.path, o.entry)
            wrote += 1
            print(f"  WROTE {o.path.relative_to(ROOT)} — {o.sentence}")
        else:
            wrote += 1
            print(f"  WOULD WRITE {o.path.relative_to(ROOT)} — {o.sentence}")
    if outcomes:
        verb = "written" if args.apply else "to write"
        print(f"  {wrote} {verb}, {refused} refused, {already} already annotated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
