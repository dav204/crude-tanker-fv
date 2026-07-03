# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.16 | +36.3% | +51.2% | +66.1% | BUY→BUY | NAV>px→NAV>px | +30 | wide-spread |
| CCEC | 0.90× | 0.96 | +55.1% | +46.5% | +37.9% | BUY→BUY | NAV>px→NAV>px | -17 | wide-spread |
| GSL | 0.75× | 1.25 | +6.5% | +19.1% | +31.6% | BUY→BUY | NAV>px→NAV>px | +25 | wide-spread |
| STNG | 0.70× | 1.38 | -2.9% | +12.0% | +26.9% | HOLD→BUY | $39,551→NAV>px | +30 | wide-spread |
| ASC | 0.75× | 1.13 | +9.6% | +15.3% | +21.1% | BUY→BUY | $7,407→NAV>px | +12 | wide-spread |
| SBLK | 0.82× | 1.03 | +13.6% | +15.2% | +16.8% | BUY→BUY | $8,259→NAV>px | +3 | narrow-spread |
| SB | 0.88× | 0.83 | +53.4% | +34.0% | +14.5% | BUY→BUY | NAV>px→NAV>px | -39 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.74× | 1.14 | -8.4% | +2.3% | +13.1% | TRIM/SHORT→BUY | $52,880→NAV>px | +21 | wide-spread |
| TRMD | 0.83× | 1.08 | +3.4% | +7.9% | +12.4% | HOLD→BUY | $24,799→NAV>px | +9 | narrow-spread |
| TNK | 0.76× | 1.25 | +0.0% | +5.9% | +11.7% | HOLD→BUY | NAV>px→NAV>px | +12 | wide-spread |
| GNK | 0.87× | 1.11 | -3.9% | +2.2% | +8.3% | HOLD→BUY | $29,692→$10,595 | +12 | wide-spread |
| CMDB | 0.62× | 0.93 | +11.9% | +8.6% | +5.3% | BUY→BUY | $7,207→$14,814 | -7 | narrow-spread |
| HAFN | 0.95× | 1.28 | -20.1% | -9.6% | +0.9% | TRIM/SHORT→HOLD | $79,286→$29,561 | +21 | wide-spread |
| CAPT | 0.67× | 1.15 | -24.2% | -12.2% | -0.3% | TRIM/SHORT→HOLD | NAV>px→NAV>px | +24 | wide-spread |
| MPCC | 1.04× | 1.09 | -13.7% | -8.4% | -3.0% | TRIM/SHORT→HOLD | $113,055→$42,654 | +11 | wide-spread |
| NAT | 0.85× | 2.06 | -61.2% | -36.3% | -11.5% | TRIM/SHORT→TRIM/SHORT | $391,067→NAV>px | +50 | wide-spread |
| INSW **(WHOLE-CO)** | 0.98× | 1.60 | -41.8% | -26.9% | -12.1% | TRIM/SHORT→TRIM/SHORT | $299,845→$73,615 | +30 | wide-spread |
| FLNG | 1.37× | 0.87 | -0.4% | -11.2% | -22.0% | HOLD→TRIM/SHORT | $124,006→$453,302 | -22 | wide-spread |
| DHT | 1.09× | 1.12 | -33.9% | -30.1% | -26.2% | TRIM/SHORT→TRIM/SHORT | $318,149→$195,482 | +8 | narrow-spread |
| FRO | 1.20× | 1.17 | -50.6% | -44.3% | -38.1% | TRIM/SHORT→TRIM/SHORT | $368,638→$235,378 | +12 | wide-spread |
| ECO | 1.21× | 1.19 | -51.6% | -45.1% | -38.6% | TRIM/SHORT→TRIM/SHORT | $343,913→$224,009 | +13 | wide-spread |
| BRUT | 0.75× | 0.94 | -41.0% | -53.4% | -65.8% | TRIM/SHORT→TRIM/SHORT | NAV>px→NAV>px | -25 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
