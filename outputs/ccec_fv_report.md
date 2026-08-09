# CCEC — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $22.37
- **Model fair value:** $29.97
- **Analyst target:** $25.17

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LNGC | 5,363.5 |
| Fleet value — MGC | 649.1 |
| + Cash & equivalents | 268.9 |
| + Working capital (net) | -81.7 |
| − Total debt | 2,930.8 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 1,697.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,571.9** |
| Diluted shares | 61,160,839 |
| **NAV / share** | **$25.70** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LNGC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 50,000 | 80,557 | 1.942 | 0.150 | 0.146 |
| Q2 | 80,000 | 83,557 | 2.044 | 0.150 | 0.142 |
| Q3 | 75,000 | 83,057 | 2.026 | 0.150 | 0.139 |
| Q4 | 48,000 | 80,357 | 1.936 | 0.150 | 0.135 |
| Q5 | 52,000 | 80,757 | 1.949 | 0.150 | 0.132 |
| Q6 | 80,000 | 83,557 | 2.044 | 0.150 | 0.128 |
| Q7 | 75,000 | 83,057 | 2.026 | 0.150 | 0.125 |
| Q8 | 50,000 | 80,557 | 1.942 | 0.150 | 0.122 |
| Σ discounted DPS | | | | | 1.07 |
| Terminal value (NAV, q9) | | | | 40.14 | 31.74 |
| **DivStrip implied price** | | | | | **$32.81** |

_FFA spot is the LNGC forward curve that drives the strip cash flows; its 12-month average is **$63,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$60,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $60,000 / 10-yr mean $85,000 = **0.78×** → **below-mid**
- Weights: w_nav = 0.40, w_earn = 0.60

## Blended fair value

0.40 × $25.70 (NAV) + 0.60 × $32.81 (strip) = **$29.97**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 39.32 | 131% |
| Balance-sheet net | -29.04 | -97% |
| Discounted DPS (strip, 8-10q) | 0.64 | 2% |
| Discounted terminal (aged NAV) | 19.04 | 64% |
| **Blend FV** | **29.97** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.40 + 0.60 × 0.97 = **98%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $30.73 |
| 95% | $30.87 |
| 100% | $30.92 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$25.70** ≥ price **$22.37** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 77,983 | 0.00× |
| 12-month FFA | 59,175 | 0.00× |
| Current spot | 38,381 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| LNGC (89% of fleet value) | 0 | 0.00× |
| MGC (11% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $12.54 | $21.12 | $29.71 | $38.29 | $46.87 |
| **-15%** | $12.67 | $21.25 | $29.84 | $38.42 | $47.00 |
| **+0%** | $12.80 | $21.38 | $29.97 | $38.55 | $47.13 |
| **+15%** | $12.93 | $21.51 | $30.10 | $38.68 | $47.26 |
| **+30%** | $13.06 | $21.64 | $30.23 | $38.81 | $47.39 |

_Current price $22.37. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$29.97** is +34.0% vs the current price ($22.37) and +19.1% vs the analyst target ($25.17). NAV alone covers the price (NAV/sh $25.70 ≥ $22.37); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

## Additional diagnostics

- [`ccec_buy_diagnostic.md`](ccec_buy_diagnostic.md) — CCEC — buy-actionability diagnostic
