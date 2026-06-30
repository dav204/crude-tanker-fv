# Book-wide scorecard (Thread 4)

## Verdict — the consolidated read (one row per name)

FV vs current price, position, and the broker-NAV bug-gate on the **same row** as the confidence tier. **This is the single handoff surface**: a downstream sizing decision reads HERE — the per-gate validation detail is the matrix in the next section, same file. A **PROVISIONAL** name is ⛔ **not handoff-ready** — do not pass its FV to a position call. Crude `rich`/TRIM reads are cycle position, not shorts (§12); see the caveat below.

| Ticker | Sector | **Tier** | Price | Model FV | Upside | Position | NAV/sh | Broker NAV | Gap | SANITY | Handoff |
|---|---|---|--:|--:|--:|:--|--:|--:|--:|:--|:--|
| DHT | crude | VALIDATED-TIGHT | $17.08 | $14.95 | -12% | TRIM/SHORT (overvalued) | $13.88 | $15.67 | -11% | OK | ready |
| FRO | crude | VALIDATED-TIGHT | $35.44 | $26.54 | -25% | TRIM/SHORT (overvalued) | $24.22 | $29.53 | -18% | OK | ready |
| TNK | crude | VALIDATED-TIGHT | $65.99 | $79.42 | +20% | BUY (undervalued) | $77.51 | $86.83 | -11% | OK | ready |
| SB | dry_bulk | VALIDATED-TIGHT | $6.36 | $10.17 | +60% | BUY (undervalued) | $10.47 | $7.23 (apx) | +45% | n-a | ready |
| SBLK | dry_bulk | VALIDATED-TIGHT | $24.64 | $28.34 | +15% | BUY (undervalued) | $29.34 | $30.05 | -2% | OK | ready |
| CAPT | crude | GOVERNED-WIDE | $12.73 | $16.03 | +26% | BUY (undervalued) | $15.49 | $19.00 | -18% | OK | ready |
| CMBT | crude | GOVERNED-WIDE | $14.08 | $15.26 | +8% | BUY (undervalued) | $15.87 | $19.03 | -17% | OK | ready |
| INSW | crude | GOVERNED-WIDE | $77.81 | $38.63 | -50% | TRIM/SHORT (overvalued) | $52.59 | $79.40 | -34% | OK | ready |
| TEN | crude | GOVERNED-WIDE | $35.76 | $61.29 | +71% | BUY (undervalued) | $88.70 | $105.18 (apx) | -16% | n-a | ready |
| CMDB | dry_bulk | GOVERNED-WIDE | $17.99 | $20.43 | +14% | BUY (undervalued) | $31.33 | $29.02 (apx) | +8% | n-a | ready |
| GNK | dry_bulk | GOVERNED-WIDE | $24.39 | $23.99 | -2% | HOLD (fairly valued) | $24.69 | $28.03 | -12% | OK | ready |
| CCEC | lng | GOVERNED-WIDE | $20.87 | $32.08 | +54% | BUY (undervalued) | $28.10 | $23.19 (apx) | +21% | n-a | ready |
| FLNG | lng | GOVERNED-WIDE | $29.29 | $28.16 | -4% | HOLD (fairly valued) | $28.45 | $21.38 | +33% | OK | ready |
| GSL | containerships | GOVERNED-WIDE | $37.74 | $43.00 | +14% | BUY (undervalued) | $38.59 | $50.32 (apx) | -23% | n-a | ready |
| MPCC | containerships | GOVERNED-WIDE | $2.62 | $2.19 | -16% | TRIM/SHORT (overvalued) | $2.02 | $2.52 (apx) | -20% | n-a | ready |
| BRUT | crude | PROVISIONAL ⛔ | $5.21 | $9.84 | +89% | BUY (undervalued) | $9.40 | $6.95 | +35% | OK | **NO** |
| ECO | crude | PROVISIONAL ⛔ | $49.60 | $37.33 | -25% | TRIM/SHORT (overvalued) | $34.56 | $40.99 | -16% | OK | **NO** |
| NAT | crude | PROVISIONAL ⛔ | $5.78 | $2.51 | -57% | TRIM/SHORT (overvalued) | $2.07 | $6.80 (apx) | -70% | n-a | **NO** |
| ASC | product | PROVISIONAL ⛔ | $16.00 | $15.09 | -6% | TRIM/SHORT (overvalued) | $15.93 | $21.33 (apx) | -25% | n-a | **NO** |
| HAFN | product | PROVISIONAL ⛔ | $6.86 | $5.66 | -17% | TRIM/SHORT (overvalued) | $5.22 | $7.22 | -28% | OK | **NO** |
| STNG | product | PROVISIONAL ⛔ | $70.09 | $78.93 | +13% | BUY (undervalued) | $80.35 | $100.13 | -20% | OK | **NO** |
| TRMD | product | PROVISIONAL ⛔ | $26.31 | $26.35 | +0% | HOLD (fairly valued) | $25.43 | $31.70 | -20% | OK | **NO** |

