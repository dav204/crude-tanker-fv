# ASC — full balance-sheet reconciliation, PRE-REGISTRATION (2026-07-01)

Clears the P0 item: ASC was **PROVISIONAL** on two counts — an uncited estimate in the
NAV equation (`NAV_FIGURE_ESTIMATE_QUEUE`) and newbuilds off the §9.6 curve
(`OFF_CONVENTION_QUEUE`). This is the *pre-registration* — every NAV figure traced to a
primary filing, the treatment decisions (owner-directed 2026-07-01), and the **predicted NAV
band committed AHEAD of the pipeline recompute**. Per the discipline: commit this, then
recompute; **halt on a miss and investigate the INPUT**; never source mid-recompute. Sourcing
was completed BEFORE this file was written.

## Sources of record (EDGAR, CIK 0001577437, this session)
- **Q1-2026 6-K** — acc `0001104659-26-056715` (`asc-20260331x6k.htm`): interim condensed
  financials **as of 2026-03-31** + notes (fleet table, MD&A "Significant Developments",
  Note 8 Subsequent Events, cash flow).
- **FY2025 20-F** — acc `0001104659-26-024690`: depreciation policy (25-yr life, $400/LWT
  residual), the "24 of 25 vessels' market values exceeded carrying value" disclosure.
- **2013 order 6-K** — acc `0000919574-13-005339`: the four 25k Fukuoka chemical tankers'
  original contract price ($118.0M / 4 = $29.5M each).
- **2026-06-16 6-K** (acc `…074572`) — checked: annual-meeting voting only; **not** an
  Engineer-delivery filing (that will be the Q2 6-K, ~late July).
- **Pareto Shipping Daily 2026-04-30** — echoes the newbuild order ($44.9M/ship); ASC not covered
  (APPROX `consensus_pnav`).

## Sourced reconciliation (2026-03-31), each figure cited ($k unless noted)

| Field | Old (YAML) | **Sourced** | Citation |
|---|---|---|---|
| `cash_and_equivalents` | 47,200 | **47,214** | BS face |
| operating WC (in `working_capital_net`) | ~46,100 (est) | **46,584** | (CA 146,185 − cash 47,214 − HFS 22,944) − (CL 30,028 − current lease 585) |
| chem-Handy sleeve (in `working_capital_net`) | 49,400 (`~$13M×4 −5%`, UNCITED) | **73,100** | carrying-value floor (see below) |
| `held_for_sale` (NEW field) | folded in WC @ 35,500 | **35,500** | MD&A L342: "agreed sale of the 2014-built Ardmore Engineer for $35.5M… delivered June 2026… classified as held for sale effective March 31, 2026" |
| `total_debt` | 103,400 | **103,359** | Non-current LT debt (no current portion) |
| `lease_liabilities` | 1,800 (double-counted current 585) | **1,746** | 585 current + 1,161 non-current operating lease |
| `preferred_equity` | 0 | **0** ✓ | Series A **fully redeemed** 2026-10-31 (all 30,000 sh) |
| `newbuild_capex_commitments` | 88,800 | **0** | see decision 1 |
| `newbuild_advances_paid` | 1,000 (`~$1M`, mislabel) | **0** | see decision 1 |
| `diluted_shares_outstanding` | 40,900,000 | **40,857,533** | Q1 income statement (wtd-avg diluted) |
| **Operating fleet (manifest)** | 19 MRs | **18 MRs** | phantom `Ardmore_Patriot` removed — see decision 2 |

## Owner treatment decisions (2026-07-01)

1. **Newbuild — EXCLUDE from Q1 entirely (not park, not on-curve — ABSENT).** Note 8 (L2000):
   *"**In April 2026**, the Company signed contracts for the construction of two 40,500 dwt
   Handysize… at $44.9 million per vessel."* The contracts were signed **after** the 3/31
   reporting date → a subsequent event that did not exist at the snapshot: no commitment (no
   commitments note, no vessels-under-construction line at 3/31), no advance (Q1 vessel capex
   $1,024k is existing-fleet deposits — mislabelled "~$1M advances"), no asset. This is
   categorically distinct from NAT (order **existed** at the snapshot, price undisclosed → parked)
   and SB (order existed; the date-mix was fleet-status). ASC's order is simply **absent from Q1**.
   Loading −$88.8M commitment-only into the 3/31 sheet was the SB date-mixing bug in pure form
   AND a §9.6 violation (commitment with no offsetting asset). Removing it fixes both and clears
   ASC from `OFF_CONVENTION_QUEUE` for Q1 (no 3/31 newbuild to place on-curve). **Date-scoped:**
   the newbuilds enter in **Q2** (real as of any Q2 date), where they go **on-curve** using the
   issuer-announced **$44.9M/ship** (a *citable* price, unlike NAT) — commitment + delivered-market
   both entering. Logged so Q1-absent doesn't silently become an omission.

