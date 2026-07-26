# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.23 | +43.6% | +64.4% | +85.2% | BUY→BUY | NAV>px→NAV>px | +42 | wide-spread |
| CCEC | 0.90× | 0.98 | +53.8% | +49.4% | +45.1% | BUY→BUY | NAV>px→NAV>px | -9 | narrow-spread |
| STNG | 0.69× | 1.54 | -3.3% | +17.7% | +38.7% | HOLD→BUY | $75,231→NAV>px | +42 | wide-spread |
| GSL | 0.75× | 1.40 | -7.0% | +10.5% | +28.0% | TRIM/SHORT→BUY | $102,435→NAV>px | +35 | wide-spread |
| TRMD | 0.82× | 1.18 | +5.2% | +14.8% | +24.4% | BUY→BUY | $43,631→NAV>px | +19 | wide-spread |
| ASC | 0.75× | 1.28 | +1.4% | +12.9% | +24.3% | HOLD→BUY | $23,306→NAV>px | +23 | wide-spread |
| TNK | 0.73× | 1.57 | -3.2% | +10.2% | +23.7% | HOLD→BUY | $51,652→NAV>px | +27 | wide-spread |
| CAPT | 0.69× | 1.12 | +1.0% | +11.7% | +22.4% | HOLD→BUY | NAV>px→NAV>px | +21 | wide-spread |
| HAFN | 0.86× | 1.50 | -18.6% | +0.4% | +19.4% | TRIM/SHORT→BUY | $98,762→$7,528 | +38 | wide-spread |
| SBLK | 0.78× | 1.16 | +0.2% | +9.1% | +18.0% | HOLD→BUY | $18,761→NAV>px | +18 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.20 | -11.1% | +3.1% | +17.4% | TRIM/SHORT→BUY | $74,898→NAV>px | +29 | wide-spread |
| SB | 0.88× | 0.92 | +22.9% | +15.6% | +8.3% | BUY→BUY | NAV>px→NAV>px | -15 | wide-spread |
| LPG | 0.84× | 1.49 | -32.6% | -14.4% | +3.8% | TRIM/SHORT→HOLD | $201,081→NAV>px | +36 | wide-spread |
| CMDB | 0.62× | 0.94 | +8.6% | +5.9% | +3.3% | BUY→HOLD | $8,510→$15,026 | -5 | narrow-spread |
| GNK | 0.89× | 1.15 | -11.6% | -4.5% | +2.7% | TRIM/SHORT→HOLD | $39,889→$14,591 | +14 | wide-spread |
| NAT | 0.85× | 2.23 | -57.3% | -27.9% | +1.4% | TRIM/SHORT→HOLD | $458,136→NAV>px | +59 | wide-spread |
| 2343 | 0.98× | 1.08 | -9.0% | -5.3% | -1.5% | TRIM/SHORT→HOLD | $23,656→$17,397 | +7 | narrow-spread |
| BRUT | 0.72× | 0.97 | +8.4% | +2.2% | -4.1% | BUY→HOLD | NAV>px→NAV>px | -13 | wide-spread |
| MPCC | 1.04× | 1.13 | -20.6% | -13.7% | -6.8% | TRIM/SHORT→TRIM/SHORT | $151,957→$50,296 | +14 | wide-spread |
| BWLP | 0.97× | 1.34 | -34.2% | -21.2% | -8.3% | TRIM/SHORT→TRIM/SHORT | $205,800→$61,791 | +26 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.58 | -41.4% | -27.3% | -13.2% | TRIM/SHORT→TRIM/SHORT | $378,011→$159,463 | +28 | wide-spread |
| FLNG | 1.35× | 0.90 | -0.6% | -9.0% | -17.4% | HOLD→TRIM/SHORT | $208,188→$468,948 | -17 | wide-spread |
| DHT | 1.14× | 1.17 | -29.0% | -23.4% | -17.8% | TRIM/SHORT→TRIM/SHORT | $431,028→$261,985 | +11 | wide-spread |
| FRO | 1.37× | 1.12 | -42.0% | -37.3% | -32.6% | TRIM/SHORT→TRIM/SHORT | $430,349→$335,434 | +9 | narrow-spread |
| ECO | 1.35× | 1.17 | -44.5% | -38.7% | -32.8% | TRIM/SHORT→TRIM/SHORT | $410,092→$304,222 | +12 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
