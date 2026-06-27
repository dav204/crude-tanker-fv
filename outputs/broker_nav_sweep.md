# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.16 | +76.8% | +94.4% | +112.0% | BUY→BUY | NAV>px→NAV>px | +35 | wide-spread |
| CAPT | 0.67× | 1.15 | +31.1% | +46.2% | +61.2% | BUY→BUY | NAV>px→NAV>px | +30 | wide-spread |
| BRUT | 0.75× | 0.92 | +102.4% | +81.6% | +60.9% | BUY→BUY | NAV>px→NAV>px | -41 | wide-spread |
| CCEC | 0.90× | 0.95 | +73.4% | +61.8% | +50.3% | BUY→BUY | NAV>px→NAV>px | -23 | wide-spread |
| STNG | 0.70× | 1.32 | +10.2% | +24.3% | +38.4% | BUY→BUY | $23,127→NAV>px | +28 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.74× | 1.14 | +11.0% | +23.2% | +35.4% | BUY→BUY | $54,596→NAV>px | +24 | wide-spread |
| TNK | 0.76× | 1.26 | +17.1% | +24.8% | +32.4% | BUY→BUY | NAV>px→NAV>px | +15 | wide-spread |
| GSL | 0.75× | 1.24 | +7.4% | +19.6% | +31.9% | BUY→BUY | NAV>px→NAV>px | +24 | wide-spread |
| ASC | 0.75× | 1.26 | +0.2% | +12.4% | +24.7% | HOLD→BUY | $25,023→NAV>px | +25 | wide-spread |
| TRMD | 0.83× | 1.19 | +1.9% | +13.1% | +24.4% | HOLD→BUY | $52,226→$6,749 | +22 | wide-spread |
| NAT | 0.85× | 2.16 | -52.5% | -15.2% | +22.1% | TRIM/SHORT→BUY | $404,139→NAV>px | +75 | wide-spread |
| SBLK | 0.82× | 1.10 | +5.6% | +11.2% | +16.9% | BUY→BUY | $16,931→$5,154 | +11 | wide-spread |
| HAFN | 0.95× | 1.32 | -15.2% | -1.9% | +11.4% | TRIM/SHORT→BUY | $87,353→$29,992 | +27 | wide-spread |
| GNK | 0.87× | 1.03 | +7.8% | +9.3% | +10.8% | BUY→BUY | $15,973→$12,402 | +3 | narrow-spread |
| INSW **(WHOLE-CO)** | 0.98× | 1.54 | -22.8% | -6.0% | +10.8% | TRIM/SHORT→BUY | $276,426→$71,380 | +34 | wide-spread |
| CMDB | 0.62× | 0.85 | +20.9% | +13.5% | +6.0% | BUY→BUY | NAV>px→$14,735 | -15 | wide-spread |
| DHT | 1.09× | 1.21 | -15.5% | -7.5% | +0.6% | TRIM/SHORT→HOLD | $423,096→$212,406 | +16 | wide-spread |
| MPCC | 1.04× | 1.14 | -19.3% | -11.8% | -4.3% | TRIM/SHORT→HOLD | $155,119→$49,153 | +15 | wide-spread |
| FRO | 1.20× | 1.15 | -18.9% | -11.9% | -4.9% | TRIM/SHORT→HOLD | $339,908→$227,971 | +14 | wide-spread |
| ECO | 1.21× | 1.15 | -20.6% | -13.8% | -7.1% | TRIM/SHORT→TRIM/SHORT | $304,990→$212,429 | +14 | wide-spread |
| FLNG | 1.37× | 0.87 | +4.1% | -6.9% | -17.8% | HOLD→TRIM/SHORT | $134,259→$457,099 | -22 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
