# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.19 | +50.4% | +68.1% | +85.9% | BUY→BUY | NAV>px→NAV>px | +36 | wide-spread |
| CCEC | 0.90× | 0.97 | +61.8% | +54.5% | +47.3% | BUY→BUY | NAV>px→NAV>px | -15 | wide-spread |
| STNG | 0.69× | 1.48 | +0.5% | +19.8% | +39.1% | HOLD→BUY | $59,337→NAV>px | +39 | wide-spread |
| GSL | 0.75× | 1.31 | +0.9% | +15.5% | +30.1% | HOLD→BUY | $21,682→NAV>px | +29 | wide-spread |
| TRMD | 0.82× | 1.12 | +12.0% | +18.8% | +25.6% | BUY→BUY | $30,419→NAV>px | +14 | wide-spread |
| TNK | 0.73× | 1.40 | +4.7% | +14.9% | +25.0% | HOLD→BUY | NAV>px→NAV>px | +20 | wide-spread |
| ASC | 0.75× | 1.18 | +9.4% | +17.2% | +24.9% | BUY→BUY | $12,385→NAV>px | +15 | wide-spread |
| CAPT | 0.69× | 1.10 | +3.3% | +12.9% | +22.4% | HOLD→BUY | NAV>px→NAV>px | +19 | wide-spread |
| HAFN | 0.86× | 1.43 | -14.1% | +3.1% | +20.4% | TRIM/SHORT→BUY | $86,362→$7,871 | +34 | wide-spread |
| SBLK | 0.78× | 1.05 | +13.8% | +16.9% | +20.0% | BUY→BUY | $5,782→NAV>px | +6 | narrow-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.16 | -5.8% | +6.3% | +18.5% | TRIM/SHORT→BUY | $56,513→NAV>px | +24 | wide-spread |
| SB | 0.88× | 0.86 | +38.9% | +24.6% | +10.3% | BUY→BUY | NAV>px→NAV>px | -29 | wide-spread |
| GNK | 0.89× | 1.05 | -1.2% | +1.6% | +4.4% | HOLD→HOLD | $23,026→$14,099 | +6 | narrow-spread |
| LPG | 0.84× | 1.36 | -25.5% | -10.6% | +4.3% | TRIM/SHORT→HOLD | $150,318→NAV>px | +30 | wide-spread |
| CMDB | 0.62× | 0.94 | +9.2% | +6.5% | +3.7% | BUY→HOLD | $8,328→$15,034 | -6 | narrow-spread |
| NAT | 0.85× | 2.11 | -54.4% | -26.3% | +1.9% | TRIM/SHORT→HOLD | $413,067→NAV>px | +56 | wide-spread |
| 2343 | 0.98× | 1.02 | -2.8% | -1.7% | -0.5% | HOLD→HOLD | $18,543→$16,762 | +2 | narrow-spread |
| BRUT | 0.72× | 0.96 | +12.8% | +3.9% | -5.0% | BUY→HOLD | NAV>px→NAV>px | -18 | wide-spread |
| MPCC | 1.04× | 1.10 | -16.9% | -11.4% | -5.9% | TRIM/SHORT→TRIM/SHORT | $123,507→$45,930 | +11 | wide-spread |
| BWLP | 0.97× | 1.26 | -28.9% | -18.3% | -7.8% | TRIM/SHORT→TRIM/SHORT | $167,334→$58,894 | +21 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.49 | -37.6% | -25.1% | -12.5% | TRIM/SHORT→TRIM/SHORT | $333,611→$150,513 | +25 | wide-spread |
| DHT | 1.14× | 1.11 | -24.8% | -20.9% | -17.1% | TRIM/SHORT→TRIM/SHORT | $354,792→$245,065 | +8 | narrow-spread |
| FLNG | 1.35× | 0.89 | +0.0% | -8.7% | -17.3% | HOLD→TRIM/SHORT | $198,475→$465,441 | -17 | wide-spread |
| FRO | 1.37× | 1.07 | -37.5% | -34.7% | -32.0% | TRIM/SHORT→TRIM/SHORT | $365,027→$312,546 | +6 | narrow-spread |
| ECO | 1.35× | 1.11 | -40.4% | -36.3% | -32.2% | TRIM/SHORT→TRIM/SHORT | $353,871→$285,119 | +8 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
