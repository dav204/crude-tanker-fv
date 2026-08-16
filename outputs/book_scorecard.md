# Book-wide scorecard (Thread 4)

> **Price basis:** all 25 prices live.

> **Balance-sheet basis: 10 of 25 names on a pre-2026-Q2 vintage:** BWLP (2026-Q1), CAPT (2026-Q1), CMBT (2026-Q1), FLNG (2026-Q1), FRO (2026-Q1), HAFN (2026-Q1), MPCC (2026-Q1), NAT (2026-Q1), TEN (2026-Q1), TRMD (2026-Q1). Their liability half is the newest sheet at or before the run quarter (loader fallback — coherent with their manifests, guard-enforced); each pair advances TOGETHER at that name's refresh (q2_cluster_transition_2026-07-31).

> **Rate basis:** Supra-Ultra 2027+2028 strip legs HELD at the 13-Jul synthesis (Cal-27 14,175): the Smax Cal27 row is cropped from every capture of the new source (Chris.Palun, 2026-07-20 →) — front (q1/q2/12M/spot) IS the 06-Aug print (ffa_promotion_2026-08-09.md). NEW: the 06-Aug capture PRINTS Smax Q1-27 14,325 vs the held q3 15,075 — the held year reads ~5% RICH (one-sided disclosure). Held-node bracket retires at the first capture showing Smax Cal27 (owner channel-ask staged). Handy-Bulk derived row inherits the same mix via the x0.90 identity.

> **Rate basis:** Tanker forward curves PROMOTED 2026-08-10 — STAGE A (PRE_REGISTRATION_TANKER_ CLUSTER_REANCHOR.md, frozen 2026-07-15; four owner rulings recorded in stage_a_computation_draft_2026-08-09.md: wait-for-INSW / §5 breaches accepted post-investigation / VLCC 12M = Mount Horizon single-print / LR2_clean term = §4-letter). The 2026-06-07 war vintage is RETIRED. Per-class provenance tags on the strip headers above. §5 for the record: VLCC front 179,650 BREACH-HIGH and term-implied 48,850 BREACH-LOW both trace to ECO's verified $206.6k QTD print (tape-corroborated MB 242-247k / Pareto TD3C 489k; bands pre-date the 7/20 blockade escalation). INSW (8/10) carried no QTD bookings — basis closed on the 8/09 computed values; BRUT 8/13 remains a Rider-4 watch; Stage B 8/26-9/04 re-checks class-bucket medians ±10%.

> **Rate basis:** Dry-bulk curves (Cape/Pana/Post-Panamax/Supra-Ultra) RE-ANCHORED 2026-07-13 from the 13-Jul FFA OCR widget (status ok; owner-ratified promotion, all three classes; decisions/ffa_promotion_2026-07-13.md). Cape front flipped to BACKWARDATION (q3 > q4) — near-dated C5TC spike, Cal-27 barely moved.

> **Rate basis:** Container TC/value curves REFRESHED 2026-07-06 from MB Container Weekly 27 (assessments 2026-07-03) — the cited §11.8 ingest event closing trigger container_mb_refresh (decisions/container_ingest_2026-07-06.md; A3 re-derived on the combined validator fleets). The Apr-01 freeze disclosed 2026-07-03 is RESOLVED; trigger re-armed to the 2026-08-07 monthly boundary.

> **Rate basis:** Handy-Bulk (§11.7.11, added 2026-07-14): NO market FFA at any tenor — its curve row + scenario deck are both DERIVED = supra x 0.90 (locked basis, identity guard-tested; regenerate BOTH with any supra promotion). as_of 2026-07-10 = the MB Dry Bulk Weekly 28 vintage (own cadence, not a hold awaiting a print).

This file lists each name **twice, by design** — once in the **Verdict** (the decision surface: FV vs price, position, tier) and once in the **Validation matrix** below (the per-gate evidence behind that tier). The Verdict is what you act on; the matrix is why. One row per name *within* each table.

## Verdict — the consolidated read (the decision surface)

FV vs current price, position, and the broker-NAV bug-gate on the **same row** as the confidence tier — **the single handoff surface** for a sizing decision. The per-gate evidence behind each tier is the Validation matrix below (same names, same file).

