# R4 / WO5 Phase 0 — crude deck re-expression: method, derivation and the Phase-3 freeze

**Status: Phases 0-3b EXECUTED 2026-09-18 from the owner's chat** ("now do WO5 phases 0-3b").
Authority: `WO5_R4_DECK_REEXPRESSION.md`, ratified 2026-09-01; fork
`r4_wo5_deck_reexpression_schedule` in `inputs/forks.yaml`, registered 2026-09-10,
`execute_after` 2026-09-15, unanswered. **Phase 4 (the three per-name void dispositions) and
Phase 5 (ratify, push) are NOT in this record — they are owner acts by the WO's own law.**

---

## 1. What was ruled, and what this executes

The Phase-0 fork was ruled at ratification (2026-09-01): **Fork B + C**.

- **Fork B — one-time re-derivation.** New absolute per-quarter paths calibrated to the live base,
  each leg's registered meaning re-expressed as a real spread: escalation = a genuine upside tail ·
  `pre_mou_baseline` ~ the observed state ~ base-tracking · `mou_bear` = normalization-disappoints ·
  `mou_base` re-derived too (zero weight, but its curve binds the bear-below-base ordering guard).
- **Fork C — the deck-coherence guard**, a test asserting each crude scenario's implied
  forward-vs-base spread stays inside registered bounds. Red = the deck has gone no-op again.
- **Fork A** (convert the deck to relative multipliers) stays registered as the Q4 refactor
  candidate. NOT ruled, NOT done here.

**Frozen inputs, byte-untouched by this work:** the scenario WEIGHTS. The WO names the C2 vector;
the live vector is C3 (0.28 / 0.59 / 0.00 / 0.13, `escalation_c3_rearm` executed 2026-09-10), which
the fork's own recommendation names as the frozen input. No weight moved.

## 2. The mechanism, stated exactly

`scenarios.run_scenarios` flexes each scenario's vessel values by its rate path relative to a FIXED
reference:

    scen_forward[leg] = sum over classes of value_weight * mean(leg 8-quarter mid curve)
    forward_ref       = sum over classes of value_weight * mean(ffa_forward_curve[class])
    vessel_scale      = clamp(1 + 0.5 * (scen_forward / forward_ref - 1), 0.65, 1.25)

The reference is `inputs/market_data/ffa_forward_curve.yaml` — the current trader forward, a fixed
anchor so the base-case NAV does not move when the scenario set changes. The leg curves are
ABSOLUTE dollars/day, built 2026-05-29 and war-re-tilted 2026-07-02. **The base has been re-anchored
repeatedly since; the curves were not.** That is the whole bug.

## 3. The diagnosis, measured 2026-09-18

Ratio = the leg's 8-quarter mid mean divided by the FFA 8-quarter mean for the same class.
Reference vintage: crude classes as-of 2026-09-09 (the post-Stage-B base the fork names) — VLCC
92,650 · Suezmax 63,225 · Aframax 54,250 · LR2c 41,907.

| Leg | vlcc | suezmax | aframax_dirty | lr2_clean | registered meaning |
|---|--:|--:|--:|--:|---|
| escalation | 2.99 | 2.11 | 1.71 | 3.94 | upside tail |
| pre_mou_baseline | 0.95 | 0.80 | 0.72 | **1.18** | the observed state |
| mou_base | 0.74 | 0.66 | 0.63 | 0.93 | normalization-partial |
| mou_bear | 0.59 | 0.57 | 0.54 | 0.69 | normalization-disappoints |

**The incoherence is not (only) the one the 2026-08-10 halt named.** That record's complaint —
`pre_mou_baseline` reading as near-zero de-escalation at Vessel-multiple 0.96 — has since been
overtaken: the leg's registered meaning CHANGED (doha restore 7/12, C2 8/16, C3 9/10; the block
comment now reads "the MoU-ineffective leg IS now the observed state"), and at THAT meaning a
base-tracking ratio is correct, not broken. What is demonstrably broken today is **class
inconsistency**: the same leg means four different things depending on the class.
`pre_mou_baseline` prices a 28% forward discount for Aframax, a 20% discount for Suezmax, a 5%
discount for VLCC and an 18% PREMIUM for clean LR2. A leg whose meaning depends on which hull you
own is not a scenario.

## 4. The derivation (Fork B), and the one sub-decision inside it

**Method: uniform per-class re-levelling.** For each of the three de-escalation legs and each of the
four classes, every quarter's low/mid/high triple is multiplied by a single factor chosen so the
leg's 8-quarter mid mean hits its registered target ratio, then rounded to the nearest $100.

**Sub-decision (mine, recorded rather than buried): the quarter SHAPE is preserved, only the LEVEL
moves.** The alternative — re-deriving each quarter independently against the forward's own term
structure — would discard the legs' registered term stories (the q3_2026 war spike decaying into a
structural back half), which no ruling asked to revisit. Re-levelling is the minimal, auditable
change that restores the registered meaning, and it keeps every leg's internal shape and its
low/mid/high spread intact.

