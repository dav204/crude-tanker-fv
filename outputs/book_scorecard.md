# Book-wide scorecard (Thread 4)

> **Price basis: 1 of 25 prices are STATIC-FALLBACK** (oldest as-of 2026-07-14): 2343. Those rows value the book at watchlist statics, not the tape — treat their Price/Upside as stale.

> **Rate basis:** Tanker forward curves (VLCC/Suezmax/Aframax/LR2/LR1/MR/Handies/LR1_clean/LR2_clean) HELD at the 2026-06-07 vintage — no market forward print exists (owner decision 2026-07-02, option (i)); refresh on trigger tanker_forward_print_lands. The C-2 rates-layer tanker effect is understated pending the print.

> **Rate basis:** Dry-bulk curves (Cape/Pana/Post-Panamax/Supra-Ultra) RE-ANCHORED 2026-07-13 from the 13-Jul FFA OCR widget (status ok; owner-ratified promotion, all three classes; decisions/ffa_promotion_2026-07-13.md). Cape front flipped to BACKWARDATION (q3 > q4) — near-dated C5TC spike, Cal-27 barely moved.

> **Rate basis:** Container TC/value curves REFRESHED 2026-07-06 from MB Container Weekly 27 (assessments 2026-07-03) — the cited §11.8 ingest event closing trigger container_mb_refresh (decisions/container_ingest_2026-07-06.md; A3 re-derived on the combined validator fleets). The Apr-01 freeze disclosed 2026-07-03 is RESOLVED; trigger re-armed to the 2026-08-07 monthly boundary.

> **Rate basis:** Handy-Bulk (§11.7.11, added 2026-07-14): NO market FFA at any tenor — its curve row + scenario deck are both DERIVED = supra x 0.90 (locked basis, identity guard-tested; regenerate BOTH with any supra promotion). as_of 2026-07-10 = the MB Dry Bulk Weekly 28 vintage (own cadence, not a hold awaiting a print).

> **Weight-family basis: STALE** — the §9.10 fragility sidecar was not computed against the current scenario_inputs.yaml (0e507744f31d); lagging: crude, dry_bulk, lng, lpg, product. W-frag / family-range fields are withheld (null), never silently current — re-run the family diagnostic scripts (WO1-F4).

This file lists each name **twice, by design** — once in the **Verdict** (the decision surface: FV vs price, position, tier) and once in the **Validation matrix** below (the per-gate evidence behind that tier). The Verdict is what you act on; the matrix is why. One row per name *within* each table.

## Verdict — the consolidated read (the decision surface)

FV vs current price, position, and the broker-NAV bug-gate on the **same row** as the confidence tier — **the single handoff surface** for a sizing decision. The per-gate evidence behind each tier is the Validation matrix below (same names, same file).

**What this says about the opportunity set:** of 25 names, the validated-and-actionable-long surface is **1 (SB — dry bulk, cheap on both NAV bases)**. 14 are directional-only (GOVERNED-WIDE); 5 are not yet trustworthy enough to act on (PROVISIONAL ⛔). **Name-specific shorts: CMBT, GNK, STNG** — every other TRIM/SHORT row is cycle-position, unreliable-read, or void. The thin actionable list is the tool refusing to manufacture conviction the validation doesn't support, not a gap.

**Reading the labels:** the tier cell carries a **sub-reason = resolution path** (`structural-class` needs a new data regime; `pending-anchor` is sourceable now; `newbuild-heavy` resolves as hulls deliver; `newbuild-indeterminate` = a newbuild parked at $0 pending a filed price; `read-flips` needs the §18.5 gate data; `void` = a derived number rests on a contradicted figure). A **`cycle position`** in Position is a NAV-relative read (§12), NOT a directional short. A **void** row prints no derived numbers — they are known-suspect, not data.

