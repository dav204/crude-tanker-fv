# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.19 | +69.3% | +90.2% | +111.0% | BUY→BUY | NAV>px→NAV>px | +42 | wide-spread |
| CAPT | 0.67× | 1.17 | +26.7% | +43.6% | +60.5% | BUY→BUY | NAV>px→NAV>px | +34 | wide-spread |
| BRUT | 0.75× | 0.93 | +100.1% | +80.3% | +60.5% | BUY→BUY | NAV>px→NAV>px | -40 | wide-spread |
| CCEC | 0.90× | 0.94 | +79.3% | +65.6% | +51.9% | BUY→BUY | NAV>px→NAV>px | -27 | wide-spread |
| STNG | 0.70× | 1.47 | -0.7% | +18.2% | +37.1% | HOLD→BUY | $62,640→NAV>px | +38 | wide-spread |
| GSL | 0.75× | 1.25 | +7.1% | +19.5% | +31.8% | BUY→BUY | NAV>px→NAV>px | +25 | wide-spread |
| TNK | 0.76× | 1.45 | +6.9% | +18.9% | +30.9% | BUY→BUY | $41,889→NAV>px | +24 | wide-spread |
| ASC | 0.75× | 1.42 | -11.3% | +6.3% | +23.8% | TRIM/SHORT→BUY | $41,676→NAV>px | +35 | wide-spread |
| TRMD | 0.83× | 1.28 | -7.1% | +7.8% | +22.7% | TRIM/SHORT→BUY | $71,405→$5,383 | +30 | wide-spread |
| NAT | 0.85× | 2.16 | -52.5% | -15.2% | +22.1% | TRIM/SHORT→BUY | $404,139→NAV>px | +75 | wide-spread |
| SBLK | 0.82× | 1.15 | -0.2% | +8.0% | +16.3% | HOLD→BUY | $22,755→NAV>px | +16 | wide-spread |
| GNK | 0.87× | 1.03 | +7.3% | +9.1% | +10.8% | BUY→BUY | $16,540→$12,419 | +3 | narrow-spread |
| HAFN | 0.95× | 1.36 | -18.2% | -3.8% | +10.7% | TRIM/SHORT→BUY | $95,336→$30,566 | +29 | wide-spread |
| INSW **(WHOLE-CO)** | 0.98× | 1.64 | -27.6% | -8.8% | +9.9% | TRIM/SHORT→BUY | $316,872→$74,962 | +38 | wide-spread |
| CMDB | 0.62× | 0.82 | +25.0% | +15.7% | +6.3% | BUY→BUY | NAV>px→$14,632 | -19 | wide-spread |
| DHT | 1.09× | 1.30 | -21.8% | -11.2% | -0.6% | TRIM/SHORT→HOLD | $529,540→$230,527 | +21 | wide-spread |
| MPCC | 1.04× | 1.12 | -17.1% | -10.4% | -3.8% | TRIM/SHORT→HOLD | $137,799→$46,477 | +13 | wide-spread |
| FRO | 1.20× | 1.27 | -29.9% | -18.6% | -7.4% | TRIM/SHORT→TRIM/SHORT | $469,143→$260,767 | +23 | wide-spread |
| ECO | 1.21× | 1.20 | -24.9% | -16.4% | -7.9% | TRIM/SHORT→TRIM/SHORT | $343,849→$222,252 | +17 | wide-spread |
| FLNG | 1.37× | 0.87 | +3.1% | -7.4% | -17.9% | HOLD→TRIM/SHORT | $148,289→$462,295 | -21 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
