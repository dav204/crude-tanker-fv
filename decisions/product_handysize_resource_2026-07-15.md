# Product-Handysize age-0 re-source — the Thread-1A bulk-row contamination corrected

**Date:** 2026-07-15 · **Owner ruling:** "Execute" (option 1 as walked through — the
ASC-contract-anchored exception) · **Window:** executed BEFORE the ASC Q2 refresh
(Jul-28/29) so the correction is a ZERO-live-impact re-anchor, not a mid-refresh reprice.

## The finding being corrected (prereg §0.2, handy_curve_sourcing_prereg_2026-07-14.md)

Thread-1A wired the PRODUCT-tanker Handysize age-0 $40M → $36M citing "xclusiv Resale
2026-06-22 — label-checked." The label check verified the RESALE row but not the SECTION:
the harvester cache proves the xclusiv "Handysize" row is the **BULK-carrier** row (it
tabulates with Capesize/Kamsarmax/Ultramax; its TC column is BHSI gross earnings —
17,014 × 0.95 = Pacific Basin's published net print, exact; its NB $30.6M matches 2343's
actual bulk contract $29.8M). The economic tell: **ASC's actual product-Handy newbuild
contract is $44.9M/hull** — a product hull marked at $36M age-0 beside a $44.9M real
contract is wrong by inspection. The guard (`XCLUSIV_WIRED` incl. "Handysize") was
ENFORCING the contamination.

## Source landscape (exhausted before choosing the basis)

No broker publicly tabulates product-Handysize secondhand values: xclusiv's tanker
section stops at MR2 (cache-proven); the MB Tanker Weekly's tables stop at MR (zero
"Handy" occurrences in issue 28, checked 2026-07-15); the Intermodal/AST-class public
tables are MR-smallest. The ONLY real, dated product-Handy mark in evidence:

> *"In April 2026, the Company signed contracts for the construction of two 40,500 dwt
> Handysize… at $44.9 million per vessel."* — ASC Q1-2026 6-K (acc 0001104659-26-056715);
> echoed by the Pareto Shipping Daily 2026-04-30 ($44.9M/ship).

## The re-source (executed)

- **Product Handysize age-0 → $44,900,000**, basis = ISSUER NEWBUILD CONTRACT (the
  citation above). Registered as an `AGE0_BASIS` exception (the MR/LR1 pattern): no
  broker resale line exists; a April-2026 arm's-length contract is a FLOOR for prompt
  resale in this market (resale ≥ contract is the hot-market norm) — conservative in the
  right direction. `basis_status` → **pending-sourceable** (Group A: resolve toward
  resale-uniform when any broker tabulates a product-Handy resale line).
- **`prompt_resale.Handysize` → 44,900,000** (same citation; contract-floor label).
- **Clean end-state rename:** the committed xclusiv extract's `Handysize` rows (resale
  36.0 / 5yr 29.5 / 10yr 23.3 / NB 30.5) are RENAMED **`Handy-Bulk`** — the row is and
  always was the bulk row; the dry class now reads it DIRECTLY (`AGE0_BASIS[Handy-Bulk]:
  xclusiv-resale`, joins `XCLUSIV_WIRED`; the alias indirection retired). The bulk row
  can no longer be mistaken for a product mark by construction.
- Product "Handysize" leaves `XCLUSIV_WIRED`; its `AGE0_BASIS` entry becomes the dated
  exception carrying the contract citation + this doc.

## Registered bands (predicted AHEAD of the gate loop)

1. **ZERO live NAV movement on every name** — age-0 shapes only the 0-5yr leg; the
   operating product-Handy tonnage is age 11+ (ASC 37-40k Handies ~11y; HAFN 18y;
   chem-Handies on carrying-value floors); ASC's two NBs are subsequent-event-EXCLUDED
   from the Q1 snapshot. Drift gate: 0 new rows, 0 EV/NAV moves from this change.
2. **Forward consequence quantified (so the Q2 refresh isn't surprised):** at the ASC Q2
   refresh the 2 NBs enter §9.6 on-curve. At the OLD $36M age-0, delivered PV
   (≈ 36/1.11^2.4 ×2 ≈ $56M) − remaining commitment (≈ $85-90M) ≈ **−$31M inception drag**
   — the model calling a contract ASC's own filing deems "attractive" a 25% overpay. At
   the corrected $44.9M: delivered PV ≈ $70M → drag ≈ **−$17M** (the honest PV-discount
   cost of far-dated slots). Correction ≈ **+$14M ≈ +$0.34/sh ≈ +1.9% of ASC NAV** at Q2
   entry — booked THEN, attributed to this doc.
3. Tier/rollup: no tier changes (ASC already GOVERNED-WIDE·structural-class; its basis
   composite already non-uniform via the MR token). Suite green except the deliberate
   guard re-pins listed above.

**Halt rule:** any live NAV/EV movement at the gate loop → STOP, investigate (band 1
says there must be none).