| Ticker | Sector | **Tier · why** | Price | Model FV | Upside | Position | Blend FV† | NAV/sh | Broker NAV | Gap | SANITY | Handoff | W-frag |
|---|---|---|--:|--:|--:|:--|--:|--:|--:|--:|:--|:--|:--|
| DHT | crude | VALIDATED-TIGHT | $17.31 | $13.34 | -23% | rich · cycle position (not a short) | $14.95 | $13.88 | $15.18 | -9% | OK | ready | — |
| ECO | crude | VALIDATED-TIGHT | $54.20 | $32.09 | -41% | rich · cycle position (not a short) | $37.18 | $34.35 | $40.15 | -14% | OK | ready | — |
| FRO | crude | VALIDATED-TIGHT | $36.92 | $22.91 | -38% | rich · cycle position (not a short) | $26.54 | $24.22 | $26.95 | -10% | OK | ready | — |
| TNK | crude | VALIDATED-TIGHT | $70.72 | $73.18 | +3% | HOLD (fairly valued) | $79.42 | $77.51 | $96.88 | -20% | OK | ready | — |
| SB | dry_bulk | VALIDATED-TIGHT | $6.96 | $9.56 | +37% | BUY (undervalued) | $9.78 | $10.12 | $7.91 (apx) | +28% | n-a | ready | — |
| SBLK | dry_bulk | VALIDATED-TIGHT | $26.54 | $27.69 | +4% | HOLD (fairly valued) | $28.50 | $29.34 | $34.03 | -14% | OK | ready | — |
| CAPT | crude | GOVERNED-WIDE · newbuild-heavy | $13.28 | $13.14 | -1% | HOLD (fairly valued) | $16.03 | $15.49 | $19.25 | -20% | OK | ready | — |
| CMBT | crude | GOVERNED-WIDE · structural-class | $15.44 | $13.87 | -10% | TRIM/SHORT (overvalued) | $15.25 | $15.87 | $21.15 | -25% | OK | ready | — |
| INSW | crude | GOVERNED-WIDE · pending-anchor | $86.17 | $52.93 | -39% | rich · cycle position (not a short) | $38.63 | $52.59 | $77.63 | -32% | OK | ready | — |
| NAT | crude | GOVERNED-WIDE · newbuild-indeterminate | $6.09 | $2.72 | -55% | rich · cycle position (not a short) | $3.09 | $2.79 | $7.16 (apx) | -61% | n-a | ready | — |
| TEN | crude | GOVERNED-WIDE · mixed | $38.83 | $56.36 | +45% | BUY (undervalued) | $61.29 | $88.70 | $114.21 (apx) | -22% | n-a | ready | — |
| ASC | product | GOVERNED-WIDE · structural-class | $15.83 | $16.28 | +3% | HOLD (fairly valued) | $16.75 | $17.80 | $21.11 (apx) | -16% | n-a | ready | — |
| TRMD | product | GOVERNED-WIDE · basis-pending | $28.86 | $28.65 | -1% | HOLD (fairly valued) | $30.97 | $30.34 | $35.20 | -14% | OK | ready | — |
| 2343 | dry_bulk | GOVERNED-WIDE · pending-anchor | $0.39 | $0.38 | -3% | HOLD (fairly valued) | $0.38 | $0.39 | $0.40 (apx) | -3% | n-a | ready | — |
| CMDB | dry_bulk | GOVERNED-WIDE · read-flips | $19.56 | $20.10 | +3% | HOLD (fairly valued) | $20.52 | $31.33 | $31.55 (apx) | -1% | n-a | ready | — |
| GNK | dry_bulk | GOVERNED-WIDE · read-flips | $25.35 | $23.15 | -9% | TRIM/SHORT (overvalued) | $23.98 | $24.69 | $28.48 | -13% | OK | ready | — |
| CCEC | lng | GOVERNED-WIDE · structural-class | $22.38 | $33.50 | +50% | BUY (undervalued) | $32.08 | $28.10 | $24.87 (apx) | +13% | n-a | ready | — |
| FLNG | lng | GOVERNED-WIDE · structural-class | $30.14 | $29.19 | -3% | HOLD (fairly valued) | $28.16 | $28.45 | $22.33 | +27% | OK | ready | — |
| GSL | containerships | GOVERNED-WIDE · structural-class | $40.81 | $40.54 | -1% | HOLD (fairly valued) | $43.06 | $38.59 | $54.41 (apx) | -29% | n-a | ready | — |
| MPCC | containerships | GOVERNED-WIDE · structural-class | $2.51 | $2.06 | -18% | unreliable read (not actionable) | $2.21 | $2.04 | $2.41 (apx) | -15% | n-a | ready | — |
| BRUT | crude | PROVISIONAL · cash-pending ⛔ | $5.54 | $6.20 | +12% | unreliable read (not actionable) | $9.27 | $8.80 | $7.69 | +14% | OK | **NO** | — |
| HAFN | product | PROVISIONAL · pool-gross-up-pending ⛔ | $7.32 | $5.61 | -23% | rich · cycle position (not a short) | $5.99 | $5.57 | $8.51 | -35% | OK | **NO** | — |
| STNG | product | PROVISIONAL · off-curve ⛔ | $77.28 | $70.90 | -8% | TRIM/SHORT (overvalued) | $76.13 | $77.47 | $112.00 | -31% | OK | **NO** | — |
| BWLP | lpg | PROVISIONAL · v1-lock-miss ⛔ | $20.10 | $14.46 | -28% | rich · cycle position (not a short) | $15.43 | $15.80 | $20.72 | -24% | OK | **NO** | — |
| LPG | lpg | PROVISIONAL · v1-lock-miss ⛔ | $40.14 | $30.55 | -24% | rich · cycle position (not a short) | $32.76 | $34.11 | $47.79 | -29% | OK | **NO** | — |

