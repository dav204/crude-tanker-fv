# ASC — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $17.36
- **Model fair value:** $17.22
- **Analyst target:** $17.95

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — MR | 572.5 |
| Fleet value — Handysize | 181.9 |
| + Cash & equivalents | 48.1 |
| + Working capital (net) | 125.8 |
| − Total debt | 33.4 |
| − Lease liabilities | 1.6 |
| − Newbuild commitments | 183.6 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **709.7** |
| Diluted shares | 40,851,870 |
| **NAV / share** | **$17.37** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 29,300 | 29,300 | 0.898 | 0.599 | 0.584 |
| Q2 | 29,300 | 29,300 | 0.898 | 0.599 | 0.569 |
| Q3 | 29,250 | 29,250 | 0.896 | 0.598 | 0.553 |
| Q4 | 29,250 | 29,250 | 0.896 | 0.598 | 0.538 |
| Q5 | 25,000 | 25,000 | 0.690 | 0.460 | 0.404 |
| Q6 | 25,000 | 25,000 | 0.690 | 0.460 | 0.393 |
| Q7 | 25,000 | 25,000 | 0.690 | 0.460 | 0.383 |
| Q8 | 25,000 | 25,000 | 0.690 | 0.460 | 0.373 |
| Σ discounted DPS | | | | | 3.80 |
| Terminal value (NAV, q9) | | | | 16.53 | 13.07 |
| **DivStrip implied price** | | | | | **$16.87** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$29,275/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$29,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $29,250 / 10-yr mean $16,000 = **1.68×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $17.37 (NAV) + 0.30 × $16.87 (strip) = **$17.22**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 12.93 | 75% |
| Balance-sheet net | -0.76 | -4% |
| Discounted DPS (strip, 8-10q) | 1.14 | 7% |
| Discounted terminal (aged NAV) | 3.92 | 23% |
| **Blend FV** | **17.22** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.77 = **93%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $17.25 |
| 95% | $17.28 |
| 100% | $17.29 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.05× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **28,607** | — |
| 10-year mean | 16,000 | 1.79× |
| 12-month FFA | 27,226 | 1.05× |
| Current spot | 31,500 | 0.91× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (76% of fleet value) | 30,760 | 1.92× |
| Handysize (24% of fleet value) | 21,829 | 1.36× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $13.08 | $14.75 | $16.41 | $18.07 | $19.73 |
| **-15%** | $13.49 | $15.15 | $16.81 | $18.47 | $20.13 |
| **+0%** | $13.90 | $15.56 | $17.22 | $18.88 | $20.54 |
| **+15%** | $14.31 | $15.97 | $17.63 | $19.29 | $20.95 |
| **+30%** | $14.72 | $16.38 | $18.04 | $19.70 | $21.36 |

_Current price $17.36. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$17.22** is -0.8% vs the current price ($17.36) and -4.1% vs the analyst target ($17.95). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$28,607/day** (1.05× the current forward) — 1.8× the value-weighted 10-yr mean ($16,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