**What this says about the opportunity set:** of 25 names, **8 are construction-validated** (VALIDATED-TIGHT — the NAV is soundly built), and of those the validated-and-actionable-long surface is **1 (SB — dry bulk, cheap on both NAV bases)**. 13 are directional-only (GOVERNED-WIDE); 4 are not yet trustworthy enough to act on (PROVISIONAL ⛔). **Name-specific shorts: 2343, ASC, CMBT, GNK** — every other TRIM/SHORT row is cycle-position, unreliable-read, or void. The thin actionable list is the tool refusing to manufacture conviction the validation doesn't support, not a gap.

**These are two different questions, and the gap between the counts is the point.** Construction-validated says the ESTIMATE is sound; edge-cleared adds that the cheap call survives the choice of §17 normalization basis and the position is a BUY. A name can be construction-validated and still not edge-cleared — its NAV is trustworthy while its discount is basis-dependent. Since 2026-08-13 those two failures cap size on separate channels and never stack (tier semantics amendment §0.3).

**Reading the labels:** the tier cell carries a **sub-reason = resolution path** (`structural-class` needs a new data regime; `pending-anchor` is sourceable now; `newbuild-heavy` resolves as hulls deliver; `newbuild-indeterminate` = a newbuild parked at $0 pending a filed price; `void` = a derived number rests on a contradicted figure). A **`cycle position`** in Position is a NAV-relative read (§12), NOT a directional short. A **void** row prints no derived numbers — they are known-suspect, not data.

