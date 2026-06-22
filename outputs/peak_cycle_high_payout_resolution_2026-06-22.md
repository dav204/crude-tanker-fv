# §12 peak-cycle high-payout — resolution memo

**Date:** 2026-06-22. **Trigger:** owner challenge to METHODOLOGY §12.1 ("…TRIM signals
that are mathematically internally consistent but commercially misaligned") — *are we
admitting the model doesn't value peak-cycle names correctly?* — surfaced while landing the
cycle-conditional terminal change (which made peak names more conservative, deepening the
apparent §12 tension). Resolved by a 4-agent analysis (theory/empirics · internal-consistency ·
resolution-design · adversarial steelman). **DECISION PENDING (owner). No further code/doc
changed pending this decision.**

---

## Verdict (answering the question)

**No — the model values peak correctly. §12 as written is the error, not the model.**

- A high-payout *pure-play* (single-class, ~100% spot-derived payout) at a genuine cycle peak,
  trading at a *true* P/NAV ~2.0×, is **overvalued on a through-cycle fair-value basis**. The
  model's "FV ≈ NAV → TRIM" is a **correct fair-value read** (it is flagging overvaluation),
  not an undervaluation.
- **Arithmetic** (NAT-like Suezmax, generous to the bull): buy at 2.0× P/NAV; collect the fat
  dividend down the cycle ≈ **+$4.6/sh**; asset value falls ~40% and trough P/NAV compresses to
  ~0.6× → capital ≈ **−$8.2/sh**; net ≈ **−36%** over ~2.5yr, worse after discounting. *The fat
  peak yield is the liquidation rate of a melting ice cube — the market handing you back your own
  capital while the asset de-rates underneath it.* For §12's "dividend stream is the value" to be
  true you'd need ~4.5yr of peak payout **with no de-rating** — a structural plateau, not a peak.
- **NAT is its own counterexample:** paid a famously high yield in 2015, then cut repeatedly into
  2017–18 as Suezmax rates collapsed; the stock lost most of its value paying out the whole way down.
- **The *valid* version of §12 — a dividend window decoupled from asset cyclicality via *contracted*
  charters — is already handled by the engine** (§3.2 coverage schedule; the GSL/MPCC machinery).
  For *spot*-derived payout (NAT), "I'm buying the dividend stream, not the NAV" double-counts the
  peak: the dividend and the NAV are the same bet on spot and fall together.
- §12's remedy ("treat FV as a NAV floor, don't act on the TRIM") is an **unfalsifiable one-way
  bullish override** — exactly the audit's finding **E-3**.

## The terminal change is vindicated — do not touch it

The 0.90× peak terminal **mean-reverts the aged *fleet asset-price level*** (a statement about
vessel values at the exit horizon) — name-agnostic, nothing to do with payout. A high-payout and a
low-payout VLCC own the same steel and should age-and-revert identically; payout flows through the
orthogonal `retained_per_share` term. **Exempting high-payout names from the 0.9× to "make room" for
§12 would be the forbidden back-solve.** The contradiction lived entirely in §12's prose claiming the
engine is too conservative right after the engine was *correctly* made more conservative. **Fix §12,
leave the terminal.** (The retained-earnings half is likewise orthogonal and correct.)

## The one steelman leg that survives — a refinement, not a reversal

The near-term **cleared-cash** component is structurally under-weighted at peak: `w_earn`=0.30
down-weights the near-term DPS strip (~27.4% of the strip is near-term cleared cash). Real. **But**
on NAT's own numbers, carrying that near-term DPS at full weight lifts FV ~$2.99 → ~$3.56 — the gap
to the $5.20 price closes from −42% to −32% and **the TRIM still stands.** So it's a refinement to be
*computed per-name*, not a blanket bullish veto.

---

## Recommended resolution — R3 (make §12 falsifiable, symmetric, computed)

Demote §12 from a prose override to a per-name classification the engine computes:

- **§12.5 Trigger gate** (mirrors §15.7's cheap gate): applies only when single-class
  (fleet Herfindahl ≈ 1) AND trailing payout > ~90% AND cycle position > 1.5× AND tool-P/NAV below
  market-P/NAV by > X. Else N/A.
- **§12.6 Break-even-dividend-window test** (the surviving steelman leg, computed): `Q* = min N such
  that Σ_{q≤N} DPS_q/(1+r)^(q/4) ≥ (price − tool_NAV_floor)`. Compare `Q*` to the rate-supported
  horizon implied by the FFA roll-off. `Q*` *inside* the supported horizon → undervaluation (floor
  framing). `Q*` *beyond* it → overvaluation, **TRIM stands**. For NAT (spot payout, retention ≈ 0,
  no contracted book) `Q*` is beyond → §12 **essentially never fires**.
- **§12.7 Ex-post falsification** (standing line in each §12 name's decision log): cumulative realized
  DPS + window-end price vs entry over 4–8q; a loss falsifies the undervaluation framing.
- **§12.3** "treat as floor / don't act on TRIM" → *gated on the §12.6 outcome*, not automatic.

**Code = one diagnostic, NO engine-valuation change** (book stays byte-identical / tests intact):
`scripts/dividend_window_test.py` (a `consensus_eps_xref`-style diagnostic) emitting
`outputs/dividend_window_test.md` with the per-name §12 / §12-inverse classification from the
already-loaded `dps_by_q` / `discount_rate` / FFA roll-off; a `high_payout_pure_play` flag +
`test_dividend_window_trigger_gate` (NAT in, DHT out); the §16 ledger row carries the resolved
direction + `Q*`. **Do NOT touch the terminal.**

*(R1 = "just reframe §12's prose, drop the bullish language" is the minimal coherent fix and is a
subset of R3 — adopt it immediately even if the §12.6 diagnostic is deferred. R2 = "model the
dividend window in" is what R3 selects per-name when the break-even test confirms the thesis. R4 =
status-quo/document-only is rejected: it leaves the contradiction standing.)*

---

## OWNER DECISION (to fill in)
- **§12 reframe:** ☐ R3 full (gate + break-even-window diagnostic + falsification) ☐ R1 prose-reframe now, R3 diagnostic deferred ☐ leave §12 as-is (not recommended)
- **Terminal change (cycle-conditional + retained earnings):** ☐ commit as-is (vindicated) ☐ bundle the commit with the §12 reframe ☐ other
- **Notes:**
