# Product Weight Comparison — Set A vs Set B (Iran-crisis analog of LNG transition)

**Driver:** Catlin VIE product tanker macro update (2026-06-03). Empirical 2026 product environment (rate spike at multi-decade highs, cargo-mile demand gains, critical regional shortages, US distillates two-decade low) is structurally tight, not glut. Set A's 50% on `glut_base` is mis-centered for 2026 — same diagnostic logic that motivated LNG Set B → Set B-revised. Product Set B applies the LNG-shift analog: +5pp refinery_squeeze, +10pp moderate_correction, -5pp glut_base, -10pp demand_softening, structural_decline unchanged.

**Naming namespace:** "Product Set A/B" are PRODUCT-sector labels. LNG "Set B / Set B-revised" are LNG-sector labels (§11.3). The destination weights are coincidentally identical (both sectors face the same Iran-crisis case), but the labels are NOT interchangeable.

## Weight sets

| Scenario | Set A (current locked v1) | **Set B (constructive v2)** | Δ |
|---|--:|--:|--:|
| refinery_squeeze | 0.10 | **0.15** | +0.05 |
| moderate_correction | 0.15 | **0.25** | +0.10 |
| glut_base | 0.50 | **0.45** | -0.05 |
| demand_softening | 0.25 | **0.15** | -0.10 |
| structural_decline | 0.00 | **0.00** | +0.00 |

**Constructive total** (refinery_squeeze + moderate_correction + glut_base): Set A 0.75 → Set B **0.85** (+0.10).

## Headline impact

| Ticker | Set A PW FV | Set B PW FV | Δ FV | Set A EV | Set B EV | Position change |
|---|--:|--:|--:|--:|--:|---|
| ASC | $15.11 | **$15.79** | $+0.68 (+4.5%) | -9.6% (TRIM/SHORT) | -5.5% (**TRIM/SHORT**) | unchanged |
| STNG | $67.59 | **$72.33** | $+4.74 (+7.0%) | -11.2% (TRIM/SHORT) | -4.9% (**HOLD**) | **FLIP** |
| INSW | $56.52 | **$58.01** | $+1.48 (+2.6%) | -38.8% (TRIM/SHORT) | -37.2% (**TRIM/SHORT**) | unchanged |

## INSW preservation invariant — HOLDS THROUGH SET B (notable property)

INSW whole-co PW FV is **$52.08 under both Set A and Set B** — unchanged. This is not coincidence: `_aggregate_hybrid_report` builds the whole-co probability-weighted FV by pairing crude scenario i with product scenario i (see METHODOLOGY §6 v2) and **uses crude scenario weights** as the aggregation probability. The per-scenario sum `c.fair_value + p.fair_value` is weight-independent (per-scenario FVs are scenario-specific values, not weight-dependent), and the aggregation weights come from the crude doc. Therefore changing product weights affects pure-product names (ASC, STNG) but **does not affect INSW whole-co FV under the current hybrid carve-out methodology**. This is a property of the framework worth documenting — the INSW preservation test will continue to pass through this transition.
