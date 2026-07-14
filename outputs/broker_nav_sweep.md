# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.20 | +45.1% | +63.9% | +82.6% | BUY→BUY | NAV>px→NAV>px | +37 | wide-spread |
| CCEC | 0.90× | 0.97 | +49.7% | +43.1% | +36.6% | BUY→BUY | NAV>px→NAV>px | -13 | wide-spread |
| GSL | 0.75× | 1.33 | -0.7% | +14.5% | +29.7% | HOLD→BUY | $36,896→NAV>px | +30 | wide-spread |
| STNG | 0.69× | 1.49 | -8.3% | +9.9% | +28.0% | TRIM/SHORT→BUY | $62,221→NAV>px | +36 | wide-spread |
| TNK | 0.73× | 1.42 | +3.5% | +14.2% | +24.9% | HOLD→BUY | $9,573→NAV>px | +21 | wide-spread |
| CAPT | 0.69× | 1.13 | -1.1% | +10.6% | +22.3% | HOLD→BUY | NAV>px→NAV>px | +23 | wide-spread |
| ASC | 0.75× | 1.21 | +2.8% | +11.7% | +20.6% | HOLD→BUY | $16,487→NAV>px | +18 | wide-spread |
| SBLK | 0.78× | 1.13 | +4.3% | +11.8% | +19.3% | HOLD→BUY | $15,171→NAV>px | +15 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.19 | -10.2% | +4.0% | +18.2% | TRIM/SHORT→BUY | $73,724→NAV>px | +28 | wide-spread |
| TRMD | 0.82× | 1.13 | -0.7% | +6.1% | +13.0% | HOLD→BUY | $33,189→NAV>px | +14 | wide-spread |
| SB | 0.88× | 0.87 | +37.4% | +23.8% | +10.1% | BUY→BUY | NAV>px→NAV>px | -27 | wide-spread |
| HAFN | 0.86× | 1.45 | -23.4% | -7.1% | +9.3% | TRIM/SHORT→BUY | $88,595→$7,828 | +33 | wide-spread |
| LPG | 0.84× | 1.34 | -23.9% | -9.7% | +4.4% | TRIM/SHORT→HOLD | $139,786→NAV>px | +28 | wide-spread |
| GNK | 0.89× | 1.12 | -8.7% | -2.4% | +3.9% | TRIM/SHORT→HOLD | $35,366→$14,346 | +13 | wide-spread |
| CMDB | 0.62× | 1.01 | +2.8% | +3.1% | +3.4% | HOLD→HOLD | $15,989→$15,158 | +1 | narrow-spread |
| NAT | 0.85× | 2.15 | -55.4% | -26.8% | +1.9% | TRIM/SHORT→HOLD | $422,616→NAV>px | +57 | wide-spread |
| 2343 | 0.98× | 1.03 | -3.2% | -1.8% | -0.4% | HOLD→HOLD | $18,774→$16,594 | +3 | narrow-spread |
| BRUT | 0.72× | 0.96 | +12.0% | +3.6% | -4.9% | BUY→HOLD | NAV>px→NAV>px | -17 | wide-spread |
| MPCC | 1.04× | 1.11 | -17.8% | -11.9% | -6.0% | TRIM/SHORT→TRIM/SHORT | $130,005→$46,936 | +12 | wide-spread |
| BWLP | 0.97× | 1.25 | -28.0% | -17.9% | -7.7% | TRIM/SHORT→TRIM/SHORT | $161,521→$58,456 | +20 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.48 | -38.6% | -26.5% | -14.4% | TRIM/SHORT→TRIM/SHORT | $330,395→$150,506 | +24 | wide-spread |
| DHT | 1.14× | 1.08 | -22.9% | -19.9% | -16.9% | TRIM/SHORT→TRIM/SHORT | $327,678→$242,573 | +6 | narrow-spread |
| FLNG | 1.35× | 0.89 | -3.2% | -12.3% | -21.4% | HOLD→TRIM/SHORT | $169,874→$455,116 | -18 | wide-spread |
| FRO | 1.37× | 1.07 | -37.9% | -35.0% | -32.0% | TRIM/SHORT→TRIM/SHORT | $372,609→$315,826 | +6 | narrow-spread |
| ECO | 1.35× | 1.12 | -40.8% | -36.5% | -32.2% | TRIM/SHORT→TRIM/SHORT | $359,265→$286,422 | +9 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
