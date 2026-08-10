# Stage A — HALT-AND-INVESTIGATE fired at the regen (2026-08-10); investigation complete

**The halt:** the ADDENDUM rule ("any flip toward BUY = halt-and-investigate") fired
THREE times at the Stage-A regen: **BRUT HOLD→BUY (+44.3pp EV) · CAPT HOLD→BUY
(+17.8pp) · TNK HOLD→BUY (+5.0pp)**, with every tanker EV up +4-14pp (14 UNEXPLAINED
gate rows) — under a re-anchor that cut the 8-quarter strip AVERAGE ~32%. NAV Δ = 0.0
on every row (correct — rates never touch NAV). Nothing is annotated or ratified;
the tree stands wired and the gate red pending the owner's disposition.

## Investigation (the input is CLEAN; the composition is the break)

1. **Not the promoted inputs.** Every §5 check was done pre-wiring (breaches
   investigated + owner-accepted); the base-curve single-point FVs moved the RIGHT
   way (BRUT single FV $9.31 → $8.83; strip implied $10.51 → $8.92).
2. **The scenario deck did it.** `scenario_inputs.yaml` scenarios are ABSOLUTE
   8-quarter curves (built 2026-05-29, war-re-tilted since). The engine flexes each
   scenario's vessel values by its rate path RELATIVE TO THE BASE (the Vessel×
   elasticity). Against the war base (12M 111.5k), Pre-MoU (assumed 12M 106.1k,
   weight 0.57) read as a real de-escalation → Vessel× 0.82, NAV/sh $3.29. Against
   the NEW base (12M **105.7k** — the Mount Horizon ruling), the SAME absolute path
   reads as ~zero de-escalation → Vessel× **0.96**, NAV/sh **$7.65**. Same shift on
   MoU-base (0.74→0.86) and MoU-bear (0.70→0.79); Escalation unchanged (1.25×).
   Weighted FVs jump book-wide; spot-heavy/NB names (BRUT, CAPT, TNK) jump most.
3. **Why this is incoherence, not signal:** the new base's back half (VLCC Q5-8
   48.85k) ALREADY embeds the Jaguar term print's de-escalation; the deck then
   prices de-escalation AGAIN as scenarios — which have become near-no-ops against
   the new base. The de-escalation risk the 0.57+0.05+0.13 weights exist to carry
   has been silently absorbed into the base, leaving the deck measuring ~nothing.
   The prereg §0 fenced scenario weights OUT of Stage A ("the Hormuz re-tilt is its
   own thread; scenario deltas stay expressed relative to whatever base curve this
   re-anchor lands") — the deltas now need RE-EXPRESSING against the landed base,
   and **the pre-registered venue for exactly that is `crude_day60_toll_cliff`
   (2026-08-16, crude+product, "full MoU-family re-derivation regardless of
   outcome")** — six days out.

## Disposition options (owner rules; no unilateral revert per the standing rule)

- **(B) LAND + VOID the affected reads until 8/16 (RECOMMENDED):** ratify the rate
  promotion (inputs verified; deadline ≤8/15 honored); mark the THREE BUY-ward flips
  PROVISIONAL·deck-incoherence — not actionable — via the POSITION_UNRELIABLE
  registry (the BRUT sign-unstable precedent); the 8/16 toll-cliff re-derivation
  re-expresses the deck against the landed base and the flips re-read there. One
  FV-moving event at a time is preserved (8/16 was already scheduled).
- **(A) REVERT the wiring until 8/16**, land rates + deck together: one coherent
  repricing, but BREACHES the frozen prereg's unconditional ≤8/15 deadline (needs
  an owner amendment) and keeps the 10-week-old war vintage live longer.
- **(C) Pull the deck re-derivation forward to TODAY:** violates one-event-at-a-time
  and guesses the toll outcome the 8/16 venue exists to observe.
