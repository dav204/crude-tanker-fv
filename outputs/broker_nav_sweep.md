# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.41× | 1.31 | +25.9% | +50.2% | +74.5% | BUY→BUY | NAV>px→NAV>px | +49 | wide-spread |
| CCEC | 0.90× | 0.98 | +55.6% | +52.0% | +48.5% | BUY→BUY | NAV>px→NAV>px | -7 | narrow-spread |
| CAPT | 0.72× | 1.32 | -5.8% | +18.5% | +42.8% | TRIM/SHORT→BUY | $349,105→NAV>px | +49 | wide-spread |
| STNG | 0.73× | 1.71 | -12.8% | +9.9% | +32.6% | TRIM/SHORT→BUY | $154,986→NAV>px | +45 | wide-spread |
| GSL | 0.75× | 1.41 | -6.3% | +10.4% | +27.2% | TRIM/SHORT→BUY | $143,167→NAV>px | +33 | wide-spread |
| ASC | 0.75× | 1.43 | -14.5% | +3.4% | +21.3% | TRIM/SHORT→BUY | $45,684→NAV>px | +36 | wide-spread |
| NAT | 0.85× | 2.87 | -60.8% | -22.3% | +16.2% | TRIM/SHORT→BUY | $898,495→NAV>px | +77 | wide-spread |
| TRMD | 0.92× | 1.24 | -8.1% | +3.0% | +14.0% | TRIM/SHORT→BUY | $85,226→$27,621 | +22 | wide-spread |
| TNK | 0.91× | 1.53 | -13.2% | -1.2% | +10.8% | TRIM/SHORT→BUY | $259,053→$16,098 | +24 | wide-spread |
| BRUT | 1.03× | 1.02 | +4.6% | +6.3% | +8.1% | HOLD→BUY | $255,698→$216,164 | +4 | narrow-spread |
| HAFN | 1.03× | 1.80 | -46.0% | -22.4% | +1.2% | TRIM/SHORT→HOLD | $225,137→$63,542 | +47 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.36 | -46.7% | -26.5% | -6.3% | TRIM/SHORT→TRIM/SHORT | $325,779→$39,107 | +40 | wide-spread |
| SBLK | 0.91× | 1.06 | -12.8% | -9.9% | -7.0% | TRIM/SHORT→TRIM/SHORT | $25,575→$14,718 | +6 | narrow-spread |
| DHT | 1.14× | 1.33 | -28.8% | -18.1% | -7.3% | TRIM/SHORT→TRIM/SHORT | $905,605→$440,963 | +22 | wide-spread |
| MPCC | 1.04× | 1.23 | -28.7% | -18.9% | -9.0% | TRIM/SHORT→TRIM/SHORT | $227,358→$62,433 | +20 | wide-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.69 | -44.4% | -28.8% | -13.2% | TRIM/SHORT→TRIM/SHORT | $635,441→$303,937 | +31 | wide-spread |
| GNK | 0.95× | 1.13 | -24.4% | -18.9% | -13.3% | TRIM/SHORT→TRIM/SHORT | $55,727→$25,834 | +11 | wide-spread |
| LPG | 1.06× | 1.58 | -45.3% | -31.6% | -17.9% | TRIM/SHORT→TRIM/SHORT | $402,810→$154,274 | +27 | wide-spread |
| FRO | 1.33× | 1.34 | -42.9% | -31.5% | -20.2% | TRIM/SHORT→TRIM/SHORT | $886,430→$535,430 | +23 | wide-spread |
| FLNG | 1.44× | 0.91 | -9.1% | -15.8% | -22.5% | TRIM/SHORT→TRIM/SHORT | $355,075→$573,836 | -13 | wide-spread |
| SB | 1.13× | 0.85 | -1.1% | -12.4% | -23.8% | HOLD→TRIM/SHORT | NAV>px→$64,803 | -23 | wide-spread |
| 2343 | 1.24× | 1.04 | -29.8% | -28.5% | -27.3% | TRIM/SHORT→TRIM/SHORT | $39,695→$37,033 | +2 | narrow-spread |
| ECO | 1.47× | 1.36 | -48.0% | -38.0% | -28.0% | TRIM/SHORT→TRIM/SHORT | $920,554→$628,692 | +20 | wide-spread |
| CMDB | 0.84× | 0.86 | -19.0% | -23.6% | -28.3% | TRIM/SHORT→TRIM/SHORT | $42,084→$63,041 | -9 | narrow-spread |
| BWLP | 1.27× | 1.23 | -44.0% | -36.6% | -29.3% | TRIM/SHORT→TRIM/SHORT | $296,620→$200,613 | +15 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
