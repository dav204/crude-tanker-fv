# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.34 | +38.0% | +67.3% | +96.6% | BUY→BUY | NAV>px→NAV>px | +59 | wide-spread |
| CCEC | 0.90× | 0.99 | +49.1% | +47.9% | +46.7% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| CAPT | 0.72× | 1.29 | -8.6% | +13.6% | +35.8% | TRIM/SHORT→BUY | $294,150→NAV>px | +44 | wide-spread |
| STNG | 0.73× | 1.62 | -8.5% | +12.2% | +32.9% | TRIM/SHORT→BUY | $125,003→NAV>px | +41 | wide-spread |
| GSL | 0.75× | 1.40 | -4.9% | +11.4% | +27.6% | HOLD→BUY | $121,953→NAV>px | +33 | wide-spread |
| ASC | 0.75× | 1.38 | -10.7% | +5.5% | +21.6% | TRIM/SHORT→BUY | $37,449→NAV>px | +32 | wide-spread |
| TRMD | 0.92× | 1.16 | -0.9% | +7.1% | +15.2% | HOLD→BUY | $65,797→$26,938 | +16 | wide-spread |
| NAT | 0.85× | 2.56 | -60.0% | -26.2% | +7.6% | TRIM/SHORT→BUY | $750,240→NAV>px | +68 | wide-spread |
| TNK | 0.91× | 1.43 | -14.4% | -5.0% | +4.3% | TRIM/SHORT→HOLD | $210,849→$14,694 | +19 | wide-spread |
| BRUT | 1.03× | 1.00 | +3.2% | +3.2% | +3.2% | HOLD→HOLD | $210,905→$210,894 | +0 | narrow-spread |
| HAFN | 1.03× | 1.66 | -40.3% | -18.9% | +2.4% | TRIM/SHORT→HOLD | $191,620→$59,049 | +43 | wide-spread |
| CMDB | 0.62× | 1.18 | -16.9% | -10.8% | -4.6% | TRIM/SHORT→HOLD | $34,947→$15,623 | +12 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.21 | -30.5% | -18.1% | -5.6% | TRIM/SHORT→TRIM/SHORT | $204,120→$34,978 | +25 | wide-spread |
| SBLK | 0.91× | 1.02 | -8.2% | -7.0% | -5.8% | TRIM/SHORT→TRIM/SHORT | $18,621→$14,328 | +2 | narrow-spread |
| MPCC | 1.04× | 1.22 | -27.6% | -18.0% | -8.5% | TRIM/SHORT→TRIM/SHORT | $214,851→$58,650 | +19 | wide-spread |
| DHT | 1.14× | 1.22 | -23.9% | -16.3% | -8.6% | TRIM/SHORT→TRIM/SHORT | $705,170→$396,570 | +15 | wide-spread |
| GNK | 0.95× | 1.10 | -20.9% | -16.3% | -11.8% | TRIM/SHORT→TRIM/SHORT | $41,661→$24,819 | +9 | narrow-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.59 | -43.3% | -29.6% | -15.9% | TRIM/SHORT→TRIM/SHORT | $569,780→$286,340 | +27 | wide-spread |
| LPG | 1.06× | 1.45 | -40.7% | -29.1% | -17.6% | TRIM/SHORT→TRIM/SHORT | $337,439→$144,194 | +23 | wide-spread |
| FRO | 1.33× | 1.26 | -40.1% | -31.0% | -22.0% | TRIM/SHORT→TRIM/SHORT | $755,089→$492,142 | +18 | wide-spread |
| FLNG | 1.44× | 0.89 | -5.3% | -13.7% | -22.0% | TRIM/SHORT→TRIM/SHORT | $286,002→$546,065 | -17 | wide-spread |
| SB | 1.13× | 0.81 | +8.5% | -7.5% | -23.5% | BUY→TRIM/SHORT | NAV>px→$57,717 | -32 | wide-spread |
| 2343 | 1.24× | 1.06 | -30.7% | -28.7% | -26.7% | TRIM/SHORT→TRIM/SHORT | $41,842→$37,563 | +4 | narrow-spread |
| BWLP | 1.27× | 1.16 | -39.9% | -34.4% | -28.9% | TRIM/SHORT→TRIM/SHORT | $255,029→$188,399 | +11 | wide-spread |
| ECO | 1.47× | 1.18 | -42.1% | -36.3% | -30.6% | TRIM/SHORT→TRIM/SHORT | $682,757→$535,358 | +12 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
