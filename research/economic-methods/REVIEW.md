# Economic-method owner review · frozen 22 September 2026

Research package; no production adoption, publication, baseline reset or orders. All values are USD per share, including 2343.

## Recommendation

Keep production methods unchanged. The isolated engine and full-book experiment are implemented, but the package is **not ready for blanket adoption**. The cash/reference/risk numbers below are assumption-led diagnostics. Their missing inputs are adoption blockers, not resolved by passing tests.

| Method | Result | Recommendation |
|---|---|---|
| Payout/cash bridge | Quarterly ledger, policy variants, terminal claims and sensitivities implemented; 22 provisional standalone valuations; three hybrids withheld | Defer every name until source schedules, financing and distribution basis reconcile. Current hybrid corporate cash is shown once; joint-scenario FV remains unavailable. |
| Fixed scenario references | FFA-only invariance passes across all 25 names and hybrid sleeves; base migration delta zero | Defer adoption until vessel-mark/reference historical pairings are evidenced. The frozen current pair is a proposal, not recovered history. |
| D-M2 risk | External broad-transportation calibration, issuer leverage and propagation implemented | Defer every name. Six separate shipping-sector asset-risk calibrations remain unfinished; financing, cash and preferred/NCI conventions need review. Do not adopt the proxy as if independently calibrated by sector. |
| D-M4 smoothing | Independent and combined effects computed; continuous interpolation, existing labels retained | Mechanically ready for review. Adopt only through the ruled D1 round, after LR1 sequencing and explicit approval of outer anchors 0.30/1.70. |
| D-M3 parity | VOID under the original >=80% class-source-coverage kill condition | Retain historical denominators. Only 10/19 current classes are calculable (52.6%, an upper bound on dated coverage). Three-vintage stability/reconciliation was not performed after this stop. No narrower post-hoc adoption. |

## Before/after, independent effects and interactions

The ordered combination is cash → reference → risk → smoothing. Independent deltas are against legacy; interaction equals combined delta less their sum. Low/high assumption corners are not confidence intervals or guaranteed FV bounds. The reference base delta is zero for every name; its ±10% uncertainty stress is in the detailed results.

| Ticker | Legacy FV | Cash Δ | Risk Δ | Smooth Δ | Combined FV | Combined Δ% | Interaction |
|---|---:|---:|---:|---:|---:|---:|---:|
| DHT | 16.561 | -0.115 | 0.270 | 0.004 | 16.725 | 0.99 | 0.006 |
| ECO | 44.154 | -0.326 | 0.656 | 0.003 | 44.499 | 0.78 | 0.013 |
| FRO | 29.377 | -0.264 | 0.446 | 0.018 | 29.592 | 0.73 | 0.015 |
| INSW | 61.812 | unavailable | 1.200 | 0.010 | unavailable | unavailable | unavailable |
| TNK | 87.592 | -0.484 | 2.560 | -0.002 | 89.767 | 2.48 | 0.103 |
| NAT | 3.236 | -0.030 | 0.053 | 0.002 | 3.265 | 0.90 | 0.004 |
| FLNG | 29.474 | -0.327 | 0.050 | 0.058 | 29.250 | -0.76 | -0.005 |
| CCEC | 33.700 | -0.675 | -1.408 | -0.238 | 31.491 | -6.56 | 0.112 |
| STNG | 75.971 | -0.325 | 2.149 | -0.016 | 77.761 | 2.36 | -0.017 |
| HAFN | 5.468 | -0.034 | 0.090 | -0.000 | 5.524 | 1.02 | 0.000 |
| TRMD | 35.141 | -0.020 | 0.760 | 0.003 | 35.829 | 1.96 | -0.055 |
| ASC | 16.283 | -0.143 | 0.459 | 0.000 | 16.605 | 1.98 | 0.006 |
| TEN | 68.146 | unavailable | 0.387 | 0.024 | unavailable | unavailable | unavailable |
| CMDB | 19.297 | -0.125 | 0.587 | 0.002 | 19.742 | 2.31 | -0.018 |
| SBLK | 28.200 | -0.302 | 0.527 | -0.040 | 28.372 | 0.61 | -0.013 |
| GNK | 21.050 | -0.347 | 0.400 | 0.007 | 21.131 | 0.38 | 0.021 |
| CAPT | 18.571 | -0.104 | 0.299 | 0.017 | 18.795 | 1.21 | 0.012 |
| MPCC | 2.162 | -0.038 | 0.069 | -0.016 | 2.175 | 0.63 | -0.001 |
| GSL | 42.940 | -0.540 | 0.874 | -0.037 | 43.207 | 0.62 | -0.030 |
| BRUT | 5.511 | 0.039 | 0.126 | 0.001 | 5.680 | 3.07 | 0.004 |
| CMBT | 10.755 | unavailable | -0.011 | -0.009 | unavailable | unavailable | unavailable |
| SB | 9.007 | -0.198 | 0.168 | -0.034 | 8.939 | -0.76 | -0.005 |
| LPG | 31.824 | -0.266 | 0.635 | -0.007 | 32.192 | 1.16 | 0.005 |
| BWLP | 14.522 | -0.135 | 0.249 | 0.004 | 14.638 | 0.80 | -0.003 |
| 2343 | 0.370 | -0.005 | 0.010 | 0.001 | 0.376 | 1.62 | 0.001 |

