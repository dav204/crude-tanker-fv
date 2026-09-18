# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.41× | 1.32 | +17.6% | +41.2% | +64.9% | BUY→BUY | NAV>px→NAV>px | +47 | wide-spread |
| CCEC | 0.90× | 0.99 | +50.8% | +49.0% | +47.1% | BUY→BUY | NAV>px→NAV>px | -4 | narrow-spread |
| CAPT | 0.72× | 1.32 | -10.0% | +13.8% | +37.6% | TRIM/SHORT→BUY | $352,168→NAV>px | +48 | wide-spread |
| STNG | 0.73× | 1.72 | -13.3% | +9.6% | +32.5% | TRIM/SHORT→BUY | $158,643→NAV>px | +46 | wide-spread |
| GSL | 0.75× | 1.42 | -6.9% | +10.1% | +27.0% | TRIM/SHORT→BUY | $152,261→NAV>px | +34 | wide-spread |
| ASC | 0.75× | 1.43 | -14.2% | +3.6% | +21.3% | TRIM/SHORT→BUY | $44,881→NAV>px | +35 | wide-spread |
| TRMD | 0.92× | 1.22 | -6.0% | +4.2% | +14.3% | TRIM/SHORT→BUY | $79,264→$27,411 | +20 | wide-spread |
| NAT | 0.85× | 2.84 | -63.7% | -27.7% | +8.2% | TRIM/SHORT→BUY | $885,636→NAV>px | +72 | wide-spread |
| BRUT | 1.03× | 1.01 | +2.1% | +3.6% | +5.1% | HOLD→BUY | $249,084→$215,386 | +3 | narrow-spread |
| TNK | 0.91× | 1.52 | -17.2% | -6.2% | +4.8% | TRIM/SHORT→HOLD | $255,080→$15,982 | +22 | wide-spread |
| HAFN | 1.03× | 1.75 | -44.2% | -21.3% | +1.6% | TRIM/SHORT→HOLD | $213,790→$62,021 | +46 | wide-spread |
| SBLK | 0.91× | 1.05 | -11.6% | -9.2% | -6.9% | TRIM/SHORT→TRIM/SHORT | $23,456→$14,666 | +5 | narrow-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.36 | -47.9% | -28.1% | -8.3% | TRIM/SHORT→TRIM/SHORT | $321,354→$39,241 | +40 | wide-spread |
| DHT | 1.14× | 1.32 | -29.3% | -18.9% | -8.5% | TRIM/SHORT→TRIM/SHORT | $888,176→$437,103 | +21 | wide-spread |
| MPCC | 1.04× | 1.22 | -27.9% | -18.4% | -8.9% | TRIM/SHORT→TRIM/SHORT | $219,618→$61,220 | +19 | wide-spread |
| GNK | 0.95× | 1.13 | -24.8% | -19.1% | -13.4% | TRIM/SHORT→TRIM/SHORT | $56,891→$25,913 | +11 | wide-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.69 | -46.1% | -30.9% | -15.7% | TRIM/SHORT→TRIM/SHORT | $636,044→$304,099 | +30 | wide-spread |
| LPG | 1.06× | 1.57 | -44.8% | -31.3% | -17.8% | TRIM/SHORT→TRIM/SHORT | $395,868→$153,204 | +27 | wide-spread |
| FRO | 1.33× | 1.34 | -43.5% | -32.5% | -21.6% | TRIM/SHORT→TRIM/SHORT | $872,079→$530,700 | +22 | wide-spread |
| FLNG | 1.44× | 0.91 | -9.3% | -16.0% | -22.6% | TRIM/SHORT→TRIM/SHORT | $359,932→$575,788 | -13 | wide-spread |
| SB | 1.13× | 0.84 | +1.9% | -10.9% | -23.7% | HOLD→TRIM/SHORT | NAV>px→$62,714 | -26 | wide-spread |
| 2343 | 1.24× | 1.04 | -29.8% | -28.5% | -27.3% | TRIM/SHORT→TRIM/SHORT | $39,695→$37,033 | +2 | narrow-spread |
| CMDB | 0.84× | 0.86 | -19.3% | -23.8% | -28.3% | TRIM/SHORT→TRIM/SHORT | $42,910→$63,258 | -9 | narrow-spread |
| BWLP | 1.27× | 1.22 | -43.2% | -36.2% | -29.2% | TRIM/SHORT→TRIM/SHORT | $287,706→$197,995 | +14 | wide-spread |
| ECO | 1.47× | 1.36 | -50.1% | -40.5% | -30.9% | TRIM/SHORT→TRIM/SHORT | $914,466→$626,302 | +19 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
