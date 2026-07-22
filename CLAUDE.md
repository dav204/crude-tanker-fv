# CLAUDE.md — agent operating rules for the Tanker FV tool

**Read this first, every session.** Mistakes that show up here have already happened
once; each rule is dated so you can see how proven it is. This file is the **router**,
kept short on purpose — when you fix a recurring mistake, append a dated ONE-LINER rule
here and the narrative to `CHANGELOG.md`. Detail lives in the companions:

- **METHODOLOGY.md** — the full valuation framework. The canonical spec.
- **PLAN.md** — the rolling sprint plan / handoff. A new agent reads CLAUDE.md → PLAN.md → starts.
- **CHANGELOG.md** — dated history of decisions, onboardings, fixes (the gotcha narratives live here).
- **TICKER_NOTES.md** — per-ticker quick-refs (consult when working a specific name).
- **WORKFLOWS.md** — step-by-step procedures + the **command runbook**, **per-source fetch mechanics**,
  and the **Week-close checklist** (all migrated out of this file 2026-07-01).
- **LIMITATIONS.md** / **PERMISSIONS_PROPOSAL.md** — known limits; permission-allowlist rationale.

## Project stance (2026-06-21)

A **forward-looking, fundamentals tool for valuing individual shipping equities** — independent NAV
(per-vessel age-curve marks) + a forward dividend strip, blended by cycle position. Judge it by whether
its per-name reads are sound, auditable, and useful for a position call — **not** by a cross-sectional
information coefficient. New sectors, refinements, features, and the Q2/event work are in scope (PLAN.md).
The tool has **no demonstrated ex-post cross-sectional edge** (`backtest/REPORT.md`,
`outputs/epistemic_soundness_memo_2026-06-22.md`) — kept as a recorded diagnostic, **not** a development
gate (the 2026-06-14 freeze on that verdict was LIFTED 2026-06-21 by owner decision).

## What this repo is

Per-share fair value tool for shipping equities. NAV (per-vessel age-curve marks) + forward dividend
strip, blended by cycle position. Sectors live in `inputs/scenario_inputs.yaml` under `sectors.<name>`.
Per-ticker artefacts: `inputs/{fleet_manifests,balance_sheets,cost_structures,dividend_policies}/` + a
row in `inputs/watchlist.yaml`. See METHODOLOGY.md for the framework.

## How to run things (essentials — full runbook in WORKFLOWS.md)

- **Tests:** `PYTHONPATH=src .venv/bin/python -m pytest -q`. Never bare `pytest` (package not installed).
- **Pipeline:** `python -m crude_tanker_fv.pipeline <QUARTER>` (e.g. `2026-Q1`).
- **Reconcile:** `python -m crude_tanker_fv.reconcile <TICKER>` (or `/reconcile <TICKER>`).
- **Drift gate:** `python -m crude_tanker_fv.drift_gate` vs `baselines/reconcile_baseline.yaml`.
  Re-anchor ONLY via `./scripts/ratify_baseline.sh "<cause>"` (mandatory cause; human commits) —
  **never hand-edit the numbers.**
- **PDFs:** `.venv/bin/python scripts/fetch_pdf.py <url>` (WebFetch fails on many FlateDecode PDFs).
- **Two venvs:** engine + tests on `.venv` (Python 3.9.6); the vendored `shipping_harvester` ONLY on
  `.venv310` (3.12). Never cross them. (`shipping_harvester/data/` is gitignored; its source is tracked.)
- Other commands (`refresh`, `sp_scan`, `price_refresh`, `commit_drift`, news pulls, `ffa_ocr`, Test-1)
  → WORKFLOWS.md §Runbook.

## What this tool is, philosophically (locked 2026-06-06)

**The tool produces independent NAV from transaction-anchored marks (single-vendor-sourced).** Broker
consensus (Pareto P/NAV) and the VIE Coverage Universe are *discrimination diagnostics*, not calibration
targets. **Wide tool↔broker spreads are FEATURES** — the divergence is the call (METHODOLOGY §6 INSW /
FLNG / ASC / NAT / TNK; §9.9); spreads documented in §6 with a thesis are intentional, not failures. So:
**do not "fix" a wide spread by tweaking marks toward Pareto.** If a spread changes, ask whether the
methodology drifted or the market moved — not whether to recalibrate the curve.

