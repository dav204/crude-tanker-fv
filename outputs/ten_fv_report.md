# TEN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $38.83
- **Model fair value:** $61.29
- **Analyst target:** $51.50

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 314.3 |
| Fleet value — Suezmax | 1,073.4 |
| Fleet value — Aframax | 1,455.7 |
| Fleet value — LR2 | 233.5 |
| Fleet value — LR1 | 250.6 |
| Fleet value — MR | 107.5 |
| Fleet value — Handysize | 26.9 |
| Fleet value — LNGC | 443.2 |
| + Cash & equivalents | 321.4 |
| + Working capital (net) | 28.0 |
| − Total debt | 2,148.2 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 400.0 |
| **= NAV total** | **2,672.2** |
| Diluted shares | 30,127,603 |
| **NAV / share** | **$88.70** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Aframax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 36,629 | 5.042 | 1.333 | 1.299 |
| Q2 | 88,000 | 38,995 | 5.502 | 1.420 | 1.348 |
| Q3 | 82,000 | 37,903 | 5.306 | 1.383 | 1.279 |
| Q4 | 64,000 | 34,627 | 4.679 | 1.264 | 1.139 |
| Q5 | 59,000 | 33,717 | 4.510 | 1.232 | 1.081 |
| Q6 | 70,000 | 35,719 | 4.908 | 1.308 | 1.118 |
| Q7 | 74,000 | 36,447 | 5.042 | 1.333 | 1.110 |
| Q8 | 56,000 | 33,171 | 4.418 | 1.214 | 0.986 |
| Σ discounted DPS | | | | | 9.36 |
| Terminal value (NAV, q9) | | | | 63.33 | 50.07 |
| **DivStrip implied price** | | | | | **$59.43** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $36,483 = **1.79×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $62.09 (NAV) + 0.30 × $59.43 (strip) = **$61.29**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 90.74 | 148% |
| Balance-sheet net | -28.65 | -47% |
| §15 governance haircut | -18.63 | -30% |
| Discounted DPS (strip, 8-10q) | 2.81 | 5% |
| Discounted terminal (aged NAV) | 15.02 | 25% |
| **Blend FV** | **61.29** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.84 = **95%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $63.74 |
| 95% | $64.34 |
| 100% | $64.54 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$88.70** ≥ price **$38.83** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 38,065 | 0.00× |
| 12-month FFA | 82,241 | 0.00× |
| Current spot | 81,386 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Aframax (37% of fleet value) | 0 | 0.00× |
| Suezmax (27% of fleet value) | 0 | 0.00× |
| LNGC (11% of fleet value) | 0 | 0.00× |
| VLCC (8% of fleet value) | 0 | 0.00× |
| LR1 (6% of fleet value) | 0 | 0.00× |
| LR2 (6% of fleet value) | 0 | 0.00× |
| MR (3% of fleet value) | 0 | 0.00× |
| Handysize (1% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $44.17 | $52.22 | $60.28 | $68.33 | $76.38 |
| **-15%** | $44.68 | $52.73 | $60.78 | $68.84 | $76.89 |
| **+0%** | $45.18 | $53.24 | $61.29 | $69.34 | $77.40 |
| **+15%** | $45.69 | $53.75 | $61.80 | $69.85 | $77.91 |
| **+30%** | $46.20 | $54.25 | $62.31 | $70.36 | $78.41 |

_Current price $38.83. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$61.29** is +57.8% vs the current price ($38.83) and +19.0% vs the analyst target ($51.50). NAV alone covers the price (NAV/sh $88.70 ≥ $38.83); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
