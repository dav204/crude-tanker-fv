# CAPT — Stage-A void disposition: RETIRED (WO5/R4 Phase 4, 2026-09-18)

**RULING: RETIRE the void.** CAPT leaves `POSITION_UNRELIABLE`. The verdict cell now prints the raw
band. `read_blocked`, `GOVERNED-WIDE` and the `newbuild-heavy` sub-reason are separate machinery and
STAND, unchanged.

Ruled 2026-09-18 from the owner's chat ("rule the three dispositions") on the Phase-3 frozen
evidence, per `WO5_R4_DECK_REEXPRESSION.md` Phase 4. Companion rulings the same sitting:
`decisions/tnk_void_disposition_2026-09-18.md` (retired, cycle-relabel) and
`decisions/brut_void_disposition_2026-09-18.md` (UPHELD).

## The ground, and why it is resolved

`provenance.py` carried one ground for CAPT, quoted:

> 2026-08-10 Stage-A halt disposition (owner RULED B): the war-calibrated ABSOLUTE scenario deck
> against the re-anchored base makes the de-escalation legs near-no-ops — the BUY-ward flips
> (BRUT +44.3pp / CAPT +17.8 / TNK +5.0) are deck-incoherence ARTIFACTS, not signal. RETIRES for
> CAPT/TNK ... at the ... re-derivation which re-expresses the deck against the landed base.

It is a deck-construction ground and nothing else — not NAV quality, not provenance, not
governance, not evaluability. It named its own retirement condition, and that condition has now
occurred: the re-derivation was re-venued from the 8/16 toll cliff to this work order and landed
2026-09-18 (49e0fb9 / c5ce304, `decisions/r4_deck_reexpression_method_2026-09-18.md`). The defect
is gone and, for the first time, guard-held:
`tests/test_scenarios.py::test_crude_deck_prices_a_real_spread_against_the_base` reds if the base
walks under the deck again.

## The evidence, and the fact that decides it

**The artifact the void suppressed no longer exists, and its replacement is conservative.** The
work order calls CAPT "the one BUY-ward void at tape". That is no longer true. After the
re-expression CAPT reads **TRIM/SHORT at EV −5.97pp** — a short-shaped row, 0.97pp from the HOLD
edge. Retiring the void therefore publishes a read that is LESS favourable than the one the void
was suppressing, which is the opposite of the failure mode a void exists to prevent.

**Weight-robustness reversed in CAPT's favour, and the work order's evidence is superseded.** The
2026-09-01 sidecar read CAPT WEIGHT-DRIVEN (+6.7% BUY on Set A against −21.2% TRIM on the
conservative bracket). The post-re-expression sidecar, which the work order designates as the
Phase-4 evidence, reads CAPT **TRIM/SHORT across all eight weight sets**, EV −6.0% to −30.5%,
`weight_sign_stable: true`. The §8 weight finding routed to the owner cannot flip this name.

**Construction checks are clean.** `reconcile CAPT`: tool NAV $17.32 vs broker $22.31, −22.4%,
SANITY OK, Δ −0.1pp stable. The 9/18 gate row moved on EV only (+4.0pp), ΔNAV 0.00, predicted =
observed to the digit.

## The strongest case against, and why it does not carry

The sharpest objection is not the strobe; it is direction. **The re-expression moved CAPT's fair
value UP +4.50%, the same direction as the original artifact.** At the 2026-09-01 tape of $16.46
the new deck would have printed roughly +12.8%, a BUY. CAPT reads TRIM today partly because the
share has risen to $19.75 since. So a critic can say the void is being retired at a flattering
price, on machinery that still leans the way the artifact leaned.

It does not carry, for a reason this book has already ruled on: **a price may never certify
construction** (`test_tier_is_price_invariant`, tier amendment 2026-08-13). The disposition asks
whether the machine can be trusted, not which way it currently points. What changed is a
price-independent, guard-enforced property — every leg's forward-vs-base ratio is now pinned per
class with a minimum bear-to-observed spread, so "the de-escalation legs measure nothing" cannot
recur silently at any tape. The residual direction risk is handled by a re-cross trigger below, not
by freezing the name at "not actionable" indefinitely.

## What renders, and the strobe exposure (recorded, per the work order)

Exactly one cell changes: the verdict position goes from `unreliable read (not actionable)` to
`TRIM/SHORT (overvalued)`. The tier cell stays `GOVERNED-WIDE · newbuild-heavy`; handoff stays
ready; the W-frag marker stays stable. The book's name-specific-shorts line gains CAPT, going from
ten names to eleven — an addition to an existing list, not a change of kind. (The work order says
the book carries "not one is a name-specific short"; that sentence has been stale since 2026-07-10
and the surface already prints the ten-name list.)

**Strobe exposure, stated because it is real.** `read_blocked` suppresses `read_flag`, so the cell
carries NO hysteresis: the raw label restates on any tape move across a band edge. CAPT sits 0.97pp
from the HOLD edge, so the live exposure is a **TRIM/SHORT ↔ HOLD** strobe. It is NOT a BUY strobe —
the BUY edge is 11pp away — which is materially less consequential than the exposure the work order
anticipated when it expected a BUY-ward CAPT. The new pin
`test_read_blocked_and_not_unreliable_renders_the_raw_band` fixes this rendering so a future change
cannot silently route a read_blocked name through a deadband or drop the tier caveat.

## Riders

1. **BUY-ward re-cross trigger, armed.** If CAPT's raw band crosses to BUY on any future run, that
   is an owner eyeball under the standing Stage-A addendum rule — not an auto-accepted read. The
   drift gate raises it as a band flip; do not annotate it as mechanical.
2. **The rendering pin** ships in this commit, as the work order asked.
3. **The promote fixture** at `tests/test_promote.py::test_a_relabelled_name_does_not_count_as_buyward`
   read the LIVE registry with CAPT as its subject and would have gone red on this change; it is
   re-pointed to MPCC, whose ground is a method mismatch that no deck work touches. The work order's
   blast-radius list missed it.
4. **The stale registry pointer** ("RETIRES ... at the crude_day60_toll_cliff re-derivation
   (2026-08-16)") is corrected in this commit, as the work order directs for the first Phase-4
   commit.
5. **`PLAN.md` still describes CAPT as "the ONE BUY-ward void at tape (+9-10%)"** — stale as of this
   ruling; rewritten at the Phase-4 close.

## What this ruling does not do

It authorizes no capital and implies no position. It does not touch the tier, the read block, the
newbuild-heavy sub-reason, the §17 construction fact, or the edge-cleared set (which stays {SB} —
CAPT is excluded by tier, not by this registry).
