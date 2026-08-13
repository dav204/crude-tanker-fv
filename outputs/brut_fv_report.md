# BRUT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $6.26
- **Model fair value:** $9.63
- **Analyst target:** $7.13

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 1,856.7 |
| + Cash & equivalents | 11.8 |
| + Working capital (net) | -0.7 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 1,272.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **595.8** |
| Diluted shares | 61,923,808 |
| **NAV / share** | **$9.62** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 179,650 | 179,650 | 0.187 | 0.000 | 0.000 |
| Q2 | 179,650 | 179,650 | 0.435 | 0.000 | 0.000 |
| Q3 | 105,700 | 105,700 | 0.221 | 0.000 | 0.000 |
| Q4 | 105,700 | 105,700 | 0.221 | 0.000 | 0.000 |
| Q5 | 48,850 | 48,850 | 0.116 | 0.000 | 0.000 |
| Q6 | 48,850 | 48,850 | 0.174 | 0.000 | 0.000 |
| Q7 | 48,850 | 48,850 | 0.174 | 0.000 | 0.000 |
| Q8 | 48,850 | 48,850 | 0.292 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 12.22 | 9.66 |
| **DivStrip implied price** | | | | | **$9.66** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$142,675/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$105,700/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $105,700 / 10-yr mean $40,000 = **2.64×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $9.62 (NAV) + 0.30 × $9.66 (strip) = **$9.63**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 20.99 | 218% |
| Balance-sheet net | -14.25 | -148% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 2.90 | 30% |
| **Blend FV** | **9.63** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $9.68 |
| 95% | $9.69 |
| 100% | $9.69 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$9.62** ≥ price **$6.26** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 40,000 | 0.00× |
| 12-month FFA | 142,675 | 0.00× |
| Current spot | 488,900 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $3.79 | $6.62 | $9.45 | $12.28 | $15.11 |
| **-15%** | $3.89 | $6.71 | $9.54 | $12.37 | $15.20 |
| **+0%** | $3.98 | $6.81 | $9.63 | $12.46 | $15.29 |
| **+15%** | $4.07 | $6.90 | $9.73 | $12.55 | $15.38 |
| **+30%** | $4.16 | $6.99 | $9.82 | $12.65 | $15.48 |

_Current price $6.26. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$9.63** is +54.0% vs the current price ($6.26) and +35.1% vs the analyst target ($7.13). NAV alone covers the price (NAV/sh $9.62 ≥ $6.26); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
