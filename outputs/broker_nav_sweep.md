# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.22 | +42.1% | +62.2% | +82.3% | BUY→BUY | NAV>px→NAV>px | +40 | wide-spread |
| CCEC | 0.90× | 0.97 | +50.2% | +43.4% | +36.7% | BUY→BUY | NAV>px→NAV>px | -13 | wide-spread |
| GSL | 0.75× | 1.30 | +1.2% | +15.7% | +30.1% | HOLD→BUY | $19,341→NAV>px | +29 | wide-spread |
| STNG | 0.69× | 1.53 | -10.6% | +8.6% | +27.7% | TRIM/SHORT→BUY | $73,052→NAV>px | +38 | wide-spread |
| TNK | 0.73× | 1.47 | +1.0% | +12.7% | +24.4% | HOLD→BUY | $24,452→NAV>px | +23 | wide-spread |
| CAPT | 0.69× | 1.12 | +1.1% | +11.7% | +22.3% | HOLD→BUY | NAV>px→NAV>px | +21 | wide-spread |
| ASC | 0.75× | 1.26 | -0.7% | +9.8% | +20.3% | HOLD→BUY | $21,504→NAV>px | +21 | wide-spread |
| SBLK | 0.78× | 1.12 | +5.1% | +12.2% | +19.4% | BUY→BUY | $14,427→NAV>px | +14 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.20 | -10.9% | +3.6% | +18.1% | TRIM/SHORT→BUY | $76,803→NAV>px | +29 | wide-spread |
| TRMD | 0.82× | 1.15 | -2.8% | +4.9% | +12.7% | HOLD→BUY | $37,673→NAV>px | +16 | wide-spread |
| SB | 0.88× | 0.86 | +38.6% | +24.4% | +10.3% | BUY→BUY | NAV>px→NAV>px | -28 | wide-spread |
| HAFN | 0.86× | 1.44 | -22.9% | -6.8% | +9.4% | TRIM/SHORT→BUY | $87,044→$7,871 | +32 | wide-spread |
| LPG | 0.84× | 1.33 | -23.7% | -9.6% | +4.4% | TRIM/SHORT→HOLD | $138,721→NAV>px | +28 | wide-spread |
| GNK | 0.89× | 1.13 | -9.2% | -2.7% | +3.9% | TRIM/SHORT→HOLD | $36,393→$14,378 | +13 | wide-spread |
| CMDB | 0.62× | 0.98 | +5.4% | +4.5% | +3.6% | BUY→HOLD | $12,888→$15,070 | -2 | narrow-spread |
| NAT | 0.85× | 2.17 | -56.0% | -27.1% | +1.8% | TRIM/SHORT→HOLD | $431,629→NAV>px | +58 | wide-spread |
| BRUT | 0.72× | 0.96 | +11.2% | +3.2% | -4.7% | BUY→HOLD | NAV>px→NAV>px | -16 | wide-spread |
| MPCC | 1.04× | 1.09 | -15.4% | -10.5% | -5.5% | TRIM/SHORT→TRIM/SHORT | $112,236→$44,184 | +10 | narrow-spread |
| BWLP | 0.97× | 1.21 | -25.6% | -16.6% | -7.5% | TRIM/SHORT→TRIM/SHORT | $146,334→$57,312 | +18 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.51 | -40.2% | -27.4% | -14.7% | TRIM/SHORT→TRIM/SHORT | $349,114→$154,276 | +25 | wide-spread |
| DHT | 1.14× | 1.11 | -24.9% | -21.1% | -17.3% | TRIM/SHORT→TRIM/SHORT | $360,665→$249,874 | +8 | narrow-spread |
| FLNG | 1.35× | 0.88 | -2.7% | -12.0% | -21.3% | HOLD→TRIM/SHORT | $162,859→$452,584 | -19 | wide-spread |
| ECO | 1.35× | 1.13 | -41.6% | -36.9% | -32.3% | TRIM/SHORT→TRIM/SHORT | $369,687→$289,955 | +9 | narrow-spread |
| FRO | 1.37× | 1.10 | -39.9% | -36.1% | -32.3% | TRIM/SHORT→TRIM/SHORT | $400,872→$325,714 | +8 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
