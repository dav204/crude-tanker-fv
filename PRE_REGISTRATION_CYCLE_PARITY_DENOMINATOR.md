# Cycle-denominator parity A/B — pre-registration (D-M3)

**FROZEN 2026-07-15 on owner ruling ("Proceed as recommended", methodology memo D-M3:
stage the Appendix-A pre-registration).** Method fixed BEFORE any result is computed;
the A/B RUNS after the Stage-A tanker re-anchor lands (≤ 2026-08-15) so the "latest"
vintage is the re-anchored curve, not the war hold. Amendments only via dated addenda
that do not loosen the acceptance criteria or kill condition. Source: Appendix A of
`outputs/METHODOLOGY_REVIEW_2026-07-14.md`, adopted verbatim with the run-timing note
and registered-artifact list added.

- **Hypothesis.** Replacing `historical_mean` with §18 `parity` as the cycle-ratio
  denominator produces band assignments that are (i) cross-sector commensurable and
  (ii) no less stable than the current basis, without degrading the calibration-lock
  reconciliation bars on any locked family.
- **Registered computation.** For every name, both ratios computed at three frozen
  vintages (2026-Q1 report date; 2026-06-07 war vintage; latest = post-Stage-A);
  band assignment under each; count of band disagreements; per-name FV under each
  (engine run with the alternative denominator behind a flag — **no production output
  changes**).
- **Registered acceptance criteria (frozen ahead of results).** (1) Parity-basis band
  flips vs history are explainable by the documented denominator biases (tanker nominal
  bias → expect some peak→elevated demotions; Handy/container elevated bias → expect
  some promotions); (2) no locked family's reconciliation moves outside its lock-time
  bar; (3) cross-vintage band stability (fraction of names holding band across the
  three vintages) ≥ the historical_mean basis.
- **Registered kill condition.** If parity inputs (newbuild price / opex / WACC grid)
  cannot be sourced at dated provenance for ≥ 80% of classes, the A/B is void — the
  denominator cannot be *less* provenanced than the anchors it replaces. (Known going
  in, recorded honestly: `newbuild_contract` deliberately omits LNGC/MGC/containers/
  LR1/product-Handies — the kill condition may fire or scope the A/B to the
  txn-anchored sectors; either outcome is information, not failure.)
- **Decision rule.** All three criteria pass → stage a D1-unfreeze ruling to adopt
  (SHARED with the D-M4 continuous-ramp adoption — one cycle.py round, one regen, one
  ratify); any fail → record, keep historical_mean, the §2.3 provenance table (already
  landed 2026-07-14) remains the documentation.
- **WACC basis note.** §18 `WACC_GRID = (0.07…0.10)`; the registered run uses
  `WACC_DEFAULT = 0.08` with the grid reported as sensitivity. D-M2 Option B (ruled
  same day) adopts a leverage-adjusted r_e for the STRIP; the parity WACC stays the
  *asset*-level rate — the two decisions are independent by construction.
- **Registered artifacts.** Run record → `decisions/cycle_parity_ab_<date>.md`
  (both-ratio table, band disagreements, stability fractions, per-name FV deltas,
  criteria verdicts); the flag stays out of production paths in all outcomes.

**Owner sign-off:** OWNER — ruled "Proceed as recommended" · **Date: 2026-07-15** ·
Runs after Stage A; adoption (if criteria pass) requires the separate D1-unfreeze
ruling, bundled with D-M4.
