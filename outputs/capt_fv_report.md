# CAPT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $14.31
- **Model fair value:** $15.10
- **Analyst target:** $18.90

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 1,922.4 |
| Fleet value — Suezmax | 1,149.0 |
| Fleet value — Aframax | 294.8 |
| Fleet value — LR2 | 382.8 |
| + Cash & equivalents | 405.0 |
| + Working capital (net) | 13.0 |
| − Total debt | 217.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 1,880.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,070.0** |
| Diluted shares | 133,700,000 |
| **NAV / share** | **$15.48** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 179,650 | 179,650 | 0.587 | 0.264 | 0.258 |
| Q2 | 179,650 | 179,650 | 0.965 | 0.434 | 0.412 |
| Q3 | 105,700 | 105,700 | 0.627 | 0.282 | 0.261 |
| Q4 | 105,700 | 105,700 | 0.726 | 0.327 | 0.294 |
| Q5 | 48,850 | 48,850 | 0.310 | 0.140 | 0.123 |
| Q6 | 48,850 | 48,850 | 0.351 | 0.158 | 0.135 |
| Q7 | 48,850 | 48,850 | 0.405 | 0.182 | 0.152 |
| Q8 | 48,850 | 48,850 | 0.459 | 0.207 | 0.168 |
| Σ discounted DPS | | | | | 1.80 |
| Terminal value (NAV, q9) | | | | 15.70 | 12.41 |
| **DivStrip implied price** | | | | | **$14.22** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$142,675/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$105,700/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $105,700 / 10-yr mean $40,000 = **2.32×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $15.48 (NAV) + 0.30 × $14.22 (strip) = **$15.10**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.63 | 130% |
| Balance-sheet net | -8.79 | -58% |
| Discounted DPS (strip, 8-10q) | 0.54 | 4% |
| Discounted terminal (aged NAV) | 3.72 | 25% |
| **Blend FV** | **15.10** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.87 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.16 |
| 95% | $15.18 |
| 100% | $15.19 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.49× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **53,520** | — |
| 10-year mean | 34,702 | 1.54× |
| 12-month FFA | 110,339 | 0.49× |
| Current spot | 288,106 | 0.19× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (51% of fleet value) | 69,205 | 1.73× |
| Suezmax (31% of fleet value) | 42,915 | 1.55× |
| LR2 (10% of fleet value) | 27,005 | 0.98× |
| Aframax (8% of fleet value) | 27,005 | 0.74× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $9.49 | $12.06 | $14.64 | $17.21 | $19.79 |
| **-15%** | $9.72 | $12.30 | $14.87 | $17.45 | $20.02 |
| **+0%** | $9.95 | $12.53 | $15.10 | $17.68 | $20.25 |
| **+15%** | $10.18 | $12.76 | $15.33 | $17.91 | $20.49 |
| **+30%** | $10.42 | $12.99 | $15.57 | $18.14 | $20.72 |

_Current price $14.31. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.10** is +5.6% vs the current price ($14.31) and -20.1% vs the analyst target ($18.90). The current price implies the fleet earning a value-weighted blended **$53,520/day** (0.49× the current forward) — 1.5× the value-weighted 10-yr mean ($34,702, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).
