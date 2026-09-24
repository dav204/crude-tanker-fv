# Broker P/NAV: do not buy separately yet

Independent broker ship-market reports do not replace equity analysts' P/NAV.
The former document ships and freight; the latter embed company balance sheets,
fleet assumptions and analyst valuation conventions. Buying one is not buying both.

The current book has 25 names, of which nine carry APPROX P/NAV classifications
(NAT, ASC, CCEC, TEN, CMDB, MPCC, GSL, SB and 2343). Those are excluded from
broker calibration denominators; several are book-value proxies or issuer-derived
values rather than Pareto observations. A new subscription should be priced on
its actual coverage, not a presumed 25-name independent check.

## Evidence reviewed

The 90-day decision-log scan is saved in diagnostic_history.json with source
hashes and selection rules. It found 26 relevant candidate sections: 24 instances
of the same A1 vintage correction and two contextual mentions (GNK's vessel
retro-flag correction and STNG's documented wide broker spread). It does not prove
that no other useful diagnostic occurred, nor does it establish a paid feed's
unique economic value.

A1 is material operational evidence: HAFN's apparent SANITY failure changed to OK
when the matched price/P-NAV pair was used. The correction changed diagnostic
broker NAV on 24 names while leaving economic values unchanged. This is evidence
of a source-vintage arithmetic problem, not evidence that paying for fresh broker
data would have corrected it. See decisions/correctness_delivery_2026-09-22.md.

GNK's correction concerned vessel transaction treatment and validator framing;
the retrieved log does not establish that paid P/NAV discovered it. STNG's wide
spread was explicitly documented as a feature. Neither establishes a standalone
purchase case. Do not classify routine broker-spread changes as investment gains.

## Controls that must survive exit

- Preserve independent fleet counts, units, balance-sheet coherence, transaction
  provenance, scenario arithmetic and the existing NAV/FV drift thresholds.
- Keep dated broker comparisons labelled archived. A missing live observation is
  UNAVAILABLE, not SANITY OK or no drift.
- The existing delta snapshot substitutes k_broker=1.0 and spread=0 without broker
  rows. Production removal must first replace those fallbacks with explicit
  unavailable states throughout drift/landing consumers. This trial does not
  authorize or make that production contract change.
- Historical sector calibration locks remain historical evidence. Removing a
  subscription does not re-run or silently erase those decisions.

Recommendation: defer a standalone quote/purchase until the live trial demonstrates
unique useful coverage or a replacement-control review establishes a necessary
unfilled check. Zero incremental cost is the preferred outcome, not a proven
conclusion that the diagnostic is worthless. Combined annual spending stays below
$1,500. FFA access receives priority within that budget.
