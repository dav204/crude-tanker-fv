# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.25 | +41.3% | +63.5% | +85.8% | BUY→BUY | NAV>px→NAV>px | +45 | wide-spread |
| CCEC | 0.90× | 0.97 | +60.4% | +53.6% | +46.9% | BUY→BUY | NAV>px→NAV>px | -13 | wide-spread |
| STNG | 0.69× | 1.50 | -0.6% | +19.2% | +39.0% | HOLD→BUY | $63,973→NAV>px | +40 | wide-spread |
| GSL | 0.75× | 1.42 | -8.5% | +9.6% | +27.7% | TRIM/SHORT→BUY | $118,655→NAV>px | +36 | wide-spread |
| TRMD | 0.82× | 1.18 | +5.6% | +15.0% | +24.5% | BUY→BUY | $42,981→NAV>px | +19 | wide-spread |
| CAPT | 0.69× | 1.15 | -1.0% | +11.6% | +24.2% | HOLD→BUY | NAV>px→NAV>px | +25 | wide-spread |
| TNK | 0.73× | 1.56 | -3.8% | +10.2% | +24.1% | HOLD→BUY | $54,688→NAV>px | +28 | wide-spread |
| ASC | 0.75× | 1.35 | -3.2% | +10.4% | +24.0% | HOLD→BUY | $30,382→NAV>px | +27 | wide-spread |
| HAFN | 0.86× | 1.51 | -18.8% | +0.3% | +19.3% | TRIM/SHORT→BUY | $99,382→$7,511 | +38 | wide-spread |
| SBLK | 0.78× | 1.16 | -0.5% | +8.7% | +17.8% | HOLD→BUY | $19,445→NAV>px | +18 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.22 | -12.7% | +2.5% | +17.7% | TRIM/SHORT→BUY | $83,165→NAV>px | +30 | wide-spread |
| SB | 0.88× | 0.89 | +29.4% | +19.1% | +8.9% | BUY→BUY | NAV>px→NAV>px | -20 | wide-spread |
| LPG | 0.84× | 1.52 | -34.4% | -15.3% | +3.7% | TRIM/SHORT→HOLD | $215,517→NAV>px | +38 | wide-spread |
| GNK | 0.89× | 1.09 | -6.5% | -1.7% | +3.1% | TRIM/SHORT→HOLD | $30,584→$14,327 | +10 | narrow-spread |
| CMDB | 0.62× | 0.95 | +7.7% | +5.4% | +3.1% | BUY→HOLD | $9,375→$15,105 | -5 | narrow-spread |
| NAT | 0.85× | 2.25 | -57.2% | -27.5% | +2.2% | TRIM/SHORT→HOLD | $466,586→NAV>px | +59 | wide-spread |
| BRUT | 0.72× | 0.98 | +8.1% | +4.5% | +0.9% | BUY→HOLD | NAV>px→NAV>px | -7 | narrow-spread |
| 2343 | 0.98× | 1.06 | -7.2% | -4.4% | -1.5% | TRIM/SHORT→HOLD | $22,126→$17,382 | +6 | narrow-spread |
| MPCC | 1.04× | 1.12 | -19.8% | -13.2% | -6.6% | TRIM/SHORT→TRIM/SHORT | $144,987→$49,217 | +13 | wide-spread |
| BWLP | 0.97× | 1.38 | -36.3% | -22.4% | -8.4% | TRIM/SHORT→TRIM/SHORT | $222,333→$63,037 | +28 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.65 | -43.3% | -28.2% | -13.1% | TRIM/SHORT→TRIM/SHORT | $408,978→$165,706 | +30 | wide-spread |
| DHT | 1.14× | 1.18 | -29.0% | -23.0% | -17.0% | TRIM/SHORT→TRIM/SHORT | $446,788→$265,483 | +12 | wide-spread |
| FLNG | 1.35× | 0.90 | -1.5% | -9.5% | -17.6% | HOLD→TRIM/SHORT | $224,647→$474,889 | -16 | wide-spread |
| FRO | 1.37× | 1.13 | -41.2% | -36.4% | -31.7% | TRIM/SHORT→TRIM/SHORT | $431,515→$335,842 | +9 | narrow-spread |
| ECO | 1.35× | 1.21 | -46.2% | -39.2% | -32.2% | TRIM/SHORT→TRIM/SHORT | $446,636→$316,639 | +14 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