| Ticker | Sector | **Tier · why** | Price | Model FV | FV range | Upside | Position | Blend FV† | NAV/sh | Broker NAV | Gap | SANITY | Handoff | W-frag |
|---|---|---|--:|--:|:--|--:|:--|--:|--:|--:|--:|:--|:--|:--|
| DHT | crude | VALIDATED-TIGHT | $19.52 | $15.97 | 11.64–21.53 | -18% | rich · cycle position (not a short) | $15.32 | $15.01 | $18.07 | -17% | OK | ready | stable |
| ECO | crude | VALIDATED-TIGHT | $60.29 | $41.71 | 28.08–60.70 | -31% | rich · cycle position (not a short) | $39.73 | $39.54 | $44.99 | -12% | OK | ready | stable |
| FRO | crude | VALIDATED-TIGHT | $41.21 | $27.79 | 17.32–41.59 | -33% | rich · cycle position (not a short) | $25.94 | $25.34 | $31.46 | -19% | OK | ready | stable |
| TNK | crude | VALIDATED-TIGHT | $85.13 | $83.93 | 71.90–102.30 | -1% | unreliable read (not actionable) | $83.23 | $84.60 | $106.41 | -20% | OK | ready | stable |
| CMDB | dry_bulk | VALIDATED-TIGHT | $18.23 | $20.11 | 16.51–23.95 | +10% | BUY (undervalued) | $21.13 | $32.13 | $29.40 (apx) | +9% | n-a | ready | stable |
| GNK | dry_bulk | VALIDATED-TIGHT | $26.34 | $22.67 | 17.42–28.59 | -14% | TRIM/SHORT (overvalued) | $24.61 | $25.12 | $28.63 | -12% | OK | ready | stable |
| SB | dry_bulk | VALIDATED-TIGHT | $7.75 | $9.53 | 7.33–12.13 | +23% | BUY (undervalued) | $10.24 | $10.58 | $8.81 (apx) | +20% | n-a | ready | stable |
| SBLK | dry_bulk | VALIDATED-TIGHT | $29.05 | $29.79 | 23.27–36.79 | +3% | HOLD (fairly valued) | $31.88 | $32.78 | $32.64 | +0% | OK | ready | **⚠ sign flips** |
| BRUT | crude | GOVERNED-WIDE · going-concern-unfinanced | $6.74 | $10.28 | 3.42–18.11 | +53% | unreliable read (not actionable) | $9.63 | $9.62 | $7.84 | +23% | OK | ready | **⚠ sign flips** |
| CAPT | crude | GOVERNED-WIDE · newbuild-heavy | $14.68 | $16.02 | 9.52–24.43 | +9% | unreliable read (not actionable) | $15.10 | $15.48 | $20.68 | -25% | OK | ready | **⚠ sign flips** |
| CMBT | crude | GOVERNED-WIDE · structural-class | $17.24 | $14.41 | 9.24–20.88 | -16% | TRIM/SHORT (overvalued) | $15.65 | $16.46 | $20.28 | -19% | OK | ready | stable |
| INSW | crude | GOVERNED-WIDE · pending-anchor | $97.05 | $59.59 | 42.71–80.41 | -39% | rich · cycle position (not a short) | $37.59 | $54.64 | $82.95 | -34% | OK | ready | stable |
| NAT | crude | GOVERNED-WIDE · newbuild-indeterminate | $6.71 | $3.07 | 2.14–4.54 | -54% | rich · cycle position (not a short) | $2.97 | $2.85 | $7.89 (apx) | -64% | n-a | ready | stable |
| TEN | crude | GOVERNED-WIDE · mixed | $41.45 | $62.66 | 47.21–82.53 | +51% | BUY (undervalued) | $59.21 | $88.16 | $121.91 (apx) | -28% | n-a | ready | stable |
| ASC | product | GOVERNED-WIDE · structural-class | $17.61 | $16.38 | 12.66–19.55 | -7% | TRIM/SHORT (overvalued) | $17.22 | $17.37 | $23.48 (apx) | -26% | n-a | ready | stable |
| TRMD | product | GOVERNED-WIDE · basis-pending | $30.08 | $33.58 | 20.10–45.25 | +12% | BUY (undervalued) | $29.98 | $30.22 | $34.98 | -14% | OK | ready | **⚠ sign flips** |
| 2343 | dry_bulk | GOVERNED-WIDE · pending-anchor | $0.50 | $0.40 | 0.33–0.46 | -20% | TRIM/SHORT (overvalued) | $0.40 | $0.41 | $0.54 (apx) | -25% | n-a | ready | stable |
| CCEC | lng | GOVERNED-WIDE · structural-class | $22.61 | $33.70 | 16.27–47.20 | +49% | BUY (undervalued) | $29.97 | $25.70 | $25.12 (apx) | +2% | n-a | ready | stable |
| FLNG | lng | GOVERNED-WIDE · structural-class | $30.80 | $30.67 | 20.36–39.36 | -0% | HOLD (fairly valued) | $28.16 | $28.45 | $21.54 | +32% | OK | ready | stable |
| GSL | containerships | GOVERNED-WIDE · structural-class | $42.17 | $42.88 | 38.58–46.64 | +2% | HOLD (fairly valued) | $44.02 | $41.20 | $56.23 (apx) | -27% | n-a | ready | — |
| MPCC | containerships | GOVERNED-WIDE · structural-class | $2.72 | $2.07 | 1.69–2.21 | -24% | unreliable read (not actionable) | $2.22 | $2.05 | $2.61 (apx) | -22% | n-a | ready | — |
| HAFN | product | PROVISIONAL · pool-gross-up-pending ⛔ | $7.74 | $6.56 | 4.01–8.86 | -15% | rich · cycle position (not a short) | $5.71 | $5.56 | $8.41 | -34% | OK | **NO** | stable |
| STNG | product | PROVISIONAL · off-curve ⛔ | $79.41 | $76.73 | 56.46–92.63 | -3% | HOLD (fairly valued) | $72.23 | $76.22 | $111.85 | -32% | OK | **NO** | stable |
| BWLP | lpg | PROVISIONAL · v1-lock-miss ⛔ | $22.75 | $14.46 | 10.82–18.27 | -36% | rich · cycle position (not a short) | $15.43 | $15.80 | $20.13 | -22% | OK | **NO** | stable |
| LPG | lpg | PROVISIONAL · v1-lock-miss ⛔ | $47.37 | $31.82 | 25.61–38.58 | -33% | rich · cycle position (not a short) | $33.93 | $35.69 | $49.34 | -28% | OK | **NO** | stable |

_Model FV / Upside = the SCENARIO-probability-weighted FV — the same basis as Position and every proposal/decomposition table (F-13, 2026-07-02: the two columns previously mixed bases and printed '+28% upside · TRIM/SHORT' rows the day the bases diverged). Blend FV† = the single-point NAV+strip blend at CURRENT market forwards — for tanker classes the HELD Jun-7 curves (see Rate basis above); a large Blend-vs-Model gap IS the scenario-dependence signal, not a discrepancy._

_W-frag = does the EV **sign** survive the §9.10 weight family (`outputs/weight_robustness.yaml`)? **⚠ sign flips** = the direction of the call is a weight-prior artifact, not a property of the name (the BRUT lesson, 2026-07-02) — a trust qualifier on the FV, consumed downstream like the tier. '—' = not in the diagnostic (non-crude family or not yet run)._

