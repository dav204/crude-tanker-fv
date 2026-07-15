# DHT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $18.18
- **Model fair value:** $14.95
- **Analyst target:** $16.00

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 2,558.1 |
| + Cash & equivalents | 126.2 |
| + Working capital (net) | 134.1 |
| − Total debt | 505.3 |
| − Lease liabilities | 1.0 |
| − Newbuild commitments | 77.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,234.7** |
| Diluted shares | 161,041,637 |
| **NAV / share** | **$13.88** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 118,981 | 1.326 | 1.326 | 1.292 |
| Q2 | 183,500 | 138,781 | 1.579 | 1.579 | 1.498 |
| Q3 | 165,500 | 128,881 | 1.452 | 1.452 | 1.343 |
| Q4 | 123,500 | 105,781 | 1.157 | 1.157 | 1.043 |
| Q5 | 111,500 | 99,181 | 1.073 | 1.073 | 0.942 |
| Q6 | 135,500 | 112,381 | 1.242 | 1.242 | 1.062 |
| Q7 | 147,500 | 118,981 | 1.326 | 1.326 | 1.105 |
| Q8 | 105,500 | 95,881 | 1.031 | 1.031 | 0.837 |
| Σ discounted DPS | | | | | 9.12 |
| Terminal value (NAV, q9) | | | | 10.56 | 8.35 |
| **DivStrip implied price** | | | | | **$17.47** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.79×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $13.88 (NAV) + 0.30 × $17.47 (strip) = **$14.95**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 11.12 | 74% |
| Balance-sheet net | -1.41 | -9% |
| Discounted DPS (strip, 8-10q) | 2.74 | 18% |
| Discounted terminal (aged NAV) | 2.50 | 17% |
| **Blend FV** | **14.95** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.48 = **84%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $14.89 |
| 95% | $14.94 |
| 100% | $14.95 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.53× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **391,452** | — |
| 10-year mean | 40,000 | 9.79× |
| 12-month FFA | 155,000 | 2.53× |
| Current spot | 285,500 | 1.37× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $11.50 | $12.91 | $14.32 | $15.73 | $17.14 |
| **-15%** | $11.82 | $13.23 | $14.64 | $16.05 | $17.46 |
| **+0%** | $12.13 | $13.54 | $14.95 | $16.36 | $17.77 |
| **+15%** | $12.45 | $13.86 | $15.27 | $16.68 | $18.09 |
| **+30%** | $12.77 | $14.18 | $15.59 | $17.00 | $18.41 |

_Current price $18.18. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$14.95** is -17.7% vs the current price ($18.18) and -6.5% vs the analyst target ($16.00). The current price implies the fleet earning a value-weighted blended **$391,452/day** (2.53× the current forward) — 9.8× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
