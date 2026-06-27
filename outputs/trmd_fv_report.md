# TRMD — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $26.81
- **Model fair value:** $26.35
- **Analyst target:** $25.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 1,366.7 |
| Fleet value — LR1 | 342.3 |
| Fleet value — MR | 2,017.1 |
| + Cash & equivalents | 196.0 |
| + Working capital (net) | 110.0 |
| − Total debt | 1,089.6 |
| − Lease liabilities | 5.0 |
| − Newbuild commitments | 360.0 |
| + Newbuild advances | 50.0 |
| **= NAV total** | **2,627.4** |
| Diluted shares | 103,300,000 |
| **NAV / share** | **$25.43** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 22,000 | 22,000 | 2.165 | 1.624 | 1.582 |
| Q2 | 30,000 | 30,000 | 2.949 | 2.212 | 2.099 |
| Q3 | 28,000 | 28,000 | 2.678 | 2.008 | 1.857 |
| Q4 | 19,000 | 19,000 | 1.703 | 1.278 | 1.151 |
| Q5 | 18,000 | 18,000 | 1.513 | 1.135 | 0.996 |
| Q6 | 23,000 | 23,000 | 2.082 | 1.561 | 1.335 |
| Q7 | 26,000 | 26,000 | 2.352 | 1.764 | 1.470 |
| Q8 | 18,000 | 18,000 | 1.431 | 1.074 | 0.871 |
| Σ discounted DPS | | | | | 11.36 |
| Terminal value (NAV, q9) | | | | 21.65 | 17.12 |
| **DivStrip implied price** | | | | | **$28.48** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.68×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $25.43 (NAV) + 0.30 × $28.48 (strip) = **$26.35**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $26.38 |
| 95% | $26.46 |
| 100% | $26.48 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.07× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **52,226** | — |
| 10-year mean | 21,320 | 2.45× |
| 12-month FFA | 48,829 | 1.07× |
| Current spot | 29,350 | 1.78× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (54% of fleet value) | 26,472 | 1.65× |
| LR2 (37% of fleet value) | 82,624 | 2.99× |
| LR1 (9% of fleet value) | 82,624 | 2.99× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.98 | $21.17 | $24.36 | $27.55 | $30.75 |
| **-15%** | $18.98 | $22.17 | $25.36 | $28.55 | $31.74 |
| **+0%** | $19.97 | $23.16 | $26.35 | $29.54 | $32.73 |
| **+15%** | $20.96 | $24.15 | $27.34 | $30.53 | $33.72 |
| **+30%** | $21.95 | $25.14 | $28.34 | $31.53 | $34.72 |

_Current price $26.81. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$26.35** is -1.7% vs the current price ($26.81) and +5.4% vs the analyst target ($25.00). The current price implies the fleet earning a value-weighted blended **$52,226/day** (1.07× the current forward) — 2.4× the value-weighted 10-yr mean ($21,320, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
