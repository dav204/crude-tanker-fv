# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.29 | +48.2% | +75.1% | +102.0% | BUY→BUY | NAV>px→NAV>px | +54 | wide-spread |
| CCEC | 0.90× | 0.99 | +49.0% | +47.8% | +46.6% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| CAPT | 0.71× | 1.28 | -3.1% | +18.8% | +40.6% | HOLD→BUY | $212,404→NAV>px | +44 | wide-spread |
| STNG | 0.71× | 1.53 | -0.6% | +19.0% | +38.5% | HOLD→BUY | $75,519→NAV>px | +39 | wide-spread |
| BRUT | 0.86× | 0.92 | +62.7% | +45.6% | +28.4% | BUY→BUY | NAV>px→NAV>px | -34 | wide-spread |
| GSL | 0.75× | 1.40 | -5.3% | +11.2% | +27.7% | TRIM/SHORT→BUY | $131,422→NAV>px | +33 | wide-spread |
| TRMD | 0.86× | 1.17 | +6.7% | +16.1% | +25.5% | BUY→BUY | $51,677→$11,523 | +19 | wide-spread |
| ASC | 0.75× | 1.36 | -9.0% | +6.7% | +22.5% | TRIM/SHORT→BUY | $34,911→NAV>px | +31 | wide-spread |
| TNK | 0.80× | 1.56 | -6.8% | +6.8% | +20.4% | TRIM/SHORT→BUY | $143,965→NAV>px | +27 | wide-spread |
| HAFN | 0.92× | 1.51 | -19.9% | -1.1% | +17.7% | TRIM/SHORT→BUY | $117,987→$24,941 | +38 | wide-spread |
| NAT | 0.85× | 2.36 | -55.5% | -22.1% | +11.3% | TRIM/SHORT→BUY | $687,243→NAV>px | +67 | wide-spread |
| 2343 | 0.91× | 1.05 | +1.4% | +3.8% | +6.2% | HOLD→BUY | $14,262→$11,346 | +5 | narrow-spread |
| SB | 0.88× | 0.81 | +49.2% | +27.4% | +5.7% | BUY→BUY | NAV>px→NAV>px | -44 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.85× | 1.18 | -20.7% | -9.5% | +1.8% | TRIM/SHORT→BUY | $165,194→$28,497 | +22 | wide-spread |
| SBLK | 0.89× | 1.06 | -4.2% | -1.4% | +1.5% | HOLD→HOLD | $20,513→$13,545 | +6 | narrow-spread |
| CMDB | 0.62× | 1.04 | -2.4% | -0.9% | +0.7% | HOLD→HOLD | $19,208→$15,166 | +3 | narrow-spread |
| GNK | 0.92× | 1.14 | -17.0% | -10.2% | -3.3% | TRIM/SHORT→HOLD | $43,985→$19,908 | +14 | wide-spread |
| DHT | 1.08× | 1.17 | -16.7% | -10.3% | -3.9% | TRIM/SHORT→HOLD | $535,858→$287,365 | +13 | wide-spread |
| LPG | 0.96× | 1.52 | -37.3% | -23.3% | -9.2% | TRIM/SHORT→TRIM/SHORT | $296,366→$73,144 | +28 | wide-spread |
| MPCC | 1.04× | 1.24 | -31.4% | -20.3% | -9.2% | TRIM/SHORT→TRIM/SHORT | $255,556→$66,850 | +22 | wide-spread |
| INSW **(WHOLE-CO)** | 1.17× | 1.56 | -39.8% | -26.1% | -12.4% | TRIM/SHORT→TRIM/SHORT | $539,187→$258,594 | +27 | wide-spread |
| FRO | 1.31× | 1.21 | -36.1% | -27.9% | -19.8% | TRIM/SHORT→TRIM/SHORT | $660,065→$444,550 | +16 | wide-spread |
| BWLP | 1.13× | 1.32 | -42.3% | -31.7% | -21.1% | TRIM/SHORT→TRIM/SHORT | $277,962→$143,958 | +21 | wide-spread |
| FLNG | 1.43× | 0.91 | -7.7% | -14.8% | -21.9% | TRIM/SHORT→TRIM/SHORT | $328,633→$556,000 | -14 | wide-spread |
| ECO | 1.34× | 1.18 | -35.9% | -29.6% | -23.4% | TRIM/SHORT→TRIM/SHORT | $589,629→$439,183 | +12 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