## Verification loop — every change runs the gate

After any change to inputs, schemas, marks, scenarios, or pipeline code:

1. **`pytest -q`** — must stay green (count guard-tested in README; includes `tests/test_drift_gate.py`). An UNEXPLAINED >2pp
   EV%/NAV move, a band flip, or a >0.05 k_broker *second-difference* vs the baseline reds the suite
   until you annotate `decisions/<t>_log.md` (dated, non-placeholder) OR re-ratify with a cause. **Don't
   auto-revert a gate-fail on requested work** — surface it, let the owner decide (memory
   `feedback_no_unilateral_revert_on_gate_fail`).
2. **`/reconcile <affected ticker>`** — must report **SANITY = OK** (tool NAV within ±50% of broker NAV).
3. If the **drift** moved >2pp since the last quarterly run, annotate the log with the why, then
   `./scripts/ratify_baseline.sh "<cause>"` once the move is accepted (advances the committed anchor).

**SANITY is a BUG gate, not a consensus gate** (INSW −36% to broker = OK, mark-driven §6; −95% = you
broke something). **The DRIFT gate is a CHANGE gate** — never asks a number to move toward Pareto
(k_broker on its second difference, so a stable wide spread sits green); it only asks an *unexplained
change* to be explained or accepted. Don't conflate the three reconciliation jobs: **Sanity** (±50%,
every run, gate) vs **v1 calibration-lock** (new sector, ≥70%/±10% of validators at lock-time, once) vs
**drift** (change alert). Existing sectors locked at ≥80%/±5%; new sectors (dry bulk / containers / LPG /
offshore) ship ≥70%/±10% v1 and tighten in Q3. The bars apply at **lock-time, not per-run.**

## Data sources — what to trust (fetch mechanics in WORKFLOWS.md §Data-sources)

- **Quarterly reports (IR PDFs) are the source of record** for fleet counts + balance sheets at
  quarter-end. The live IR fleet *page* disagrees at quarter-end — **trust the report.** (FRO 2026-05.)
- **Pareto Shipping Daily** is the source for `consensus_pnav` / `consensus_fwd_pe`. Pareto does NOT
  publish P/NAV for **NAT / ASC / CCEC** — those carry APPROX values; `/reconcile` flags + downweights.
- **VIE (Catlin/Mintzmyer) and MB Shipbrokers are independent cross-checks, NOT calibration inputs** —
  track disagreements in §6 footnotes; do NOT bulk-update from them without a per-class methodology decision.

## Recurring gotchas to NOT relearn (distilled; narrative in CHANGELOG.md + the named logs)

- **Any NAV-moving manifest field must resolve to a citation** (2026-06-30, DHT/NAT). Field-general: a
  verification CLAIM (`(confirmed)`/`verified`) AND a value-moving FIGURE (commitment / advance / price)
  must each trace to a specific filing / note / broker / owner / dated reference. A `~` or `[ESTIMATE]`
  is a **RED, not data** — "present but uncited" fails like "absent" (an uncited NAV-driver silently
  moves the number). Enforced by `test_manifest_provenance` (+ `test_scrubber_provenance` /
  `test_newbuild_convention` / AGE0_BASIS for the value flags). **Before wiring a §9.6 on-curve fix, the
  name's commitment/advance must be OUT of the figure-provenance queue** (`NAV_FIGURE_ESTIMATE_QUEUE`;
  else the move builds on sand). The live blocked list is in PLAN.md, not here (it's dynamic).
- **Never type a market price from filing/report prose** (2026-06-10, TEN $44). Prices come from
  `prices_daily.yaml` or a dated quote; a watchlist `current_price` NEVER moves without rebasing
  `consensus_pnav` / `consensus_fwd_pe` from the same vintage (broker NAV = price/pnav drifts otherwise).
- **The snapshot MUST match the NAV/balance-sheet date — fleet AND every balance-sheet figure** (2026-07-01,
  SB fleet + ASC newbuild). A results 6-K's fleet table is as-of the FILING date, and its **Subsequent Events
  note is where post-quarter events hide** — a delivery/sale/newbuild ORDER dated after quarter-end does NOT
  belong in the snapshot (ASC's April-2026 Handysize order was wrongly loaded as a −$88.8M Q1 commitment; SB
  was the fleet-table version). **Audit the subsequent-events note FIRST** on every reconciliation; build
  AS-OF the NAV date from the closest-to-quarter filing (20-F / prior 6-K), not the newest page. The "nothing
  changed" intuition is the trap — the quarter-boundary transactions are what a stale snapshot gets wrong.
- **Cross-foot the OPERATING-scrubber COUNT vs the issuer's disclosed aggregate at onboarding** (2026-07-01,
  SB) — a blanket per-class `scrubber:true` is the CAPT peer-borrowed-flag bug. Scrubber is a static
  value-adding flag with no build-year rule; source it per-vessel — its sum MUST equal the issuer's
  disclosed aggregate — and move the name to `OPERATING_SCRUBBER_VERIFIED{name:count}`
  (`test_verified_operating_scrubber_count` asserts the count). **Work the queue at onboarding** — don't
  ship a blanket default into `OPERATING_SCRUBBER_QUEUE` and leave it (a queued name can still carry a wrong count).
