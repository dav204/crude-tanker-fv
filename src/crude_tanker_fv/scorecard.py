"""Book-wide validation scorecard (Thread 4 — the durable deliverable).

A *reporting* pass over the hardened machinery: every watchlist name graded on ONE
consistent, validated machine. The product is not "name X is cheap" — it is "here are
the names that clear every gate, here are the ones that don't, and why," with **pending
≠ passed** enforced (a name with a registered-pending gate is shown pending, never
blessed). NO new inputs are sourced in this pass; if a name reveals a needed input it is
registered separately, not patched here.

Definition of done per name (the grading standard this scorecard reports against):
  1. **NAV-basis** — age-0 on the uniform xclusiv Resale basis (`resale-uniform`), or
     flagged (`pending-sourceable` / `structural-unavailable` / `unverified-...`).
     Composite over the name's fleet from `inputs/market_data/basis_status.yaml` (single
     source): `resale-uniform` ONLY if every class the name holds is resale-uniform.
  2. **Justified P/NAV on BOTH bases** (parity headline + historical cross-check) — §17.
  3. **Parity band** — each held class's parity clears its registered §A1.2 band, or
     `unvalidated` (no band registered for that class).
  4. **§18.5a mean-reversion gate** on the historical basis — or `pending` (Thread 3 data).
  5. **§18.5b orderbook cross-check** on the parity divergence — or `pending` (Thread 5 data).
  6. **Robust vs flips** — does the cheap/rich read survive the parity↔historical choice?
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .justified_pnav import JustifiedPnavRow, compute_justified_pnav_rows
from .loaders import ALLOWED_CLASSES, INPUTS_DIR, load_basis_status, load_company_inputs, load_watchlist
from .nav import compute_nav
from .normal_rates import (
    PARITY_BANDS,
    mean_reversion_gate_table,
    normal_rate_table,
    orderbook_crosscheck_table,
)
from .provenance import (
    NAV_DERIVED_VOID,
    OPERATING_SCRUBBER_QUEUE,
    POSITION_CYCLE_RELABEL,
    POSITION_UNRELIABLE,
    TIER_SUBREASON,
    confidence_tier,
    is_handoff_ready,
)
from .reconcile import APPROX_PNAV_TICKERS
from .report import OUTPUTS_DIR


def _op_scrubber_error_pct(ci) -> float:
    """Max possible FV error from a name's UNCITED operating-scrubber flags, as a fraction of NAV
    (premium × uncited hulls / NAV). Feeds the tier's materiality gate — only a LARGE uncited
    surface widens the tier; a handful of hulls is a tracked-but-immaterial paperwork item."""
    curves = ci.market_data.vessel_value_curves
    err = sum(
        curves[v.cls].scrubber_premium * v.count
        for v in ci.fleet.vessels
        if v.scrubber and not (v.years_to_delivery or 0)
    )
    nav = compute_nav(ci).nav_total
    return err / nav if nav > 0 else 0.0

# NAV-basis composite priority: the name's PRIMARY label is the most-salient non-uniform
# status present across its fleet. structural (no clean market) > pending-sourceable (market
# exists, dated mark unsourced — Thread 1A) > unverified (mark exists, no current xclusiv line
# — MR) > resale-uniform. The detail lists EVERY non-uniform class, so nothing is hidden.
_BASIS_PRIORITY = (
    "structural-unavailable",
    "pending-sourceable",
    "unverified-no-current-xclusiv-line",
    "resale-uniform",
)


@dataclass
class ScorecardRow:
    ticker: str
    sector: str
    classes_held: list[str]
    nav_basis: str                 # composite (resale-uniform or the worst flag present)
    nav_basis_detail: str          # the flagged classes, when not resale-uniform
    pnav_mkt: Optional[float]
    read_par: str
    read_hist: str
    robust: str
    justified_flag: Optional[str]
    parity_band: str               # clears / OUT:<cls> / unvalidated / mixed
    gate_5a: str                   # pending / pass / reject / n-a
    gate_5b: str                   # pending / coincide / contradict / n-a
    verdict: str
    governance_discount_pct: float = 0.0   # §15 haircut (>0 only TEN/CMDB); read is clean-NAV
    confidence_tier: str = "PROVISIONAL"   # VALIDATED-TIGHT / GOVERNED-WIDE / PROVISIONAL (handoff)


def _nav_basis_composite(classes: list[str], status: dict[str, str]) -> tuple[str, str]:
    """Primary (most-salient) basis status across the fleet + a FULL breakdown of every
    non-uniform class grouped by status (so a name with both pending and unverified tonnage
    shows both)."""
    present = {c: status.get(c, "unverified-no-current-xclusiv-line") for c in classes}
    worst = min(present.values(), key=lambda s: _BASIS_PRIORITY.index(s)
                if s in _BASIS_PRIORITY else 0)
    if worst == "resale-uniform":
        return "resale-uniform", ""
    parts = []
    for st in _BASIS_PRIORITY[:-1]:                       # every non-uniform status, in order
        cls_in = sorted(c for c, s in present.items() if s == st)
        if cls_in:
            parts.append(f"{st}: {', '.join(cls_in)}")
    return worst, " | ".join(parts)


def _parity_band_status(classes: list[str], parity: dict[str, Optional[float]]) -> str:
    """Do the name's banded classes clear their registered §A1.2 parity bands?"""
    out_of_band = []
    banded = unvalidated = 0
    for c in classes:
        if c in PARITY_BANDS:
            p = parity.get(c)
            if p is None:
                unvalidated += 1
                continue
            lo, hi = PARITY_BANDS[c]
            banded += 1
            if not (lo <= p <= hi):
                out_of_band.append(c)
        else:
            unvalidated += 1
    if out_of_band:
        return "OUT:" + ",".join(sorted(out_of_band))
    if banded and unvalidated:
        return "clears (+unvalidated)"
    if banded:
        return "clears"
    return "unvalidated"


