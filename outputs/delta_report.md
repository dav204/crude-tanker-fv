# Pipeline Delta Report

- **This run:** 2026-09-18T21:05:24+00:00
- **Previous run:** 2026-09-18T20:00:05+00:00

## Headline changes (material moves)

- **No material changes.** All tickers within thresholds (|ΔFV%|≤10%, |Δspread|≤5pp, |ΔNAV%|≤5%) and no position flips.

## §17 read-flip strobe — tape vs the flip boundary

> ⚡ **STROBE ZONE — 2 name(s) inside the ±2.0% deadband at the tape: CMDB (-1.30%), GNK (-1.05%).** The governed `read_flag` holds its state on the watchlist vintage, but at today's close the read sits close enough to its settling boundary that the next vintage rebase could restate it — and `read_flag` caps position size. This is the hazard the deadband exists for: surfaced, not acted on.

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (fair/rich) | $24.01 | $24.33 | parity · fair\|rich | **-1.30%** | -3.47% (@ $23.48) | ⚡ inside ±2.0% deadband |
| GNK | flips (cheap/fair) | $28.10 | $28.40 | hist · fair\|rich | **-1.05%** | -0.28% (@ $25.80) | ⚡ inside ±2.0% deadband |
| SBLK | flips (cheap/fair) | $32.06 | $33.22 | parity · cheap\|fair | -3.48% | -8.48% (@ $30.40) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/forks.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $23.09 (no change) | $15.26 (no change) | $16.56 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +21.1pp (no change) |
| ECO | $84.61 (no change) | $39.87 (no change) | $44.15 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +19.9pp (no change) |
| FRO | $50.96 (no change) | $26.71 (no change) | $29.38 (no change) | $26.04 (no change) | TRIM/SHORT (overvalued) | +22.3pp (no change) |
| INSW | $111.21 (no change) | $37.95 (no change) | $61.81 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +31.2pp (no change) |
| TNK | $100.54 (no change) | $84.12 (no change) | $87.59 (no change) | $84.60 (no change) | TRIM/SHORT (overvalued) | +23.7pp (no change) |
| NAT | $8.16 (no change) | $2.95 (no change) | $3.24 (no change) | $2.76 (no change) | TRIM/SHORT (overvalued) | +76.6pp (no change) |
| FLNG | $32.51 (no change) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -13.2pp (no change) |
| CCEC | $22.34 (no change) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -3.7pp (no change) |
| STNG | $87.66 (no change) | $72.66 (no change) | $75.97 (no change) | $76.22 (no change) | TRIM/SHORT (overvalued) | +45.9pp (no change) |
| HAFN | $9.79 (no change) | $4.92 (no change) | $5.47 (no change) | $4.64 (no change) | TRIM/SHORT (overvalued) | +45.7pp (no change) |
| TRMD | $37.38 (no change) | $32.62 (no change) | $35.14 (no change) | $32.30 (no change) | TRIM/SHORT (overvalued) | +20.3pp (no change) |
| ASC | $18.97 (no change) | $17.26 (no change) | $16.28 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +35.5pp (no change) |
| TEN | $52.55 (no change) | $59.49 (no change) | $65.59 (no change) | $88.16 (no change) | BUY (undervalued) | +49.6pp (no change) |
| CMDB | $24.01 (no change) | $21.93 (no change) | $19.37 (no change) | $32.60 (no change) | TRIM/SHORT (overvalued) | -9.0pp (no change) |
| SBLK | $32.06 (no change) | $32.75 (no change) | $28.34 (no change) | $33.27 (no change) | TRIM/SHORT (overvalued) | +4.8pp (no change) |
| GNK | $28.10 (no change) | $25.19 (no change) | $21.14 (no change) | $25.37 (no change) | TRIM/SHORT (overvalued) | +11.4pp (no change) |
| CAPT | $19.75 (no change) | $17.09 (no change) | $18.57 (no change) | $17.32 (no change) | TRIM/SHORT (overvalued) | +48.7pp (no change) |
| MPCC | $3.00 (no change) | $2.33 (no change) | $2.16 (no change) | $2.15 (no change) | TRIM/SHORT (overvalued) | +19.1pp (no change) |
| GSL | $46.13 (no change) | $44.17 (no change) | $42.94 (no change) | $41.37 (no change) | TRIM/SHORT (overvalued) | +33.9pp (no change) |
| BRUT | $5.24 (no change) | $4.71 (no change) | $5.51 (no change) | $4.92 (no change) | BUY (undervalued) | +3.0pp (no change) |
| CMBT | $20.15 (no change) | $13.02 (no change) | $10.81 (no change) | $13.36 (no change) | TRIM/SHORT (overvalued) | +40.1pp (no change) |
| SB | $8.91 (no change) | $10.41 (no change) | $9.08 (no change) | $10.72 (no change) | HOLD (fairly valued) | -25.6pp (no change) |
| LPG | $57.67 (no change) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +27.0pp (no change) |
| BWLP | $25.55 (no change) | $15.48 (no change) | $14.52 (no change) | $15.83 (no change) | TRIM/SHORT (overvalued) | +13.9pp (no change) |
| 2343 | $0.53 (no change) | $0.41 (no change) | $0.37 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +2.5pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._