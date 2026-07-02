# Book-wide scorecard (Thread 4)

> **Price basis:** all 22 prices live.

This file lists each name **twice, by design** — once in the **Verdict** (the decision surface: FV vs price, position, tier) and once in the **Validation matrix** below (the per-gate evidence behind that tier). The Verdict is what you act on; the matrix is why. One row per name *within* each table.

## Verdict — the consolidated read (the decision surface)

FV vs current price, position, and the broker-NAV bug-gate on the **same row** as the confidence tier — **the single handoff surface** for a sizing decision. The per-gate evidence behind each tier is the Validation matrix below (same names, same file).

**What this says about the opportunity set:** of 22 names, the validated-and-actionable-long surface is **2 (SB, SBLK — dry bulk, cheap on both NAV bases)**. 13 are directional-only (GOVERNED-WIDE); 3 are not yet trustworthy enough to act on (PROVISIONAL ⛔). TNK is VALIDATED-TIGHT and BUY but reads *rich* — a near-peak-earnings long, cycle-dependent, not a clean value long. And **every one of the book's TRIM/SHORT positions is cycle-position, unreliable-read, or void — not one is a name-specific short.** The thin actionable list is the tool refusing to manufacture conviction the validation doesn't support, not a gap.

**Reading the labels:** the tier cell carries a **sub-reason = resolution path** (`structural-class` needs a new data regime; `pending-anchor` is sourceable now; `newbuild-heavy` resolves as hulls deliver; `newbuild-indeterminate` = a newbuild parked at $0 pending a filed price; `read-flips` needs the §18.5 gate data; `void` = a derived number rests on a contradicted figure). A **`cycle position`** in Position is a NAV-relative read (§12), NOT a directional short. A **void** row prints no derived numbers — they are known-suspect, not data.

