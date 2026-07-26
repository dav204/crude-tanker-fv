# Book-wide scorecard (Thread 4)

> **Price basis:** all 25 prices live.

> **Rate basis:** Supra-Ultra 2027+2028 strip legs HELD at the 13-Jul synthesis (Cal-27 14,175): the Smax Cal27 row is cropped from every capture of the new source (Chris.Palun, 2026-07-20 →) — front (q1/q2/12M/spot) IS the 24-Jul print. Held-node bracket per ffa_promotion_2026-07-24.md; retires at the first capture showing Smax Cal27 (owner channel-ask staged). Handy-Bulk derived row inherits the same mix via the x0.90 identity.

> **Rate basis:** Tanker forward curves (VLCC/Suezmax/Aframax/LR2/LR1/MR/Handies/LR1_clean/LR2_clean) HELD at the 2026-06-07 vintage — TERM PRINT EXISTS (DHT 6-K 2026-07-13: 3-yr VLCC TC $75k/day Sep-26 start; Q3 QTD bookings $139.7k corroborate the front within ~5%; back-half implied 40-55% below this vintage). Promotion deferred to the Q2-cluster re-anchor by owner ruling 2026-07-14, SIGNED 2026-07-15 (decisions/tanker_forward_print_ruling_2026-07-14.md): Stage A no later than 2026-08-15 (unconditional — DHT-print fallback if cluster basis insufficient), Stage B true-up ≤2026-09-04 band-gated. Estimated strip overhang while held: −3 to −4% FV on peak-weighted crude, direction-safe (can only make rich names richer; the one qualified case — TRMD's post-re-tilt BUY — is in the Stage-A eyeball inventory, ruling ADDENDUM). Method: PRE_REGISTRATION_TANKER_CLUSTER_REANCHOR.md (frozen at signature).

> **Rate basis:** Dry-bulk curves (Cape/Pana/Post-Panamax/Supra-Ultra) RE-ANCHORED 2026-07-13 from the 13-Jul FFA OCR widget (status ok; owner-ratified promotion, all three classes; decisions/ffa_promotion_2026-07-13.md). Cape front flipped to BACKWARDATION (q3 > q4) — near-dated C5TC spike, Cal-27 barely moved.

> **Rate basis:** Container TC/value curves REFRESHED 2026-07-06 from MB Container Weekly 27 (assessments 2026-07-03) — the cited §11.8 ingest event closing trigger container_mb_refresh (decisions/container_ingest_2026-07-06.md; A3 re-derived on the combined validator fleets). The Apr-01 freeze disclosed 2026-07-03 is RESOLVED; trigger re-armed to the 2026-08-07 monthly boundary.

> **Rate basis:** Handy-Bulk (§11.7.11, added 2026-07-14): NO market FFA at any tenor — its curve row + scenario deck are both DERIVED = supra x 0.90 (locked basis, identity guard-tested; regenerate BOTH with any supra promotion). as_of 2026-07-10 = the MB Dry Bulk Weekly 28 vintage (own cadence, not a hold awaiting a print).

This file lists each name **twice, by design** — once in the **Verdict** (the decision surface: FV vs price, position, tier) and once in the **Validation matrix** below (the per-gate evidence behind that tier). The Verdict is what you act on; the matrix is why. One row per name *within* each table.

## Verdict — the consolidated read (the decision surface)

FV vs current price, position, and the broker-NAV bug-gate on the **same row** as the confidence tier — **the single handoff surface** for a sizing decision. The per-gate evidence behind each tier is the Validation matrix below (same names, same file).

**What this says about the opportunity set:** of 25 names, the validated-and-actionable-long surface is **1 (SB — dry bulk, cheap on both NAV bases)**. 14 are directional-only (GOVERNED-WIDE); 5 are not yet trustworthy enough to act on (PROVISIONAL ⛔). **Name-specific shorts: 2343, CMBT, GNK, GSL** — every other TRIM/SHORT row is cycle-position, unreliable-read, or void. The thin actionable list is the tool refusing to manufacture conviction the validation doesn't support, not a gap.

**Reading the labels:** the tier cell carries a **sub-reason = resolution path** (`structural-class` needs a new data regime; `pending-anchor` is sourceable now; `newbuild-heavy` resolves as hulls deliver; `newbuild-indeterminate` = a newbuild parked at $0 pending a filed price; `read-flips` needs the §18.5 gate data; `void` = a derived number rests on a contradicted figure). A **`cycle position`** in Position is a NAV-relative read (§12), NOT a directional short. A **void** row prints no derived numbers — they are known-suspect, not data.

| Ticker | Sector | **Tier · why** | Price | Model FV | FV range | Upside | Position | Blend FV† | NAV/sh | Broker NAV | Gap | SANITY | Handoff | W-frag |
|---|---|---|--:|--:|:--|--:|:--|--:|--:|--:|--:|:--|:--|:--|
| DHT | crude | VALIDATED-TIGHT | $18.45 | $13.10 | 9.22–20.25 | -29% | rich · cycle position (not a short) | $14.68 | $13.58 | $16.18 | -16% | OK | ready | stable |
| ECO | crude | VALIDATED-TIGHT | $57.88 | $32.10 | 19.63–55.63 | -45% | rich · cycle position (not a short) | $37.19 | $34.42 | $42.87 | -20% | OK | ready | stable |
| FRO | crude | VALIDATED-TIGHT | $39.29 | $22.80 | 13.43–40.10 | -42% | rich · cycle position (not a short) | $26.41 | $24.11 | $28.68 | -16% | OK | ready | stable |
| TNK | crude | VALIDATED-TIGHT | $75.81 | $73.35 | 62.43–95.01 | -3% | HOLD (fairly valued) | $79.61 | $77.73 | $103.85 | -25% | OK | ready | stable |
| SB | dry_bulk | VALIDATED-TIGHT | $7.67 | $9.42 | 7.06–12.16 | +23% | BUY (undervalued) | $9.70 | $10.02 | $8.72 (apx) | +15% | n-a | ready | stable |
| SBLK | dry_bulk | VALIDATED-TIGHT | $28.14 | $28.19 | 21.66–35.21 | +0% | HOLD (fairly valued) | $29.22 | $30.13 | $36.08 | -16% | OK | ready | **⚠ sign flips** |
| CAPT | crude | GOVERNED-WIDE · newbuild-heavy | $13.01 | $13.14 | 7.21–24.41 | +1% | HOLD (fairly valued) | $16.03 | $15.49 | $18.86 | -18% | OK | ready | **⚠ sign flips** |
| CMBT | crude | GOVERNED-WIDE · structural-class | $15.74 | $13.99 | 8.80–21.22 | -11% | TRIM/SHORT (overvalued) | $15.50 | $16.12 | $21.56 | -25% | OK | ready | stable |
| INSW | crude | GOVERNED-WIDE · pending-anchor | $92.28 | $54.12 | 38.47–77.73 | -41% | rich · cycle position (not a short) | $38.50 | $52.48 | $83.14 | -37% | OK | ready | stable |
| NAT | crude | GOVERNED-WIDE · newbuild-indeterminate | $6.45 | $2.76 | 1.88–4.54 | -57% | rich · cycle position (not a short) | $3.14 | $2.85 | $7.59 (apx) | -63% | n-a | ready | stable |
| TEN | crude | GOVERNED-WIDE · mixed | $39.40 | $56.56 | 41.52–82.07 | +44% | BUY (undervalued) | $59.78 | $87.57 | $115.88 (apx) | -24% | n-a | ready | stable |
| ASC | product | GOVERNED-WIDE · structural-class | $16.61 | $16.85 | 13.26–19.79 | +1% | HOLD (fairly valued) | $16.77 | $17.82 | $22.15 (apx) | -20% | n-a | ready | **⚠ sign flips** |
| TRMD | product | GOVERNED-WIDE · basis-pending | $30.28 | $31.87 | 18.47–45.34 | +5% | BUY (undervalued) | $30.94 | $30.30 | $36.93 | -18% | OK | ready | **⚠ sign flips** |
| 2343 | dry_bulk | GOVERNED-WIDE · pending-anchor | $0.42 | $0.38 | 0.32–0.44 | -9% | TRIM/SHORT (overvalued) | $0.38 | $0.39 | $0.43 (apx) | -8% | n-a | ready | stable |
| CMDB | dry_bulk | GOVERNED-WIDE · read-flips | $18.84 | $20.47 | 16.79–24.41 | +9% | BUY (undervalued) | $21.01 | $32.10 | $30.39 (apx) | +6% | n-a | ready | stable |
| GNK | dry_bulk | GOVERNED-WIDE · read-flips | $26.77 | $23.66 | 18.29–29.71 | -12% | TRIM/SHORT (overvalued) | $24.71 | $25.48 | $30.08 | -15% | OK | ready | stable |
| CCEC | lng | GOVERNED-WIDE · structural-class | $23.35 | $35.91 | 18.18–49.70 | +54% | BUY (undervalued) | $32.08 | $28.10 | $25.94 (apx) | +8% | n-a | ready | stable |
| FLNG | lng | GOVERNED-WIDE · structural-class | $30.85 | $30.67 | 20.36–39.36 | -1% | HOLD (fairly valued) | $28.16 | $28.45 | $22.85 | +25% | OK | ready | stable |
| GSL | containerships | GOVERNED-WIDE · structural-class | $43.61 | $40.54 | 36.14–44.39 | -7% | TRIM/SHORT (overvalued) | $43.06 | $38.59 | $58.15 (apx) | -34% | n-a | ready | — |
| MPCC | containerships | GOVERNED-WIDE · structural-class | $2.60 | $2.06 | 1.69–2.20 | -21% | unreliable read (not actionable) | $2.21 | $2.04 | $2.50 (apx) | -18% | n-a | ready | — |
| BRUT | crude | PROVISIONAL · cash-pending ⛔ | $5.72 | $6.21 | 0.07–17.18 | +8% | unreliable read (not actionable) | $9.27 | $8.80 | $7.95 | +11% | OK | **NO** | **⚠ sign flips** |
| HAFN | product | PROVISIONAL · pool-gross-up-pending ⛔ | $7.65 | $6.23 | 3.70–8.87 | -19% | rich · cycle position (not a short) | $5.99 | $5.57 | $8.90 | -37% | OK | **NO** | stable |
| STNG | product | PROVISIONAL · off-curve ⛔ | $79.49 | $76.87 | 51.31–101.53 | -3% | HOLD (fairly valued) | $75.86 | $77.13 | $115.20 | -33% | OK | **NO** | stable |
| BWLP | lpg | PROVISIONAL · v1-lock-miss ⛔ | $22.00 | $14.46 | 10.82–18.27 | -34% | rich · cycle position (not a short) | $15.43 | $15.80 | $22.68 | -30% | OK | **NO** | stable |
| LPG | lpg | PROVISIONAL · v1-lock-miss ⛔ | $45.32 | $30.55 | 23.06–38.50 | -33% | rich · cycle position (not a short) | $32.76 | $34.11 | $53.95 | -37% | OK | **NO** | stable |

_Model FV / Upside = the SCENARIO-probability-weighted FV — the same basis as Position and every proposal/decomposition table (F-13, 2026-07-02: the two columns previously mixed bases and printed '+28% upside · TRIM/SHORT' rows the day the bases diverged). Blend FV† = the single-point NAV+strip blend at CURRENT market forwards — for tanker classes the HELD Jun-7 curves (see Rate basis above); a large Blend-vs-Model gap IS the scenario-dependence signal, not a discrepancy._

_W-frag = does the EV **sign** survive the §9.10 weight family (`outputs/weight_robustness.yaml`)? **⚠ sign flips** = the direction of the call is a weight-prior artifact, not a property of the name (the BRUT lesson, 2026-07-02) — a trust qualifier on the FV, consumed downstream like the tier. '—' = not in the diagnostic (non-crude family or not yet run)._

## Validation matrix — per-gate detail

Every covered name on ONE consistent, validated machine. **The product is the *boundary of what's comparable*, not a buy list.** `pending` ≠ `passed`: a name with a registered-pending gate is shown pending, never blessed. NAV age-0 basis is the uniform **xclusiv Resale** line (2026-06-22); mid-age is transaction-anchored (§9.9).

**Gates per name:** (1) NAV-basis (resale-uniform ⇒ comparable; else flagged); (2) Justified P/NAV both bases (§17); (3) parity band (§A1.2); (4) §18.5a mean-reversion (Thread 3, data-pending); (5) §18.5b orderbook cross-check (Thread 5, data-pending); (6) robust vs flips (does the read survive the parity↔historical choice).

**Confidence tier (governance handoff):** the FV's reliability for a sizing decision, read from the validation state above — **VALIDATED-TIGHT** (traced basis + robust across both §17 bases — broker OR internal two-basis corroboration; SB-class), **GOVERNED-WIDE** (NAV traces but rests on a structural-unavailable input or a read that flips — usable directional anchor, wide band; CMBT-class), **PROVISIONAL** (a NAV-driving figure is uncited / off-basis — **NOT handoff-ready, flag don't pass**; NAT-class). APPROX-pnav does not demote a robust name; an immaterial uncited operating-scrubber surface does not either (see provenance.py).

