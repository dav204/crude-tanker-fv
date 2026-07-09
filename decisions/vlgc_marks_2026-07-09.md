# VLGC marks — WO3 Phase 2 decision record (2026-07-09)

**Authority:** WO3_LPG_ONBOARDING.md Phase 2 · methodology `decisions/lpg_methodology_2026-07-07.md`
(ratified) · sample `decisions/sec99_print_hunt_2026-07-06.md` (verdict: v1-PROVISIONAL — 10-yr node
strong, 5-yr node empty). Produced by the WO3 agent; §9.9 discipline throughout (no back-solve, no
forced fit, every print cited).

## What shipped

1. **`transactions/vlgc.yaml`** — 7 in-window prints (ages 9-17, sale_year−build_year convention,
   matching every other class file) + 3 documentation rows (Hampshire 18yr / Lycaste Peace 23yr /
   BW Yushi OPTION strike, all `in_fit: false`).
2. **`vessel_value_curves.yaml` VLGC block** — flat class (no dwt scaling), 54k dwt / ~84k cbm
   reference: NB $117.5M · 5yr $92M · 10yr $80M · age-25 anchor $42M.
3. **Basis registries:** `AGE0_BASIS["VLGC"]` = documented exception (no broker gas resale line in
   the corpus); `basis_status.yaml` VLGC = **pending-sourceable** (Group A — real S&P market, no
   dated age-0 resale mark).

## The fit (as_of 2026-07-09, production path `apply_transaction_anchored_curves`)

n=7, slope **−$2.40M/yr**, no clamps. Anchors: **age-10 $80.3M / age-5 $92.3M**.

| Sensitivity cut | n | slope | age-5 | age-10 |
|---|--:|--:|--:|--:|
| full 7-print sample | 7 | −2.40 | 92.3 | **80.3** |
| ex BW Lord (Cedar carries old node) | 6 | −1.88 | 89.7 | **80.3** |
| ex BW Cedar (Lord carries) | 6 | −2.53 | 92.9 | **80.3** |
| ex related-party pair (Chinook/Pampero) | 5 | −2.70 | 95.9 | 82.4 |
| ex ALL FOUR BW prints | 3 | +1.68 | — | — (solver falls back, by design) |

- **The age-10 anchor is the strong node** — $80.3M invariant across every single-source exclusion.
- **The age-5 anchor is EXTRAPOLATED** (zero 5-yr prints exist) — $89.7-95.9M across cuts →
  **flagged WIDE**. Cross-checks: age-5/NB = **0.79, exactly the VLCC curve's 138/175 ratio**;
  the BW Yushi 2020-built option strike ~$70M sits below it, as a strike should.
- **The slope rests on the BW old-node prints** (Lord 17/$61M company-announced + Cedar 17/$65M
  signed Nov-2024, recency-weighted ~0.40). Excluding all BW prints degenerates the sample and the
  solver's negative-slope guard correctly refuses to fit. Documented, not hidden.
- **Related-party downweight** (memo instruction): delivered mechanically by recency weighting
  (Mar-2025 prints carry w≈0.45 vs ~0.85 for the 2026 arm's-length cluster); `quality_flag`
  kept `standard` — a +5% financing-style uplift would guess the direction of any JV mispricing.

## Old-age leg (the sector's no-scrappage cell)

`scrap_25yr` $42M is an **age-25 VALUE anchor** (LNGC convention), NOT demolition (~$12M at
~21k LDT): the 10yr→25yr interpolation reads **$59.7M @18 vs Hampshire $57M** and
**$47.1M @23 vs Lycaste Peace $48M** — the two out-of-window prints reproduce within $2-3M.
Old VLGCs trade far above demo (the charter's "no scrappage lever" market cell, priced).

## Broker cross-reads (recorded, NOT calibration)

- Pareto generic-2016 quote **$72M** vs fitted age-10 **$80.3M**: the tool sits ~+11% above
  Pareto's quote — consistent with the prints themselves ("10%+ beat vs our $72m quote", Pareto's
  own comment on Sinogas). Per the two-regime k_broker semantics (§9.9/B4), LPG now reads as a
  TRANSACTION-ANCHORED sector; expect k_broker BELOW the crude 1.12-1.14 premium, possibly <1.
- Pareto NAV pegs (BWLP NOK 148 / Dorian $34, Dec-2025) remain the Phase-5 lock validators —
  the ≥70%/±10% v1 bar applies at lock-time against tool NAV built on THESE marks.

## Conservatisms + watch items

- `scrubber_premium: 0` and `eco_premium_pct: 0.0` — no sourced VLGC premium print for either;
  a value-adding flag without a source would violate the figure-provenance rule.
- **Watch:** Dorian trio per-vessel splits (filings by Q4-26 delivery — replace the Cobra
  broker-reported row); Jag Vishnu (2002) if priced; **Advanced full-year re-harvest** (corpus is
  quarterly-sampled; true 2025 counts likely 3-10× — the single highest-value sample upgrade).
- Age-0 re-wire toward resale-uniform on the first VLGC resale print.

## Gate impact

Zero LPG names on the watchlist → no NAV/EV/band moves anywhere in the book; the fit adds a
VLGC row to `outputs/transaction_anchor_comparison.md` on the next pipeline run. Drift gate
unaffected (no valued name touches the VLGC curve).
