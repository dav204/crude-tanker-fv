# Methodology review memo — blend structure, discount rate, cycle inputs (2026-07-14)

**Status:** FOR OWNER REVIEW — no engine change has been made; every recommendation below
is staged as a proposal, and the two that touch frozen surfaces (M-3, M-4 → `cycle.py`,
owner decision D1) are explicitly gated on a new owner ruling. · **Written:** 2026-07-14 ·
**Reviewer:** Claude (independent clone-and-run review — companion to
`outputs/EXTERNAL_AUDIT_2026-07-14.md`, which carries the ops/code findings; this memo
carries the methodology findings). · **Commit basis:** `1d3db14` (HEAD). · **Evidence
basis:** METHODOLOGY §§2–3, 9.2, 11.7–11.8, 17–18; `cycle.py`, `dividend_strip.py`,
`justified_pnav.py`, `normal_rates.py`, `nav.py`; the committed 2026-Q1 DHT report worked
through by hand; `inputs/market_data/historical_tce_means.yaml` and
`vessel_value_curves.yaml` provenance comments; RATIFY_LOG flip history 2026-07-02 → 07-14.

**Framing.** Nothing here is a defect — the 07-14 external audit verified the engine
reproduces byte-identical from a cold clone and the drift gate reads clean. These are
structural observations of the form *the model's reported structure implies more
differentiation and precision than its effective structure delivers, and the gap is being
paid for in owner attention* (flip eyeballs, staleness angst on low-leverage inputs).
Findings M-1, M-4, M-5 are three views of that one sentence.

---

## Findings register

| ID | Finding | FV impact | Effort | Touches frozen surface? | Disposition path |
|---|---|---|---|---|---|
| M-1 | Effective asset-value weight is ~0.65–0.85, not `w_nav`; strip terminal is ~half the strip leg. §2.1's "two independent lenses" overstates diversification and misorders the data-effort hierarchy | Understanding / effort allocation (no FV change proposed) | Low (reporting line) | No | Mechanical: add FV-attribution line to fv_report + one §2.1 sentence |
| M-2 | Flat 11% cost of equity across a book spanning net-cash → high-LTV compresses cross-sectional dispersion; flatters levered names' strip + §17 justified legs. Second order: container coverage-schedule cash discounted at spot-equity r | Cross-sectional, systematic, sign-known | Medium (~1 day + re-lock affected families) | No (`nav.py` constant, not D1) | Owner decision: leverage-adjusted r_e (Option B below) |
| M-3 | The cycle denominator is not one thing: true 10-yr mean (VLCC) vs 9-obs 2024–26 ELEVATED median (Handy-Bulk) vs boom-tilted FY21–25 avg (containers). "Cycle position" is not cross-sector comparable; band thresholds implicitly tanker-calibrated; nominal means bias tanker ratios high | Per-sector weighting regime (band selection) | Medium | **Yes — D1** | Pre-registered A/B: §18 `parity` as denominator (skeleton in Appendix A) |
| M-4 | Step-function bands (w_nav AND terminal_multiple step together) create discrete FV jumps at 1.5×/1.2×/0.8×/0.5× — ≈2.4% for DHT at the 1.5× edge before the terminal-multiple step. This is a standing generator of shallow-crossing flip-eyeball churn (open decision 9.1) | Removes a discontinuity class + governance load | Low-medium | **Yes — D1** | Owner decision 9.1: close as continuous ramp; pair with M-3 in one regen |
| M-5 | Verdict surface hands off point FVs/upsides with no value interval; tiers encode *validation* confidence, not *value* uncertainty. Flip triage ("shallow crossing") is therefore manual judgment that a printed interval would convert to a rule | Governance automation + honest precision at the handoff | Low (data already computed in scenario + 5×5 outputs) | No | Mechanical: FV interval column + interval-exit flip rule (schema bump) |
| M-6 | Smaller: (a) `scrap_25yr` anchors carry no dated provenance (unlike age-0/5/10 anchors) and drive the 10→25 slope that matters most for old fleets — newly relevant with 2343's handies; (b) off-hire is a global 0.02 constant, not a per-name/per-quarter schedule, though special-survey drydocks are lumpy and disclosed; (c) payout 0.95 base is the last non-cycle-aware strip parameter now that the terminal multiple is cycle-conditional (§3.4 already flags it) | Small, name-specific | Low each | No | Mechanical (a, b); (c) rides the existing §3.4 enhancement note |

