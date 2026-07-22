# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 1.05-1.25 (~1.12-1.14 at the Jun-2026 fit, ~+13-17pp spread); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.22 | +45.6% | +65.5% | +85.4% | BUY→BUY | NAV>px→NAV>px | +40 | wide-spread |
| CCEC | 0.90× | 0.97 | +59.9% | +53.3% | +46.7% | BUY→BUY | NAV>px→NAV>px | -13 | wide-spread |
| STNG | 0.69× | 1.51 | -1.4% | +18.7% | +38.9% | HOLD→BUY | $67,231→NAV>px | +40 | wide-spread |
| GSL | 0.75× | 1.33 | -1.4% | +14.1% | +29.5% | HOLD→BUY | $43,684→NAV>px | +31 | wide-spread |
| TRMD | 0.82× | 1.14 | +9.6% | +17.4% | +25.2% | BUY→BUY | $34,968→NAV>px | +16 | wide-spread |
| ASC | 0.75× | 1.21 | +6.5% | +15.6% | +24.7% | BUY→BUY | $16,227→NAV>px | +18 | wide-spread |
| TNK | 0.73× | 1.45 | +2.0% | +13.3% | +24.6% | HOLD→BUY | $18,151→NAV>px | +23 | wide-spread |
| CAPT | 0.69× | 1.10 | +4.3% | +13.4% | +22.5% | HOLD→BUY | NAV>px→NAV>px | +18 | wide-spread |
| HAFN | 0.86× | 1.45 | -15.0% | +2.6% | +20.2% | TRIM/SHORT→BUY | $88,842→$7,802 | +35 | wide-spread |
| SBLK | 0.78× | 1.09 | +8.7% | +14.1% | +19.5% | BUY→BUY | $10,780→NAV>px | +11 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.73× | 1.17 | -6.5% | +5.9% | +18.4% | TRIM/SHORT→BUY | $59,342→NAV>px | +25 | wide-spread |
| SB | 0.88× | 0.88 | +32.3% | +21.0% | +9.7% | BUY→BUY | NAV>px→NAV>px | -23 | wide-spread |
| LPG | 0.84× | 1.42 | -29.1% | -12.5% | +4.1% | TRIM/SHORT→HOLD | $174,694→NAV>px | +33 | wide-spread |
| GNK | 0.89× | 1.09 | -5.7% | -0.9% | +4.0% | TRIM/SHORT→HOLD | $30,323→$14,326 | +10 | narrow-spread |
| CMDB | 0.62× | 0.93 | +10.3% | +7.0% | +3.8% | BUY→HOLD | $7,192→$15,001 | -7 | narrow-spread |
| NAT | 0.85× | 2.14 | -55.2% | -26.7% | +1.8% | TRIM/SHORT→HOLD | $425,461→NAV>px | +57 | wide-spread |
| 2343 | 0.98× | 1.02 | -2.5% | -1.5% | -0.5% | HOLD→HOLD | $18,267→$16,732 | +2 | narrow-spread |
| BRUT | 0.72× | 0.96 | +14.6% | +4.6% | -5.4% | BUY→TRIM/SHORT | NAV>px→NAV>px | -20 | wide-spread |
| MPCC | 1.04× | 1.09 | -16.3% | -11.1% | -5.8% | TRIM/SHORT→TRIM/SHORT | $117,818→$45,007 | +10 | wide-spread |
| BWLP | 0.97× | 1.30 | -31.5% | -19.7% | -8.0% | TRIM/SHORT→TRIM/SHORT | $184,952→$60,221 | +23 | wide-spread |
| INSW **(WHOLE-CO)** | 1.11× | 1.52 | -38.8% | -25.7% | -12.7% | TRIM/SHORT→TRIM/SHORT | $346,802→$153,172 | +26 | wide-spread |
| FLNG | 1.35× | 0.89 | +0.4% | -8.5% | -17.3% | HOLD→TRIM/SHORT | $192,539→$463,298 | -18 | wide-spread |
| DHT | 1.14× | 1.14 | -26.8% | -22.1% | -17.4% | TRIM/SHORT→TRIM/SHORT | $389,978→$252,874 | +9 | narrow-spread |
| FRO | 1.37× | 1.08 | -38.3% | -35.2% | -32.1% | TRIM/SHORT→TRIM/SHORT | $375,292→$316,143 | +6 | narrow-spread |
| ECO | 1.35× | 1.12 | -40.8% | -36.5% | -32.3% | TRIM/SHORT→TRIM/SHORT | $358,931→$286,838 | +9 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 1.05-1.25 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
