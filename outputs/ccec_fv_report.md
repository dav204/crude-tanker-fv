# CCEC — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $22.68
- **Model fair value:** $32.08
- **Analyst target:** $25.17

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LNGC | 5,399.5 |
| Fleet value — MGC | 585.0 |
| + Cash & equivalents | 546.4 |
| + Working capital (net) | 12.9 |
| − Total debt | 2,602.9 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 2,251.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,689.3** |
| Diluted shares | 60,121,845 |
| **NAV / share** | **$28.10** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LNGC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 50,000 | 80,557 | 1.938 | 0.150 | 0.146 |
| Q2 | 80,000 | 83,557 | 2.041 | 0.150 | 0.142 |
| Q3 | 75,000 | 83,057 | 2.023 | 0.150 | 0.139 |
| Q4 | 48,000 | 80,357 | 1.932 | 0.150 | 0.135 |
| Q5 | 52,000 | 80,757 | 1.946 | 0.150 | 0.132 |
| Q6 | 80,000 | 83,557 | 2.041 | 0.150 | 0.128 |
| Q7 | 75,000 | 83,057 | 2.023 | 0.150 | 0.125 |
| Q8 | 50,000 | 80,557 | 1.938 | 0.150 | 0.122 |
| Σ discounted DPS | | | | | 1.07 |
| Terminal value (NAV, q9) | | | | 42.59 | 33.67 |
| **DivStrip implied price** | | | | | **$34.74** |

_FFA spot is the LNGC forward curve that drives the strip cash flows; its 12-month average is **$63,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$60,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $60,000 / 10-yr mean $85,000 = **0.77×** → **below-mid**
- Weights: w_nav = 0.40, w_earn = 0.60

## Blended fair value

0.40 × $28.10 (NAV) + 0.60 × $34.74 (strip) = **$32.08**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 39.82 | 124% |
| Balance-sheet net | -28.58 | -89% |
| Discounted DPS (strip, 8-10q) | 0.64 | 2% |
| Discounted terminal (aged NAV) | 20.20 | 63% |
| **Blend FV** | **32.08** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.40 + 0.60 × 0.97 = **98%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $32.85 |
| 95% | $32.99 |
| 100% | $33.04 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$28.10** ≥ price **$22.68** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 78,646 | 0.00× |
| 12-month FFA | 59,560 | 0.00× |
| Current spot | 38,534 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| LNGC (90% of fleet value) | 0 | 0.00× |
| MGC (10% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $14.43 | $23.13 | $31.82 | $40.52 | $49.21 |
| **-15%** | $14.56 | $23.26 | $31.95 | $40.65 | $49.34 |
| **+0%** | $14.69 | $23.39 | $32.08 | $40.78 | $49.47 |
| **+15%** | $14.83 | $23.52 | $32.22 | $40.91 | $49.61 |
| **+30%** | $14.96 | $23.65 | $32.35 | $41.04 | $49.74 |

_Current price $22.68. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$32.08** is +41.4% vs the current price ($22.68) and +27.5% vs the analyst target ($25.17). NAV alone covers the price (NAV/sh $28.10 ≥ $22.68); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

## Additional diagnostics

- [`ccec_buy_diagnostic.md`](ccec_buy_diagnostic.md) — CCEC — buy-actionability diagnostic