def _aggregate_gate(classes: list[str], table: dict, reject_tokens: tuple[str, ...],
                    pass_token: str) -> str:
    """Aggregate a per-class gate over a name's classes: any reject ⇒ reject; all pending
    ⇒ pending; any insufficient ⇒ pending; else pass."""
    statuses = [getattr(table[c], "status", "pending") for c in classes if c in table]
    if not statuses:
        return "n-a"
    if any(s in reject_tokens for s in statuses):
        return reject_tokens[0]
    if any(s in ("pending", "insufficient") for s in statuses):
        return "pending"
    return pass_token


def _verdict(nav_basis: str, justified_flag: Optional[str], robust: str,
             parity_band: str) -> str:
    if nav_basis != "resale-uniform":
        return f"NAV basis: {nav_basis}"
    if parity_band.startswith("OUT:"):
        return f"parity OUT-OF-BAND ({parity_band[4:]}) — investigate input"
    if justified_flag:
        return f"no justified multiple ({justified_flag})"
    if robust.startswith("flips"):
        return "read flips — normalization-dependent"
    if robust == "robust":
        return "comparable; §18.5 gates pending"
    return "comparable; §18.5 gates pending (read n/a)"


def compute_scorecard(quarter: str, inputs_dir: Path = INPUTS_DIR) -> list[ScorecardRow]:
    classes = sorted(ALLOWED_CLASSES)
    status = load_basis_status(inputs_dir)
    parity = {c: nr.parity for c, nr in normal_rate_table(quarter, classes, inputs_dir=inputs_dir).items()}
    mr = mean_reversion_gate_table(quarter, classes, inputs_dir=inputs_dir)
    ob = orderbook_crosscheck_table(quarter, classes, inputs_dir=inputs_dir)
    jrows: dict[str, JustifiedPnavRow] = {
        r.ticker: r for r in compute_justified_pnav_rows(quarter, inputs_dir)
    }
    rows: list[ScorecardRow] = []
    for ticker, entry in load_watchlist(inputs_dir).items():
        try:
            ci = load_company_inputs(ticker, quarter, inputs_dir)
        except FileNotFoundError:
            continue
        held = sorted({v.cls for v in ci.fleet.vessels})
        nav_basis, detail = _nav_basis_composite(held, status)
        jr = jrows.get(ticker)
        robust = jr.robust if jr else "n/a"
        # Operating-scrubber surface is only uncited (and so tier-relevant) for queued names.
        op_err = _op_scrubber_error_pct(ci) if ticker.upper() in OPERATING_SCRUBBER_QUEUE else 0.0
        tier = confidence_tier(ticker, nav_basis, robust, op_scrubber_error_pct=op_err, inputs_dir=inputs_dir)
        rows.append(ScorecardRow(
            ticker=ticker,
            sector=entry.get("sector", "crude"),
            classes_held=held,
            nav_basis=nav_basis,
            nav_basis_detail=detail,
            pnav_mkt=(jr.pnav_mkt if jr else None),
            read_par=(jr.read if jr else "n/a"),
            read_hist=(jr.read_hist if jr else "n/a"),
            robust=(jr.robust if jr else "n/a"),
            justified_flag=(jr.flag if jr else None),
            parity_band=_parity_band_status(held, parity),
            gate_5a=_aggregate_gate(held, mr, ("reject",), "pass"),
            gate_5b=_aggregate_gate(held, ob, ("contradict",), "coincide"),
            verdict=_verdict(nav_basis, (jr.flag if jr else None),
                             (jr.robust if jr else "n/a"),
                             _parity_band_status(held, parity)),
            governance_discount_pct=(jr.governance_discount_pct if jr else 0.0),
            confidence_tier=tier,
        ))
    return rows


@dataclass
class _Valuation:
    """The valuation half of one name's verdict — joined from the pipeline's in-scope objects
    (fv / scenario / broker sweep), so the scorecard carries FV-vs-price + position + broker NAV
    on the same row as tier + validation state. ONE consolidated output, not three to cross-join.

    BASIS (F-13, 2026-07-02): ``fv`` / ``upside_pct`` are the SCENARIO-WEIGHTED FV — the
    same basis as ``position``, the proposal tables, and the C-2 decomposition. The prior
    form took fv from the single-point blend while position came from the scenario EV; the
    two bases agreed incidentally under the Jun-9 war weights and the vintage separated
    them, printing "+28% upside · TRIM/SHORT" rows. The blend survives as the explicitly
    labeled secondary ``blend_fv`` (NAV+strip at CURRENT market forwards — for tankers the
    held Jun-7 curves, see the Rate-basis header)."""
    price: float
    fv: float                  # scenario probability-weighted FV (the headline basis)
    upside_pct: float          # (fv / price − 1) × 100 — same basis as position
    position: str
    nav_ps: float              # tool NAV/share
    broker_nav: Optional[float]
    gap_pct: Optional[float]   # (nav_ps − broker_nav) / broker_nav × 100
    sanity: str                # OK / FAIL / n-a (APPROX) — the reconcile ±50% bug-gate
    approx: bool
    blend_fv: Optional[float] = None   # single-point blend (secondary, labeled column)
    sleeve_fvs: Optional[dict] = None  # hybrid per-sleeve PW-FV contributions (WO1 V-1)


