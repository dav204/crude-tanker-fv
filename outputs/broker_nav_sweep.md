# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.17 | +67.7% | +86.6% | +105.4% | BUY→BUY | NAV>px→NAV>px | +38 | wide-spread |
| CAPT | 0.67× | 1.04 | +38.2% | +43.1% | +48.0% | BUY→BUY | NAV>px→NAV>px | +10 | narrow-spread |
| STNG | 0.70× | 1.38 | -4.0% | +12.7% | +29.4% | HOLD→BUY | $2,725,019→NAV>px | +33 | wide-spread |
| NAT | 0.85× | 1.96 | -44.4% | -8.5% | +27.3% | TRIM/SHORT→BUY | $329,458→NAV>px | +72 | wide-spread |
| ASC | 0.75× | 1.36 | -8.1% | +8.0% | +24.1% | TRIM/SHORT→BUY | $43,209→NAV>px | +32 | wide-spread |
| TNK | 0.76× | 1.39 | +1.7% | +12.7% | +23.8% | HOLD→BUY | $39,131→NAV>px | +22 | wide-spread |
| TRMD | 0.83× | 1.26 | -7.9% | +6.7% | +21.3% | TRIM/SHORT→BUY | $76,149→NAV>px | +29 | wide-spread |
| CCEC | 0.90× | 0.96 | +37.7% | +28.6% | +19.5% | BUY→BUY | NAV>px→$2,977,992 | -18 | wide-spread |
| SBLK | 0.82× | 1.20 | -4.3% | +6.2% | +16.8% | HOLD→BUY | $27,187→NAV>px | +21 | wide-spread |
| GNK | 0.87× | 1.03 | +8.7% | +10.5% | +12.3% | BUY→BUY | $16,592→$12,421 | +4 | narrow-spread |
| HAFN | 0.95× | 1.37 | -20.8% | -5.8% | +9.1% | TRIM/SHORT→BUY | $110,531→$27,874 | +30 | wide-spread |
| INSW **(WHOLE-CO)** | 0.98× | 1.61 | -28.0% | -9.5% | +9.0% | TRIM/SHORT→BUY | $392,865→$71,592 | +37 | wide-spread |
| GSL | 0.75× | 1.28 | -18.5% | -4.9% | +8.8% | TRIM/SHORT→BUY | $2,757,173→NAV>px | +27 | wide-spread |
| DHT | 1.09× | 1.16 | -9.4% | -2.9% | +3.7% | TRIM/SHORT→HOLD | $334,603→$171,590 | +13 | wide-spread |
| CMDB | 0.62× | 0.86 | +13.5% | +6.4% | -0.7% | BUY→HOLD | NAV>px→$1,068,984 | -14 | wide-spread |
| FRO | 1.20× | 1.18 | -20.9% | -12.6% | -4.4% | TRIM/SHORT→HOLD | $375,677→$230,245 | +17 | wide-spread |
| ECO | 1.21× | 1.15 | -21.0% | -13.9% | -6.9% | TRIM/SHORT→TRIM/SHORT | $333,248→$222,848 | +14 | wide-spread |
| MPCC | 1.04× | 1.11 | -29.6% | -23.9% | -18.2% | TRIM/SHORT→TRIM/SHORT | $350,590→$180,943 | +11 | wide-spread |
| FLNG | 1.37× | 0.89 | -2.5% | -11.9% | -21.3% | HOLD→TRIM/SHORT | $3,162,500→$3,162,500 | -19 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