---

## M-1 — The blend is ~85% asset value in effective terms

**Mechanism.** FV = `w_nav`·NAV + `w_earn`·strip, but the strip = PV(DPS, 8–10q) +
PV(terminal), and the terminal **is** NAV (fleet aged on the curve, cycle-conditional
multiple, retained earnings added — §9.2). So the asset-value content of FV is
`w_nav + w_earn × (terminal share of strip)`, not `w_nav`.

**Evidence (DHT, committed 2026-Q1 report).** NAV/sh $13.88. Strip $17.47 = $9.12
discounted DPS + $8.35 discounted terminal → terminal = **47.8% of the strip leg**.
Effective asset-value weight at peak weighting = 0.70 + 0.30 × 0.478 ≈ **0.84**. At trough
weighting (0.30/0.70) with a similar terminal share it is still ≈ 0.65. The blend's
apparent 0.70↔0.30 swing is, in asset-content terms, roughly a 0.84↔0.65 swing.

**Two consequences.**

1. *§2.1's language.* "Two independent valuation lenses" overstates the diversification:
   both legs share one driver (the rate cycle prices both ships and cash flows), and the
   strip hands back to NAV at the horizon. The honest sentence is that the strip
   contributes **timing information** — 8–10 quarters of contracted/forward cash and the
   fleet schedule — layered on an asset-value chassis. One sentence in §2.1 fixes this;
   no number moves.
2. *Effort hierarchy.* The lever order for data work is steeper than intuition suggests.
   Worked example: a **25% haircut to DHT's entire dividend leg** moves FV by
   0.30 × 0.25 × $9.12 ≈ **$0.68 (~4.6%)** — that is the outer bound of what the held
   war-vintage tanker FFA curve (the book's most prominent disclosed staleness, F-5
   residue) can be costing on a peak-weighted crude name. A 5% marks error moves FV
   through *both* legs at near-full strength (~4.5% directly through the NAV term alone,
   plus the terminal). Marks/curve provenance work has roughly **5× the FV leverage** of
   strip-side rate refreshes. The repo already prioritizes provenance — this makes the
   gradient explicit and defensible.

**Recommendation (mechanical, no owner ruling needed).** Add a standing **FV attribution
block** to each fv_report (and a book-level roll-up): FV decomposed into marks /
balance-sheet net / discounted DPS / discounted terminal / scenario-weight delta
(Model FV − Blend FV). All five numbers already exist in the report internals; this is a
rendering change plus a lock test. It also gives the pre-flight checklist a principled
sort order: refresh the inputs feeding the largest attribution term first.

---

## M-2 — Flat 11% cost of equity is a systematic cross-sectional bias

**Mechanism.** `COST_OF_EQUITY = 0.11` (shared `nav.py`/`dividend_strip.py`, BUG-7) prices
the strip and the §17 justified-P/NAV leg identically for every name. Equity risk scales
mechanically with leverage. Discounting a high-LTV name's DPS and terminal at the same r
as a net-cash name overstates the levered name's strip leg and its justified multiple —
i.e., the flat r **compresses exactly the dispersion a margin-of-safety gate exists to
measure**, and the compression has a known sign (flatters leverage). Post the null-IC
repositioning, the tool's claim is *absolute calibration*; an absolute margin of safety
computed at a leverage-blind discount rate is overstated precisely where safety matters.

**Second-order instance, same direction.** The §11.8 coverage schedule earns contracted
rates (MPCC FY-26 ≈ 99% fixed) — near-contractual cash from rated counterparties — yet
those quarters discount at the same 11% as uncovered spot dry-bulk quarters. This
understates the value of the very backlog the coverage machinery was built to capture,
and it partially offsets the §11.8.6 v1 limitation (charter-attached premium not in NAV)
in an unplanned way: two known biases in opposite directions is worse than one priced one.

**Recommendation (owner decision — two options).**
- **Option A (status quo, ratify):** keep flat 11%, document the leverage-blindness as a
  §12-class limitation with the sign stated. Zero effort; the bias stays but becomes a
  disclosed read-adjustment like §12/§15.
