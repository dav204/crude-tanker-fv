# PLAN.md — active plan / sprint handoff

A new agent reads CLAUDE.md, then this file, then starts. This is a
**forward-looking valuation aid** for shipping equities (independent NAV +
forward dividend strip, blended by cycle position), judged by the soundness of
its per-name reads — not by a cross-sectional backtest. Development proceeds
normally (the 2026-06-14 "development freeze" was lifted 2026-06-21).

**Current state (2026-06-22):** 20 watchlist names across 5 sectors; **315 tests
green** (+13 backtest, run separately); `reconcile --all` 20/20 SANITY OK (0 fail,
0 drift); committed drift gate ratified (Phase 2 below). This session ran a **methodology-soundness sprint** (full
adversarial audit → fixes — see below) and then built the **Phase 2 ongoing
accuracy gate**. Per-change detail is in `CHANGELOG.md`; the full analyses live in
the `outputs/*_2026-06-22.md` memos.

## This session — methodology-soundness sprint (2026-06-22)

Driven by a full adversarial audit (`outputs/METHODOLOGY_AUDIT_2026-06-22.md`) +
an epistemic deep-dive (`outputs/epistemic_soundness_memo_2026-06-22.md`). All
landed + pushed (5 commits, `e57e447..HEAD`):

- **Terminal value made honest (§9.2)** — was a doc-vs-code contradiction.
  Implemented (a) a **cycle-conditional multiple** on the terminal *fleet* value
  (peak 0.90× … trough 1.10× via `cycle.terminal_multiple`) and (b) **net
  retained earnings** (`terminal cash += Σ(EPS−DPS)/share`). Book moved
  (CCEC +31pp; GSL/TNK/STNG → BUY; DHT FV 14.31→14.00); SANITY 0 fail. Decision
  record: `outputs/terminal_value_options_memo.md` §5.
- **§12 reframed (R3)** — the high-payout-peak "undervaluation / NAV-floor /
  don't-act-on-the-TRIM" override (audit finding E-3) → a **falsifiable computed
  test**: §12.5 trigger gate, §12.6 break-even-dividend-window test (`Q*` vs the
  FFA-supported horizon), §12.7 ex-post falsification. New diagnostic-only
  `dividend_window.py` → `outputs/dividend_window_test.md` (NAT gates in → TRIM
  stands). Analysis: `outputs/peak_cycle_high_payout_resolution_2026-06-22.md`.
  *(The 0.9× terminal is vindicated and NOT exempted for high-payout names.)*
- **Bug fixes:** BUG-1 (Aframax dual cycle-anchor 27,600→36,483 + cross-file
  guard), BUG-2 (Sinokor en-bloc row out of the VLCC fit via a new `in_fit`
  flag), Phase 0b inert (BUG-4 §15 report blend line foots / BUG-5 Crude Set A
  weights value-pinned / BUG-6 loader raises on a partial-null curve / BUG-7
  shared `nav.COST_OF_EQUITY` / BUG-8 backtest framing / G-1 empty-fleet guard).
- **Honest framing (Phase 1):** README + LIMITATIONS §1 independence note
  (independence from broker *opinion*, not *data*; no demonstrated ex-post edge);
  "transaction-validated" → "transaction-anchored (single-vendor-sourced)".
- **CLAUDE.md restructured** 1147→259 lines (→ `CHANGELOG.md` / `TICKER_NOTES.md`
  / `WORKFLOWS.md`).

## Methodology-audit remediation — REMAINING (the staged plan's next phases)

Full remediation plan + designs are in the three memos above. Open phases, in order:

- **Phase 2 — ongoing accuracy gate (Option B). ✅ DONE (2026-06-22).** Built
  `src/crude_tanker_fv/drift_gate.py` + committed
  `baselines/reconcile_baseline.yaml` (20 names: EV% / tool_NAV / position_band /
  k_broker + ratifying commit + cause) + `tests/test_drift_gate.py` (17 tests; the
  live gate fails the build on an unexplained >2pp EV%/NAV move, a band flip, or a
  >0.05 k_broker SECOND-DIFFERENCE move — greps `decisions/<ticker>_log.md` for a
  dated non-placeholder annotation; APPROX names tracked on self-consistency only,
  no Δk gate) + `scripts/ratify_baseline.sh` (mandatory cause; writes the YAML,
  human commits). Pareto-free by construction (k tracked on its change, never its
  level); reuses `reconcile.APPROX_PNAV_TICKERS` single-sourced. Baseline ratified
  from the current 2026-Q1 outputs @ d382bfd. **Standing care:** at each quarterly
  refresh, expect the gate to flag the legitimate moves — annotate the material
  ones, then `./scripts/ratify_baseline.sh "<Qx refresh>"` to re-anchor.
