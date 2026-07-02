# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.12 | +85.2% | +99.0% | +112.8% | BUY→BUY | NAV>px→NAV>px | +28 | wide-spread |
| BRUT | 0.75× | 0.94 | +96.6% | +79.3% | +62.0% | BUY→BUY | NAV>px→NAV>px | -35 | wide-spread |
| CAPT | 0.67× | 1.12 | +36.4% | +48.7% | +61.1% | BUY→BUY | NAV>px→NAV>px | +25 | wide-spread |
| CCEC | 0.90× | 0.96 | +68.2% | +58.6% | +48.9% | BUY→BUY | NAV>px→NAV>px | -19 | wide-spread |
| STNG | 0.70× | 1.43 | +2.0% | +19.7% | +37.4% | HOLD→BUY | $53,301→NAV>px | +35 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.74× | 1.11 | +14.9% | +24.6% | +34.4% | BUY→BUY | $39,378→NAV>px | +19 | wide-spread |
| GSL | 0.75× | 1.24 | +8.0% | +20.0% | +32.0% | BUY→BUY | NAV>px→NAV>px | +24 | wide-spread |
| TNK | 0.76× | 1.34 | +12.4% | +22.1% | +31.8% | BUY→BUY | $10,261→NAV>px | +19 | wide-spread |
| TRMD | 0.83× | 1.17 | +4.8% | +14.9% | +24.9% | HOLD→BUY | $46,693→$7,144 | +20 | wide-spread |
| ASC | 0.75× | 1.23 | +5.2% | +14.9% | +24.6% | BUY→BUY | $18,010→NAV>px | +19 | wide-spread |
| NAT | 0.85× | 1.98 | -39.9% | -9.3% | +21.2% | TRIM/SHORT→BUY | $360,646→NAV>px | +61 | wide-spread |
| SBLK | 0.82× | 1.03 | +13.6% | +15.5% | +17.5% | BUY→BUY | $8,819→NAV>px | +4 | narrow-spread |
| SB | 0.88× | 0.82 | +53.4% | +33.1% | +12.9% | BUY→BUY | NAV>px→NAV>px | -40 | wide-spread |
| HAFN | 0.95× | 1.22 | -6.2% | +3.1% | +12.5% | TRIM/SHORT→BUY | $67,495→$28,712 | +19 | wide-spread |
| INSW **(WHOLE-CO)** | 0.98× | 1.49 | -19.9% | -4.2% | +11.4% | TRIM/SHORT→BUY | $252,764→$69,122 | +31 | wide-spread |
| GNK | 0.87× | 1.12 | -2.9% | +3.7% | +10.4% | HOLD→BUY | $28,690→$12,311 | +13 | wide-spread |
| CMDB | 0.62× | 0.89 | +16.3% | +11.2% | +6.0% | BUY→BUY | NAV>px→$14,550 | -10 | wide-spread |
| DHT | 1.09× | 1.07 | -3.9% | -0.6% | +2.7% | HOLD→HOLD | $260,972→$184,868 | +7 | narrow-spread |
| MPCC | 1.04× | 1.12 | -17.4% | -10.6% | -3.8% | TRIM/SHORT→HOLD | $140,273→$46,859 | +14 | wide-spread |
| FRO | 1.20× | 1.12 | -16.5% | -10.4% | -4.4% | TRIM/SHORT→HOLD | $316,083→$221,830 | +12 | wide-spread |
| ECO | 1.21× | 1.14 | -20.2% | -13.7% | -7.2% | TRIM/SHORT→TRIM/SHORT | $301,800→$212,954 | +13 | wide-spread |
| FLNG | 1.37× | 0.85 | +9.3% | -3.9% | -17.1% | BUY→TRIM/SHORT | $57,631→$428,722 | -26 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
