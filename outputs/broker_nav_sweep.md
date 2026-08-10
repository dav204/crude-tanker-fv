# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.22 | +59.6% | +81.2% | +102.7% | BUY→BUY | NAV>px→NAV>px | +43 | wide-spread |
| BRUT | 0.72× | 1.00 | +45.6% | +46.4% | +47.1% | BUY→BUY | NAV>px→NAV>px | +1 | narrow-spread |
| CCEC | 0.90× | 0.99 | +50.7% | +48.9% | +47.1% | BUY→BUY | NAV>px→NAV>px | -4 | narrow-spread |
| CAPT | 0.69× | 1.17 | +13.9% | +29.5% | +45.1% | BUY→BUY | $27,208→NAV>px | +31 | wide-spread |
| STNG | 0.69× | 1.56 | +0.9% | +21.6% | +42.4% | HOLD→BUY | $67,990→NAV>px | +42 | wide-spread |
| TNK | 0.73× | 1.43 | +8.4% | +20.4% | +32.3% | BUY→BUY | $11,451→NAV>px | +24 | wide-spread |
| TRMD | 0.82× | 1.16 | +13.9% | +22.9% | +31.9% | BUY→BUY | $37,671→NAV>px | +18 | wide-spread |
| GSL | 0.75× | 1.32 | +1.0% | +15.2% | +29.3% | HOLD→BUY | $41,213→NAV>px | +28 | wide-spread |
| HAFN | 0.86× | 1.48 | -12.7% | +6.8% | +26.3% | TRIM/SHORT→BUY | $96,485→$7,814 | +39 | wide-spread |
| ASC | 0.75× | 1.27 | -2.0% | +10.6% | +23.1% | HOLD→BUY | $22,102→NAV>px | +25 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.21 | -11.7% | +3.2% | +18.1% | TRIM/SHORT→BUY | $106,340→NAV>px | +30 | wide-spread |
| SBLK | 0.78× | 1.11 | +3.1% | +9.1% | +15.2% | HOLD→BUY | $12,307→NAV>px | +12 | wide-spread |
| NAT | 0.85× | 2.23 | -52.8% | -20.7% | +11.3% | TRIM/SHORT→BUY | $620,285→NAV>px | +64 | wide-spread |
| SB | 0.88× | 0.89 | +25.4% | +14.7% | +4.0% | BUY→HOLD | NAV>px→NAV>px | -21 | wide-spread |
| LPG | 0.84× | 1.57 | -30.5% | -13.4% | +3.7% | TRIM/SHORT→HOLD | $223,619→NAV>px | +34 | wide-spread |
| CMDB | 0.62× | 0.88 | +12.9% | +7.4% | +1.9% | BUY→HOLD | NAV>px→$14,648 | -11 | wide-spread |
| GNK | 0.89× | 1.10 | -10.5% | -5.1% | +0.3% | TRIM/SHORT→HOLD | $31,845→$14,263 | +11 | wide-spread |
| 2343 | 0.98× | 1.20 | -18.4% | -10.5% | -2.7% | TRIM/SHORT→HOLD | $29,068→$17,269 | +16 | wide-spread |
| MPCC | 1.04× | 1.12 | -19.1% | -12.8% | -6.5% | TRIM/SHORT→TRIM/SHORT | $139,574→$48,856 | +13 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.53 | -35.7% | -21.7% | -7.7% | TRIM/SHORT→TRIM/SHORT | $469,118→$201,666 | +28 | wide-spread |
| BWLP | 0.97× | 1.32 | -33.0% | -20.6% | -8.2% | TRIM/SHORT→TRIM/SHORT | $196,627→$61,101 | +25 | wide-spread |
| DHT | 1.14× | 1.09 | -15.4% | -11.9% | -8.5% | TRIM/SHORT→TRIM/SHORT | $494,031→$362,684 | +7 | narrow-spread |
| FLNG | 1.35× | 0.90 | -0.5% | -9.0% | -17.4% | HOLD→TRIM/SHORT | $207,648→$468,753 | -17 | wide-spread |
| FRO | 1.37× | 1.10 | -30.6% | -26.5% | -22.3% | TRIM/SHORT→TRIM/SHORT | $545,468→$444,556 | +8 | narrow-spread |
| ECO | 1.35× | 1.13 | -33.0% | -28.5% | -23.9% | TRIM/SHORT→TRIM/SHORT | $530,104→$425,044 | +9 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
