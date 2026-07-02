# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.12 | +81.9% | +95.5% | +109.2% | BUY→BUY | NAV>px→NAV>px | +27 | wide-spread |
| BRUT | 0.75× | 0.94 | +98.1% | +80.2% | +62.3% | BUY→BUY | NAV>px→NAV>px | -36 | wide-spread |
| CAPT | 0.67× | 1.11 | +37.4% | +49.3% | +61.2% | BUY→BUY | NAV>px→NAV>px | +24 | wide-spread |
| CCEC | 0.90× | 0.96 | +65.6% | +56.9% | +48.3% | BUY→BUY | NAV>px→NAV>px | -17 | wide-spread |
| STNG | 0.70× | 1.31 | +10.9% | +24.7% | +38.5% | BUY→BUY | $21,075→NAV>px | +28 | wide-spread |
| TNK | 0.76× | 1.16 | +23.7% | +28.6% | +33.4% | BUY→BUY | NAV>px→NAV>px | +10 | narrow-spread |
| GSL | 0.75× | 1.24 | +7.4% | +19.7% | +31.9% | BUY→BUY | NAV>px→NAV>px | +24 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.74× | 1.11 | +10.7% | +20.5% | +30.3% | BUY→BUY | $40,799→NAV>px | +20 | wide-spread |
| TRMD | 0.83× | 1.03 | +21.5% | +23.7% | +25.8% | BUY→BUY | $14,186→$5,336 | +4 | narrow-spread |
| ASC | 0.75× | 1.08 | +18.1% | +21.8% | +25.5% | BUY→BUY | NAV>px→NAV>px | +7 | narrow-spread |
| NAT | 0.85× | 1.98 | -40.1% | -9.5% | +21.2% | TRIM/SHORT→BUY | $362,899→NAV>px | +61 | wide-spread |
| SBLK | 0.82× | 1.03 | +14.3% | +15.9% | +17.5% | BUY→BUY | $8,164→NAV>px | +3 | narrow-spread |
| SB | 0.88× | 0.82 | +53.4% | +33.1% | +12.9% | BUY→BUY | NAV>px→NAV>px | -40 | wide-spread |
| HAFN | 0.95× | 1.20 | -5.1% | +3.8% | +12.7% | TRIM/SHORT→BUY | $65,013→$28,534 | +18 | wide-spread |
| GNK | 0.87× | 1.12 | -2.5% | +4.0% | +10.4% | HOLD→BUY | $28,077→$12,294 | +13 | wide-spread |
| INSW **(WHOLE-CO)** | 0.98× | 1.51 | -22.6% | -6.8% | +9.1% | TRIM/SHORT→BUY | $262,407→$70,042 | +32 | wide-spread |
| CMDB | 0.62× | 0.93 | +12.2% | +8.9% | +5.7% | BUY→BUY | $7,318→$14,664 | -7 | narrow-spread |
| DHT | 1.09× | 1.08 | -4.6% | -1.0% | +2.5% | HOLD→HOLD | $270,502→$186,637 | +7 | narrow-spread |
| MPCC | 1.04× | 1.09 | -13.0% | -7.9% | -2.8% | TRIM/SHORT→HOLD | $108,107→$41,889 | +10 | wide-spread |
| FRO | 1.20× | 1.13 | -16.9% | -10.7% | -4.5% | TRIM/SHORT→HOLD | $320,754→$223,034 | +12 | wide-spread |
| ECO | 1.21× | 1.14 | -19.9% | -13.5% | -7.1% | TRIM/SHORT→TRIM/SHORT | $299,265→$212,288 | +13 | wide-spread |
| FLNG | 1.37× | 0.86 | +7.2% | -5.1% | -17.3% | BUY→TRIM/SHORT | $87,851→$439,913 | -25 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
