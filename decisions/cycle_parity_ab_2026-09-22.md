# D-M3 full-book eligibility outcome — 2026-09-22

**VOID; retain historical cycle denominators.** This records the original
`PRE_REGISTRATION_CYCLE_PARITY_DENOMINATOR.md` kill condition, not an adoption decision.

At frozen production commit `4f222489b1b2c918fc8cbcd578ed22fc60816b55`, the registered
contract-price/opex calculation supplies 10 of 19 covered vessel classes (52.63%).
This is an upper bound on fully dated source coverage, already below the required
80%. Classes without a calculable parity input set: Ctr-Feeder, Ctr-Intermediate,
Ctr-Large, Handymax, Handysize, LNGC, LR1, MGC and VLGC. Exact spellings and values
are retained in `research/economic-methods/results/parity.json`.

The latest input set therefore fails eligibility. The Q1-report-date and June 7
historical replays, cross-vintage stability and lock-time family tests were **not
run after the kill**; their verdicts remain null, not passed. The report-date
historical snapshot is not established; later information was not backfilled.
This does not claim that the missing source evidence can never be recovered.

No narrower study was substituted. A narrower follow-on requires advance
registration; a future eligible full-book run requires dated inputs at the three
specified vintages. D1 remains a separate owner decision. D-M4 smoothing is
reported independently with historical denominators, and the overdue LR1 round
remains a separately attributable adoption dependency.

Full package: `research/economic-methods/REVIEW.md`.
