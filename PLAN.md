# PLAN.md — active plan / sprint handoff

A new agent reads CLAUDE.md, then this file, then starts. This is a
**forward-looking valuation aid** for shipping equities (independent NAV +
forward dividend strip, blended by cycle position), judged by the soundness of
its per-name reads — not by a cross-sectional backtest.

**Current state (2026-06-29):** **22 watchlist names across 5 sectors**; **378 main
tests green** (+13 backtest via `PYTHONPATH=. pytest backtest/`; +57 harvester via
`.venv310`); drift gate **0 unexplained** (headline FV untouched all arc); pipeline
clean; pushed to `origin/main` @ `5fa1050`. The engine GAINED two **diagnostic-only**
legs this arc (both documented + tested; NEITHER wired into headline FV):
1. **Justified P/NAV diagnostic** (METHODOLOGY §17, `justified_pnav.py`) — a coverage-
   independent fair-multiple per name: `P/NAV* = (RONAV_norm − g)/(r − g)`, where RONAV is
   return on the tool's marked NAV at through-cycle rates. Gives the APPROX names a NAV
   benchmark; uses the production transaction-anchored NAV (P0 fix).
2. **Through-cycle normal-rate layer** (METHODOLOGY §18, `normal_rates.py`) — two tagged
   bases per class: **parity** (replacement economics, from `newbuild_contract_prices.yaml`)
   and **historical_mean**; the justified leg shows RONAV under both with a Robust verdict.
   Pre-registered AHEAD of results (`PRE_REGISTRATION_NORMAL_RATES.md` + 2 amendments); a
   per-class halt-band + an input-basis resale invariant gate the inputs. `cycle.py` FROZEN.
   Finding: SB cheap on both (robust); crude reads robust-rich (a stale-NB artifact was caught
   and purged); LNG/container/product parity UNVALIDATED/pending (see Open threads).

