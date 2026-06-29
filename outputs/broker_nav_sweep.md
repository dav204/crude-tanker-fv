# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.13 | +83.1% | +97.8% | +112.5% | BUY→BUY | NAV>px→NAV>px | +29 | wide-spread |
| BRUT | 0.75× | 0.92 | +107.4% | +84.5% | +61.7% | BUY→BUY | NAV>px→NAV>px | -46 | wide-spread |
| CAPT | 0.67× | 1.12 | +35.6% | +48.2% | +60.9% | BUY→BUY | NAV>px→NAV>px | +25 | wide-spread |
| CCEC | 0.90× | 0.95 | +72.0% | +61.0% | +50.0% | BUY→BUY | NAV>px→NAV>px | -22 | wide-spread |
| STNG | 0.70× | 1.27 | +14.1% | +26.5% | +38.8% | BUY→BUY | $10,829→NAV>px | +25 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.74× | 1.12 | +14.1% | +24.2% | +34.3% | BUY→BUY | $41,510→NAV>px | +20 | wide-spread |
| TNK | 0.76× | 1.20 | +20.6% | +26.8% | +33.0% | BUY→BUY | NAV>px→NAV>px | +12 | wide-spread |
| GSL | 0.75× | 1.24 | +7.6% | +19.7% | +31.9% | BUY→BUY | NAV>px→NAV>px | +24 | wide-spread |
| TRMD | 0.83× | 1.17 | +3.8% | +14.3% | +24.7% | HOLD→BUY | $48,537→$7,012 | +21 | wide-spread |
| ASC | 0.75× | 1.33 | -5.3% | +9.5% | +24.3% | TRIM/SHORT→BUY | $32,539→NAV>px | +30 | wide-spread |
| NAT | 0.85× | 2.14 | -51.9% | -14.8% | +22.3% | TRIM/SHORT→BUY | $397,445→NAV>px | +74 | wide-spread |
| SBLK | 0.82× | 1.09 | +5.8% | +11.3% | +16.9% | BUY→BUY | $16,572→NAV>px | +11 | wide-spread |
| HAFN | 0.95× | 1.30 | -13.8% | -1.1% | +11.7% | TRIM/SHORT→BUY | $83,976→$29,748 | +26 | wide-spread |
| INSW **(WHOLE-CO)** | 0.98× | 1.51 | -21.2% | -5.0% | +11.2% | TRIM/SHORT→BUY | $262,650→$70,065 | +32 | wide-spread |
| GNK | 0.87× | 1.11 | -1.4% | +4.6% | +10.6% | HOLD→BUY | $26,698→$12,255 | +12 | wide-spread |
| SB | 0.88× | 0.77 | +52.0% | +31.2% | +10.4% | BUY→BUY | NAV>px→NAV>px | -42 | wide-spread |
| CMDB | 0.62× | 0.91 | +13.6% | +9.7% | +5.8% | BUY→BUY | $5,949→$14,626 | -8 | narrow-spread |
| DHT | 1.09× | 1.17 | -12.7% | -5.8% | +1.1% | TRIM/SHORT→HOLD | $379,413→$204,295 | +14 | wide-spread |
| MPCC | 1.04× | 1.14 | -19.6% | -12.0% | -4.3% | TRIM/SHORT→HOLD | $157,594→$49,535 | +15 | wide-spread |
| FRO | 1.20× | 1.14 | -18.7% | -11.8% | -4.9% | TRIM/SHORT→HOLD | $338,039→$227,490 | +14 | wide-spread |
| ECO | 1.21× | 1.13 | -19.0% | -13.0% | -7.1% | TRIM/SHORT→TRIM/SHORT | $292,039→$211,357 | +12 | wide-spread |
| FLNG | 1.37× | 0.87 | +4.7% | -6.5% | -17.7% | HOLD→TRIM/SHORT | $124,006→$453,302 | -22 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
