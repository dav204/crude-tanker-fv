# PLAN.md — active plan / sprint handoff

A new agent reads CLAUDE.md, then this file, then starts. This is a
**forward-looking valuation aid** for shipping equities (independent NAV +
forward dividend strip, blended by cycle position), judged by the soundness of
its per-name reads — not by a cross-sectional backtest. Development proceeds
normally (the 2026-06-14 "development freeze" was lifted 2026-06-21).

**Current state (2026-06-23):** 20 watchlist names across 5 sectors; **315 main
tests green** (+13 backtest, run via `PYTHONPATH=. pytest backtest/`); `reconcile
--all` 20/20 SANITY OK (0 fail, 0 drift); drift gate 0 unexplained; tree clean,
pushed to origin/main. **The live valuation engine is unchanged this arc** — all
work below is the methodology-soundness remediation (audit fixes + the Phase 2/3
guardrails and ex-post validation). Per-change chronology is in `CHANGELOG.md`.

**A NEW AGENT: read CLAUDE.md, then this file. Everything below "Methodology-audit
remediation" is DONE except the Phase 3(c) power backfill and the Tier-4 backlog.
The one thing to internalise before touching Test 1: the ⚠ HANDOFF box in 3(c) —
the harvester + its parser work are NOT in this repo's git.**

## Recent arc — methodology-soundness remediation (2026-06-22 → 06-23)

Three stages, all pushed (see `CHANGELOG.md` for the commit-by-commit detail):
**(1) methodology-soundness sprint** (audit fixes, below); **(2) Phase 2 ongoing
accuracy gate**; **(3) Phase 3 ex-post validation** — the value-premium proxy test
(powered null) and the engine EV% Test-1 backfill pipeline (built end-to-end,
INCONCLUSIVE at n=5). Stage-1 detail:

Driven by a full adversarial audit (`outputs/METHODOLOGY_AUDIT_2026-06-22.md`) +
an epistemic deep-dive (`outputs/epistemic_soundness_memo_2026-06-22.md`):

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
  - **(c) Powered engine EV% Test 1 — FAITHFUL end-to-end pipeline BUILT; result
    INCONCLUSIVE at n=5; the only remaining step is POWER (the 2018–2023 backfill).**
    Pre-registered (`backtest/PRE_REGISTRATION_TEST1.md`, committed before any result —
    within-sector pooled IC of engine EV%-cheapness, FAIL only on a *significant
    anti-predictive* result), data contract (`backtest/DATA_CONTRACT_TEST1.md`), harness
    (`backtest/run_engine_test1.py`, unit-tested). The full chain runs on real data for 5
    quarters (2024Q3, 2025Q1–Q4): PDF→harvester→factor→`build_vintage`→as-of engine→EV%→IC.
    **Every signal-moving leg is vintaged point-in-time** — NAV vessel marks (xclusiv
    geometry), 12M-TC-anchored scenario forward, price (Sharadar raw close), BS core
    (cash/debt/shares, quarterly ARQ). Held/slow-rolled: working capital, newbuild & lease
    lines, fleet ages. **Result: mean IC +0.005, t 0.02, Nq 5 → INCONCLUSIVE** — faithful but
    underpowered by design (consistent with the powered proxy null, Amendment 3).

    **⚠ HANDOFF — the moving parts and what's gitignored:**
    - `shipping_harvester/` **source IS tracked** (since 2026-06-23) — incl. the xclusiv
      geometry secondhand age-curve extractor, the spot `avg|average` markers, and
      `_period_tc`. Only `shipping_harvester/data/` (the 62M crawl cache + broker PDFs) is
      gitignored. The harvester is NOT in `src/` and runs only on `.venv310` (its own deps).
    - **`.venv310`** (Python 3.12, gitignored, `uv`-provisioned) is the harvester env; the
      engine + 315-suite stay on **`.venv` (3.9)**. Never run one on the other. A fresh clone
      must re-provision `.venv310` (`uv venv --python 3.12 .venv310 && uv pip install --python
      .venv310/bin/python -r shipping_harvester/requirements.txt`) and re-crawl the cache.
    - Bridge artifacts (gitignored, regenerable): `backtest/vintages/_factor_marks.json`
      (harvester→glue), `backtest/vintages/_bs_quarterly.csv` (Sharadar ARQ pull), the
      `backtest/vintages/<q>/` trees. Committed glue: `build_vintage.py`,
      `run_engine_test1.py`, `pull_bs_quarterly.py`.

    **Reproduce the pipeline:** (1) `cd shipping_harvester && PYTHONPATH=. ../.venv310/bin/python
    -m shipping_harvester.cli run --since 2024Q1 --until 2026Q2 --capitallink`; (2) re-parse
    cached xclusiv + export `_factor_marks.json` **filtering `broker!='allied'`** (Allied is one
    stale 2024-02-20 issue, junk); (3) `set -a; source ~/.config/factor-portfolio.env; set +a;
    PYTHONPATH=~/Projects/factor-portfolio/src .venv310/bin/python backtest/pull_bs_quarterly.py`;
    (4) `PYTHONPATH=. .venv/bin/python -m backtest.build_vintage`; (5) `... -m
    backtest.run_engine_test1`.

    **Coverage reality (the binding constraint):** only **xclusiv** parses cleanly. Vessel
    age-curves + 12M-TC cover 2024Q3/2025Q1/2025Q2 (xclusiv dropped 1y-T/C prose after 2025Q2 →
    2025Q3/Q4 forward falls back to the through-cycle mean). intermodal/banchero/weber parsers
    return nothing; Allied is dropped.

    **NEXT — (c) the 2018–2023 backfill for POWER (the only thing that buys a verdict; n=5 is
    underpowered).** Multi-week per-era parser work: each era's xclusiv format needs its own
    tuning (the 2024-vs-2025 spot/TC variants prove it) + the OCR-era risks the feasibility memo
    flags (`outputs/test1_data_feasibility_memo_2026-06-22.md`). Lower-value polish: vintage
    working-capital/fleet-ages; extend the parsers to Allied/other houses.
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
- `PYTHONPATH=src .venv/bin/python -m pytest -q` — main suite, must stay green (**315** at
  2026-06-23; includes the Phase 2 drift gate, which can legitimately go red on accepted
  drift — annotate + re-ratify rather than revert).
- `PYTHONPATH=. .venv/bin/python -m pytest backtest/ -q` — backtest suite (**13**; separate,
  `testpaths=["tests"]` excludes it from the main run).
- (Test-1 tooling, optional) `cd shipping_harvester && PYTHONPATH=. ../.venv310/bin/python -m
  pytest -q` — harvester (**57**, the gitignored vendored tool).
- `python -m crude_tanker_fv.pipeline 2026-Q1` runs clean.
- `python -m crude_tanker_fv.reconcile --all` — SANITY all OK/n-a-APPROX; annotate
  any >2pp drift / band flip in `decisions/<ticker>_log.md`.
- Clean git state; push `origin main`. **Note:** `.venv310/`, `shipping_harvester/`,
  `backtest/vintages/*/`, and `backtest/vintages/_*.{json,csv}` are gitignored by design —
  a clean `git status` is expected even with the Test-1 tooling present (see 3(c) ⚠ HANDOFF).
