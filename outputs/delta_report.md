# Pipeline Delta Report

- **This run:** 2026-07-02T14:53:03+00:00
- **Previous run:** 2026-07-02T14:44:16+00:00

## Headline changes (material moves)

- **TNK:** broker spread -9.6pp
- **STNG:** position HOLD (fairly valued) → BUY (undervalued); broker spread -7.9pp
- **ASC:** broker spread -12.0pp

## Input files changed since last run

- `inputs/market_data/prices_daily.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $16.53 (+0.13) | $14.95 (no change) | $15.77 (no change) | $13.88 (no change) | HOLD (fairly valued) | +7.1pp (+0.6pp) |
| ECO | $49.94 (-0.18) | $37.18 (no change) | $40.02 (no change) | $34.35 (no change) | TRIM/SHORT (overvalued) | +12.8pp (-0.2pp) |
| FRO | $34.70 (+0.20) | $26.54 (no change) | $28.82 (no change) | $24.22 (no change) | TRIM/SHORT (overvalued) | +12.5pp (+0.4pp) |
| INSW | $77.78 (+1.19) | $38.63 (no change) | $61.34 (no change) | $52.59 (no change) | TRIM/SHORT (overvalued) | +32.3pp (+1.0pp) |
| TNK ⚑ | $64.33 (-6.47) | $79.42 (no change) | $79.59 (no change) | $77.51 (no change) | BUY (undervalued) | +9.7pp (-9.6pp) |
| NAT | $5.56 (+0.02) | $3.09 (no change) | $3.33 (no change) | $2.79 (no change) | TRIM/SHORT (overvalued) | +61.3pp (+0.2pp) |
| FLNG | $28.62 (+0.56) | $28.16 (no change) | $30.67 (no change) | $28.45 (no change) | BUY (undervalued) | -24.5pp (+1.9pp) |
| CCEC | $21.68 (+0.33) | $32.08 (no change) | $35.91 (no change) | $28.10 (no change) | BUY (undervalued) | -17.4pp (+1.8pp) |
| STNG ⚑ | $69.53 (-6.07) | $76.13 (no change) | $77.13 (no change) | $77.47 (no change) | BUY (undervalued) ⟵ | +27.5pp (-7.9pp) |
| HAFN | $6.56 (-0.08) | $5.99 (no change) | $6.23 (no change) | $5.57 (no change) | TRIM/SHORT (overvalued) | +17.8pp (-0.9pp) |
| TRMD | $26.25 (+0.19) | $30.97 (no change) | $31.90 (no change) | $30.34 (no change) | BUY (undervalued) | +4.3pp (+0.8pp) |
| ASC ⚑ | $14.25 (-1.75) | $16.75 (no change) | $16.83 (no change) | $17.80 (no change) | BUY (undervalued) | +7.4pp (-12.0pp) |
| TEN | $35.37 (no change) | $61.29 (no change) | $65.49 (no change) | $88.70 (no change) | BUY (undervalued) | +27.6pp (no change) |
| CMDB | $18.21 (+0.65) | $20.43 (no change) | $20.43 (no change) | $31.33 (no change) | BUY (undervalued) | -6.5pp (+3.8pp) |
| SBLK | $24.81 (-0.16) | $28.34 (no change) | $28.37 (no change) | $29.34 (no change) | BUY (undervalued) | +3.2pp (-0.7pp) |
| GNK | $24.66 (-0.12) | $23.99 (no change) | $24.05 (no change) | $24.69 (no change) | HOLD (fairly valued) | +12.9pp (-0.4pp) |
| CAPT | $12.49 (-0.09) | $16.03 (no change) | $17.16 (no change) | $15.49 (no change) | BUY (undervalued) | +23.8pp (-0.9pp) |
| MPCC | $2.42 (-0.13) | $2.19 (no change) | $2.11 (no change) | $2.02 (no change) | TRIM/SHORT (overvalued) | +10.1pp (-3.5pp) |
| GSL | $37.78 (+0.18) | $43.00 (no change) | $40.59 (no change) | $38.59 (no change) | BUY (undervalued) | +24.4pp (+0.3pp) |
| BRUT | $5.17 (-0.04) | $9.27 (no change) | $10.24 (no change) | $8.80 (no change) | BUY (undervalued) | -35.8pp (-1.3pp) |
| CMBT | $14.05 (+0.06) | $15.26 (no change) | $16.07 (no change) | $15.87 (no change) | BUY (undervalued) | +19.9pp (+0.4pp) |
| SB | $6.31 (no change) | $9.87 (no change) | $9.68 (no change) | $10.12 (no change) | BUY (undervalued) | -40.5pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 3 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._