- **Phase 3 — ex-post validation (Option C).**
  - **(a) Value-premium proxy test — ✅ DONE (2026-06-22).** Pre-registered
    Amendment 3 (committed `db9c4f6` *before* the runner — git-order proof), then
    built `backtest/loaders_sharadar.py` (reads factor-portfolio's
    `v2-validation-first` Sharadar cache CSVs directly — point-in-time via
    `filed`-date, no 3.10+ cross-repo import) + `backtest/run_proxy_powered.py`,
    reusing `evaluate_wide`/`loaders`. **Result: powered near-null** — sector-neutral
    pooled P/B IC **+0.036, t 0.62, Nq 72** (2008–2025, 17 watchlist names incl. all
    5 crude flagships + full product), bootstrap 95% CI [−0.079, +0.151], split-half
    unstable (early +0.090 / late −0.018). Excludes a *moderate* within-sector value
    premium, blind to a small one. The Amendment-2 null reproduced on the *right*
    universe; still a PROXY (book≠NAV) so NOT an engine verdict. +3 backtest tests
    (cache-guarded). Full write-up: `backtest/REPORT.md` Amendment 3.
  - **(b) Engine as-of-quarter plumbing — ✅ DONE (2026-06-22).** Parametrized
    `scenarios.quarter_keys(n, start_q, start_y)` + added `strip_start_from_asof`
    (report quarter + 2 → q3_2026 for the live 2026-Q1) and an `asof_quarter`
    parameter threaded `run_scenarios → _run_scenarios_for_ticker →
    run_scenarios_watchlist`. `None` default = the live q3_2026 anchor, **byte-identical**
    (315 tests green; pipeline 0 material deltas; drift gate 20/20 +0.0pp). A
    non-default as-of with no vintage scenario curves **fails fast** naming the
    missing keys. The single-point NAV/strip path was already as-of-correct via
    `quarter` (positional strip), so only the scenario quarter-key labels needed
    routing. +4 tests. **What 3c still needs:** the vintage scenario curves
    (the data backfill) — the plumbing is ready to consume them.
  - **(c) Powered engine EV% Test 1 — method LOCKED + harness READY; blocked only
    on the (env-gated) free-broker-weekly backfill.** ✅ Pre-registered
    (`backtest/PRE_REGISTRATION_TEST1.md`, committed before any result — within-sector
    pooled IC of EV%-cheapness, FAIL only on a significant anti-predictive result),
    ✅ data contract written (`backtest/DATA_CONTRACT_TEST1.md` — per-vintage source /
    no-look-ahead / slow-roll spec, free-broker-weekly), ✅ harness built + tested
    (`backtest/run_engine_test1.py` — reads `backtest/vintages/<q>/`, runs the as-of
    engine, computes the pre-registered statistic; sign convention + decision rule
    unit-tested; runs clean with no vintages). **Remaining = data only:** populate
    vintages via the free-broker-weekly backfill. Owner-committed to free broker-weekly
    (over a paid feed). **Env gate CLEARED (2026-06-22):** provisioned Python 3.12 via
    `uv` into `.venv310` (gitignored; engine + 315-suite stay on `.venv` 3.9); the
    harvester imports, its 57 tests pass, and it parses real broker PDFs under 3.12.
    **Remaining = the backfill itself:** (i) crawl/download 2024-Q1+ issues (the tuned
    era) → vintage `market_data` via the factor adapter + class-rename/`dwt` shim;
    (ii) Sharadar BS core + slow-rolled fleet/cost/div per `DATA_CONTRACT_TEST1.md`;
    (iii) run `run_engine_test1` (expect INCONCLUSIVE at MVP n); then the 2018–2023
    powered window. **Per-era parser development is now the EMPIRICALLY-CONFIRMED binding
    constraint** (not just estimated): the full MVP crawl (`run --since 2024Q1 --until
    2026Q2 --capitallink`, 1,412 issues, 60 mark-sets) parses only via **xclusiv + allied**;
    `vessel_value` came back **dry-bulk + NEWBUILD-anchor only** (no tanker values, no
    5yr/10yr), which is not valuation-grade for the age-curve NAV. Parser work: (a) ✅ **xclusiv
    geometry age-curve extractor done** — the pre-2025 two-column secondhand table now yields the
    full age curves for **both tanker (VLCC/Suezmax/Aframax/MR) and dry tiers (Capesize→Cape,
    Kamsarmax→Pana, Ultramax→Supra-Ultra, Handy)** — all 8 classes resale/5/10/15yr, newbuild
    merged (re-parsed 10 cached issues → 183 vessel_value rows, verified through the factor
    schema). (b) extend the same geometry approach to allied; (c) fix intermodal/banchero/weber;
    (d) per-era format coverage 2018–2023 + the 2026 post-redesign grid. The
    factor→engine glue is **built** (`backtest/build_vintage.py`: class-rename/dwt/`musd`×1e6,
    resale→newbuild, merge-over-live, scenario re-key, as-of raw close). **END-TO-END CHAIN
    PROVEN (2026-06-22):** generated 5 vintages (2024Q3, 2025Q1–Q4) and ran `run_engine_test1`
    — PDF→harvester→factor→glue→as-of engine→EV%→IC executes on real data for all 16–17 names.
    **#1 (scenario-forward synthesis) + #2 (vintaged rates) ✅ DONE (2026-06-22):** a one-line
    xclusiv marker fix (`average`→`avg`, the 2025 redesign) unlocked consistent vintaged tanker
    spot across all 5 quarters; `build_vintage.synthesize_scenarios` replaces the held 2026 levels
    with a neutral mean-reversion forward (vintaged spot → through-cycle TC mean, ±25%). Re-run:
    EV%s no longer uniformly-BUY, per-quarter ICs vary (+0.50/+0.68/−0.32/−0.24/−0.16),
    **mean IC +0.092 / t 0.44 / Nq 5 → INCONCLUSIVE** — now a *legitimate* vintaged read (real NAV
    marks + real spot-derived forward + real price), not plumbing-validation. (a) ✅ **12M-TC
    anchoring DONE (2026-06-23):** added `xclusiv._period_tc` (1y-T/C prose; Allied's period_tc
    was one stale junk issue, dropped) → vintaged 12M TC for 2024Q3/2025Q1/2025Q2 (xclusiv
    dropped the prose after, so 2025Q3/Q4 mean-fallback); `synthesize_scenarios` now anchors on
    TC (TC-consistent with the means). Re-run mean IC +0.086 → INCONCLUSIVE (unchanged at n=5).
    **Remaining for a fully-faithful Test 1:** (b) vintage the BS core (Sharadar —
    `loaders_sharadar` has it); (c) the 2018–2023 backfill for POWER (n=5 is underpowered by
    design); (d) more houses/eras. Vintage trees + schema JSON gitignored
    (reproducible via `build_vintage`). Deliberate ~2–4 wk build —
    `outputs/test1_data_feasibility_memo_2026-06-22.md`. Harvester runs on `.venv310` from
    `shipping_harvester/` (gitignored).
