# CLAUDE.md — agent operating rules for the Tanker FV tool

**Read this first, every session.** Mistakes that show up here are mistakes
that have already happened once. Each rule has a date so you can see how
old/proven it is. When you correct a recurring mistake, append a dated rule
to the relevant section here; the narrative goes in `CHANGELOG.md`.

This file is the operational rulebook — kept short on purpose. The detail
lives in companion docs:

- **METHODOLOGY.md** (~1450 lines) — the full valuation framework. The canonical spec.
- **PLAN.md** — the rolling sprint plan / handoff doc. A new agent reads CLAUDE.md, then PLAN.md, then starts.
- **CHANGELOG.md** — dated history of decisions, onboardings, fixes (was this file's Changelog section).
- **TICKER_NOTES.md** — per-ticker quick-refs (consult when working a specific name).
- **WORKFLOWS.md** — step-by-step procedures: onboarding a ticker, report-day refresh, onboarding a sector.
- **LIMITATIONS.md** / **PERMISSIONS_PROPOSAL.md** — known limits; permission-allowlist rationale.

## Project stance — a forward-looking valuation aid (2026-06-21)

This is a **forward-looking, fundamentals tool for valuing individual shipping
equities** — independent NAV (per-vessel age-curve marks) + a forward dividend
strip, blended by cycle position. Judge it by whether its per-name reads are
sound, auditable, and useful for a position call — **not** by a cross-sectional
information coefficient. New sectors, methodology refinements, features, and the
Q2/event-window work are all in scope (see PLAN.md). A crude-subsector "edge"
backtest lives in `backtest/`: its real-P/NAV crude tests are inconclusive by design
(~6 quarters); its two *powered* tests (Amendment-2 P/B proxy N=31, and Amendment-3
P/B proxy on the actual 17-name watchlist incl. all crude flagships + product, N=72,
sector-neutral IC +0.036/t 0.62) both exclude a *moderate* within-sector value premium
— but on a book-value proxy, so they bound the value *premise*, not *this* engine's
market-NAV marks (the powered engine EV% test is still unrun). The tool has **no
demonstrated ex-post cross-sectional edge** (see `outputs/epistemic_soundness_memo_2026-06-22.md`,
`backtest/REPORT.md`);
kept as a recorded diagnostic, **not** a development gate. (A 2026-06-14 "development
freeze" gated on that verdict was **LIFTED 2026-06-21 by owner decision**.)

## What this repo is

Per-share fair value tool for shipping equities. NAV (per-vessel age-curve
marks) + forward dividend strip, blended by cycle position. Sectors live
in `inputs/scenario_inputs.yaml` under `sectors.<name>`. Per-ticker
artefacts: `inputs/{fleet_manifests,balance_sheets,cost_structures,dividend_policies}/`,
plus a row in `inputs/watchlist.yaml`. See `METHODOLOGY.md` for the full framework.

## How to run things

- Tests: `PYTHONPATH=src .venv/bin/python -m pytest -q` (174 baseline at
  2026-06-05; should only ever grow). Never `pytest` without `PYTHONPATH=src`
  — the package isn't installed.
- Pipeline: `python -m crude_tanker_fv.pipeline <QUARTER>` (e.g. `2026-Q1`).
- Pre-flight (what's stale / missing): `python -m crude_tanker_fv.refresh`
  (its §0 consumes `inputs/earnings_calendar.yaml` — hand-maintained; update
  on sight when the weekly digest flags a newly-announced date).
- Reconcile a name: `python -m crude_tanker_fv.reconcile <TICKER>`
  (or `/reconcile <TICKER>`).
- Drift gate (committed, Pareto-free): `python -m crude_tanker_fv.drift_gate`
  — compares current pipeline outputs against the tracked
  `baselines/reconcile_baseline.yaml` (EV% / tool NAV / position band / k_broker
  on its *second difference*); exit 1 on UNEXPLAINED drift. `tests/test_drift_gate.py`
  runs it as a build gate. Re-anchor the baseline ONLY via
  `./scripts/ratify_baseline.sh "<cause>"` (mandatory cause; human commits) —
  **never hand-edit the numbers.** See the Verification loop below.
- S&P print scan (incremental): `python -m crude_tanker_fv.sp_scan` — scans
  Pareto dailies newer than the cursor, writes the review queue to
  `outputs/sp_print_candidates.md`. Human-classified into
  `transactions/<class>.yaml`; **never auto-promote.**
- Daily price refresh: `python -m crude_tanker_fv.price_refresh` — fetches
  watchlist closes (Yahoo) into the automation-writable `prices_daily.yaml`;
  launchd 18:30 daily. Pipeline values at the live close; watchlist statics
  stay as the consensus_pnav/fwd_pe vintage anchors. Flagged quotes (>15% day
  move, >30% vs static) are written but never applied.
- Flush automation drift: `./scripts/commit_drift.sh` — stages + commits (one
  step) the 8 automation-written files the launchd jobs churn. COMMIT-ONLY
  (push stays manual). Decision logs + per-name pipeline outputs EXCLUDED —
  commit those deliberately with their annotations.
- Weekly news pull (mechanical): `scripts/news_pull_cron.sh` — launchd Sat
  08:00, chains RC ingest → `sp_scan` → `--links` → `fetch_links` →
  `pareto_archive --build-manifest` → `ffa_ocr`. The download step is its own
  module `crude_tanker_fv.fetch_links` so every `sp_scan` mode stays local-only.
- FFA widget OCR (incremental): `python -m crude_tanker_fv.ffa_ocr` — parses the
  daily 3-panel Cape/Pmax/Smax screenshot into `state/ffa_ocr_curves.json` +
  review queue; `--staleness` exits 1 if the feed is >7 days quiet. Promotion to
  `inputs/market_data/ffa_forward_curve.yaml` is HUMAN-ONLY. Scratch under
  `state/ffa_scratch/` — tesseract can't read /tmp in the agent sandbox.
- Weekly news pull (agent-judgment): `/news-pull` — web-sweeps watchlist names
  (weighted to APPROX + live-event names) into a dated digest. Review-only;
  promotion is human-only.
- The venv at `.venv/` has `pypdf` installed. **Use it for PDFs that fail WebFetch.**

## What this tool is, philosophically (locked 2026-06-06)

**The tool produces independent NAV from transaction-anchored marks (single-vendor-sourced).** Broker
consensus (Pareto P/NAV) and VIE Coverage Universe are *discrimination
diagnostics*, not calibration targets. Wide tool↔broker spreads are **features**
— the divergence is the call (METHODOLOGY §6 INSW, FLNG, ASC, NAT, TNK; §9.9).
Spreads already documented in §6 with a thesis are intentional, not failures.

This means: **do not "fix" wide spreads by tweaking marks toward Pareto.** If a
name's spread changes, the question is whether the methodology drifted or the
market moved — not whether to recalibrate the curve.

## Verification loop — every change runs the gate

After any change to inputs, schemas, marks, scenarios, or pipeline code:

1. `pytest -q` — must stay at 308+ passing. This now INCLUDES the drift gate
   (`tests/test_drift_gate.py`): an UNEXPLAINED >2pp EV%/NAV move, a band flip,
   or a >0.05 k_broker *second-difference* vs the committed baseline turns the
   suite red until you either annotate `decisions/<ticker>_log.md` (a dated,
   non-placeholder note) **or** re-ratify the baseline with a cause. Don't
   auto-revert a gate-fail on requested work — surface it and let the owner
   decide (memory `feedback_no_unilateral_revert_on_gate_fail`).
2. `/reconcile <affected ticker>` — must report **SANITY = OK** (tool NAV
   within ±50% of broker NAV — anything wider is a bug, not a call).
3. If the **drift column** moved >2pp since the previous quarterly run, update
   the ticker's `decisions/<ticker>_log.md` with the why (market move?
   methodology change? data refresh?) — and re-ratify the baseline
   (`./scripts/ratify_baseline.sh "<cause>"`) once the move is accepted, so the
   annotation window advances and the change becomes the new committed anchor.

The sanity check is a **bug gate**, not a consensus-matching gate. INSW at −36%
to broker NAV is OK (mark-driven, §6 documented); INSW at −95% would be
SANITY=FAIL (you broke something). The drift gate is a **change gate** — it
never asks a number to move toward Pareto (k_broker is tracked on its second
difference, so a stable wide spread sits green); it only asks an *unexplained
change* to be explained or accepted.

## Reconciliation has three jobs, do not conflate them

| Job | What it checks | When it runs | Gate? |
|---|---|---|---|
| **A. Sanity** | Tool NAV within ±50% of broker NAV (no unit error, mis-routed sector, miscount). | Every run, every name. | Yes — pytest fails. |
| **B. v1 calibration lock** | When a new sector ships, ≥70% of validator names land within ±10% of broker NAV at lock-time. | Once per new sector. | Yes, one-time. |
| **C. Drift detection** | Has any name's spread moved >2pp since the previous run without an explainable cause? | Each quarterly refresh. | No — alert. |

Existing sectors (crude / product / LNG) were locked at the tighter ≥80%/±5%
bar; new sectors (dry bulk, containers, LPG, offshore drilling) ship at
≥70%/±10% v1 and tighten in Q3 with one more quarter of data. **The bars apply
at lock-time, not per-run.**

## Data sources — what to trust and how to fetch

- **Quarterly reports (IR PDFs)** are the source of record for fleet counts and
  balance sheets at quarter-end. The live IR fleet *page* disagrees with the
  report at quarter-end — **trust the report.** (Caught on FRO 2026-05.)
- **WebFetch fails on many IR PDFs** (FlateDecode binary). Pattern:
  `.venv/bin/python scripts/fetch_pdf.py <url>` (downloads to /tmp, validates
  the host against `inputs/data_sources.yaml` — add new sources THERE, not to
  the script), then parse with pypdf. Raw `curl` works but prompts.
- **ECO's domain TLS chain fails WebFetch entirely** — use fetch_pdf.py, which
  carries the one audited TLS-verification exception for that host.
- **Compass Maritime weekly URL changes every week** — pattern
  `compassmar.com/wp-content/uploads/YYYY/MM/Compass-Weekly-Report-MMM-DD-YY.pdf`.
- **Pareto Shipping Daily** is the source for `consensus_pnav` /
  `consensus_fwd_pe` in `watchlist.yaml`. Pareto does NOT publish P/NAV for NAT,
  ASC, CCEC — those carry APPROX values; `/reconcile` flags them and downweights.
- **The dailies carry hyperlinks to Pareto's detailed research** as PDF
  annotations — `extract_text()` NEVER sees them (they live in /Annots). Harvest:
  `sp_scan --links` → `fetch_links` → `pareto_archive --build-manifest`. Full NAV
  breakdowns/estimates, far richer than the daily prose. Part of weekly/quarterly ingest.
- **MB Shipbrokers weeklies** (Container/Dry Bulk/Tanker, Fridays by email): the
  email tables are IMAGES — the PDF behind the "Download report" flexmail link is
  the artifact. Harvest links from Gmail (read-only), fetch with `fetch_pdf.py`
  (cdn.flxml.eu allowlisted), archive at `inputs/research_mb/<feed>/YYYY/`.
  Independent cross-check, not a calibration input — same discipline as VIE.
- **VIE Coverage Universe** (Catlin / Mintzmyer) is an independent external check,
  not a calibration input. Track disagreements in §6 footnotes; do NOT bulk-update
  from VIE without an explicit methodology decision per class.

## Recurring gotchas to NOT relearn

(Each is the distilled rule; the incident narrative lives in CHANGELOG.md +
the named decision logs.)

- **Never type a market price from filing/report prose** (2026-06-10, TEN $44).
  Prices come from `prices_daily.yaml` (auto-fetched) or a dated quote source. A
  watchlist `current_price` NEVER moves without rebasing `consensus_pnav` /
  `consensus_fwd_pe` from the same vintage — broker NAV = price/pnav drifts
  silently otherwise. See ten_log.
- **Cross-foot the manifest against the source table before shipping**
  (2026-06-11, TEN): sum the vessel rows, check against the issuer table AND the
  `fleet_summary` block. Machine-enforced by
  `test_fleet_summary_totals_cross_foot_against_vessel_rows`.
- **Long-running background jobs die silently under nohup** (block-buffered
  stdout; 2026-06-10). Pattern: `nohup sh -c 'PYTHONUNBUFFERED=1 ... ; echo "EXIT
  CODE $?"' >> log 2>&1 &`. Watch the log mtime, not just its contents.
- **Newbuilds valued at delivered market less remaining commitment**, NOT sunk
  cost (§3.1, §9.6). Since 2026-06-22 also PV-discounted by
  `1.11^(−years_to_delivery)` per vessel (`years_to_delivery` defaults 0 = on the water).
- **ECO sale-leaseback is in "borrowings"** — no separate operating-lease line; don't double-count.
- **Frontline's SWS yard is Chinese**, not Korean.
- **TC anchors, not spot.** `historical_tce_means.yaml` is TC-anchored; VIE
  multipliers are spot-anchored — they don't numerically compose. (§10.)
- **Weight-set names are sector-namespaced** ("Crude Set A", "LNG Set B-revised").
  A cross-sector "Set B" without a prefix is a methodology error.
- **`use_transaction_anchored` is DEFAULT-ON** (2026-06-09 owner decision).
  Transaction-validated marks ARE the headline marks; pass `False` for the
  un-anchored baseline. k_broker reads as the broker premium over transaction
  levels (~1.12-1.14 on crude pure-plays). Eight classes have own fits
  (VLCC/Suezmax/Aframax/LR2/MR/Cape/Pana/Supra-Ultra) — don't add classes
  without a comparable sample (§9.9). Exclude aggregate prints only when no
  per-vessel split is disclosed (no-back-solve).
- **When new transaction prints land, that IS the drift gate** (2026-06-09):
  re-run, read `outputs/transaction_anchor_comparison.md`, annotate the log of
  every name whose txn-anchored EV moved >2pp or whose band flipped.
- **Two structural framework limits are codified**: §12 (high-payout pure-plays
  at peak — tool UNDERvalues; NAT archetype) and §15 (governance/value-trap — tool
  OVERvalues; `governance_discount_pct` knob, applied at blend + strip terminal
  but NOT to `compute_nav`; TEN archetype). The haircut is judgmental — store it
  auditably per-name with a rationale.
- **Don't back-solve validator marks to broker NAV** (2026-06-09, SBLK). A wide
  validator gap is a methodology question (transaction-anchor per §9.9, or accept
  as documented mark-driven), NOT a license to tune marks. See sblk_log.

## Workflows (see WORKFLOWS.md for the full steps)

- **Onboarding a new ticker** — `/add-ticker` scaffold → fill manifest/balance
  sheet/cost/dividend from the latest filing → `sp_scan --names <TICKER>` Pareto
  sweep → §15 governance screen → watchlist row → pipeline + tests +
  `/reconcile`. SANITY=OK closes the log baseline; SANITY=FAIL → **stop and
  investigate.** The `--names` sweep is also a quarterly-refresh habit.
- **Report-day refresh** — pull the 6-K/10-Q (trust report counts, not the fleet
  page) → update balance sheet → issuer-report S&P sweep → rebase the watchlist
  vintage TOGETHER (price + pnav + fwd_pe from the same daily) → `sp_scan --names`
  → pipeline + `/reconcile` → drift gate.
- **Onboarding a new sector** — methodology decision doc FIRST (time-boxed one
  session) → YAML structure + routing → first validator + reconcile → second
  validator + locked-weights test → `/reconcile --calibration-lock`.

## What NOT to do

- Don't change locked weights (Crude Set A, LNG Set B-revised, Product Set B v2)
  without a §11.x revision and a new lock test.
- **Don't widen `.claude/settings.json` permission rules casually** (2026-06-12;
  rationale in `PERMISSIONS_PROPOSAL.md`). Every `sp_scan` mode is local-only BY
  CONSTRUCTION (network download lives in `fetch_links`, which asks); watchlist /
  transactions / FFA-curve edits ask because promotion is human-only; `git push`
  asks because pushing is deliberate. Bash rules are PREFIX matchers (a network
  flag on an allowed module leaks when flags are reordered — that's why
  fetch_links is its own module, keep it that way), and file-rules govern only the
  agent's file tools, not `cat`/`sed` via Bash. Per-machine "don't ask again" goes
  in `.claude/settings.local.json` (gitignored), never the tracked file.
- Don't add classes to the transaction-anchored pipeline without a comparable
  sample (§9.9 scope discipline).
- Don't bulk-update market data from VIE — directional cross-check only.
- Don't fix a wide tool↔broker spread by tweaking marks. Document the divergence
  in §6 if it's a real call.
- Don't run pipeline against state you didn't author. `state/last_run.json` is
  gitignored and quarter-specific.
- Don't add error handling for cases that can't happen, or comments explaining
  what the code does. METHODOLOGY.md carries the why.
- **Don't drop credential files in the repo.** Secrets (Rocket.Chat PATs, API
  tokens, broker creds) live in `~/.config/crude-tanker-fv.env` — the launchd
  wrapper sources it. `.gitignore` blocks `*_token*`, `*_credentials*`,
  `*_secret*`, `*.rtf`, `.env*` defensively, but the gate is discipline.
  (Caught 2026-06-09: a stray `rocketchat_token.rtf` at repo root.)

