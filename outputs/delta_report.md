# Pipeline Delta Report

- **This run:** 2026-09-19T15:16:06+00:00
- **Previous run:** 2026-09-18T21:51:05+00:00

## Headline changes (material moves)

- **BRUT:** position BUY (undervalued) → HOLD (fairly valued)

## §17 read-flip strobe — tape vs the flip boundary

> ⚡ **STROBE ZONE — 2 name(s) inside the ±2.0% deadband at the tape: CMDB (-1.71%), GNK (-1.54%).** The governed `read_flag` holds its state on the watchlist vintage, but at today's close the read sits close enough to its settling boundary that the next vintage rebase could restate it — and `read_flag` caps position size. This is the hazard the deadband exists for: surfaced, not acted on.

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (fair/rich) | $23.91 | $24.33 | parity · fair\|rich | **-1.71%** | -3.47% (@ $23.48) | ⚡ inside ±2.0% deadband |
| GNK | flips (cheap/fair) | $27.96 | $28.40 | hist · fair\|rich | **-1.54%** | -0.28% (@ $25.80) | ⚡ inside ±2.0% deadband |
| SBLK | flips (cheap/fair) | $32.48 | $33.22 | parity · cheap\|fair | -2.22% | -8.48% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/market_data/prices_daily.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $23.27 (+0.18) | $15.26 (no change) | $16.56 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +21.5pp (+0.4pp) |
| ECO | $84.95 (+0.34) | $39.87 (no change) | $44.15 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +20.0pp (+0.1pp) |
| FRO | $51.42 (+0.46) | $26.71 (no change) | $29.38 (no change) | $26.04 (no change) | TRIM/SHORT (overvalued) | +22.7pp (+0.4pp) |
| INSW | $111.15 (-0.06) | $37.95 (no change) | $61.81 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +31.2pp (no change) |
| TNK | $100.92 (+0.38) | $84.12 (no change) | $87.59 (no change) | $84.60 (no change) | TRIM/SHORT (overvalued) | +24.0pp (+0.3pp) |
| NAT | $8.25 (+0.09) | $2.95 (no change) | $3.24 (no change) | $2.76 (no change) | TRIM/SHORT (overvalued) | +77.0pp (+0.4pp) |
| FLNG | $32.42 (-0.09) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -13.5pp (-0.3pp) |
| CCEC | $21.66 (-0.68) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -7.1pp (-3.4pp) |
| STNG | $87.16 (-0.50) | $72.66 (no change) | $75.97 (no change) | $76.22 (no change) | TRIM/SHORT (overvalued) | +45.4pp (-0.5pp) |
| HAFN | $10.12 (+0.33) | $4.92 (no change) | $5.47 (no change) | $4.64 (no change) | TRIM/SHORT (overvalued) | +47.1pp (+1.4pp) |
| TRMD | $38.23 (+0.85) | $32.62 (no change) | $35.14 (no change) | $32.30 (no change) | TRIM/SHORT (overvalued) | +22.1pp (+1.8pp) |
| ASC | $19.05 (+0.08) | $17.26 (no change) | $16.28 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +35.8pp (+0.3pp) |
| TEN | $52.09 (-0.46) | $59.49 (no change) | $65.59 (no change) | $88.16 (no change) | BUY (undervalued) | +48.6pp (-1.0pp) |
| CMDB | $23.91 (-0.10) | $21.93 (no change) | $19.37 (no change) | $32.60 (no change) | TRIM/SHORT (overvalued) | -9.3pp (-0.3pp) |
| SBLK | $32.48 (+0.42) | $32.75 (no change) | $28.34 (no change) | $33.27 (no change) | TRIM/SHORT (overvalued) | +5.8pp (+1.0pp) |
| GNK | $27.96 (-0.14) | $25.19 (no change) | $21.14 (no change) | $25.37 (no change) | TRIM/SHORT (overvalued) | +11.1pp (-0.3pp) |
| CAPT | $19.73 (-0.02) | $17.09 (no change) | $18.57 (no change) | $17.32 (no change) | TRIM/SHORT (overvalued) | +48.6pp (-0.1pp) |
| MPCC | $3.03 (+0.03) | $2.33 (no change) | $2.16 (no change) | $2.15 (no change) | TRIM/SHORT (overvalued) | +19.7pp (+0.6pp) |
| GSL | $45.84 (-0.29) | $44.17 (no change) | $42.94 (no change) | $41.37 (no change) | TRIM/SHORT (overvalued) | +33.5pp (-0.4pp) |
| BRUT ⚑ | $5.27 (+0.03) | $4.71 (no change) | $5.51 (no change) | $4.92 (no change) | HOLD (fairly valued) ⟵ | +3.6pp (+0.6pp) |
| CMBT | $20.29 (+0.14) | $13.02 (no change) | $10.81 (no change) | $13.36 (no change) | TRIM/SHORT (overvalued) | +40.4pp (+0.3pp) |
| SB | $9.18 (+0.27) | $10.41 (no change) | $9.08 (no change) | $10.72 (no change) | HOLD (fairly valued) | -22.8pp (+2.8pp) |
| LPG | $58.15 (+0.48) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +27.4pp (+0.4pp) |
| BWLP | $25.95 (+0.40) | $15.48 (no change) | $14.52 (no change) | $15.83 (no change) | TRIM/SHORT (overvalued) | +14.7pp (+0.8pp) |
| 2343 | $0.53 (no change) | $0.41 (no change) | $0.37 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +2.5pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._