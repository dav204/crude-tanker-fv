# Changelog — Tanker FV tool

Split out of CLAUDE.md (2026-06-22) to keep the operating rulebook short.
Append new dated entries at the TOP. This is the running history of
methodology decisions, onboardings, and fixes; CLAUDE.md carries only the
live rules distilled from it.

- **2026-06-23 — Phase 3(c) point-in-time balance-sheet core (Sharadar).** `build_vintage`
  now vintages **cash, total_debt** (Sharadar `LongTermDebtNoncurrent + DebtCurrent`) and
  **diluted shares** per name, point-in-time (ARY, filed-date <= quarter-end, no look-ahead),
  overwriting the slow-rolled base. (Cash was initially thought absent — it is cached under
  `CashAndCashEquivalentsAtCarryingValue`, a field-name mismatch, now included; DHT 2024Q3 cash
  $74.7M.) The shipping-specific lines (working capital, newbuild commitments, leases) stay
  slow-rolled. **Confirmed I can run a direct Sharadar SF1 pull** (key
  `NASDAQ_DATA_LINK_API_KEY` in `~/.config/factor-portfolio.env`, factor-portfolio's
  `fetch/sharadar.py`, deps in `.venv310`) — live-fetched DHT to verify — so the cache can be
  extended (quarterly ARQ grain, SG&A/interest/tax for the strip) on demand. Verified per-quarter variation
  (DHT debt 428.7M @2024Q3 → 409.4M @2025Q2; shares ~160M). Re-ran `run_engine_test1`:
  **mean IC +0.056, t 0.31, Nq 5 → INCONCLUSIVE** (shifted from +0.086 as vintaged debt/shares
  move NAV/share; still near-zero at n=5). Debt + share count were the dominant held BS drivers;
  residual held = cash, working capital, fleet ages, newbuild/lease lines.
- **2026-06-23 — Phase 3(c) 12M-TC anchoring — the scenario forward is now TC-consistent.**
  Replaced the spot anchor (which mismatched the TC-anchored cycle means, the §10 gotcha) with
  vintaged 12-month TC. Source: not Allied (its `period_tc` is one stale 2024-02-20 issue,
  mis-parsed to a constant — dropped from the panel), but **xclusiv's 1y-T/C prose**, which the
  parser ignored. Added `xclusiv._period_tc`: each `USD n/day` level is a TC mark only when
  "1y T/C" is the nearer rate-type keyword before it (vs the spot "T/CE"), class = nearest class
  word; a sanity band + change-figure guard ("…firmer…, at USD …") + a 115-char back-window
  handle the 2024 vs 2025 prose variants. Yields full tanker 12M TC (VLCC/Suezmax/Aframax/LR2/MR,
  on the TC scale ~29–49k) for **2024-Q3 / 2025-Q1 / 2025-Q2**; xclusiv dropped the 1y-T/C prose
  after 2025-Q2, so **2025-Q3/Q4 fall back to the through-cycle mean** (neutral, not spot, to
  avoid a TC-vs-spot level confound). `build_vintage.synthesize_scenarios` now anchors on
  `vintaged_tc` (mean fallback). Re-ran `run_engine_test1`: VLCC forward now on the TC scale
  (2024Q3 base 48312 ≈ TC 49.5k; 2025Q4 base = mean 40k); **mean IC +0.086, t 0.42, Nq 5 →
  INCONCLUSIVE** (unchanged near-zero at n=5, as the cross-sectional NAV signal dominates). The
  methodology mismatch is fixed; remaining fidelity gap = the held balance sheet (Sharadar BS
  vintaging). Harvester 57 tests green. Allied excluded at the export step (note in
  `build_vintage`).
- **2026-06-22 — Phase 3(c) neutral scenario-forward synthesis + vintaged spot — first
  *legitimate* Test-1 read (still small-n).** Removed the dominant contaminant (held 2026-Hormuz
  scenario levels). **(#2 vintaged rates):** found the Allied `period_tc` is a constant mis-parse
  (VLCC 5934 every quarter — signal-free) and xclusiv carries no period TC; but the 2025 xclusiv
  redesign abbreviates "average T/CE"→"avg T/CE", so a one-line marker fix
  (`(?:average|avg)`) unlocked **consistent vintaged tanker spot across all 5 quarters**
  (VLCC 38.6k→42.9k→35.1k→89.3k→95.9k). **(#1 synthesis):** `build_vintage.synthesize_scenarios`
  replaces the held curves with one neutral scenario per sector whose per-class forward glides
  the vintaged spot toward the through-cycle TC mean (±25% band) — DATA_CONTRACT_TEST1.md's
  neutral forward. Scale verified: the cycle-anchor means (VLCC 40k) are on the same $/day scale
  as xclusiv spot, so the synthesized forward yields realistic vintaged cycle positions (2024Q3
  VLCC ~0.97×, 2025Q4 ~2.4×). Re-ran `run_engine_test1`: EV%s no longer uniformly-BUY; per-quarter
  ICs vary (+0.50/+0.68/−0.32/−0.24/−0.16); **mean IC +0.092, t 0.44, Nq 5, CI [−0.155,+0.223],
  hit-rate 49% → INCONCLUSIVE** (expected at n=5). Now a legitimate vintaged read (real NAV marks
  + real vintaged spot-derived forward + real price), no longer plumbing-validation. Caveats:
  SPOT-anchored not 12M-TC (no reliable vintaged TC), BS held, n=5. Remaining for fully-faithful
  Test 1: 12M-TC anchoring, Sharadar BS vintaging, the 2018–2023 backfill for power.
- **2026-06-22 — Phase 3(c) factor→vintage glue + first end-to-end Test-1 chain run
  (plumbing-validation).** Built `backtest/build_vintage.py`: reads the harvester's resolved
  marks (`_factor_marks.json`, exported from `.venv310`), converts to engine
  `vessel_value_curves` (class-rename Capesize→Cape / Kamsarmax→Pana / Ultramax→Supra-Ultra,
  resale→newbuild proxy, musd×1e6), **merges** over the live curves (uncovered classes keep
  live marks so NAV never breaks), re-keys `scenario_inputs` to the vintage's strip quarters
  (so the Phase-3b as-of routing fires), sets `current_price` to the Sharadar raw close at the
  quarter-end, and assembles the full vintage tree (fleet/cost/dividend held; balance sheet
  quarter-renamed). Generated 5 vintages (2024Q3, 2025Q1–Q4 — the valuation-grade quarters) and
  ran `run_engine_test1`: **the whole chain executes end-to-end on real data** (PDF → harvester
  → factor → glue → as-of engine → EV% → within-sector IC) for all 16–17 names, no errors.
  Result **mean IC +0.220, t 1.70, Nq 5, CI [+0.014, +0.294] → INCONCLUSIVE**. **This is a
  PLUMBING-VALIDATION read, NOT a valid Test-1 result:** only vessel_value + price are vintaged;
  TC, scenario *levels*, and balance sheets are held from live (held 2026-peak scenario levels
  value fleets against lower 2024–25 prices → near-universal BUY), so the number is not
  interpretable as signal — it proves the chain works. For a valid result still needed: synthesise
  the neutral mean-reversion scenario forward (vs held levels), vintage the TC (fix the Allied
  parser), vintage the balance-sheet core (Sharadar), + more quarters/houses. Generated vintage
  trees + the schema JSON exports are gitignored (reproducible via `build_vintage`); the glue
  code is committed.
- **2026-06-22 — Phase 3(c) first parser extension: xclusiv geometry-based age-curve
  extractor — unlocks the tanker vessel-value curves.** Closed the highest-leverage coverage
  gap. The pre-2025 Xclusiv secondhand-values table is a **two-column text layout** (value
  table left, S&P prose right) that pdfplumber does NOT detect as a ruled grid, so the existing
  `_secondhand(tables)` extractor missed it entirely (newbuild-only output). Added a
  **word-geometry** extractor (`xclusiv.XclusivParser._secondhand_geom`, wired via a `parse()`
  override that has the pdf_path): isolates the left value column by x-coordinate, reads the age
  label (Resale/5/10/15yr at x0≈85) + the current value (first numeric to its right),
  reconstructs one class per Resale→15yr block, and applies a **monotonic-curve sanity filter**
  so mis-joins drop rather than corrupt. Result on the real 2024-Q3 issue: **36 vessel_value
  marks** (was newbuild-only), incl. the **complete tanker age curves VLCC/Suezmax/Aframax/MR
  (resale/5/10/15yr)** — the previously-absent marks the engine's age-curve NAV needs for the
  crude/product watchlist names. Dry then completed too: the dump revealed the table groups
  **Kamsarmax/Panamax and Ultramax/Supramax into single curves — the same Pana / Supra-Ultra
  tiers the engine uses** — so assigning each block its *topmost* label (not block-center) yields
  full curves for Capesize→Cape, Kamsarmax→Pana, Ultramax→Supra-Ultra, Handy, with the text
  newbuild merging in. **All 8 classes (4 tanker + 4 dry tiers) now carry full age curves**,
  verified through the factor schema (re-parsed 10 cached issues → 183 vessel_value rows, 80
  tanker age-curve rows). Harvester's own xclusiv + dispatch tests stay green (15). **The harvester is gitignored
  (vendored cross-check), so the parser code lives in the working tree, not this repo's history;
  the committed deliverable is the coverage win + (next) the assembled vintages.** Remaining:
  dry class-naming, fix intermodal/banchero/weber, per-era 2018–2023, then the factor→vintage
  glue + `run_engine_test1`.
- **2026-06-22 — Phase 3(c) MVP backfill kicked off — pipeline proven, parser coverage
  measured as the binding constraint.** Ran the harvester end-to-end: small validation crawl
  (HSN, recent quarters) then the full MVP crawl `run --since 2024Q1 --until 2026Q2
  --max-pages 70 --capitallink` (1,412 raw issues, 60 (broker,quarter) mark-sets stored; crawl
  → dedupe → download → parse → store → panel/coverage/factor all working under `.venv310`).
  **Measured coverage (2024Q1–2026Q2):** only **xclusiv + allied** parse; intermodal /
  banchero / weber / fearnleys / advanced yield 0 (parser gaps / generic fallback).
  `period_tc` = VLCC/Suezmax/Aframax (tanker 1yr); `spot_tce` = 9 tanker+dry classes (broad);
  **`vessel_value` = Capesize/Handy/Kamsarmax/Ultramax, NEWBUILD anchor ONLY** — no tanker
  vessel values and no 5yr/10yr age anchors anywhere. **This is not valuation-grade:** the
  engine's age-curve NAV needs newbuild+5yr+10yr+scrap per class, so the MVP vintage cannot be
  assembled from current parser output. The memo's estimate (per-era parser development is the
  ~2–4 wk bottleneck) is now an empirical fact. The factor→engine glue is fully specified
  (class-rename `Capesize`→`Cape` etc., dwt injection, `musd`×1e6) and ready; it is gated on
  parser coverage, not the other way round. Harvester crawl cache is gitignored
  (`shipping_harvester/data/`).
- **2026-06-22 — Phase 3(c) env gate cleared: Python 3.12 provisioned for the harvester.**
  Owner chose provisioning a 3.10+ interpreter over a 3.9 backport. Installed CPython 3.12.13
  via `uv` into a dedicated **`.venv310`** (gitignored) with the harvester's deps (requests,
  beautifulsoup4, lxml, pdfplumber, pandas, pyarrow); the engine + the 315-test suite stay on
  `.venv` (3.9.6), untouched. The vendored `shipping_harvester` now imports under 3.12, its
  **57 tests pass**, and it parses real broker-weekly PDFs (smoke-tested on
  `state/fdprobe/Allied_2025.pdf`). That smoke test also confirmed the data contract's per-era
  reality: a non-2024-tuned format (the 2025 Allied sample) parses `confident=True` but yields
  only partial TC marks and no age-anchors — i.e. the env is unblocked, but **per-era parser
  tuning remains the real backfill work** (the 2024+ era is the tuned one). CLAUDE.md "How to
  run things" documents the two-venv split. Remaining for a result: the free-broker-weekly
  backfill (crawl 2024-Q1+ → vintages) per `backtest/DATA_CONTRACT_TEST1.md`.