def valuation_index(fv_reports, scenario_reports, broker_rows) -> dict[str, "_Valuation"]:
    """Join the pipeline's per-name objects into the verdict's valuation half, keyed by ticker.

    The **scenario report is the whole-company spine** for price / NAV / FV / position —
    same as delta.snapshot_current_run. This matters for hybrid carve-outs (INSW, CMBT):
    the CompanyReport in fv_reports is a single SLEEVE (INSW = crude sleeve, price/NAV
    sleeve-allocated), so reading price off it understates the whole. The single-point
    blend is carried only as the labeled secondary ``blend_fv`` (F-13)."""
    fv_by = {r.ticker: r for r in fv_reports}
    bk = {r.ticker: r for r in broker_rows}
    out: dict[str, _Valuation] = {}
    for s in scenario_reports:
        t = s.ticker
        price = s.current_price
        nav_ps = s.base_nav_per_share
        fv = s.probability_weighted_fv
        f = fv_by.get(t)
        blend_fv = f.blended.fair_value_per_share if f else None
        b = bk.get(t)
        broker_nav = (price / b.consensus_pnav) if (b and b.consensus_pnav) else None
        gap = ((nav_ps - broker_nav) / broker_nav * 100.0) if broker_nav else None
        approx = t in APPROX_PNAV_TICKERS
        sanity = ("n-a" if approx else
                  ("OK" if (gap is not None and abs(gap) <= 50.0) else
                   ("FAIL" if gap is not None else "—")))
        out[t] = _Valuation(
            price=price, fv=fv, upside_pct=(fv / price - 1.0) * 100.0 if price else 0.0,
            position=s.position_recommendation,
            nav_ps=nav_ps, broker_nav=broker_nav, gap_pct=gap, sanity=sanity, approx=approx,
            blend_fv=blend_fv,
            sleeve_fvs=(dict(getattr(s, "sleeve_fvs", {}) or {}) or None),
        )
    return out


def price_basis_summary(inputs_dir: Path = INPUTS_DIR) -> dict:
    """Which names' prices are live vs static-fallback, for the scorecard header
    and the JSON handoff. A stale-price scorecard must ANNOUNCE itself: on
    2026-06-30 five names silently fell back to June-4 statics on the one day
    fresh prices mattered most, and nothing in the output said so (audit F-1)."""
    wl = load_watchlist(inputs_dir, live_prices=True)
    static = {t: e for t, e in sorted(wl.items()) if "price_as_of" not in e}
    return {
        "total": len(wl),
        "static_fallback": {
            t: {"as_of": str(e.get("as_of")),
                "reason": e.get("price_fallback", "no fresh daily quote")}
            for t, e in static.items()
        },
        "oldest_static_as_of": min(
            (str(e.get("as_of")) for e in static.values() if e.get("as_of")), default=None
        ),
        "market_event_review": {
            t: e["price_review"] for t, e in sorted(wl.items()) if e.get("price_review")
        },
    }


def update_weight_fragility_sidecar(
    family: str, weight_sets: dict, names: dict, outputs_dir: Path = OUTPUTS_DIR,
) -> Path:
    """Merge one sector family's EV-sign-stability entries into the shared
    sidecar (outputs/weight_robustness.yaml). MERGE, not overwrite — the crude
    script used to rewrite the whole file, which is why product/LNG names could
    never carry the flag (S-2, 2026-07-02): the seam exported null for names
    whose diagnostics had run. weight_sets are namespaced per family."""
    import yaml

    path = outputs_dir / "weight_robustness.yaml"
    doc = (yaml.safe_load(path.read_text()) or {}) if path.exists() else {}
    ws = doc.get("weight_sets") or {}
    if not (set(ws) <= {"crude", "product", "lng"}):
        ws = {}   # pre-namespacing shape (crude-only): drop; each family rewrites its block
    ws[family] = weight_sets
    merged = doc.get("names") or {}
    merged.update(names)
    out = {"weight_sets": ws, "names": dict(sorted(merged.items()))}
    outputs_dir.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(out, sort_keys=False))
    return path


def load_weight_fragility(outputs_dir: Path = OUTPUTS_DIR) -> dict[str, dict]:
    """{ticker: ev_sign_stable} from the §9.10 diagnostic's sidecar
    (outputs/weight_robustness.yaml, written by scripts/crude_weight_robustness.py).

    Review 2026-07-02 W-1: whether a name's EV SIGN survives the defensible
    weight family belongs on the verdict row — BRUT read BUY +98% under the
    locked set and HOLD −5% under the post-stand-down set; that sensitivity is
    the durable, mechanical form of the BRUT lesson and must be visible at the
    handoff, not buried in a diagnostic file. Names absent from the sidecar
    (non-crude, or the diagnostic hasn't run) render as un-flagged."""
    import yaml

    path = outputs_dir / "weight_robustness.yaml"
    if not path.exists():
        return {}
    doc = yaml.safe_load(path.read_text()) or {}
    # Full entries (2026-07-03 seam decision): the RANGE is the datum — the
    # boolean is derived from it, and the consumer derives its own
    # magnitude-sensitivity judgment from the same range (a producer choosing
    # the consumer's threshold is the S-1-class footgun). Sign-unstable →
    # consumer conviction zero; sign-stable → consumer sizes against
    # ev_pct_family_min, not the point estimate.
    return {t: {"ev_sign_stable": bool(e.get("ev_sign_stable")),
                "ev_min_pct": e.get("ev_min_pct"),
                "ev_max_pct": e.get("ev_max_pct")}
            for t, e in (doc.get("names") or {}).items()}