_Model FV / Upside = the SCENARIO-probability-weighted FV — the same basis as Position and every proposal/decomposition table (F-13, 2026-07-02: the two columns previously mixed bases and printed '+28% upside · TRIM/SHORT' rows the day the bases diverged). Blend FV† = the single-point NAV+strip blend at CURRENT market forwards — for tanker classes the HELD Jun-7 curves (see Rate basis above); a large Blend-vs-Model gap IS the scenario-dependence signal, not a discrepancy._

## Validation matrix — per-gate detail

Every covered name on ONE consistent, validated machine. **The product is the *boundary of what's comparable*, not a buy list.** `pending` ≠ `passed`: a name with a registered-pending gate is shown pending, never blessed. NAV age-0 basis is the uniform **xclusiv Resale** line (2026-06-22); mid-age is transaction-anchored (§9.9).

**Gates per name:** (1) NAV-basis (resale-uniform ⇒ comparable; else flagged); (2) Justified P/NAV both bases (§17); (3) parity band (§A1.2); (4) §18.5a mean-reversion (Thread 3, data-pending); (5) §18.5b orderbook cross-check (Thread 5, data-pending); (6) robust vs flips (does the read survive the parity↔historical choice).

**Confidence tier (governance handoff):** the FV's reliability for a sizing decision, read from the validation state above — **VALIDATED-TIGHT** (traced basis + robust across both §17 bases — broker OR internal two-basis corroboration; SB-class), **GOVERNED-WIDE** (NAV traces but rests on a structural-unavailable input or a read that flips — usable directional anchor, wide band; CMBT-class), **PROVISIONAL** (a NAV-driving figure is uncited / off-basis — **NOT handoff-ready, flag don't pass**; NAT-class). APPROX-pnav does not demote a robust name; an immaterial uncited operating-scrubber surface does not either (see provenance.py).

| Ticker | Sector | **Tier** | NAV-basis | P/NAV(mkt) | Read par→hist | Robust? | Parity band | §18.5a | §18.5b | Verdict |
|---|---|---|---|--:|---|---|---|---|---|---|
| BRUT | crude | PROVISIONAL ⛔ | resale-uniform | 0.60× | newbuild-heavy (unreliable)→newbuild-heavy (unreliable) | n/a | clears | pending | pending | no justified multiple (newbuild-heavy (unreliable)) |
| CAPT | crude | GOVERNED-WIDE | resale-uniform | 0.86× | newbuild-heavy (unreliable)→newbuild-heavy (unreliable) | n/a | clears | pending | pending | no justified multiple (newbuild-heavy (unreliable)) |
| CMBT | crude | GOVERNED-WIDE | structural-unavailable | 0.92× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: structural-unavailable |
| DHT | crude | VALIDATED-TIGHT | resale-uniform | 1.24× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| ECO | crude | VALIDATED-TIGHT | resale-uniform | 1.55× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| FRO | crude | VALIDATED-TIGHT | resale-uniform | 1.52× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| INSW | crude | GOVERNED-WIDE | pending-sourceable | 1.57× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| NAT | crude | GOVERNED-WIDE | resale-uniform | 2.08× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| TEN | crude | GOVERNED-WIDE | structural-unavailable | 0.42× | no anchor→cheap | n/a | clears (+unvalidated) | pending | pending | NAV basis: structural-unavailable |
| TNK | crude | VALIDATED-TIGHT | resale-uniform | 0.87× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| ASC | product | GOVERNED-WIDE | unverified-no-current-xclusiv-line | 0.84× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: unverified-no-current-xclusiv-line |
| HAFN | product | PROVISIONAL ⛔ | pending-sourceable | 1.26× | no anchor→fair | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| STNG | product | PROVISIONAL ⛔ | pending-sourceable | 0.94× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| TRMD | product | GOVERNED-WIDE | pending-sourceable | 0.91× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| 2343 | dry_bulk | GOVERNED-WIDE | resale-uniform | 1.01× | cheap→cheap | robust | clears (+unvalidated) | pending | pending | comparable; §18.5 gates pending |
| CMDB | dry_bulk | GOVERNED-WIDE | resale-uniform | 0.55× | cheap→fair | flips (cheap/fair) | clears | pending | pending | read flips — normalization-dependent |
| GNK | dry_bulk | GOVERNED-WIDE | resale-uniform | 0.99× | cheap→fair | flips (cheap/fair) | clears | pending | pending | read flips — normalization-dependent |
| SB | dry_bulk | VALIDATED-TIGHT | resale-uniform | 0.63× | cheap→cheap | robust | clears | pending | pending | comparable; §18.5 gates pending |
| SBLK | dry_bulk | VALIDATED-TIGHT | resale-uniform | 0.86× | cheap→cheap | robust | clears | pending | pending | comparable; §18.5 gates pending |
| CCEC | lng | GOVERNED-WIDE | structural-unavailable | 0.77× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| FLNG | lng | GOVERNED-WIDE | structural-unavailable | 1.03× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| GSL | containerships | GOVERNED-WIDE | structural-unavailable | 1.01× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| MPCC | containerships | GOVERNED-WIDE | structural-unavailable | 1.20× | no anchor→newbuild-heavy (unreliable) | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| BWLP | lpg | PROVISIONAL ⛔ | pending-sourceable | 1.17× | no anchor→fair | n/a | unvalidated | pending | pending | NAV basis: pending-sourceable |
| LPG | lpg | PROVISIONAL ⛔ | pending-sourceable | 1.06× | no anchor→rich | n/a | unvalidated | pending | pending | NAV basis: pending-sourceable |

