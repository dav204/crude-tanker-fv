# TNK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $74.45
- **Model fair value:** $73.94
- **Analyst target:** $75.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 721.7 |
| Fleet value — Aframax | 795.6 |
| Fleet value — VLCC | 73.3 |
| + Cash & equivalents | 996.2 |
| + Working capital (net) | 97.3 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,684.0** |
| Diluted shares | 34,643,858 |
| **NAV / share** | **$77.47** |
| NAV / share (ex yard discount) | $78.82 |
| Yard-discount impact / share | $-1.35 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Aframax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 68,400 | 5.086 | 1.521 | 1.482 |
| Q2 | 88,000 | 78,540 | 6.123 | 1.781 | 1.690 |
| Q3 | 82,000 | 73,860 | 5.671 | 1.668 | 1.542 |
| Q4 | 64,000 | 59,820 | 4.247 | 1.312 | 1.182 |
| Q5 | 59,000 | 55,920 | 3.832 | 1.208 | 1.060 |
| Q6 | 70,000 | 64,500 | 4.782 | 1.445 | 1.236 |
| Q7 | 74,000 | 67,620 | 5.051 | 1.513 | 1.260 |
| Q8 | 56,000 | 53,580 | 3.613 | 1.153 | 0.936 |
| Σ discounted DPS | | | | | 10.39 |
| Terminal value (NAV, q9) | | | | 69.95 | 55.31 |
| **DivStrip implied price** | | | | | **$65.70** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **2.15×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $77.47 (NAV) + 0.30 × $65.70 (strip) = **$73.94**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $79.62 |
| 95% | $81.17 |
| 100% | $81.69 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.19× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **100,249** | — |
| 10-year mean | 28,238 | 3.55× |
| 12-month FFA | 84,348 | 1.19× |
| Current spot | 74,317 | 1.35× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Aframax (50% of fleet value) | 91,814 | 3.33× |
| Suezmax (45% of fleet value) | 101,025 | 3.64× |
| VLCC (5% of fleet value) | 184,222 | 4.61× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $64.89 | $69.01 | $73.14 | $77.26 | $81.38 |
| **-15%** | $65.29 | $69.41 | $73.54 | $77.66 | $81.79 |
| **+0%** | $65.69 | $69.82 | $73.94 | $78.07 | $82.19 |
| **+15%** | $66.10 | $70.22 | $74.35 | $78.47 | $82.60 |
| **+30%** | $66.50 | $70.63 | $74.75 | $78.87 | $83.00 |

_Current price $74.45. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$73.94** is -0.7% vs the current price ($74.45) and -1.4% vs the analyst target ($75.00). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$100,249/day** (1.19× the current forward) — 3.6× the value-weighted 10-yr mean ($28,238, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
