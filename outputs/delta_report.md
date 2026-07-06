# Pipeline Delta Report

- **This run:** 2026-07-06T18:18:04+00:00
- **Previous run:** 2026-07-03T13:42:41+00:00

## Headline changes (material moves)

- **No material changes.** All tickers within thresholds (|ΔFV%|≤10%, |Δspread|≤5pp, |ΔNAV%|≤5%) and no position flips.

## Input files changed since last run

- `inputs/notify.yaml` (new)
- `inputs/data_sources.yaml` (modified)
- `inputs/earnings_calendar.yaml` (modified)
- `inputs/market_data/ffa_forward_curve.yaml` (modified)
- `inputs/market_data/prices_daily.yaml` (modified)
- `inputs/market_data/spot_tce.yaml` (modified)
- `inputs/market_data/twelve_month_tc.yaml` (modified)
- `inputs/market_data/vessel_value_curves.yaml` (modified)
- `inputs/reweight_triggers.yaml` (modified)
- `inputs/rocketchat_sources.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $17.18 (no change) | $14.95 (no change) | $11.35 (no change) | $13.88 (no change) | TRIM/SHORT (overvalued) | +7.8pp (no change) |
| ECO | $53.11 (no change) | $37.18 (no change) | $25.73 (no change) | $34.35 (no change) | TRIM/SHORT (overvalued) | +12.9pp (no change) |
| FRO | $36.75 (no change) | $26.54 (no change) | $18.17 (no change) | $24.22 (no change) | TRIM/SHORT (overvalued) | +12.4pp (no change) |
| INSW | $82.40 (no change) | $38.63 (no change) | $48.00 (no change) | $52.59 (no change) | TRIM/SHORT (overvalued) | +29.6pp (no change) |
| TNK | $67.60 (no change) | $79.42 (no change) | $67.61 (no change) | $77.51 (no change) | HOLD (fairly valued) | +11.7pp (no change) |
| NAT | $5.81 (no change) | $3.09 (no change) | $2.25 (no change) | $2.79 (no change) | TRIM/SHORT (overvalued) | +49.7pp (no change) |
| FLNG | $29.29 (no change) | $28.16 (no change) | $29.19 (no change) | $28.45 (no change) | HOLD (fairly valued) | -21.6pp (no change) |
| CCEC | $21.60 (no change) | $32.08 (no change) | $33.50 (no change) | $28.10 (no change) | BUY (undervalued) | -17.2pp (no change) |
| STNG | $73.01 (no change) | $76.13 (no change) | $70.90 (no change) | $77.47 (no change) | HOLD (fairly valued) | +29.8pp (no change) |
| HAFN | $7.02 (no change) | $5.99 (no change) | $5.61 (no change) | $5.57 (no change) | TRIM/SHORT (overvalued) | +21.1pp (no change) |
| TRMD | $27.70 (no change) | $30.97 (no change) | $28.65 (no change) | $30.34 (no change) | HOLD (fairly valued) | +8.9pp (no change) |
| ASC | $14.86 (no change) | $16.75 (no change) | $16.28 (no change) | $17.80 (no change) | BUY (undervalued) | +11.5pp (no change) |
| TEN | $37.37 (no change) | $61.29 (no change) | $50.92 (no change) | $88.70 (no change) | BUY (undervalued) | +29.8pp (no change) |
| CMDB | $18.18 (no change) | $20.43 (no change) | $20.34 (no change) | $31.33 (no change) | BUY (undervalued) | -6.6pp (no change) |
| SBLK | $25.15 (+0.34) | $28.32 (no change) | $28.19 (no change) | $29.34 (no change) | BUY (undervalued) | +4.6pp (+1.4pp) |
| GNK | $24.50 (no change) | $23.85 (no change) | $23.56 (no change) | $24.69 (no change) | HOLD (fairly valued) | +12.1pp (no change) |
| CAPT | $13.68 (+0.40) | $16.03 (no change) | $10.07 (no change) | $15.49 (no change) | TRIM/SHORT (overvalued) | +26.5pp (+2.6pp) |
| MPCC | $2.52 (+0.08) | $2.21 (+0.9%) | $2.06 (-2.4%) | $2.04 (+1.0%) | TRIM/SHORT (overvalued) | +12.0pp (+1.3pp) |
| GSL | $38.11 (no change) | $43.06 (+0.1%) | $40.54 (-0.1%) | $38.59 (no change) | BUY (undervalued) | +25.1pp (no change) |
| BRUT | $5.32 (+0.03) | $9.27 (no change) | $3.12 (no change) | $8.80 (no change) | TRIM/SHORT (overvalued) | -24.1pp (+0.7pp) |
| CMBT | $14.56 (no change) | $15.19 (no change) | $13.35 (+0.1%) | $15.87 (no change) | TRIM/SHORT (overvalued) | +21.4pp (no change) |
| SB | $6.40 (no change) | $9.75 (no change) | $9.82 (no change) | $10.12 (no change) | BUY (undervalued) | -38.9pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 3 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._