## Summary

**NAV-basis (comparability boundary):** pending-sourceable 6, resale-uniform 12, structural-unavailable 6, unverified-no-current-xclusiv-line 1.

**Read robustness (parity↔historical):** flips 2, n/a 15, robust 8.

**Confidence tier (handoff):** GOVERNED-WIDE 14, PROVISIONAL 5, VALIDATED-TIGHT 6.

**⛔ NOT handoff-ready (PROVISIONAL — do NOT pass a governed FV):** BRUT, BWLP, HAFN, LPG, STNG. Each carries a NAV-driving figure that is uncited or off-basis (figure-provenance / off-convention queue); flag, don't pass, until it traces.

**Both §18.5 gates are registered-PENDING book-wide** — no Baltic $/day series (§18.5a) or orderbook ratios (§18.5b) in-repo; see `backtest/DATA_CONTRACT_NORMAL_RATES.md`. So no name is *fully* validated yet; the resale-uniform names are comparable and parity-banded, awaiting only the two data-gated gates.

**Caveat — crude `rich` is cycle position, not a short.** Crude pure-plays read rich because the §17 RONAV is through-cycle while price embeds the near-peak NTM rate (§12 NAT mechanism); read the crude reads with cycle position, not as TRIM/SHORT calls.

**§15 governance dual-read:** CMDB (30%), TEN (30%) carry a realisation haircut applied downstream (blend + strip terminal), NOT in the clean-NAV reads above — their reads are clean-basis; the haircut basis scales NAV/FV by (1 − haircut).

**NAV-basis-flagged (not yet comparable to the resale-uniform set):**
- **ASC** — unverified-no-current-xclusiv-line: MR
- **BWLP** — pending-sourceable: VLGC
- **CCEC** — structural-unavailable: LNGC, MGC
- **CMBT** — structural-unavailable: Ctr-Large
- **FLNG** — structural-unavailable: LNGC
- **GSL** — structural-unavailable: Ctr-Intermediate, Ctr-Large
- **HAFN** — pending-sourceable: LR1 | unverified-no-current-xclusiv-line: MR
- **INSW** — pending-sourceable: LR1 | unverified-no-current-xclusiv-line: MR
- **LPG** — pending-sourceable: VLGC
- **MPCC** — structural-unavailable: Ctr-Feeder, Ctr-Intermediate
- **STNG** — pending-sourceable: Handymax | unverified-no-current-xclusiv-line: MR
- **TEN** — structural-unavailable: LNGC | pending-sourceable: LR1 | unverified-no-current-xclusiv-line: MR
- **TRMD** — pending-sourceable: LR1 | unverified-no-current-xclusiv-line: MR

**§9.9 wide-node exposure (fitted anchor EXTRAPOLATED at the node — a flagged-wide band, not a tight mark; registry `provenance.MARK_WIDE_NODES`):**
- **BWLP** — VLGC@five_year (decisions/vlgc_marks_2026-07-09.md)
- **LPG** — VLGC@five_year (decisions/vlgc_marks_2026-07-09.md)