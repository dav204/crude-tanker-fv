# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.41× | 1.23 | +29.0% | +47.6% | +66.2% | BUY→BUY | NAV>px→NAV>px | +37 | wide-spread |
| CCEC | 0.90× | 0.99 | +51.0% | +49.1% | +47.2% | BUY→BUY | NAV>px→NAV>px | -4 | narrow-spread |
| CAPT | 0.72× | 1.28 | -5.9% | +16.0% | +38.0% | TRIM/SHORT→BUY | $274,660→NAV>px | +44 | wide-spread |
| STNG | 0.73× | 1.65 | -10.1% | +11.3% | +32.8% | TRIM/SHORT→BUY | $135,680→NAV>px | +43 | wide-spread |
| GSL | 0.75× | 1.41 | -6.3% | +10.4% | +27.2% | TRIM/SHORT→BUY | $142,540→NAV>px | +33 | wide-spread |
| ASC | 0.75× | 1.41 | -12.8% | +4.3% | +21.5% | TRIM/SHORT→BUY | $41,868→NAV>px | +34 | wide-spread |
| TRMD | 0.92× | 1.15 | +0.2% | +7.8% | +15.3% | HOLD→BUY | $63,131→$26,845 | +15 | wide-spread |
| NAT | 0.85× | 2.62 | -60.2% | -25.7% | +8.9% | TRIM/SHORT→BUY | $778,983→NAV>px | +69 | wide-spread |
| BRUT | 1.03× | 0.99 | +7.0% | +6.4% | +5.8% | BUY→BUY | $196,633→$209,215 | -1 | narrow-spread |
| TNK | 0.91× | 1.53 | -17.4% | -6.3% | +4.8% | TRIM/SHORT→HOLD | $258,112→$16,071 | +22 | wide-spread |
| HAFN | 1.03× | 1.69 | -41.7% | -19.8% | +2.1% | TRIM/SHORT→HOLD | $199,301→$60,079 | +44 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.22 | -31.7% | -19.1% | -6.6% | TRIM/SHORT→TRIM/SHORT | $208,228→$34,853 | +25 | wide-spread |
| SBLK | 0.91× | 1.03 | -9.3% | -8.1% | -6.9% | TRIM/SHORT→TRIM/SHORT | $18,888→$14,496 | +2 | narrow-spread |
| DHT | 1.14× | 1.26 | -25.8% | -16.9% | -8.0% | TRIM/SHORT→TRIM/SHORT | $782,633→$413,727 | +18 | wide-spread |
| MPCC | 1.04× | 1.20 | -26.3% | -17.4% | -8.5% | TRIM/SHORT→TRIM/SHORT | $202,981→$58,613 | +18 | wide-spread |
| GNK | 0.95× | 1.09 | -21.2% | -17.1% | -13.1% | TRIM/SHORT→TRIM/SHORT | $46,066→$25,058 | +8 | narrow-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.58 | -42.2% | -28.6% | -15.0% | TRIM/SHORT→TRIM/SHORT | $560,027→$283,727 | +27 | wide-spread |
| LPG | 1.06× | 1.50 | -42.3% | -30.0% | -17.7% | TRIM/SHORT→TRIM/SHORT | $359,856→$147,651 | +25 | wide-spread |
| FRO | 1.33× | 1.30 | -41.5% | -31.4% | -21.2% | TRIM/SHORT→TRIM/SHORT | $817,484→$512,706 | +20 | wide-spread |
| FLNG | 1.44× | 0.90 | -7.0% | -14.6% | -22.2% | TRIM/SHORT→TRIM/SHORT | $316,222→$558,215 | -15 | wide-spread |
| SB | 1.13× | 0.82 | +5.2% | -9.7% | -24.7% | BUY→TRIM/SHORT | NAV>px→$59,141 | -30 | wide-spread |
| 2343 | 1.24× | 1.06 | -31.3% | -29.2% | -27.0% | TRIM/SHORT→TRIM/SHORT | $42,275→$37,682 | +4 | narrow-spread |
| CMDB | 0.84× | 0.88 | -21.0% | -24.8% | -28.5% | TRIM/SHORT→TRIM/SHORT | $46,840→$64,071 | -7 | narrow-spread |
| BWLP | 1.27× | 1.20 | -42.3% | -35.7% | -29.1% | TRIM/SHORT→TRIM/SHORT | $278,732→$195,360 | +13 | wide-spread |
| ECO | 1.47× | 1.24 | -44.6% | -37.3% | -30.0% | TRIM/SHORT→TRIM/SHORT | $762,978→$566,844 | +15 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