| Ticker | Sector | **Tier** | NAV-basis | P/NAV(mkt) | Read par→hist | Robust? | Parity band | §18.5a | §18.5b | Verdict |
|---|---|---|---|--:|---|---|---|---|---|---|
| BRUT | crude | PROVISIONAL ⛔ | resale-uniform | 0.60× | newbuild-heavy (unreliable)→newbuild-heavy (unreliable) | n/a | clears | pending | pending | no justified multiple (newbuild-heavy (unreliable)) |
| CAPT | crude | GOVERNED-WIDE | resale-uniform | 0.86× | newbuild-heavy (unreliable)→newbuild-heavy (unreliable) | n/a | clears | pending | pending | no justified multiple (newbuild-heavy (unreliable)) |
| CMBT | crude | GOVERNED-WIDE | structural-unavailable | 0.91× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: structural-unavailable |
| DHT | crude | VALIDATED-TIGHT | resale-uniform | 1.27× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| ECO | crude | VALIDATED-TIGHT | resale-uniform | 1.54× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| FRO | crude | VALIDATED-TIGHT | resale-uniform | 1.53× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| INSW | crude | GOVERNED-WIDE | pending-sourceable | 1.57× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| NAT | crude | GOVERNED-WIDE | resale-uniform | 2.04× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| TEN | crude | GOVERNED-WIDE | structural-unavailable | 0.42× | no anchor→cheap | n/a | clears (+unvalidated) | pending | pending | NAV basis: structural-unavailable |
| TNK | crude | VALIDATED-TIGHT | resale-uniform | 0.87× | rich→rich | robust | clears | pending | pending | comparable; §18.5 gates pending |
| ASC | product | GOVERNED-WIDE | pending-sourceable | 0.84× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| HAFN | product | PROVISIONAL ⛔ | pending-sourceable | 1.26× | no anchor→fair | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| STNG | product | PROVISIONAL ⛔ | pending-sourceable | 0.95× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| TRMD | product | GOVERNED-WIDE | pending-sourceable | 0.91× | no anchor→rich | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| 2343 | dry_bulk | GOVERNED-WIDE | resale-uniform | 0.99× | cheap→cheap | robust | clears (+unvalidated) | pending | pending | comparable; §18.5 gates pending |
| CMDB | dry_bulk | GOVERNED-WIDE | resale-uniform | 0.54× | cheap→fair | flips (cheap/fair) | clears | pending | pending | read flips — normalization-dependent |
| GNK | dry_bulk | GOVERNED-WIDE | resale-uniform | 0.96× | cheap→fair | flips (cheap/fair) | clears | pending | pending | read flips — normalization-dependent |
| SB | dry_bulk | VALIDATED-TIGHT | resale-uniform | 0.64× | cheap→cheap | robust | clears | pending | pending | comparable; §18.5 gates pending |
| SBLK | dry_bulk | VALIDATED-TIGHT | resale-uniform | 0.84× | cheap→cheap | robust | clears | pending | pending | comparable; §18.5 gates pending |
| CCEC | lng | GOVERNED-WIDE | structural-unavailable | 0.77× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| FLNG | lng | GOVERNED-WIDE | structural-unavailable | 1.03× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| GSL | containerships | GOVERNED-WIDE | structural-unavailable | 1.01× | no anchor→cheap | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| MPCC | containerships | GOVERNED-WIDE | structural-unavailable | 1.20× | no anchor→newbuild-heavy (unreliable) | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| BWLP | lpg | PROVISIONAL ⛔ | pending-sourceable | 1.17× | no anchor→fair | n/a | unvalidated | pending | pending | NAV basis: pending-sourceable |
| LPG | lpg | PROVISIONAL ⛔ | pending-sourceable | 1.06× | no anchor→rich | n/a | unvalidated | pending | pending | NAV basis: pending-sourceable |