- **§16 overlay-ledger row for §12 — ✅ DONE (2026-06-22).** `overlay_ledger.py`
  now auto-derives a **§12.6** row per gated name from the COMPUTED
  dividend-window classification (`dividend_window.build_rows`), mirroring the §15
  auto-population. NAT renders as a *neutral* "TRIM stands (value trap), no FV
  change" row (Q*>strip vs H=8.0); the stale hand-written NAT "treat FV as a NAV
  floor" §12 row (which contradicted the computed TRIM-stands) is removed and SBLK
  relabelled §12.2. Closes audit E-2 ("ledger is documentation, not a control")
  for this overlay type — the row can no longer drift from the diagnostic. +3 tests.
- **Tier-4 structural backlog (manage/document — owner judgment, detail per item
  in `outputs/METHODOLOGY_AUDIT_2026-06-22.md` §A–G):** cycle step-band vs
  logistic (C-1); cross-sector anchor commensurability + suppress cross-sector
  pair-trades (C-2); marks statistical thinness / age-5 extrapolation / duplicate
  prints (B-1/B-2); k_broker band vs live (B-3); the 11% rate calibration (B-4);
  §15 haircut derivation rule (E-1); data staleness — frozen container feed +
  APPROX names (F).

## Active backlog (operational — predates this sprint, still live)