- **Option B (recommended):** unlever a per-sector asset "beta" (really: an asset-level
  r_a per sector, one new YAML block) and relever per name by debt/NAV — every input is
  already in the balance-sheet YAMLs; ~1 day including a sweep memo in the
  `terminal_value_options_memo` style showing the per-name FV deltas before adoption.
  Optionally (B′): discount coverage-schedule quarters at r_a (or r_a + a spread) and
  only uncovered quarters at r_e — one extra parameter, closes the container second-order
  item. Affected weight families re-lock per the standing bars.

Either way, keep the flat-r output as a reported sensitivity column for one quarter so
the delta is auditable.

---

## M-3 — The cycle denominator is not one thing (D1-gated; pre-registration skeleton in Appendix A)

**Evidence, from the input file's own comments** (`historical_tce_means.yaml`): VLCC
$40,000 is a genuine 10-yr mean; **Handy-Bulk $12,850 is a 9-observation 2024Q3→2026Q3
median carrying the file's own ELEVATED-bias caveat**; containers anchor on an MB
FY2021-2025 average annotated "boom-tilted, NOT a 10-year TC mean." The band thresholds
(1.5×/1.2×/0.8×/0.5×) were calibrated implicitly on the tanker basis and are reused
across all six sectors. Consequences:

1. **Cross-sector incomparability.** "Cycle position 1.3×" selects the same weighting
   band for 2343 (elevated 2-yr denominator → ratio biased **down** → more earnings
   weight, terminal multiple nearer 1.0) as for DHT (clean 10-yr denominator) while
   meaning different things. The per-class caveat comments are honest but the *band
   machinery consumes the ratios as if they were commensurable*.
2. **Nominal bias even where the window is clean.** Opex and newbuild parity inflated
   ~25–30% over the 10-yr window; a nominal trailing mean sets the "1.0×" reference too
   low for tankers, biasing their ratios high (DHT prints 2.79×) and pinning them in the
   peak band. Direction is conservative for longs at peak (more NAV weight), but it is an
   unmodeled tilt, and it interacts with M-4's hard thresholds.

**The fix is already built.** §18's `parity` basis — the TCE at which a *newbuild* earns
its WACC — is computable identically for every class from current newbuild price + opex +
WACC, is inflation-consistent by construction (newbuild prices are current-dollar), and
closes the §17 loop (parity is the rate at which justified P/NAV = 1.0 for a newbuild).
`cycle position = 12M TC / parity_class` would mean the same thing for every name in the
book. §18 was deliberately built as a no-headline-FV computation layer (owner decision
D1 froze `cycle.py`) — so this is a proposal to *graduate* one §18 basis into the cycle
input, via a pre-registered A/B, at the owner's option. Appendix A stages the skeleton.

**Interim step needing no ruling:** normalize the *documentation* — a one-table
`historical_tce_means` provenance summary (window, statistic, bias direction per class)
in §2.3, so the incomparability is visible at the point of use rather than only in YAML
comments.

---

## M-4 — Step-function bands are a standing generator of flip churn (open decision 9.1 — recommend closing it)

**Mechanism.** `_BANDS` steps **two levers simultaneously** at each threshold: `w_nav`
(±0.10) and `terminal_multiple` (±0.05). Crossing is driven by the 12M TC print — an
input that moves daily relative to a slow denominator.

**Quantified at the 1.5× edge (DHT).** w_nav 0.70→0.60 alone reprices FV from $14.95 to
0.60×13.88 + 0.40×17.47 = $15.32 — a discrete **+$0.36 (~2.4%) on a marginal TC tick**,
before the simultaneous terminal-multiple step (0.90→0.95, fleet value only) adds in the
same crossing.