def _fragility_cell(ticker: str, fragility: dict[str, dict]) -> str:
    if ticker not in fragility:
        return "—"
    return "stable" if fragility[ticker]["ev_sign_stable"] else "**⚠ sign flips**"


def handoff_coherence_flags(doc: dict) -> list[str]:
    """Sign/label contradictions in a handoff document — the F-13 semantic
    check, shared by the committed-surface test AND the sentinel (one
    implementation; two callers asserting the same thing is how F-13 happened).
    ±0.15pp edge tolerance absorbs the JSON's 1-dp rounding."""
    flags = []
    for n in doc.get("names", []):
        ev, pos = n.get("ev_pct"), n.get("position") or ""
        if n.get("void") or ev is None:
            continue
        if pos.startswith("BUY") and not ev > 5 - 0.15:
            flags.append(f"{n['ticker']}: BUY at {ev:+.1f}%")
        elif pos.startswith("TRIM/SHORT") and not ev < -5 + 0.15:
            flags.append(f"{n['ticker']}: TRIM/SHORT at {ev:+.1f}%")
        elif pos.startswith("HOLD") and not (-5 - 0.15 < ev < 5 + 0.15):
            flags.append(f"{n['ticker']}: HOLD at {ev:+.1f}%")
    return flags


def rate_basis_notes(inputs_dir: Path = INPUTS_DIR) -> list[str]:
    """`vintage_notes` from ffa_forward_curve.yaml — rate-anchor staleness the
    mtime-based preflight check cannot see (a held VALUE keeps a fresh mtime).
    Reviewer condition 2026-07-02: a held anchor must announce itself in the
    OUTPUTS, not only in a YAML comment."""
    import yaml

    path = inputs_dir / "market_data" / "ffa_forward_curve.yaml"
    if not path.exists():
        return []
    doc = yaml.safe_load(path.read_text()) or {}
    return [" ".join(str(n).split()) for n in (doc.get("vintage_notes") or [])]


def _verdict_position(ticker: str, raw: str) -> str:
    """Displayed position — a cycle-rich or unreliable read is relabeled away from TRIM/SHORT so a
    skim can't read a NAV-relative cycle signal as a directional short (owner 2026-06-30, §12)."""
    if ticker in POSITION_CYCLE_RELABEL:
        return "rich · cycle position (not a short)"
    if ticker in POSITION_UNRELIABLE:
        return "unreliable read (not actionable)"
    return raw


def _verdict_tier(ticker: str, tier: str) -> str:
    """Tier cell + its sub-reason (the resolution path) + the PROVISIONAL gate mark."""
    sub = TIER_SUBREASON.get(ticker)
    return tier + (f" · {sub}" if sub else "") + (" ⛔" if tier == "PROVISIONAL" else "")


