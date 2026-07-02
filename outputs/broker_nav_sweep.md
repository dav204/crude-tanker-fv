# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.12 | +44.0% | +55.3% | +66.7% | BUY→BUY | NAV>px→NAV>px | +23 | wide-spread |
| CCEC | 0.90× | 0.96 | +54.5% | +46.1% | +37.8% | BUY→BUY | NAV>px→NAV>px | -17 | wide-spread |
| GSL | 0.75× | 1.24 | +7.4% | +19.7% | +31.9% | BUY→BUY | NAV>px→NAV>px | +24 | wide-spread |
| STNG | 0.70× | 1.31 | +2.0% | +14.7% | +27.5% | HOLD→BUY | $21,075→NAV>px | +26 | wide-spread |
| ASC | 0.75× | 1.08 | +14.2% | +17.8% | +21.4% | BUY→BUY | NAV>px→NAV>px | +7 | narrow-spread |
| SBLK | 0.82× | 1.03 | +13.6% | +15.2% | +16.8% | BUY→BUY | $8,259→NAV>px | +3 | narrow-spread |
| SB | 0.88× | 0.82 | +55.6% | +35.2% | +14.8% | BUY→BUY | NAV>px→NAV>px | -41 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.74× | 1.11 | -5.0% | +4.1% | +13.1% | TRIM/SHORT→BUY | $40,799→NAV>px | +18 | wide-spread |
| TRMD | 0.83× | 1.03 | +9.1% | +11.1% | +13.1% | BUY→BUY | $14,186→$5,336 | +4 | narrow-spread |
| TNK | 0.76× | 1.16 | +5.1% | +8.9% | +12.8% | BUY→BUY | NAV>px→NAV>px | +8 | narrow-spread |
| GNK | 0.87× | 1.12 | -4.5% | +1.9% | +8.2% | HOLD→BUY | $30,712→$10,604 | +13 | wide-spread |
| CMDB | 0.62× | 0.93 | +11.7% | +8.5% | +5.2% | BUY→BUY | $7,396→$14,819 | -6 | narrow-spread |
| HAFN | 0.95× | 1.20 | -14.5% | -6.3% | +2.0% | TRIM/SHORT→HOLD | $65,013→$28,534 | +17 | wide-spread |
| CAPT | 0.67× | 1.11 | -19.4% | -10.1% | -0.9% | TRIM/SHORT→HOLD | NAV>px→NAV>px | +19 | wide-spread |
| MPCC | 1.04× | 1.09 | -13.0% | -7.9% | -2.8% | TRIM/SHORT→HOLD | $108,107→$41,889 | +10 | wide-spread |
| NAT | 0.85× | 1.98 | -59.5% | -35.4% | -11.3% | TRIM/SHORT→TRIM/SHORT | $362,899→NAV>px | +48 | wide-spread |
| INSW **(WHOLE-CO)** | 0.98× | 1.51 | -38.3% | -25.0% | -11.6% | TRIM/SHORT→TRIM/SHORT | $262,407→$70,042 | +27 | wide-spread |
| FLNG | 1.37× | 0.86 | +2.0% | -9.9% | -21.7% | HOLD→TRIM/SHORT | $87,851→$439,913 | -24 | wide-spread |
| DHT | 1.09× | 1.08 | -31.3% | -28.6% | -25.8% | TRIM/SHORT→TRIM/SHORT | $270,502→$186,637 | +6 | narrow-spread |
| FRO | 1.20× | 1.13 | -47.6% | -42.8% | -38.0% | TRIM/SHORT→TRIM/SHORT | $320,754→$223,034 | +10 | narrow-spread |
| ECO | 1.21× | 1.14 | -48.5% | -43.5% | -38.5% | TRIM/SHORT→TRIM/SHORT | $299,265→$212,288 | +10 | narrow-spread |
| BRUT | 0.75× | 0.94 | -39.7% | -53.5% | -67.4% | TRIM/SHORT→TRIM/SHORT | NAV>px→NAV>px | -28 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
