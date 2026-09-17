# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.41× | 1.32 | +18.2% | +41.6% | +64.9% | BUY→BUY | NAV>px→NAV>px | +47 | wide-spread |
| CCEC | 0.90× | 0.99 | +53.2% | +50.5% | +47.8% | BUY→BUY | NAV>px→NAV>px | -5 | narrow-spread |
| CAPT | 0.72× | 1.32 | -10.3% | +13.6% | +37.6% | TRIM/SHORT→BUY | $357,794→NAV>px | +48 | wide-spread |
| STNG | 0.73× | 1.69 | -12.3% | +10.2% | +32.6% | TRIM/SHORT→BUY | $151,037→NAV>px | +45 | wide-spread |
| GSL | 0.75× | 1.41 | -5.8% | +10.8% | +27.3% | TRIM/SHORT→BUY | $134,387→NAV>px | +33 | wide-spread |
| ASC | 0.75× | 1.45 | -15.2% | +3.0% | +21.2% | TRIM/SHORT→BUY | $47,271→NAV>px | +36 | wide-spread |
| TRMD | 0.92× | 1.20 | -4.0% | +5.4% | +14.7% | HOLD→BUY | $73,723→$27,217 | +19 | wide-spread |
| NAT | 0.85× | 2.81 | -63.3% | -27.5% | +8.3% | TRIM/SHORT→BUY | $873,534→NAV>px | +72 | wide-spread |
| BRUT | 1.03× | 1.02 | +1.4% | +3.2% | +5.0% | HOLD→BUY | $257,563→$216,383 | +4 | narrow-spread |
| TNK | 0.91× | 1.54 | -18.1% | -6.7% | +4.7% | TRIM/SHORT→HOLD | $266,059→$16,302 | +23 | wide-spread |
| HAFN | 1.03× | 1.74 | -43.7% | -21.0% | +1.7% | TRIM/SHORT→HOLD | $210,822→$61,623 | +45 | wide-spread |
| SBLK | 0.91× | 1.03 | -8.4% | -6.9% | -5.4% | TRIM/SHORT→TRIM/SHORT | $19,641→$14,443 | +3 | narrow-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.37 | -47.6% | -27.1% | -6.7% | TRIM/SHORT→TRIM/SHORT | $332,100→$38,915 | +41 | wide-spread |
| DHT | 1.14× | 1.31 | -28.7% | -18.6% | -8.4% | TRIM/SHORT→TRIM/SHORT | $869,198→$432,900 | +20 | wide-spread |
| MPCC | 1.04× | 1.23 | -28.9% | -19.0% | -9.1% | TRIM/SHORT→TRIM/SHORT | $229,157→$62,715 | +20 | wide-spread |
| GNK | 0.95× | 1.11 | -21.9% | -16.8% | -11.8% | TRIM/SHORT→TRIM/SHORT | $44,614→$25,334 | +10 | wide-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.68 | -45.8% | -30.7% | -15.7% | TRIM/SHORT→TRIM/SHORT | $629,961→$302,468 | +30 | wide-spread |
| LPG | 1.06× | 1.58 | -45.3% | -31.6% | -17.9% | TRIM/SHORT→TRIM/SHORT | $403,895→$154,441 | +27 | wide-spread |
| FRO | 1.33× | 1.40 | -46.6% | -34.4% | -22.1% | TRIM/SHORT→TRIM/SHORT | $964,735→$561,237 | +25 | wide-spread |
| SB | 1.13× | 0.83 | +5.2% | -8.5% | -22.3% | BUY→TRIM/SHORT | NAV>px→$61,014 | -28 | wide-spread |
| FLNG | 1.44× | 0.91 | -8.5% | -15.5% | -22.5% | TRIM/SHORT→TRIM/SHORT | $343,203→$569,063 | -14 | wide-spread |
| 2343 | 1.24× | 1.05 | -30.0% | -28.3% | -26.7% | TRIM/SHORT→TRIM/SHORT | $40,561→$37,096 | +3 | narrow-spread |
| CMDB | 0.84× | 0.85 | -17.4% | -22.5% | -27.5% | TRIM/SHORT→TRIM/SHORT | $36,427→$52,520 | -10 | wide-spread |
| BWLP | 1.27× | 1.23 | -43.7% | -36.5% | -29.3% | TRIM/SHORT→TRIM/SHORT | $293,888→$199,811 | +14 | wide-spread |
| ECO | 1.47× | 1.37 | -50.7% | -40.8% | -31.0% | TRIM/SHORT→TRIM/SHORT | $933,268→$633,682 | +20 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