Earlier this same push-block (P2, §11.7.10): **Post-Panamax sub-class** split out of the
collapsed Pana class (SB's 16 hulls; the over-mark closed, SB NAV $10.14→$9.82) + SB
disclosed charter rates wired; baseline re-ratified. **dwt-scaling** of the dry-bulk curves
(§11.7.10) — **dry-bulk manifest `dwt` is LOAD-BEARING**; crude/product/lng/container flat.

**A NEW AGENT: read CLAUDE.md, then this file.** Everything below "Recent arc" is DONE
and committed. The prioritized open threads are in "Open threads"; the standing
operational threads (Q2 refresh, FFA, news-pull, backtest, Tier-4 backlog) carry forward
unchanged. Per-change chronology in `CHANGELOG.md`; per-name detail in `decisions/<t>_log.md`.

## Recent arc — equity onboarding + dry-bulk marks (2026-06-26 → 06-28)

Three pushed commits (`b1c07db`, `9774411`, `a77e217`):

- **CMBT (CMB.TECH, ex-Euronav) onboarded — 21st name, first crude+dry_bulk+containerships
  MULTI-SLEEVE hybrid** (§11.9). Five-segment conglomerate post the Aug-2025 Golden Ocean
  merger (dry bulk ~72% of vessel value); chemical/offshore(Windcat)/FSO/HFS/newbuild book
  held off-curve. PARETO-ANCHORED (P/NAV 0.74x, NAV ~$20/sh; the onboarding briefly mis-read
  it as APPROX — corrected same day). Read: BUY +11% at the live close. §15 declined +
  tripwires (Saverys/CMB NV control). Memo: `outputs/cmbt_multisleeve_methodology_2026-06-26.md`
  + `outputs/cmbt_onboarding/`; record in `decisions/cmbt_log.md`.
- **dwt-scaling (§11.7.10)** — "split Newcastlemax properly" was implemented as dwt-scaling
  (owner decision: NMax/Cape trade at the same $/dwt, so it's size, not a structural premium).
  A **correctness fix, not a gap-closer** (measured): standard-Capesize/Supramax-heavy names
  corrected DOWN to their own transaction level (GNK −6.2%, CMDB −3.6%); NMax/Ultramax-heavy
  stayed ~flat (CMBT +0.1%, SBLK +1.3%). CMBT's −24% Pareto gap unchanged (uniform in-band
  conservatism × leverage). +4 tests; baseline re-ratified.
- **SB (Safe Bulkers) onboarded — 22nd name, 4th dry-bulk validator.** Greek dry-bulk
  pure-play; 43 on-curve (36 Pana + 7 Cape) + 2 HFS off-curve + $100M Series C/D preferred;
  Hajioannou control. APPROX P/BV (no Pareto/VIE NAV — verified). Read: BUY +49% but
  **mark-rich** — book is conservative depreciated/impaired cost ($24.7M/vessel) AND SB
  exercises the §11.7.10 Post-Panamax limitation more than any name. `decisions/sb_log.md`.
- **Toolchain:** `scripts/fetch_pdf.py` UA patched to an SEC-compliant contact string —
  EDGAR fetches now work (was 403 on `Mozilla/5.0`).

## Open threads (prioritized — start here)

**P1 normal-rate / justified-leg follow-ons** (the §18 layer is diagnostic-only; these
harden it and the OTHER names — none affect the durable SB-cheap finding, which rests on the
§5b-independent historical floor 0.733). All data-gated routes were pre-registered to defer:

   a. **§18.5b orderbook validation** — the parity "under-ordered" signal (dry-bulk −24%) is
      PROVISIONAL until validated against an INDEPENDENTLY observed orderbook-to-fleet ratio
      per sector (run per sector, crude included). Until then the parity column is a hypothesis
      with a test attached, not a result. This is what makes parity trustworthy or rejects it.
   b. **§18.5a Baltic mean-reversion data** — the historical_mean basis is v1 = current
      `historical_tce_means` (unvalidated); upgrade to a true $/day realized mean (BCI 5TC /
      BPI 4TC / BSI 10TC / New ConTex) and run the registered ≥70%-of-≥12q mean-reversion gate.
   c. **Product LR1 / Handysize / Handymax `newbuild_contract` marks** — DEFERRED (not sourced
      mid-recompute, on purpose). Source dated broker contract marks, predict per-class bands,
      register AHEAD of computing (same discipline as the 8 done classes); then product/hybrid
      parity computes (now reads "pending"). LNG/container stay unvalidated (boom + resale-inflated).
   d. **NAV-layer thread — `curve.newbuild` basis inconsistency** (substantive, NOT cosmetic):
      the age-0 NAV mark means CONTRACT for dry-bulk/MR (Cape $74M≈contract) but RESALE for
      crude (VLCC $175M, plausibly stale-high even as resale), so cross-sector NAV comparisons
      inherit the inconsistency — upstream of crude P/NAV on both bases. Separate P2-style NAV
      curve-refresh (would move headline crude NAV → delta-review + re-ratify). See §18 close.
   e. **P3 presentation guards** (no number changes): suppress the non-composable LNG/container
      medians from the headline vector; "rich-near-peak" caveat on crude; §15 governance dual-read
      for TEN/CMDB (clean-NAV-justified ≠ haircut basis). Lowest-stakes; timebox.

Older dry-bulk refinement threads (now DONE by P2): Post-Panamax sub-class split + SB charter
rates — landed this push-block; removed from this list.
2. **CMBT open items** (in `cmbt_log.md`): verify FSO owned-vs-JV (zero `shuttle_contracted_book`
   if the FSOs are inside the equity-JV line); apply the §9.4 yard-quality discount to the
   China-heavy dry-bulk book (v1 is the "without discount" leg); confirm the NMax newbuild
   level vs a current NB quote; G&A/interest are Q1-annualised estimates; chemical/Windcat
   segment books are Dec-2025 vintage; `consensus_fwd_pe` APPROX (Q1 EPS one-off-gain-distorted).
3. **SB open items** (in `sb_log.md`): refresh `consensus_pnav` if a VIE SB NAV is obtained
   (currently P/BV common-book proxy); confirm the finance-lease current/non-current split,
   the exact €950/day + €5.0M mgmt-fee figures, and the buyback authorization from the raw 20-F.
4. **GNK/Diana tender** — the $24.80/sh cash-tender deadline was 2026-06-26 (now PAST). Verify
   the scheduled `gnk-diana-tender-jun26-check` fired and the outcome (deal vs lapse → revert to
   NAV-discount) is captured in `gnk_log.md`; re-frame GNK if not.

## Standing operational threads (carry forward)

### Q2-refresh carry-forwards (earnings calendar + preflight §0 drive timing)
- **Early cluster Jul-28 → Aug-6:** STNG/ASC/TNK/CCEC, then ECO/GNK/GSL/CMDB/DHT/INSW/SBLK.
  Now also **CMBT** (ex-Euronav reports ~mid-Aug; H1 basis) and **SB** (early-Aug 6-K) join the
  dry-bulk refresh cycle.
- **BRUT (H1, Aug-13):** first issuer report vs the Pareto-estimate balance sheet; §15 screen.
- **CAPT (Q2):** verify the Jun-16 sponsor VLCC deal terms (§15 tripwire).
- **MPCC (Aug-26):** issuer fleet list → built years + NB delivery quarters; sale prints.
- **GSL (Aug-4/6):** Series B prefs post-ATM; the Jun-26 $917M NB order (apply §9.6).
- **TEN (Sep, H1):** TCM fee-load (§15 anchor); ten_log Q2 kit deltas. **CMDB:** Astros sale.

### Standing threads
- **FFA feed DORMANT since 2026-06-12** (source-side — the single poster stopped). Only the
  ffa_vs_strip diagnostic is stale; no live valuation input affected. Action is upstream.
- **Weekly /news-pull** — resume the Saturday cadence.
- **OWNER ACTION pending:** ratify-or-revise the A1 horizon (10 strip quarters = end-2028).
- **MB weeklies:** container current-rate refresh (owner-gated); Pana anchor flagged
  structurally low; LNG weekly not yet delivered.
- **Hormuz weight-revisit trigger** — standing (trigger NOT met).
- **Deferred by owner:** /news-pull agent-half orchestration; Task-3 weight adjuster;
  demand-destruction overlay; FFA Stage 2.

### Methodology-soundness remediation — Tier-4 backlog (manage/document; owner judgment)
Per `outputs/METHODOLOGY_AUDIT_2026-06-22.md` §A–G: cycle step-band vs logistic (C-1);
cross-sector anchor commensurability (C-2); marks statistical thinness / age-5 extrapolation
(B-1/B-2); k_broker band vs live (B-3); the 11% rate calibration (B-4); §15 haircut derivation
rule (E-1); data staleness (frozen container feed + APPROX names, F). Phase 2 drift gate is
DONE; **standing care: at each quarterly refresh expect the gate to flag legitimate moves —
annotate the material ones, then `./scripts/ratify_baseline.sh "<Qx refresh>"` to re-anchor.**

## Backtest (reference, not a gate)
`backtest/REPORT.md`: no statistically demonstrated cross-sectional edge. Test 1 (engine EV%,
Nq 23, IC −0.020, INCONCLUSIVE) and the powered P/B-proxy tests (Amendment-2 N=31 / Amendment-3
N=72, both exclude a moderate within-sector value premium on a book proxy) do NOT gate
development. **Test 2** (time-series reversion to fair value, in-sample IC +0.234, p 0.018) is a
HYPOTHESIS — pre-registered out-of-sample/multi-cycle confirmation runs at +8q (~end-2028) or on
a paid feed. Net: not a name-ranker (Test 1 null), plausibly a cycle/value timer (Test 2), unproven.

## Verification gate (run before any handoff / Week-close)
- `PYTHONPATH=src .venv/bin/python -m pytest -q` — main suite, **334** at 2026-06-28 (includes
  the Phase 2 drift gate, which can legitimately go red on accepted drift — annotate + re-ratify).
- `PYTHONPATH=. .venv/bin/python -m pytest backtest/ -q` — backtest (**13**; separate).
- (optional) `cd shipping_harvester && PYTHONPATH=. ../.venv310/bin/python -m pytest -q` — **57**.
- `python -m crude_tanker_fv.pipeline 2026-Q1` runs clean.
- `python -m crude_tanker_fv.reconcile --all` — SANITY all OK/n-a-APPROX; annotate >2pp drift.
- Clean git state; push `origin main`. `.venv310/`, `shipping_harvester/data/`,
  `backtest/vintages/*/` are gitignored by design. NOTE: every pipeline run auto-prepends a
  model-state entry to ALL `decisions/<t>_log.md` and regenerates `outputs/*` — commit that
  churn deliberately (it is expected, mostly "+0.0pp no material moves").
