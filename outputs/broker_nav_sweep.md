# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.41× | 1.17 | +38.2% | +52.7% | +67.2% | BUY→BUY | NAV>px→NAV>px | +29 | wide-spread |
| CCEC | 0.90× | 0.99 | +49.6% | +48.2% | +46.8% | BUY→BUY | NAV>px→NAV>px | -3 | narrow-spread |
| CAPT | 0.72× | 1.26 | -3.5% | +17.4% | +38.2% | HOLD→BUY | $230,787→NAV>px | +42 | wide-spread |
| STNG | 0.73× | 1.65 | -10.1% | +11.3% | +32.8% | TRIM/SHORT→BUY | $135,607→NAV>px | +43 | wide-spread |
| GSL | 0.75× | 1.41 | -5.7% | +10.8% | +27.3% | TRIM/SHORT→BUY | $133,760→NAV>px | +33 | wide-spread |
| ASC | 0.75× | 1.39 | -11.8% | +4.9% | +21.5% | TRIM/SHORT→BUY | $39,759→NAV>px | +33 | wide-spread |
| TRMD | 0.92× | 1.14 | +1.6% | +8.6% | +15.6% | HOLD→BUY | $59,764→$26,726 | +14 | wide-spread |
| NAT | 0.85× | 2.54 | -58.9% | -24.8% | +9.2% | TRIM/SHORT→BUY | $741,163→NAV>px | +68 | wide-spread |
| BRUT | 1.03× | 1.00 | +6.5% | +6.1% | +5.7% | BUY→BUY | $201,672→$209,808 | -1 | narrow-spread |
| TNK | 0.91× | 1.47 | -15.3% | -5.1% | +5.1% | TRIM/SHORT→BUY | $231,134→$15,285 | +20 | wide-spread |
| HAFN | 1.03× | 1.69 | -41.6% | -19.7% | +2.1% | TRIM/SHORT→HOLD | $198,602→$59,985 | +44 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.22 | -30.1% | -17.6% | -5.1% | TRIM/SHORT→TRIM/SHORT | $205,068→$34,949 | +25 | wide-spread |
| SBLK | 0.91× | 1.01 | -7.0% | -6.3% | -5.7% | TRIM/SHORT→TRIM/SHORT | $16,536→$14,278 | +1 | narrow-spread |
| DHT | 1.14× | 1.23 | -23.8% | -15.7% | -7.6% | TRIM/SHORT→TRIM/SHORT | $727,441→$401,502 | +16 | wide-spread |
| MPCC | 1.04× | 1.20 | -26.4% | -17.4% | -8.5% | TRIM/SHORT→TRIM/SHORT | $203,942→$58,763 | +18 | wide-spread |
| GNK | 0.95× | 1.09 | -19.7% | -15.7% | -11.7% | TRIM/SHORT→TRIM/SHORT | $39,276→$24,599 | +8 | narrow-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.55 | -41.3% | -28.1% | -14.9% | TRIM/SHORT→TRIM/SHORT | $544,843→$279,658 | +26 | wide-spread |
| LPG | 1.06× | 1.47 | -41.5% | -29.6% | -17.6% | TRIM/SHORT→TRIM/SHORT | $348,720→$145,934 | +24 | wide-spread |
| FRO | 1.33× | 1.28 | -40.5% | -30.8% | -21.0% | TRIM/SHORT→TRIM/SHORT | $792,214→$504,378 | +19 | wide-spread |
| FLNG | 1.44× | 0.90 | -6.8% | -14.5% | -22.2% | TRIM/SHORT→TRIM/SHORT | $311,365→$556,262 | -15 | wide-spread |
| SB | 1.13× | 0.81 | +8.2% | -7.6% | -23.5% | BUY→TRIM/SHORT | NAV>px→$57,869 | -32 | wide-spread |
| 2343 | 1.24× | 1.07 | -31.6% | -29.2% | -26.8% | TRIM/SHORT→TRIM/SHORT | $43,127→$37,942 | +5 | narrow-spread |
| CMDB | 0.84× | 0.83 | -16.4% | -22.0% | -27.6% | TRIM/SHORT→TRIM/SHORT | $34,154→$51,645 | -11 | wide-spread |
| BWLP | 1.27× | 1.19 | -41.7% | -35.4% | -29.1% | TRIM/SHORT→TRIM/SHORT | $272,330→$193,480 | +13 | wide-spread |
| ECO | 1.47× | 1.20 | -42.1% | -35.9% | -29.6% | TRIM/SHORT→TRIM/SHORT | $705,140→$544,143 | +12 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
