# PLAN.md — active plan / sprint handoff

A new agent reads CLAUDE.md, then this file, then starts. This is a
**forward-looking valuation aid** for shipping equities (independent NAV +
forward dividend strip, blended by cycle position), judged by the soundness of
its per-name reads — not by a cross-sectional backtest.

**Current state (2026-07-02):** **22 watchlist names across 5 sectors**; **444 main
tests green, 16 xfailed** (+13 backtest via `PYTHONPATH=. pytest backtest/`; +57 harvester
via `.venv310`); drift gate **0 unexplained** (TRMD explained); pipeline clean; SANITY 14 OK / 8
n-a-APPROX / 0 FAIL. **The P0 reconciliation queue (`NAV_FIGURE_ESTIMATE_QUEUE ∩ PROVISIONAL`) is CLEARED —
EIGHT names done: NAT/SB/ASC/BRUT/ECO/HAFN/STNG/TRMD.** EIGHT P0 names worked this arc: **NAT DE-VOIDED** (2026-06-30, NAV $2.07→$2.79,
GOVERNED-WIDE·newbuild-indeterminate), **SB corrected** (date-mix + CAPT blanket-scrubber bug; NAV
$10.47→$10.12, ~0.63×), **ASC reconciled** (April-2026 newbuild wrongly loaded as a −$88.8M Q1
commitment [subsequent event] + phantom `Ardmore_Patriot` removed + chem-Handies → cited 20-F
carrying-value floor; NAV $15.96→$17.80, PROVISIONAL → GOVERNED-WIDE, BUY +5.2%), and **BRUT traced**
(2026-07-01 — a DIFFERENT outcome: the reconciliation VALIDATES the model [commitment $1,373.1M ≈ Pareto
$1,370M; debt $0; shares 61.9M all now issuer-traced] but BRUT STAYS PROVISIONAL — cash booked at a $66M
conservative floor keeps it flagged `cash-pending-H1-report`; also fixed a fabricated governance block +
flagged going-concern doubt; NAV $9.40→$8.80; NOT actionable — going-concern-doubtful, max-torque), and
**ECO cleared to VALIDATED-TIGHT** (2026-07-01 — the first TIGHT of the arc; figures all verified vs the
Q1-2026 6-K, the 2 Suezmax NBs wired on-curve §9.6 + 16 scrubbers verified; the value-flag guard caught a
peer-default and the NBs were booked scrubber=false; NAV $34.56→$34.35 [sub-threshold]. But ECO is
validated-but-RICH [rich · cycle position, ~1.39× NAV] — NOT a new long), and **HAFN reconciled**
(2026-07-01 — the most consequential: an ASC-pattern 3-Apr-2026 subsequent-event newbuild removed [+$365M],
debt/lease corrected to the Note-2/4 split [−$46M], the TORM stake to Hafnia's own lower-of-cost NAV basis
[−$118M; precedent: marketable stakes take the issuer's method], and operating WC held at a conservative
pool-gross-up floor [precedent: pool receivables are custodial, not NAV-economic]; NAV $5.22→$5.57, stays
PROVISIONAL·pool-gross-up-pending, rich · cycle position — NOT actionable; price-refresh isolated out), and
**STNG reconciled** (2026-07-01 — the most TANGLED: two large errors pointing OPPOSITE ways that nearly
cancelled, so the model reported a plausible-but-wrong NAV. `total_debt` $789.1M DOUBLE-COUNTED the $200M
2030 notes [→$589.1M, +$200M]; the $395M held-for-sale line double-counted 6 operating-manifest MRs AND
listed the wrong hulls [→ real March 8-vessel agreement $305M, fleet MR 41→35 / on-curve 87→81, −$280M];
plus opWC $207.8M→$163.3M [omitted accrued] and NB advances $90M[est]→$69.069M. NAV $83.87→$80.97 base /
$80.35→$77.47 headline, BUY→HOLD; leaves `NAV_FIGURE_ESTIMATE_QUEUE`, stays PROVISIONAL·off-curve. FLAGGED
separately: the 10-vessel NB [incl. 2 VLCC — first crude exposure] off-curve carries a −$504M commitment
drag; §9.6 on-curve wiring would add ~+$481M NAV [~+$9.6/sh] — a cross-sector methodology decision, deferred),
and **TRMD reconciled** (2026-07-02 — the estimate-heaviest name [six `[ESTIMATE]` figures] and the FIRST of
the arc to move NAV materially UP. Two errors SUPPRESSED NAV: `newbuild_capex_commitments` $360M→$31.2M [the
$360M bundled 6 MR resales bought AFTER quarter-end — the ASC/HAFN subsequent-event pattern a THIRD time; only
the 2 Q1 resales remain], and `working_capital_net` $110M[est]→$254.9M [sourced: $249.6M trade rec + $82.5M
bunker inv]. Plus debt $1,089.6M→$1,081.8M, leases $5M→$0 [SLB bought out], advances $50M→$0 on-curve. All
6-K-verified by an 8-agent workflow. Owner forks [all completeness]: WC operating $254.9M; the 2 MR resales
wired ON-CURVE §9.6 [in-sector, clean — leaves `OFF_CONVENTION_QUEUE`]; scrubbers corrected to the disclosed
85 [FY2025 20-F — leaves `OPERATING_SCRUBBER_QUEUE`, `{TRMD:85}`]. NAV $26.74→$31.65 base / $25.43→$30.34
headline, HOLD→BUY +17-22%; k_broker 1.17→1.03 [TIGHTEST spread in the book; headline ≈ TORM's own NAV $29.7].
→ GOVERNED-WIDE·basis-pending [product nav_basis pending-sourceable, not TIGHT]. **This CLEARS the P0 queue.**).
CLAUDE.md was also restructured to a lean ~3.8k-token router with a build-enforced size cap. These
hardened **provenance + handoff + hygiene**, not the thesis — SB stays cheap on every version of its numbers.

**THE consolidated handoff output is `outputs/book_scorecard.md`** (2026-06-30). One file,
two sections: a **Verdict** table on top (per name: confidence tier · FV vs current price ·
upside · position · NAV/sh · broker NAV · gap · SANITY · handoff-ready) and the **Validation
matrix** (per-gate detail) below. This is the single surface a downstream sizing decision
reads — it replaces hand-joining three sources (scorecard / reconcile / decision logs). The
Verdict's price/NAV/position come from the **scenario whole-company spine** (so hybrids INSW
/ CMBT show the whole, not a sleeve — regression-tested); the single-point FV from the
CompanyReport. Generated by the pipeline (`run_scorecard_xref` with the in-scope reports).

Three owner-directed label corrections make the verdict un-misreadable (verified per name +
adversarially, registered in `provenance.py`): (1) a **cycle-rich position is relabeled** away
from "TRIM/SHORT" to "rich · cycle position (not a short)" — a NAV-relative §12 read is not a
trade signal (crude AND product near peak; MPCC → "unreliable read"); **all 8 of the book's
TRIM/SHORT positions are cycle/unreliable/void — not one is a name-specific short**; (2) the
tier cell carries a **sub-reason = resolution path** (`structural-class` / `newbuild-heavy` /
`pending-anchor` / `mixed` / `read-flips` / `void` / `uncited-figure` / `off-curve`) so
GOVERNED-WIDE / PROVISIONAL aren't junk drawers; (3) NAT's derived NAV + gap WERE voided (they
rested on the contradicted $17M-advance figure) — **NAT was DE-VOIDED 2026-06-30** by the P0
reconciliation (advance sourced to $0, whole balance sheet re-sourced); the void-rendering path is
retained as coverage for the next contradicted-figure name (`NAV_DERIVED_VOID` now empty). The verdict header states the **opportunity-set finding**:
of 22 names the validated-actionable-long surface is **2 (SB, SBLK)** — the tool refusing to
manufacture conviction, not a gap.

The xfail-strict guard queues ARE the visible work queue — `provenance.py` is their single
source of truth (imported by both the guards and the tier, so they can't drift):
1. **§9.6 newbuild on-curve convention** (`test_newbuild_convention`) — newbuilds valued at
   delivered-market PV − remaining commitment, advances→0. SB/SBLK/DHT/CAPT are on-curve;
   `OFF_CONVENTION_QUEUE` (CMBT/STNG/TEN — 3; NAT parked, ASC+HAFN April-2026 subsequent-event NBs,
   ECO/TRMD on-curve via years_to_delivery [ECO 2 Suezmax NBs; TRMD 2 MR resales 2026-07-02]) is the
   remaining xfail-strict queue. CCEC/CMBT are STRUCTURAL (Group-B, commitment-net not on-curve).
2. **Operating-scrubber provenance gradient** (`test_scrubber_provenance`) — contradicted→hard-
   fail; untraced-newbuild→hard-fail; untraced-operating→xfail-strict. `OPERATING_SCRUBBER_VERIFIED
   = {CAPT:5, SB:20, ECO:16, TRMD:85}` (TRMD → FY2025 20-F "installed scrubbers on 85 of our vessels"
   = all 22 LR2 + all 63 MR, 2026-07-02); `OPERATING_SCRUBBER_QUEUE` = 8 names.
3. **NAV-figure provenance** (`test_manifest_provenance`) — field-GENERAL: any figure in the NAV
   equation (debt/cash/leases/commitment/advances/preferred/shuttle/working-capital) that rests
   on an estimate marker (a tilde, `[ESTIMATE]`, `approx`) without a citation is a red. Plus the
   claims half: a `(confirmed)`/`verified` assertion must cite a source. `NAV_FIGURE_ESTIMATE_QUEUE`
   = brut/cmbt/flng/hafn/ten (5; nat/asc/stng left; **trmd left 2026-07-02 — all six [ESTIMATE] figures
   sourced to the Q1-2026 6-K, workflow-verified). The P0 reconciliation queue [figure-queue ∩ PROVISIONAL]
   is now CLEARED**: brut + hafn were reconciled but stay in the figure-queue via a DELIBERATE conservative
   `[ESTIMATE]` floor (brut cash-pending, hafn pool-gross-up); cmbt/flng/ten are structural/not-yet-worked.
   "Present but uncited" fails like "absent".

**Confidence tier (governance handoff, `provenance.confidence_tier`)** — read from the existing
validation state, NOT a new model: **VALIDATED-TIGHT** (6: DHT, FRO, SB, SBLK, TNK, **ECO** — traced +
robust two-basis; ECO cleared 2026-07-01 via the §9.6 on-curve fix + scrubber verification, but is
validated-but-RICH [rich · cycle position], NOT a new long), **GOVERNED-WIDE** (13 — traces but
structural-unavailable input, read flips, or newbuild parked/absent: **NAT** `newbuild-indeterminate`;
**ASC** `structural-class`; **TRMD** `basis-pending` — cleared 2026-07-02, all figures sourced + all 3 queues
cleared, but product nav_basis is `pending-sourceable` [product resale-curve marks deferred, thread P1c], so
GOVERNED-WIDE not TIGHT; BUY +17%, k_broker 1.03 — the tightest tool↔broker spread in the book), **PROVISIONAL**
(3: **STNG** `off-curve` — all figures now sourced to the Q1-2026 6-K [2026-07-01 rebuild], but the 10-vessel
NB stays off the §9.6 curve; + **BRUT** `cash-pending` — 4/5 issuer-traced, cash flagged pending the H1-2026
report; + **HAFN** `pool-gross-up-pending` — all figures sourced/decided except operating WC, held at a
conservative floor because pool custodial receivables can't be netted from the filing; **NOT handoff-ready,
flag don't pass**). APPROX-pnav does NOT demote a robust name
(SB's two-basis corroboration substitutes for the missing broker check); an immaterial uncited
operating-scrubber surface does not either (materiality-gated at 10% of NAV). Emitted in the
scorecard Verdict + the `/add-ticker` handoff (a PROVISIONAL name may not hand off a governed FV).

**A NEW AGENT: read CLAUDE.md, then this file.** The lead open thread is the **reconciliation
queue** (below) — clearing PROVISIONAL names to handoff-ready. **CLEARED 2026-07-02: all EIGHT done
(NAT+SB+ASC+BRUT+ECO+HAFN+STNG+TRMD).** Next work is the remaining `OFF_CONVENTION_QUEUE` (CMBT/STNG-NB/TEN)
+ the P1 product-basis thread (P1c). Per-change chronology in `CHANGELOG.md`; per-name detail in `decisions/<t>_log.md`.

## Recent arc — convention + provenance + handoff + hygiene (2026-06-29 → 07-01)

- **§9.6 newbuild convention standardized** (SB/SBLK first, then DHT/CAPT) — newbuilds were
  inconsistently valued book-wide; the 3-clause guard + per-name pre-registered sourcing put the
  worked names on-curve and made the rest a visible xfail-strict queue.
- **Provenance turned from attention-dependent to ENFORCED.** Four catches (xclusiv resale mislabel
  → crude age-0 → DHT scrubber `(confirmed)` → NAT newbuild figure the cash flow contradicts) →
  the field-GENERAL guard: any NAV-moving manifest field must trace to a citation; a tilde/`[ESTIMATE]`
  is a red. Two more instances landed on the SB audit (below), both now guarded.
- **NAT reconciled + DE-VOIDED** (2026-06-30) — advance $17M→$0 (contradicted), newbuild parked at
  $0 (undisclosed price), fleet 18→16 + a `held_for_sale` field; NAV $2.07→$2.79,
  GOVERNED-WIDE·newbuild-indeterminate. (Was HALTED-as-VOID; the reconciliation cleared it.)
- **SB corrected** (2026-07-01) — an audit of the headline actionable name found a date-mix (the
  manifest was the June-12 fleet on the 3/31 balance sheet: Katerina double-counted, Michalis H the
  one HFS, Xenia/Ped.Commander mis-bucketed) AND the CAPT blanket-scrubber bug (29 flagged vs 20
  disclosed). NAV $10.47→$10.12 (still ~0.63×); scrubber set traced to the 20-F → cleared to
  OPERATING_SCRUBBER_VERIFIED. Two new CLAUDE.md rules + the post-mortem in CHANGELOG.
- **CLAUDE.md restructured to a lean router** (2026-07-01, 357→189 lines / ~6.2k→~3.8k tokens) —
  gotchas compressed to one-liners, runbook/fetch-mechanics/week-close migrated to WORKFLOWS.md;
  the compounding-knowledge habit made self-limiting with a build-enforced size cap
  (`tests/test_docs_stay_lean.py`). Verified lossless by an independent audit.
- **Confidence tier + consolidated Verdict output** — the handoff surface above.

## Open threads (prioritized — start here)

**P0 — reconciliation queue: clear PROVISIONAL → handoff-ready (owner-directed, START HERE).**
The PROVISIONAL names each carry a NAV-driving figure that is uncited or off the §9.6 curve;
each clears ONLY by sourcing the figure to a citation in a **full balance-sheet reconciliation**
(newbuild commitment + debt + cash + working capital), NOT a single-figure plug. Discipline:
pre-register the predicted bands AHEAD, commit, then recompute; halt on a miss and investigate
the INPUT; never source mid-recompute.
   - **NAT — DONE (2026-06-30).** Full reconciliation vs the FY2025 20-F (acc 0001140361-26-017809)
     + Q1-2026 6-K (acc 0000919574-26-003779): advance $17M→$0 (contradicted); commitment PARKED at
     $0 (firm price undisclosed by NAT — only a Pareto LOI; §9.6 on-curve unauthorized); operating
     fleet 18→16 + a new `held_for_sale` field ($65M contracted). NAV $2.07→$2.79, de-voided,
     GOVERNED-WIDE·newbuild-indeterminate. Reusable pattern: `held_for_sale` model field +
     `NEWBUILD_PRICE_PENDING` (park-at-$0-pending-filed-price → GOVERNED-WIDE not TIGHT). Record:
     `decisions/nat_reconciliation_prereg_2026-06-30.md` (commits df2c616 pre-reg, b44c3c4 fix).
   - **ASC — DONE (2026-07-01).** Full reconciliation vs the Q1-2026 6-K (acc 0001104659-26-056715),
     FY2025 20-F (acc 0001104659-26-024690), 2013 order 6-K (acc 0000919574-13-005339): the 2×40,500 DWT
     Handysize newbuild EXCLUDED from Q1 (signed **April-2026** = subsequent event; was a −$88.8M
     commitment-only drag + §9.6 violation); phantom `Ardmore_Patriot` removed (0 mentions in 6-K/20-F);
     4 chem-Handies re-marked to a cited **20-F carrying-value floor** (~$18.3M/hull); HFS Engineer →
     `held_for_sale` field ($35.5M). NAV $15.96→$17.80, PROVISIONAL → GOVERNED-WIDE·structural-class,
     BUY +5.2% but §12 cycle-position. Newbuild to go on-curve in Q2 (§9.6, issuer $44.9M/ship). Record:
     `decisions/asc_reconciliation_prereg_2026-07-01.md` (commits 48b3956 recon, cfc904e re-ratify).
     LESSON (owner): **audit the subsequent-events note FIRST** — it's where post-quarter events leak
     into a Q1 snapshot (ASC's newbuild; the SB fleet-table version).
   - **BRUT — DONE (2026-07-01), a DIFFERENT outcome: the reconciliation VALIDATES the model, and BRUT
     stays PROVISIONAL (does NOT clear).** Workflow-sourced (9 agents) to the FY2025 Annual Report
     (`inputs/research_issuer/2025_brut_annual_report.pdf`) + the Euronext admission doc. The Pareto
     estimates were ACCURATE: commitment $1,373.1M (Note 10 $661.7M + Note 15 Jan $236.0M + CIMC $499.0M
     − $23.6M) ≈ prior $1,370M; debt $0; shares 61,923,808 — 4 figures now TRACE to the issuer. Cash
     booked at the **$66M conservative FLOOR** (owner: not the $116M point, not Pareto's $100M; the
     Mar-2026 CIMC ~$50M execution deposit likely hit Q1) → NAV $9.40→$8.80. **Cash keeps BRUT
     PROVISIONAL** — new sub-reason **`cash-pending-H1-report`** (a WAITING state, resolves at H1-2026
     2026-08-13; re-ratify AGAIN then). Also fixed a **FABRICATED governance** block (no Goodwood/Koch;
     managers 2020 Bulkers+Himalaya, Trøim-sponsored, Magni zero-fee) + recorded the **going-concern
     doubt** as the §15/risk headline. NOT actionable (going-concern-doubtful, max-torque, resale-level-
     provisional). Record: `decisions/brut_reconciliation_prereg_2026-07-01.md`. Baseline re-ratify
     (BRUT-only) pending — owner. **NEW PATTERN: a reconciliation can VALIDATE + still not clear** (sourced
     except one figure with a known resolution date → `cash-pending`, distinct from `void`/`uncited`).
   - **ECO — DONE (2026-07-01), → VALIDATED-TIGHT (first TIGHT of the arc), the CLEANEST (no forks).**
     ECO (Okeanis) was PROVISIONAL only on `OFF_CONVENTION` (2 Suezmax NBs at delivered market with no
     `years_to_delivery`). ALL figures verified vs the Q1-2026 6-K (acc 0001104659-26-060273): debt $683.1M
     (incl. SLB), cash $176.5M, advances $39.74M → commitment $158.86M, NBs $99.3M each (Tigani May-26, Vous
     Jul-26), shares 39,044,655, 8 VLCC + 8 Suezmax (no phantoms). FIX: split the NB row + set years_to_delivery
     (0.12 / 0.29) → on-curve, leaves `OFF_CONVENTION_QUEUE`; verified 16 on-water scrubbers → leaves
     `OPERATING_SCRUBBER_QUEUE` (`{ECO:16}`). PROVENANCE CATCH: the value-flag guard blocked defaulting
     scrubber=true on the NBs (6-Ks' scrubber statements are existing-fleet-scoped — the SB trap), so the NBs are
     booked **scrubber=false** (conservative, `newbuild_specs.yaml`). NAV $34.56→$34.35 (−0.6%, sub-threshold —
     gate stable, no re-ratify needed). Record: `decisions/eco_reconciliation_prereg_2026-07-01.md`. **ECO is
     validated-but-RICH (rich · cycle position, ~1.39× NAV) — NOT a new actionable long.**
   - **HAFN — DONE (2026-07-01), the MOST consequential (multiple errors + genuine forks); stays PROVISIONAL.**
     Workflow-sourced (12 agents) + independent read vs the Q1-2026 6-K (acc 0001140361-26-022910). Recurring
     theme: **balance-sheet-literal ≠ NAV-economic**, three times. (1) The 8 MR HHI newbuild EXCLUDED from Q1 —
     signed **3-Apr-2026** (Note 7 subsequent event) → the −$405M commitment + $40M phantom advance was the ASC
     double-anachronism (+$365M; HAFN leaves `OFF_CONVENTION_QUEUE`). (2) `total_debt` $943.5M→$953.9M (Note 2/4
     bank borrowings) + `lease_liabilities` $35.9M→$71.6M (model dropped the $35.7M SLB) (−$46M). (3) TORM 13.97%
     stake → **$277.2M lower-of-cost** (Hafnia's OWN NAV method, comparability to its $8.09 NAV — NOT $395M market;
     **precedent: a marketable stake in NAV takes the issuer's disclosed method, not fair value**). (4) operating
     WC — the gross balance-sheet $335.9M carries **pool custodial gross-up** (Hafnia runs the world's largest
     product pool; the $670M receivables aren't NAV-economic); booked at a conservative **$85.7M floor** →
     `pool-gross-up-pending` (**precedent: pool receivables are custodial, not NAV-economic**). (5) shares → 505.3M.
     NAV $5.22→$5.57 headline; SANITY OK. Incidental daily price-refresh (5 names, EV-only) REVERTED to isolate the
     commit. HAFN stays PROVISIONAL·pool-gross-up-pending, rich · cycle position — NOT actionable. Record:
     `decisions/hafn_reconciliation_prereg_2026-07-01.md`. Baseline re-ratify (HAFN-only) pending — owner.
   - **STNG — DONE (2026-07-01), the MOST TANGLED (two large offsetting errors); leaves the figure queue,
     stays PROVISIONAL·off-curve.** Owner-directed FULL per-vessel rebuild vs the Q1-2026 6-K (acc
     0001483934-26-000042). Two errors pointing OPPOSITE ways nearly cancelled, so a half-fix would report a
     wildly wrong intermediate: (1) `total_debt` $789.1M **double-counted the $200M 2030 notes** — STNG's own
     "Gross debt outstanding 3/31 $589,056K" (bank $389.1M + notes $200M; ties to net cash $395.3M) → $589.1M
     (+$200M). (2) The $395M held-for-sale line **double-counted 6 operating-manifest MRs AND listed wrong hulls**
     (it counted operating LR2s Broadway/Condotti/Winnie/Lauren + the Q1-CLOSED STI Lavender); the real 3/31 HFS
     is the March 8-vessel agreement **$305M** (Solidarity LR2 + 7 MRs; $215M carrying). Removed the 6 double-counted
     MRs from the fleet (**MR 41→35, on-curve 87→81**) + re-booked HFS via a new `held_for_sale` field (−$280M net).
     Also: opWC $207.8M→**$163.3M** (omitted $44.6M accrued), NB advances $90M[est]→**$69.069M** (BS "Vessels under
     construction"), cash $984.321M, shares 50,025,865, leases 0 — all 6-K-verified. **NAV $83.87→$80.97 base /
     $80.35→$77.47 headline, BUY→HOLD** (in the pre-reg band); SANITY OK (−28.3% to broker $108, documented spread).
     STNG **leaves `NAV_FIGURE_ESTIMATE_QUEUE`** (advances sourced) but **stays `OFF_CONVENTION_QUEUE` →
     PROVISIONAL·off-curve**. Record: `decisions/stng_reconciliation_prereg_2026-07-01.md`.
     **§9.6 NEWBUILD — DEFERRED as its own pre-registered step (owner decision 2026-07-01), NOT wired with the
     rebuild.** The 10-vessel NB (2 MR + 4 LR2 + **2 VLCC**) off-curve is a −$504M commitment drag; full on-curve
     wiring would add **~+$481M NAV (~+$9.6/sh → base ~$90.6)** and flip the read toward BUY. Deferred because it is
     a reconciliation-sized methodology move, not a flag-flip, and it must NOT be bundled with a data correction
     (attributable-step discipline) or import unresolved crude-level uncertainty onto a product name:
       · **The 2 VLCC portion is BLOCKED on thread (d)** — STNG's VLCCs would mark on the CRUDE age-0 curve, whose
         RESALE-basis level is itself provisional (thread (d), `curve.newbuild` basis inconsistency). Wiring them now
         imports that quarantined crude-level uncertainty onto STNG's clean product NAV. **Thread (d) now gates the
         VLCC portion of STNG too — not just the crude names / BRUT.**
       · **Likely future structure (pre-register separately):** wire the **6 product hulls (2 MR + 4 LR2) on-curve**
         (within-sector, settled product curve; ~+$7/sh) and **park the 2 VLCCs off-curve pending thread (d)**.
         Source per-hull delivered marks + the delivery schedule, predict bands AHEAD, gate the move as its OWN
         attributable re-ratify (a +$7–9.6/sh headline move cannot be a footnote).
       · **Classification:** even fully wired at ~$90.6 (a deep nominal BUY vs price $75.60), the cheapness would rest
         partly on the provisional VLCC resale mark → **GOVERNED-WIDE at best, not TIGHT**. So the §9.6 wiring does
         NOT manufacture a clean tight long either — same arc finding. Baseline re-ratify (STNG-only) pending — owner.
   - **TRMD — DONE (2026-07-02), the estimate-heaviest name + the FIRST of the arc to move NAV materially UP;
     leaves ALL THREE queues → GOVERNED-WIDE·basis-pending, handoff-ready BUY.** Full balance-sheet sourcing to
     the Q1-2026 6-K (acc 0000919574-26-003082), independently confirmed by an 8-agent verification workflow (5
     extractors + 3 adversarial verifiers, all verdicts agree). Two errors SUPPRESSED NAV: (1)
     `newbuild_capex_commitments` $360M→**$31.2M** (Note 10 "Second-hand vessels commitments") — the $360M bundled
     the **6 MR resales bought "after the end of the quarter"** (subsequent event, the ASC/HAFN pattern a THIRD
     time); only the 2 Q1-agreed resales (Dehradun/Dapitan) remain. (2) `working_capital_net` $110M[est]→**$254.9M**
     (sourced: $249.6M trade rec + $82.5M bunker inv at a record-rate quarter-end). Also debt $1,089.6M→$1,081.8M,
     leases $5M→$0 (SLB bought out — the $10M ROU is inside borrowings), advances $50M→$0 (on-curve). **Owner forks
     (all completeness, 2026-07-02):** WC operating $254.9M; the **2 MR resales wired ON-CURVE §9.6** (age-11 MRs,
     years_to_delivery 0.12 — in-sector, near-immediate, no cross-sector blocker unlike STNG → leaves
     `OFF_CONVENTION_QUEUE`); scrubbers corrected to the disclosed **85** (FY2025 20-F "installed scrubbers on 85 of
     our vessels" = all 22 LR2 + all 63 MR → leaves `OPERATING_SCRUBBER_QUEUE`, `{TRMD:85}`; the 2 resale hulls
     scrubber=FALSE, no NB statement). NAV $26.74→**$31.65** base / $25.43→**$30.34** headline (in the pre-reg band);
     HOLD→**BUY** +17-22%; **k_broker 1.17→1.03** — the TIGHTEST tool↔broker spread in the book (headline ≈ TORM's
     OWN disclosed NAV $29.7 — a triple corroboration). → **GOVERNED-WIDE·basis-pending** (NOT TIGHT: product
     nav_basis `pending-sourceable`, thread P1c — a book-wide product limitation, not TRMD-specific). Record:
     `decisions/trmd_reconciliation_prereg_2026-07-01.md`. Baseline re-ratify (TRMD-only) pending — owner.
   - **P0 RECONCILIATION QUEUE CLEARED (2026-07-02)** — all 8 `NAV_FIGURE_ESTIMATE_QUEUE ∩ PROVISIONAL` names
     done. Remaining reconciliation-style work: the `OFF_CONVENTION_QUEUE` fixable names (CMBT / STNG's own NB
     [gated on thread (d) for the VLCC portion] / TEN) onto the §9.6 curve, and the **P1 product-basis thread
     (P1c)** — sourcing the product LR1/Handysize/Handymax `newbuild_contract` marks would move the product names
     (TRMD/ASC/STNG) from `basis-pending`/`pending-sourceable` toward `resale-uniform` and unlock VALIDATED-TIGHT.

**P1 normal-rate / justified-leg follow-ons** (the §18 layer is diagnostic-only; these
harden it and the OTHER names — none affect the durable SB-cheap finding, which rests on the
§5b-independent historical floor 0.733). All data-gated routes were pre-registered to defer:

   a. **§18.5b orderbook validation** — the parity "under-ordered" signal (dry-bulk −24%) is
      PROVISIONAL until validated against an INDEPENDENTLY observed orderbook-to-fleet ratio
      per sector (run per sector, crude included). Until then the parity column is a hypothesis
      with a test attached, not a result. This is what makes parity trustworthy or rejects it.
   b. **§18.5a Baltic mean-reversion data** — the historical_mean basis is v1 = current
      `historical_tce_means` (unvalidated); upgrade to a true $/day realized mean (BCI 5TC /
      BPI 4TC / BSI 10TC / New ConTex) and run the registered ≥70%-of-≥12q mean-reversion gate.
   c. **Product LR1 / Handysize / Handymax `newbuild_contract` marks** — DEFERRED (not sourced
      mid-recompute, on purpose). Source dated broker contract marks, predict per-class bands,
      register AHEAD of computing (same discipline as the 8 done classes); then product/hybrid
      parity computes (now reads "pending"). LNG/container stay unvalidated (boom + resale-inflated).
   d. **NAV-layer thread — `curve.newbuild` basis inconsistency** (substantive, NOT cosmetic):
      the age-0 NAV mark means CONTRACT for dry-bulk/MR (Cape $74M≈contract) but RESALE for
      crude (VLCC $175M, plausibly stale-high even as resale), so cross-sector NAV comparisons
      inherit the inconsistency — upstream of crude P/NAV on both bases. Separate P2-style NAV
      curve-refresh (would move headline crude NAV → delta-review + re-ratify). See §18 close.
      **NEW gate (2026-07-01): this thread now also gates the VLCC portion of STNG's §9.6 newbuild
      wiring** — STNG's 2 VLCC NBs can't go on-curve until the crude age-0 RESALE level is resolved
      (else STNG's product NAV inherits the provisional crude mark). Wire STNG's 6 product hulls
      first; park the 2 VLCCs here. (Same open item that most moves BRUT + the crude names.)
   e. **P3 presentation guards** (no number changes): suppress the non-composable LNG/container
      medians from the headline vector; "rich-near-peak" caveat on crude; §15 governance dual-read
      for TEN/CMDB (clean-NAV-justified ≠ haircut basis). Lowest-stakes; timebox.

Older dry-bulk refinement threads (now DONE by P2): Post-Panamax sub-class split + SB charter
rates — landed this push-block; removed from this list.
2. **CMBT open items** (in `cmbt_log.md`): verify FSO owned-vs-JV (zero `shuttle_contracted_book`
   if the FSOs are inside the equity-JV line); apply the §9.4 yard-quality discount to the
   China-heavy dry-bulk book (v1 is the "without discount" leg); confirm the NMax newbuild
   level vs a current NB quote; G&A/interest are Q1-annualised estimates; chemical/Windcat
   segment books are Dec-2025 vintage; `consensus_fwd_pe` APPROX (Q1 EPS one-off-gain-distorted).
3. **SB open items** (in `sb_log.md`): refresh `consensus_pnav` if a VIE SB NAV is obtained
   (currently P/BV common-book proxy); confirm the finance-lease current/non-current split,
   the exact €950/day + €5.0M mgmt-fee figures, and the buyback authorization from the raw 20-F.
4. **GNK/Diana tender** — the $24.80/sh cash-tender deadline was 2026-06-26 (now PAST). Verify
   the scheduled `gnk-diana-tender-jun26-check` fired and the outcome (deal vs lapse → revert to
   NAV-discount) is captured in `gnk_log.md`; re-frame GNK if not.

## Standing operational threads (carry forward)

### Q2-refresh carry-forwards (earnings calendar + preflight §0 drive timing)
- **Early cluster Jul-28 → Aug-6:** STNG/ASC/TNK/CCEC, then ECO/GNK/GSL/CMDB/DHT/INSW/SBLK.
  Now also **CMBT** (ex-Euronav reports ~mid-Aug; H1 basis) and **SB** (early-Aug 6-K) join the
  dry-bulk refresh cycle.
- **BRUT (H1, Aug-13):** first issuer report vs the Pareto-estimate balance sheet; §15 screen.
- **CAPT (Q2):** verify the Jun-16 sponsor VLCC deal terms (§15 tripwire).
- **MPCC (Aug-26):** issuer fleet list → built years + NB delivery quarters; sale prints.
- **GSL (Aug-4/6):** Series B prefs post-ATM; the Jun-26 $917M NB order (apply §9.6).
- **TEN (Sep, H1):** TCM fee-load (§15 anchor); ten_log Q2 kit deltas. **CMDB:** Astros sale.

### Standing threads
- **Daily price-refresh re-ratify pending (deferred 2026-06-30).** The 2026-06-30 close refresh
  moved 9 names' EV vs the baseline (ΔNAV 0% — pure price), incl. two price-driven BAND FLIPS
  (DHT TRIM/SHORT→HOLD +3.8pp, FLNG HOLD→BUY +4.6pp). It was kept OUT of the NAT reconciliation
  commit (owner: don't launder market drift through a sourcing commit) and reverted from the tree
  to isolate NAT. Handle as its OWN deliberate re-ratify on the next refresh: accept the 7 pure-EV
  drifts as routine, but **eyeball whether the DHT/FLNG flips are trivial boundary-crossings or real
  position signals before absorbing them** — don't batch-accept a band flip.
- **FFA feed DORMANT since 2026-06-12** (source-side — the single poster stopped). Only the
  ffa_vs_strip diagnostic is stale; no live valuation input affected. Action is upstream.
- **Weekly /news-pull** — resume the Saturday cadence.
- **OWNER ACTION pending:** ratify-or-revise the A1 horizon (10 strip quarters = end-2028).
- **MB weeklies:** container current-rate refresh (owner-gated); Pana anchor flagged
  structurally low; LNG weekly not yet delivered.
- **Hormuz weight-revisit trigger** — standing (trigger NOT met).
- **Deferred by owner:** /news-pull agent-half orchestration; Task-3 weight adjuster;
  demand-destruction overlay; FFA Stage 2.

### Methodology-soundness remediation — Tier-4 backlog (manage/document; owner judgment)
Per `outputs/METHODOLOGY_AUDIT_2026-06-22.md` §A–G: cycle step-band vs logistic (C-1);
cross-sector anchor commensurability (C-2); marks statistical thinness / age-5 extrapolation
(B-1/B-2); k_broker band vs live (B-3); the 11% rate calibration (B-4); §15 haircut derivation
rule (E-1); data staleness (frozen container feed + APPROX names, F). Phase 2 drift gate is
DONE; **standing care: at each quarterly refresh expect the gate to flag legitimate moves —
annotate the material ones, then `./scripts/ratify_baseline.sh "<Qx refresh>"` to re-anchor.**

## Backtest (reference, not a gate)
`backtest/REPORT.md`: no statistically demonstrated cross-sectional edge. Test 1 (engine EV%,
Nq 23, IC −0.020, INCONCLUSIVE) and the powered P/B-proxy tests (Amendment-2 N=31 / Amendment-3
N=72, both exclude a moderate within-sector value premium on a book proxy) do NOT gate
development. **Test 2** (time-series reversion to fair value, in-sample IC +0.234, p 0.018) is a
HYPOTHESIS — pre-registered out-of-sample/multi-cycle confirmation runs at +8q (~end-2028) or on
a paid feed. Net: not a name-ranker (Test 1 null), plausibly a cycle/value timer (Test 2), unproven.

## Verification gate (run before any handoff / Week-close)
- `PYTHONPATH=src .venv/bin/python -m pytest -q` — main suite, **440 passed / 25 xfailed** at
  2026-07-01 (includes the Phase 2 drift gate, which can legitimately go red on accepted drift —
  annotate + re-ratify; and the xfail-strict provenance queues — an xfail CLEARING is the work).
- `PYTHONPATH=. .venv/bin/python -m pytest backtest/ -q` — backtest (**13**; separate).
- (optional) `cd shipping_harvester && PYTHONPATH=. ../.venv310/bin/python -m pytest -q` — **57**.
- `python -m crude_tanker_fv.pipeline 2026-Q1` runs clean.
- `python -m crude_tanker_fv.reconcile --all` — SANITY all OK/n-a-APPROX; annotate >2pp drift.
- Clean git state; push `origin main`. `.venv310/`, `shipping_harvester/data/`,
  `backtest/vintages/*/` are gitignored by design. NOTE: every pipeline run auto-prepends a
  model-state entry to ALL `decisions/<t>_log.md` and regenerates `outputs/*` — commit that
  churn deliberately (it is expected, mostly "+0.0pp no material moves").
