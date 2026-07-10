# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.18 | +33.2% | +49.5% | +65.8% | BUY→BUY | NAV>px→NAV>px | +33 | wide-spread |
| CCEC | 0.90× | 0.97 | +49.0% | +42.7% | +36.4% | BUY→BUY | NAV>px→NAV>px | -13 | wide-spread |
| GSL | 0.75× | 1.29 | +2.8% | +16.7% | +30.6% | HOLD→BUY | NAV>px→NAV>px | +28 | wide-spread |
| STNG | 0.69× | 1.47 | -7.0% | +10.6% | +28.1% | TRIM/SHORT→BUY | $56,752→NAV>px | +35 | wide-spread |
| SBLK | 0.78× | 1.10 | +8.9% | +15.3% | +21.7% | BUY→BUY | $12,503→NAV>px | +13 | wide-spread |
| ASC | 0.75× | 1.17 | +6.3% | +13.5% | +20.8% | BUY→BUY | $11,815→NAV>px | +15 | wide-spread |
| TNK | 0.73× | 1.38 | -2.4% | +6.3% | +15.0% | HOLD→BUY | NAV>px→NAV>px | +17 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.17 | -10.6% | +2.0% | +14.5% | TRIM/SHORT→BUY | $61,644→NAV>px | +25 | wide-spread |
| SB | 0.88× | 0.85 | +46.6% | +30.2% | +13.9% | BUY→BUY | NAV>px→NAV>px | -33 | wide-spread |
| TRMD | 0.82× | 1.11 | +2.1% | +7.7% | +13.4% | HOLD→BUY | $27,403→NAV>px | +11 | wide-spread |
| HAFN | 0.86× | 1.39 | -20.1% | -5.1% | +9.9% | TRIM/SHORT→BUY | $79,286→$8,086 | +30 | wide-spread |
| GNK | 0.89× | 1.09 | -3.1% | +1.5% | +6.1% | HOLD→BUY | $28,480→$14,038 | +9 | narrow-spread |
| LPG | 0.84× | 1.21 | -15.1% | -5.0% | +5.1% | TRIM/SHORT→BUY | $90,798→NAV>px | +20 | wide-spread |
| CMDB | 0.62× | 0.98 | +6.6% | +5.7% | +4.9% | BUY→HOLD | $12,866→$14,974 | -2 | narrow-spread |
| CAPT | 0.69× | 1.12 | -22.9% | -13.3% | -3.6% | TRIM/SHORT→HOLD | NAV>px→NAV>px | +19 | wide-spread |
| MPCC | 1.04× | 1.10 | -17.1% | -11.5% | -5.9% | TRIM/SHORT→TRIM/SHORT | $124,928→$46,150 | +11 | wide-spread |
| BWLP | 0.97× | 1.16 | -21.9% | -14.5% | -7.1% | TRIM/SHORT→TRIM/SHORT | $124,605→$55,676 | +15 | wide-spread |
| NAT | 0.85× | 2.09 | -61.8% | -36.7% | -11.5% | TRIM/SHORT→TRIM/SHORT | $401,208→NAV>px | +50 | wide-spread |
| FLNG | 1.35× | 0.87 | +0.1% | -10.5% | -21.0% | HOLD→TRIM/SHORT | $117,530→$436,220 | -21 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.42 | -42.2% | -31.8% | -21.5% | TRIM/SHORT→TRIM/SHORT | $304,545→$145,301 | +21 | wide-spread |
| DHT | 1.14× | 1.06 | -33.0% | -30.9% | -28.9% | TRIM/SHORT→TRIM/SHORT | $299,823→$236,407 | +4 | narrow-spread |
| ECO | 1.35× | 1.09 | -50.7% | -47.8% | -44.8% | TRIM/SHORT→TRIM/SHORT | $331,519→$277,016 | +6 | narrow-spread |
| FRO | 1.37× | 1.07 | -50.3% | -47.9% | -45.5% | TRIM/SHORT→TRIM/SHORT | $364,200→$312,883 | +5 | narrow-spread |
| BRUT | 0.72× | 0.97 | -44.9% | -51.1% | -57.3% | TRIM/SHORT→TRIM/SHORT | NAV>px→NAV>px | -12 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
