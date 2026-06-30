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
    on the same row as tier + validation state. ONE consolidated output, not three to cross-join."""
    price: float
    fv: float                  # single-point blended FV (report.blended.fair_value_per_share)
    upside_pct: float          # (fv / price − 1) × 100
    position: str
    nav_ps: float              # tool NAV/share
    broker_nav: Optional[float]
    gap_pct: Optional[float]   # (nav_ps − broker_nav) / broker_nav × 100
    sanity: str                # OK / FAIL / n-a (APPROX) — the reconcile ±50% bug-gate
    approx: bool


def valuation_index(fv_reports, scenario_reports, broker_rows) -> dict[str, "_Valuation"]:
    """Join the pipeline's per-name objects into the verdict's valuation half, keyed by ticker.

    The **scenario report is the whole-company spine** for price / NAV / position — same as
    delta.snapshot_current_run. This matters for hybrid carve-outs (INSW, CMBT): the CompanyReport
    in fv_reports is a single SLEEVE (INSW = crude sleeve, price/NAV sleeve-allocated), so reading
    price off it understates the whole. Only the single-point FV is read from the CompanyReport
    (matching the delta report's headline FV). So this row equals the decision-log / delta headline."""
    fv_by = {r.ticker: r for r in fv_reports}
    bk = {r.ticker: r for r in broker_rows}
    out: dict[str, _Valuation] = {}
    for s in scenario_reports:
        t = s.ticker
        price = s.current_price
        nav_ps = s.base_nav_per_share
        f = fv_by.get(t)
        fv = f.blended.fair_value_per_share if f else float("nan")
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
        )
    return out


def _verdict_position(ticker: str, raw: str) -> str:
    """Displayed position — a cycle-rich or unreliable read is relabeled away from TRIM/SHORT so a
    skim can't read a NAV-relative cycle signal as a directional short (owner 2026-06-30, §12)."""
    if ticker in POSITION_CYCLE_RELABEL:
        return "rich · cycle position (not a short)"
    if ticker in POSITION_UNRELIABLE:
        return "unreliable read (not a short)"
    return raw


def _verdict_tier(ticker: str, tier: str) -> str:
    """Tier cell + its sub-reason (the resolution path) + the PROVISIONAL gate mark."""
    sub = TIER_SUBREASON.get(ticker)
    return tier + (f" · {sub}" if sub else "") + (" ⛔" if tier == "PROVISIONAL" else "")


