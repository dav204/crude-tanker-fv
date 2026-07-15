# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.24 | +42.0% | +63.6% | +85.2% | BUY→BUY | NAV>px→NAV>px | +43 | wide-spread |
| CCEC | 0.90× | 0.97 | +58.3% | +52.3% | +46.3% | BUY→BUY | NAV>px→NAV>px | -12 | wide-spread |
| STNG | 0.69× | 1.50 | -1.0% | +19.0% | +38.9% | HOLD→BUY | $65,353→NAV>px | +40 | wide-spread |
| GSL | 0.75× | 1.34 | -1.7% | +13.9% | +29.4% | HOLD→BUY | $46,961→NAV>px | +31 | wide-spread |
| TRMD | 0.82× | 1.15 | +8.4% | +16.7% | +24.9% | BUY→BUY | $37,275→NAV>px | +17 | wide-spread |
| ASC | 0.75× | 1.25 | +4.0% | +14.3% | +24.5% | HOLD→BUY | $19,623→NAV>px | +20 | wide-spread |
| TNK | 0.73× | 1.47 | +1.3% | +12.9% | +24.5% | HOLD→BUY | $22,904→NAV>px | +23 | wide-spread |
| CAPT | 0.69× | 1.14 | -1.9% | +10.2% | +22.3% | HOLD→BUY | NAV>px→NAV>px | +24 | wide-spread |
| HAFN | 0.86× | 1.47 | -16.7% | +1.5% | +19.8% | TRIM/SHORT→BUY | $93,560→$7,691 | +37 | wide-spread |
| SBLK | 0.78× | 1.13 | +4.3% | +11.8% | +19.3% | HOLD→BUY | $15,250→NAV>px | +15 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.21 | -12.1% | +3.0% | +18.1% | TRIM/SHORT→BUY | $81,778→NAV>px | +30 | wide-spread |
| SB | 0.88× | 0.88 | +34.1% | +22.0% | +9.8% | BUY→BUY | NAV>px→NAV>px | -24 | wide-spread |
| LPG | 0.84× | 1.38 | -26.6% | -11.2% | +4.2% | TRIM/SHORT→HOLD | $157,417→NAV>px | +31 | wide-spread |
| GNK | 0.89× | 1.13 | -9.0% | -2.6% | +3.9% | TRIM/SHORT→HOLD | $36,008→$14,366 | +13 | wide-spread |
| CMDB | 0.62× | 1.03 | +0.8% | +2.0% | +3.3% | HOLD→HOLD | $18,395→$15,226 | +2 | narrow-spread |
| NAT | 0.85× | 2.21 | -56.8% | -27.6% | +1.6% | TRIM/SHORT→HOLD | $445,150→NAV>px | +58 | wide-spread |
| 2343 | 0.98× | 1.03 | -3.3% | -1.9% | -0.4% | HOLD→HOLD | $18,872→$16,604 | +3 | narrow-spread |
| BRUT | 0.72× | 0.96 | +11.3% | +3.3% | -4.7% | BUY→HOLD | NAV>px→NAV>px | -16 | wide-spread |
| MPCC | 1.04× | 1.12 | -18.7% | -12.5% | -6.2% | TRIM/SHORT→TRIM/SHORT | $137,011→$48,022 | +12 | wide-spread |
| BWLP | 0.97× | 1.30 | -31.6% | -19.8% | -8.0% | TRIM/SHORT→TRIM/SHORT | $186,184→$60,314 | +24 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.51 | -38.5% | -25.6% | -12.7% | TRIM/SHORT→TRIM/SHORT | $346,197→$153,688 | +26 | wide-spread |
| FLNG | 1.35× | 0.90 | -0.4% | -8.9% | -17.4% | HOLD→TRIM/SHORT | $206,030→$468,168 | -17 | wide-spread |
| DHT | 1.14× | 1.13 | -26.6% | -22.1% | -17.6% | TRIM/SHORT→TRIM/SHORT | $391,452→$256,689 | +9 | narrow-spread |
| FRO | 1.37× | 1.10 | -40.3% | -36.3% | -32.4% | TRIM/SHORT→TRIM/SHORT | $406,711→$327,758 | +8 | narrow-spread |
| ECO | 1.35× | 1.16 | -43.4% | -38.0% | -32.5% | TRIM/SHORT→TRIM/SHORT | $394,899→$298,502 | +11 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
