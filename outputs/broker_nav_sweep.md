# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.27 | +51.2% | +76.7% | +102.3% | BUY→BUY | NAV>px→NAV>px | +51 | wide-spread |
| CCEC | 0.90× | 0.99 | +49.1% | +47.8% | +46.6% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| CAPT | 0.71× | 1.19 | +9.1% | +25.5% | +41.9% | BUY→BUY | $80,462→NAV>px | +33 | wide-spread |
| STNG | 0.71× | 1.58 | -3.4% | +17.5% | +38.3% | HOLD→BUY | $90,377→NAV>px | +42 | wide-spread |
| GSL | 0.75× | 1.32 | +1.7% | +15.6% | +29.4% | HOLD→BUY | $32,696→NAV>px | +28 | wide-spread |
| BRUT | 0.86× | 0.94 | +52.5% | +39.9% | +27.3% | BUY→BUY | NAV>px→NAV>px | -25 | wide-spread |
| TRMD | 0.86× | 1.13 | +11.6% | +18.9% | +26.3% | BUY→BUY | $41,844→$11,832 | +15 | wide-spread |
| ASC | 0.75× | 1.33 | -7.0% | +7.8% | +22.6% | TRIM/SHORT→BUY | $31,108→NAV>px | +30 | wide-spread |
| TNK | 0.80× | 1.44 | -1.4% | +9.8% | +21.0% | HOLD→BUY | $93,157→NAV>px | +22 | wide-spread |
| HAFN | 0.92× | 1.43 | -15.3% | +1.7% | +18.7% | TRIM/SHORT→BUY | $103,758→$24,347 | +34 | wide-spread |
| NAT | 0.85× | 2.31 | -54.3% | -21.4% | +11.5% | TRIM/SHORT→BUY | $658,330→NAV>px | +66 | wide-spread |
| 2343 | 0.91× | 1.31 | -20.2% | -8.1% | +4.0% | TRIM/SHORT→HOLD | $30,729→$12,225 | +24 | wide-spread |
| SB | 0.88× | 0.90 | +23.0% | +13.4% | +3.9% | BUY→HOLD | NAV>px→NAV>px | -19 | wide-spread |
| SBLK | 0.89× | 1.00 | +2.5% | +2.3% | +2.1% | HOLD→HOLD | $12,864→$13,327 | -0 | narrow-spread |
| CMBT **(WHOLE-CO)** | 0.85× | 1.14 | -16.4% | -7.2% | +2.0% | TRIM/SHORT→BUY | $136,080→$29,760 | +18 | wide-spread |
| CMDB | 0.62× | 0.90 | +10.3% | +6.0% | +1.7% | BUY→HOLD | NAV>px→$14,728 | -9 | narrow-spread |
| GNK | 0.92× | 1.11 | -13.9% | -8.5% | -3.0% | TRIM/SHORT→HOLD | $38,006→$19,532 | +11 | wide-spread |
| DHT | 1.08× | 1.19 | -18.2% | -11.2% | -4.1% | TRIM/SHORT→HOLD | $571,564→$293,729 | +14 | wide-spread |
| MPCC | 1.04× | 1.16 | -23.9% | -15.7% | -7.6% | TRIM/SHORT→TRIM/SHORT | $180,285→$55,172 | +16 | wide-spread |
| LPG | 0.96× | 1.41 | -32.8% | -20.8% | -8.9% | TRIM/SHORT→TRIM/SHORT | $246,904→$69,874 | +24 | wide-spread |
| INSW **(WHOLE-CO)** | 1.17× | 1.53 | -38.6% | -25.4% | -12.2% | TRIM/SHORT→TRIM/SHORT | $518,082→$253,467 | +26 | wide-spread |
| FRO | 1.31× | 1.16 | -32.6% | -25.9% | -19.1% | TRIM/SHORT→TRIM/SHORT | $590,752→$422,460 | +13 | wide-spread |
| BWLP | 1.13× | 1.22 | -36.4% | -28.5% | -20.6% | TRIM/SHORT→TRIM/SHORT | $223,480→$132,721 | +16 | wide-spread |
| FLNG | 1.43× | 0.87 | -0.4% | -10.8% | -21.2% | HOLD→TRIM/SHORT | $205,490→$527,389 | -21 | wide-spread |
| ECO | 1.34× | 1.11 | -30.8% | -26.7% | -22.7% | TRIM/SHORT→TRIM/SHORT | $500,715→$409,525 | +8 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