**Governance cost, from the repo's own record.** The RATIFY_LOG's recurring individually-
eyeballed shallow flips — GSL BUY→HOLD (07-10), STNG HOLD→TRIM (07-10, "price-position
artifact"), ASC BUY→HOLD (07-13, "shallow price-crossing"), CMDB and SBLK BUY→HOLD
(07-14, +$0.49 / +$0.19) — are the price-band discontinuity class; the cycle-band class
is the same shape one layer down and fires whenever a TC print crosses a threshold. Every
such crossing consumes an owner eyeball under the (correct) don't-batch-accept rule.

**Recommendation.** Close open decision 9.1 as a **continuous ramp**: piecewise-linear
interpolation of (w_nav, terminal_multiple) between the current band midpoints (simplest,
preserves the current values at midpoints, zero new parameters), or a logistic if a
smooth derivative is preferred. Expected effects: the discontinuity class disappears, FV
becomes C0 in the TC input, drift decomposition gets cleaner (cycle drift becomes a
smooth attributable term), and a measurable fraction of flip-eyeball load retires.
D1-gated: stage as the same owner round as M-3 (one `cycle.py` change, one regen, one
re-ratify with both causes).

---

## M-5 — Put a value interval on the Verdict surface and make flip triage a rule

**Gap.** The tier column encodes *validation* confidence (is the read trustworthy); no
column encodes *value* uncertainty (how wide is the read). FV and Upside hand off to the
governance repo at $0.01 / 1pp precision. The inputs for an interval already exist per
name in committed outputs: the scenario deck (min/max scenario FV) and the 5×5 grid
(±1-cell neighborhood around base).

**Recommendation (mechanical; schema_version bump).**
1. Add `fv_low` / `fv_high` to the Verdict table and `book_scorecard.json` (proposed
   basis: scenario min/max, which is already probability-structured; the 5×5 ±1-cell is
   the fallback for names whose scenario deck is degenerate).
2. Define the flip rule: **a band flip is auto-classifiable as price-mechanical when the
   price remains inside [fv_low, fv_high]**; only interval-exiting flips require an
   individual owner eyeball. This converts the judgment the owner keeps making by hand
   ("shallow crossing, accepted") into a pre-stated rule — same governance philosophy as
   the drift gate's second-difference design: never ask a number to move, only ask an
   *unexplained* move to be explained.
3. Governance repo asserts the new schema_version on ingest (same requirement as F-4).

---

## M-6 — Smaller items

- **(a) Scrap anchors.** `scrap_25yr` rows in `vessel_value_curves.yaml` carry no dated
  source comments, unlike the age-0/5/10 anchors (xclusiv-dated). Scrap tracks LDT steel
  prices and moves; it is the anchor with the most curve weight for old fleets, which now
  matters more with 2343's handies (58 hulls, oldest cohort in the book). Give scrap the
  same dated-provenance + quarterly-refresh treatment as the other anchors. Mechanical.
- **(b) Off-hire.** `DEFAULT_OFFHIRE_RATE = 0.02` is a global constant with no per-name
  or per-quarter override. Special-survey drydocks are lumpy, scheduled, and usually
  disclosed; for a small fleet one drydock quarter is a visible EPS event. A per-quarter
  `offhire_schedule` (same optional-field pattern as `fleet_schedule`) is a cheap
  generalization, applied only where a name discloses drydock plans. Mechanical.
- **(c) Payout.** With the terminal multiple now cycle-conditional (§9.2, 2026-06-22),
  the 0.95 base payout is the last major non-cycle-aware parameter in the strip. §3.4
  already names cycle-linked payout as the enhancement; noting here only that its
  priority rises now that it is the *last* such parameter. Rides the existing note.

---

## Proposed disposition order

1. **M-1** attribution line + §2.1 sentence (mechanical, immediately improves effort
   allocation; makes M-2/M-3 deltas legible when they land).
2. **M-5** interval column + flip rule (mechanical + schema bump; retires governance load
   this quarter).
3. **M-2** owner ruling (Option B recommended; sweep memo before adoption).
4. **M-3 + M-4** as one D1 round: pre-registered parity-denominator A/B (Appendix A) +
   ruling on 9.1 continuous ramp; one regen, one re-ratify, flips eyeballed under the
   M-5 rule if it has landed first.
5. **M-6a/b** opportunistically with the next quarterly anchor refresh.

## DECISION blocks (owner)

- **D-M2 (discount rate):** ☐ Option A · ☑ **Option B leverage-adjusted r_e — RULED
  2026-07-15 ("Proceed as recommended"); B′ deferred to the container refresh as a
  rider; EXECUTION post-Stage-A (sweep memo gates adoption; flat-r sensitivity column
  kept one quarter)** · ☐ B′ now
- **D-M3 (cycle denominator):** ☑ **stage the Appendix-A pre-registration — RULED
  2026-07-15; FROZEN as PRE_REGISTRATION_CYCLE_PARITY_DENOMINATOR.md; A/B RUNS
  post-Stage-A; adoption needs the separate D1-unfreeze ruling** · ☐ decline
- **D-M4 (open decision 9.1):** ☑ **continuous ramp (piecewise-linear) — RULED
  2026-07-15; ADOPTION scheduled in ONE D1 round with D-M3's outcome (~late Aug: one
  cycle.py change, one regen, one ratify); open decision 9.1 CLOSED as ruled** ·
  ☐ logistic · ☐ keep steps