## Validation matrix — per-gate detail

Every covered name on ONE consistent, validated machine. **The product is the *boundary of what's comparable*, not a buy list.** `pending` ≠ `passed`: a name with a registered-pending gate is shown pending, never blessed. NAV age-0 basis is the uniform **xclusiv Resale** line (2026-06-22); mid-age is transaction-anchored (§9.9).

**Gates per name:** (1) NAV-basis (resale-uniform ⇒ comparable; else flagged); (2) Justified P/NAV both bases (§17); (3) parity band (§A1.2); (4) §18.5a mean-reversion (Thread 3, data-pending); (5) §18.5b orderbook cross-check (Thread 5, data-pending); (6) robust vs flips (does the read survive the parity↔historical choice). Gate 6 is a read-CORROBORATION line, not a construction gate — it does not feed the tier.

**Confidence tier (governance handoff):** how the NAV is BUILT — and ONLY that. **VALIDATED-TIGHT** = traced resale-uniform basis, NAV-driving figures sourced, on-convention, known-gap surfaces immaterial, and the §17 multiple is EVALUABLE (SB-class). **GOVERNED-WIDE** = the NAV traces but rests on a structural-unavailable input, or no §17 multiple can be produced at all — a usable directional anchor with a wide band (CMBT-class). **PROVISIONAL** = a NAV-driving figure is uncited / off-basis — **NOT handoff-ready, flag don't pass** (NAT-class). APPROX-pnav does not demote: an external broker cross-foot is estimate-level evidence that may inform the tier where coverage exists, never a requirement. An immaterial uncited operating-scrubber surface does not demote either (see provenance.py).

**A price movement may never change a tier** (amendment 2026-08-13; `test_tier_is_price_invariant`). Whether the §17 read AGREES across bases is an EDGE fact, not a construction fact: it is a function of where the price sits, so it left the tier and now ships as the read-corroboration line (`Robust?` / `read_flag` below), standing BESIDE the tier exactly as `weight_sign_stable` does. **The tier does not double-count either of them** — each caps size on its own channel and the two never stack as a repeated discount penalty (TNK precedent).

**Reading the §17 margin block:** `J par`/`J hist` are the justified P/NAV under the two normalization bases and `Boundary` is the nearest price at which the read state would change; `Margin%` is the signed distance to it. `read_flag` is the GOVERNED read state that governance consumes — it adopts a new state only once `|Margin%|` clears ±2.0%, so a name parked on a boundary reports one stable sizing input instead of strobing. `Robust?` is the instantaneous read and is display only.