## Summary

**NAV-basis (comparability boundary):** pending-sourceable 7, resale-uniform 12, structural-unavailable 6.

**Read robustness (parity↔historical):** flips 2, n/a 15, robust 8.

**Confidence tier (handoff):** GOVERNED-WIDE 14, PROVISIONAL 5, VALIDATED-TIGHT 6.

**⛔ NOT handoff-ready (PROVISIONAL — do NOT pass a governed FV):** BRUT, BWLP, HAFN, LPG, STNG. Each carries a NAV-driving figure that is uncited or off-basis (figure-provenance / off-convention queue); flag, don't pass, until it traces.

**Both §18.5 gates are registered-PENDING book-wide** — no Baltic $/day series (§18.5a) or orderbook ratios (§18.5b) in-repo; see `backtest/DATA_CONTRACT_NORMAL_RATES.md`. So no name is *fully* validated yet; the resale-uniform names are comparable and parity-banded, awaiting only the two data-gated gates.

**Caveat — crude `rich` is cycle position, not a short.** Crude pure-plays read rich because the §17 RONAV is through-cycle while price embeds the near-peak NTM rate (§12 NAT mechanism); read the crude reads with cycle position, not as TRIM/SHORT calls.

**§15 governance dual-read:** CMDB (30%), TEN (30%) carry a realisation haircut applied downstream (blend + strip terminal), NOT in the clean-NAV reads above — their reads are clean-basis; the haircut basis scales NAV/FV by (1 − haircut).

