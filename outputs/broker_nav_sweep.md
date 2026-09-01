# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.30 | +47.4% | +74.6% | +101.9% | BUY→BUY | NAV>px→NAV>px | +54 | wide-spread |
| CCEC | 0.90× | 1.00 | +48.3% | +47.4% | +46.4% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| CAPT | 0.72× | 1.17 | +6.7% | +22.3% | +37.8% | BUY→BUY | $63,532→NAV>px | +31 | wide-spread |
| STNG | 0.73× | 1.50 | -1.7% | +16.6% | +34.9% | HOLD→BUY | $81,099→NAV>px | +37 | wide-spread |
| GSL | 0.75× | 1.38 | -3.7% | +12.2% | +28.1% | HOLD→BUY | $106,820→NAV>px | +32 | wide-spread |
| ASC | 0.75× | 1.31 | -5.7% | +8.6% | +22.8% | TRIM/SHORT→BUY | $28,607→NAV>px | +28 | wide-spread |
| TRMD | 0.92× | 1.08 | +9.7% | +14.2% | +18.7% | BUY→BUY | $43,444→$24,848 | +9 | narrow-spread |
| NAT | 0.85× | 2.40 | -55.8% | -22.2% | +11.3% | TRIM/SHORT→BUY | $678,594→NAV>px | +67 | wide-spread |
| TNK | 0.91× | 1.26 | -5.4% | +1.0% | +7.3% | TRIM/SHORT→BUY | $130,174→$12,273 | +13 | wide-spread |
| HAFN | 1.03× | 1.55 | -34.0% | -14.2% | +5.7% | TRIM/SHORT→BUY | $159,436→$53,122 | +40 | wide-spread |
| BRUT | 1.03× | 0.99 | +3.6% | +2.4% | +1.3% | HOLD→HOLD | $203,062→$229,942 | -2 | narrow-spread |
| CMDB | 0.62× | 1.02 | -4.9% | -4.3% | -3.6% | HOLD→HOLD | $16,931→$15,108 | +1 | narrow-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.17 | -25.7% | -15.3% | -4.8% | TRIM/SHORT→TRIM/SHORT | $168,098→$35,260 | +21 | wide-spread |
| SBLK | 0.91× | 1.01 | -6.2% | -5.9% | -5.6% | TRIM/SHORT→TRIM/SHORT | $15,280→$14,279 | +1 | narrow-spread |
| MPCC | 1.04× | 1.19 | -24.8% | -16.0% | -7.1% | TRIM/SHORT→TRIM/SHORT | $192,190→$54,836 | +18 | wide-spread |
| DHT | 1.14× | 1.14 | -18.8% | -13.7% | -8.6% | TRIM/SHORT→TRIM/SHORT | $585,846→$383,020 | +10 | wide-spread |
| GNK | 0.95× | 1.06 | -17.1% | -14.3% | -11.6% | TRIM/SHORT→TRIM/SHORT | $34,013→$24,146 | +6 | narrow-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.50 | -39.7% | -27.3% | -14.9% | TRIM/SHORT→TRIM/SHORT | $536,654→$284,074 | +25 | wide-spread |
| LPG | 1.06× | 1.34 | -36.1% | -26.7% | -17.3% | TRIM/SHORT→TRIM/SHORT | $281,759→$135,608 | +19 | wide-spread |
| FRO | 1.33× | 1.20 | -36.0% | -28.6% | -21.3% | TRIM/SHORT→TRIM/SHORT | $715,733→$499,366 | +15 | wide-spread |
| FLNG | 1.44× | 0.90 | -6.4% | -14.3% | -22.2% | TRIM/SHORT→TRIM/SHORT | $304,350→$553,442 | -16 | wide-spread |
| SB | 1.13× | 0.82 | +6.7% | -8.3% | -23.4% | BUY→TRIM/SHORT | NAV>px→$59,090 | -30 | wide-spread |
| 2343 | 1.24× | 1.04 | -29.4% | -28.0% | -26.6% | TRIM/SHORT→TRIM/SHORT | $40,189→$37,148 | +3 | narrow-spread |
| BWLP | 1.27× | 1.16 | -39.6% | -34.3% | -28.9% | TRIM/SHORT→TRIM/SHORT | $252,777→$187,737 | +11 | wide-spread |
| ECO | 1.47× | 1.12 | -37.6% | -33.6% | -29.6% | TRIM/SHORT→TRIM/SHORT | $623,698→$524,309 | +8 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