**Escalation is NOT re-derived.** All four of its classes already sit far above the 1.25 vessel
clamp, so its vessel multiple is 1.25 either way; re-levelling it would change only its EARNINGS
leg, on a tail whose registered meaning nobody has questioned. The 2026-08-10 record made the same
call ("Escalation unchanged (1.25x)"). Its ratios are registered as a floor in the guard instead.

**Registered targets and achieved ratios (all four classes, after integer rounding):**

| Leg | target ratio | achieved | Vessel multiple before -> after |
|---|--:|--:|---|
| escalation | >= 1.50 (untouched) | 1.71 - 3.94 | 1.250 -> 1.250 (clamped) |
| pre_mou_baseline | 1.00 | 1.000 | 0.86 - 1.09 -> 1.000 |
| mou_base | 0.80 | 0.800 | 0.81 - 0.97 -> 0.900 |
| mou_bear | 0.60 | 0.600 | 0.77 - 0.85 -> 0.800 |

Ordering after the re-derivation, per class: mou_bear 0.60 < mou_base 0.80 < pre_mou_baseline 1.00
< escalation >= 1.71. The bear-below-base guard in `tests/test_scenarios.py` holds by construction.

## 5. Fork C — the deck-coherence guard

`tests/test_scenarios.py::test_crude_deck_prices_a_real_spread_against_the_base` asserts, for every
leg and every class, that the ratio above sits inside its registered band, and that the
bear-to-pre-MoU spread stays at least 0.30 wide. It reds when the base moves far enough that a leg
loses its registered meaning — the next time this bug starts to recur — and when someone edits a
curve out of its band. Guard over prose: this is the durable artifact of the whole work order.

## 6. PHASE 3 — THE FREEZE (dated 2026-09-18, computed off-tree BEFORE anything landed)

Computed in an isolated worktree of `421bf77` with the staged deck applied and nothing else
changed; the live tree was not touched. Comparator: the committed surface at `3eefd88`.

| Name | Sector | ΔNAV/sh | FV before | FV after | ΔFV % | EV before | EV after | ΔEV pp | Rendered read |
|---|---|--:|--:|--:|--:|--:|--:|--:|---|
| 2343 | dry_bulk | +0.00 | 0.37 | 0.37 | +0.00 | -29.8 | -29.8 | +0.0 | unchanged |
| ASC | product | +0.00 | 16.28 | 16.28 | +0.00 | -14.2 | -14.2 | +0.0 | unchanged |
| BRUT | crude | +0.00 | 5.35 | 5.51 | +2.99 | +2.1 | +5.2 | +3.1 | unchanged |
| BWLP | lpg | +0.00 | 14.52 | 14.52 | +0.00 | -43.2 | -43.2 | +0.0 | unchanged |
| CAPT | crude | +0.00 | 17.77 | 18.57 | +4.50 | -10.0 | -6.0 | +4.0 | unchanged |
| CCEC | lng | +0.00 | 33.70 | 33.70 | +0.00 | +50.8 | +50.8 | +0.0 | unchanged |
| CMBT | crude | +0.00 | 10.50 | 10.81 | +2.95 | -47.9 | -46.4 | +1.5 | unchanged |
| CMDB | dry_bulk | +0.00 | 19.37 | 19.37 | +0.00 | -19.3 | -19.3 | +0.0 | unchanged |
| DHT | crude | +0.00 | 16.32 | 16.56 | +1.47 | -29.3 | -28.3 | +1.0 | unchanged |
| ECO | crude | +0.00 | 42.22 | 44.15 | +4.57 | -50.1 | -47.8 | +2.3 | unchanged |
| FLNG | lng | +0.00 | 29.47 | 29.47 | +0.00 | -9.3 | -9.3 | +0.0 | unchanged |
| FRO | crude | +0.00 | 28.79 | 29.38 | +2.05 | -43.5 | -42.4 | +1.1 | unchanged |
| GNK | dry_bulk | +0.00 | 21.14 | 21.14 | +0.00 | -24.8 | -24.8 | +0.0 | unchanged |
| GSL | containerships | +0.00 | 42.94 | 42.94 | +0.00 | -6.9 | -6.9 | +0.0 | unchanged |
| HAFN | product | +0.00 | 5.47 | 5.47 | +0.00 | -44.2 | -44.2 | +0.0 | unchanged |
| INSW | crude | +0.00 | 59.91 | 61.81 | +3.17 | -46.1 | -44.4 | +1.7 | unchanged |
| LPG | lpg | +0.00 | 31.82 | 31.82 | +0.00 | -44.8 | -44.8 | +0.0 | unchanged |
| MPCC | containerships | +0.00 | 2.16 | 2.16 | +0.00 | -27.9 | -27.9 | +0.0 | unchanged |
| NAT | crude | +0.00 | 2.97 | 3.24 | +9.09 | -63.7 | -60.4 | +3.3 | unchanged |
| SB | dry_bulk | +0.00 | 9.08 | 9.08 | +0.00 | +1.9 | +1.9 | +0.0 | unchanged |
| SBLK | dry_bulk | +0.00 | 28.34 | 28.34 | +0.00 | -11.6 | -11.6 | +0.0 | unchanged |
| STNG | product | +0.00 | 75.97 | 75.97 | +0.00 | -13.3 | -13.3 | +0.0 | unchanged |
| TEN | crude | +0.00 | 61.80 | 65.59 | +6.13 | +17.6 | +24.8 | +7.2 | unchanged |
| TNK | crude | +0.00 | 83.24 | 87.59 | +5.23 | -17.2 | -12.9 | +4.3 | unchanged |
| TRMD | product | +0.00 | 35.14 | 35.14 | +0.00 | -6.0 | -6.0 | +0.0 | unchanged |

