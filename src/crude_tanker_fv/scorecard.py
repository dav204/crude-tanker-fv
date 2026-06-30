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
from .normal_rates import (
    PARITY_BANDS,
    mean_reversion_gate_table,
    normal_rate_table,
    orderbook_crosscheck_table,
)
from .report import OUTPUTS_DIR

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
        ))
    return rows


def write_scorecard(rows: list[ScorecardRow], outputs_dir: Path = OUTPUTS_DIR) -> Path:
    outputs_dir.mkdir(parents=True, exist_ok=True)
    out: list[str] = []
    w = out.append
    w("# Book-wide validation scorecard (Thread 4)\n")
    w("Every covered name on ONE consistent, validated machine. **The product is the "
      "*boundary of what's comparable*, not a buy list.** `pending` ≠ `passed`: a name with a "
      "registered-pending gate is shown pending, never blessed. NAV age-0 basis is the uniform "
      "**xclusiv Resale** line (2026-06-22); mid-age is transaction-anchored (§9.9).\n")
    w("**Gates per name:** (1) NAV-basis (resale-uniform ⇒ comparable; else flagged); "
      "(2) Justified P/NAV both bases (§17); (3) parity band (§A1.2); (4) §18.5a mean-reversion "
      "(Thread 3, data-pending); (5) §18.5b orderbook cross-check (Thread 5, data-pending); "
      "(6) robust vs flips (does the read survive the parity↔historical choice).\n")

    w("| Ticker | Sector | NAV-basis | P/NAV(mkt) | Read par→hist | Robust? | Parity band | "
      "§18.5a | §18.5b | Verdict |")
    w("|---|---|---|--:|---|---|---|---|---|---|")
    order = {"crude": 0, "product": 1, "dry_bulk": 2, "lng": 3, "containerships": 4}
    for r in sorted(rows, key=lambda r: (order.get(r.sector, 9), r.ticker)):
        pm = f"{r.pnav_mkt:.2f}×" if r.pnav_mkt is not None else "n/a"
        w(f"| {r.ticker} | {r.sector} | {r.nav_basis} | {pm} | {r.read_par}→{r.read_hist} | "
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
    w("\n**Both §18.5 gates are registered-PENDING book-wide** — no Baltic $/day series (§18.5a) "
      "or orderbook ratios (§18.5b) in-repo; see `backtest/DATA_CONTRACT_NORMAL_RATES.md`. So no "
      "name is *fully* validated yet; the resale-uniform names are comparable and parity-banded, "
      "awaiting only the two data-gated gates.")
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
) -> list[ScorecardRow]:
    rows = compute_scorecard(quarter, inputs_dir)
    if rows:
        path = write_scorecard(rows, outputs_dir)
        n_uniform = sum(1 for r in rows if r.nav_basis == "resale-uniform")
        print(f"book scorecard ({n_uniform}/{len(rows)} resale-uniform; §18.5 gates pending) -> {path}")
    return rows
