# Producer development freeze — 2026-09-24

**Authority:** owner rulings of 2026-09-24 (`../portfolio-governance/reviews/2026-09-24-wo-scout-1-rulings.md`
R-4), under `../portfolio-governance/WO-SCOUT-1.md` v4 §3 and the approved sequencing plan
(`../portfolio-governance/WO-SCOUT-1-PLAN.md`, Phase 1). Status: **ACTIVE from the commit of this record.**

**What the freeze is:**
- A scope decision. Discretionary producer development stops: new sectors, speculative data infrastructure, further economic-method work, roadmap anchors, and tanker/container/LPG re-expressions for names nobody holds.
- **Holding support continues** for SB, CCEC and SBLK (SBLK exits on GTC 2133904449), and for TEN while it is a routed prereg candidate.
- It is **not** a verdict that the engine has no useful information. Existing research stays as research. No code is deleted and no archive is moved.

**What the freeze is NOT:** the repo-root `PAUSE` file. That stops the delivery worker, sentinel digests and healthchecks, which are receipts this freeze retains. **Do not create `PAUSE` to implement this record.**

## Last supported state (recorded before any change)

| item | value |
|---|---|
| accepted publication | `4d1c91461afa8181c0a39546d6b0c690d56f60e5ef0dfd80b3237ffea079fba5` (accepted 2026-09-24T04:05:04Z) |
| publication source / output commits | `9913185f` / `575cc21d` |
| scorecard | schema 2.9, generated 2026-09-24T04:03:57Z, quarter 2026-Q2, 25 names |
| repo HEAD before this record | `13d652e5` (work_items `paused` status; isolated suite 1023 passed, 2 pre-existing worktree-only failures) |

## Service inventory — keep / pause / retire (one row per `graph.yaml` node)

| node | kind | consumer | essential output | disposition |
|---|---|---|---|---|
| `edgar-poll` | launchd hourly | filings triage, governor falsifier coverage | new filings for held names (SB, CCEC, SBLK, TEN) | **KEEP** |
| `price-refresh` | launchd nightly | price-leg, governor seam | fresh `prices_daily.yaml` so the scorecard stays inside the seam's 72h contract | **KEEP** |
| `sentinel` + lanes `sentinel-checks`, `weekly-report`, `commit-outputs`, `price-leg`, `annotate`, `auto-land`, `auto-push` | launchd daily | owner email, publication | liveness, price-vintage regen/land, truthful failure reporting | **KEEP** |
| `delivery-worker` | launchd 5-min | owner email, governor | publication + SMTP receipts, seam consumption, `work_items.yaml` sync | **KEEP** (it also runs `vie_trial run --if-due`, which records `disabled` while the trial is paused) |
| `accepted-publication`, `governor-seam` | lane / script | governor monitor | accepted-publication history, consumption receipts | **KEEP** |
| `crude-fv-filings-triage` | task daily | owner, governor | filing dispositions for held names | **KEEP** |
| `crude-fv-weekly-news-pull` | task Sat | owner | issuer releases for watchlist names | **KEEP** |
| `crude-fv-mb-weekly-harvest` | task Sat | archive; retained independent data | MB weekly PDFs | **KEEP** |
| `crude-fv-results-shadow-build` | task daily | balance-sheet refresh | quarterly sheet drafts; required for held names and TEN | **KEEP** |
| `crude-fv-fork-executor` | task daily | producer landing | tape absorb + land (infrastructure) and execution of already-open forks. **No new discretionary forks are opened under the freeze.** | **KEEP** |
| `rocketchat-ingest`, `news-pull`, `ffa-promote` | launchd / script | dry-bulk curve behind SB's (and SBLK's) FV | VIE FFA screenshots → dry curve | **KEEP UNTIL VIE CUTOVER** (plan Phase 4). This is the one live VIE dependency behind a held name. |
| `harvester` | launchd Sat | archive + VIE trial | independent market data; its `vie_trial run` step now records `disabled` | **KEEP** |
| `vie-exit-shadow` | lane | VIE-exit trial | replacement-feed comparison | **PAUSE**: `research/vie-exit/trial.json` `enabled: false` (the documented rollback). Receipts and the 94-PDF queue are retained. Vendor inquiries stay unsent. |
| `crude-fv-trigger-check-draft` | task Thu | `crude_geopolitics_weekly` card | crude-tanker geopolitics draft; no crude-tanker holding | **PAUSE**: scheduled task disabled (folder and node kept, so R5 holds) |
| `crude-fv-pinggap-drill-arm` / `-restore` | one-shot tasks | — | already fired and disabled | **RETIRE** at the next graph housekeeping (move to `retired_tasks`). No runtime effect today. |
| `commit-drift`, `regen`, `preflight`, `rebase` | on-demand scripts | chat sessions | used by retained holding-support work | **KEEP** (on demand) |
| `portfolio-weekly-monitor`, `portfolio-quarterly-review-kickoff` | governor tasks | owner | weekly/quarterly governance | **KEEP** |
| `sentinel-lite`, `healthchecks` | external | owner | dead-man coverage | **KEEP** |

