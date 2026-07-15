# NAT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $6.29
- **Model fair value:** $3.09
- **Analyst target:** $6.00

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 807.5 |
| + Cash & equivalents | 81.1 |
| + Working capital (net) | 53.6 |
| − Total debt | 415.4 |
| − Lease liabilities | 0.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **591.5** |
| Diluted shares | 211,750,663 |
| **NAV / share** | **$2.79** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 81,500 | 69,781 | 0.347 | 0.347 | 0.338 |
| Q2 | 99,000 | 81,812 | 0.427 | 0.427 | 0.405 |
| Q3 | 92,000 | 77,000 | 0.395 | 0.395 | 0.365 |
| Q4 | 67,500 | 60,156 | 0.283 | 0.283 | 0.255 |
| Q5 | 60,000 | 55,000 | 0.249 | 0.249 | 0.219 |
| Q6 | 78,000 | 67,375 | 0.331 | 0.331 | 0.283 |
| Q7 | 81,500 | 69,781 | 0.347 | 0.347 | 0.289 |
| Q8 | 56,500 | 52,594 | 0.233 | 0.233 | 0.189 |
| Σ discounted DPS | | | | | 2.34 |
| Terminal value (NAV, q9) | | | | 1.83 | 1.45 |
| **DivStrip implied price** | | | | | **$3.79** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.21×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $2.79 (NAV) + 0.30 × $3.79 (strip) = **$3.09**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 2.67 | 86% |
| Balance-sheet net | -0.71 | -23% |
| Discounted DPS (strip, 8-10q) | 0.70 | 23% |
| Discounted terminal (aged NAV) | 0.44 | 14% |
| **Blend FV** | **3.09** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.38 = **81%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $3.08 |
| 95% | $3.09 |
| 100% | $3.09 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **5.24× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **445,150** | — |
| 10-year mean | 27,747 | 16.04× |
| 12-month FFA | 85,000 | 5.24× |
| Current spot | 124,800 | 3.57× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $2.20 | $2.53 | $2.87 | $3.20 | $3.54 |
| **-15%** | $2.31 | $2.65 | $2.98 | $3.32 | $3.65 |
| **+0%** | $2.42 | $2.76 | $3.09 | $3.43 | $3.76 |
| **+15%** | $2.54 | $2.87 | $3.21 | $3.54 | $3.88 |
| **+30%** | $2.65 | $2.99 | $3.32 | $3.65 | $3.99 |

_Current price $6.29. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$3.09** is -50.8% vs the current price ($6.29) and -48.4% vs the analyst target ($6.00). The current price implies the fleet earning a value-weighted blended **$445,150/day** (5.24× the current forward) — 16.0× the value-weighted 10-yr mean ($27,747, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
