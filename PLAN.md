# PLAN.md — the handoff. What is owed, what is next, and where the truth lives.

A new agent reads CLAUDE.md, then this, then starts. **This file holds only what is still OWED.**
History lives in `CHANGELOG.md`; state lives in the registries named below. Rewritten 2026-09-18,
executing the F5 ruling (`decisions/prune_ledger_2026-09-02.md`) that PLAN stays under 150 lines —
it had reached 980, of which an audit found roughly three quarters was work already done.

## The rule that keeps this file short

**An item lives here only until a registry can answer it.** Completion is recorded in
`inputs/forks.yaml`, `RATIFY_LOG.md`, `inputs/reweight_triggers.yaml` and the decisions/ records;
PLAN kept the *request* and nobody struck it, so the backlog looked like it grew with every
automation. When you finish something, delete its line. When you land a dated commitment, move it to
the trigger register. **Never copy regenerated state into this file** — tier lists, opportunity-set
counts and trigger dates rot within days. Point at the source instead. Guarded by
`tests/test_docs_stay_lean.py`.

## Where the truth actually lives — read these, not a prose copy

| Question | Authority |
|---|---|
| What is due, and when | `inputs/reweight_triggers.yaml` (8 armed cards; the sentinel pages them) |
| What is executing on silence | `inputs/forks.yaml` |
| What the book reads today | `outputs/book_scorecard.md` / `.json` |
| Which names are voided / relabelled / queued | `src/crude_tanker_fv/provenance.py` registries |
| What the anchor is and why | `baselines/reconcile_baseline.yaml` + `RATIFY_LOG.md` |
| What runs unattended | `graph.yaml`, rendered into `OPERATING.md` |
| What happened | `CHANGELOG.md` |

## OWED BY THE OWNER — five, and only these

1. **The crude weight question.** After the 2026-09-18 deck re-expression, 59% of the crude mass
   sits on a base-tracking leg and 13% carries the only real downside. The deck is now coherent; its
   de-escalation CONTENT is a weight question, which WO5's kill-switch fences out of agent scope.
   Not a registered fork. `decisions/r4_deck_reexpression_method_2026-09-18.md` §8.
2. **The product deck's own re-expression.** Same absolute-curve construction against the same
   moving base; WO5 was crude-scoped by design. Not a registered fork.
3. **B1** — re-armed 2026-09-18 when TNK's void retired, never ruled. Trigger: the day a registry
   name reads robust-cheap (none does). `decisions/forks_registered_2026-09-10.md` item 7.
4. **TEN's alternative anchor.** TEN is structurally APPROX — no broker anchor exists. VIE?
   company-implied? none? Resolving it moves TEN out of `tests/test_approx_roster.py`'s guard.
5. **The A1 horizon.** Wired at 10 and unratified since 2026-06-11 — ratify it or drop it.

## OWED BY AN AGENT — prioritized, start at the top

1. **LR1 contract-floor anchor round.** The only overdue valuation work. Frozen prereg
   (`PRE_REGISTRATION_LR1_CONTRACT_FLOOR.md`), its post-Stage-A gate cleared 2026-08-10 and Stage B
   landed 2026-09-09. Predicts INSW +$7.80M, TEN +$1.17M, TRMD and HAFN exactly 0, and takes TRMD to
   VALIDATED-TIGHT.
2. **Land TEN's Q2 pair** from the 2026-09-18 shadow drafts (`ten_2026-Q2.yaml.draft`,
   `ten.yaml.draft`; prereg band 91.7–92.0 HIT, verdict WOULD-HOLD). **Blocker:**
   `shuttle_contracted_book` is an uncited APPROX struck as-of 3/31 and not re-struck at 6/30 —
   non-conservative, and it must clear the figure-provenance queue first. TEN is the last Q1-vintage
   sheet in the book; its 6-K window is re-set to 2026-10-01.
3. **Register the TEN newbuild commitment as a fork** ($2,233,409K, GSL/CMBT/BWLP convention)
   before any §9.6 wiring. It was never registered.
4. **STNG 10-hull §9.6 wiring** — un-gated since thread (d) signed 2026-07-15, ~+$9.6/sh, its own
   pre-registered step.
5. **GSL containers commitment-net prereg** — the shape CMBT took on 2026-09-16. `OFF_CONVENTION_QUEUE`
   is {GSL, STNG, TEN} and GSL leaves by this route.
6. **D-M2 / D-M3 / D-M4** (per-sector asset r_a and relever · cycle-parity denominator A/B ·
   piecewise-linear cycle) are RULED and UNEXECUTED; their post-Stage-A gate expired 2026-08-10.
