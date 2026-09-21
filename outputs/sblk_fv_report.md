# SBLK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $32.48
- **Model fair value:** $32.81
- **Analyst target:** $34.50

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,557.8 |
| Fleet value — Pana | 1,414.3 |
| Fleet value — Supra-Ultra | 1,391.6 |
| + Cash & equivalents | 565.3 |
| + Working capital (net) | 84.2 |
| − Total debt | 1,036.6 |
| − Lease liabilities | 142.4 |
| − Newbuild commitments | 122.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,712.2** |
| Diluted shares | 111,585,370 |
| **NAV / share** | **$33.27** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 50,000 | 50,000 | 2.159 | 2.051 | 1.998 |
| Q2 | 46,875 | 46,875 | 2.204 | 2.094 | 1.988 |
| Q3 | 32,500 | 32,500 | 1.464 | 1.391 | 1.286 |
| Q4 | 34,667 | 34,667 | 1.514 | 1.438 | 1.296 |
| Q5 | 34,667 | 34,667 | 1.514 | 1.438 | 1.262 |
| Q6 | 34,666 | 34,666 | 1.514 | 1.438 | 1.230 |
| Q7 | 34,166 | 34,166 | 1.471 | 1.398 | 1.165 |
| Q8 | 33,666 | 33,666 | 1.433 | 1.361 | 1.105 |
| Σ discounted DPS | | | | | 11.33 |
| Terminal value (NAV, q9) | | | | 25.81 | 20.41 |
| **DivStrip implied price** | | | | | **$31.74** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$41,010/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$39,688/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $39,688 / 10-yr mean $23,650 = **1.60×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $33.27 (NAV) + 0.30 × $31.74 (strip) = **$32.81**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 27.37 | 83% |
| Balance-sheet net | -4.09 | -12% |
| Discounted DPS (strip, 8-10q) | 3.40 | 10% |
| Discounted terminal (aged NAV) | 6.12 | 19% |
| **Blend FV** | **32.81** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.64 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $32.75 |
| 95% | $32.81 |
| 100% | $32.83 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.94× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **25,530** | — |
| 10-year mean | 16,742 | 1.52× |
| 12-month FFA | 27,190 | 0.94× |
| Current spot | 33,379 | 0.76× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 38,507 | 1.63× |
| Pana (32% of fleet value) | 18,987 | 1.60× |
| Supra-Ultra (32% of fleet value) | 17,652 | 1.27× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $24.24 | $27.72 | $31.19 | $34.66 | $38.13 |
| **-15%** | $25.05 | $28.53 | $32.00 | $35.47 | $38.94 |
| **+0%** | $25.86 | $29.34 | $32.81 | $36.28 | $39.75 |
| **+15%** | $26.67 | $30.15 | $33.62 | $37.09 | $40.56 |
| **+30%** | $27.48 | $30.96 | $34.43 | $37.90 | $41.38 |

_Current price $32.48. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$32.81** is +1.0% vs the current price ($32.48) and -4.9% vs the analyst target ($34.50). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$25,530/day** (0.94× the current forward) — 1.5× the value-weighted 10-yr mean ($16,742, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
