# ASC — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $16.00
- **Model fair value:** $14.88
- **Analyst target:** $17.95

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — MR | 617.4 |
| Fleet value — Handysize | 49.1 |
| + Cash & equivalents | 47.2 |
| + Working capital (net) | 131.0 |
| − Total debt | 103.4 |
| − Lease liabilities | 1.8 |
| − Newbuild commitments | 88.8 |
| + Newbuild advances | 1.0 |
| **= NAV total** | **651.7** |
| Diluted shares | 40,900,000 |
| **NAV / share** | **$15.93** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 22,000 | 22,000 | 0.465 | 0.310 | 0.302 |
| Q2 | 30,000 | 30,000 | 0.831 | 0.555 | 0.526 |
| Q3 | 28,000 | 28,000 | 0.740 | 0.493 | 0.456 |
| Q4 | 19,000 | 19,000 | 0.328 | 0.219 | 0.197 |
| Q5 | 18,000 | 18,000 | 0.282 | 0.188 | 0.165 |
| Q6 | 23,000 | 23,000 | 0.511 | 0.341 | 0.291 |
| Q7 | 26,000 | 26,000 | 0.648 | 0.432 | 0.360 |
| Q8 | 18,000 | 18,000 | 0.282 | 0.188 | 0.153 |
| Σ discounted DPS | | | | | 2.45 |
| Terminal value (NAV, q9) | | | | 13.72 | 10.85 |
| **DivStrip implied price** | | | | | **$13.30** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.37×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $15.93 (NAV) + 0.40 × $13.30 (strip) = **$14.88**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.08 |
| 95% | $15.30 |
| 100% | $15.37 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.56× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **38,532** | — |
| 10-year mean | 16,000 | 2.41× |
| 12-month FFA | 24,750 | 1.56× |
| Current spot | 20,000 | 1.93× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (93% of fleet value) | 38,532 | 2.41× |
| Handysize (7% of fleet value) | 38,532 | 2.41× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $11.43 | $12.85 | $14.28 | $15.70 | $17.12 |
| **-15%** | $11.73 | $13.16 | $14.58 | $16.00 | $17.42 |
| **+0%** | $12.03 | $13.46 | $14.88 | $16.30 | $17.73 |
| **+15%** | $12.34 | $13.76 | $15.18 | $16.60 | $18.03 |
| **+30%** | $12.64 | $14.06 | $15.48 | $16.91 | $18.33 |

_Current price $16.00. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$14.88** is -7.0% vs the current price ($16.00) and -17.1% vs the analyst target ($17.95). The current price implies the fleet earning a value-weighted blended **$38,532/day** (1.56× the current forward) — 2.4× the value-weighted 10-yr mean ($16,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $30.2M (-8%) / 10yr $22.1M (-12%) [n=20], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
