# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.19 | +50.1% | +68.0% | +86.0% | BUY→BUY | NAV>px→NAV>px | +36 | wide-spread |
| CCEC | 0.90× | 0.97 | +61.8% | +54.5% | +47.3% | BUY→BUY | NAV>px→NAV>px | -15 | wide-spread |
| STNG | 0.69× | 1.48 | +0.8% | +20.0% | +39.1% | HOLD→BUY | $58,027→NAV>px | +38 | wide-spread |
| GSL | 0.75× | 1.31 | +0.9% | +15.5% | +30.1% | HOLD→BUY | $21,682→NAV>px | +29 | wide-spread |
| TRMD | 0.82× | 1.12 | +12.1% | +18.8% | +25.5% | BUY→BUY | $30,223→NAV>px | +13 | wide-spread |
| TNK | 0.73× | 1.40 | +4.4% | +14.7% | +25.0% | HOLD→BUY | NAV>px→NAV>px | +21 | wide-spread |
| ASC | 0.75× | 1.18 | +9.3% | +17.1% | +24.9% | BUY→BUY | $12,560→NAV>px | +16 | wide-spread |
| CAPT | 0.69× | 1.10 | +3.3% | +12.9% | +22.4% | HOLD→BUY | NAV>px→NAV>px | +19 | wide-spread |
| HAFN | 0.86× | 1.43 | -14.1% | +3.1% | +20.4% | TRIM/SHORT→BUY | $86,423→$7,889 | +34 | wide-spread |
| SBLK | 0.78× | 1.07 | +11.2% | +15.6% | +20.0% | BUY→BUY | $8,685→NAV>px | +9 | narrow-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.17 | -7.3% | +5.5% | +18.3% | TRIM/SHORT→BUY | $62,354→NAV>px | +26 | wide-spread |
| SB | 0.88× | 0.86 | +40.2% | +25.3% | +10.4% | BUY→BUY | NAV>px→NAV>px | -30 | wide-spread |
| GNK | 0.89× | 1.08 | -4.0% | +0.2% | +4.4% | HOLD→HOLD | $27,466→$14,102 | +8 | narrow-spread |
| LPG | 0.84× | 1.36 | -25.5% | -10.6% | +4.3% | TRIM/SHORT→HOLD | $150,318→NAV>px | +30 | wide-spread |
| CMDB | 0.62× | 0.96 | +6.8% | +5.3% | +3.7% | BUY→HOLD | $11,242→$15,024 | -3 | narrow-spread |
| NAT | 0.85× | 2.13 | -55.1% | -26.6% | +1.9% | TRIM/SHORT→HOLD | $418,109→NAV>px | +57 | wide-spread |
| 2343 | 0.98× | 1.04 | -4.6% | -2.5% | -0.5% | HOLD→HOLD | $19,858→$16,712 | +4 | narrow-spread |
| BRUT | 0.72× | 0.96 | +12.8% | +3.9% | -5.0% | BUY→TRIM/SHORT | NAV>px→NAV>px | -18 | wide-spread |
| MPCC | 1.04× | 1.10 | -16.9% | -11.4% | -5.9% | TRIM/SHORT→TRIM/SHORT | $123,507→$45,930 | +11 | wide-spread |
| BWLP | 0.97× | 1.26 | -28.9% | -18.3% | -7.8% | TRIM/SHORT→TRIM/SHORT | $167,334→$58,894 | +21 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.49 | -37.5% | -25.0% | -12.5% | TRIM/SHORT→TRIM/SHORT | $335,176→$151,469 | +25 | wide-spread |
| DHT | 1.14× | 1.09 | -23.4% | -20.2% | -17.0% | TRIM/SHORT→TRIM/SHORT | $335,008→$244,195 | +6 | narrow-spread |
| FLNG | 1.35× | 0.89 | +0.0% | -8.7% | -17.3% | HOLD→TRIM/SHORT | $198,475→$465,441 | -17 | wide-spread |
| FRO | 1.37× | 1.07 | -37.2% | -34.6% | -31.9% | TRIM/SHORT→TRIM/SHORT | $362,565→$312,311 | +5 | narrow-spread |
| ECO | 1.35× | 1.11 | -40.4% | -36.3% | -32.1% | TRIM/SHORT→TRIM/SHORT | $354,758→$284,894 | +8 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