**NAV-basis-flagged (not yet comparable to the resale-uniform set):**
- **ASC** — pending-sourceable: Handysize
- **BWLP** — pending-sourceable: VLGC
- **CCEC** — structural-unavailable: LNGC, MGC
- **CMBT** — structural-unavailable: Ctr-Large
- **FLNG** — structural-unavailable: LNGC
- **GSL** — structural-unavailable: Ctr-Intermediate, Ctr-Large
- **HAFN** — pending-sourceable: Handysize, LR1
- **INSW** — pending-sourceable: LR1
- **LPG** — pending-sourceable: VLGC
- **MPCC** — structural-unavailable: Ctr-Feeder, Ctr-Intermediate
- **STNG** — pending-sourceable: Handymax
- **TEN** — structural-unavailable: LNGC | pending-sourceable: Handysize, LR1
- **TRMD** — pending-sourceable: LR1

**§9.9 wide-node exposure (fitted anchor EXTRAPOLATED at the node — a flagged-wide band, not a tight mark; registry `provenance.MARK_WIDE_NODES`):**
- **BWLP** — VLGC@five_year (decisions/vlgc_marks_2026-07-09.md)
- **LPG** — VLGC@five_year (decisions/vlgc_marks_2026-07-09.md)
- **SB** — Post-Panamax@five_year+ten_year (decisions/ppmx_fit_seed_prereg_2026-07-18.md)