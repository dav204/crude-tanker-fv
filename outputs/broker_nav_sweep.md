# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.16 | +36.3% | +51.2% | +66.1% | BUY→BUY | NAV>px→NAV>px | +30 | wide-spread |
| CCEC | 0.90× | 0.96 | +55.1% | +46.5% | +37.9% | BUY→BUY | NAV>px→NAV>px | -17 | wide-spread |
| GSL | 0.75× | 1.25 | +6.4% | +18.9% | +31.5% | BUY→BUY | NAV>px→NAV>px | +25 | wide-spread |
| STNG | 0.69× | 1.40 | -2.9% | +12.9% | +28.6% | HOLD→BUY | $39,551→NAV>px | +32 | wide-spread |
| SBLK | 0.78× | 1.08 | +12.1% | +17.1% | +22.0% | BUY→BUY | $9,650→NAV>px | +10 | narrow-spread |
| ASC | 0.75× | 1.13 | +9.6% | +15.3% | +21.1% | BUY→BUY | $7,407→NAV>px | +12 | wide-spread |
| TNK | 0.73× | 1.33 | +0.0% | +7.8% | +15.5% | HOLD→BUY | NAV>px→NAV>px | +15 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.15 | -8.3% | +3.1% | +14.6% | TRIM/SHORT→BUY | $52,880→NAV>px | +23 | wide-spread |
| SB | 0.88× | 0.83 | +53.4% | +34.0% | +14.5% | BUY→BUY | NAV>px→NAV>px | -39 | wide-spread |
| TRMD | 0.82× | 1.09 | +3.4% | +8.5% | +13.6% | HOLD→BUY | $24,799→NAV>px | +10 | wide-spread |
| HAFN | 0.86× | 1.39 | -20.1% | -5.1% | +9.9% | TRIM/SHORT→BUY | $79,286→$8,086 | +30 | wide-spread |
| GNK | 0.89× | 1.09 | -3.9% | +1.1% | +6.1% | HOLD→BUY | $29,692→$14,076 | +10 | narrow-spread |
| CMDB | 0.62× | 0.93 | +11.9% | +8.6% | +5.3% | BUY→BUY | $7,207→$14,814 | -7 | narrow-spread |
| CAPT | 0.69× | 1.15 | -26.4% | -14.8% | -3.1% | TRIM/SHORT→HOLD | $6,063→NAV>px | +23 | wide-spread |
| MPCC | 1.04× | 1.11 | -18.1% | -12.1% | -6.1% | TRIM/SHORT→TRIM/SHORT | $132,543→$47,330 | +12 | wide-spread |
| NAT | 0.85× | 2.06 | -61.2% | -36.3% | -11.5% | TRIM/SHORT→TRIM/SHORT | $391,067→NAV>px | +50 | wide-spread |
| FLNG | 1.35× | 0.87 | -0.4% | -10.7% | -21.0% | HOLD→TRIM/SHORT | $124,006→$438,558 | -21 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.41 | -41.8% | -31.6% | -21.4% | TRIM/SHORT→TRIM/SHORT | $299,845→$144,354 | +20 | wide-spread |
| DHT | 1.14× | 1.08 | -33.9% | -31.5% | -29.0% | TRIM/SHORT→TRIM/SHORT | $318,149→$240,463 | +5 | narrow-spread |
| ECO | 1.35× | 1.10 | -51.6% | -48.2% | -44.8% | TRIM/SHORT→TRIM/SHORT | $343,913→$281,217 | +7 | narrow-spread |
| FRO | 1.37× | 1.07 | -50.6% | -48.0% | -45.5% | TRIM/SHORT→TRIM/SHORT | $368,638→$314,436 | +5 | narrow-spread |
| BRUT | 0.72× | 0.95 | -41.4% | -51.3% | -61.3% | TRIM/SHORT→TRIM/SHORT | NAV>px→NAV>px | -20 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
