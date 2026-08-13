# Broker-NAV sensitivity sweep

Each name valued at three vessel-mark levels: **tool marks** (k=1.00, transaction-anchored since 2026-06-09), **midpoint**, and **broker-equivalent** (k lifts the tool NAV to the consensus broker NAV = price / consensus P/NAV). EV% = probability-weighted scenario FV vs price (crude-allocated for hybrids). k_broker is two-regime: on transaction-anchored sectors (crude/product/dry-bulk) it is the broker premium over transaction levels, and validated pure-plays are EXPECTED inside the uniform band k 0.95-1.15 (re-pinned 2026-08-09 at the marks-trail war-tape fit, ~1.00-1.04 observed; was 1.05-1.25 at the Jun-2026 fit); on un-anchored sectors (LNG, containerships) it keeps the original broker-vs-independent-curve reading (validated ≈ 1.0). The **Read** column is mechanical spread width only — per-name mark-driven / mark-validated classification lives in METHODOLOGY 6.

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |
|---|--:|--:|--:|--:|--:|---|--:|--:|---|
| TEN | 0.34× | 1.22 | +58.9% | +80.8% | +102.6% | BUY→BUY | NAV>px→NAV>px | +44 | wide-spread |
| CCEC | 0.90× | 0.99 | +49.2% | +47.9% | +46.7% | BUY→BUY | NAV>px→NAV>px | -2 | narrow-spread |
| CAPT | 0.71× | 1.17 | +11.0% | +26.0% | +41.1% | BUY→BUY | $53,520→NAV>px | +30 | wide-spread |
| STNG | 0.71× | 1.51 | +0.8% | +19.7% | +38.6% | HOLD→BUY | $68,460→NAV>px | +38 | wide-spread |
| GSL | 0.75× | 1.29 | +4.0% | +17.0% | +30.0% | HOLD→BUY | NAV>px→NAV>px | +26 | wide-spread |
| TRMD | 0.86× | 1.09 | +15.9% | +21.4% | +27.0% | BUY→BUY | $33,992→$12,078 | +11 | wide-spread |
| BRUT | 0.86× | 0.92 | +61.8% | +44.0% | +26.3% | BUY→BUY | NAV>px→NAV>px | -36 | wide-spread |
| ASC | 0.75× | 1.26 | -1.8% | +10.7% | +23.1% | HOLD→BUY | $21,702→NAV>px | +25 | wide-spread |
| TNK | 0.80× | 1.33 | +3.5% | +12.4% | +21.3% | HOLD→BUY | $49,193→NAV>px | +18 | wide-spread |
| HAFN | 0.92× | 1.39 | -12.5% | +3.4% | +19.3% | TRIM/SHORT→BUY | $95,853→$24,018 | +32 | wide-spread |
| NAT | 0.85× | 2.22 | -52.6% | -20.6% | +11.4% | TRIM/SHORT→BUY | $617,242→NAV>px | +64 | wide-spread |
| 2343 | 0.91× | 1.05 | +1.4% | +3.8% | +6.2% | HOLD→BUY | $14,262→$11,346 | +5 | narrow-spread |
| SB | 0.88× | 0.88 | +27.8% | +16.0% | +4.2% | BUY→HOLD | NAV>px→NAV>px | -24 | wide-spread |
| SBLK | 0.89× | 0.96 | +6.8% | +4.7% | +2.5% | BUY→HOLD | $8,480→$13,204 | -4 | narrow-spread |
| CMDB | 0.62× | 0.87 | +13.7% | +7.8% | +1.9% | BUY→HOLD | NAV>px→$14,626 | -12 | wide-spread |
| CMBT **(WHOLE-CO)** | 0.85× | 1.12 | -14.2% | -6.1% | +1.9% | TRIM/SHORT→BUY | $120,740→$30,426 | +16 | wide-spread |
| GNK | 0.92× | 1.07 | -10.2% | -6.5% | -2.7% | TRIM/SHORT→HOLD | $31,418→$19,118 | +8 | narrow-spread |
| DHT | 1.08× | 1.14 | -15.2% | -9.6% | -4.1% | TRIM/SHORT→HOLD | $489,951→$279,182 | +11 | wide-spread |
| MPCC | 1.04× | 1.11 | -18.8% | -12.6% | -6.5% | TRIM/SHORT→TRIM/SHORT | $136,966→$48,452 | +12 | wide-spread |
| LPG | 0.96× | 1.33 | -28.9% | -18.7% | -8.6% | TRIM/SHORT→TRIM/SHORT | $208,723→$67,351 | +20 | wide-spread |
| INSW **(WHOLE-CO)** | 1.17× | 1.45 | -35.7% | -23.8% | -11.9% | TRIM/SHORT→TRIM/SHORT | $468,801→$241,493 | +24 | wide-spread |
| FRO | 1.31× | 1.13 | -30.3% | -24.8% | -19.2% | TRIM/SHORT→TRIM/SHORT | $540,231→$406,359 | +11 | wide-spread |
| BWLP | 1.13× | 1.19 | -34.5% | -27.5% | -20.4% | TRIM/SHORT→TRIM/SHORT | $207,795→$129,486 | +14 | wide-spread |
| FLNG | 1.43× | 0.85 | +4.0% | -8.3% | -20.6% | HOLD→TRIM/SHORT | $135,338→$499,557 | -25 | wide-spread |
| ECO | 1.34× | 1.15 | -34.1% | -28.8% | -23.6% | TRIM/SHORT→TRIM/SHORT | $549,197→$425,696 | +11 | wide-spread |

_**(WHOLE-CO)** = hybrid name valued via crude + product sleeve carve-outs aggregated against the whole-company tape price (METHODOLOGY 6 v2). The breakeven shown is the crude-sleeve breakeven (proxy)._


_On txn-anchored sectors, k_broker inside the 0.95-1.15 pure-play band ⇒ the broker premium is the expected uniform one (mark-validated); k_broker outside the band (either side) ⇒ the name's apparent cheapness/richness is partly a NAV-mark choice (mark-driven — see the METHODOLOGY 6 entry for the per-name thesis). Pre-2026-06-09, validated read as k ≈ 1.0; that semantics survives only on un-anchored sectors. Uniform k also lifts the disposal-validated old-age leg (a known overshoot); leg-specific recalibration is the follow-up (METHODOLOGY 9)._
