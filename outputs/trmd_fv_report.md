# TRMD — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $29.49
- **Model fair value:** $30.87
- **Analyst target:** $25.00

## Data validation warnings

- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 1,355.7 |
| Fleet value — LR1 | 342.3 |
| Fleet value — MR | 2,085.3 |
| + Cash & equivalents | 196.4 |
| + Working capital (net) | 254.9 |
| − Total debt | 1,081.8 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 31.2 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,121.6** |
| Diluted shares | 103,300,000 |
| **NAV / share** | **$30.22** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 22,000 | 22,000 | 2.188 | 1.641 | 1.599 |
| Q2 | 30,000 | 30,000 | 2.986 | 2.240 | 2.126 |
| Q3 | 28,000 | 28,000 | 2.712 | 2.034 | 1.881 |
| Q4 | 19,000 | 19,000 | 1.722 | 1.291 | 1.163 |
| Q5 | 18,000 | 18,000 | 1.530 | 1.148 | 1.007 |
| Q6 | 23,000 | 23,000 | 2.107 | 1.580 | 1.351 |
| Q7 | 26,000 | 26,000 | 2.383 | 1.787 | 1.489 |
| Q8 | 18,000 | 18,000 | 1.448 | 1.086 | 0.882 |
| Σ discounted DPS | | | | | 11.50 |
| Terminal value (NAV, q9) | | | | 26.40 | 20.88 |
| **DivStrip implied price** | | | | | **$32.38** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.67×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $30.22 (NAV) + 0.30 × $32.38 (strip) = **$30.87**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 25.64 | 83% |
| Balance-sheet net | -4.48 | -15% |
| Discounted DPS (strip, 8-10q) | 3.45 | 11% |
| Discounted terminal (aged NAV) | 6.26 | 20% |
| **Blend FV** | **30.87** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.64 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $30.89 |
| 95% | $30.98 |
| 100% | $31.00 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.79× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **38,395** | — |
| 10-year mean | 21,206 | 1.81× |
| 12-month FFA | 48,313 | 0.79× |
| Current spot | 34,816 | 1.10× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (55% of fleet value) | 19,669 | 1.23× |
| LR2 (36% of fleet value) | 61,392 | 2.22× |
| LR1 (9% of fleet value) | 61,392 | 2.22× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $22.37 | $25.61 | $28.86 | $32.10 | $35.34 |
| **-15%** | $23.38 | $26.62 | $29.86 | $33.10 | $36.34 |
| **+0%** | $24.38 | $27.62 | $30.87 | $34.11 | $37.35 |
| **+15%** | $25.39 | $28.63 | $31.87 | $35.11 | $38.35 |
| **+30%** | $26.39 | $29.64 | $32.88 | $36.12 | $39.36 |

_Current price $29.49. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$30.87** is +4.7% vs the current price ($29.49) and +23.5% vs the analyst target ($25.00). The current price implies the fleet earning a value-weighted blended **$38,395/day** (0.79× the current forward) — 1.8× the value-weighted 10-yr mean ($21,206, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
