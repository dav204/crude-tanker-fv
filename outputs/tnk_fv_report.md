# TNK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $94.54
- **Model fair value:** $84.12
- **Analyst target:** $75.00

## Data validation warnings

- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 934.9 |
| Fleet value — Aframax | 794.4 |
| + Cash & equivalents | 1,211.6 |
| + Working capital (net) | 149.8 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 156.6 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,934.0** |
| Diluted shares | 34,680,112 |
| **NAV / share** | **$84.60** |
| NAV / share (ex yard discount) | $85.82 |
| Yard-discount impact / share | $-1.22 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 117,600 | 105,036 | 6.510 | 1.878 | 1.829 |
| Q2 | 117,600 | 105,036 | 6.510 | 1.878 | 1.782 |
| Q3 | 74,500 | 70,987 | 4.202 | 1.300 | 1.203 |
| Q4 | 74,500 | 70,987 | 4.202 | 1.300 | 1.172 |
| Q5 | 30,400 | 36,148 | 2.199 | 0.800 | 0.702 |
| Q6 | 30,400 | 36,148 | 2.199 | 0.800 | 0.684 |
| Q7 | 30,400 | 36,148 | 2.199 | 0.800 | 0.666 |
| Q8 | 30,400 | 36,148 | 2.199 | 0.800 | 0.649 |
| Σ discounted DPS | | | | | 8.69 |
| Terminal value (NAV, q9) | | | | 93.98 | 74.31 |
| **DivStrip implied price** | | | | | **$83.00** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$96,050/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$74,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $74,500 / 10-yr mean $27,747 = **2.16×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $84.60 (NAV) + 0.30 × $83.00 (strip) = **$84.12**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 34.90 | 41% |
| Balance-sheet net | 24.32 | 29% |
| Discounted DPS (strip, 8-10q) | 2.61 | 3% |
| Discounted terminal (aged NAV) | 22.29 | 27% |
| **Blend FV** | **84.12** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.90 = **97%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $84.74 |
| 95% | $84.90 |
| 100% | $84.96 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.31× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **192,341** | — |
| 10-year mean | 31,760 | 6.06× |
| 12-month FFA | 83,394 | 2.31× |
| Current spot | 106,289 | 1.81× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (54% of fleet value) | 221,530 | 7.98× |
| Aframax (46% of fleet value) | 157,989 | 4.33× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $72.92 | $77.32 | $81.73 | $86.13 | $90.54 |
| **-15%** | $74.11 | $78.52 | $82.92 | $87.33 | $91.74 |
| **+0%** | $75.31 | $79.72 | $84.12 | $88.53 | $92.93 |
| **+15%** | $76.51 | $80.91 | $85.32 | $89.72 | $94.13 |
| **+30%** | $77.70 | $82.11 | $86.51 | $90.92 | $95.32 |

_Current price $94.54. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$84.12** is -11.0% vs the current price ($94.54) and +12.2% vs the analyst target ($75.00). The current price implies the fleet earning a value-weighted blended **$192,341/day** (2.31× the current forward) — 6.1× the value-weighted 10-yr mean ($31,760, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