| Ticker | Sector | **Tier** | NAV-basis | P/NAV(mkt) | Read par→hist | Robust? | J par | J hist | Boundary | Margin% | read_flag | Parity band | §18.5a | §18.5b | Verdict |
|---|---|---|---|--:|---|---|--:|--:|--:|--:|---|---|---|---|---|
| BRUT | crude | GOVERNED-WIDE | resale-uniform | 0.66× | newbuild-heavy (unreliable)→newbuild-heavy (unreliable) | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | clears | pending | pending | no justified multiple (newbuild-heavy (unreliable)) |
| CAPT | crude | GOVERNED-WIDE | resale-uniform | 0.91× | newbuild-heavy (unreliable)→newbuild-heavy (unreliable) | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | clears | pending | pending | no justified multiple (newbuild-heavy (unreliable)) |
| CMBT | crude | GOVERNED-WIDE | structural-unavailable | 1.00× | no anchor→rich | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | clears (+unvalidated) | pending | pending | NAV basis: structural-unavailable |
| DHT | crude | VALIDATED-TIGHT | resale-uniform | 1.23× | rich→rich | robust | 0.805× | 0.747× | $13.42 | +37.13% | robust | clears | pending | pending | comparable; §18.5 gates pending |
| ECO | crude | VALIDATED-TIGHT | resale-uniform | 1.61× | rich→rich | robust | 0.568× | 0.456× | $24.97 | +155.48% | robust | clears | pending | pending | comparable; §18.5 gates pending |
| FRO | crude | VALIDATED-TIGHT | resale-uniform | 1.56× | rich→rich | robust | 0.903× | 0.818× | $25.43 | +55.71% | robust | clears | pending | pending | comparable; §18.5 gates pending |
| INSW | crude | GOVERNED-WIDE | pending-sourceable | 1.71× | no anchor→rich | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| NAT | crude | GOVERNED-WIDE | resale-uniform | 2.25× | rich→rich | robust | 1.191× | 0.865× | $3.76 | +70.06% | robust | clears | pending | pending | comparable; §18.5 gates pending |
| TEN | crude | GOVERNED-WIDE | structural-unavailable | 0.42× | no anchor→cheap | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | clears (+unvalidated) | pending | pending | NAV basis: structural-unavailable |
| TNK | crude | VALIDATED-TIGHT | resale-uniform | 0.91× | rich→rich | robust | 0.589× | 0.716× | $67.27 | +14.62% | robust | clears | pending | pending | comparable; §18.5 gates pending |
| ASC | product | GOVERNED-WIDE | pending-sourceable | 0.98× | no anchor→rich | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| HAFN | product | PROVISIONAL ⛔ | pending-sourceable | 1.37× | no anchor→rich | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| STNG | product | PROVISIONAL ⛔ | pending-sourceable | 1.00× | no anchor→rich | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| TRMD | product | GOVERNED-WIDE | pending-sourceable | 0.98× | no anchor→rich | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | clears (+unvalidated) | pending | pending | NAV basis: pending-sourceable |
| 2343 | dry_bulk | GOVERNED-WIDE | resale-uniform | 0.96× | cheap→cheap | robust | 1.100× | 1.158× | $0.41 | -4.14% | robust | clears (+unvalidated) | pending | pending | comparable; §18.5 gates pending |
| CMDB | dry_bulk | VALIDATED-TIGHT | resale-uniform | 0.54× | cheap→fair | flips (cheap/fair) | 0.683× | 0.554× | $16.17 | +6.68% | flips (cheap/fair) | clears | pending | pending | read flips — normalization-dependent |
| GNK | dry_bulk | VALIDATED-TIGHT | resale-uniform | 1.00× | cheap→fair | flips (cheap/fair) | 1.134× | 1.019× | $25.90 | -3.08% | flips (cheap/fair) | clears | pending | pending | read flips — normalization-dependent |
| SB | dry_bulk | VALIDATED-TIGHT | resale-uniform | 0.60× | cheap→cheap | robust | 1.381× | 0.892× | $8.58 | -25.50% | robust | clears | pending | pending | comparable; §18.5 gates pending |
| SBLK | dry_bulk | VALIDATED-TIGHT | resale-uniform | 0.87× | cheap→fair | flips (cheap/fair) | 1.116× | 0.930× | $27.72 | +3.18% | flips (cheap/fair) | clears | pending | pending | read flips — normalization-dependent |
| CCEC | lng | GOVERNED-WIDE | structural-unavailable | 0.89× | no anchor→cheap | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| FLNG | lng | GOVERNED-WIDE | structural-unavailable | 1.09× | no anchor→cheap | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| GSL | containerships | GOVERNED-WIDE | structural-unavailable | 0.95× | no anchor→cheap | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| MPCC | containerships | GOVERNED-WIDE | structural-unavailable | 1.24× | no anchor→newbuild-heavy (unreliable) | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | unvalidated | pending | pending | NAV basis: structural-unavailable |
| BWLP | lpg | PROVISIONAL ⛔ | pending-sourceable | 1.38× | no anchor→rich | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | unvalidated | pending | pending | NAV basis: pending-sourceable |
| LPG | lpg | PROVISIONAL ⛔ | pending-sourceable | 1.24× | no anchor→rich | n/a | *blocked* | *blocked* | *blocked* | *blocked* | n/a | unvalidated | pending | pending | NAV basis: pending-sourceable |

## Summary

**NAV-basis (comparability boundary):** pending-sourceable 7, resale-uniform 12, structural-unavailable 6.

**Read robustness (parity↔historical), instantaneous:** flips 3, n/a 15, robust 7.

**Read flag (GOVERNED — what governance consumes, ±2.0% deadband):** flips 3, n/a 15, robust 7. No name sits inside the deadband.

**Confidence tier (handoff):** GOVERNED-WIDE 13, PROVISIONAL 4, VALIDATED-TIGHT 8.

**⛔ NOT handoff-ready (PROVISIONAL — do NOT pass a governed FV):** BWLP, HAFN, LPG, STNG. Each carries a NAV-driving figure that is uncited or off-basis (figure-provenance / off-convention queue); flag, don't pass, until it traces.

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