# PLAN.md — active plan / sprint handoff

A new agent reads CLAUDE.md, then this file, then starts. This is a
**forward-looking valuation aid** for shipping equities (independent NAV +
forward dividend strip, blended by cycle position), judged by the soundness of
its per-name reads — not by a cross-sectional backtest.

**Current state (2026-06-28):** **22 watchlist names across 5 sectors**; **334 main
tests green** (+13 backtest via `PYTHONPATH=. pytest backtest/`; +57 harvester via
`.venv310`); `reconcile --all` **22/22 SANITY OK** (0 fail, 0 drift); drift gate 0
unexplained; pipeline clean; pushed to `origin/main` @ `a77e217`. The live engine
GAINED two capabilities this arc (both documented + tested):
1. **N-sleeve multi-sleeve generalization** (METHODOLOGY §11.9, `MULTI_SLEEVE_TICKERS`)
   — `sector_carve_out` + `_aggregate_multi_sleeve_report` over arbitrary sector sets;
   fixed a latent `_sleeve_for` bug routing dry_bulk/container classes to crude.
2. **dwt-scaling of the dry-bulk value curves** (METHODOLOGY §11.7.10) — Cape/Pana/
   Supra-Ultra value scales by `vessel.dwt / curve.dwt` (the curve carries `dwt_scaled`);
   the transaction fit dwt-normalizes prints to the baseline. **Dry-bulk manifest `dwt`
   is now LOAD-BEARING.** Crude/product/lng/container stay flat-per-class.

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

1. **Post-Panamax sub-class — HIGHEST-VALUE refinement (§11.7.10).** The dry-bulk "Pana"
   class collapses 74k Panamax → 96k Post-Panamax onto one 82k Kamsarmax curve; dwt-scaling
   lifts the 85-96k hulls 1.04-1.17× but old Post-Panamax trade at a per-tonne discount, so
   the tool over-values them. **SB (16 Post-Panamax) is the clearest case** — its +49% BUY is
   mark-rich because of this; CMBT/SBLK also carry some. Separating ~85-96k Post-Panamax into
   its own value class (own newbuild/scrap anchors; could share Pana rates like NMax shares
   Cape) would tighten the dry-bulk marks. Scoped but DEFERRED pending owner go-ahead.
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
