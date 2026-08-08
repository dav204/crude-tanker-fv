# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.22 | +45.2% | +65.7% | +86.2% | BUY→BUY | NAV>px→NAV>px | +41 | wide-spread |
| CCEC | 0.90× | 0.97 | +60.5% | +53.7% | +46.9% | BUY→BUY | NAV>px→NAV>px | -14 | wide-spread |
| STNG | 0.69× | 1.47 | +1.0% | +20.1% | +39.2% | HOLD→BUY | $57,165→NAV>px | +38 | wide-spread |
| GSL | 0.75× | 1.37 | -4.5% | +12.1% | +28.7% | HOLD→BUY | $75,049→NAV>px | +33 | wide-spread |
| TRMD | 0.82× | 1.15 | +8.1% | +16.5% | +24.9% | BUY→BUY | $37,928→NAV>px | +17 | wide-spread |
| ASC | 0.75× | 1.29 | +0.8% | +12.6% | +24.3% | HOLD→BUY | $24,202→NAV>px | +23 | wide-spread |
| CAPT | 0.69× | 1.17 | -4.0% | +10.0% | +24.1% | HOLD→BUY | $19,107→NAV>px | +28 | wide-spread |
| TNK | 0.73× | 1.61 | -4.6% | +9.7% | +24.0% | HOLD→BUY | $64,022→NAV>px | +29 | wide-spread |
| HAFN | 0.86× | 1.48 | -17.1% | +1.3% | +19.7% | TRIM/SHORT→BUY | $94,422→$7,648 | +37 | wide-spread |
| SBLK | 0.78× | 1.17 | -1.0% | +8.4% | +17.8% | HOLD→BUY | $19,951→NAV>px | +19 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.22 | -13.4% | +2.2% | +17.7% | TRIM/SHORT→BUY | $86,221→NAV>px | +31 | wide-spread |
| SB | 0.88× | 0.91 | +24.6% | +16.5% | +8.5% | BUY→BUY | NAV>px→NAV>px | -16 | wide-spread |
| LPG | 0.84× | 1.50 | -33.2% | -14.7% | +3.8% | TRIM/SHORT→HOLD | $206,288→NAV>px | +37 | wide-spread |
| CMDB | 0.62× | 0.86 | +16.8% | +10.3% | +3.7% | BUY→HOLD | NAV>px→$14,830 | -13 | wide-spread |
| GNK | 0.89× | 1.08 | -4.9% | -0.8% | +3.2% | HOLD→HOLD | $27,848→$14,242 | +8 | narrow-spread |
| NAT | 0.85× | 2.23 | -56.8% | -27.2% | +2.3% | TRIM/SHORT→HOLD | $459,263→NAV>px | +59 | wide-spread |
| BRUT | 0.72× | 1.00 | +0.7% | +1.4% | +2.1% | HOLD→HOLD | NAV>px→NAV>px | +1 | narrow-spread |
| 2343 | 0.98× | 1.21 | -19.9% | -11.3% | -2.8% | TRIM/SHORT→HOLD | $35,266→$18,824 | +17 | wide-spread |
| MPCC | 1.04× | 1.12 | -19.4% | -12.9% | -6.5% | TRIM/SHORT→TRIM/SHORT | $141,591→$48,690 | +13 | wide-spread |
| BWLP | 0.97× | 1.32 | -33.0% | -20.6% | -8.2% | TRIM/SHORT→TRIM/SHORT | $196,627→$61,101 | +25 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.59 | -41.1% | -26.9% | -12.7% | TRIM/SHORT→TRIM/SHORT | $379,056→$159,674 | +28 | wide-spread |
| DHT | 1.14× | 1.18 | -29.4% | -23.3% | -17.1% | TRIM/SHORT→TRIM/SHORT | $453,752→$267,029 | +12 | wide-spread |
| FLNG | 1.35× | 0.90 | -0.5% | -9.0% | -17.4% | HOLD→TRIM/SHORT | $207,648→$468,753 | -17 | wide-spread |
| FRO | 1.37× | 1.13 | -41.8% | -36.8% | -31.8% | TRIM/SHORT→TRIM/SHORT | $440,847→$339,112 | +10 | narrow-spread |
| ECO | 1.35× | 1.23 | -47.4% | -39.9% | -32.4% | TRIM/SHORT→TRIM/SHORT | $466,032→$323,230 | +15 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