Cash and risk effects can offset. They are not additive because discounting, retained cash, payout caps and cycle weights interact. CCEC is the largest combined decline in this frozen base corner; TNK is the largest dollar increase. These are model comparisons, not revised actionable price targets.

## Existing thresholds and restrictions

Independent current NAV is exactly unchanged in every available experiment. Broker matched pairs and prices are unchanged, so this work does not alter the broker-NAV spread or its multiplier. Baseline reproduction includes all governed numeric fields, intervals, labels, cycles, blend and hybrid contributions, not just rounded headline FV.

The existing >2pp EV, >2% NAV and >0.05 broker-multiplier drift thresholds are retained. The table below lists forcing breaches versus the committed producer baseline; raw states remain UNEXPLAINED pending owner acceptance, with no research re-ratification. An inside-interval band change is described as inside-interval, not proof of a price-only cause.

| Experiment | Forcing breaches | Missing computations |
|---|---|---|
| legacy | none | none |
| cash | CCEC: EV%; SB: EV% | CMBT, INSW, TEN |
| reference | none | none |
| risk | ASC: EV%; BRUT: EV%,band-mech; CCEC: EV%; CMDB: EV%; MPCC: EV%; STNG: EV%; TNK: EV% | none |
| smooth | none | none |
| cash_reference | CCEC: EV%; SB: EV% | CMBT, INSW, TEN |
| cash_reference_risk | BRUT: EV%,band-mech; CCEC: EV%; STNG: EV%; TNK: EV% | CMBT, INSW, TEN |
| combined | BRUT: EV%,band-mech; CCEC: EV%; STNG: EV%; TNK: EV% | CMBT, INSW, TEN |
| reference_risk_smooth | 2343: EV%; ASC: EV%; BRUT: EV%,band-mech; CCEC: EV%; CMDB: EV%; STNG: EV%; TNK: EV% | none |

The mechanically attributed source of each method move is its registered equation, with all other determinants fixed. Forcing moves are listed for review; the protocol has not been widened. Method-specific capital/retained-cash and discount-rate rows are in [DETAILS.md](DETAILS.md); scenario-level cash ledgers and vessel multipliers are in `results/<method>.json`.

Governor comparison uses the frozen review registry through the real checker with in-memory shadow envelopes. It does not consume live publications or update last-observed/review state. Construction tiers remain frozen input-quality classifications; they do not certify the new methods. All shadow documents carry an explicit research-only adoption gate.

| Experiment | New or changed conditions versus legacy | Conditions absent in that shadow only |
|---|---|---|
| cash | SB:FV_DRIFT (page); SBLK:CHANGED_read_flag (page); TEN:DATA_UNAVAILABLE (page) | SB:VALUATION_CONVICTION_ZERO; SBLK:READ_CAP; TEN:WIDE_CAP; TEN:GATE_current_balance_sheet; TEN:GATES_PENDING |
| reference | none | none |
| risk | SBLK:CHANGED_read_flag (page) | SBLK:READ_CAP |
| smooth | none | none |
| cash_reference | SB:FV_DRIFT (page); SBLK:CHANGED_read_flag (page); TEN:DATA_UNAVAILABLE (page) | SB:VALUATION_CONVICTION_ZERO; SBLK:READ_CAP; TEN:WIDE_CAP; TEN:GATE_current_balance_sheet; TEN:GATES_PENDING |
| cash_reference_risk | SB:CHANGED_read_flag (page); SBLK:CHANGED_read_flag (page); SBLK:READ_CAP (page); TEN:DATA_UNAVAILABLE (page) | TEN:WIDE_CAP; TEN:GATE_current_balance_sheet; TEN:GATES_PENDING |
| combined | SB:CHANGED_read_flag (page); SBLK:CHANGED_read_flag (page); SBLK:READ_CAP (page); TEN:DATA_UNAVAILABLE (page) | TEN:WIDE_CAP; TEN:GATE_current_balance_sheet; TEN:GATES_PENDING |
| reference_risk_smooth | SBLK:CHANGED_read_flag (page) | SBLK:READ_CAP |

