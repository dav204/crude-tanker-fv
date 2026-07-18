# Pipeline Delta Report

- **This run:** 2026-07-18T20:21:53+00:00
- **Previous run:** 2026-07-18T20:07:52+00:00

## Headline changes (material moves)

- **No material changes.** All tickers within thresholds (|ΔFV%|≤10%, |Δspread|≤5pp, |ΔNAV%|≤5%) and no position flips.

## Input files changed since last run

- `inputs/market_data/transactions/post_panamax.yaml` (new)
- `inputs/reweight_triggers.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $17.41 (no change) | $14.68 (no change) | $13.10 (no change) | $13.58 (no change) | TRIM/SHORT (overvalued) | +7.7pp (no change) |
| ECO | $53.88 (no change) | $37.19 (no change) | $32.10 (no change) | $34.42 (no change) | TRIM/SHORT (overvalued) | +8.2pp (no change) |
| FRO | $36.49 (no change) | $26.41 (no change) | $22.80 (no change) | $24.11 (no change) | TRIM/SHORT (overvalued) | +5.6pp (no change) |
| INSW | $86.76 (no change) | $38.50 (no change) | $54.12 (no change) | $52.48 (no change) | TRIM/SHORT (overvalued) | +25.1pp (no change) |
| TNK | $70.07 (no change) | $79.61 (no change) | $73.35 (no change) | $77.73 (no change) | HOLD (fairly valued) | +20.3pp (no change) |
| NAT | $6.05 (no change) | $3.14 (no change) | $2.76 (no change) | $2.85 (no change) | TRIM/SHORT (overvalued) | +56.3pp (no change) |
| FLNG | $30.67 (no change) | $28.16 (no change) | $30.67 (no change) | $28.45 (no change) | HOLD (fairly valued) | -17.4pp (no change) |
| CCEC | $22.19 (no change) | $32.08 (no change) | $35.91 (no change) | $28.10 (no change) | BUY (undervalued) | -14.6pp (no change) |
| STNG | $76.49 (no change) | $75.86 (no change) | $76.87 (no change) | $77.13 (no change) | HOLD (fairly valued) | +38.6pp (no change) |
| HAFN | $7.25 (no change) | $5.99 (no change) | $6.23 (no change) | $5.57 (no change) | TRIM/SHORT (overvalued) | +34.5pp (no change) |
| TRMD | $28.45 (no change) | $30.94 (no change) | $31.87 (no change) | $30.30 (no change) | BUY (undervalued) | +13.5pp (no change) |
| ASC | $15.40 (no change) | $16.77 (no change) | $16.85 (no change) | $17.82 (no change) | BUY (undervalued) | +15.5pp (no change) |
| TEN | $37.62 (no change) | $59.78 (no change) | $56.56 (no change) | $87.57 (no change) | BUY (undervalued) | +35.6pp (no change) |
| CMDB | $18.81 (no change) | $20.98 (no change) | $20.55 (no change) | $32.10 (no change) | BUY (undervalued) | -5.6pp (no change) |
| SBLK | $24.90 (no change) | $29.16 (no change) | $28.35 (no change) | $30.13 (no change) | BUY (undervalued) | +6.1pp (no change) |
| GNK | $24.12 (no change) | $24.65 (no change) | $23.82 (no change) | $25.48 (no change) | HOLD (fairly valued) | +5.6pp (no change) |
| CAPT | $12.72 (no change) | $16.03 (no change) | $13.14 (no change) | $15.49 (no change) | HOLD (fairly valued) | +19.1pp (no change) |
| MPCC | $2.48 (no change) | $2.21 (no change) | $2.06 (no change) | $2.04 (no change) | TRIM/SHORT (overvalued) | +11.1pp (no change) |
| GSL | $40.16 (no change) | $43.06 (no change) | $40.54 (no change) | $38.59 (no change) | HOLD (fairly valued) | +29.1pp (no change) |
| BRUT | $5.50 (no change) | $9.27 (no change) | $6.21 (no change) | $8.80 (no change) | BUY (undervalued) | -17.8pp (no change) |
| CMBT | $14.96 (no change) | $15.48 (no change) | $14.09 (no change) | $16.12 (no change) | TRIM/SHORT (overvalued) | +24.2pp (no change) |
| SB | $6.82 (no change) | $9.69 (-1.3%) | $9.47 (-1.4%) | $10.02 (-1.5%) | BUY (undervalued) | -28.6pp (+1.9pp) |
| LPG | $41.03 (no change) | $32.76 (no change) | $30.55 (no change) | $34.11 (no change) | TRIM/SHORT (overvalued) | +29.9pp (no change) |
| BWLP | $20.35 (no change) | $15.43 (no change) | $14.46 (no change) | $15.80 (no change) | TRIM/SHORT (overvalued) | +21.1pp (no change) |
| 2343 | $0.40 (no change) | $0.38 (no change) | $0.38 (no change) | $0.39 (no change) | HOLD (fairly valued) | +2.3pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._