- **2026-06-22 — Phase 3(c) Test 1 pre-registration + data contract + harness (engine EV%
  ex-post test; method locked, data pending).** Owner committed to the **free broker-weekly**
  data path. Wrote `backtest/PRE_REGISTRATION_TEST1.md` (locked before any result, git-order
  proof): the test of the tool's OWN signal — within-sector pooled IC of engine EV%-cheapness
  vs 1q-forward total return, valued as-of via the Phase-3b plumbing; decision rule **FAILs
  only on a significant anti-predictive result** (mean IC<0, t≤−2), EDGE on significant
  positive, INCONCLUSIVE the expected MVP outcome. Wrote `backtest/DATA_CONTRACT_TEST1.md`:
  per-vintage source / no-look-ahead / slow-roll spec mapped to the free broker-weekly sources
  (vessel marks + TC + spot are the only sign-moving per-quarter legs; BS core from Sharadar;
  fleet/cost/dividend slow-rolled; FFA + scenario forward are *derived* via mean-reversion
  synthesis — the live 2026 MoU scenario set is NOT back-projected, a locked departure). Built
  `backtest/run_engine_test1.py`: reads `backtest/vintages/<q>/`, runs the as-of engine
  (`run_scenarios_watchlist(asof_quarter=q, inputs_dir=…)`), computes the pre-registered
  statistic; the load-bearing EV%-cheapness sign convention (high EV% = cheap, via `−EV%` into
  the reused `wide_quarter_ic`) and the decision rule are unit-tested; runs clean with no
  vintages. +2 backtest tests (11→13; main `tests/` unaffected at 315). **Binding execution
  gate surfaced:** the vendored `shipping_harvester` is Python 3.10+ (`@dataclass(slots=True)`
  → TypeError under this Mac's 3.9.6), so the vessel-mark/TC vintage production needs a 3.10+
  interpreter or a small 3.9 backport — everything downstream already runs in the 3.9 venv.
  Design basis: `outputs/test1_data_feasibility_memo_2026-06-22.md`.
- **2026-06-22 — Phase 3(b) engine as-of-quarter plumbing (the prerequisite for the powered
  engine EV% test).** The scenario path hard-anchored the strip/scenario timeline to "now"
  (`QUARTER_KEYS = q3_2026…`), so it could not value a name as-of a historical quarter.
  Parametrized `scenarios.quarter_keys(n, start_q=3, start_y=2026)` (no-arg/single-arg calls
  unchanged) + added `scenarios.strip_start_from_asof(asof_quarter)` (report quarter + 2 ⇒
  q3_2026 for the live 2026-Q1 vintage) and an `asof_quarter` parameter threaded
  `run_scenarios → _run_scenarios_for_ticker → run_scenarios_watchlist`. `None` (default) =
  the live q3_2026 anchor, **byte-identical** to prior behaviour (315 tests green; `pipeline
  2026-Q1` 0 material deltas; drift gate 20/20 at +0.0pp/+0.0%/+0.000). A non-default as-of
  whose scenario doc lacks the vintage's forward-quarter curves **fails fast** naming the
  missing keys (the expected 3c "no historical data" failure mode — never silent mis-routing).
  The single-point NAV/strip path needed no change: the strip is positional and already
  as-of-correct via the `quarter` arg; only the scenario quarter-key *labels* (which index
  `scenario_inputs.yaml`) were calendar-anchored. +4 tests (311→315). 3(c) — the powered
  engine EV% test — now needs only the vintage scenario-curve backfill (its own go/no-go).
- **2026-06-22 — §16 overlay ledger: §12 dividend-window is now a control, not docs
  (closes audit E-2 for this overlay type).** `overlay_ledger.py` gains
  `dividend_window_rows(quarter)`, which auto-derives a **§12.6** row per gated name
  from the COMPUTED `dividend_window.build_rows` classification (same pattern as the §15
  governance auto-rows). NAT now renders as a *neutral* row — "TRIM stands (value trap)
  — premium NOT rate-supported (Q*>strip > H=8.0); no floor, no FV change" — with a "·"
  arrow (render gained a neutral direction). The **stale hand-written NAT §12 row**
  (`direction: up`, "treat tool FV as the NAV floor") is removed from `inputs/overlays.yaml`:
  it directly contradicted the computed TRIM-stands classification — the exact
  documentation-vs-control drift E-2 named. SBLK's peak-cycle note relabelled **§12.2**
  to disambiguate it from the §12.6 dividend-window gate (SBLK is not a high-payout
  single-class pure-play). `overlay_ledger.main` takes `--quarter` (defaults to latest
  balance-sheet quarter). +3 tests (308→311).
- **2026-06-22 — Phase 3(a) value-premium proxy test (Option C; powered, on the actual
  universe).** Pre-registered **Amendment 3** to `backtest/PRE_REGISTRATION.md` and committed
  it (`db9c4f6`) *before* writing any result-producing code — the same git-order discipline as
  Amendments 0–2. Then built `backtest/loaders_sharadar.py` (point-in-time book value + prices
  from factor-portfolio's `v2-validation-first` Sharadar cache, read directly from the cache
  CSVs with `filed`-date no-look-ahead — avoids a 3.10+ cross-repo import) and
  `backtest/run_proxy_powered.py`, reusing `evaluate_wide.wide_quarter_ic`/`mean_t` and
  `loaders.bvps_at`/`price_at`/`quarter_ends`. The Amendment-2 powered null ran on a 9-name
  SEC-XBRL panel that excluded DHT/FRO/ECO and all product; Sharadar standardizes the FPI
  20-F/6-K filings, so this runs on **17 of the 20 watchlist names — all 5 crude flagships +
  full product + dry-bulk + LNG — over deep history** (NAT→1997). **Result: a powered
  near-null** — sector-neutral pooled P/B IC **+0.036, t 0.62, Nq 72** (2008–2025), quarter-block
  bootstrap 95% CI [−0.079, +0.151], split-half unstable (early +0.090 / late −0.018); the raw
  whole-panel read +0.059 (t 1.36) is not significant. Excludes a *moderate* within-sector value
  premium, blind to a small one. It is a **book proxy** (book≠market NAV), so it bounds the
  value-premium *premise*, NOT the engine's marks — the powered engine EV% test (Phase 3 b/c)
  remains the only read that can validate/refute them. +3 cache-guarded backtest tests (backtest
  suite 8→11; the main `tests/` suite is unaffected at 308 — `testpaths=["tests"]`). Updated
  `backtest/REPORT.md` (Amendment 3 + combined verdict), README, LIMITATIONS §1 ("no demonstrated
  ex-post edge" now backed by a powered test on the right universe), PLAN.md.
- **2026-06-22 — Phase 2 ongoing accuracy gate (Option B; closes audit A-2).** The
  tool had no automated accuracy gate after sector launch — the one-time calibration
  lock is manual and never auto-invoked, and the >2pp drift alert ran against a
  gitignored, self-overwriting snapshot (`state/last_reconcile.json`), so drift had no
  durable anchor and no teeth. Built a **committed, Pareto-free drift gate**:
  `src/crude_tanker_fv/drift_gate.py`, the tracked `baselines/reconcile_baseline.yaml`
  (20 names — EV% / tool NAV / position band / k_broker, plus meta: ratified_at /
  ratified_commit / quarter / cause), `tests/test_drift_gate.py` (17 tests; +291→308),
  and `scripts/ratify_baseline.sh` (deliberate re-ratify, mandatory cause, human
  commits). The gate tracks the tool's **own** EV%/NAV/band against its committed prior
  (never broker NAV) and k_broker on its **second difference** (the *change* in the
  tool↔broker spread, never its level) — so a persistently-wide documented §6 spread
  (INSW k≈1.64, NAT k≈2.16) sits green forever and the gate never asks a number to move
  toward Pareto; only an *unexplained change* fails. Thresholds (ΔEV>2pp / ΔNAV>2% /
  Δk>0.05) live in the baseline `thresholds:` block (tunable without a code change). A
  breach clears via a dated, non-placeholder `decisions/<ticker>_log.md` annotation on/
  after `ratified_at`, or by re-ratifying with a cause; APPROX names (the reconcile set,
  single-sourced) are tracked on self-consistency only (no Δk gate). Baseline ratified
  from the current 2026-Q1 outputs @ d382bfd. Wired into CLAUDE.md "How to run things" +
  the Verification loop, and PLAN.md. Reuses the reconcile drift-delta pattern
  (`reconcile.py:144-150`) and `reconcile.APPROX_PNAV_TICKERS`. Design of record:
  `outputs/epistemic_soundness_memo_2026-06-22.md` §4 Option B.
- **2026-06-22 — Phase 1 honest framing (Option A; the direct fix for the CRITICAL
  epistemic finding).** Doc-only. Added an "independence and ex-post validation status"
  note to README + LIMITATIONS §1: the NAV is independent of broker *opinion* but not
  broker *data* (~76% of anchoring prints single-vendor-sourced, ~87% in dry-bulk/product;
  six shared-source names), so "independent" is narrow, and the tool has **no demonstrated
  ex-post cross-sectional edge** (auditable opinion, not backtested forecast). Retired the
  unqualified **"transaction-validated"** doctrine phrase → **"transaction-anchored
  (single-vendor-sourced)"** (CLAUDE.md "philosophically", METHODOLOGY Appendix A). README
  test count 286→291. *(Per-name corroboration-tier tags in `delta_report.md` deferred — a
  renderer change; the tiers are stated in the README/LIMITATIONS note for now.)*
- **2026-06-22 — Phase 0b inert cheap fixes (audit BUG-4/5/6/7 + G-1; framing BUG-8).**
  No valuation change (291 tests green). **BUG-4:** the §15 report blend line printed raw
  NAV while FV used the post-haircut value → now prints `nav_per_share_effective` so it
  foots for TEN/CMDB. **BUG-5:** value-pinned the Crude Set A weights (0.25/0.45/0.18/0.12)
  — sum-to-1 alone let a silent crude weight edit pass (LNG/product were already pinned).
  **BUG-6:** `loaders._list_map` silently dropped a partially-null FFA curve → now raises
  (a partial-null is a data error, not "class not covered"). **BUG-7:** the two decoupled
  `0.11` constants (`nav.NEWBUILD_DELIVERY_DISCOUNT_RATE`, `dividend_strip.DEFAULT_DISCOUNT_RATE`)
  now both reference `nav.COST_OF_EQUITY`. **G-1:** `compute_cycle` raises on an empty fleet
  instead of silently falling to the trough band. **BUG-8:** corrected the CLAUDE.md/PLAN.md
  backtest framing to match `REPORT.md` — the powered Amendment-2 null is a clean negative on
  a P/B proxy / different universe, not "expected small-sample" (which only fits the
  underpowered real-P/NAV tests).
- **2026-06-22 — BUG-1 (Aframax dual cycle-anchor) + BUG-2 (Sinokor row in the VLCC
  fit) fixed** (methodology audit, `outputs/METHODOLOGY_AUDIT_2026-06-22.md`).
  **BUG-1:** `historical_tce_means.yaml` carried a stale Aframax 10yr-mean of **27,600**
  while `scenario_inputs.yaml` `aframax_dirty` carried the B5-curated **36,483** — so the
  per-name FV / breakeven / sensitivity path (`compute_cycle`) and the scenario path
  computed *different cycle positions* for every Aframax-exposed name (TNK/TEN/INSW/HAFN/
  STNG). Reconciled to 36,483 (VLCC/Suezmax already matched) + new guard
  `test_cycle_anchor_cross_file_consistency`. **BUG-2:** the Sinokor en-bloc VLCC row
  (`vlcc.yaml`, age 12, $71M, labeled "documentation only — excluded") was actually IN the
  regression — the loader filtered on the age window only. Added an `in_fit: bool` flag to
  `TransactionPrint` + loader + `fit_curve_anchors`; set `in_fit: false` on the Sinokor row
  and the FRO-NB doc row. VLCC fit drops the $71M age-12 drag → age-10 anchor up → VLCC NAVs
  **+0.3–1.1pp** (DHT $12.93→$13.10; DHT report FV 14.00→14.15). All **under the 2pp drift
  gate; SANITY 0 fail; no position flips.** Tests 290 → 291.
- **2026-06-22 — cycle-conditional terminal + net retained earnings (§9.2) + §12
  reframed to a falsifiable dividend-window test (R3).** Part of the
  methodology-soundness audit (`outputs/METHODOLOGY_AUDIT_2026-06-22.md`). Resolved a
  doc-vs-code contradiction the audit found: METHODOLOGY:2115/824 claimed the strip
  terminal was "depleted by the dividends paid out" + "mean-reverts," but the engine
  aged hulls at a flat price level with the balance sheet held constant. Owner chose to
  make the engine honest, not walk back the docs.
  **Terminal (`dividend_strip.py` / `cycle.py`):** (1) **cycle-conditional multiple** on
  the terminal FLEET value — peak 0.90× / elevated 0.95× / mid 1.00× / below-mid 1.05× /
  trough 1.10× via `cycle.terminal_multiple` (cash/debt not reverted); (2) **net retained
  earnings** — terminal cash += Σ(EPS−DPS)/share (flat for ~100%-payout names, RISES for
  low-payout retainers — fixes the §12 buyback/low-payout undercount — falls for over-payers).
  No double-count (strip = PV(8q earnings) + PV(terminal asset), the standard
  explicit-period-plus-terminal DCF). The literal "subtract dividends" form was rejected as
  a double-count (owner decision). **Book impact (SANITY 0 fail; NAV untouched):**
  low-payout retainers up — **CCEC +31pp; GSL TRIM→BUY; TNK HOLD→BUY; STNG TRIM→BUY**;
  MPCC/FLNG/CMDB/HAFN/TRMD/INSW up — peak crude down — **DHT FV 14.31→14.00** (0.9×),
  FRO/ECO slightly down. Re-pinned: `test_terminal_multiple_cycle_conditional` +
  `test_terminal_retains_earnings_low_payout`; CCEC/INSW/STNG FV bands; DHT report FV;
  breakeven/sensitivity helpers (aligned to pass `terminal_multiple`).
  **§12 reframe (R3):** the owner-challenged §12 line ("TRIM signals … commercially
  misaligned") — an unfalsifiable one-way bullish override (audit E-3) — was reframed after
  a 4-agent analysis (`outputs/peak_cycle_high_payout_resolution_2026-06-22.md`) found the
  **model is right**: a high-payout pure-play at peak P/NAV ~2× is overvalued through-cycle
  (the fat yield is "the liquidation rate of a melting ice cube," ~−36% on the NAT
  arithmetic; NAT is its own 2015→2018 counterexample). The 0.9× terminal is **vindicated
  and not exempted** for high-payout names (exempting = the forbidden back-solve). §12 is now
  a falsifiable, computed classification: **§12.5** trigger gate (single-class + payout>90% +
  cycle>1.5× + price/tool-NAV>1.5×), **§12.6** break-even-dividend-window test (Q* vs the
  FFA-supported horizon H), **§12.7** ex-post falsification. New `dividend_window.py`
  (diagnostic-only, no FV change, consensus_eps-style) → `outputs/dividend_window_test.md`:
  **NAT gates in (premium 2.51×) → Q*=None (DPS never bridge the $3.13 premium) → TRIM stands**
  (value-trap, no override); DHT (1.27×) / SBLK (diversified) / all others gate out. Tests 287 → 290.
- **2026-06-22 — §9.6 time-to-delivery discount ROLLED OUT to the other newbuild
  books (owner-approved, post-BRUT).** Applied per-vessel `years_to_delivery` to
  CAPT / FRO / MPCC manifests (GSL's NB order is post-snapshot; CMDB has none).
  Moves, all SANITY-OK: **CAPT NAV $17.74 → $15.05, gap −2.6% → −17.3%** (the
  material one — NB-heavy; the discount makes the tool *more conservative on NB
  timing than Pareto*, opening a documented divergence where CAPT was a tight
  validator — a call, not a bug; position held BUY); **MPCC $2.27 → $2.02**
  (−9.4pp; test_mpcc_gsl baseline re-pinned); **FRO $24.40 → $24.08** (−1.1pp,
  negligible — its NBs deliver Apr'26-Q1'27). `reconcile --all`: 20 names, 0
  SANITY FAIL, 2 drift alerts (CAPT/MPCC) annotated with the methodology cause.
  286 tests green. Cohort `years_to_delivery` are estimates (CAPT from the
  Q1-release schedule; MPCC from the deck's ~qN hints) — refine at the Q2 reports.
- **2026-06-22 — BRUT (Bruton Ltd) onboarded as the 20th name + §9.6
  time-to-delivery newbuild discount resolved (BRUT-first).** Bruton =
  pure-play VLCC newbuild vehicle (Trøim/Magni; Koch 26% / Trøim 20% / float
  54%), Oslo Growth, 12 firm VLCC NB (0 on the water), deliveries Jul-2026 →
  Q3-2029. Real per-vessel fleet from bruton-ltd.com/fleet/; financials from the
  Pareto initiation 2026-04-22 (half-yearly reporter — H1-2026 due Aug-13
  confirms). **The build first hit SANITY=FAIL +116%**: the §3.1/§9.6
  delivered-less-commitment convention credited the full delivered-today VLCC
  mark ($175M) to ships arriving up to 3 years out — on a 100%-NB balance sheet
  the ~30% mark premium over Pareto's ~$143M/VLCC levered ~2.5x ("max torque").
  **Fix (owner-directed, resolves the long-open §9 #6):** `compute_nav` now
  PV-discounts a not-yet-delivered NB's delivered value by `1.11^(−years_to_delivery)`
  per vessel (`NEWBUILD_DELIVERY_DISCOUNT_RATE`; commitment kept at face); the
  strip terminal advances `years_to_delivery`. **Backward-compatible** —
  `years_to_delivery` defaults to 0 (on the water → factor 1.0), so the other 19
  names are byte-identical (286 tests green, all pins held). BRUT lands NAV $9.40
  vs Pareto $7.20 = **+30.6%, SANITY OK**, BUY (EV +97%). New manifest field +
  loader; schemas.Vessel.years_to_delivery; data_sources + NAME_ALIASES +
  earnings-calendar (Aug-13) wired; §15 partial (provisional 0%, fee/control
  pending the prospectus). **Mistake corrected mid-task:** I began unilaterally
  reverting BRUT on the +116% FAIL — Dan stopped me; a failed gate is a finding
  to surface, not a trigger to back out (memory saved). **ROLLOUT of the §9.6
  discount to the other newbuild books (CAPT/FRO/MPCC/GSL/CMDB) is a pending
  owner decision** — it moves their NAVs and needs re-validation.
- **2026-06-21 — automation-drift policy set + `commit_drift.sh` helper added
  (owner decision).** The recurring problem: launchd jobs write to TRACKED files
  (prices_daily, baltic CSV, sp_scan cursor + candidates, `_manifest.json`,
  preflight, FFA queue), so the working tree perpetually accumulates uncommitted
  drift. Decision (vs gitignoring them or cron auto-commit): **keep them tracked,
  flush via a manual one-step helper.** `scripts/commit_drift.sh` stages +
  commits exactly those 8 files when run; COMMIT-ONLY (push stays the deliberate
  human event); decision logs + per-name pipeline outputs excluded (committed
  deliberately with their annotations / driving input change). Documented in
  "How to run things." Rationale: preserves full history + owner control of
  every commit; no cron clutter; drift cleanup is now one command.
- **2026-06-21 — daily S&P scan wired into the RC-ingest job + ingest-lag
  diagnosis (NOT an ingest failure).** Symptom: the `sp_scan` cursor sat at
  2026-06-11 while dailies through 06-19 were on disk. Diagnosis: the daily
  07:00 RC ingest (`com.crude-tanker-fv.rocketchat-ingest` →
  `scripts/ingest_rocketchat_cron.sh`) is **healthy and current** — ran Jun-21
  07:00, downloaded the 06-18/06-19 dailies, cursors at pareto_research 06-19 /
  baltic 06-20; its 14 KB `state/rocketchat_ingest.err` is ~99% a cosmetic
  urllib3 `NotOpenSSLWarning` (LibreSSL) + one transient TLS-read retry. The
  real gap was **cadence**: dailies arrive DAILY but `sp_scan` only ran in the
  WEEKLY news-pull cron, so prints lagged up to a week. **Fix:** added an
  incremental `sp_scan` (local-only, cursor-based, idempotent — verified
  "nothing to scan" on a same-day re-run) to the daily ingest wrapper after the
  ingest step; the linked-report harvest + manifest stay weekly in
  `news_pull_cron.sh`. (My first instinct — reorder `fetch_links` before
  `sp_scan` — was WRONG: `fetch_links` downloads linked detail reports, not the
  dailies, which come from `ingest_rocketchat`.) Manual catch-up this session
  advanced the cursor 06-11 → 06-19 (+4 review candidates: VLCC ~$180m via FRO;
  LR2/LR1/MR 06-16 cluster). **SEPARATE open item:** the FFA-OCR staleness alarm
  (>7 days) is NOT an ingest problem — the ingest still SEES `ffa_drybulk`
  messages (last 06-19) but `ffa_ocr` hasn't PARSED a 3-panel grid in 9 days, so
  the single-source poster likely stopped posting the parseable grid (or changed
  format). Verify the channel content.
- **2026-06-21 — B6 §9.2 terminal-value multiple LOCKED at 1.0× (owner decision).**
  Closes the last open Week-5 item. Owner ratified the memo recommendation
  (`outputs/terminal_value_options_memo.md`): keep the q9 terminal at 1.0× ×
  aged-NAV — `w_earn` + the conservative transaction-anchored marks already carry
  the cycle view, the sweep flips are immaterial band-edge wiggles, and the
  alternatives are flawed (uniform 0.9× wrong at troughs; 1.1× = forbidden
  calibrate-to-broker). Cycle-conditional recorded as the designated successor,
  revisited only on an adoption trigger. No engine change (1.0× was production);
  now PINNED by `tests/test_dividend_strip.py::test_terminal_nav_multiple_locked_at_1x`
  (locked-weights idiom — changing it needs a deliberate memo + test edit).
  §9.2 item 2 marked *resolved*; memo DECISION block filled; dividend_strip.py
  constant comment updated. tests: +1 (the pin); full suite 283 passed (the two
  reconcile state-tests un-skip now that `state/last_run.json` is fresh).
- **2026-06-21 — DEVELOPMENT FREEZE LIFTED (owner decision).** The 2026-06-14
  freeze (which gated all feature/sector/methodology work on a crude-backtest
  "edge" verdict) is removed. Rationale: this is a forward-looking valuation aid
  for picking/valuing individual shipping names, not a cross-sectional quant
  portfolio, so a cross-sectional IC backtest is not the right gate — and the
  backtest's null is an expected small-sample result, not a refutation of the
  per-name work. The freeze DECISION RECORD at the top of CLAUDE.md was replaced
  with a forward-looking project-stance note; PLAN.md was rewritten from a
  backtest-gate plan into the live forward plan (Week-5 hardening status + active
  backlog), with the backtest demoted to a reference section. The `backtest/`
  artefacts (PRE_REGISTRATION.md, REPORT.md) are retained as a recorded
  diagnostic — accurate history, no longer a gate. (Unrelated uses of "frozen"
  for stale data archives/vintages — container feed, MB anchor — are untouched;
  they mean a stale feed, not the dev freeze.)
- **2026-06-21 (Week 5) — B6 §9.2 terminal-value options memo WRITTEN (owner
  decision pending).** Re-ran the terminal-NAV-multiple sweep over the full
  19-name watchlist (`scripts/terminal_value_sensitivity.py`; was 12 names at
  the Jun-5 first run) → 7 band-edge flippers (0.9× turns peak names DHT/ECO
  more bearish; 1.1× turns ASC/SBLK→HOLD + GNK→BUY [deal-pinned, discount];
  12/19 never flip; CCEC most sensitive but holds BUY). Wrote
  `outputs/terminal_value_options_memo.md`: four options (1.0× / 0.9× / 1.1× /
  cycle-conditional), each steelmanned by an independent agent panel, with an
  empty owner DECISION block. **Recommendation: ratify 1.0× now** (auditable;
  marks already conservative; `w_earn` already down-weights the strip at peak —
  the at-stake flips are immaterial band-edge wiggles), **cycle-conditional as
  the designated successor** pending two adoption triggers (empirically-sized
  embedded-mark error, or the book gaining trough-band names); **reject uniform
  0.9×** (wrong sign at troughs — dominated by cycle-conditional) **and 1.1×**
  (its broker-gap justification is the forbidden "calibrate to broker" move,
  §6/§9). Key mechanism point: the terminal = current marks aged forward (never
  re-priced), so the multiple sets the *embedded asset-price level* — orthogonal
  to `w_earn`, which only weights the leg; §15's `governance_discount_pct` is the
  architectural precedent for a multiplier at this layer. No engine change (rec
  is status-quo); `TERMINAL_NAV_MULTIPLE` stays 1.0. §9.2 item 2 + PLAN.md B6
  updated to point at the memo. Was a parked Week-5 item; resumed at owner
  direction.
- **2026-06-21 (Week 5) — B5 anchor-basis commensurability SHIPPED** (commit
  5fc3b7d). Cycle-position anchors carry three non-composable bases (a cycle
  ratio is forward-12M-TC / anchor): `tc_10yr_mean` (crude/product/lng),
  `archive_22mo_median` (dry_bulk), `fy_calendar_avg` (containerships). Every
  `cycle_anchors` block in `scenario_inputs.yaml` now declares an `anchor_basis`
  enum (12 added; containerships' 3 prose tags normalized). Shared helpers in
  `scenarios.py` (`all_sector_anchor_bases` / `detect_mixed_anchor_basis` /
  `format_mixed_anchor_basis` / `ANCHOR_BASIS_LABELS`) drive a **MIXED-ANCHOR-
  BASIS** flag on the two cross-sector surfaces: the delta-report table
  footnote and the `reconcile --all` footer (per-name basis shown in
  `--verbose`); `--sector` / single-name runs use one basis so never flag.
  METHODOLOGY §10 gains the three-basis subsection. Metadata + diagnostics
  ONLY — the engine reads just `ten_year_mean`, ignores the new key, so the
  valuation core is untouched (FV-band + cycle/blend pins unchanged). Tests
  +5 (3 scenarios, 2 delta) → 280 passed, 2 skipped. The B5 commit was kept
  to the 7 source/doc/yaml/test files; the verification pipeline run's
  regenerated outputs + routine decision-log stubs were reverted (they
  regenerate on the next real refresh). Was a parked Week-5 item; resumed at
  owner direction with the freeze set aside.
- **2026-06-12 (Week 5) — MB Weekly 24 prints PROMOTED (owner decision,
  7 prints recategorized per owner review) + drift loop run.** Fit
  inputs: **Seamusic** (Aframax age-17 $52.5M, in-window WITH
  premium-channel note — buyer screen: undisclosed buyer + immediate
  rename to VIRTUS MARIS + no ice notation = NOT confirmed-clean;
  single-print drift GATE passed: 5yr −3.6%/10yr +0.1%/slope negative,
  no flip on the print alone; REVISIT if no second clean corroborating
  print by Q3), Vulcania (Pana n=4→5, TC-ATTACHED caveat — residual
  could be entirely the charter), Ausone + Santa Rita (Supra-Ultra,
  curve-bracketing pair). Documentation-only (owner recategorization —
  original note overstated): Proteas (age 21 — old-age-leg validation
  DEAD-ON, the Picardy/Predator pattern; NOT fit thickening), White Bay
  (age 22), Shanhaiguan (age 0 NB; Dalian print on a Korean-spec anchor
  = conservative-to-fair, not validated-exactly). Drift loop: ONE flip
  — SBLK TRIM/SHORT→HOLD (+1.1% NAV; Pana fit +6.9/+3.0 → +11.5/+7.5;
  band-edge third oscillation, leans on the TC-attached print — sblk_log
  annotated, no size action). Ethanol/corn driver re-routed from
  demand-destruction overlay to dry-bulk scenario tree
  (framework_breakers entry — sector-structural ≠ macro recession).
  Tests 277 green, no re-pins. Fit counts: Aframax 13 / Pana 5 /
  Supra-Ultra 22.
- **2026-06-12 (Week 5) — MB weeklies first direct delivery: ingest route
  built + three-sector once-over run (review-only, nothing promoted).**
  Container/Dry Bulk/Tanker Weekly 24 archived to `inputs/research_mb/`
  (LNG not delivered — verify subscription); route = Gmail link harvest →
  fetch_pdf.py (cdn.flxml.eu added to data_sources.yaml
  `mb_shipbrokers_weeklies`). Findings in
  `outputs/mb_weekly_check_2026-06-12.md`: (1) container — frozen 10
  weeks hid a feeder rally (+13.4%, position 0.98x→1.12x; MBCI +13.9%;
  intermediate/large drift normal; marks layer current; MPCC most
  exposed) → owner-gated `twelve_month_tc.yaml` container refresh queued;
  (2) tanker — MB 5yr assessments land 5/6 classes inside
  TXN_PURE_PLAY_K_BAND over our txn marks (first INDEPENDENT
  confirmation of the B4 band semantics), but crude NB anchors read
  14-35% above MB Korea NB with a 5yr>NB prompt inversion (review item);
  Hormuz trigger NOT met (draft memo, 30-day window, conditions — the
  closest signal yet); (3) dry bulk — txn marks validated by MB's own
  prints (Proteas $12.10M dead-on the age-21 Pana curve), Supra
  assessment gap = basis not error, **Pana anchor flagged structurally
  LOW** (MB 5yr tenor never below ~16k vs anchor 11.9k — Q3 refinement +
  B5 xref). 7 promotable print candidates queued (Seamusic Aframax
  $52.5M ~65% above fit; Shanhaiguan NB resale $90M; Vulcania/Proteas
  Pana; 3 Supra-Ultra) — promotion human-only, each triggers the
  prints→rerun→drift loop.
- **2026-06-12 (Week 5, Session A) — B4 shipped: mark-driven classification
  restated to post-flip k_broker semantics + fetch_links argparse fix.**
  Two-regime definition landed in METHODOLOGY §9 item 9: txn-anchored
  sectors (crude/product/dry bulk) — mark-validated = k_broker inside the
  uniform pure-play band `TXN_PURE_PLAY_K_BAND = (1.05, 1.25)` (constants
  in `marks.py`, uniformity < 0.05; DHT/ECO/FRO 1.12-1.14 at the Jun-2026
  fit, ~+13-17pp spread EXPECTED); mark-driven = outside the band either
  side. Un-anchored sectors (LNG/containerships) keep the original ≈1.0
  reading. Broker-sweep Read column relabeled MECHANICAL
  (`wide-spread`/`narrow-spread`, owner decision) — it had been printing
  the canonical validators DHT/ECO/FRO as "mark-driven" at their expected
  band premium; §6 prose is the canonical classification. Dated
  restatements appended to §6 INSW/TNK/ASC/STNG/HAFN/SBLK, §7.5, §9
  item 10, §15.2; LIMITATIONS §1 definition updated. No mark changes —
  pipeline re-run diff was text-only, delta 0 material, reconcile 19/19.
  fetch_links: zero-option argparse front door (`--help` exits 0
  pre-network, unknown flags exit 2 — closes the Week-4 §5 observation);
  no-arg cron path unchanged. tests: 274 → 277.
- **2026-06-12 (post-Week-4-close) — brokerage MCP decision REVISED:
  keep the IBKR connector attached, DENY it in Claude Code.** The
  Week 4 owner action ("detach entirely") is superseded: the connector
  feeds a weekly Cowork portfolio routine + ad-hoc Chat discussion, and
  claude.ai connectors are account-level all-or-nothing (no per-surface
  Chat/Cowork/Code scoping exists; Code's `deniedMcpServers` doesn't
  match cloud-synced connectors). DENY rules on the synced server id
  (`mcp__8de167eb-dbd9-4178-b52a-a756c1f27b24`) added to
  `~/.claude/settings.json` (machine-wide) AND the tracked
  `.claude/settings.json`. Deny, not ask — the §5 red-team proved
  autonomous sessions auto-approve ask-tier. Verified live same
  session: read-only `get_account_summary` probe refused at the
  permission layer (deny rules hot-reload mid-session). CAVEAT: if
  IBKR is disconnected/reconnected at claude.ai, the UUID may change
  and the deny goes silently stale — re-check the id in a fresh
  session's tool list. Full rationale: PERMISSIONS_PROPOSAL.md §6.4
  revision note. Same session: `settings.local.json` pruned 262 → 38
  allow entries (arbitrary-write/interpreter/credential-exposing
  allows, ffmpeg-era strays, ask-tier-bypassing curl/launchctl
  carve-outs, tracked-allowlist duplicates, stale one-offs).
- **2026-06-12 (Week 4, Step 3 — WEEK 4 CLOSED)** — Week-close checklist
  run. **§5 red-team pass (first session with the allowlist active):
  DENY rules ENFORCE** (env-file Read refused, `rm -rf` refused);
  allow-tier friction-free (pytest, reordered-flag sp_scan, outputs
  edit, sec.gov WebFetch — probes 7-10 clean); **ASK tier NOT testable
  in an autonomous session** — the autonomous permission mode
  auto-approves ask-class calls (curl with no matching rule executed;
  watchlist Edit applied + immediately reverted; fetch_links ran), so
  the prompt half of §5 carries to Week 5 as an INTERACTIVE-session
  item. Real finding, fixed: `Bash(git push *)` had accumulated in
  `.claude/settings.local.json` as a blanket allow — it defeated the
  tracked ask-on-push policy in EVERY session, not just this one —
  pruned. Two new leak observations recorded: `git -C <path> push`
  dodges the `git push` prefix matcher (the -C variant of the
  flag-reorder leak), and fetch_links ignores unknown flags (`--help`
  ran a real pass; dedupe held, 0 downloads — argparse fix queued
  Week 5). **Verification gate: 274 passed; pipeline clean (0 material,
  0 input changes); `/reconcile --all` 19/19, 0 SANITY FAIL, 0 drift
  alerts.** Documentation audit (two read-only agents, fixes applied in
  main session): README 17→19 names / 4→5 sectors / 243→274 tests +
  containerships watchlist table + METHODOLOGY line count ~720→~2,900;
  METHODOLOGY §1 coverage header 19/5, stale "Week 4 candidate" lines
  closed, **§11.8.6.4 horizon header corrected "12 quarters"→"10 strip
  quarters"** (body and Appendix A already said 10; owner ratification
  of the A1 interpretation still pending); LIMITATIONS gains the
  containerships-CLOSED sector entry, the §11.8.5 stale-vintage +
  old-age-tilt OPEN limitation, the APPROX consensus_pnav list
  completed to all SEVEN names with actual bases (audit agent's
  suggested values were wrong — re-verified against watchlist.yaml
  before applying), §15 declined list completed
  (TNK/CCEC/CAPT/MPCC/GSL), validator list extended to all 5 sectors.
  Quick-ref preamble gains the vintage-prices note (quick-ref prices
  are note-vintage, not live — stop "fixing" them). PLAN.md rewritten
  for Week 5 (B4/B5/B6 + Q2 carry-forwards per owner direction).
  OWNER ACTIONS re-flagged: brokerage MCP connector was STILL attached
  in this session (order-writing surfaces reachable); A1 horizon
  ratification.
- **2026-06-12 (Week 4, Step 2 + maintenance)** — **CONTAINERSHIPS SHIPPED:
  engine (per-sector `strip_horizon` + `coverage_schedule`, zero-drift
  verified on all 17 prior names), Container Set A wiring (A2 class
  signatures, A3 TEU-weighted intermediate $43,400/$33,700 applied at
  onboarding), MPCC + GSL onboarded (19 names, SANITY 0 FAIL, both
  n/a-APPROX), §15.7 screens both DECLINED (GSL = the dimension-6
  charter-affiliation founding pass: CMA CGM equity zero since 2022,
  13/71 vessels), calibration lock recorded N/A-by-construction
  (machine-confirmed; primary substitute = MPCC's 3 disclosed sale
  prints — tool old-age marks 0-33% BELOW realized, conservative by
  design).** Maintenance landed: B1 overlay ledger (§16, 11 active
  rows), B2 §14.4 double-count warning, B3 all 10 weight-skips
  re-pinned (DHT wnav-vs-base direction REVERSED under Jun-9 weights).
  SESSION-LOG NOTES: (a) A1 horizon — owner brief said "~12q from
  report date"; under the repo's q3_2026 strip-start convention,
  end-2028 = **10 strip quarters** — wired as 10, flagged for owner
  review; (b) MPCC cohort AGES and NB delivery quarters are ESTIMATES
  (deck discloses no built years) — refine at Q2 (2026-08-26); (c) GSL
  analyst_target/consensus_pnav are book-based placeholders (CMDB
  convention) — replace if VIE coverage surfaces; (d) PR #2 reviewed +
  worktree-verified, MERGED by owner same day (entry below); changelog
  conflict resolved additively at integration. Tests 243 → 274. Full
  detail: METHODOLOGY Appendix A 2026-06-12.
- **2026-06-11 (Week 4, Step 1)** — **§11.8 containerships methodology
  decision doc LOCKED** (time-boxed one session, doc before code, dry-bulk
  §11.7 as template). Decisions: 3-class collapse (ctr_feeder ≤2,000 /
  ctr_intermediate 2,000-5,500 / ctr_large >5,500, WB variants excluded
  from class averages); **charter-book convention = coverage-schedule
  generalization of the §3.2 blend** (strip earns disclosed contracted
  rates through expiry via per-quarter cov_q, re-fixes at scenario rates;
  NAV stays on-curve at bare marks; charter premium/discount = v1
  limitation), NOT §11.6 off-curve; Container Set A scenarios
  0.25/0.40/0.20/0.15 (disruption_persists / gradual_normalization /
  normalization_plus_overhang / demand_recession); cycle anchors from the
  weekly's FY21-25 table NOT the boom-only 19-month archive median
  (feeder $20,850 / intermediate $32,300 / large $41,000 → positions
  0.98x/1.30x/1.53x at the Apr-01 vintage); **external anchor: NONE —
  all-APPROX sector** (verified: Pareto's own liner table dashes MPCC's
  P/NAV; they value the space on EV/EBITDA) → v1 calibration lock
  recorded N/A-by-construction with VIE + marks-consistency substitutes;
  validators MPCC + **GSL** (DAC deferred — Capesize hybrid, same logic
  as CMRE). Empirical basis: mechanical extraction of all four data
  tables across the 42-issue MB archive (40-42/42 parse rate). Key
  fresh source found on disk: Pareto MPCC quarterly review 2026-05-28
  (HOLD, TP NOK 25, 99/69/41% of 26/27/28 days fixed, $2bn backlog).
- **2026-06-12 — Permission allowlist shipped (`.claude/settings.json`,
  tracked) + fetch_links module split + fetch_pdf.py wrapper.** Full
  rationale in `PERMISSIONS_PROPOSAL.md` (decision record). Narrow
  allows for the constant loop (pytest/reconcile/pipeline/refresh/
  sp_scan/price_refresh, git add/commit, WebFetch to the
  data_sources.yaml host set); ask on git push, fetch_links,
  ingest_rocketchat, curl, launchctl, and the three human-only
  promotion surfaces (watchlist vintage / transactions / FFA curve —
  the TEN-$44 and promotion rules turned mechanical); deny on
  credential-shaped reads. Two structural changes: `--fetch-links`
  moved out of sp_scan into `crude_tanker_fv.fetch_links` (Bash rules
  are prefix matchers — a network flag on an allowed module leaks when
  flags are reordered, so the boundary is now a module boundary;
  news_pull_cron.sh updated), and `scripts/fetch_pdf.py` replaces the
  ad-hoc curl pattern (host-validated against data_sources.yaml in
  code; carries the single audited Okeanis TLS exception). Brokerage
  MCP decision: detach from Claude Code entirely (owner action),
  not deny-rules. New "What NOT to do" rule on widening the allowlist.
  *(Ordering note: this entry lands between Step 1 and Step 2 of Week 4
  chronologically; merged after Step 2 completed — see the entry above.)*
- **2026-06-11 (post-close) — TEN June-5 data-kit reconcile (user-supplied
  PDF; tenn.gr blocks agent fetching).** Found + fixed a Q1 manifest
  omission: Dr Irene Tsakos + Silia T (2025-built conventional Suezmaxes)
  were never entered — the onboarding plan's "14 conventional Suezmax"
  slip; fleet_summary claimed 60 on-curve over 58 rows. NAV/sh $80.79 →
  $88.13 (+9.1%), gap to APPROX broker −26.0% → −19.3%, BUY unchanged.
  Q2-vintage kit deltas (Ulysses sale confirmed — no gross price, not
  promotable; Sola TS step-up; Dimitris P spot→TC $40k; Alaska/Archangel
  to spot-indexed TC) documented in ten_log for the September H1 refresh,
  NOT applied to the Mar-31 snapshot. New cross-foot guard test
  (test_validate.py) + gotcha rule. tests: 244 passed.
- **2026-06-11 (WEEK 3 CLOSED)** — **first Week-close checklist run
  (checklist itself codified this session, owner decision).**
  Documentation audit via two read-only agents, fixes applied:
  METHODOLOGY line-46 monster paragraph → dated scope-change log;
  coverage header 8→17 names/4 sectors; preferred_equity comment
  (TEN is the user, not "none"); STNG §6 mark-validated→mark-driven
  with date-stamps; INSW version-label footnote; §6 entries ADDED for
  CMDB + CAPT; FFA-OCR saga moved OUT of §11.7.7 "NOT in v1" into new
  §11.7.8 (onboarding table → §11.7.9); Appendix A entries added for
  2026-06-10 + 2026-06-11 (closing the §15.7 dangling promise).
  README: status 2026-06-11, 17 names/4 sectors/243 tests, dry-bulk +
  CAPT/HAFN/TRMD watchlist tables, DP2/dry-bulk scope line corrected.
  LIMITATIONS: dry-bulk greenfield marked CLOSED, §15 names updated
  (TEN+CMDB cases; TNK/CCEC screened-declined), mark-driven snapshot
  marked as vintage with pointer to the live sweep. CLAUDE.md
  quick-refs reconciled (INSW k 1.52+, SBLK HOLD); earnings-calendar
  maintenance line added; stale "(Coming end of Week 0)" removed.
  Verification gate: 243 passed/10 skipped; `/reconcile --all` 17/17
  SANITY OK, 0 drift alerts; refresh checklist regenerated 17/17.
  **PLAN.md created** (the rolling sprint-plan/handoff doc — Week 4 =
  containers; Step 0 flags the Container Weekly feed stale since
  Apr-01). Week 3 final tally: news-pull v1, daily price refresh +
  TEN fix, FFA-OCR Stage 1 + market-consistency diagnostic, earnings
  readiness, CAPT (17th name), §15.7 + full-book retro screen,
  Week-close checklist.
- **2026-06-11 (Week 3, day 2, Part 4)** — **§15.7 screening procedure
  FORMALISED + full-book retro screen run (owner-approved).** New
  METHODOLOGY §15.7: cheap gate (multi-year median P/NAV ≥0.85 → N/A),
  structured screen below it (control/share structure, related-party
  fee load %GAV/yr, distribution behaviour, natural-experiment comp,
  external anchor), the evidence-vs-mechanism doctrine (haircuts price
  EVIDENCE; mechanism → tripwires), two quantitative calibration
  anchors (capitalized fee drag; external-anchor implied discount),
  mandatory recording per name + onboarding step 4. Retro outcomes,
  all 17: 9 gated N/A (DHT ECO FRO FLNG INSW HAFN NAT-§12 ASC GNK);
  3 Step-1 declines (STNG TRMD SBLK — open payout/buyback channels, §6
  mark-driven discounts); 2 full-screen declines with tripwires —
  **TNK 0%** (dual-class 54.9%-votes-on-30.8%-economics BUT fee leakage
  internalized Dec-24, $6.00/sh specials since mid-23; TK-combination
  tripwire) and **CCEC 0%, closest call** (float ~13%, sponsor-paid
  exec comp, fiduciary waiver, ~24% payout vs CAPT-like 0.4%-of-GAV
  fees, real conflicts committee, 76-quarter dividend record;
  payout-path + CAPT↔CCEC cross-dealing tripwires; 10% alternative
  documented — owner call). **Haircut recalibrations: TEN HOLD 30%**
  (band 30-36; VIE-implied drifted to 36.3% but the payout raise argues
  down; TCM fee anchor due at Q2) and **CMDB HOLD 30%, RE-GROUNDED** —
  capitalized fee drag ($28M/yr ÷ 10-12%) = 30-36% of the $779M equity
  NAV, landing on the haircut independently of TEN-equivalence.
- **2026-06-11 (Week 3, day 2, Part 3)** — **CAPT onboarded (17th name,
  Week 3 stretch goal) — first Oslo/NOK listing.** Assembled entirely
  from the linked-report harvest (Pareto initiation Apr-19 + Q1 review
  May-27, both already on disk) — zero new fetching for data assembly;
  issuer-report confirmation deferred to the Q2 refresh. 30 firm
  vessels (12 VLCC / 10 Suez / 4 Afra / 4 LR2-crude-routed), 9 on-water
  at Mar-31, 21 NBs at delivered-market-less-$1,880M-commitment with a
  Pareto-waypoint fleet_schedule ramp (11 Apr-26 → 17 Nov-26 → 24 YE-27
  → 30 mid-28); 13 options at cost excluded. NOK handling: watchlist in
  USD (NOK 116.2 / 9.5221 = $12.20, Jun-10 vintage incl. pnav 0.67 +
  P/E 11.1 from the same daily); price_refresh gains `yahoo_symbol` +
  `quote_currency` fields (CAPT.OL + NOK=X conversion — bare "CAPT" is
  Captivision). NAME_ALIASES + data_sources + earnings calendar
  entries added; 23-mention Pareto sweep distilled. **First reconcile:
  −2.6% gap on a real Pareto print, SANITY OK, k_broker 1.04 — the
  tightest onboarding baseline on record; BUY EV +38.8%.** §15
  considered + declined (documented in the balance sheet + log).
  tests: 243 passed, 10 skipped.
- **2026-06-11 (Week 3, day 2, Part 2)** — **Q2 earnings-readiness pass.**
  `inputs/earnings_calendar.yaml` built for all 16 names (web-swept +
  cadence-verified: 5 calendar-confirmed — ECO Aug-4, SBLK Aug-5,
  TRMD Aug-26, HAFN+FLNG Aug-28; 11 expected windows; TEN is a
  SEPTEMBER H1 reporter). Preflight gains §0 earnings check
  (`refresh.check_earnings_calendar`): 🔴 REFRESH DUE when a report
  window opens with no target-quarter balance sheet, 🟡 within 14 days.
  Report-day refresh runbook added to CLAUDE.md (7 steps incl. the
  issuer-report S&P sweep — Appendix A backlog CLOSED — and the
  vintage-rebase rule). Season shape: early cluster Jul-28→Aug-6
  (STNG/ASC/TNK/CCEC/ECO/GNK/INSW/DHT/SBLK/CMDB), late cluster
  Aug-20→31 (FLNG/FRO/NAT/TRMD/HAFN), TEN mid-Sep. tests: 238 passed.
- **2026-06-11 (Week 3, day 2)** — **FFA-OCR Stage 1 SHIPPED** (the
  Week 3 centerpiece; owner-approved re-scope, no longer trigger-gated).
  `ffa_ocr.py`: classifier (Cape + Cal2\d + "Produc* Price Change"
  signature) + TSV-positional parser (x-band panel assignment, per-row
  tenor majority vote, conf≥60 gate, trailing-only punct strip) +
  sanity model + review queue (`outputs/ffa_ocr_queue.md`) + incremental
  cursor + `--staleness` alarm, wired as the new tail of the weekly
  news-pull chain. Key empirics: the widget posts EVERY business day
  (45/46 days Apr-1→Jun-11; the ~7% archive-wide rate was format-era
  dilution); recipe = grayscale → 4× LANCZOS → psm 6 (color drops the
  headers; tesseract can't read /tmp in the sandbox — scratch lives in
  `state/ffa_scratch/`); DISCOVERED tick model — months/Cal tick $12.5
  truncated, Q tenors display the unrounded 3-month average (31766 =
  95300/3 is real, not noise). 29/45 days fully clean, 16 flagged
  (incomplete grids only; the parser refuses to guess on mangled
  tokens like "(3800"). Promotion to `ffa_forward_curve.yaml` is
  human-only; strip integration is diagnostic-first pending one review
  cycle. Stage 2 (2020-2026 backfill) open. tests: 233 passed.
- **2026-06-10 (night, Week 3 opener, Part 2)** — **first `/news-pull` run
  + TEN price-input error fixed + daily price refresh BUILT.** The
  inaugural digest (`outputs/news_digest_2026-06-10.md`, 4 agents / 16
  names) caught: TEN watchlist price $44.00 was an input ERROR (6-K prose
  "~$44" typed as a live price; actual $36-37.5 all week) — fixed to
  $37.14 with `consensus_pnav` REBASED 0.40→0.34 to preserve the implied
  broker NAV anchor (~$110) and `consensus_fwd_pe` 5.5→4.6 (drift +0.5pp,
  stable; BUY strengthens, EV +30.9%→+55.1%); an unrecorded Pareto stance
  change INSW BUY→HOLD 2026-05-18 (TP raised $84→$88, valuation-driven —
  confirmed verbatim in the archived daily, annotated); GNK deal risk
  front-loaded to the Jun-18 AGM (all 3 proxy advisors back Genco, Diana
  withdrew 4/6 nominees + floated dropping the tender, 38 shares
  tendered); STNG 4×LR2 $285.8M EN-BLOC (documented-not-promoted, watch
  Q2 6-K for splits); CMDB Astros bounded ~$22.8M (inference — NOT
  promotable). **Process fix shipped same session: daily price refresh**
  — `price_refresh.py` fetches all watchlist closes (Yahoo chart API)
  into automation-writable `prices_daily.yaml` with sanity flags (>15%
  day move / >30% vs static, flagged = never applied); launchd
  `com.crude-tanker-fv.price-refresh` daily 18:30; pipeline CLI passes
  `live_prices=True` (tests keep deterministic statics by default).
  VINTAGE RULE: broker NAV (reconcile) + consensus EPS keep the
  watchlist-static `as_of_price` — Pareto ratios pair with Pareto-vintage
  prices; only EV/position reads live. SBLK TRIM/SHORT→HOLD on the
  live-price introduction (band-edge wiggle, annotated). tests: 220
  passed, 10 skipped.
- **2026-06-10 (night, Week 3 opener)** — **periodic news pull v1 BUILT**
  (registered backlog, owner spec + 4 vetting amendments, one session as
  time-boxed). Mechanical half: `scripts/news_pull_cron.sh` + launchd
  plist `com.crude-tanker-fv.news-pull` (Saturdays 08:00, after the
  07:00 daily RC ingest per amendment 2), chaining RC ingest → `sp_scan`
  → `--links` → `--fetch-links` → `pareto_archive --build-manifest`,
  PYTHONUNBUFFERED + per-step banners + exit-code echo per the silent-
  death gotcha. Agent half: `/news-pull` command — web-sweep weighted to
  APPROX (read from `reconcile.APPROX_PNAV_TICKERS`, not hardcoded) +
  live-event names (detected from decision logs), digest at
  `outputs/news_digest_YYYY-MM-DD.md` with promotable-candidate (built-
  year + en-bloc-split fields, amendment 4) / stance-change / live-deal /
  stale-price (APPROX fresher-price-only, amendment 3) / no-action
  sections + drift-loop reminder. Never writes pipeline-loaded YAMLs
  (amendment 1). Dry-run clean end-to-end (cursor Jun-08 → Jun-10).
- **2026-06-06** — file created. Verification-loop, three-jobs
  reconciliation framework, "what this tool is, philosophically" section,
  gotcha list, per-ticker quick-refs all promoted from session memory +
  decision logs.
- **2026-06-09** — added secrets-discipline rule to "What NOT to do" after
  a `rocketchat_token.rtf` was dropped at repo root during Rocket.Chat
  ingest setup. Caught untracked but not gitignored. Defensive `.gitignore`
  patterns added (`*_token*`, `*_credentials*`, `*_secret*`, `*.rtf`, `.env*`).
- **2026-06-09 (evening Part 2)** — dry-bulk classes added to the
  transaction-anchored pipeline. Cape (24 prints) / Pana (6) / Supra-Ultra
  (18) YAMLs landed at `inputs/market_data/transactions/`. Sources are
  the Pareto Shipping Daily archive 2025-01→2026-06 plus the SBLK Q1 2026
  6-K Stonington print. SBLK gap moved −21.7% → −21.1% post-fit, locking
  it in the §6 mark-driven taxonomy (k_broker 1.27). Per-ticker quick-ref
  for SBLK + the §9.9 scope-discipline line updated. tests: 192 passed.
- **2026-06-09 (late evening Part 3)** — tanker classes swept from the same
  Pareto archive: VLCC/Suezmax/Aframax/MR samples expanded, LR2 graduates
  to own-fit (proxy retired). Tanker 10yr anchors were running HOT — VLCC
  fit −18% at both legs; 5 names flip under txn-anchored marks
  (DHT/ECO/FRO→TRIM-or-HOLD-down, TNK BUY→HOLD, TRMD HOLD→TRIM). Toggle
  still opt-in; default-on is an OPEN owner decision. `sp_scan.py` +
  `_scan_state.json` added for incremental future scans (191-candidate
  review queue archived at `outputs/sp_print_candidates.md`). One locked
  test expectation reversed with rationale (Suezmax fit direction — thin-
  sample artifact). Affected decision logs annotated (9 names). tests:
  198 passed. Backlogs registered in METHODOLOGY Appendix A: exogenous
  demand-destruction overlay, issuer-report S&P sweep at refresh, GNK
  onboarding, §6 SBLK promotion, Pana print disambiguation.
- **2026-06-09 (late evening Part 4)** — **txn-anchored marks made the
  pipeline DEFAULT** (owner decision; Sinokor's bid IS the VLCC market).
  Defaults flipped in `value_company` / `run_scenarios_watchlist` /
  `run_broker_sweep` (sweep now recalibrates its "tool" endpoint too).
  Headline re-base: DHT BUY→TRIM/SHORT $14.31, ECO/FRO →TRIM/SHORT,
  TNK BUY→HOLD, TRMD →TRIM/SHORT; FLNG/CCEC untouched. k_broker semantics
  now "broker premium over transaction levels" — uniform 1.12-1.14 on
  crude pure-plays. vlcc.yaml Sinokor exclusion re-grounded on
  data-quality only (no per-vessel split). FV-band + sweep tests re-based.
  Drift flags on this run are the re-base, not market moves — 9 logs
  annotated. tests: 198 passed.
- **2026-06-10 (later still)** — **Pareto linked-report harvest: 220
  detail reports pulled from the dailies' hyperlink annotations.** User
  tip: the dailies embed links to Pareto's full research. pypdf
  `extract_text()` is blind to /Annots — every prior sweep missed them.
  240 of 351 dailies carry links → 267 unique tracked-download URLs
  (FactSet/BlueMatrix, public, long-lived tokens; 100 arrived
  Proofpoint-wrapped and are unwrapped offline). Downloaded 220 new
  reports (47 already archived), 0 failures; 217 classify as
  company_report incl. ~70 on watchlist names (full NAV breakdowns /
  estimates). `sp_scan --links` + `--fetch-links` codified with
  inventory + report_id dedupe (no re-fetching on re-runs);
  `outputs/pareto_daily_links.json` committed. The "Capital Tankers"
  reports in the set are CAPT (Oslo-listed crude newbuild player,
  initiated by Pareto Apr-2026, BUY TP NOK 180 at 0.75-0.84x NAV) — a
  DIFFERENT entity from CCEC, whose no-coverage APPROX status stands.
  CAPT noted as a future onboarding candidate (Pareto-covered pure
  crude, deepest crude NAV discount). tests: 207 passed.
- **2026-06-10 (later)** — **Pareto free-text name-sweep added to the
  process + run retroactively for all 15 names.** `sp_scan.py --names`
  mode (alias-aware: OET=ECO, HAFNI=HAFN, TORM=TRMD, Tsakos=TEN;
  share-price-table noise filtered). 15 review files at
  `outputs/pareto_mentions_<ticker>.md`; distilled entries in every
  decision log. Findings: inputs validated (NAT NB commitments + ASC
  payout-doubling already captured); 1 missed print promoted (TEN Mar-25
  Suezmax $40M — fit moved <0.5pp, under drift gate); Pareto stance
  changes recorded (FLNG→SELL 2026-05-27, OET+FRO→HOLD 2026-05-26,
  INSW→BUY 2026-01-21); consensus_pnav plumbing confirmed by exact
  matches (TRMD stated $34 vs implied $33.98; INSW $80 vs $79.59; SBLK
  $33 vs $33.17). Mention-count distribution empirically confirms the
  APPROX taxonomy (CCEC 0, NAT 4, TEN 5, ASC 6 — "We don't cover ASC"
  verbatim — vs covered names 34-96). Onboarding workflow updated with
  the sweep as step 3; quarterly-refresh habit noted. tests: 205 passed.
- **2026-06-10 (evening)** — **CMDB onboarded (16th name, third dry-bulk
  validator) — Week 2 dry-bulk sequence CLOSED.** APPROX-anchored (zero
  Pareto/VIE coverage; P/BV 0.62 proxies P/NAV on spinoff fair-value
  book). 29 owned at Mar-31 (Clara/Miracle sold Q1; Astros closed Q2);
  CBI chartered-in platform excluded as P&L-only. Tool NAV $32.23 =
  +15.8% over book; 0.54× price/NAV, EV +64% — **flagged §15 candidate
  (related-party fees / no payout / family control), haircut decision
  with owner before the signal is actionable.** CMDB added to
  `APPROX_PNAV_TICKERS` (was missing — briefly mis-entered the lock
  denominator as 1/3; corrected to 1/2 excluded-APPROX same session).
  No promotable prints (Clara+Miracle aggregate gain only — no per-vessel
  prices; no-back-solve). §11.7.8 table marked DONE throughout.
  tests: 210 passed. **Same evening: §15 haircut set at 30% (owner
  decision, TEN-equivalent) — PW FV $28.32 → $19.82, EV +64% → +14.9%
  mild BUY; asset NAV untouched; §15.3 second-case entry added.**
- **2026-06-10** — **GNK onboarded** (15th name, second dry-bulk validator)
  from the Q1 2026 10-Q. k_broker 1.04 / gap −5.2% — VALIDATES the
  transaction-anchored dry-bulk curves on a no-Pana fleet; isolates SBLK's
  −21% as name-specific. v1 dry-bulk calibration lock recorded as 1/2
  (50%) FAIL-with-explanation (SBLK = documented §6 mark-driven miss; no
  tuning per the back-solve rule); revisit at Q3 with the ≥80%/±5% bar.
  6 prints harvested at onboarding (2× GNK nmax $72.75M + Courageous
  $63.55M + Maran SWS cape $30M in-window; Picardy/Predator $10.6M
  documentation) — Cape fit n 21→25, +16.0%/+12.7%; SBLK moved −0.1%
  (under drift gate). Diana tender deal overlay documented in
  decisions/gnk_log.md + watchlist comment — GNK price is tender-pinned
  until Jun-26. tests: 201 passed.