7. **Q3 calendar re-seed** — CMBT 11/26, BRUT 11/19, OMC AR 2027-02-25. Dispositions are parked in
   `state/filings_triaged.json`; `inputs/earnings_calendar.yaml` still carries Q2 dates.
8. **Auto-fetch page images for image-only filings.** Detection ships (`arrivals.validate_html`);
   recovery is still done by hand, 86 images last time.

## Code defects worth a commit each

- `drift_gate` has no from-inputs recompute mode, so a clean clone cannot run the gate.
- `decision_log_annotated_since` string-matches `**Decision:**` exactly (`drift_gate.py`); a dated
  prefix is invisible to it and untested.
- `_fetch` catches only `HTTPError` in `hkex_poll.py` and `newsweb_poll.py` — a `URLError` escapes
  both pollers. One module-level fix.
- CLAUDE.md's APPROX list names five tickers; `reconcile.APPROX_PNAV_TICKERS` holds nine (adds
  CMDB, GSL, SB, 2343).
- The eight-item news-pull limitations backlog has never been triaged (GlobeNewswire timeout,
  sec.gov/efts 403, hellenic/splash 403, PDF primaries via `fetch_pdf`, JS-shell IR pages,
  Glob/Grep restore-or-bless, the missing 8/14 daily).

## Housekeeping rulings, ruled and unexecuted

- **F13** — merge `TICKER_NOTES.md` into the per-ticker log headers and delete it; CLAUDE.md's
  router still points at it.
- **F16** — four worktrees live under `.claude/worktrees/`; confirm `goldstine` is merged, then
  remove them.
- **F19 remainder** — the `sp_scan` tanker-period-signal internals are dead data.
- **Autopilot Stage A is 3 of 5**: `promote check`/`land`, the weekly report and the "Needs your
  word" queue ship; the **Saturday stager** and the **pin migration** (`tests/fixtures/pins.yaml`)
  do not. Gate 0→A has no owner attestation on file — write it or delete the gate.
- **Standing rule that belongs elsewhere:** source sweeps run single-threaded, no parallel fleets of
  web-fetch-heavy agents. Graduate it to WORKFLOWS.md and drop it from here.

## Carry notes — apply at the name's next vintage, then delete the line

- **SBLK** share count 111,671,386 → 116,071,386.
- **HAFN** Q3 cash-for-investment swap: ΔNAV ≈ 0 only if both legs move together.
- **TRMD** next vintage carries the exact count (104,000,000 is rounded, +0.031%, below any gate).
- **FRO** whether the associate stake belongs in NAV is a methodology question for the owner.
- **Front Vefsna** $135.0M (FRO P1 leg) stays unpromoted, blocked on issuer vessel-name disclosure.
- **CMBT** §9.4 yard-quality discount and Dec-2025 segment vintages — revisit at the November
  Bermuda appeal.
- **SB** `analyst_target` 7.10 has been STALE-flagged since 8/29. **GNK** dividend guidance wants a
  cross-check against `dividend_policies/gnk.yaml`.
- **PANL** onboarding deferred; the B3 IR query went out 2026-08-12 and is still waiting. Scaffolded
  in `data_sources.yaml`, not watchlisted.

## Gated on data that does not exist yet

§18.5a Baltic realized-mean and §18.5b independent orderbook-to-fleet. The parity/divergence column
is a hypothesis with a test attached, not a result. Do not present it as a finding.

## Backtest

No demonstrated edge, cross-sectional or time-series. The powered 72-quarter proxy deflated Test 2's
+0.234 to +0.078, effectively null. Reference only, **never a gate** (`backtest/REPORT.md`).

## The verification gate

`bash scripts/regen.sh <QUARTER>` → `PYTHONPATH=src .venv/bin/python -m pytest -q` → `reconcile --all`
with 0 SANITY failures → drift gate 0 UNEXPLAINED. The anchor then advances by itself: `promote land`
ratifies behind its five preconditions and the morning lane pushes. The real predicate is
`promote.evaluate_land` (a)–(e) — read it rather than a prose copy.

## Recent landings (agents append one line here, newest first; prune below ten)

- 2026-09-18 — WO5/R4 complete: deck re-expressed, three void dispositions ruled (CAPT retired, TNK
  retired to cycle-relabel, BRUT upheld), Phase 5 ratified.
- 2026-09-18 — fork executor absorbs the inherited tape before judging its own promote (owner ruling).
- 2026-09-18 — one clock per pipeline run; the surface and the run state no longer skew.
- 2026-09-18 — trigger-check draft task installed (Thursdays 09:00); TRIGGER-DUE paging fixed.