def _write_verdict(w, rows: list[ScorecardRow], valuation: dict[str, "_Valuation"], order: dict,
                   fragility: Optional[dict[str, bool]] = None) -> None:
    """The consolidated Verdict table — one row per name, the single handoff surface. Carries the
    owner's three corrections: cycle-position relabel, tier sub-reasons, and voided derived numbers."""
    by = {r.ticker: r for r in rows}
    longs = sorted(
        r.ticker for r in rows
        if r.confidence_tier == "VALIDATED-TIGHT" and r.read_hist == "cheap"
        and valuation.get(r.ticker) and valuation[r.ticker].position.startswith("BUY")
    )
    n_wide = sum(1 for r in rows if r.confidence_tier == "GOVERNED-WIDE")
    n_prov = sum(1 for r in rows if r.confidence_tier == "PROVISIONAL")
    # Every name-specific sentence below is DERIVED from the rows, never hand-written:
    # a literal claim ("TNK ... reads rich") goes stale silently the day the state
    # changes, and this file is the decision surface (audit 2026-07-02, F-8).
    long_color = ""
    if longs:
        sectors = ", ".join(sorted({by[t].sector.replace("_", " ") for t in longs}))
        both = all(by[t].read_par == "cheap" for t in longs)
        long_color = f" — {sectors}" + (", cheap on both NAV bases" if both else "")
    rich_longs = sorted(
        r.ticker for r in rows
        if r.confidence_tier == "VALIDATED-TIGHT" and r.read_hist == "rich"
        and valuation.get(r.ticker) and valuation[r.ticker].position.startswith("BUY")
    )
    if len(rich_longs) == 1:
        rich_sentence = (f"{rich_longs[0]} is VALIDATED-TIGHT and BUY but reads *rich* — a "
                         f"near-peak-earnings long, cycle-dependent, not a clean value long. ")
    elif rich_longs:
        rich_sentence = (f"{', '.join(rich_longs)} are VALIDATED-TIGHT and BUY but read *rich* — "
                         f"near-peak-earnings longs, cycle-dependent, not clean value longs. ")
    else:
        rich_sentence = ""
    raw_shorts = sorted(
        r.ticker for r in rows
        if valuation.get(r.ticker) and valuation[r.ticker].position.startswith("TRIM/SHORT")
    )
    named_shorts = [t for t in raw_shorts
                    if t not in POSITION_CYCLE_RELABEL and t not in POSITION_UNRELIABLE
                    and t not in NAV_DERIVED_VOID]
    if raw_shorts and not named_shorts:
        shorts_sentence = ("And **every one of the book's TRIM/SHORT positions is cycle-position, "
                           "unreliable-read, or void — not one is a name-specific short.** ")
    elif named_shorts:
        shorts_sentence = (f"**Name-specific shorts: {', '.join(named_shorts)}** — every other "
                           f"TRIM/SHORT row is cycle-position, unreliable-read, or void. ")
    else:
        shorts_sentence = ""
    w("## Verdict — the consolidated read (the decision surface)\n")
    w("FV vs current price, position, and the broker-NAV bug-gate on the **same row** as the confidence "
      "tier — **the single handoff surface** for a sizing decision. The per-gate evidence behind each "
      "tier is the Validation matrix below (same names, same file).\n")
    w(f"**What this says about the opportunity set:** of {len(rows)} names, the validated-and-actionable-"
      f"long surface is **{len(longs)} ({', '.join(longs)}{long_color})**. "
      f"{n_wide} are directional-only (GOVERNED-WIDE); {n_prov} are not yet trustworthy enough to act on "
      f"(PROVISIONAL ⛔). {rich_sentence}{shorts_sentence}The thin actionable "
      f"list is the tool refusing to manufacture conviction the validation doesn't support, not a gap.\n")
    w("**Reading the labels:** the tier cell carries a **sub-reason = resolution path** "
      "(`structural-class` needs a new data regime; `pending-anchor` is sourceable now; `newbuild-heavy` "
      "resolves as hulls deliver; `newbuild-indeterminate` = a newbuild parked at $0 pending a filed "
      "price; `read-flips` needs the §18.5 gate data; `void` = a derived number rests "
      "on a contradicted figure). A **`cycle position`** in Position is a NAV-relative read (§12), NOT a "
      "directional short. A **void** row prints no derived numbers — they are known-suspect, not data.\n")
    fragility = fragility or {}
    w("| Ticker | Sector | **Tier · why** | Price | Model FV | Upside | Position | Blend FV† | "
      "NAV/sh | Broker NAV | Gap | SANITY | Handoff | W-frag |")
    w("|---|---|---|--:|--:|--:|:--|--:|--:|--:|--:|:--|:--|:--|")
    torder = {"VALIDATED-TIGHT": 0, "GOVERNED-WIDE": 1, "PROVISIONAL": 2}
    for r in sorted(rows, key=lambda r: (torder.get(r.confidence_tier, 9), order.get(r.sector, 9), r.ticker)):
        tier = _verdict_tier(r.ticker, r.confidence_tier)
        ready = "ready" if is_handoff_ready(r.confidence_tier) else "**NO**"
        frag = _fragility_cell(r.ticker, fragility)
        v = valuation.get(r.ticker)
        if v is None:
            w(f"| {r.ticker} | {r.sector} | {tier} | — | — | — | — | — | — | — | — | — | {ready} | {frag} |")
            continue
        if r.ticker in NAV_DERIVED_VOID:
            w(f"| {r.ticker} | {r.sector} | {tier} | ${v.price:.2f} | _void_ | _void_ "
              f"| _void — pending reconciliation_ | _void_ | _void_ | _void_ | _void_ | _void_ | **NO** | {frag} |")
            continue
        bn = (f"${v.broker_nav:.2f}" + (" (apx)" if v.approx else "")) if v.broker_nav else ("apx" if v.approx else "—")
        gp = f"{v.gap_pct:+.0f}%" if v.gap_pct is not None else "—"
        bl = f"${v.blend_fv:.2f}" if (v.blend_fv is not None and v.blend_fv == v.blend_fv) else "—"
        w(f"| {r.ticker} | {r.sector} | {tier} | ${v.price:.2f} | ${v.fv:.2f} | {v.upside_pct:+.0f}% "
          f"| {_verdict_position(r.ticker, v.position)} | {bl} | ${v.nav_ps:.2f} | {bn} | {gp} | {v.sanity} | {ready} | {frag} |")
    w("")
    w("_Model FV / Upside = the SCENARIO-probability-weighted FV — the same basis as Position "
      "and every proposal/decomposition table (F-13, 2026-07-02: the two columns previously mixed "
      "bases and printed '+28% upside · TRIM/SHORT' rows the day the bases diverged). "
      "Blend FV† = the single-point NAV+strip blend at CURRENT market forwards — for tanker "
      "classes the HELD Jun-7 curves (see Rate basis above); a large Blend-vs-Model gap IS the "
      "scenario-dependence signal, not a discrepancy._\n")
    if fragility:
        w("_W-frag = does the EV **sign** survive the §9.10 weight family "
          "(`outputs/weight_robustness.yaml`)? **⚠ sign flips** = the direction of the call is a "
          "weight-prior artifact, not a property of the name (the BRUT lesson, 2026-07-02) — a "
          "trust qualifier on the FV, consumed downstream like the tier. '—' = not in "
          "the diagnostic (non-crude family or not yet run)._\n")