## Week-close checklist (codified 2026-06-11, owner decision)

Work is organised in sprints called "Weeks". At the END of each Week, before
handoff, run this checklist — documentation accretes seams during a sprint and
this is where they get smoothed:

1. **Documentation audit.** METHODOLOGY.md: relocate misfiled content, fix stale
   counts/k_brokers/positions, verify cross-references, write the Week's Appendix
   A entry. CLAUDE.md: rules current; TICKER_NOTES.md reconciled against the
   latest delta report; README.md + LIMITATIONS.md refreshed (closed limitations
   marked closed, not deleted). Fan out read-only audit agents; apply fixes in
   the main session.
2. **Verification gate.** Full pytest green; pipeline runs clean; `/reconcile
   --all` SANITY column all OK/n-a-APPROX.
3. **PLAN.md rewritten** for the next Week (theme, steps, standing threads,
   definition of done).
4. **Clean git state** — everything committed with the Week-close CHANGELOG.md
   entry; no untracked strays (check for credential-shaped files).
5. **Push to GitHub** (`git push origin main`) — at Week close at minimum;
   mid-week pushes after significant commits are fine too.

## The compounding-knowledge habit

Anytime the agent makes a mistake that wasn't caught by these rules, append a
dated rule to the relevant section here, and the narrative to CHANGELOG.md.
Ruthlessly edit until the mistake rate visibly drops. This file is checked into
git; rules survive sessions.
