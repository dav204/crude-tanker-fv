# Q2 cluster transition — a DESIGN GAP found the hard way (2026-07-31)

**Status: RULED + MECHANISM LANDED 2026-08-08 (Decision block at the end of this doc);
the transition itself (price-absorb regen → Q2 block) is the next scheduled step.**

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

## Decision (2026-08-08) — owner ruling, as amended by the v2 vet

**Ruling 1 (morning): BOTH candidate fixes** — the atomic-quarter guard as backstop, the
loader-vintage fallback + disclosure as the rolling-transition mechanism.

**Ruling 2 (same day): the "Vintage Coherence v2" proposal, vetted and adopted as amended.**
A 5-agent adversarial vet (workflow `wf_56a55a2a-f74`) ran the proposal against both repos;
the owner then ruled on the package. What landed, exactly:

- **Mechanism A — loader-vintage fallback:** `resolve_balance_sheet_path` returns the newest
  sheet AT OR BEFORE the run quarter (never forward); `BalanceSheet.quarter` self-reports the
  vintage actually used; a file whose content disagrees with its own filename key hard-fails
  at the named file. Disclosure = the scorecard's exceptions-only **Balance-sheet basis**
  header + `balance_sheet_basis` (run-level map) + `names[].balance_sheet_vintage` (per-row,
  derived from the one map) in the JSON handoff — schema 2.6 → **2.7**, additive. The
  proposal's per-name md COLUMN was rejected (the consumer diffs JSON rows, never the md;
  the "header averages away the information" claim was false against the implementation).
  Consumer wiring landed governance-side in the same change (CADENCE seam + monitor PROMPT).
- **Mechanism B — pair guard:** `load_company_inputs` hard-fails when the manifest's quarter
  label disagrees with the RESOLVED sheet vintage (the run quarter is a ceiling, not an
  equality). The four proposal case rows are named tests in `tests/test_quarter_coherence.py`.
  Plus an **all-names preflight** in `pipeline.main()` (fail-BEFORE-writes, F-6 pattern) so a
  mismatch can never abort mid-write-loop and tear the committed outputs/ tree.
- **Mechanism C — reject as stated, adopt narrowed.** The proposed "any manifest content
  change requires a report_date change" rule was evidence-checked against all 35
  manifest-touching commits: 22 legitimate within-quarter edits would have false-fired
  (~96% FP rate), and post-guard-B a compliance bump is a label lie the guard converts into
  run failures. The narrowed form: `scripts/check_snapshot_advance.py` warns when a diff
  carries the snapshot-advance signature (age-basis line change / uniform age shift) without
  a `report_date` bump. **Evidence honesty (owner):** the signature was fitted on the SINGLE
  observed true positive (the SB 7/31 refresh, f8809d0) — 0/22 false positives is the tested
  half; the true-positive side is essentially untested. It ships as a WARNING with no
  enforcement authority; the higher-confidence half is the WORKFLOWS.md report-day step
  ("a snapshot advance moves BOTH halves in one commit").
- **The label-vs-truth residual (owner-named):** every mechanism above checks labels against
  labels; a sheet wrong-but-self-consistent passes all of them. Partial fix landed:
  **provenance at ingest** — `source_url` / `retrieved_at` / `filing_period_end` on every
  sheet keyed 2026-Q2 onward (guard-tested; the three staged sheets carry them), so each
  sheet has one anchor OUTSIDE the repo, spot-checkable in seconds. Additionally
  `add_ticker --quarter` is now REQUIRED and defined as the FILING's vintage (the old
  run-state default manufactured coherent-but-false labels).
- **Second instance of the half-application shape, found and closed:** `overlay_ledger`'s
  quarter default was max-over-file-keys — with staged future sheets present it computed the
  §12.6 dividend-window classification on exactly the three half-applied pairs (and its §15
  rows read newest-wins). Both now route through the book quarter + the same at-or-before
  resolver as the valuation. (`governance_rows` was also silently skipping numeric tickers —
  2343 — via an `[a-z]+` glob regex; fixed.) `pipeline.main()`'s hardcoded `2026-Q1`
  no-arg default (a guaranteed post-transition crash) now derives from `state/last_run.json`
  or requires an explicit quarter.
- **Reproducibility acceptance test re-scoped** per the vet: the true guarantee is
  RESOLUTION invariance (a Q1 run never reads later-keyed sheets) plus fail-loud (after a
  manifest advances, a Q1 re-run refuses at the pair guard). Byte-identical re-execution was
  never on offer: the JSON stamps `generated_at` by documented design, and the delta/log
  surfaces are stateful.
- **Deferred (recorded, not landed):** the staleness ceiling. The vet found warn>1q
  false-fires structurally on 2343 (semi-annual: lag 2 every Q4 window with no clearing
  action) and a loader hard-fail crashes 25 names for 1 (and contradicts the 5a3f28e
  loud-over-refuse precedent). Follow-up shape when taken up: cadence-aware threshold
  (per-name `reporting_cadence`, default 1), surfaced through the balance-sheet-basis
  header/banner + the sentinel's existing earnings-calendar checks, with the >3q ceiling as
  per-name exclusion — never a run crash. Also deferred: ruling the forward-keying
  convention for future semi-annual sheets (key at true vintage vs run slot).

**Transition sequencing (owner ruling — the split):** (1) guards + tests land as their own
commit (this one); (2) **price-absorb regen at 2026-Q1** — the 7/31→8/07 price vintage
(cd8f55f) absorbs against the Q1 book as its own ratify, so tape moves cannot launder into
the transition event (the 2026-07-26 dirty-tree rule, applied at event scale); (3) the
**Q2 transition** on a frozen tape: SB/TNK/ASC manifests advance WITH their staged sheets,
run as 2026-Q2. **Forward-invariance check at step 3 (vet gap #1):** every LAGGING name
reads identical inputs across the roll, so its NAV must print delta exactly 0.0 — any
nonzero delta on a lagging name IS the laundering signature and halts the transition.
Under the pair guard the three names are internally coherent independently; the block is
for attribution comparability (the VOIDed SB/TNK curve hypotheses re-test on paired inputs),
not correctness.