def write_scorecard(
    rows: list[ScorecardRow],
    outputs_dir: Path = OUTPUTS_DIR,
    valuation: Optional[dict[str, "_Valuation"]] = None,
    price_basis: Optional[dict] = None,
    quarter: Optional[str] = None,
    fragility: Optional[dict[str, bool]] = None,
    rate_basis: Optional[list[str]] = None,
) -> Path:
    outputs_dir.mkdir(parents=True, exist_ok=True)
    out: list[str] = []
    w = out.append
    order = {"crude": 0, "product": 1, "dry_bulk": 2, "lng": 3, "containerships": 4}
    w("# Book-wide scorecard (Thread 4)\n")

    if price_basis:
        n_static = len(price_basis["static_fallback"])
        if n_static:
            names = ", ".join(price_basis["static_fallback"])
            w(f"> **Price basis: {n_static} of {price_basis['total']} prices are STATIC-FALLBACK** "
              f"(oldest as-of {price_basis['oldest_static_as_of']}): {names}. Those rows value the "
              f"book at watchlist statics, not the tape — treat their Price/Upside as stale.\n")
        else:
            w(f"> **Price basis:** all {price_basis['total']} prices live.\n")
        if price_basis.get("market_event_review"):
            names = ", ".join(price_basis["market_event_review"])
            w(f"> **Market-event review:** {names} — the day-band circuit breaker applied fresh "
              f"prices on a multi-name repricing; eyeball these moves before acting.\n")

    for note in (rate_basis or []):
        w(f"> **Rate basis:** {note}\n")

    if valuation:
        w("This file lists each name **twice, by design** — once in the **Verdict** (the decision "
          "surface: FV vs price, position, tier) and once in the **Validation matrix** below (the "
          "per-gate evidence behind that tier). The Verdict is what you act on; the matrix is why. "
          "One row per name *within* each table.\n")
        _write_verdict(w, rows, valuation, order, fragility)
        w("## Validation matrix — per-gate detail\n")

    w("Every covered name on ONE consistent, validated machine. **The product is the "
      "*boundary of what's comparable*, not a buy list.** `pending` ≠ `passed`: a name with a "
      "registered-pending gate is shown pending, never blessed. NAV age-0 basis is the uniform "
      "**xclusiv Resale** line (2026-06-22); mid-age is transaction-anchored (§9.9).\n")
    w("**Gates per name:** (1) NAV-basis (resale-uniform ⇒ comparable; else flagged); "
      "(2) Justified P/NAV both bases (§17); (3) parity band (§A1.2); (4) §18.5a mean-reversion "
      "(Thread 3, data-pending); (5) §18.5b orderbook cross-check (Thread 5, data-pending); "
      "(6) robust vs flips (does the read survive the parity↔historical choice).\n")

    w("**Confidence tier (governance handoff):** the FV's reliability for a sizing decision, read "
      "from the validation state above — **VALIDATED-TIGHT** (traced basis + robust across both §17 "
      "bases — broker OR internal two-basis corroboration; SB-class), **GOVERNED-WIDE** (NAV traces "
      "but rests on a structural-unavailable input or a read that flips — usable directional anchor, "
      "wide band; CMBT-class), **PROVISIONAL** (a NAV-driving figure is uncited / off-basis — "
      "**NOT handoff-ready, flag don't pass**; NAT-class). APPROX-pnav does not demote a robust name; "
      "an immaterial uncited operating-scrubber surface does not either (see provenance.py).\n")
    w("| Ticker | Sector | **Tier** | NAV-basis | P/NAV(mkt) | Read par→hist | Robust? | Parity band | "
      "§18.5a | §18.5b | Verdict |")
    w("|---|---|---|---|--:|---|---|---|---|---|---|")
    for r in sorted(rows, key=lambda r: (order.get(r.sector, 9), r.ticker)):
        pm = f"{r.pnav_mkt:.2f}×" if r.pnav_mkt is not None else "n/a"
        tier = r.confidence_tier + (" ⛔" if r.confidence_tier == "PROVISIONAL" else "")
        w(f"| {r.ticker} | {r.sector} | {tier} | {r.nav_basis} | {pm} | {r.read_par}→{r.read_hist} | "
          f"{r.robust} | {r.parity_band} | {r.gate_5a} | {r.gate_5b} | {r.verdict} |")

    # Summary
    def _count(key) -> dict[str, int]:
        c: dict[str, int] = {}
        for r in rows:
            c[key(r)] = c.get(key(r), 0) + 1
        return c

    w("\n## Summary\n")
    nb = _count(lambda r: r.nav_basis)
    w("**NAV-basis (comparability boundary):** " +
      ", ".join(f"{k} {v}" for k, v in sorted(nb.items())) + ".")
    rob = _count(lambda r: "flips" if r.robust.startswith("flips") else r.robust)
    w("\n**Read robustness (parity↔historical):** " +
      ", ".join(f"{k} {v}" for k, v in sorted(rob.items())) + ".")
    tiers = _count(lambda r: r.confidence_tier)
    provisional = sorted(r.ticker for r in rows if r.confidence_tier == "PROVISIONAL")
    w("\n**Confidence tier (handoff):** " +
      ", ".join(f"{k} {v}" for k, v in sorted(tiers.items())) + ".")
    w(f"\n**⛔ NOT handoff-ready (PROVISIONAL — do NOT pass a governed FV):** {', '.join(provisional)}. "
      "Each carries a NAV-driving figure that is uncited or off-basis (figure-provenance / off-convention "
      "queue); flag, don't pass, until it traces.")
    w("\n**Both §18.5 gates are registered-PENDING book-wide** — no Baltic $/day series (§18.5a) "
      "or orderbook ratios (§18.5b) in-repo; see `backtest/DATA_CONTRACT_NORMAL_RATES.md`. So no "
      "name is *fully* validated yet; the resale-uniform names are comparable and parity-banded, "
      "awaiting only the two data-gated gates.")
    w("\n**Caveat — crude `rich` is cycle position, not a short.** Crude pure-plays read rich because "
      "the §17 RONAV is through-cycle while price embeds the near-peak NTM rate (§12 NAT mechanism); "
      "read the crude reads with cycle position, not as TRIM/SHORT calls.")
    gov = [r for r in rows if r.governance_discount_pct > 0]
    if gov:
        names = ", ".join(f"{r.ticker} ({r.governance_discount_pct:.0%})" for r in sorted(gov, key=lambda r: r.ticker))
        w(f"\n**§15 governance dual-read:** {names} carry a realisation haircut applied downstream "
          "(blend + strip terminal), NOT in the clean-NAV reads above — their reads are clean-basis; "
          "the haircut basis scales NAV/FV by (1 − haircut).")
    flagged = [r for r in rows if r.nav_basis != "resale-uniform"]
    if flagged:
        w("\n**NAV-basis-flagged (not yet comparable to the resale-uniform set):**")
        for r in sorted(flagged, key=lambda r: r.ticker):
            w(f"- **{r.ticker}** — {r.nav_basis_detail}")
    md_path = outputs_dir / "book_scorecard.md"
    md_path.write_text("\n".join(out))
    if valuation is not None:
        _write_handoff_json(rows, valuation, outputs_dir, price_basis, quarter, fragility,
                            rate_basis)
    return md_path