2. **Phantom vessel removed.** The 6-K's 2017 cohort is exactly **3** MRs (Gibraltar Apr-2017,
   Pursuit Feb-2017, Persistence Jan-2017). The manifest invented a 4th, `Ardmore_Patriot` (age-9
   MR, $36.80M mark) — **0 mentions** in both the 6-K and the 20-F; never an Ardmore vessel
   (the author appears to have added a hull to represent "4 product TCs"). Actual owned fleet =
   18 operating MRs + Engineer (HFS) + 2 product Handies + 4 chemical Handies = **25** ✓.

3. **Chemical Handies — carrying-value floor, cited (§11.5 structural, NOT resale-uniform).**
   The 4 × 25,217 DWT stainless Fukuoka chemical tankers have no clean resale curve (a 38k product
   curve would over-value; borrowing the product-Handy curve would be a wrong-class fabrication).
   Mark at **carrying value**, cited to the 20-F "24 of 25 vessels' market > carrying value"
   disclosure → carrying is a *conservative floor* (worth ≥ carrying per ASC's broker-informed
   statement). Reconstructed from cited inputs: cost $29.5M (2013 6-K) − straight-line dep
   (25-yr life, $400/LWT residual ≈ $3.6M; 20-F) over ~10.4–11.2 yrs since delivery →
   **~$18.3M/hull, ~$73.1M total** (base-vessel only, excl capitalized drydock → conservative).
   Validation: the same method on the *on-curve* product Handies gives ~$20.0M carrying vs their
   $24.57M market mark (carrying ~19% below market — consistent with the 20-F). So the chem-Handy
   carrying floor ($18.3M) sits below implied market (~$21.8M); the old $13M estimate was too low.
   Basis flag: `carrying-value-floor · §11.5 structural · no clean 25k-stainless resale market`.

4. **Tier: leaves PROVISIONAL → GOVERNED-WIDE (structural basis), NOT VALIDATED-TIGHT.** Every NAV
   figure now traces (→ out of `NAV_FIGURE_ESTIMATE_QUEUE`); no 3/31 newbuild (→ out of
   `OFF_CONVENTION_QUEUE`). But part of the fleet rests on a carrying-value floor for a class with
   no clean resale market → wide band, GOVERNED-WIDE (like CMBT's structural container class).
   Sub-reason changes `uncited-figure` → `structural-class`. ASC still reads **rich · cycle
   position (not a short)** (§12, product near peak) — NOT a new actionable long.

## PRE-REGISTERED PREDICTION (committed ahead of the pipeline recompute)
- **NAV/sh: $17.82** — band **$17.70 – $17.95**. Baseline $15.96 reproduced; delta +$1.86 =
  newbuild-removal +$2.149 · Patriot −$0.901 · chem-Handy carrying +$0.580 · re-source net +$0.03.
- Price $16.00 → **P/NAV ≈ 0.90×** (was ~1.00×). Tool NAV −16% to the APPROX broker NAV ($21.33
  implied at pnav 0.75) — moved incidentally toward broker via sourcing, not tuning; SANITY OK.
- **Read:** slightly cheap on corrected NAV, rich only vs the near-peak product rate → GOVERNED-WIDE,
  **rich · cycle position (not a short)** unchanged.
- **Guards:** `test_manifest_provenance` clears for ASC (no uncited estimate left in the NAV
  equation); ASC leaves `NAV_FIGURE_ESTIMATE_QUEUE` + `OFF_CONVENTION_QUEUE`; cross-foot
  (fleet_summary vs rows) stays green; tier → GOVERNED-WIDE. Drift gate expects a **material,
  annotated** ASC move (NAV +12%) → re-ratify after acceptance.

## HALT criteria (investigate the INPUT; do not tune to match)
- Recomputed NAV/sh **outside $17.70 – $17.95** → halt, find the input discrepancy.
- SANITY ≠ OK (tool NAV vs broker NAV wider than ±50%) → halt.
- Any guard red that isn't the *expected* ASC clearances above → halt.

## OUTCOME (post-recompute, 2026-07-01)
NAV/sh landed **$17.80** — inside the pre-registered band $17.70–17.95 ✓ (halt not triggered). Guards cleared
as predicted: ASC left `NAV_FIGURE_ESTIMATE_QUEUE` + `OFF_CONVENTION_QUEUE`; tier PROVISIONAL →
**GOVERNED-WIDE · structural-class**; 440 pass / 23 xfail; drift gate 0 unexplained (ASC annotated).
**One prediction MISS (not a halt criterion — the NAV band was the gate):** the position was predicted to stay
"rich · cycle position (not a short)", but the corrected NAV ($17.80 > price $16.00 = **0.90×**) flips the read
to a mild **BUY (+5.2%)** — ASC is no longer rich, so it **LEFT `POSITION_CYCLE_RELABEL`**. The §12 product-cycle
caveat still applies to the earnings/strip leg (near-peak rates; the Q2 newbuild on-curve will trim NAV ~$0.49),
but it is not a rich-NAV read. This is the honest downstream of removing an erroneous −$88.8M drag — surfaced
to the owner. ASC-only baseline re-ratify pending (owner action).
