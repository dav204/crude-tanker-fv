# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.34 | +41.4% | +71.3% | +101.2% | BUY→BUY | NAV>px→NAV>px | +60 | wide-spread |
| CCEC | 0.90× | 0.99 | +49.1% | +47.9% | +46.7% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| CAPT | 0.72× | 1.29 | -8.1% | +14.2% | +36.5% | TRIM/SHORT→BUY | $341,733→NAV>px | +45 | wide-spread |
| STNG | 0.73× | 1.62 | -7.6% | +13.4% | +34.4% | TRIM/SHORT→BUY | $114,916→NAV>px | +42 | wide-spread |
| GSL | 0.75× | 1.40 | -4.8% | +11.5% | +27.8% | HOLD→BUY | $122,590→NAV>px | +33 | wide-spread |
| ASC | 0.75× | 1.38 | -10.2% | +6.1% | +22.4% | TRIM/SHORT→BUY | $37,312→NAV>px | +33 | wide-spread |
| TRMD | 0.92× | 1.16 | +0.9% | +9.1% | +17.3% | HOLD→BUY | $62,308→$25,510 | +16 | wide-spread |
| NAT | 0.85× | 2.56 | -58.8% | -24.0% | +10.7% | TRIM/SHORT→BUY | $754,682→NAV>px | +70 | wide-spread |
| TNK | 0.91× | 1.43 | -12.9% | -3.2% | +6.5% | TRIM/SHORT→BUY | $209,082→$14,571 | +19 | wide-spread |
| HAFN | 1.03× | 1.66 | -39.0% | -17.2% | +4.6% | TRIM/SHORT→HOLD | $182,362→$56,196 | +44 | wide-spread |
| BRUT | 1.03× | 1.00 | +1.0% | +1.0% | +1.0% | HOLD→HOLD | $233,540→$233,527 | +0 | narrow-spread |
| CMDB | 0.62× | 1.18 | -16.9% | -10.8% | -4.6% | TRIM/SHORT→HOLD | $34,947→$15,623 | +12 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.21 | -29.5% | -17.1% | -4.8% | TRIM/SHORT→TRIM/SHORT | $199,311→$34,303 | +25 | wide-spread |
| SBLK | 0.91× | 1.02 | -8.2% | -7.0% | -5.8% | TRIM/SHORT→TRIM/SHORT | $18,621→$14,328 | +2 | narrow-spread |
| MPCC | 1.04× | 1.22 | -27.0% | -17.3% | -7.6% | TRIM/SHORT→TRIM/SHORT | $212,543→$58,020 | +19 | wide-spread |
| DHT | 1.14× | 1.22 | -24.7% | -17.1% | -9.5% | TRIM/SHORT→TRIM/SHORT | $742,951→$417,816 | +15 | wide-spread |
| GNK | 0.95× | 1.10 | -20.9% | -16.3% | -11.8% | TRIM/SHORT→TRIM/SHORT | $41,661→$24,819 | +9 | narrow-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.59 | -43.0% | -29.3% | -15.5% | TRIM/SHORT→TRIM/SHORT | $597,965→$300,504 | +28 | wide-spread |
| LPG | 1.06× | 1.45 | -40.7% | -29.1% | -17.6% | TRIM/SHORT→TRIM/SHORT | $337,439→$144,194 | +23 | wide-spread |
| FRO | 1.33× | 1.26 | -40.1% | -31.0% | -22.0% | TRIM/SHORT→TRIM/SHORT | $817,770→$532,995 | +18 | wide-spread |
| FLNG | 1.44× | 0.89 | -5.3% | -13.7% | -22.0% | TRIM/SHORT→TRIM/SHORT | $286,002→$546,065 | -17 | wide-spread |
| SB | 1.13× | 0.81 | +8.5% | -7.5% | -23.5% | BUY→TRIM/SHORT | NAV>px→$57,717 | -32 | wide-spread |
| 2343 | 1.24× | 1.06 | -30.7% | -28.7% | -26.7% | TRIM/SHORT→TRIM/SHORT | $41,842→$37,563 | +4 | narrow-spread |
| BWLP | 1.27× | 1.16 | -39.9% | -34.4% | -28.9% | TRIM/SHORT→TRIM/SHORT | $255,029→$188,399 | +11 | wide-spread |
| ECO | 1.47× | 1.18 | -41.8% | -36.0% | -30.2% | TRIM/SHORT→TRIM/SHORT | $713,735→$559,648 | +12 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