def _num(x: Optional[float], nd: int = 2) -> Optional[float]:
    """Round for the JSON handoff; NaN (a name missing from fv_reports) -> null —
    json.dumps would otherwise emit bare NaN, which is not valid JSON."""
    return None if x is None or x != x else round(x, nd)


def _vintage_stamp() -> dict:
    """generated_at + source_commit for the handoff (WO1 V-1) — the vintage
    stamp the governance repo's G-1 captures next to every figure it copies.
    source_commit gets a '-dirty' suffix when the tree carries uncommitted
    tracked changes (a mid-surgery export must say so). Semantics: the stamp is
    the tree the run STARTED from — one behind the commit that ships this file
    (outputs are committed with their generation), so '-dirty' in a committed
    artifact is normal and means "generated together with the changes in this
    very commit". A consumer wanting the exact reproducible vintage uses the
    commit that CONTAINS the JSON; source_commit is for cross-repo drift
    detection, not checkout. This deliberately trades the JSON's byte-stable
    regeneration for consumer traceability; the markdown stays wall-clock-free."""
    import subprocess
    from datetime import datetime, timezone

    try:
        root = Path(__file__).resolve().parents[2]
        head = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, timeout=5,
                              cwd=root).stdout.strip()
        # 'dirty' means the run's DETERMINANTS (code + inputs) differ from
        # HEAD — the pipeline's own output/decision-log writes mid-run are its
        # products, not dirt (WO1-F1: an unscoped check stamped every normal
        # run -dirty because earlier pipeline stages had already written
        # outputs by the time the scorecard stamped).
        porcelain = subprocess.run(["git", "status", "--porcelain", "--", "src", "inputs"],
                                   capture_output=True, text=True, timeout=5,
                                   cwd=root).stdout.strip()
        commit = (head + "-dirty" if porcelain else head) if head else None
    except Exception:
        commit = None
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_commit": commit,
    }


