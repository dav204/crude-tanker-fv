# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.30 | +46.3% | +74.0% | +101.7% | BUY→BUY | NAV>px→NAV>px | +55 | wide-spread |
| CCEC | 0.90× | 0.99 | +49.1% | +47.9% | +46.7% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| CAPT | 0.72× | 1.19 | +4.3% | +20.9% | +37.6% | HOLD→BUY | $103,260→NAV>px | +33 | wide-spread |
| STNG | 0.73× | 1.54 | -3.6% | +15.5% | +34.7% | HOLD→BUY | $91,722→NAV>px | +38 | wide-spread |
| GSL | 0.75× | 1.38 | -3.6% | +12.3% | +28.1% | HOLD→BUY | $105,558→NAV>px | +32 | wide-spread |
| ASC | 0.75× | 1.34 | -7.4% | +7.6% | +22.6% | TRIM/SHORT→BUY | $31,809→NAV>px | +30 | wide-spread |
| TRMD | 0.92× | 1.10 | +7.8% | +13.1% | +18.4% | BUY→BUY | $47,363→$24,985 | +11 | wide-spread |
| NAT | 0.85× | 2.44 | -56.6% | -22.8% | +11.1% | TRIM/SHORT→BUY | $699,898→NAV>px | +68 | wide-spread |
| TNK | 0.91× | 1.25 | -4.9% | +1.2% | +7.4% | HOLD→BUY | $126,027→$12,153 | +12 | wide-spread |
| HAFN | 1.03× | 1.57 | -34.9% | -14.7% | +5.5% | TRIM/SHORT→BUY | $163,423→$53,657 | +40 | wide-spread |
| BRUT | 1.03× | 0.99 | +2.9% | +2.1% | +1.3% | HOLD→HOLD | $211,075→$230,885 | -2 | narrow-spread |
| CMDB | 0.62× | 1.01 | -4.6% | -4.1% | -3.5% | HOLD→HOLD | $16,463→$15,059 | +1 | narrow-spread |
| CMBT **(WHOLE-CO)** | 0.86× | 1.17 | -25.3% | -15.0% | -4.7% | TRIM/SHORT→TRIM/SHORT | $165,601→$35,337 | +21 | wide-spread |
| SBLK | 0.91× | 1.02 | -7.9% | -6.8% | -5.8% | TRIM/SHORT→TRIM/SHORT | $18,075→$14,315 | +2 | narrow-spread |
| MPCC | 1.04× | 1.20 | -25.7% | -16.5% | -7.3% | TRIM/SHORT→TRIM/SHORT | $199,994→$56,057 | +18 | wide-spread |
| DHT | 1.14× | 1.14 | -18.9% | -13.7% | -8.6% | TRIM/SHORT→TRIM/SHORT | $588,906→$383,697 | +10 | wide-spread |
| GNK | 0.95× | 1.06 | -17.5% | -14.5% | -11.5% | TRIM/SHORT→TRIM/SHORT | $34,874→$24,191 | +6 | narrow-spread |
| INSW **(WHOLE-CO)** | 1.21× | 1.52 | -40.3% | -27.6% | -15.0% | TRIM/SHORT→TRIM/SHORT | $546,679→$286,760 | +25 | wide-spread |
| LPG | 1.06× | 1.37 | -37.4% | -27.4% | -17.3% | TRIM/SHORT→TRIM/SHORT | $297,378→$138,017 | +20 | wide-spread |
| FRO | 1.33× | 1.20 | -36.2% | -28.8% | -21.3% | TRIM/SHORT→TRIM/SHORT | $720,125→$500,813 | +15 | wide-spread |
| FLNG | 1.44× | 0.90 | -6.3% | -14.2% | -22.2% | TRIM/SHORT→TRIM/SHORT | $303,810→$553,225 | -16 | wide-spread |
| SB | 1.13× | 0.83 | +3.7% | -10.0% | -23.7% | HOLD→TRIM/SHORT | NAV>px→$60,694 | -27 | wide-spread |
| 2343 | 1.24× | 1.03 | -28.7% | -27.6% | -26.5% | TRIM/SHORT→TRIM/SHORT | $38,973→$36,717 | +2 | narrow-spread |
| BWLP | 1.27× | 1.18 | -41.0% | -35.0% | -29.0% | TRIM/SHORT→TRIM/SHORT | $266,288→$191,705 | +12 | wide-spread |
| ECO | 1.47× | 1.13 | -38.6% | -34.2% | -29.8% | TRIM/SHORT→TRIM/SHORT | $644,288→$532,390 | +9 | narrow-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
