# DHT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $19.17
- **Model fair value:** $15.32
- **Analyst target:** $16.00

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 2,633.4 |
| + Cash & equivalents | 161.7 |
| + Working capital (net) | 137.6 |
| − Total debt | 434.8 |
| − Lease liabilities | 1.0 |
| − Newbuild commitments | 77.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,419.4** |
| Diluted shares | 161,235,573 |
| **NAV / share** | **$15.01** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 179,650 | 132,922 | 1.502 | 1.502 | 1.463 |
| Q2 | 179,650 | 132,922 | 1.502 | 1.502 | 1.426 |
| Q3 | 105,700 | 94,468 | 1.012 | 1.012 | 0.936 |
| Q4 | 105,700 | 94,468 | 1.012 | 1.012 | 0.912 |
| Q5 | 48,850 | 64,906 | 0.635 | 0.635 | 0.558 |
| Q6 | 48,850 | 64,906 | 0.635 | 0.635 | 0.543 |
| Q7 | 48,850 | 64,906 | 0.635 | 0.635 | 0.529 |
| Q8 | 48,850 | 64,906 | 0.635 | 0.635 | 0.516 |
| Σ discounted DPS | | | | | 6.88 |
| Terminal value (NAV, q9) | | | | 11.58 | 9.16 |
| **DivStrip implied price** | | | | | **$16.04** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$142,675/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$105,700/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $105,700 / 10-yr mean $40,000 = **2.64×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $15.01 (NAV) + 0.30 × $16.04 (strip) = **$15.32**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 11.43 | 75% |
| Balance-sheet net | -0.93 | -6% |
| Discounted DPS (strip, 8-10q) | 2.06 | 13% |
| Discounted terminal (aged NAV) | 2.75 | 18% |
| **Blend FV** | **15.32** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.57 = **87%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.26 |
| 95% | $15.30 |
| 100% | $15.32 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.76× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **535,858** | — |
| 10-year mean | 40,000 | 13.40× |
| 12-month FFA | 142,675 | 3.76× |
| Current spot | 488,900 | 1.10× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $12.00 | $13.45 | $14.90 | $16.35 | $17.80 |
| **-15%** | $12.21 | $13.66 | $15.11 | $16.56 | $18.01 |
| **+0%** | $12.42 | $13.87 | $15.32 | $16.77 | $18.21 |
| **+15%** | $12.63 | $14.08 | $15.53 | $16.98 | $18.42 |
| **+30%** | $12.84 | $14.29 | $15.74 | $17.18 | $18.63 |

_Current price $19.17. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.32** is -20.1% vs the current price ($19.17) and -4.3% vs the analyst target ($16.00). The current price implies the fleet earning a value-weighted blended **$535,858/day** (3.76× the current forward) — 13.4× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
