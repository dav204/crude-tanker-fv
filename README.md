# Shipping Equity Fair Value Tool

Independent fair-value estimate per share for shipping equities — 25 names
across **crude tanker / product tanker / LNG / dry bulk / containership /
LPG** — built to validate and stress-test sell-side analyst targets. Blends
two lenses — net asset value (NAV, from per-vessel transaction-anchored
marks) and a forward dividend strip — with the blend weight set by cycle
position, then runs scenario sensitivities, a broker-NAV sweep, and a
transaction-anchored curve diagnostic. **Not investment advice.**

See [METHODOLOGY.md](METHODOLOGY.md) for the full framework (~3,000 lines);
this README is orientation for someone landing on the repo cold.

### How this was built

End-to-end through **agentic development with Claude Code** — this repo is
itself the working example of that workflow. Concretely, and verifiable in
the history:

- Effectively every commit is agent-written under human direction: all but
  ~14 (early scaffolding) carry `Co-Authored-By: Claude` trailers, and the merged
  PRs (#1, #2) plus the `claude/*` branches are cloud agents opening PRs
  against the repo for review.
- **Sprint handoffs are spec-first:** [PLAN.md](PLAN.md) is the rolling
  handoff a fresh agent session reads to pick up mid-sprint ("a new agent
  reads CLAUDE.md, then this file, then starts"), rewritten at each weekly
  close with the current state, dated gates, and definition of done.
- **[CLAUDE.md](CLAUDE.md) is the standing engineering convention set** —
  dated, mistake-derived rules with a build-enforced size cap
  (`tests/test_docs_stay_lean.py`), so the always-loaded rulebook cannot
  grow without evicting: when a rule can be a test, it becomes a test.
- **The ~600-test suite is what lets agents extend the system safely:**
  validator fair values are band-locked, doc counts are census-guarded,
  data-provenance rules are enforced as xfail-strict queues (an xfail
  *clearing* is the work), and an owner-ratified drift baseline turns any
  unexplained output move into a red build. Agents work inside those
  guardrails; the human rules on anything that moves a number.

### What "independent" means here, and what it does not

The NAV is methodologically independent of broker *opinion*: it builds per-vessel
marks from disclosed transaction prices and ages them on its own curves rather than
backing into a target P/NAV, and a wide gap to a broker's published NAV is treated as
a signal to investigate, not an error to close. That independence is real but narrow,
and two dependencies should be stated plainly. First, the transaction marks that
anchor the curves are not source-independent of the brokers compared against: roughly
three-quarters of the in-window prints (about 76%, and closer to 87% in dry bulk and
product) are drawn from a single vendor's research, and for six names that vendor
supplies both the comparison NAV and the calibrating prints, so agreement between them
is weaker evidence than it appears. Crude pure-plays are the best-corroborated tier
(about half their prints carry issuer-filing or trade-press cross-checks); dry bulk and
product are the most single-source. Adding further broker houses softens but does not
cure this: brokerages recycle overlapping market intelligence, so a second house
reporting the same deal is corroboration of the report, not an independent observation
of the market — multi-house counts overstate statistical independence. Second, a disagreement with a broker cannot, by
construction, prove a mark wrong; only a disclosed transaction at odds with a mark, or a
gross sanity-gate breach, can. The per-name EV% and BUY/TRIM/HOLD label are a structured,
auditable valuation opinion relative to price and to one broker's NAV, not a backtested
forecast of returns: no cross-sectional return edge has been demonstrated — two *powered*
P/B-proxy backtests (incl. one on the actual 17-name watchlist over 72 quarters) exclude a
moderate within-sector value premium, while the engine's own signal has only an underpowered
(n=5, INCONCLUSIVE) ex-post read — a faithful vintaged pipeline is built, but reaching
significance needs a pre-2024 backfill
(see [backtest/REPORT.md](backtest/REPORT.md) and
[outputs/epistemic_soundness_memo_2026-06-22.md](outputs/epistemic_soundness_memo_2026-06-22.md)).
Use the reads as one disciplined input to a position call, sized accordingly.

## Status (2026-08-09)

- **25 tickers** across 6 sectors: crude (10, incl. **TEN** the 3-sleeve hybrid,
  **CAPT** the first Oslo/NOK listing, **BRUT** the pure-play VLCC newbuild
  vehicle, and **CMBT** the multi-sleeve), LNG (2), product (4), dry bulk (5,
  incl. **2343** Pacific Basin — the first HKEX/HKD listing and the first
  Handy-Bulk carrier, Stage-3 intake 2026-07-14), containerships (2), LPG (2,
  the WO3 Phase-4 validators)
- **602+ tests passing** end-to-end (ticker count, sector split, AND this test
  count are guarded by `tests/test_docs_stay_lean.py` — the count asserts
  against the suite's own test-function census within a tolerance band, audit
  N-7 2026-07-14)
- **8 output families** regenerated per pipeline run + 5 standalone diagnostics
  (LNG weight robustness, crude weight robustness, VIE coverage universe xref,
  VIE market rates xref, terminal-value sensitivity)
- **Onboarded sector validators:** DHT (crude) / FLNG (LNG) / ASC (product) /
  SBLK + GNK + CMDB (dry bulk, 2026-06-09/10) / MPCC + GSL (containerships,
  2026-06-12 — first charter-coverage sector); TRMD added 2026-06-03 (first
  full-3-class product), HAFN 2026-06-04 (first IFRS + pool operator), CAPT
  2026-06-11 (17th name, newbuild-heavy crude, tightest first reconcile on record)
- **Locked weight families:** crude Set A (current); LNG Set B-revised v3
  (2026-06-01, §11.3); product Set B v2 (2026-06-03, §11.5)
- **Framework limitations now documented:** §12 (high-payout pure-plays at
  peak), §13 (scenario-weight stability), §14 (MEG export infrastructure
  + cargo switching + sanction waiver + stockpile replenishment dynamics),
  §10 (TC-vs-spot baseline methodology + VIE within-window structural
  adjustment refinement), §11.6 (DP2 shuttle off-curve-at-contracted-book
  convention — closes the TEN architectural blocker), §15 (governance /
  structural-NAV-trap discount — the inverse of §12; first applied to TEN
  at 30% haircut for controlled-FPI + related-party + low-payout drivers)
- **External counter-signals tracked:** VIE Coverage Universe cross-reference
  (Catlin / Mintzmyer) — full 10-of-10 overlap; CCEC / ASC / TRMD / HAFN
  direct opposite-direction signals documented in §6 footnotes

## Where the official output lives (start here)

**The producer's official output is the committed `outputs/book_scorecard.md` /
`.json` pair at pushed HEAD.** Everything else in `outputs/` is evidence and
decomposition behind it. (Added 2026-07-15 — owner feedback: this map took too
long to find.)

| Surface | What it is | Consumer |
|---|---|---|
| `outputs/book_scorecard.md` | **THE handoff** — Verdict table (tier·sub-reason, price, Model FV, FV range, upside, position, Blend FV, NAV/sh, broker NAV, gap, SANITY, handoff-ready, W-frag) + Validation matrix. Header discloses price basis, rate basis (incl. any held-curve state), weight-family vintage | Humans: the single surface a sizing decision reads |
| `outputs/book_scorecard.json` | The same content as a **schema-versioned machine contract** (currently 2.5; consumer asserts major == 2). Adds `fv_low`/`fv_high`, `weight_sign_stable` + family EV ranges, `mark_wide_nodes`, hybrid sleeve FVs, vintage stamps (`generated_at`, `source_commit`) | The governance repo's monitor (its §4 seam check) |
| `outputs/<ticker>_fv_report.md` / `.xlsx` | Per-name single-point build: NAV breakdown, dividend strip, cycle weighting, blend + FV attribution, breakeven, 5×5 grid, divergence diagnosis | Per-name deep dives |
| `outputs/<ticker>_scenarios.md` | The scenario deck + probability-weighted FV that feeds the Verdict | Per-name deep dives |
| `baselines/reconcile_baseline.yaml` + `RATIFY_LOG.md` | The accepted-state anchor + the dated, cause-carrying record of every ratify (the drift gate reds on unexplained moves against it) | The audit trail; the governance monitor reads RATIFY_LOG weekly |
| `decisions/*.md` | Per-name logs + dated decision/ruling docs — the provenance trail | The "why" behind any number |
| `outputs/weight_robustness.yaml`, `broker_nav_sweep.*`, `transaction_anchor_comparison.md`, `delta_report.md`, … | Diagnostics the scorecard summarizes | Inputs to judgment, not handoff surfaces |

Trust markers on any copy: it is committed at HEAD, its `source_commit` stamp is
clean (a `-dirty` stamp on a committed scorecard reds the suite), and the whole
tree regenerates byte-identical from a cold clone (verified by both external
audits). Handoff rule: a PROVISIONAL tier never hands off a governed FV —
flag, don't pass; only VALIDATED-TIGHT and GOVERNED-WIDE are handoff-ready.

## What this tool does

1. **Per-name fair value.** For each ticker on the watchlist, compute a tool
   fair value per share by blending NAV (per-vessel age-curve marks, balance
   sheet adjustments, newbuild orderbook valued at delivered-market-less-
   remaining-commitments) and a forward dividend strip (8 quarters of EPS →
   DPS → discounted DPS, with a terminal NAV). Cycle-position weighting shifts
   the blend toward NAV at peak and toward earnings at trough.

2. **Scenario sensitivity.** Each sector has 4-5 macro scenarios with their
   own probability weights, vessel-value multipliers, and forward curves. The
   crude sector uses a three-phase MoU framework (escalation / pre-MoU
   baseline / MoU base / MoU bear); LNG runs glut-cycle scenarios with a
   `vessel_scale_multiplier`-driven structural-reset tail; product runs
   refinery-margin / glut scenarios.

3. **Decision-relevant diagnostics.** The pipeline surfaces (a) the implied
   breakeven TCE that justifies the current price (and how far above the
   forward curve it sits), (b) a 5×5 sensitivity heatmap (rate shock × vessel-
   value shock), (c) a broker-NAV sweep showing how mark-driven each call is
   (the `k_broker` premium that lifts tool NAV to consensus NAV — wide spreads
   signal mark-uncertain names; tight spreads signal mark-validated ones),
   and (d) a transaction-anchored curve recalibration toggle that re-fits
   mid-age curve anchors against disclosed second-hand transactions.

4. **Pre-flight + post-flight workflow.** A `refresh` command emits a
   pre-flight checklist of what's stale or missing for the target quarter
   (with IR URLs to pull from); the pipeline emits a post-flight delta
   report (what changed since last run) and prepends a structured
   model-state entry to a per-ticker decision log where you annotate what
   you actually did and why.

## What this tool is NOT

Pre-empting the "where does this go wrong?" question — see
[LIMITATIONS.md](LIMITATIONS.md) for the full set with detail. Headlines:

- **Not investment advice.** The tool produces a fair-value estimate; the
  decision is yours. Documented framework limitations (§12) exist for
  high-payout cyclicals at peak — see NAT and STNG entries in METHODOLOGY §6.
- **Not real-time.** Inputs are point-in-time per quarter. The tool is for
  decision support around Q-end earnings, not intraday rate moves.
- **Not API-stable.** The Python modules are private surface; treat them
  as research scaffolding, not a contract. Input YAML schemas are
  documented (METHODOLOGY §4) but may evolve.
- **Not multi-user.** No auth, no permissioning, no API endpoint. This is
  single-user research infrastructure.
- **Not a Bloomberg / Clarksons / VesselsValue replacement.** The tool
  consumes data from those sources (vessel value curves, broker NAVs); it
  doesn't substitute for them.
- **Coverage scope: Handysize-and-above clean product + Chemical Handymax.**
  Clean-product Handysize (~37-40k) and Chemical Handymax (38k IMO-II coated)
  are now ON-curve as of 2026-06-05 — HAFN's 22, ASC's 2, and STNG's 14 hulls
  migrated from `working_capital_net`. Residual gaps: ASC's 4 × 25k stainless
  chemical hulls (sub-25k specialty pool, off-curve) and pure-chemical parcel
  operators above Handysize (Stolt-Nielsen / Odfjell — un-onboardable until a
  stainless-Handymax curve at the Odfjell-NB $72.5M anchor lands). DP2 shuttle
  tankers were RESOLVED via the §11.6 off-curve-at-contracted-book convention
  (TEN onboarded 2026-06-06); dry bulk is IN-scope as of 2026-06-09 (§11.7,
  SBLK/GNK/CMDB); containerships are IN-scope as of 2026-06-12 (§11.8,
  MPCC/GSL — coverage-schedule charter framework, all-APPROX external
  anchors). Offshore remains out of scope.

## Current watchlist

**Crude sector (`sectors.crude` — three-phase MoU framework):**

| Ticker | Company | Fleet shape |
|---|---|---|
| DHT  | DHT Holdings | Pure VLCC (22 vessels) — crude methodology validator |
| ECO  | Okeanis Eco Tankers | Modern VLCC + Suezmax, all-spot, eco design |
| FRO  | Frontline | VLCC + Suezmax + LR2; 9 Hemen VLCC NBs newbuild-at-market |
| INSW | International Seaways | Hybrid crude + product (whole-company v2 carve-out) |
| TNK  | Teekay Tankers | Atlantic-skewed: Suezmax + Aframax/LR2 + 1 VLCC |
| NAT  | Nordic American Tankers | Pure Suezmax (18 vessels) — §12 framework-limitation case |
| TEN  | Tsakos Energy Navigation | 3-sleeve hybrid: crude + product + LNG (60 in-water + 19 NBs); 4 DP2 shuttle off-curve via §11.6 convention; §15 case (30% haircut) |
| CAPT | Capital Tankers | 12 VLCC + 10 Suezmax + 4 Aframax + 4 LR2; 21 NBs at delivered-market-less-commitment; Oslo/NOK (added 2026-06-11) |
| BRUT | Brut Tankers | Pure-play VLCC newbuild vehicle (12 firm NBs, 0 on-water) — the §9.6 max-torque case; Oslo Growth/NOK (added 2026-06-22) |
| CMBT | CMB.TECH | Multi-sleeve conglomerate (crude + dry-bulk + chemical/Windcat, §11.9); ex-Euronav (added 2026-06-27) |

**LNG sector (`sectors.lng` — glut-cycle framework):**

| Ticker | Company | Fleet shape |
|---|---|---|
| FLNG | Flex LNG | 13 modern 174k cbm LNGCs (MEGI / X-DF) — LNG methodology validator |
| CCEC | Capital Clean Energy Carriers | 12 LNGCs + 9 LNG NBs + 1 MGC + 8 gas NBs |

**Product sector (`sectors.product` — refining-margin / glut framework, unlocked 2026-06-01):**

| Ticker | Company | Fleet shape |
|---|---|---|
| ASC  | Ardmore Shipping | 19 active MRs + 6 off-curve Handysize/chem — product validator |
| STNG | Scorpio Tankers | 32 LR2 + 41 MR on-curve + 14 Handymax off-curve + 10 NBs (incl. 2 VLCC) |
| HAFN | Hafnia | Largest product fleet (~120 incl. pools); IFRS reporter |
| TRMD | Torm | First full 3-class product (LR2 + LR1 + MR) |

**Dry bulk sector (`sectors.dry_bulk` — Bulk Set A, unlocked 2026-06-09):**

| Ticker | Company | Fleet shape |
|---|---|---|
| SBLK | Star Bulk Carriers | 135 bulkers (Cape 31 / Pana 46 / Supra-Ultra 58) — first dry-bulk validator; §6 mark-driven |
| GNK  | Genco Shipping | 44 bulkers (Cape 20 / Supra-Ultra 24, no Pana — Q2: Volunteer in, Predator out) — dry validator for the txn-anchored curves (k 1.10 at 2026-08-09; live value in outputs/broker_nav_sweep.md) |
| CMDB | Costamare Bulkers | 30 owned older bulkers + P&L-only chartered-in platform; §15 case (30% haircut), APPROX anchor |
| SB   | Safe Bulkers | 44 operating + 1 HFS + 8 NB (Cape/Pana/PPMX mix) — the lone VALIDATED-TIGHT BUY (added 2026-06-27) |
| 2343 | Pacific Basin | ~110 owned Handy-Bulk/Supra (40.7% Handy) + P&L-only chartered-in book; 1st HKEX; §11.7.11 (added 2026-07-14) |

**LPG sector (`sectors.lpg` — WO3 Phase-4 validators, 2026-07-10; sector
PROVISIONAL·v1-lock-miss, re-run 2026-11-13):**

| Ticker | Company | Fleet shape |
|---|---|---|
| LPG  | Dorian LPG | 22 owned VLGCs (16 scrubber/dual-fuel-tagged); US domestic filer |
| BWLP | BW LPG | ~50 VLGCs incl. 20+ LPG dual-fuel; BW India listed sub (NCI via preferred_equity); Product Services trading arm |

**Containerships sector (`sectors.containerships` — Container Set A,
coverage-schedule charter framework, unlocked 2026-06-12):**

| Ticker | Company | Fleet shape |
|---|---|---|
| MPCC | MPC Container Ships | 51 on-water (21 feeder / 30 intermediate) + 15 owned NBs net-of-commitment; Oslo/NOK; first containerships validator |
| GSL  | Global Ship Lease | 71 vessels (30 intermediate / 41 large, 18.2-yr TEU-weighted); full charter table — the coverage-convention stress test; APPROX P/B anchor |

## Sample output: broker-NAV sweep

_Illustrative snapshot from the 2026-06-04 vintage (13 names); the live
25-name table regenerates every run at `outputs/broker_nav_sweep.md`._

The diagnostic that distinguishes mark-validated calls from mark-driven ones.
Per name: `k_broker` is the uniform vessel-mark premium that lifts tool NAV
to the consensus broker NAV (= price ÷ consensus P/NAV). The EV%-spread is
how much of the call is value vs mark choice.

| Ticker | Cons. P/NAV | k_broker | EV @ tool | EV @ broker | Spread | Read |
|---|---:|---:|---:|---:|---:|---|
| DHT  | 1.09 | 0.99 | -18.7% | -19.8% | -1pp  | mark-validated |
| ECO  | 1.22 | 0.99 | -32.4% | -33.2% | -1pp  | mark-validated |
| FRO  | 1.21 | 0.99 | -30.8% | -31.4% | -1pp  | mark-validated |
| STNG | 0.87 | 1.10 | -13.0% | -5.9%  | +7pp  | mostly mark-validated |
| CCEC | 0.90 | 0.98 | +14.1% | +5.0%  | -9pp  | mark-validated, weight-driven BUY |
| TNK  | 0.76 | 1.18 | -1.7%  | +8.0%  | +10pp | mark-driven |
| FLNG | 1.42 | 0.87 | -7.2%  | -28.3% | -21pp | tool above broker |
| INSW | 0.97 | 1.37 | -32.2% | -10.1% | +22pp | mark-driven |
| ASC  | 0.75 | 1.59 | -26.5% | +13.1% | +40pp | mark-driven |
| NAT  | 0.85 | 1.79 | -57.8% | -5.2%  | +53pp | mark-driven + §12 case |

A 0pp spread means the call is the same at tool marks and broker marks; a
wide spread means the call would flip under reasonable mark choices.
Mark-validated bucket = the tool's NAV machinery agrees with broker
consensus on the assets it covers. Mark-driven bucket = the call is
dominantly a question of which vessel marks you believe.

## The two-command workflow

```sh
# Start of quarter (or whenever something feels stale):
python -m crude_tanker_fv.refresh           # → outputs/refresh_checklist.md
#   Scan the checklist; pull missing balance sheets via the IR URLs it lists;
#   update stale market data files; refresh APPROX consensus_pnav entries.

# After data assembly:
python -m crude_tanker_fv.pipeline 2026-Q1  # → 8 output families
#   Then open outputs/delta_report.md for the "what changed" summary,
#   and annotate decisions/{ticker}_log.md with your calls.
```

### Operations (unattended watches)

The read-only sentinel answers "does anything need the owner's eyes?" and, with
`--notify`, emails the owner (PAGE for incidents, one unconditional daily digest
otherwise — notifier death is detectable by the digest's absence and by the
healthchecks dead-man ping, which fires only after a completed run whose sends
succeeded). Tags: `TRIGGER-DUE`, `STALE-INPUT`, `SURFACE-INCOHERENT`,
`PRICE-BASIS`, `SIDECAR-STALE`, `NOTIFY-UNCONFIGURED`, `FETCH-FAILED`,
`UNINGESTED-PRINTS`, `TRIGGER-EVIDENCE` (+`DIRTY-TOO-LONG` in dirty meta-mode);
routing in `inputs/notify.yaml`. On a dirty tree the sentinel runs META-MODE
(content checks suspended, liveness alive); tracked-tree writers skip outright;
staging-only fetchers keep fetching (`PAUSE` file stops everything). A GitHub
Action (`sentinel-lite`) runs the repo-pure subset daily against pushed state
as the off-machine backstop. Every drift-gate re-ratify appends a row to
`RATIFY_LOG.md` (the consuming repo's monitor reads it).

```sh
python -m crude_tanker_fv.sentinel --log state/sentinel.log --notify --ping
```

Five launchd jobs (plists in `scripts/`, installation human-only — see
`decisions/launchagents_reconciliation_2026-07-03.md`): RC ingest (daily
07:00), sentinel (daily 08:15), price refresh (daily 18:30), news-pull chain
(Sat 08:00), broker-marks harvester (Sat 09:00). Every wrapper heartbeats to
`state/heartbeat/<job>` (even on SKIP) and ledgers to
`state/automation_runs.log` with its initiator — launchd label vs
`manual:user@tty` — the no-human-fetches instrument. launchd
`StartCalendarInterval` COALESCES missed firings: N sleeps collapse to ONE run
on wake (measured semantics: `decisions/ctxprobe_checklist_2026-07-03.md`);
fetchers are cursor-based, so one coalesced run recovers the whole gap.

#### Staging → ingest map (how data reaches a number)

Fetching is automated; **ingestion of determinants is always a deliberate,
cited, committed, gate-annotated human event.** Arrivals are validated at
staging (PDF magic + opens + ≥1 page; failures → `_quarantine/` + flag) and
ledgered to `state/arrivals.jsonl` with a stable identity (RC message-id /
accession number).

| Staging tree (gitignored) | Fetcher (schedule) | Cursor | Review surface | Determinant fed | Promotion rule |
|---|---|---|---|---|---|
| `inputs/research_pareto/` | RC ingest (daily 07:00) | `state/rocketchat_ingest.json` | `outputs/sp_print_candidates.md`, name sweeps, links | `spot_tce`/`twelve_month_tc` (+`transactions/*.yaml` prints) | human, cited, same-vintage rebase; `UNINGESTED-PRINTS` at >7d |
| `inputs/ffa_drybulk/` | RC ingest + daily `ffa_ocr` | `state/ffa_ocr_state.json` | `outputs/ffa_ocr_queue.md` | `ffa_forward_curve` + dry-bulk 12M TC | human promotion of the OCR diff (owner eyeballs) |
| `inputs/market_data/baltic_indexes_daily.csv` | RC ingest (text parse) | same RC cursor | — | **none — deliberately unconsumed** | blocked on a real $/day TC series (§18.5a contract; never scale index points) |
| `shipping_harvester/data/` | harvester (Sat 09:00, `.venv310`) | `data/manifest.jsonl` | marks-trail flag → manual triage | `transactions/*.yaml`; Xclusiv Resale cross-checks | human per §9.9; `UNINGESTED-PRINTS marks-trail` at >7d |
| `inputs/research_mb/<feed>/` | Gmail agent step + `scripts/mb_harvest.py` (Sat session, initiator `session:mb-batch`) | idempotent by filename | manual read of the weekly | container Ctr-* TC/values (§11.8 **source of record**) | cited §11.8 ingest event (trigger `container_mb_refresh`) |
| `inputs/market_data/prices_daily.yaml` | price refresh (daily 18:30) | overwrite-per-run | `PRICE-BASIS` flags | watchlist `current_price` | never moves without rebasing consensus from the same vintage |
| `inputs/filings/<ticker>/` | EDGAR poller (WO2 Phase 2) | `state/edgar_poll.json` | `/filing-packet` drafts | balance sheets, fleet manifests | human reconciliation; SANITY gate; subsequent-events note first |

The 8 output families per pipeline run:

| Output | What it answers |
|---|---|
| `{ticker}_fv_report.md` + `.xlsx` | Single-point FV with full NAV breakdown, dividend strip, breakeven, 5×5 sensitivity (per name) |
| `{ticker}_scenarios.md` | Probability-weighted FV across the sector's scenarios, with EV% and position recommendation (per name) |
| `fair_value_summary.xlsx` | Watchlist roll-up: tool FV vs current vs analyst target, all names in one table |
| `scenario_summary.xlsx` | Per-sector scenario sheets + cross-name pair-trade implied returns |
| `broker_nav_sweep.md` + `.xlsx` | The mark-validated vs mark-driven discrimination diagnostic (shown above) |
| `transaction_anchor_comparison.md` + `.xlsx` | NAV / EV impact of applying transaction-anchored mid-age curves (Aframax + Suezmax) |
| `justified_pnav.md` + `.xlsx` | Coverage-independent justified P/NAV per name (does the fleet earn its cost of capital on its marked NAV?) — benchmarks the APPROX names; ordering tool (§17) |
| `delta_report.md` + `decisions/{ticker}_log.md` | What changed since last run + per-ticker decision log with structured model-state entries |

## Architecture at a glance

```
src/crude_tanker_fv/
  schemas.py         input data structures               (METHODOLOGY §4)
  loaders.py         YAML input loaders                  (§4)
  vessel_values.py   per-class age-curve marks           (§3.1)
  nav.py             NAV per share                       (§3.1)
  dividend_strip.py  forward dividend strip              (§3.2)
  cycle.py           cycle-position weighting            (§2.3)
  blend.py           blended fair value                  (§2.1-2.2)
  breakeven.py       implied breakeven TCE               (§3.3)
  sensitivity.py     5×5 sensitivity grid                (§3.4)
  scenarios.py       scenario engine + sector class maps (§11)
  carveout.py        hybrid crude+product carve-out      (§6)
  marks.py           broker-NAV sweep + k_broker solve   (§9.9)
  transactions.py    transaction-anchored curve recalibration (§9.9)
  validate.py        input validation + warnings         (§4.6)
  report.py          per-name + watchlist output         (§7)
  pipeline.py        orchestration / CLI entry           (§8)
  delta.py           snapshot + delta report + decision-log prepend (§7.7, §7.8)
  refresh.py         pre-flight quarterly refresh checklist (§8.3)
inputs/
  fleet_manifests/      {ticker}.yaml
  balance_sheets/       {ticker}_{quarter}.yaml
  cost_structures/      {ticker}.yaml
  dividend_policies/    {ticker}.yaml
  market_data/          vessel_value_curves, spot_tce, twelve_month_tc,
                        ffa_forward_curve, historical_tce_means
                        + transactions/{class}.yaml
  scenario_inputs.yaml  per-sector scenarios + forward curves
  watchlist.yaml        current prices + analyst targets + consensus_pnav
  data_sources.yaml     per-ticker IR URLs for the refresh checklist
outputs/                generated reports (md + xlsx), regenerated each run
decisions/              per-ticker decision logs (user-curated, git-tracked)
state/                  pipeline state snapshot (machine-local, gitignored)
tests/                  the full guard suite (count guard-tested above)
```

## Install

```sh
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q                                    # full suite (count guard-tested above)
python -m crude_tanker_fv.refresh             # smoke-test refresh
python -m crude_tanker_fv.pipeline 2026-Q1   # smoke-test full pipeline
```

To regenerate the methodology PDF (requires Pandoc + LaTeX):

```sh
# macOS:  brew install pandoc basictex
# Linux:  apt install pandoc texlive-xetex
bash scripts/build_methodology_pdf.sh        # → METHODOLOGY.pdf
```

## Validation status

- **Per-sector methodology validators:** DHT (pure VLCC, single-class, full-
  payout) for crude; FLNG (pure modern LNGCs, fixed dividend, no NBs) for
  LNG; ASC (pure MR, single-class, variable payout) for product. Each
  validator's fair value is band-locked in tests so structural regressions
  surface immediately.
- **Mark discrimination:** the broker-NAV sweep classifies every name on the
  B4 two-regime semantics (k_broker 1.05–1.25 = the validated pure-play band
  on txn-anchored sectors; outside = mark-driven, the spread documented in §6
  with a thesis). *(The pre-2026-06 "≤10pp validated / >10pp driven" list that
  used to sit here is vintage language — see LIMITATIONS §1.)* Critical for
  sizing — wide spreads mean the call is sensitive to vessel-mark choice.
- **Transaction anchoring:** Aframax and Suezmax curves were recalibrated
  against disclosed second-hand transactions (TNK Aframax sale-leasebacks,
  NAT Suezmax disposals). The recalibration is opt-in (default off in
  production) to preserve the broker-marked baseline as the primary lens.
- **Hybrid carve-out preservation invariant:** INSW's whole-company FV is
  pinned to within $0.20/sh across the v2 product-sector refactor — the
  refactor swapped the v1 shortcut (MR forwards under `sectors.crude`)
  for the clean `sectors.product` routing without disturbing the answer.

## Documentation

- **[METHODOLOGY.md](METHODOLOGY.md)** — full framework (canonical spec;
  §1-§18 + Appendix A change record + per-ticker §6 notes)
- **[LIMITATIONS.md](LIMITATIONS.md)** — known framework limitations and
  validation status (the "where does this go wrong?" doc)
- **[decisions/README.md](decisions/README.md)** — decision-log format and
  workflow guidance
- Per-name reports include a Modeling Notes section + data-validation
  warnings at the top

## Repo layout cheatsheet

```
README.md           ← you are here
METHODOLOGY.md      ← the framework (canonical)
LIMITATIONS.md      ← the credibility doc
src/                ← code (16 modules, ~3500 lines)
inputs/             ← per-ticker YAMLs + market data + scenarios
outputs/            ← generated each run
decisions/          ← user-curated per-ticker logs
state/              ← machine-local snapshot (gitignored)
tests/              ← the guard suite
scripts/            ← PDF build script
notebooks/          ← exploratory / hand-check work
```