- **"Read-only" agents must not run pytest/pipeline in the shared tree** (2026-07-18) — the run
  regenerates outputs+logs; one agent's stash swept live session work. Worktree-isolate them.
- **Newbuilds valued at delivered market LESS remaining commitment** (NOT sunk cost; §3.1/§9.6),
  PV-discounted `1.11^(−years_to_delivery)` per vessel (defaults 0 = on the water).
- **`use_transaction_anchored` is DEFAULT-ON** (2026-06-09). Txn-anchored marks ARE the headline; k_broker
  reads as the broker premium over transaction levels (~1.12-1.14 crude). 8 classes have own fits
  (VLCC/Suezmax/Aframax/LR2/MR/Cape/Pana/Supra-Ultra) — **don't add classes without a comparable sample**
  (§9.9); exclude aggregate prints only when no per-vessel split is disclosed (no back-solve).
- **When new transaction prints land, that IS the drift gate** (2026-06-09) — re-run, read
  `outputs/transaction_anchor_comparison.md`, annotate every name whose txn-anchored EV moved >2pp / band flipped.
- **Don't back-solve validator marks to broker NAV** (2026-06-09, SBLK) — a wide validator gap is a
  methodology question (txn-anchor per §9.9, or accept as documented mark-driven), not a license to tune.
- **Dry-bulk manifest `dwt` is LOAD-BEARING** (§11.7.10) — Cape/Pana/Supra-Ultra/Handy-Bulk curves are
  `dwt_scaled` (value ∝ dwt/baseline: Cape 180k / Pana 82k / Supra-Ultra 62k / Handy 38k, §11.7.11), so a rough dwt mis-values a hull; use
  the issuer's exact per-vessel dwt, split mixed cohorts by sub-class. (Crude/product/lng/container stay
  flat-per-class.) PPMX §9.9 fit SEEDED 2026-07-18 (mark-wide both nodes, refit armed; overhang residual — ppmx prereg).
- **Two structural framework limits are codified:** §12 (high-payout pure-plays at peak — tool
  UNDERvalues; NAT archetype) and §15 (governance/value-trap — tool OVERvalues; `governance_discount_pct`
  applied at blend + strip terminal but NOT to `compute_nav`; TEN archetype). The haircut is judgmental —
  store it auditably per-name with a rationale.
- **An output column must not encode a NAV-relative read as a trade signal** (2026-06-30). A §12
  cycle-rich position is RELABELED ("rich · cycle position (not a short)"); a number derived off a
  CONTRADICTED figure is VOIDED in the output (not just its FV); a wide/provisional tier carries a
  **sub-reason = resolution path**. Registry in `provenance.py` (`POSITION_CYCLE_RELABEL`,
  `POSITION_UNRELIABLE`, `NAV_DERIVED_VOID`, `TIER_SUBREASON`), no-drift-tested.
- **An incidental identity is NOT an invariant — two surfaces assumed to agree need a TEST that they
  agree** (2026-07-02, 3× same day; guards: test_scorecard F-13, test_outputs_hygiene, test_carveout).
- **Gate expectations scale by determinant LEG, not past event** (2026-07-22, owner catch): the 7/06
  container elasticity was TC+value JOINT — a TC-only refresh predicts NAV exactly 0.00; nonzero NAV =
  HALT (frozen file touched). Predicted-impact blocks state which files may move and which are frozen.
