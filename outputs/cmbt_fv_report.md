# CMBT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $14.10
- **Model fair value:** $14.68
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 624.4 |
| Fleet value — Suezmax | 1,248.7 |
| Fleet value — Cape | 4,626.7 |
| Fleet value — Pana | 943.1 |
| Fleet value — Ctr-Large | 257.2 |
| + Cash & equivalents | 202.9 |
| + Working capital (net) | 912.1 |
| − Total debt | 5,238.2 |
| − Lease liabilities | 6.2 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 759.8 |
| **= NAV total** | **4,430.6** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$15.27** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 31,200 | 31,200 | 0.954 | 0.477 | 0.465 |
| Q2 | 31,450 | 31,450 | 1.075 | 0.537 | 0.510 |
| Q3 | 28,500 | 28,500 | 0.928 | 0.464 | 0.429 |
| Q4 | 27,000 | 27,000 | 0.719 | 0.359 | 0.324 |
| Q5 | 25,500 | 25,500 | 0.626 | 0.313 | 0.275 |
| Q6 | 25,000 | 25,000 | 0.725 | 0.362 | 0.310 |
| Q7 | 24,500 | 24,500 | 0.738 | 0.369 | 0.307 |
| Q8 | 24,000 | 24,000 | 0.550 | 0.275 | 0.223 |
| Σ discounted DPS | | | | | 2.84 |
| Terminal value (NAV, q9) | | | | 13.23 | 10.46 |
| **DivStrip implied price** | | | | | **$13.30** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$29,538/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$27,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $27,000 / 10-yr mean $23,650 = **1.50×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $15.27 (NAV) + 0.30 × $13.30 (strip) = **$14.68**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $14.74 |
| 95% | $14.77 |
| 100% | $14.78 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.79× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **38,337** | — |
| 10-year mean | 24,781 | 1.55× |
| 12-month FFA | 48,386 | 0.79× |
| Current spot | 70,060 | 0.55× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 23,403 | 0.99× |
| Suezmax (16% of fleet value) | 67,348 | 2.43× |
| Pana (12% of fleet value) | 14,614 | 1.23× |
| VLCC (8% of fleet value) | 122,811 | 3.07× |
| Ctr-Large (3% of fleet value) | 48,035 | 1.17× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $9.11 | $11.48 | $13.84 | $16.21 | $18.57 |
| **-15%** | $9.53 | $11.90 | $14.26 | $16.62 | $18.99 |
| **+0%** | $9.95 | $12.32 | $14.68 | $17.04 | $19.41 |
| **+15%** | $10.37 | $12.73 | $15.10 | $17.46 | $19.83 |
| **+30%** | $10.79 | $13.15 | $15.52 | $17.88 | $20.24 |

_Current price $14.10. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$14.68** is +4.1% vs the current price ($14.10) and -11.5% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$38,337/day** (0.79× the current forward) — 1.5× the value-weighted 10-yr mean ($24,781, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
