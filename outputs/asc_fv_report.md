# ASC — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $18.46
- **Model fair value:** $17.26
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
| Q1 | 29,600 | 29,600 | 0.910 | 0.607 | 0.591 |
| Q2 | 29,600 | 29,600 | 0.910 | 0.607 | 0.576 |
| Q3 | 30,000 | 30,000 | 0.930 | 0.620 | 0.574 |
| Q4 | 30,000 | 30,000 | 0.930 | 0.620 | 0.559 |
| Q5 | 25,250 | 25,250 | 0.699 | 0.466 | 0.409 |
| Q6 | 25,250 | 25,250 | 0.699 | 0.466 | 0.399 |
| Q7 | 25,250 | 25,250 | 0.699 | 0.466 | 0.389 |
| Q8 | 25,250 | 25,250 | 0.699 | 0.466 | 0.379 |
| Σ discounted DPS | | | | | 3.88 |
| Terminal value (NAV, q9) | | | | 16.58 | 13.11 |
| **DivStrip implied price** | | | | | **$16.98** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$29,800/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$30,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $30,000 / 10-yr mean $16,000 = **1.72×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $17.37 (NAV) + 0.30 × $16.98 (strip) = **$17.26**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 12.93 | 75% |
| Balance-sheet net | -0.76 | -4% |
| Discounted DPS (strip, 8-10q) | 1.16 | 7% |
| Discounted terminal (aged NAV) | 3.93 | 23% |
| **Blend FV** | **17.26** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.77 = **93%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $17.28 |
| 95% | $17.31 |
| 100% | $17.32 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.44× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **39,759** | — |
| 10-year mean | 16,000 | 2.48× |
| 12-month FFA | 27,666 | 1.44× |
| Current spot | 31,500 | 1.26× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (76% of fleet value) | 42,825 | 2.68× |
| Handysize (24% of fleet value) | 30,107 | 1.88× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $13.11 | $14.77 | $16.43 | $18.09 | $19.75 |
| **-15%** | $13.52 | $15.18 | $16.84 | $18.50 | $20.16 |
| **+0%** | $13.93 | $15.60 | $17.26 | $18.92 | $20.58 |
| **+15%** | $14.35 | $16.01 | $17.67 | $19.33 | $20.99 |
| **+30%** | $14.76 | $16.42 | $18.08 | $19.74 | $21.40 |

_Current price $18.46. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$17.26** is -6.5% vs the current price ($18.46) and -3.9% vs the analyst target ($17.95). The current price implies the fleet earning a value-weighted blended **$39,759/day** (1.44× the current forward) — 2.5× the value-weighted 10-yr mean ($16,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