- **D-M5 (verdict interval):** ☑ **scenario min/max basis — RULED 2026-07-15 and
  EXECUTED SAME DAY** (fv_low/fv_high over weight>0 scenarios in the Verdict table +
  book_scorecard.json schema 2.4; the interval flip-triage rule implemented in
  drift_gate.evaluate: band-mech auto-classified inside the interval, band-EXIT keeps
  the eyeball; guard-tested; the M-1 book-level attribution roll-up noted for the same
  schema line at the next touch) · ☐ 5×5 basis · ☐ decline

---

## Appendix A — Pre-registration skeleton: parity-basis cycle denominator (M-3)

*To be frozen as `PRE_REGISTRATION_CYCLE_PARITY_DENOMINATOR.md` before any result is
computed, per house discipline.*

- **Hypothesis.** Replacing `historical_mean` with §18 `parity` as the cycle-ratio
  denominator produces band assignments that are (i) cross-sector commensurable and
  (ii) no less stable than the current basis, without degrading the calibration-lock
  reconciliation bars on any locked family.
- **Registered computation.** For every name, both ratios computed at three frozen
  vintages (2026-Q1 report date; 2026-06-07 war vintage; latest); band assignment under
  each; count of band disagreements; per-name FV under each (engine run with the
  alternative denominator behind a flag — **no production output changes**).
- **Registered acceptance criteria (frozen ahead of results).** (1) Parity-basis band
  flips vs history are explainable by the documented denominator biases (tanker nominal
  bias → expect some peak→elevated demotions; Handy/container elevated bias → expect some
  promotions); (2) no locked family's reconciliation moves outside its lock-time bar;
  (3) cross-vintage band stability (fraction of names holding band across the three
  vintages) ≥ the historical_mean basis.
- **Registered kill condition.** If parity inputs (newbuild price / opex / WACC grid)
  cannot be sourced at dated provenance for ≥ 80% of classes, the A/B is void — the
  denominator cannot be *less* provenanced than the anchors it replaces.
- **Decision rule.** All three criteria pass → stage a D1-unfreeze ruling to adopt;
  any fail → record, keep historical_mean, add the provenance table only.
- **WACC basis note.** §18 `WACC_GRID = (0.07…0.10)`; the registered run uses
  `WACC_DEFAULT = 0.08` with the grid reported as sensitivity. If D-M2 Option B adopts a
  leverage-adjusted r_e first, the parity WACC stays the *asset*-level rate — the two
  decisions are independent by construction.

---

## DISPOSITION (2026-07-14, same day — mechanical items executed; ALL FOUR DECISIONS RESERVED TO THE OWNER)

- **M-1 EXECUTED** (memo's own "no ruling needed" class): standing **"FV attribution"**
  block now renders in every fv_report (marks / balance-sheet net / §15 haircut when
  nonzero / discounted DPS / discounted terminal, footing to the blend FV, plus the
  effective asset-value share line); lock test
  `test_fv_attribution_block_foots_to_blend_fv` reproduces the memo's DHT 0.84. The fifth
  term (scenario-weight delta) already sits per-name in `book_scorecard.json` (blend vs
  scenario columns) — noted in the block rather than re-derived. The **book-level
  roll-up** is deferred to the M-5 schema round (it belongs in the scorecard, whose
  schema only bumps once). §2.1 amended with the effective-structure paragraph.
- **M-3 interim EXECUTED** (memo's own "needing no ruling" step): the denominator
  provenance table now sits in §2.3 at the point of use.
- **M-6c**: rides the existing §3.4 note, as the memo proposes. **M-6a/b**: registered in
  PLAN for the next quarterly anchor refresh (M-6a is value-touching when re-sourced —
  it takes the predict-bands-ahead discipline, not a same-day edit).
- **M-2 / M-3 / M-4 / M-5: NOT DECIDED — awaiting the owner's DECISION blocks above.**
  Staged in PLAN.md PENDING OWNER DECISIONS. Arithmetic verification performed before
  execution: COST_OF_EQUITY 0.11 shared (BUG-7) confirmed; `_BANDS` double-step
  confirmed; DHT decomposition (13.88 / 9.12 / 8.35 / 17.47 / 14.95 → terminal share
  47.8%, step +2.4% at the 1.5× edge) reproduces exactly from the committed report.
