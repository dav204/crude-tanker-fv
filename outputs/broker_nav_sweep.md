# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.41× | 1.13 | +45.1% | +56.3% | +67.5% | BUY→BUY | NAV>px→NAV>px | +22 | wide-spread |
| CCEC | 0.90× | 1.00 | +54.6% | +53.8% | +53.0% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| STNG | 0.73× | 1.49 | -6.4% | +10.4% | +27.2% | TRIM/SHORT→BUY | $111,437→NAV>px | +34 | wide-spread |
| CAPT | 0.72× | 1.16 | +0.7% | +13.5% | +26.4% | HOLD→BUY | $234,601→NAV>px | +26 | wide-spread |
| ASC | 0.75× | 1.34 | -7.5% | +7.5% | +22.6% | TRIM/SHORT→BUY | $31,172→NAV>px | +30 | wide-spread |
| GSL | 0.75× | 1.22 | -3.6% | +5.6% | +14.9% | HOLD→BUY | $102,874→NAV>px | +19 | wide-spread |
| TRMD | 0.92× | 1.06 | +2.1% | +5.1% | +8.1% | HOLD→BUY | $58,502→$44,414 | +6 | narrow-spread |
| NAT | 0.85× | 2.41 | -57.6% | -26.2% | +5.2% | TRIM/SHORT→BUY | $803,945→$109,935 | +63 | wide-spread |
| TNK | 0.91× | 1.25 | -7.3% | -1.4% | +4.6% | TRIM/SHORT→HOLD | $192,341→$78,519 | +12 | wide-spread |
| BRUT | 1.03× | 0.97 | +8.4% | +5.1% | +1.8% | BUY→HOLD | $213,747→$285,927 | -7 | narrow-spread |
| HAFN | 1.03× | 1.53 | -39.9% | -22.6% | -5.3% | TRIM/SHORT→TRIM/SHORT | $189,525→$82,954 | +35 | wide-spread |
| SBLK | 0.91× | 1.00 | -6.7% | -6.5% | -6.3% | TRIM/SHORT→TRIM/SHORT | $15,065→$14,445 | +0 | narrow-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.28 | -43.4% | -26.9% | -10.3% | TRIM/SHORT→TRIM/SHORT | $289,751→$67,969 | +33 | wide-spread |
| MPCC | 1.04× | 1.19 | -27.3% | -19.0% | -10.6% | TRIM/SHORT→TRIM/SHORT | $213,456→$75,864 | +17 | wide-spread |
| DHT | 1.14× | 1.12 | -22.2% | -17.8% | -13.4% | TRIM/SHORT→TRIM/SHORT | $712,916→$540,004 | +9 | narrow-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.51 | -39.4% | -26.9% | -14.4% | TRIM/SHORT→TRIM/SHORT | $543,938→$299,656 | +25 | wide-spread |
| GNK | 0.95× | 1.06 | -19.8% | -17.2% | -14.6% | TRIM/SHORT→TRIM/SHORT | $42,937→$29,815 | +5 | narrow-spread |
| FLNG | 1.44× | 0.90 | -4.8% | -13.0% | -21.2% | HOLD→TRIM/SHORT | $276,829→$531,729 | -16 | wide-spread |
| SB | 1.13× | 0.82 | +8.0% | -7.3% | -22.5% | BUY→TRIM/SHORT | NAV>px→$53,810 | -31 | wide-spread |
| LPG | 1.06× | 1.33 | -40.1% | -31.7% | -23.2% | TRIM/SHORT→TRIM/SHORT | $330,570→$190,291 | +17 | wide-spread |
| CMDB | 0.84× | 0.84 | -13.2% | -18.8% | -24.4% | TRIM/SHORT→TRIM/SHORT | $29,091→$52,641 | -11 | wide-spread |
| FRO | 1.33× | 1.19 | -38.2% | -31.5% | -24.8% | TRIM/SHORT→TRIM/SHORT | $766,008→$574,382 | +13 | wide-spread |
| 2343 | 1.24× | 1.04 | -28.4% | -27.0% | -25.5% | TRIM/SHORT→TRIM/SHORT | $38,262→$35,219 | +3 | narrow-spread |
| BWLP | 1.27× | 1.16 | -40.5% | -35.0% | -29.5% | TRIM/SHORT→TRIM/SHORT | $260,833→$193,653 | +11 | wide-spread |
| ECO | 1.47× | 1.11 | -43.3% | -40.0% | -36.7% | TRIM/SHORT→TRIM/SHORT | $794,493→$705,510 | +7 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
