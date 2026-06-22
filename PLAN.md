# PLAN.md — active plan / sprint handoff

A new agent reads CLAUDE.md, then this file, then starts. This is a
**forward-looking valuation aid** for shipping equities (independent NAV +
forward dividend strip, blended by cycle position), judged by the soundness of
its per-name reads — not by a cross-sectional backtest. Development proceeds
normally (the 2026-06-14 "development freeze" was lifted 2026-06-21).

**Current state (2026-06-22):** 20 watchlist names across 5 sectors; **308 tests
green**; `reconcile --all` 20/20 SANITY OK (0 fail, 0 drift); committed drift gate
ratified (Phase 2 below). This session ran a **methodology-soundness sprint** (full
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
- **Phase 3 — ex-post validation (Option C).** (a) **Value-premium proxy test**
  (recommended first — powered, data cached): `backtest/loaders_sharadar.py`
  reading factor-portfolio's `~/Projects/factor-portfolio` (branch
  `v2-validation-first`) Sharadar cache via its `SharadarProvider`
  (`fundamental_at`/`price_at`, no-look-ahead via `datekey`; key in
  `~/.config/factor-portfolio.env`) + `backtest/run_proxy_powered.py`; reuses
  `backtest/evaluate.py`/`evaluate_wide.py`/`panel.py`; ~17 covered names × deep
  history; **pre-register before running**. (b) **Engine as-of-quarter plumbing**
  (mechanical: parametrize `scenarios.quarter_keys(start_q,start_y)` + add
  `run_scenarios(asof_quarter=…)`). (c) **Pre-register Test 1** (the engine EV%
  sign test). Full design + the Sharadar field-population result (17/20 covered,
  incl. crude flagships) + the 2018–19 broker-archive depth + the ~2–4-week
  per-era-parser backfill sizing: `outputs/test1_data_feasibility_memo_2026-06-22.md`.
  Carried decisions: proxy-test-FIRST; the powered *engine* test needs the
  broker-weekly backfill — its own go/no-go (Clarksons/VesselsValue declined).
- **§16 overlay-ledger row for §12** (small): wire the §12 dividend-window
  classification into the overlay ledger (resolved direction + `Q*`), closing the
  audit E-2 "ledger is documentation, not a control" gap for this overlay type.
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
demonstrated* cross-sectional edge. The real-P/NAV crude tests are inconclusive by
design (~6q); the one *powered* test (Amendment-2, P/B proxy, N=31) is a clean
negative — but on a book proxy / different universe, so not a refutation of *this*
engine nor support. The path to running the engine's own Test 1 is **now scoped**
(Phase 3 above; `outputs/test1_data_feasibility_memo_2026-06-22.md`). No longer
gates development.

## Verification gate (run before any handoff / Week-close)
- `PYTHONPATH=src .venv/bin/python -m pytest -q` — must stay green (308 at 2026-06-22;
  includes the Phase 2 drift gate, which can legitimately go red on accepted drift —
  annotate + re-ratify rather than revert).
- `python -m crude_tanker_fv.pipeline 2026-Q1` runs clean.
- `python -m crude_tanker_fv.reconcile --all` — SANITY all OK/n-a-APPROX; annotate
  any >2pp drift / band flip in `decisions/<ticker>_log.md`.
- Clean git state; push `origin main`.
