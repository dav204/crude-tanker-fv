# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| CCEC | 0.90× | 1.00 | +55.6% | +54.8% | +54.0% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| TEN | 0.41× | 1.13 | +30.8% | +40.9% | +51.0% | BUY→BUY | NAV>px→NAV>px | +20 | wide-spread |
| STNG | 0.73× | 1.49 | -12.8% | +2.8% | +18.5% | TRIM/SHORT→BUY | $154,986→NAV>px | +31 | wide-spread |
| CAPT | 0.72× | 1.16 | -5.7% | +6.3% | +18.4% | TRIM/SHORT→BUY | $347,836→NAV>px | +24 | wide-spread |
| ASC | 0.75× | 1.34 | -14.5% | -0.6% | +13.3% | TRIM/SHORT→BUY | $45,684→NAV>px | +28 | wide-spread |
| GSL | 0.75× | 1.22 | -6.3% | +2.7% | +11.7% | TRIM/SHORT→BUY | $143,167→NAV>px | +18 | wide-spread |
| BRUT | 1.03× | 0.97 | +4.6% | +1.4% | -1.8% | HOLD→HOLD | $254,855→$327,035 | -6 | narrow-spread |
| TNK | 0.91× | 1.25 | -13.2% | -7.6% | -2.0% | TRIM/SHORT→HOLD | $259,053→$145,232 | +11 | wide-spread |
| TRMD | 0.92× | 1.06 | -8.1% | -5.4% | -2.7% | TRIM/SHORT→HOLD | $85,226→$71,138 | +5 | narrow-spread |
| NAT | 0.85× | 2.41 | -60.8% | -31.8% | -2.7% | TRIM/SHORT→HOLD | $898,495→$204,485 | +58 | wide-spread |
| MPCC | 1.04× | 1.19 | -28.6% | -20.4% | -12.2% | TRIM/SHORT→TRIM/SHORT | $226,840→$89,248 | +16 | wide-spread |
| SBLK | 0.91× | 1.00 | -13.2% | -13.0% | -12.8% | TRIM/SHORT→TRIM/SHORT | $25,530→$24,910 | +0 | narrow-spread |
| HAFN | 1.03× | 1.53 | -46.0% | -30.4% | -14.9% | TRIM/SHORT→TRIM/SHORT | $225,137→$118,566 | +31 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.28 | -47.0% | -31.4% | -15.8% | TRIM/SHORT→TRIM/SHORT | $325,779→$103,999 | +31 | wide-spread |
| GNK | 0.95× | 1.06 | -24.7% | -22.3% | -19.9% | TRIM/SHORT→TRIM/SHORT | $55,689→$42,553 | +5 | narrow-spread |
| DHT | 1.14× | 1.12 | -28.8% | -24.8% | -20.8% | TRIM/SHORT→TRIM/SHORT | $905,605→$732,692 | +8 | narrow-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.51 | -44.4% | -32.9% | -21.4% | TRIM/SHORT→TRIM/SHORT | $635,441→$391,159 | +23 | wide-spread |
| FLNG | 1.44× | 0.90 | -9.1% | -16.9% | -24.8% | TRIM/SHORT→TRIM/SHORT | $355,075→$609,975 | -16 | wide-spread |
| 2343 | 1.24× | 1.04 | -30.2% | -28.7% | -27.3% | TRIM/SHORT→TRIM/SHORT | $39,488→$36,459 | +3 | narrow-spread |
| SB | 1.13× | 0.82 | -1.9% | -15.8% | -29.6% | HOLD→TRIM/SHORT | NAV>px→$84,593 | -28 | wide-spread |
| CMDB | 0.84× | 0.84 | -19.3% | -24.5% | -29.7% | TRIM/SHORT→TRIM/SHORT | $41,984→$65,501 | -10 | wide-spread |
| LPG | 1.06× | 1.33 | -45.3% | -37.5% | -29.8% | TRIM/SHORT→TRIM/SHORT | $402,810→$262,531 | +15 | wide-spread |
| FRO | 1.33× | 1.19 | -42.9% | -36.7% | -30.5% | TRIM/SHORT→TRIM/SHORT | $886,430→$694,804 | +12 | wide-spread |
| BWLP | 1.27× | 1.16 | -44.0% | -38.8% | -33.7% | TRIM/SHORT→TRIM/SHORT | $296,190→$229,010 | +10 | wide-spread |
| ECO | 1.47× | 1.11 | -48.0% | -45.0% | -41.9% | TRIM/SHORT→TRIM/SHORT | $920,554→$831,571 | +6 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
