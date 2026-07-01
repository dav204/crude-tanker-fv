# ECO — §9.6 on-curve fix + operating-scrubber verification, PRE-REGISTRATION (2026-07-01)

Fifth P0 reconciliation, and the CLEANEST — no forks. ECO (Okeanis Eco Tankers) was PROVISIONAL for
ONE reason: `OFF_CONVENTION_QUEUE` (its 2 Suezmax newbuilds sit in the manifest at delivered market but
with NO `years_to_delivery`, so they classify "commitment-net" not "on-curve"). Its figures are already
issuer-cited (NOT in `NAV_FIGURE_ESTIMATE_QUEUE`), so the §9.6 on-curve fix is authorized (CLAUDE.md).

## Verification (all figures confirmed vs the Q1-2026 6-K, this session)
Source: Okeanis Q1-2026 6-K, EDGAR acc `0001104659-26-060273`, Exhibit 99.1 (`tm2613201d1_ex99-1.htm`,
"Reports Financial Results for the First Quarter of 2026", as-of 2026-03-31). Every ECO balance-sheet
figure CONFIRMED:
- Total debt **$683.1M** (incl. sale-leasebacks, no separate lease line) ✓ | Total cash **$176.5M** ✓
- Advances for acquisition of vessels **$39,737,420** ✓ (→ remaining commitment $198.6M − $39.74M = $158.86M ✓)
- 2 Suezmax newbuilds (Tigani, Vous), **$99.3M each**, MOA Jan-2026, delivery **May & July 2026** ✓ (L266/L303)
- Shares 39,044,655 (35,433,544 + Jan-2026 offering 3,611,111) ✓ | inventories/receivables ✓
- Fleet **8 VLCC + 8 Suezmax** on-water (avg age 5.8y) + 2 NB, "all scrubber-fitted" (L76) ✓ — no phantoms.
- The $90M newbuild financing facility (L293) was signed **April 30, 2026** — a subsequent event, correctly
  NOT in the 3/31 sheet (no debt draw pre-delivery).

## The fix (mechanical, no judgment)
1. **§9.6 on-curve:** split the `SMX_nb` row into **Tigani (`years_to_delivery: 0.12`, May-2026)** and
   **Vous (`years_to_delivery: 0.29`, Jul-2026)** — from the 3/31 snapshot. This PV-discounts their delivered
   value (`1.11^−yr`) instead of crediting full delivered value today → ECO leaves `OFF_CONVENTION_QUEUE`.
2. **Operating-scrubber verification:** the issuer states ALL 16 on-water vessels are scrubber-fitted (L76).
   After the §9.6 fix (the 2 NB drop out of "operating"), the operating scrubber count = **16**. Move ECO
   `OPERATING_SCRUBBER_QUEUE` → `OPERATING_SCRUBBER_VERIFIED = {…, "ECO": 16}` (cited to the Q1-2026 6-K).
   (No CAPT peer-borrow risk: "all scrubber-fitted" IS the per-vessel truth.)

## PRE-REGISTERED PREDICTION (committed ahead of the pipeline recompute)
- **Headline (txn-anchored) NAV $34.56 → band $34.35 – $34.56** (a small decrease — the §9.6 PV discount on
  2 newbuilds delivering in ~2–4 months is ~$4–5M of a ~$2.1bn fleet; base-curve delta was −$0.13/sh).
- **Tier PROVISIONAL → VALIDATED-TIGHT** (traced resale-uniform + robust two-basis; op-scrubber surface
  immaterial at 2.2%, now also verified). ECO leaves `OFF_CONVENTION_QUEUE` + `OPERATING_SCRUBBER_QUEUE`.
  **First VALIDATED-TIGHT of the reconciliation arc.**
- **Position stays rich · cycle position (not a short)** — ECO trades RICH (price $47.70 ≈ 1.21× broker NAV;
  ~1.38× tool NAV). VALIDATED-TIGHT means the NAV is SOLID, not that ECO is cheap — it is a validated-but-RICH
  name, NOT a new actionable long. The tight-actionable-LONG surface stays SB + SBLK.
- Guards: ECO leaves both queues (provenance.py + test copies synced); `test_verified_operating_scrubber_count`
  asserts ECO:16; `test_newbuild_convention` ECO now "on-curve"; suite stays green; drift gate expects a
  small annotated ECO NAV move → re-ratify.

## HALT criteria
- Recomputed headline NAV outside **$34.35 – $34.56** → halt, investigate the input.
- ECO tier not VALIDATED-TIGHT, or SANITY not OK → halt.
- Any guard red that isn't the expected ECO queue-clearances → halt.