| Ticker | Sector | **Tier · why** | Price | Model FV | Upside | Position | NAV/sh | Broker NAV | Gap | SANITY | Handoff | W-frag |
|---|---|---|--:|--:|--:|:--|--:|--:|--:|:--|:--|:--|
| DHT | crude | VALIDATED-TIGHT | $16.53 | $14.95 | -10% | rich · cycle position (not a short) | $13.88 | $15.17 | -8% | OK | ready | stable |
| ECO | crude | VALIDATED-TIGHT | $49.94 | $37.18 | -26% | rich · cycle position (not a short) | $34.35 | $41.27 | -17% | OK | ready | stable |
| FRO | crude | VALIDATED-TIGHT | $34.70 | $26.54 | -24% | rich · cycle position (not a short) | $24.22 | $28.92 | -16% | OK | ready | stable |
| TNK | crude | VALIDATED-TIGHT | $64.33 | $79.42 | +23% | BUY (undervalued) | $77.51 | $84.64 | -8% | OK | ready | stable |
| SB | dry_bulk | VALIDATED-TIGHT | $6.31 | $9.87 | +56% | BUY (undervalued) | $10.12 | $7.17 (apx) | +41% | n-a | ready | — |
| SBLK | dry_bulk | VALIDATED-TIGHT | $24.81 | $28.34 | +14% | BUY (undervalued) | $29.34 | $30.26 | -3% | OK | ready | — |
| CAPT | crude | GOVERNED-WIDE · newbuild-heavy | $12.49 | $16.03 | +28% | BUY (undervalued) | $15.49 | $18.64 | -17% | OK | ready | **⚠ sign flips** |
| CMBT | crude | GOVERNED-WIDE · structural-class | $14.05 | $15.26 | +9% | BUY (undervalued) | $15.87 | $18.99 | -16% | OK | ready | **⚠ sign flips** |
| INSW | crude | GOVERNED-WIDE · pending-anchor | $77.78 | $38.63 | -50% | rich · cycle position (not a short) | $52.59 | $79.37 | -34% | OK | ready | stable |
| NAT | crude | GOVERNED-WIDE · newbuild-indeterminate | $5.56 | $3.09 | -44% | rich · cycle position (not a short) | $2.79 | $6.54 (apx) | -57% | n-a | ready | stable |
| TEN | crude | GOVERNED-WIDE · mixed | $35.37 | $61.29 | +73% | BUY (undervalued) | $88.70 | $104.03 (apx) | -15% | n-a | ready | stable |
| ASC | product | GOVERNED-WIDE · structural-class | $14.25 | $16.75 | +18% | BUY (undervalued) | $17.80 | $19.00 (apx) | -6% | n-a | ready | — |
| TRMD | product | GOVERNED-WIDE · basis-pending | $26.25 | $30.97 | +18% | BUY (undervalued) | $30.34 | $31.63 | -4% | OK | ready | — |
| CMDB | dry_bulk | GOVERNED-WIDE · read-flips | $18.21 | $20.43 | +12% | BUY (undervalued) | $31.33 | $29.37 (apx) | +7% | n-a | ready | — |
| GNK | dry_bulk | GOVERNED-WIDE · read-flips | $24.66 | $23.99 | -3% | HOLD (fairly valued) | $24.69 | $28.34 | -13% | OK | ready | — |
| CCEC | lng | GOVERNED-WIDE · structural-class | $21.68 | $32.08 | +48% | BUY (undervalued) | $28.10 | $24.09 (apx) | +17% | n-a | ready | — |
| FLNG | lng | GOVERNED-WIDE · structural-class | $28.62 | $28.16 | -2% | BUY (undervalued) | $28.45 | $20.89 | +36% | OK | ready | — |
| GSL | containerships | GOVERNED-WIDE · structural-class | $37.78 | $43.00 | +14% | BUY (undervalued) | $38.59 | $50.37 (apx) | -23% | n-a | ready | — |
| MPCC | containerships | GOVERNED-WIDE · structural-class | $2.42 | $2.19 | -10% | unreliable read (not actionable) | $2.02 | $2.33 (apx) | -13% | n-a | ready | — |
| BRUT | crude | PROVISIONAL · cash-pending ⛔ | $5.17 | $9.27 | +79% | unreliable read (not actionable) | $8.80 | $6.89 | +28% | OK | **NO** | **⚠ sign flips** |
| HAFN | product | PROVISIONAL · pool-gross-up-pending ⛔ | $6.56 | $5.99 | -9% | rich · cycle position (not a short) | $5.57 | $6.91 | -19% | OK | **NO** | — |
| STNG | product | PROVISIONAL · off-curve ⛔ | $69.53 | $76.13 | +9% | BUY (undervalued) | $77.47 | $99.33 | -22% | OK | **NO** | — |

_W-frag = does the EV **sign** survive the §9.10 weight family (`outputs/weight_robustness.yaml`)? **⚠ sign flips** = the direction of the call is a weight-prior artifact, not a property of the name (the BRUT lesson, 2026-07-02) — a trust qualifier on the FV, consumed downstream like the tier. '—' = not in the diagnostic (non-crude family or not yet run)._

## Validation matrix — per-gate detail

Every covered name on ONE consistent, validated machine. **The product is the *boundary of what's comparable*, not a buy list.** `pending` ≠ `passed`: a name with a registered-pending gate is shown pending, never blessed. NAV age-0 basis is the uniform **xclusiv Resale** line (2026-06-22); mid-age is transaction-anchored (§9.9).

**Gates per name:** (1) NAV-basis (resale-uniform ⇒ comparable; else flagged); (2) Justified P/NAV both bases (§17); (3) parity band (§A1.2); (4) §18.5a mean-reversion (Thread 3, data-pending); (5) §18.5b orderbook cross-check (Thread 5, data-pending); (6) robust vs flips (does the read survive the parity↔historical choice).

**Confidence tier (governance handoff):** the FV's reliability for a sizing decision, read from the validation state above — **VALIDATED-TIGHT** (traced basis + robust across both §17 bases — broker OR internal two-basis corroboration; SB-class), **GOVERNED-WIDE** (NAV traces but rests on a structural-unavailable input or a read that flips — usable directional anchor, wide band; CMBT-class), **PROVISIONAL** (a NAV-driving figure is uncited / off-basis — **NOT handoff-ready, flag don't pass**; NAT-class). APPROX-pnav does not demote a robust name; an immaterial uncited operating-scrubber surface does not either (see provenance.py).