## Validation matrix — per-gate detail

Every covered name on ONE consistent, validated machine. **The product is the *boundary of what's comparable*, not a buy list.** `pending` ≠ `passed`: a name with a registered-pending gate is shown pending, never blessed. NAV age-0 basis is the uniform **xclusiv Resale** line (2026-06-22); mid-age is transaction-anchored (§9.9).

**Gates per name:** (1) NAV-basis (resale-uniform ⇒ comparable; else flagged); (2) Justified P/NAV both bases (§17); (3) parity band (§A1.2); (4) §18.5a mean-reversion (Thread 3, data-pending); (5) §18.5b orderbook cross-check (Thread 5, data-pending); (6) robust vs flips (does the read survive the parity↔historical choice).

**Confidence tier (governance handoff):** the FV's reliability for a sizing decision, read from the validation state above — **VALIDATED-TIGHT** (traced basis + robust across both §17 bases — broker OR internal two-basis corroboration; SB-class), **GOVERNED-WIDE** (NAV traces but rests on a structural-unavailable input or a read that flips — usable directional anchor, wide band; CMBT-class), **PROVISIONAL** (a NAV-driving figure is uncited / off-basis — **NOT handoff-ready, flag don't pass**; NAT-class). APPROX-pnav does not demote a robust name; an immaterial uncited operating-scrubber surface does not either (see provenance.py).

| Ticker | Sector | **Tier** | NAV-basis | P/NAV(mkt) | Read par→hist | Robust? | Parity band | §18.5a | §18.5b | Verdict |
|---|---|---|---|--:|---|---|---|---|---|---|
| BRUT | crude | PROVISIONAL ⛔ | resale-uniform | 0.57× | newbuild-heavy (unreliable)→newbuild-heavy (unreliable) | n/a | clears | pending | pending | no justified multiple (newbuild-heavy (unreliable)) |
| CAPT | crude | GOVERNED-WIDE | resale-uniform | 0.79× | newbuild-heavy (unreliable)→newbuild-heavy (unreliable) | n/a | clears | pending | pending | no justified multiple (newbuild-heavy (unreliable)) |
| CMBT | crude | GOVERNED-WIDE | structural-unavailable | 0.94× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: structural-unavailable |
| DHT | crude | VALIDATED-TIGHT | resale-uniform | 1.18× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| ECO | crude | PROVISIONAL ⛔ | resale-uniform | 1.38× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| FRO | crude | VALIDATED-TIGHT | resale-uniform | 1.42× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| INSW | crude | GOVERNED-WIDE | pending-sourceable | 1.48× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| NAT | crude | PROVISIONAL ⛔ | resale-uniform | 2.51× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| TEN | crude | GOVERNED-WIDE | structural-unavailable | 0.42× | no anchor→cheap | n/a | clears (+unvalidated) | pending | pending | NAV basis: structural-unavailable |
| TNK | crude | VALIDATED-TIGHT | resale-uniform | 0.91× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| ASC | product | PROVISIONAL ⛔ | unverified-no-current-xclusiv-line | 1.00× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: unverified-no-current-xclusiv-line |
| HAFN | product | PROVISIONAL ⛔ | pending-sourceable | 1.48× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| STNG | product | PROVISIONAL ⛔ | pending-sourceable | 0.94× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| TRMD | product | PROVISIONAL ⛔ | pending-sourceable | 1.11× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| CMDB | dry_bulk | GOVERNED-WIDE | resale-uniform | 0.55× | cheap→fair | flips (cheap/fair) | clears | pending | pending | read flips — normalization-dependent |
| GNK | dry_bulk | GOVERNED-WIDE | resale-uniform | 0.97× | cheap→fair | flips (cheap/fair) | clears | pending | pending | read flips — normalization-dependent |
| SB | dry_bulk | VALIDATED-TIGHT | resale-uniform | 0.61× | cheap→cheap | robust | clears | pending | pending | comparable; §18.5 gates pending |
| SBLK | dry_bulk | VALIDATED-TIGHT | resale-uniform | 0.93× | cheap→cheap | robust | clears | pending | pending | comparable; §18.5 gates pending |
| CCEC | lng | GOVERNED-WIDE | structural-unavailable | 0.78× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| FLNG | lng | GOVERNED-WIDE | structural-unavailable | 1.04× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| GSL | containerships | GOVERNED-WIDE | structural-unavailable | 1.01× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| MPCC | containerships | GOVERNED-WIDE | structural-unavailable | 1.37× | no anchor→newbuild-heavy (unreliable) | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |

## Summary

**NAV-basis (comparability boundary):** pending-sourceable 4, resale-uniform 11, structural-unavailable 6, unverified-no-current-xclusiv-line 1.

**Read robustness (parity↔historical):** flips 2, n/a 13, robust 7.

**Confidence tier (handoff):** GOVERNED-WIDE 10, PROVISIONAL 7, VALIDATED-TIGHT 5.

**⛔ NOT handoff-ready (PROVISIONAL — do NOT pass a governed FV):** ASC, BRUT, ECO, HAFN, NAT, STNG, TRMD. Each carries a NAV-driving figure that is uncited or off-basis (figure-provenance / off-convention queue); flag, don't pass, until it traces.

**Both §18.5 gates are registered-PENDING book-wide** — no Baltic $/day series (§18.5a) or orderbook ratios (§18.5b) in-repo; see `backtest/DATA_CONTRACT_NORMAL_RATES.md`. So no name is *fully* validated yet; the resale-uniform names are comparable and parity-banded, awaiting only the two data-gated gates.

**Caveat — crude `rich` is cycle position, not a short.** Crude pure-plays read rich because the §17 RONAV is through-cycle while price embeds the near-peak NTM rate (§12 NAT mechanism); read the crude reads with cycle position, not as TRIM/SHORT calls.

**§15 governance dual-read:** CMDB (30%), TEN (30%) carry a realisation haircut applied downstream (blend + strip terminal), NOT in the clean-NAV reads above — their reads are clean-basis; the haircut basis scales NAV/FV by (1 − haircut).

**NAV-basis-flagged (not yet comparable to the resale-uniform set):**
- **ASC** — unverified-no-current-xclusiv-line: MR
- **CCEC** — structural-unavailable: LNGC, MGC
- **CMBT** — structural-unavailable: Ctr-Large
- **FLNG** — structural-unavailable: LNGC
- **GSL** — structural-unavailable: Ctr-Intermediate, Ctr-Large
- **HAFN** — pending-sourceable: LR1 | unverified-no-current-xclusiv-line: MR
- **INSW** — pending-sourceable: LR1 | unverified-no-current-xclusiv-line: MR
- **MPCC** — structural-unavailable: Ctr-Feeder, Ctr-Intermediate
- **STNG** — pending-sourceable: Handymax | unverified-no-current-xclusiv-line: MR
- **TEN** — structural-unavailable: LNGC | pending-sourceable: LR1 | unverified-no-current-xclusiv-line: MR
- **TRMD** — pending-sourceable: LR1 | unverified-no-current-xclusiv-line: MR