# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.22 | +45.2% | +65.7% | +86.2% | BUY→BUY | NAV>px→NAV>px | +41 | wide-spread |
| CCEC | 0.90× | 0.99 | +50.7% | +48.9% | +47.1% | BUY→BUY | NAV>px→NAV>px | -4 | narrow-spread |
| STNG | 0.69× | 1.55 | -3.1% | +16.4% | +35.9% | HOLD→BUY | $71,456→NAV>px | +39 | wide-spread |
| GSL | 0.75× | 1.32 | +1.4% | +15.5% | +29.7% | HOLD→BUY | $16,874→NAV>px | +28 | wide-spread |
| ASC | 0.75× | 1.27 | +2.4% | +15.6% | +28.7% | HOLD→BUY | $21,597→NAV>px | +26 | wide-spread |
| TNK | 0.73× | 1.43 | +3.4% | +14.3% | +25.2% | HOLD→BUY | $8,968→NAV>px | +22 | wide-spread |
| TRMD | 0.82× | 1.15 | +8.1% | +16.5% | +24.9% | BUY→BUY | $37,928→NAV>px | +17 | wide-spread |
| CAPT | 0.69× | 1.17 | -4.0% | +10.0% | +24.1% | HOLD→BUY | $19,107→NAV>px | +28 | wide-spread |
| HAFN | 0.86× | 1.48 | -17.1% | +1.3% | +19.7% | TRIM/SHORT→BUY | $94,422→$7,648 | +37 | wide-spread |
| SBLK | 0.78× | 1.12 | +4.6% | +11.3% | +18.1% | HOLD→BUY | $13,931→NAV>px | +14 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.22 | -13.4% | +2.2% | +17.7% | TRIM/SHORT→BUY | $86,221→NAV>px | +31 | wide-spread |
| SB | 0.88× | 0.92 | +24.6% | +16.7% | +8.7% | BUY→BUY | NAV>px→NAV>px | -16 | wide-spread |
| LPG | 0.84× | 1.57 | -30.5% | -13.4% | +3.7% | TRIM/SHORT→HOLD | $223,619→NAV>px | +34 | wide-spread |
| CMDB | 0.62× | 0.89 | +14.2% | +8.9% | +3.6% | BUY→HOLD | NAV>px→$14,918 | -11 | wide-spread |
| GNK | 0.89× | 1.10 | -7.5% | -2.2% | +3.0% | TRIM/SHORT→HOLD | $32,091→$14,737 | +11 | wide-spread |
| NAT | 0.85× | 2.23 | -56.8% | -27.2% | +2.3% | TRIM/SHORT→HOLD | $459,263→NAV>px | +59 | wide-spread |
| BRUT | 0.72× | 1.00 | +0.7% | +1.4% | +2.1% | HOLD→HOLD | NAV>px→NAV>px | +1 | narrow-spread |
| 2343 | 0.98× | 1.19 | -17.5% | -9.9% | -2.3% | TRIM/SHORT→HOLD | $32,650→$18,346 | +15 | wide-spread |
| MPCC | 1.04× | 1.12 | -19.4% | -12.9% | -6.5% | TRIM/SHORT→TRIM/SHORT | $141,591→$48,690 | +13 | wide-spread |
| BWLP | 0.97× | 1.32 | -33.0% | -20.6% | -8.2% | TRIM/SHORT→TRIM/SHORT | $196,627→$61,101 | +25 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.59 | -41.1% | -26.9% | -12.7% | TRIM/SHORT→TRIM/SHORT | $379,056→$159,674 | +28 | wide-spread |
| DHT | 1.14× | 1.17 | -28.0% | -22.4% | -16.7% | TRIM/SHORT→TRIM/SHORT | $437,369→$266,381 | +11 | wide-spread |
| FLNG | 1.35× | 0.90 | -0.5% | -9.0% | -17.4% | HOLD→TRIM/SHORT | $207,648→$468,753 | -17 | wide-spread |
| ECO | 1.35× | 1.17 | -42.3% | -36.9% | -31.6% | TRIM/SHORT→TRIM/SHORT | $421,886→$319,860 | +11 | wide-spread |
| FRO | 1.37× | 1.13 | -41.8% | -36.8% | -31.8% | TRIM/SHORT→TRIM/SHORT | $440,847→$339,112 | +10 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
