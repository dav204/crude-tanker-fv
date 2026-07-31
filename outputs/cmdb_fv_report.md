# CMDB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $19.30
- **Model fair value:** $21.34
- **Analyst target:** $27.98

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 220.9 |
| Fleet value — Pana | 142.0 |
| Fleet value — Supra-Ultra | 326.3 |
| + Cash & equivalents | 258.5 |
| + Working capital (net) | 3.8 |
| − Total debt | 141.4 |
| − Lease liabilities | 20.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **789.5** |
| Diluted shares | 24,180,472 |
| **NAV / share** | **$32.65** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Supra-Ultra, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,100 | 19,100 | 1.270 | 0.000 | 0.000 |
| Q2 | 18,450 | 18,450 | 1.248 | 0.000 | 0.000 |
| Q3 | 15,075 | 15,075 | 0.890 | 0.000 | 0.000 |
| Q4 | 14,475 | 14,475 | 0.817 | 0.000 | 0.000 |
| Q5 | 13,875 | 13,875 | 0.744 | 0.000 | 0.000 |
| Q6 | 13,275 | 13,275 | 0.671 | 0.000 | 0.000 |
| Q7 | 12,975 | 12,975 | 0.632 | 0.000 | 0.000 |
| Q8 | 12,675 | 12,675 | 0.595 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 24.11 | 19.06 |
| **DivStrip implied price** | | | | | **$19.06** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$16,775/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$18,800/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $18,800 / 10-yr mean $13,930 = **1.45×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $22.86 (NAV) + 0.40 × $19.06 (strip) = **$21.34**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 17.10 | 80% |
| Balance-sheet net | 2.49 | 12% |
| §15 governance haircut | -5.88 | -28% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 7.62 | 36% |
| **Blend FV** | **21.34** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $22.11 |
| 95% | $22.26 |
| 100% | $22.30 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.42× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **9,375** | — |
| 10-year mean | 16,627 | 0.56× |
| 12-month FFA | 22,161 | 0.42× |
| Current spot | 24,521 | 0.38× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (47% of fleet value) | 7,096 | 0.51× |
| Cape (32% of fleet value) | 13,852 | 0.59× |
| Pana (21% of fleet value) | 7,646 | 0.64× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $16.85 | $18.56 | $20.28 | $22.00 | $23.71 |
| **-15%** | $17.38 | $19.09 | $20.81 | $22.53 | $24.24 |
| **+0%** | $17.91 | $19.62 | $21.34 | $23.05 | $24.77 |
| **+15%** | $18.43 | $20.15 | $21.87 | $23.58 | $25.30 |
| **+30%** | $18.96 | $20.68 | $22.39 | $24.11 | $25.83 |

_Current price $19.30. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$21.34** is +10.5% vs the current price ($19.30) and -23.7% vs the analyst target ($27.98). The current price implies the fleet earning a value-weighted blended **$9,375/day** (0.42× the current forward) — 0.6× the value-weighted 10-yr mean ($16,627, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