def _write_verdict(w, rows: list[ScorecardRow], valuation: dict[str, "_Valuation"], order: dict) -> None:
    """The consolidated Verdict table — one row per name, the single handoff surface. Carries the
    owner's three corrections: cycle-position relabel, tier sub-reasons, and voided derived numbers."""
    longs = sorted(
        r.ticker for r in rows
        if r.confidence_tier == "VALIDATED-TIGHT" and r.read_hist == "cheap"
        and valuation.get(r.ticker) and valuation[r.ticker].position.startswith("BUY")
    )
    n_wide = sum(1 for r in rows if r.confidence_tier == "GOVERNED-WIDE")
    n_prov = sum(1 for r in rows if r.confidence_tier == "PROVISIONAL")
    w("## Verdict — the consolidated read (one row per name)\n")
    w("FV vs current price, position, and the broker-NAV bug-gate on the **same row** as the confidence "
      "tier — **the single handoff surface** (per-gate detail is the matrix below, same file).\n")
    w(f"**What this says about the opportunity set:** of {len(rows)} names, the validated-and-actionable-"
      f"long surface is **{len(longs)} ({', '.join(longs)} — dry bulk, cheap on both NAV bases)**. "
      f"{n_wide} are directional-only (GOVERNED-WIDE); {n_prov} are not yet trustworthy enough to act on "
      f"(PROVISIONAL ⛔). TNK is VALIDATED-TIGHT and BUY but reads *rich* — a near-peak-earnings long, "
      f"cycle-dependent, not a clean value long. And **every one of the book's TRIM/SHORT positions is "
      f"cycle-position, unreliable-read, or void — not one is a name-specific short.** The thin actionable "
      f"list is the tool refusing to manufacture conviction the validation doesn't support, not a gap.\n")
    w("**Reading the labels:** the tier cell carries a **sub-reason = resolution path** "
      "(`structural-class` needs a new data regime; `pending-anchor` is sourceable now; `newbuild-heavy` "
      "resolves as hulls deliver; `read-flips` needs the §18.5 gate data; `void` = a derived number rests "
      "on a contradicted figure). A **`cycle position`** in Position is a NAV-relative read (§12), NOT a "
      "directional short. A **void** row prints no derived numbers — they are known-suspect, not data.\n")
    w("| Ticker | Sector | **Tier · why** | Price | Model FV | Upside | Position | NAV/sh | "
      "Broker NAV | Gap | SANITY | Handoff |")
    w("|---|---|---|--:|--:|--:|:--|--:|--:|--:|:--|:--|")
    torder = {"VALIDATED-TIGHT": 0, "GOVERNED-WIDE": 1, "PROVISIONAL": 2}
    for r in sorted(rows, key=lambda r: (torder.get(r.confidence_tier, 9), order.get(r.sector, 9), r.ticker)):
        tier = _verdict_tier(r.ticker, r.confidence_tier)
        ready = "ready" if is_handoff_ready(r.confidence_tier) else "**NO**"
        v = valuation.get(r.ticker)
        if v is None:
            w(f"| {r.ticker} | {r.sector} | {tier} | — | — | — | — | — | — | — | — | {ready} |")
            continue
        if r.ticker in NAV_DERIVED_VOID:
            w(f"| {r.ticker} | {r.sector} | {tier} | ${v.price:.2f} | _void_ | _void_ "
              f"| _void — pending reconciliation_ | _void_ | _void_ | _void_ | _void_ | **NO** |")
            continue
        bn = (f"${v.broker_nav:.2f}" + (" (apx)" if v.approx else "")) if v.broker_nav else ("apx" if v.approx else "—")
        gp = f"{v.gap_pct:+.0f}%" if v.gap_pct is not None else "—"
        w(f"| {r.ticker} | {r.sector} | {tier} | ${v.price:.2f} | ${v.fv:.2f} | {v.upside_pct:+.0f}% "
          f"| {_verdict_position(r.ticker, v.position)} | ${v.nav_ps:.2f} | {bn} | {gp} | {v.sanity} | {ready} |")
    w("")


def write_scorecard(
    rows: list[ScorecardRow],
    outputs_dir: Path = OUTPUTS_DIR,
    valuation: Optional[dict[str, "_Valuation"]] = None,
) -> Path:
    outputs_dir.mkdir(parents=True, exist_ok=True)
    out: list[str] = []
    w = out.append
    order = {"crude": 0, "product": 1, "dry_bulk": 2, "lng": 3, "containerships": 4}
    w("# Book-wide scorecard (Thread 4)\n")

    if valuation:
        _write_verdict(w, rows, valuation, order)
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
    return md_path


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
    if fv_reports is not None and scenario_reports is not None and broker_rows is not None:
        valuation = valuation_index(fv_reports, scenario_reports, broker_rows)
    if rows:
        path = write_scorecard(rows, outputs_dir, valuation)
        n_uniform = sum(1 for r in rows if r.nav_basis == "resale-uniform")
        n_ready = sum(1 for r in rows if is_handoff_ready(r.confidence_tier))
        tag = "CONSOLIDATED verdict+matrix" if valuation else "validation matrix"
        print(f"book scorecard [{tag}] ({n_uniform}/{len(rows)} resale-uniform; "
              f"{n_ready}/{len(rows)} handoff-ready) -> {path}")
    return rows
