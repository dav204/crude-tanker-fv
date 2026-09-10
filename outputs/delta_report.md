# Pipeline Delta Report

- **This run:** 2026-09-10T03:39:04+00:00
- **Previous run:** 2026-09-10T03:36:18+00:00

## Headline changes (material moves)

- **DHT:** broker spread +5.8pp
- **TNK:** broker spread +7.5pp
- **STNG:** position HOLD (fairly valued) → TRIM/SHORT (overvalued); broker spread +6.7pp
- **HAFN:** broker spread +5.7pp
- **TRMD:** position BUY (undervalued) → HOLD (fairly valued); broker spread +9.9pp
- **TEN:** broker spread +24.9pp
- **GSL:** position BUY (undervalued) → HOLD (fairly valued); broker spread +11.1pp

## §17 read-flip strobe — tape vs the flip boundary

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (cheap/fair) | $23.48 | $24.33 | parity · fair\|rich | -3.48% | +6.96% (@ $17.25) | clear of the deadband |
| GNK | flips (cheap/fair) | $27.14 | $28.40 | hist · fair\|rich | -4.43% | -0.29% (@ $25.80) | clear of the deadband |
| SBLK | flips (cheap/fair) | $31.16 | $33.22 | parity · cheap\|fair | -6.20% | -8.48% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/market_data/ffa_forward_curve.yaml` (modified)
- `inputs/market_data/prices_daily.yaml` (modified)
- `inputs/market_data/twelve_month_tc.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT ⚑ | $21.20 (+1.80) | $15.32 (+0.4%) | $15.97 (-0.9%) | $15.01 (no change) | TRIM/SHORT (overvalued) | +15.2pp (+5.8pp) |
| ECO | $71.67 (+5.37) | $39.73 (-0.4%) | $41.71 (+0.5%) | $39.54 (no change) | TRIM/SHORT (overvalued) | +11.6pp (+4.1pp) |
| FRO | $47.21 (+3.41) | $26.58 (-0.5%) | $28.29 (no change) | $26.04 (no change) | TRIM/SHORT (overvalued) | +18.1pp (+3.9pp) |
| INSW | $104.62 (+5.32) | $37.59 (-0.9%) | $59.59 (+0.5%) | $54.64 (no change) | TRIM/SHORT (overvalued) | +27.6pp (+2.7pp) |
| TNK ⚑ | $96.31 (+8.11) | $83.23 (-1.1%) | $83.93 (+1.8%) | $84.60 (no change) | TRIM/SHORT (overvalued) | +19.3pp (+7.5pp) |
| NAT | $7.27 (+0.47) | $2.89 (-2.0%) | $3.00 (+3.1%) | $2.76 (no change) | TRIM/SHORT (overvalued) | +69.5pp (+4.1pp) |
| FLNG | $31.14 (-0.16) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -16.7pp (-0.5pp) |
| CCEC | $22.60 (-0.20) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -2.5pp (-1.0pp) |
| STNG ⚑ | $83.06 (+5.66) | $72.23 (-0.6%) | $76.73 (+1.0%) | $76.22 (no change) | TRIM/SHORT (overvalued) ⟵ | +42.0pp (+6.7pp) |
| HAFN ⚑ | $9.16 (+0.86) | $4.83 (-1.8%) | $5.59 (+2.2%) | $4.64 (no change) | TRIM/SHORT (overvalued) | +43.6pp (+5.7pp) |
| TRMD ⚑ | $35.46 (+3.66) | $32.14 (-1.5%) | $35.79 (+1.8%) | $32.30 (no change) | HOLD (fairly valued) ⟵ | +16.4pp (+9.9pp) |
| ASC | $18.23 (+0.53) | $17.22 (-0.2%) | $16.38 (+0.6%) | $17.37 (no change) | TRIM/SHORT (overvalued) | +32.5pp (+2.6pp) |
| TEN ⚑ | $44.32 (+7.18) | $59.21 (-0.5%) | $62.66 (+2.4%) | $88.16 (no change) | BUY (undervalued) | +59.8pp (+24.9pp) |
| CMDB | $23.48 (-0.47) | $21.83 (no change) | $19.52 (no change) | $32.60 (no change) | TRIM/SHORT (overvalued) | +12.3pp (-1.5pp) |
| SBLK | $31.16 (+0.76) | $32.67 (no change) | $28.59 (no change) | $33.27 (no change) | TRIM/SHORT (overvalued) | +2.4pp (+2.0pp) |
| GNK | $27.14 (+1.34) | $25.41 (no change) | $21.48 (no change) | $25.37 (no change) | TRIM/SHORT (overvalued) | +9.1pp (+3.8pp) |
| CAPT | $19.11 (+0.60) | $16.95 (-0.8%) | $17.56 (+0.6%) | $17.32 (no change) | TRIM/SHORT (overvalued) | +44.6pp (+2.8pp) |
| MPCC | $2.94 (+0.04) | $2.29 (no change) | $2.15 (no change) | $2.10 (no change) | TRIM/SHORT (overvalued) | +19.3pp (+0.7pp) |
| GSL ⚑ | $45.02 (+6.03) | $44.02 (no change) | $42.88 (no change) | $41.20 (no change) | HOLD (fairly valued) ⟵ | +32.6pp (+11.1pp) |
| BRUT | $5.07 (+0.04) | $4.70 (-0.2%) | $5.12 (-2.1%) | $4.92 (no change) | HOLD (fairly valued) | +0.0pp (+0.8pp) |
| CMBT | $19.35 (+1.05) | $15.94 (-0.3%) | $13.65 (+0.5%) | $16.54 (no change) | TRIM/SHORT (overvalued) | +24.7pp (+4.0pp) |
| SB | $8.36 (-0.16) | $10.42 (no change) | $9.07 (no change) | $10.72 (no change) | BUY (undervalued) | -32.0pp (-2.0pp) |
| LPG | $53.63 (+4.33) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +23.1pp (+4.9pp) |
| BWLP | $24.15 (+0.46) | $15.48 (no change) | $14.52 (no change) | $15.83 (no change) | TRIM/SHORT (overvalued) | +11.0pp (+1.1pp) |
| 2343 | $0.54 (no change) | $0.41 (no change) | $0.38 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +4.0pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._