No shadow recovery lifts SB sign-instability, SBLK read caps, candidate restrictions, war/thesis gates, or missing review-baseline attestations in production. Existing filing and quarterly follow-ups remain open. Owner review must distinguish data movement from acceptance of a new model.

## Financing and data exceptions

| Experiment | Names with a funding gap or intended-dividend shortfall in at least one case |
|---|---|
| legacy | none in computed cases |
| cash | FRO, TRMD, CAPT, BRUT |
| reference | none in computed cases |
| risk | none in computed cases |
| smooth | none in computed cases |
| cash_reference | FRO, TRMD, CAPT, BRUT |
| cash_reference_risk | FRO, TRMD, CAPT, BRUT |
| combined | FRO, TRMD, CAPT, BRUT |
| reference_risk_smooth | none in computed cases |

See `results/funding_exceptions.json` for each quarter/case and amount. Negative cash identifies required financing and is not an assumed borrowing facility. Zero modeled draws, sales, buybacks or issuance do not certify that no documented obligations/events exist. Full schedule verification remains open. Preferred/NCI and restricted-cash treatment are especially material for TEN, BWLP and the newbuilding names.

The normalized justified-P/NAV earnings diagnostic remains explicitly labelled as the legacy pre-depreciation proxy. Cash-strip accounting EPS has separate versioned semantics. Completing a reconciled normalized accounting-EPS diagnostic is an additional adoption task; changing its label alone would not fix the underlying definition.

## Evidence and reproducibility

Production input commit: `4f222489b1b2c918fc8cbcd578ed22fc60816b55`. Accepted publication retained: `402b3fc5d56691b112824b24acac4c9970220f35cc01d7e141ff94efe92dc700`. Governor registry frozen from `b7bd2b3163194cc8f689788a67a27be073cacff4`.

The preregistration was committed at `e533134` before changed fair values were evaluated. It freezes formulas, rates, source cutoff, analyst ranges, expected directions and invariants. Later source observations are recorded separately in [SOURCE_SUPPLEMENT.md](SOURCE_SUPPLEMENT.md); they have not been slipped into the comparison.

Identity checks passed over 3,792 current/scenario ledger rows. All 25 baseline fair values and governed handoff fields reproduce. Full verification commands and test receipts are in [VERIFICATION.md](VERIFICATION.md). A real committed shadow fixture is rejected by the publication validator as research; no SMTP or healthcheck transport was enabled.

Review [PARAMETERS.md](PARAMETERS.md) for issuer policy/rate assumptions, [DETAILS.md](DETAILS.md) for each name and sleeve, and `results/sensitivity.json` for frozen low/high corners. `results/comparison.json` retains every ordered experiment and interaction. `results/parity.json` records the void and unevaluated vintages.

## Owner decisions and adoption sequence

1. Complete issuer cash/claim schedules and verified accounting-to-distributable adjustments; resolve financing gaps and hybrid joint-scenario mapping. Replace proxy depreciation and reserve estimates with disclosed bases. Re-register source changes separately before recalculating effects.
2. Recover historical vessel-mark/reference pairings, or review an explicit alternative reference range as a new decision. Current-reference invariance proves the mechanism, not the historical calibration.
3. Finish independent shipping-sector asset-risk calibration; review the numerical rate table, funding rates, cash risk, leases, tax-shield and preferred/NCI treatment. Keep the 11% comparator and separate 11% newbuild / 8% parity rates.
4. Complete the overdue LR1 anchor round as its own attributed input leg. Then take the single ruled D1 cycle round: parity remains historical following VOID; review smoothing and its proposed outer anchors separately.
5. Only after scoped owner adoption: regenerate at a newly frozen live price/input vintage, explain existing-threshold breaches, review all governor events and expressly ratify any changed producer or governor review baseline. Processing/emailing a study never ratifies it.

## Rollback / storage

Implementation is retained on local branch `codex/economic-method-review`; production receives only review artifacts and operational status. Research code requires an isolated checkout, and research-marked handoffs cannot publish. To abandon the study, keep production as it is and stop invoking the research runner. Preserve the frozen package and receipts. Any later activation needs a separately reviewable commit and a recorded previous accepted-publication pointer; reverting that adoption must not erase receipts or reset governor baselines.
