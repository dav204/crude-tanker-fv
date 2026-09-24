# Publication repair — 2026-09-23

Owner asked to resolve the publication-hold notice. This repairs the production workflow; economic-method research remains unadopted.

## Findings

- The run state used the September 23 price file, but the committed scorecard still used the earlier $9.18 SB price. Current SB price is $8.37; NAV $10.72 and weighted fair value $9.01 are unchanged.
- The required SB BUY-flip fork was absent. The publisher only evaluates landing gates; its five-minute retry does not open the fork. Waiting alone could not start the objection window.
- Source changes include notification-only modules. The conservative source-coherence gate correctly requested regeneration; its generic message did not name those paths or SB.
- Ordinary regeneration checked only the scenario hash before reusing scenario-weight diagnostics. At the new prices, the handoff withheld required family fields. Rebuilding all five families clears the output-hygiene guard. scripts/regen.sh now always rebuilds those diagnostics before generating the book; --sidecars remains compatible.

## Measured result

All 25 names retain identical NAV, weighted FV, blended FV, scenario bounds, broker NAV, confidence tier and cycle readings. Prices and price-relative diagnostics move. The JSON companion records the full book comparison.

| Name | Price before → after | Label before → after | Weight sign stable before → after |
|---|---:|---|---|
| SB | 9.18 → 8.37 | HOLD (fairly valued) → BUY (undervalued) | False → True |
| CAPT | 19.7 → 18.45 | TRIM/SHORT (overvalued) → HOLD (fairly valued) | True → False |
| TRMD | 38.23 → 34.42 | TRIM/SHORT (overvalued) → HOLD (fairly valued) | True → False |
| FLNG | 32.42 → 30.97 | TRIM/SHORT (overvalued) → HOLD (fairly valued) | True → True |
| GSL | 45.84 → 44.55 | TRIM/SHORT (overvalued) → HOLD (fairly valued) | None → None |

## Authority and remaining hold

Fork buyflip_sb_2026-09-23 is OPEN under the standing three-business-day objection policy. It becomes executable on 2026-09-28. Execution permits the existing publication process to continue only if its other checks pass. No portfolio decision or governor review baseline changes here.
SB now has positive upside across the tested weight families at the lower price, but that observation is not an owner review. The prior accepted publication and its restrictions remain governing while publication is held.
Both producer and governor accepted-publication pointers and review baselines must remain unchanged during this repair. Raw generated outputs are not an accepted publication.

## Validation

Isolated Q2 regeneration with all five family diagnostics: output-hygiene checks passed.
Full suite: 1004 passed, 12 expected failures, and one failure caused by the isolated test
checkout lacking the local historical OCR fixture. Copied that source-data fixture and
re-ran the failing historical replay: 1 passed. Thus all 1005 ordinary tests passed;
no failing assertion was waived or threshold changed. Reconciliation: 25 names, zero
SANITY failures and zero reconciliation drift alerts. Producer drift gate: 25 rows,
zero unexplained changes, 22 explained. Shadow publication validation reports only the
open SB fork. The governor checker has no schema, missing-data or cycle-data errors;
it retains the owner baseline reviews and candidate restrictions. No transports invoked.
The existing production run state exactly matches the candidate's quarter, ticker values
and input hashes; no run-state copy or accepted-pointer change is required.

## Freshness while waiting

The prior accepted scorecard was generated 2026-09-22 at 19:47:40 UTC. Its 72-hour consumer
freshness limit is reached on September 25 at 15:47:40 America/New_York, before the
September 28 objection window ends. Retaining the standard window therefore means a
visible stale-data block over the intervening period unless a separately authorized
publication supersedes it. An earlier acceptance requires an explicit owner waiver of
this SB publication window; it does not authorize an order or a governor baseline reset.


## Owner waiver — 2026-09-23

The owner replied "yes" to the explicit request to waive this SB publication waiting
period and publish the verified price update now. The objection window is therefore
executed early by owner ruling. The standard September 28 date above is retained as
the audit history, not a remaining blocker. Scope: price-only publication and the
producer landing baseline required by the existing gated process. No trade, portfolio
decision, scenario-weight change or governor review-baseline reset is authorized.
