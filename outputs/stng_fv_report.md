# STNG — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $76.49
- **Model fair value:** $75.86
- **Analyst target:** $94.00

## Data validation warnings

- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 2,081.7 |
| Fleet value — MR | 1,211.8 |
| Fleet value — Handymax | 205.3 |
| + Cash & equivalents | 984.3 |
| + Working capital (net) | 163.3 |
| − Total debt | 589.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 572.8 |
| + Newbuild advances | 69.1 |
| **= NAV total** | **3,858.6** |
| Diluted shares | 50,025,865 |
| **NAV / share** | **$77.13** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LR2, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 69,375 | 3.812 | 0.450 | 0.438 |
| Q2 | 88,000 | 80,750 | 5.163 | 0.450 | 0.427 |
| Q3 | 82,000 | 75,500 | 4.688 | 0.450 | 0.416 |
| Q4 | 64,000 | 59,750 | 2.999 | 0.450 | 0.405 |
| Q5 | 59,000 | 55,375 | 2.661 | 0.450 | 0.395 |
| Q6 | 70,000 | 65,000 | 3.649 | 0.450 | 0.385 |
| Q7 | 74,000 | 68,500 | 4.112 | 0.450 | 0.375 |
| Q8 | 56,000 | 52,750 | 2.511 | 0.450 | 0.365 |
| Σ discounted DPS | | | | | 3.21 |
| Terminal value (NAV, q9) | | | | 88.12 | 69.67 |
| **DivStrip implied price** | | | | | **$72.88** |

_FFA spot is the LR2 forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **1.77×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $77.13 (NAV) + 0.30 × $72.88 (strip) = **$75.86**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 48.96 | 65% |
| Balance-sheet net | 5.03 | 7% |
| Discounted DPS (strip, 8-10q) | 0.96 | 1% |
| Discounted terminal (aged NAV) | 20.90 | 28% |
| **Blend FV** | **75.86** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.96 = **99%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $76.62 |
| 95% | $76.76 |
| 100% | $76.81 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.06× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **59,337** | — |
| 10-year mean | 22,902 | 2.59× |
| 12-month FFA | 55,986 | 1.06× |
| Current spot | 39,646 | 1.50× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| LR2 (59% of fleet value) | 81,874 | 2.97× |
| MR (35% of fleet value) | 26,231 | 1.64× |
| Handymax (6% of fleet value) | 26,231 | 1.64× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $60.29 | $66.49 | $72.69 | $78.89 | $85.08 |
| **-15%** | $61.87 | $68.07 | $74.27 | $80.47 | $86.67 |
| **+0%** | $63.46 | $69.66 | $75.86 | $82.06 | $88.26 |
| **+15%** | $65.04 | $71.24 | $77.44 | $83.64 | $89.84 |
| **+30%** | $66.63 | $72.83 | $79.03 | $85.23 | $91.43 |

_Current price $76.49. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$75.86** is -0.8% vs the current price ($76.49) and -19.3% vs the analyst target ($94.00). The current price implies the fleet earning a value-weighted blended **$59,337/day** (1.06× the current forward) — 2.6× the value-weighted 10-yr mean ($22,902, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
