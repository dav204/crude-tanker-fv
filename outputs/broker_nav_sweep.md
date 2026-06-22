# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.19 | +62.5% | +83.7% | +105.0% | BUY→BUY | NAV>px→NAV>px | +42 | wide-spread |
| CAPT | 0.67× | 1.17 | +22.4% | +39.6% | +56.9% | BUY→BUY | NAV>px→NAV>px | +35 | wide-spread |
| BRUT | 0.75× | 0.93 | +97.3% | +76.9% | +56.6% | BUY→BUY | NAV>px→NAV>px | -41 | wide-spread |
| STNG | 0.70× | 1.47 | -9.2% | +10.0% | +29.3% | TRIM/SHORT→BUY | $2,725,019→NAV>px | +39 | wide-spread |
| NAT | 0.85× | 2.16 | -51.1% | -12.9% | +25.2% | TRIM/SHORT→BUY | $396,401→NAV>px | +76 | wide-spread |
| ASC | 0.75× | 1.42 | -11.8% | +6.0% | +23.9% | TRIM/SHORT→BUY | $51,701→NAV>px | +36 | wide-spread |
| TNK | 0.76× | 1.45 | -1.0% | +11.3% | +23.6% | HOLD→BUY | $100,249→NAV>px | +25 | wide-spread |
| TRMD | 0.83× | 1.28 | -9.3% | +5.9% | +21.1% | TRIM/SHORT→BUY | $80,541→NAV>px | +30 | wide-spread |
| CCEC | 0.90× | 0.94 | +47.9% | +34.3% | +20.7% | BUY→BUY | NAV>px→$2,977,992 | -27 | wide-spread |
| SBLK | 0.82× | 1.15 | +0.6% | +9.0% | +17.3% | HOLD→BUY | $21,396→NAV>px | +17 | wide-spread |
| GNK | 0.87× | 1.03 | +8.8% | +10.5% | +12.3% | BUY→BUY | $16,540→$12,419 | +4 | narrow-spread |
| HAFN | 0.95× | 1.36 | -20.3% | -5.5% | +9.2% | TRIM/SHORT→BUY | $108,657→$27,779 | +29 | wide-spread |
| GSL | 0.75× | 1.25 | -16.2% | -3.7% | +8.8% | TRIM/SHORT→BUY | $2,757,173→NAV>px | +25 | wide-spread |
| INSW **(WHOLE-CO)** | 0.98× | 1.64 | -29.6% | -10.4% | +8.8% | TRIM/SHORT→BUY | $414,323→$73,188 | +38 | wide-spread |
| DHT | 1.09× | 1.30 | -20.2% | -9.3% | +1.6% | TRIM/SHORT→HOLD | $506,266→$200,241 | +22 | wide-spread |
| CMDB | 0.62× | 0.82 | +18.2% | +8.7% | -0.7% | BUY→HOLD | NAV>px→$1,068,984 | -19 | wide-spread |
| FRO | 1.20× | 1.27 | -28.7% | -17.1% | -5.6% | TRIM/SHORT→TRIM/SHORT | $472,015→$248,780 | +23 | wide-spread |
| ECO | 1.21× | 1.20 | -25.1% | -16.4% | -7.7% | TRIM/SHORT→TRIM/SHORT | $377,597→$233,717 | +17 | wide-spread |
| MPCC | 1.04× | 1.12 | -27.3% | -20.6% | -13.9% | TRIM/SHORT→TRIM/SHORT | $299,648→$120,040 | +13 | wide-spread |
| FLNG | 1.37× | 0.87 | -0.0% | -10.5% | -21.0% | HOLD→TRIM/SHORT | $3,162,500→$3,162,500 | -21 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