| Ticker | Sector | **Tier** | NAV-basis | P/NAV(mkt) | Read par→hist | Robust? | Parity band | §18.5a | §18.5b | Verdict |
|---|---|---|---|--:|---|---|---|---|---|---|
| BRUT | crude | PROVISIONAL ⛔ | resale-uniform | 0.61× | newbuild-heavy (unreliable)→newbuild-heavy (unreliable) | n/a | clears | pending | pending | no justified multiple (newbuild-heavy (unreliable)) |
| CAPT | crude | GOVERNED-WIDE | resale-uniform | 0.79× | newbuild-heavy (unreliable)→newbuild-heavy (unreliable) | n/a | clears | pending | pending | no justified multiple (newbuild-heavy (unreliable)) |
| CMBT | crude | GOVERNED-WIDE | structural-unavailable | 0.94× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: structural-unavailable |
| DHT | crude | VALIDATED-TIGHT | resale-uniform | 1.18× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| ECO | crude | VALIDATED-TIGHT | resale-uniform | 1.39× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| FRO | crude | VALIDATED-TIGHT | resale-uniform | 1.42× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| INSW | crude | GOVERNED-WIDE | pending-sourceable | 1.48× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| NAT | crude | GOVERNED-WIDE | resale-uniform | 1.86× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| TEN | crude | GOVERNED-WIDE | structural-unavailable | 0.42× | no anchor→cheap | n/a | clears (+unvalidated) | pending | pending | NAV basis: structural-unavailable |
| TNK | crude | VALIDATED-TIGHT | resale-uniform | 0.91× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| ASC | product | GOVERNED-WIDE | unverified-no-current-xclusiv-line | 0.90× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: unverified-no-current-xclusiv-line |
| HAFN | product | PROVISIONAL ⛔ | pending-sourceable | 1.38× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| STNG | product | PROVISIONAL ⛔ | pending-sourceable | 0.98× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| TRMD | product | GOVERNED-WIDE | pending-sourceable | 0.93× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| CMDB | dry_bulk | GOVERNED-WIDE | resale-uniform | 0.55× | cheap→fair | flips (cheap/fair) | clears | pending | pending | read flips — normalization-dependent |
| GNK | dry_bulk | GOVERNED-WIDE | resale-uniform | 0.97× | cheap→fair | flips (cheap/fair) | clears | pending | pending | read flips — normalization-dependent |
| SB | dry_bulk | VALIDATED-TIGHT | resale-uniform | 0.63× | cheap→cheap | robust | clears | pending | pending | comparable; §18.5 gates pending |
| SBLK | dry_bulk | VALIDATED-TIGHT | resale-uniform | 0.93× | cheap→cheap | robust | clears | pending | pending | comparable; §18.5 gates pending |
| CCEC | lng | GOVERNED-WIDE | structural-unavailable | 0.78× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| FLNG | lng | GOVERNED-WIDE | structural-unavailable | 1.04× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| GSL | containerships | GOVERNED-WIDE | structural-unavailable | 1.01× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| MPCC | containerships | GOVERNED-WIDE | structural-unavailable | 1.37× | no anchor→newbuild-heavy (unreliable) | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |

## Summary

**NAV-basis (comparability boundary):** pending-sourceable 4, resale-uniform 11, structural-unavailable 6, unverified-no-current-xclusiv-line 1.

**Read robustness (parity↔historical):** flips 2, n/a 13, robust 7.

**Confidence tier (handoff):** GOVERNED-WIDE 13, PROVISIONAL 3, VALIDATED-TIGHT 6.

**⛔ NOT handoff-ready (PROVISIONAL — do NOT pass a governed FV):** BRUT, HAFN, STNG. Each carries a NAV-driving figure that is uncited or off-basis (figure-provenance / off-convention queue); flag, don't pass, until it traces.

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