def _write_handoff_json(
    rows: list[ScorecardRow],
    valuation: dict[str, "_Valuation"],
    outputs_dir: Path,
    price_basis: Optional[dict],
    quarter: Optional[str],
    fragility: Optional[dict[str, bool]] = None,
    rate_basis: Optional[list[str]] = None,
) -> Path:
    """The machine-readable half of the handoff surface (audit 2026-07-02, F-4).

    The Verdict table is rendered markdown — format-fragile for the governance
    repo's ingestion (a column reorder silently mis-maps a field). This JSON is
    the CONTRACT: schema-versioned, same underlying objects as the table (tiers,
    sub-reasons, positions, void striking), locked by test_scorecard. Bump
    schema_version on any breaking field change; the ingesting side must assert
    it. No wall-clock stamp — the temporal anchor is price_basis, so an
    unchanged book regenerates byte-identical (the audit's reproducibility
    property, F-10)."""
    names = []
    torder = {"VALIDATED-TIGHT": 0, "GOVERNED-WIDE": 1, "PROVISIONAL": 2}
    sorder = {"crude": 0, "product": 1, "dry_bulk": 2, "lng": 3, "containerships": 4}
    for r in sorted(rows, key=lambda r: (torder.get(r.confidence_tier, 9),
                                         sorder.get(r.sector, 9), r.ticker)):
        v = valuation.get(r.ticker)
        void = r.ticker in NAV_DERIVED_VOID
        frag = (fragility or {}).get(r.ticker) or {}
        names.append({
            "ticker": r.ticker,
            "sector": r.sector,
            "confidence_tier": r.confidence_tier,
            "tier_subreason": TIER_SUBREASON.get(r.ticker),
            "handoff_ready": is_handoff_ready(r.confidence_tier) and not void,
            "nav_basis": r.nav_basis,
            "void": void,
            "sanity": v.sanity if v else None,
            "price": _num(v.price) if v else None,
            # Void striking mirrors the md table: a number derived off a
            # contradicted figure is not data and must not reach the consumer.
            "position": (None if v is None else
                         ("void — pending reconciliation" if void
                          else _verdict_position(r.ticker, v.position))),
            # fv/ev_pct = SCENARIO-weighted basis, same as position (F-13 —
            # schema_version 2; v1 exported the single-point blend here, which
            # produced "+28% upside, SHORT" rows once the bases diverged).
            "fv": None if (v is None or void) else _num(v.fv),
            "ev_pct": None if (v is None or void) else _num(v.upside_pct, 1),
            "blend_fv": None if (v is None or void) else _num(v.blend_fv),
            "nav_per_share": None if (v is None or void) else _num(v.nav_ps),
            "broker_nav": None if (v is None or void) else _num(v.broker_nav),
            "gap_pct": None if (v is None or void) else _num(v.gap_pct, 1),
            # Percentage POINTS like every other _pct field (S-1, schema v3 —
            # v2 exported the engine-internal fraction: TEN's 30% haircut read
            # as 0.3% to a literal-minded consumer). Internal convention stays
            # fractional; the conversion lives at the seam.
            "governance_discount_pct": _num(r.governance_discount_pct * 100.0, 1),
            # WO1 V-1: hybrid per-sleeve PW-FV contributions (per-share; sum ==
            # fv by the C-3 identity) — lets the governance repo watch e.g.
            # CMBT's dry-bulk sleeve instead of the whole-co proxy. null for
            # pure-plays; suppressed for void rows like every derived number.
            "sleeves": (None if (v is None or void or not v.sleeve_fvs) else
                        [{"sleeve": sec, "sector": sec,
                          "fv_contribution_per_share": _num(fv_c)}
                         for sec, fv_c in v.sleeve_fvs.items()]),
            # null = not in a §9.10 family diagnostic. weight_sign_stable is
            # THE derived boolean ((min>0)==(max>0)); the family EV range is
            # the underlying datum, exported so the consumer computes its own
            # magnitude-sensitivity judgment (2026-07-03: sign-unstable →
            # conviction zero; sign-stable → size against family_min).
            "weight_sign_stable": frag.get("ev_sign_stable") if frag else None,
            "ev_pct_family_min": frag.get("ev_min_pct"),
            "ev_pct_family_max": frag.get("ev_max_pct"),
        })
    doc = {
        # "2.1" (2026-07-02, WO1 Task 1 — string; the consumer asserts
        # major == 2, so 2 -> 2.1 is non-breaking by design). Collapses the
        # same-day dev iterations: F-13 fv re-basing to the scenario-weighted
        # basis + blend_fv (was int 2); governance_discount_pct to percentage
        # POINTS + weight_sign_stable for product/LNG (was int 3);
        # generated_at/source_commit vintage stamp + hybrid sleeves (was int 4).
        # 2.2 (2026-07-03): + ev_pct_family_min/max — the family range as the
        # seam datum; weight_sign_stable stays the one derived boolean.
        "schema_version": "2.2",
        **_vintage_stamp(),
        "quarter": quarter,
        "price_basis": price_basis,
        "rate_basis": rate_basis or [],
        # Hybrid sleeves: contributions are per-share scenario PW FVs and SUM
        # TO fv EXACTLY (C-3 identity) — corporate-level items (debt, working
        # capital, preferred, shuttle book) are PRO-RATED INTO the sleeves by
        # carveout.py, not held outside them.
        "sleeves_note": (
            "sleeves[*].fv_contribution_per_share are per-share scenario-weighted FVs; "
            "sum(sleeves) == fv to the cent (C-3 per-sleeve identity). Corporate-level "
            "balance-sheet items (debt, working capital, preferred, shuttle contracted "
            "book) are pro-rated INTO the sleeve carve-outs (carveout.py), so nothing "
            "sits outside the per-sleeve lines."
        ),
        "names": names,
    }
    path = outputs_dir / "book_scorecard.json"
    path.write_text(json.dumps(doc, indent=2, allow_nan=False) + "\n")
    return path


def run_scorecard_xref(
    quarter: str, inputs_dir: Path = INPUTS_DIR, outputs_dir: Path = OUTPUTS_DIR,
    *, fv_reports=None, scenario_reports=None, broker_rows=None,
) -> list[ScorecardRow]:
    """Compute + write the book scorecard. When the pipeline passes its in-scope per-name objects
    (fv / scenario / broker sweep), the scorecard becomes the CONSOLIDATED handoff output — verdict
    (FV-vs-price + position + broker NAV) joined onto tier + validation state in one file. Called
    standalone (no reports) it emits the validation matrix only — backward compatible."""
    rows = compute_scorecard(quarter, inputs_dir)
    valuation = None
    price_basis = None
    fragility = None
    rate_basis = None
    if fv_reports is not None and scenario_reports is not None and broker_rows is not None:
        valuation = valuation_index(fv_reports, scenario_reports, broker_rows)
        price_basis = price_basis_summary(inputs_dir)
        fragility = load_weight_fragility(outputs_dir)
        rate_basis = rate_basis_notes(inputs_dir)
    if rows:
        path = write_scorecard(rows, outputs_dir, valuation, price_basis, quarter, fragility,
                               rate_basis)
        n_uniform = sum(1 for r in rows if r.nav_basis == "resale-uniform")
        n_ready = sum(1 for r in rows if is_handoff_ready(r.confidence_tier))
        tag = "CONSOLIDATED verdict+matrix" if valuation else "validation matrix"
        print(f"book scorecard [{tag}] ({n_uniform}/{len(rows)} resale-uniform; "
              f"{n_ready}/{len(rows)} handoff-ready) -> {path}")
    return rows
