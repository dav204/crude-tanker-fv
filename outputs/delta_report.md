# Pipeline Delta Report

- **This run:** 2026-06-27T00:31:14+00:00
- **Previous run:** 2026-06-26T20:14:34+00:00

## Headline changes (material moves)

- **SBLK:** position HOLD (fairly valued) → BUY (undervalued)
- **CAPT:** broker spread -6.7pp
- **BRUT:** broker spread -7.4pp
- **CMBT:** position TRIM/SHORT (overvalued) → BUY (undervalued); broker spread +10.3pp

## Input files changed since last run

- `inputs/market_data/prices_daily.yaml` (modified)
- `inputs/watchlist.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $17.65 (-0.43) | $14.15 (no change) | $14.92 (no change) | $13.10 (no change) | TRIM/SHORT (overvalued) | +16.0pp (-1.7pp) |
| ECO | $49.88 (-2.00) | $36.78 (no change) | $39.59 (no change) | $33.88 (no change) | TRIM/SHORT (overvalued) | +13.6pp (-2.4pp) |
| FRO | $35.52 (-2.95) | $26.54 (no change) | $28.82 (no change) | $24.22 (no change) | TRIM/SHORT (overvalued) | +14.0pp (-4.8pp) |
| INSW | $79.51 (-1.98) | $38.63 (no change) | $61.34 (no change) | $52.59 (no change) | TRIM/SHORT (overvalued) | +33.7pp (-1.5pp) |
| TNK | $67.99 (-2.29) | $79.42 (no change) | $79.59 (no change) | $77.51 (no change) | BUY (undervalued) | +15.4pp (-3.2pp) |
| NAT | $5.85 (-0.41) | $2.51 (no change) | $2.78 (no change) | $2.07 (no change) | TRIM/SHORT (overvalued) | +74.6pp (-2.1pp) |
| FLNG | $29.48 (-0.48) | $28.16 (no change) | $30.67 (no change) | $28.45 (no change) | HOLD (fairly valued) | -21.8pp (-1.4pp) |
| CCEC | $20.71 (+0.12) | $32.08 (no change) | $35.91 (no change) | $28.10 (no change) | BUY (undervalued) | -23.0pp (+0.8pp) |
| STNG | $72.58 (-2.88) | $78.93 (no change) | $79.99 (no change) | $80.35 (no change) | BUY (undervalued) | +28.2pp (-3.7pp) |
| HAFN | $6.97 (-0.30) | $5.66 (no change) | $5.91 (no change) | $5.22 (no change) | TRIM/SHORT (overvalued) | +26.6pp (-2.7pp) |
| TRMD | $26.81 (-0.89) | $26.35 (no change) | $27.32 (no change) | $25.43 (no change) | HOLD (fairly valued) | +22.5pp (-2.6pp) |
| ASC | $15.12 (-0.81) | $15.09 (no change) | $15.15 (no change) | $15.93 (no change) | HOLD (fairly valued) | +24.5pp (-4.7pp) |
| TEN | $36.72 (-0.96) | $60.74 (no change) | $64.93 (no change) | $87.70 (no change) | BUY (undervalued) | +35.2pp (-3.9pp) |
| CMDB | $17.47 (-0.29) | $21.12 (no change) | $21.13 (no change) | $32.49 (no change) | BUY (undervalued) | -14.9pp (-1.8pp) |
| SBLK ⚑ | $24.40 (-0.93) | $25.68 (no change) | $25.76 (no change) | $26.57 (no change) | BUY (undervalued) ⟵ | +11.3pp (-3.5pp) |
| GNK | $23.57 (+0.12) | $25.30 (no change) | $25.41 (no change) | $26.27 (no change) | BUY (undervalued) | +3.0pp (+0.5pp) |
| CAPT ⚑ | $12.79 (-0.82) | $15.66 (no change) | $16.77 (no change) | $15.03 (no change) | BUY (undervalued) | +30.0pp (-6.7pp) |
| MPCC | $2.61 (+0.07) | $2.19 (no change) | $2.11 (no change) | $2.02 (no change) | TRIM/SHORT (overvalued) | +15.1pp (+1.8pp) |
| GSL | $37.79 (-0.30) | $43.00 (no change) | $40.59 (no change) | $38.59 (no change) | BUY (undervalued) | +24.5pp (-0.6pp) |
| BRUT ⚑ | $5.34 (-0.24) | $9.84 (no change) | $10.81 (no change) | $9.40 (no change) | BUY (undervalued) | -41.5pp (-7.4pp) |
| CMBT ⚑ | $14.10 (-1.86) | $14.69 (no change) | $15.66 (no change) | $15.26 (no change) | BUY (undervalued) ⟵ | +24.3pp (+10.3pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 3 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._