# Book-wide scorecard (Thread 4)

> **Price basis:** all 22 prices live.

> **Rate basis:** Tanker forward curves (VLCC/Suezmax/Aframax/LR2/LR1/MR/Handies/LR1_clean/LR2_clean) HELD at the 2026-06-07 vintage — no market forward print exists (owner decision 2026-07-02, option (i)); refresh on trigger tanker_forward_print_lands. The C-2 rates-layer tanker effect is understated pending the print.

> **Rate basis:** Container TC/value curves REFRESHED 2026-07-06 from MB Container Weekly 27 (assessments 2026-07-03) — the cited §11.8 ingest event closing trigger container_mb_refresh (decisions/container_ingest_2026-07-06.md; A3 re-derived on the combined validator fleets). The Apr-01 freeze disclosed 2026-07-03 is RESOLVED; trigger re-armed to the 2026-08-07 monthly boundary.

This file lists each name **twice, by design** — once in the **Verdict** (the decision surface: FV vs price, position, tier) and once in the **Validation matrix** below (the per-gate evidence behind that tier). The Verdict is what you act on; the matrix is why. One row per name *within* each table.

## Verdict — the consolidated read (the decision surface)

FV vs current price, position, and the broker-NAV bug-gate on the **same row** as the confidence tier — **the single handoff surface** for a sizing decision. The per-gate evidence behind each tier is the Validation matrix below (same names, same file).

**What this says about the opportunity set:** of 22 names, the validated-and-actionable-long surface is **2 (SB, SBLK — dry bulk, cheap on both NAV bases)**. 13 are directional-only (GOVERNED-WIDE); 3 are not yet trustworthy enough to act on (PROVISIONAL ⛔). **Name-specific shorts: CAPT, CMBT** — every other TRIM/SHORT row is cycle-position, unreliable-read, or void. The thin actionable list is the tool refusing to manufacture conviction the validation doesn't support, not a gap.

**Reading the labels:** the tier cell carries a **sub-reason = resolution path** (`structural-class` needs a new data regime; `pending-anchor` is sourceable now; `newbuild-heavy` resolves as hulls deliver; `newbuild-indeterminate` = a newbuild parked at $0 pending a filed price; `read-flips` needs the §18.5 gate data; `void` = a derived number rests on a contradicted figure). A **`cycle position`** in Position is a NAV-relative read (§12), NOT a directional short. A **void** row prints no derived numbers — they are known-suspect, not data.

