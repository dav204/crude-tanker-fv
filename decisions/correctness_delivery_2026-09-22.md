# A1–A4 correctness and delivery — 2026-09-22

Owner authorized the implementation plan and requested that routine scheduled tasks stop parking on repeated approvals.

## Economic check

Compared all 25 schema-2.9 rows to the committed pre-change scorecard: independent NAV/share, scenario-weighted FV and single-point blend are exactly unchanged at exported precision. Scenario inputs, weights and cycle bands are unchanged. Broker reference NAV changes on 24 rows because the latest quote no longer divides a historical broker P/NAV. HAFN changes from $9.83/SANITY FAIL to $8.06/SANITY OK. Fourteen k_broker diagnostics breach their former drift anchor; per-name decision entries document the arithmetic correction. They are not tape-only annotations or economic revaluations.

## Migration

Governor review FV stamps remain SB $9.82, SBLK $29.79, CCEC $33.70. Historical fields not documented on the cards remain UNKNOWN and generate bootstrap review events. TEN's balance-sheet gate can now clear without silently clearing its family-minimum or qualitative gates. No trade or order change is authorized by this implementation.

The full filing queue reveals 100 unacknowledged arrivals, oldest 2026-07-14, with zero malformed rows. Many predate the September acknowledgment ledger. They are queued for evidence-based triage, not silently marked complete. Existing acknowledgments are retained. Bounded batches preserve total pending count and all remaining work.

## Execution and verification

Implementation and regeneration ran in isolated clones. Notification, healthcheck and landing fault tests use mocks. Detailed test results, shadow events, deployment and activation receipts will be recorded below before completion. The new worker must not be called operational until its installed launchd receipt is verified.

### Verification before installation

Full isolated producer run: 962 passed, 12 expected failures, three failures. The documentation cap and scoped-commit assertion were corrected; the remaining graph failure is the expected missing worker installation, to be rerun after installation. Focused follow-up: 33 documentation/promote/plist tests passed; 24 contract/delivery/filing/governor tests passed; two operation-receipt tests passed. Additional governor boundary tests cover exact family-minimum clearance, interval edges, vintage escalation and repeated review drift. DNS guard fixtures use a deterministic resolver. The isolated publication→consumer→failed-SMTP→five-minute retry test preserves the original message and review baseline and avoids a duplicate event.

The final regeneration again preserved all 25 independent NAV/share, weighted FV and blend values exactly. The existing automatic landing lane passed all five gates and committed the explained diagnostic re-anchor. Production source publication remains distinct from remote push.

Initial shadow events were inspected before enabling notifications: SB's weight-family sign instability and SBLK's weaker-basis read remain binding; historical sign-stability baselines for SB/SBLK/CCEC need explicit review; TEN's current-balance-sheet and TRMD's sign-stability gates have changed. TEN still fails the 20% family-minimum gate and lacks a Stage-A attestation; TRMD still lacks its tier/BUY and qualitative anchor gates. R-3 does not fire. The checker records SB's inside-interval position change without inferring its cause.

`read_flag` is governed for SB/SBLK; the producer's `n/a` on the other covered sectors is valid, with other gates evaluated normally. A regression now covers that distinction. No historical review baseline was replaced with a current observation.
