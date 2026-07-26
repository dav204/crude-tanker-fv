# NAT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $6.45
- **Model fair value:** $3.14
- **Analyst target:** $6.00

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 818.5 |
| + Cash & equivalents | 81.1 |
| + Working capital (net) | 53.6 |
| − Total debt | 415.4 |
| − Lease liabilities | 0.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **602.4** |
| Diluted shares | 211,750,663 |
| **NAV / share** | **$2.85** |

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
| Terminal value (NAV, q9) | | | | 1.87 | 1.48 |
| **DivStrip implied price** | | | | | **$3.82** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.21×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $2.85 (NAV) + 0.30 × $3.82 (strip) = **$3.14**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 2.71 | 86% |
| Balance-sheet net | -0.71 | -23% |
| Discounted DPS (strip, 8-10q) | 0.70 | 22% |
| Discounted terminal (aged NAV) | 0.44 | 14% |
| **Blend FV** | **3.14** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.39 = **82%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $3.12 |
| 95% | $3.13 |
| 100% | $3.14 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **5.39× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **458,136** | — |
| 10-year mean | 27,747 | 16.51× |
| 12-month FFA | 85,000 | 5.39× |
| Current spot | 124,800 | 3.67× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $2.23 | $2.57 | $2.91 | $3.25 | $3.59 |
| **-15%** | $2.35 | $2.69 | $3.03 | $3.36 | $3.70 |
| **+0%** | $2.46 | $2.80 | $3.14 | $3.48 | $3.82 |
| **+15%** | $2.57 | $2.91 | $3.25 | $3.59 | $3.93 |
| **+30%** | $2.69 | $3.03 | $3.36 | $3.70 | $4.04 |

_Current price $6.45. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$3.14** is -51.3% vs the current price ($6.45) and -47.7% vs the analyst target ($6.00). The current price implies the fleet earning a value-weighted blended **$458,136/day** (5.39× the current forward) — 16.5× the value-weighted 10-yr mean ($27,747, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