**Maintenance cost:** the retained set is the existing automation, unchanged. The saving is agent/owner development time, not jobs. Shrinking the retained set further is a pilot-review decision (plan Phase 5): (a) minimal, or (b) full retire after moving the governor's delivery dependency off this repo's venv/SMTP.

## Work items — PAUSED-BY-FREEZE (status `paused`, evidence = this record)

**Discretionary development (paused, not won't-do; each resumes only by owner decision):**
- Owner-resolved: `roadmap:a1-horizon`, `roadmap:b1`, `roadmap:crude-weights`, `roadmap:product-reexpression`, `roadmap:ten-anchor`, `roadmap:dm2-dm3-dm4`, `economic:adoption-review`, `carry:04` (FRO associate-stake methodology).
- Agent-resolved: `economic:cash-schedules`, `economic:hybrid-joint-scenarios`, `economic:normalized-accounting-eps`, `economic:reference-pairs`, `economic:risk-calibration`, `roadmap:gsl-commitment`, `roadmap:image-filings`, `roadmap:lr1-anchor`, `roadmap:stng-newbuild`, `roadmap:q3-calendar`, `housekeeping:01`, `housekeeping:03`, `housekeeping:04` (autopilot Stage A build-out).
- Data carries for names nobody holds: `carry:02` (HAFN), `carry:03` (TRMD), `carry:05` (FRO), `carry:06` (CMBT), `carry:08` (PANL).

**Adapter-projected triggers** (`inputs/reweight_triggers.yaml`) are **policy-paused**: agents don't work them under the freeze unless they touch a held name or TEN. Their domain status is unchanged. They are agent-resolved and don't force a page. `tce_means_semiannual_review` stays live because it moves every FV, SB's included.

**VIE-trial items** leave the registry when the trial is disabled. Two are re-recorded as manual items because they're still needed:
- `vie:renewal-terms` (owner): check the account's cancellation deadline and access-after-cancellation terms.
- `vie:pnav-controls` (agent): explicit UNAVAILABLE broker states before any production removal (plan Phase 4).

`vie:procurement`, `vie:contract-identity`, `vie:transport`, `vie:unattended` and `vie:broker-triage` pause with the trial.

## Live risks and unresolved financial questions (NOT paused, NOT closed)

- **Stay live:** `filings:pending`, `carry:01` (SBLK share count), `carry:07` (SB `analyst_target`), `trigger:container_mb_refresh`, `defect:01/02/03/05/06`, `housekeeping:02/05`, `quarterly:G-2`, `quarterly:G-3`, and every `governor:*` restriction (the governor's rulings record lists the standing pages).
- `fork:ten_commitments_convention`: open, recommendation HOLD (advances-only), execute-after 2026-09-24. It executes by silence under the existing fork policy. Allowed, because it is an already-open fork on a routed candidate.

## Reversal

- Set any `paused` row back to its prior status with fresh evidence.
- Set `trial.json` `enabled: true`.
- Re-enable `crude-fv-trigger-check-draft`.
- None of these needs code.