| Ticker | Sector | **Tier · why** | Price | Model FV | Upside | Position | Blend FV† | NAV/sh | Broker NAV | Gap | SANITY | Handoff | W-frag |
|---|---|---|--:|--:|--:|:--|--:|--:|--:|--:|:--|:--|:--|
| DHT | crude | VALIDATED-TIGHT | $17.18 | $11.35 | -34% | rich · cycle position (not a short) | $14.95 | $13.88 | $15.76 | -12% | OK | ready | stable |
| ECO | crude | VALIDATED-TIGHT | $53.11 | $25.73 | -52% | rich · cycle position (not a short) | $37.18 | $34.35 | $43.89 | -22% | OK | ready | stable |
| FRO | crude | VALIDATED-TIGHT | $36.75 | $18.17 | -51% | rich · cycle position (not a short) | $26.54 | $24.22 | $30.62 | -21% | OK | ready | stable |
| TNK | crude | VALIDATED-TIGHT | $67.60 | $67.61 | +0% | HOLD (fairly valued) | $79.42 | $77.51 | $88.95 | -13% | OK | ready | **⚠ sign flips** |
| SB | dry_bulk | VALIDATED-TIGHT | $6.40 | $9.82 | +53% | BUY (undervalued) | $9.75 | $10.12 | $7.27 (apx) | +39% | n-a | ready | — |
| SBLK | dry_bulk | VALIDATED-TIGHT | $25.15 | $28.19 | +12% | BUY (undervalued) | $28.32 | $29.34 | $30.67 | -4% | OK | ready | — |
| CAPT | crude | GOVERNED-WIDE · newbuild-heavy | $13.68 | $10.07 | -26% | TRIM/SHORT (overvalued) | $16.03 | $15.49 | $20.42 | -24% | OK | ready | stable |
| CMBT | crude | GOVERNED-WIDE · structural-class | $14.56 | $13.35 | -8% | TRIM/SHORT (overvalued) | $15.19 | $15.87 | $19.68 | -19% | OK | ready | stable |
| INSW | crude | GOVERNED-WIDE · pending-anchor | $82.40 | $48.00 | -42% | rich · cycle position (not a short) | $38.63 | $52.59 | $84.08 | -37% | OK | ready | stable |
| NAT | crude | GOVERNED-WIDE · newbuild-indeterminate | $5.81 | $2.25 | -61% | rich · cycle position (not a short) | $3.09 | $2.79 | $6.84 (apx) | -59% | n-a | ready | stable |
| TEN | crude | GOVERNED-WIDE · mixed | $37.37 | $50.92 | +36% | BUY (undervalued) | $61.29 | $88.70 | $109.91 (apx) | -19% | n-a | ready | stable |
| ASC | product | GOVERNED-WIDE · structural-class | $14.86 | $16.28 | +10% | BUY (undervalued) | $16.75 | $17.80 | $19.81 (apx) | -10% | n-a | ready | stable |
| TRMD | product | GOVERNED-WIDE · basis-pending | $27.70 | $28.65 | +3% | HOLD (fairly valued) | $30.97 | $30.34 | $33.37 | -9% | OK | ready | **⚠ sign flips** |
| CMDB | dry_bulk | GOVERNED-WIDE · read-flips | $18.18 | $20.34 | +12% | BUY (undervalued) | $20.43 | $31.33 | $29.32 (apx) | +7% | n-a | ready | — |
| GNK | dry_bulk | GOVERNED-WIDE · read-flips | $24.50 | $23.56 | -4% | HOLD (fairly valued) | $23.85 | $24.69 | $28.16 | -12% | OK | ready | — |
| CCEC | lng | GOVERNED-WIDE · structural-class | $21.60 | $33.50 | +55% | BUY (undervalued) | $32.08 | $28.10 | $24.00 (apx) | +17% | n-a | ready | stable |
| FLNG | lng | GOVERNED-WIDE · structural-class | $29.29 | $29.19 | -0% | HOLD (fairly valued) | $28.16 | $28.45 | $21.38 | +33% | OK | ready | **⚠ sign flips** |
| GSL | containerships | GOVERNED-WIDE · structural-class | $38.11 | $40.54 | +6% | BUY (undervalued) | $43.06 | $38.59 | $50.81 (apx) | -24% | n-a | ready | — |
| MPCC | containerships | GOVERNED-WIDE · structural-class | $2.52 | $2.06 | -18% | unreliable read (not actionable) | $2.21 | $2.04 | $2.42 (apx) | -16% | n-a | ready | — |
| BRUT | crude | PROVISIONAL · cash-pending ⛔ | $5.32 | $3.12 | -41% | unreliable read (not actionable) | $9.27 | $8.80 | $7.09 | +24% | OK | **NO** | **⚠ sign flips** |
| HAFN | product | PROVISIONAL · pool-gross-up-pending ⛔ | $7.02 | $5.61 | -20% | rich · cycle position (not a short) | $5.99 | $5.57 | $7.39 | -25% | OK | **NO** | stable |
| STNG | product | PROVISIONAL · off-curve ⛔ | $73.01 | $70.90 | -3% | HOLD (fairly valued) | $76.13 | $77.47 | $104.30 | -26% | OK | **NO** | **⚠ sign flips** |

_Model FV / Upside = the SCENARIO-probability-weighted FV — the same basis as Position and every proposal/decomposition table (F-13, 2026-07-02: the two columns previously mixed bases and printed '+28% upside · TRIM/SHORT' rows the day the bases diverged). Blend FV† = the single-point NAV+strip blend at CURRENT market forwards — for tanker classes the HELD Jun-7 curves (see Rate basis above); a large Blend-vs-Model gap IS the scenario-dependence signal, not a discrepancy._

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
| MPCC | containerships | GOVERNED-WIDE | structural-unavailable | 1.36× | no anchor→newbuild-heavy (unreliable) | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |

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