- **Weight-set names are sector-namespaced** ("Crude Set A", "LNG Set B-revised"). A cross-sector "Set B"
  without a prefix is a methodology error.
- **ECO sale-leaseback is in "borrowings"** — no separate operating-lease line; don't double-count.
- **Frontline's SWS yard is Chinese**, not Korean. **TC anchors, not spot** — `historical_tce_means` is
  TC-anchored, VIE multipliers spot-anchored; they don't numerically compose (§10).

## Workflows (full steps in WORKFLOWS.md)

- **Onboarding a ticker / report-day refresh / onboarding a sector** — the multi-step procedures live in
  WORKFLOWS.md. Load-bearing discipline: SANITY=OK closes the log baseline, **SANITY=FAIL → stop and
  investigate**; trust the report counts (not the fleet page); rebase the watchlist vintage TOGETHER
  (price + pnav + fwd_pe from the same daily); a new sector gets its methodology decision doc FIRST.

## What NOT to do

- **Don't change locked weights** (Crude Set A, LNG Set B-revised, Product Set B v2) without a §11.x
  revision and a new lock test.
- **Don't widen `.claude/settings.json` permission rules casually** (2026-06-12; rationale +
  full detail in PERMISSIONS_PROPOSAL.md). `sp_scan` is local-only by construction (network lives in
  `fetch_links`, which asks); watchlist / transactions / FFA-curve edits + `git push` ask because
  promotion/pushing is human-only. Bash rules are PREFIX matchers (keep `fetch_links` its own module).
  Per-machine "don't ask again" → `.claude/settings.local.json` (gitignored), never the tracked file.
- **Don't run the pipeline against state you didn't author** — `state/last_run.json` is gitignored and
  quarter-specific.
- **Headless agents are "constrained, unattended, zero authority"** (2026-07-03): drafts only
  (`*prereg*.md`, `*.yaml.draft`), no Bash/git/web; ambiguity → "requires human", never silently
  resolved. Full rules in `.claude/commands/filing-packet.md`.
- **Don't add error handling for cases that can't happen, or comments explaining what the code does** —
  METHODOLOGY.md carries the why.
- **Don't drop credential files in the repo.** Secrets (Rocket.Chat PATs, API tokens, broker creds) live
  in `~/.config/crude-tanker-fv.env` (the launchd wrapper sources it). `.gitignore` blocks `*_token*`,
  `*_credentials*`, `*_secret*`, `*.rtf`, `.env*` defensively — but the gate is discipline. (Caught
  2026-06-09: a stray `rocketchat_token.rtf` at repo root.)

- **Owner navigation lives in README, not PLAN** (2026-07-15): if the owner must ask
  "where does X live," add it to README the same day.

## Week-close checklist + the compounding-knowledge habit

- **Week-close checklist** (doc audit → verification gate → PLAN.md rewrite → clean git → push) →
  WORKFLOWS.md §Week-close.
- **The compounding-knowledge habit — self-limiting BY DESIGN** (so it stops re-bloating this file, the
  way it grew to 357 lines / ~6.2k tokens before the 2026-07-01 restructure). Compounding is monotonic —
  accretion needs a paired eviction policy or the always-loaded router degrades every session. When a
  mistake wasn't caught, add the guard in this order:
  1. **Prefer a GUARD/TEST over prose.** A test enforces the rule forever at ZERO context cost (it isn't
     read into the prompt); the durable artifact is the guard, not the sentence. Codify what's codifiable,
     then make the CLAUDE.md line a one-line pointer at the test — or drop it.
  2. **On the Nth instance of a pattern, GENERALIZE and DELETE the specifics** — never append a 4th
     instance-rule; merge into one field-general rule + guard (as the four provenance catches collapsed).
  3. **One-liner only; the narrative goes to CHANGELOG.md** (read on demand, not every session); any
     detail past a line migrates to a companion (WORKFLOWS/METHODOLOGY) with a pointer left behind.
  4. **Hard budget:** `tests/test_docs_stay_lean.py` reds the build if CLAUDE.md exceeds ~16k chars
     (~4k tokens). At the cap you EVICT / MIGRATE / GENERALIZE — you do NOT raise the cap to fit a rule.
  5. **Compact at Week-close** — sweep for rules now subsumed by a guard, obsolete, or duplicated, and
     graduate them out. Accretion + eviction = a router that stays a router. (Git-tracked; rules survive.)
