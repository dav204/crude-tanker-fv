# PLAN.md — active plan / sprint handoff

A new agent reads CLAUDE.md, then this file, then starts. This is a
**forward-looking valuation aid** for shipping equities (independent NAV +
forward dividend strip, blended by cycle position), judged by the soundness of
its per-name reads — not by a cross-sectional backtest. Development proceeds
normally; the earlier 2026-06-14 "development freeze" was **lifted 2026-06-21**
by owner decision (see the project-stance note at the top of CLAUDE.md).

## Recent work — Week 5 (hardening)

- **B4 — §9.9 mark-driven classification restated: SHIPPED 2026-06-12** (commit
  cb83315; two-regime k_broker band in METHODOLOGY §9, mechanical sweep relabel,
  fetch_links argparse fix).
- **B5 — anchor-basis commensurability: SHIPPED 2026-06-21** (commit 5fc3b7d).
  `anchor_basis` enum on every cycle-anchor block in `scenario_inputs.yaml`;
  shared helpers in `scenarios.py`; MIXED-ANCHOR-BASIS flag in the delta report
  + `reconcile --all` (per-name basis in `--verbose`); METHODOLOGY §10
  subsection; +5 tests (280 passed). Metadata + diagnostics only.
- **B6 — §9.2 terminal-value multiple: LOCKED at 1.0× (owner, 2026-06-21).**
  Four-option memo (`outputs/terminal_value_options_memo.md`, each option
  steelmanned) on the refreshed 19-name sweep; owner ratified 1.0× (status quo),
  with cycle-conditional recorded as the designated successor pending an adoption
  trigger (memo §4). No engine change (1.0× is production); decision pinned by
  `test_terminal_nav_multiple_locked_at_1x` and recorded in §9.2 item 2 + the
  memo DECISION block. **DONE.**

## Active backlog

### Event window
- **GNK AGM / Diana tender — IN PROGRESS.** Jun-18 AGM outcome read + annotated
  (`decisions/gnk_log.md` 2026-06-21: Diana lost the proxy fight; the $24.80
  tender is still live to Jun-26 + a non-binding $27.34 cash+stock under board
  review). A one-time Jun-26 tender-resolution check is SCHEDULED
  (`gnk-diana-tender-jun26-check`) — it re-reads the outcome and re-frames the
  position (deal-arb → NAV-discount on a lapse).
- **FFA-OCR go/no-go:** owner reviews the 16 flagged queue days, then record the
  diagnostic-vs-strip decision; Stage 2 (2020-2026 backfill) rides on it.
- **Weekly `/news-pull` digests** — resume the Saturday cadence (the Jun-13 /
  Jun-20 slots lapsed during the freeze).

### Q2-refresh carry-forwards (earnings calendar + preflight §0 drive timing)
- **MPCC (reports 2026-08-26):** replace cohort built-year ESTIMATES + NB
  delivery quarters with the issuer fleet list; clean per-vessel prices on the
  three handed-over sale prints; refresh the company-implied NAV anchor.
- **GSL (Aug-04/06):** Series B preferred count post-ATM; the Jun-26 $917M NB
  order's charter attachments; 20-F Item 6 board-rights verify.
- **TEN (September, H1 reporter):** TCM fee-load computation (§15 anchor); apply
  ten_log Q2-vintage kit deltas (Ulysses sale, Sola TS step-up, rolls).
- **CMDB:** the Astros sale price — clean age-8 Ultramax print if per-vessel.

### Standing threads
- **MB Shipbrokers weeklies — LANDED 2026-06-12.** Ingest route established
  (Gmail link harvest → `scripts/fetch_pdf.py` → `inputs/research_mb/`).
  Container current-rate refresh queued (owner-gated); crude NB anchor review;
  Pana anchor flagged structurally low; LNG weekly not yet delivered. Full
  once-over: `outputs/mb_weekly_check_2026-06-12.md`.
- **shipping_harvester (sibling repo) — reviewed 2026-06-21.** Verdict: keep as
  a separate sibling and vendor it as a VIE-style cross-check; do NOT integrate
  into `src/`. Only the rate/demolition feeds (spot/period-TC, demolition→scrap)
  are clean, human-promoted candidates; broker vessel-VALUE legs stay
  diagnostic-only (anti-calibration rule). Currently untracked inside the repo
  tree — gitignore or move out to avoid an accidental commit.
- **Brokerage MCP — CLOSED 2026-06-12** (DENY rules on the synced server id;
  re-check the UUID in a fresh session's tool list — disconnect/reconnect can
  stale it).
- **OWNER ACTION pending:** ratify-or-revise the A1 horizon interpretation
  (wired as 10 strip quarters = end-2028; brief said "~12q from report date").
- **Hormuz weight-revisit trigger** — standing; preempts everything if
  physical-transit confirmation lands. (MB Weekly 24: draft memo + 30-day
  window, trigger NOT met.)
- **§5 ask-tier verification (interactive session):** confirm git push /
  watchlist-edit / fetch_links / curl actually PROMPT with a human present (the
  autonomous session could only prove deny rules enforce).
- **Deferred by owner:** /news-pull agent-half orchestration; Task-3 weight
  adjuster; demand-destruction overlay; FFA Stage 2.

## Backtest (complete — reference only, not a gate)

A crude-subsector edge backtest lives in `backtest/` (pre-registration +
`backtest/REPORT.md`). Finding: no *statistically demonstrated* cross-sectional
edge on the ~1.5 years of published P/NAV available — expected given a 4-name
universe / ~6 quarters, a known limitation of cross-sectional testing at that
scale, not a refutation of the per-name valuation work. Kept as a recorded
diagnostic. Test 1 (engine EV% vs naive P/NAV) was never run (blocked on
historical point-in-time `CompanyInputs`); revisit only if an independent
multi-year vintage source is supplied. This no longer gates development.
