# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.41× | 1.25 | +26.5% | +46.2% | +65.9% | BUY→BUY | NAV>px→NAV>px | +39 | wide-spread |
| CCEC | 0.90× | 0.99 | +52.3% | +49.9% | +47.6% | BUY→BUY | NAV>px→NAV>px | -5 | narrow-spread |
| CAPT | 0.72× | 1.30 | -8.4% | +14.7% | +37.7% | TRIM/SHORT→BUY | $320,282→NAV>px | +46 | wide-spread |
| STNG | 0.73× | 1.67 | -11.3% | +10.7% | +32.7% | TRIM/SHORT→BUY | $144,236→NAV>px | +44 | wide-spread |
| GSL | 0.75× | 1.41 | -6.1% | +10.6% | +27.2% | TRIM/SHORT→BUY | $140,032→NAV>px | +33 | wide-spread |
| ASC | 0.75× | 1.40 | -12.6% | +4.4% | +21.5% | TRIM/SHORT→BUY | $41,416→NAV>px | +34 | wide-spread |
| TRMD | 0.92× | 1.09 | +6.6% | +11.5% | +16.4% | BUY→BUY | $48,261→$26,322 | +10 | narrow-spread |
| NAT | 0.85× | 2.71 | -61.7% | -26.5% | +8.6% | TRIM/SHORT→BUY | $822,098→NAV>px | +70 | wide-spread |
| BRUT | 1.03× | 1.02 | +2.0% | +3.6% | +5.1% | HOLD→BUY | $250,393→$215,540 | +3 | narrow-spread |
| TNK | 0.91× | 1.51 | -17.0% | -6.1% | +4.9% | TRIM/SHORT→HOLD | $252,518→$15,908 | +22 | wide-spread |
| HAFN | 1.03× | 1.69 | -41.8% | -19.8% | +2.1% | TRIM/SHORT→HOLD | $199,650→$60,125 | +44 | wide-spread |
| SBLK | 0.91× | 1.01 | -6.7% | -6.0% | -5.3% | TRIM/SHORT→TRIM/SHORT | $16,893→$14,377 | +1 | narrow-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.32 | -44.5% | -25.6% | -6.7% | TRIM/SHORT→TRIM/SHORT | $295,440→$40,030 | +38 | wide-spread |
| DHT | 1.14× | 1.28 | -26.8% | -17.5% | -8.1% | TRIM/SHORT→TRIM/SHORT | $811,681→$420,161 | +19 | wide-spread |
| MPCC | 1.04× | 1.21 | -26.9% | -17.8% | -8.6% | TRIM/SHORT→TRIM/SHORT | $209,069→$59,567 | +18 | wide-spread |
| GNK | 0.95× | 1.09 | -20.4% | -16.0% | -11.6% | TRIM/SHORT→TRIM/SHORT | $41,274→$25,025 | +9 | narrow-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.60 | -43.2% | -29.2% | -15.2% | TRIM/SHORT→TRIM/SHORT | $577,573→$288,429 | +28 | wide-spread |
| LPG | 1.06× | 1.49 | -42.1% | -29.9% | -17.7% | TRIM/SHORT→TRIM/SHORT | $357,253→$147,249 | +24 | wide-spread |
| FRO | 1.33× | 1.35 | -44.1% | -32.9% | -21.7% | TRIM/SHORT→TRIM/SHORT | $889,706→$536,509 | +22 | wide-spread |
| SB | 1.13× | 0.81 | +11.5% | -5.3% | -22.0% | BUY→TRIM/SHORT | NAV>px→$57,257 | -33 | wide-spread |
| FLNG | 1.44× | 0.90 | -6.3% | -14.2% | -22.1% | TRIM/SHORT→TRIM/SHORT | $302,515→$552,704 | -16 | wide-spread |
| 2343 | 1.24× | 1.03 | -28.9% | -27.7% | -26.6% | TRIM/SHORT→TRIM/SHORT | $39,039→$36,647 | +2 | narrow-spread |
| CMDB | 0.84× | 0.87 | -18.8% | -23.2% | -27.7% | TRIM/SHORT→TRIM/SHORT | $38,942→$53,233 | -9 | narrow-spread |
| BWLP | 1.27× | 1.20 | -42.3% | -35.7% | -29.1% | TRIM/SHORT→TRIM/SHORT | $278,744→$195,363 | +13 | wide-spread |
| ECO | 1.47× | 1.30 | -47.4% | -38.9% | -30.4% | TRIM/SHORT→TRIM/SHORT | $835,499→$595,308 | +17 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