**The frozen expectations, which the production landing must reproduce or HALT:**

1. **NAV/share moves EXACTLY 0.00 on all 25 names.** The re-derivation moves no mark and no balance
   sheet; the headline NAV is the unflexed reference.
2. **Every non-crude name EXACTLY 0.00 on FV and EV** — all 15 of them (2343, ASC, BWLP, CCEC,
   CMDB, FLNG, GNK, GSL, HAFN, LPG, MPCC, SB, SBLK, STNG, TRMD). This is the determinant-leg law;
   a frozen-leg name printing nonzero is a HALT, not a surprise.
3. **Exactly 10 crude names move, all upward in FV**, between +1.47% (DHT) and +9.09% (NAT).
4. **Exactly six rows breach the drift gate's 2pp EV threshold** — BRUT +3.1, CAPT +4.0, ECO +2.3,
   NAT +3.3, TEN +7.2, TNK +4.3 — and each needs a dated per-name log annotation. Four crude names
   move under the threshold and raise no gate row: CMBT +1.5, DHT +1.0, FRO +1.1, INSW +1.7. (The
   WO's estimate of about nine rows was written before C3; six is the measured number.)
5. **No RENDERED band flips**, on any name.
6. **Exactly two test pins move**, both named in the WO's blast-radius list: the INSW whole-company
   FV pin in `test_scenarios.py` (62.82 +/-2.5% -> 65.40) and the ECO whole-company EV pin in
   `test_eco.py` (-3.0..0.0 -> +0.10). Both are re-pinned in the landing commit citing this record.
   Every other pin the WO listed as possibly moving held: the bear-below-base ordering, the FRO
   TRIM pin, the TEN pins, `test_nav_flexes_with_scenario`.

**HALT RULES for the production landing:** any non-crude name moving at all · any name's NAV moving
· any rendered band flip · any crude name outside its frozen change in FV by more than 0.05pp · any
test red other than the drift gate and the two re-pinned pins. On a halt: stop, do not revert, page
the owner (the standing no-unilateral-revert rule).

## 7. THE ONE MATERIAL FINDING — BRUT crosses the BUY edge by 0.2pp, under its void

The re-expression moves BRUT's RAW band from HOLD to BUY: EV +2.1 -> **+5.2**, against a +5.0 edge.
That is **0.2pp of margin**, with no hysteresis on the raw label.

This does NOT trip the WO's kill-switch, which fires on "any flip toward BUY on a NON-void name".
BRUT is one of the three Stage-A voids; its rendered read stays "unreliable read (not actionable)"
before and after this landing, and this work retires no void. But it is exactly the evidence the
owner's Phase-4 BRUT disposition turns on, and it is fragile: a 0.2pp margin is inside the noise of
a single day's tape.

**Stated plainly for the Phase-4 sitting:** after this re-expression, retiring BRUT's void would
publish a BUY-shaped read on a hairline. CAPT's raw band does not flip (-10.0 -> -6.0) but now sits
1.0pp from the HOLD edge, which sharpens the strobe exposure the WO already flagged for it. TNK
moves -17.2 -> -12.9 and stays comfortably TRIM-shaped, unchanged in character.

## 8. Findings routed to the owner, NOT resolved here

1. **A weight question the WO fences out of scope.** After this re-expression, 59% of the crude
   probability mass sits on a leg that tracks the base by construction and 13% on the only leg
   pricing a real downside. The deck is now internally coherent and class-consistent, but its
   de-escalation CONTENT is a function of the weights, not the curves. The WO's kill-switch is
   explicit: "any scenario WEIGHT question surfacing = finding to the owner, never in-scope work."
   Raised, not touched.
2. **The product deck's own re-expression.** Unanswered by design — this WO is crude-scoped. The
   product legs carry the same absolute-curve construction against the same moving base.
3. **The stale pointer at `provenance.py:152`** ("RETIRES ... at the crude_day60_toll_cliff
   re-derivation") is superseded by this docket. The WO assigns that comment fix to the FIRST
   Phase-4 disposition commit, so it is deliberately NOT fixed here.

## 9. What this record does not do

No void retired · no weight moved · no tier moved · no registry edited · no ratify · no push. The
post-re-expression crude sidecar regenerated by the landing supersedes the 2026-09-01 sidecar as the
weight-robustness evidence for Phase 4, as the WO directs.
