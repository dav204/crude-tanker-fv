# SB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $6.82
- **Model fair value:** $9.69
- **Analyst target:** $7.10

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Pana | 985.8 |
| Fleet value — Post-Panamax | 407.1 |
| Fleet value — Cape | 273.2 |
| + Cash & equivalents | 171.8 |
| + Working capital (net) | 53.8 |
| − Total debt | 544.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 227.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,020.2** |
| Diluted shares | 101,826,580 |
| **NAV / share** | **$10.02** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Pana, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,700 | 18,227 | 0.590 | 0.177 | 0.172 |
| Q2 | 19,250 | 18,047 | 0.581 | 0.174 | 0.166 |
| Q3 | 17,100 | 17,187 | 0.516 | 0.155 | 0.143 |
| Q4 | 16,500 | 16,947 | 0.500 | 0.150 | 0.135 |
| Q5 | 15,900 | 16,707 | 0.484 | 0.145 | 0.127 |
| Q6 | 15,300 | 16,467 | 0.468 | 0.141 | 0.120 |
| Q7 | 14,900 | 16,307 | 0.459 | 0.138 | 0.115 |
| Q8 | 14,600 | 16,187 | 0.451 | 0.135 | 0.110 |
| Σ discounted DPS | | | | | 1.09 |
| Terminal value (NAV, q9) | | | | 9.92 | 7.84 |
| **DivStrip implied price** | | | | | **$8.93** |

_FFA spot is the Pana forward curve that drives the strip cash flows; its 12-month average is **$18,138/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$19,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $19,500 / 10-yr mean $11,900 = **1.62×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $10.02 (NAV) + 0.30 × $8.93 (strip) = **$9.69**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 11.45 | 118% |
| Balance-sheet net | -4.44 | -46% |
| Discounted DPS (strip, 8-10q) | 0.33 | 3% |
| Discounted terminal (aged NAV) | 2.35 | 24% |
| **Blend FV** | **9.69** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.88 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $9.76 |
| 95% | $9.78 |
| 100% | $9.78 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$10.02** ≥ price **$6.82** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 13,827 | 0.00× |
| 12-month FFA | 20,484 | 0.00× |
| Current spot | 22,623 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Pana (59% of fleet value) | 0 | 0.00× |
| Post-Panamax (24% of fleet value) | 0 | 0.00× |
| Cape (16% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $6.50 | $7.96 | $9.43 | $10.89 | $12.36 |
| **-15%** | $6.63 | $8.10 | $9.56 | $11.02 | $12.49 |
| **+0%** | $6.77 | $8.23 | $9.69 | $11.16 | $12.62 |
| **+15%** | $6.90 | $8.36 | $9.83 | $11.29 | $12.75 |
| **+30%** | $7.03 | $8.49 | $9.96 | $11.42 | $12.89 |

_Current price $6.82. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$9.69** is +42.1% vs the current price ($6.82) and +36.5% vs the analyst target ($7.10). NAV alone covers the price (NAV/sh $10.02 ≥ $6.82); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