### Near-term
- **GNK / Diana tender — RESOLVES Jun-26.** A one-time check is SCHEDULED
  (`gnk-diana-tender-jun26-check`, ~Jun-26 8pm ET): read the tender outcome + any
  board decision on the non-binding $27.34 proposal and re-frame GNK (deal-arb →
  NAV-discount on a lapse; expect reversion toward ~0.70× Pareto NAV). Then
  annotate `decisions/gnk_log.md`.
- **FFA feed DORMANT since 2026-06-12** (source-side — the single poster stopped
  posting the parseable grid; NOT a pipeline fault; the staleness alarm fires
  weekly). Action is upstream: check the Rocket.Chat channel / consider an
  alternative FFA source (Baltic settlements, MB weekly). Only the ffa_vs_strip
  diagnostic is stale meanwhile — no live valuation input is affected.
- **Weekly /news-pull** — resume the Saturday cadence (Jun-21 digest done).

### Q2-refresh carry-forwards (earnings calendar + preflight §0 drive timing)
- **Early cluster Jul-28 → Aug-6:** STNG/ASC/TNK/CCEC, then ECO/GNK/GSL/CMDB/
  DHT/INSW/SBLK.
- **BRUT (H1, Aug-13):** confirm the Pareto-estimate balance sheet against the
  first issuer report; complete the §15 screen (needs the admission prospectus);
  refine the NB cohorts.
- **CAPT (Q2):** verify the Jun-16 sponsor VLCC deal terms/funding (§15 tripwire).
- **MPCC (Aug-26):** issuer fleet list → built years + NB delivery quarters (the
  `years_to_delivery` are deck estimates); 3 sale-print prices; NAV anchor.
- **GSL (Aug-4/6):** Series B prefs post-ATM; the Jun-26 $917M NB order's
  charterers + delivery schedule (then apply §9.6 to GSL); 20-F board rights.
- **TEN (Sep, H1):** TCM fee-load (§15 anchor; the +36% dividend argues the 30%
  haircut down — feeds the §12.6 window test too); ten_log Q2 kit deltas.
  **CMDB:** the Astros sale price.

### Standing threads
- **OWNER ACTION pending:** ratify-or-revise the A1 horizon (wired as 10 strip
  quarters = end-2028).
- **MB weeklies:** container current-rate refresh (owner-gated); Pana anchor
  flagged structurally low; LNG weekly not yet delivered.
- **Hormuz weight-revisit trigger** — standing (trigger NOT met).
- **§5 ask-tier verification** — confirm git push / watchlist-edit / fetch_links
  / curl actually PROMPT in an interactive session.
- **Deferred by owner:** /news-pull agent-half orchestration; Task-3 weight
  adjuster; demand-destruction overlay; FFA Stage 2.

## Backtest (reference, not a gate)
Crude-subsector edge backtest in `backtest/` (`REPORT.md`): no *statistically
demonstrated* cross-sectional edge. The real-P/NAV tests are inconclusive by design
(~6q). **Two powered P/B-proxy tests now exist:** Amendment-2 (N=31, 9 names, no
DHT/FRO/ECO/product) and **Amendment-3 (N=72, the actual 17-name watchlist incl. all
crude flagships + product; sector-neutral IC +0.036/t 0.62, CI [−0.079,+0.151])** —
both exclude a *moderate* within-sector value premium. Both are *book* proxies, so they
bound the value premise, NOT *this* engine's market-NAV marks. The powered **engine** EV%
test (Phase 3 b/c) is still the only read that can validate/refute the marks
(`outputs/test1_data_feasibility_memo_2026-06-22.md`). No longer gates development.

## Verification gate (run before any handoff / Week-close)
- `PYTHONPATH=src .venv/bin/python -m pytest -q` — must stay green (308 at 2026-06-22;
  includes the Phase 2 drift gate, which can legitimately go red on accepted drift —
  annotate + re-ratify rather than revert).
- `python -m crude_tanker_fv.pipeline 2026-Q1` runs clean.
- `python -m crude_tanker_fv.reconcile --all` — SANITY all OK/n-a-APPROX; annotate
  any >2pp drift / band flip in `decisions/<ticker>_log.md`.
- Clean git state; push `origin main`.
