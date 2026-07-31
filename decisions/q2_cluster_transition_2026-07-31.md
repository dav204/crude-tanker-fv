# Q2 cluster transition — a DESIGN GAP found the hard way (2026-07-31)

**Status: finding recorded; three refreshes REVERTED to staged; the transition is now a
planned owner-gated event, not a per-name side effect.**

## What happened

Three Q2 report-day refreshes were done today (SB, TNK, ASC). Each wrote a
`{ticker}_2026-Q2.yaml` balance sheet AND edited the fleet manifest. The pipeline was run,
as always, with `2026-Q1`. Results looked plausible and were investigated in good faith
(SB +6.6%, TNK +4.8%, ASC +16.9%).

**They were artifacts.** `loaders.load_balance_sheet` resolves an EXACT path
`{ticker}_{quarter}.yaml` with **no fallback**, while `load_fleet_manifest(ticker)` is
**quarter-agnostic** — one file, always live. So a per-name refresh is **not atomic**:

- the manifest edit (the ASSET side: hulls added/removed, newbuild rows, ages) goes live
  on the current `2026-Q1` run immediately;
- the balance-sheet edit (the LIABILITY/cash side: commitments, debt, WC, held-for-sale)
  lands in a Q2 file that the Q1 run never opens.

The failure mode is therefore always in the same direction on a name adding newbuilds:
**count the asset, ignore the liability.** ASC is the clean demonstration — 4 Handysize
newbuild rows entered the curve at delivered PV while the Q1 balance sheet's
`newbuild_capex_commitments: 0` stayed in force, hiding the $183.6M commitment; NAV printed
+16.9% when the paired figures predict ≈ −2.9%.

## Why it wasn't caught immediately

The band-miss discipline worked — it flagged SB (0.6% over) and ASC (sign error, way over)
— but the INVESTIGATIONS then attributed the misses to substantive causes (SB: the
young-Panamax age-0 anchor; TNK: the VLCC old-age curve level) because those effects are
real and directionally present. **A plausible substantive explanation is exactly what makes
this dangerous:** the investigation stopped when it found a satisfying cause instead of
verifying that the inputs it reasoned about were the inputs the run actually used. The
TNK/SB attributions are NOT retracted as observations — they are re-labelled as
**unverified until recomputed on paired inputs**.

## Disposition

- Manifests for SB / TNK / ASC **REVERTED** to their Q1 state; the live run is coherent
  again (Q1 manifest + Q1 balance sheet), verified: SB $10.07 · TNK $77.73 (VALIDATED-TIGHT,
  TRIM/SHORT) · ASC $17.82 — all back to their pre-refresh values.
- The three **`*_2026-Q2.yaml` balance sheets are KEPT** — they are correctly sourced,
  cited, and reviewed (including the ASC as-of catch below). They are STAGED for the
  transition, not deleted.
- Pins that tracked the reverted manifests (SB fleet shape, SB scrubber ledger 19→20, TNK
  TIER_SUBREASON read-flips) reverted with them. The `newbuild_specs.yaml` registrations
  for TNK and ASC are KEPT — they are provenance facts about those orders, valid whenever
  the rows land.
- Findings that survive independently and stay on the record: the ASC as-of catch (the
  $165.2M installment table is dated 7/29, AFTER the $18.4M Q3 payment ⇒ the 6/30
  commitment is $183.6M with zero advances — verified twice in the filing); the Stage-A
  basis inventory; the ECO/LPG triages; the TNK/SB curve observations as hypotheses.

## The design gap, stated plainly

**Balance sheets are quarter-keyed; fleet manifests are not.** Nothing in the system
requires the two to be from the same quarter, and nothing warns when they aren't. During a
rolling earnings cluster — where names arrive one at a time over ~3 weeks — this makes
every individual refresh a half-application until the whole book transitions.

**Two candidate fixes (owner call, NOT taken tonight):**
1. **Loader fallback + disclosure** — `load_balance_sheet` resolves the newest sheet at or
   before the requested quarter, and the returned `BalanceSheet.quarter` self-reports the
   vintage actually used; the scorecard prints a balance-sheet-vintage header exactly like
   the price-basis header. Then the book can run as `2026-Q2` with refreshed names on Q2
   and the rest explicitly on Q1. This is the better design and it is what a rolling
   cluster needs.
2. **Atomic-quarter guard** — a test/preflight that hard-fails when a manifest's
   `report_date` disagrees with the run quarter. Cheap, catches this class forever, and
   does not fix the rolling problem (it forbids it instead).
**Recommendation: build (2) immediately as the guard, and (1) as the transition mechanism,
then re-run the three staged refreshes together as the Q2 cluster's first block.**

## Rule earned (for CLAUDE.md)

**A refresh is not applied until the run that consumes it uses BOTH halves.** Verify by
reading the run's own NAV breakdown (`outputs/<ticker>_fv_report.md`) and confirming the
balance-sheet lines match the file just written — before attributing any band miss to a
substantive cause. A satisfying explanation is not a verified one.
