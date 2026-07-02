# External audit 2026-07-02 — findings register + disposition

An independent clone-and-run review (Claude, cloud) of commit `6749362`, delivered
2026-07-02. The full audit text is preserved verbatim below the disposition. Every
finding was re-verified locally the same day by a 18-agent verification workflow
(12 finding-verifiers + adversarial re-checks on all P0/P1 verdicts + a
launchd-health check); all five P0/P1 verdicts survived adversarial refutation.

## Disposition (2026-07-02)

| ID | Sev | Verdict | Status | Where fixed |
|---|---|---|---|---|
| F-1 | P0 | confirmed — **worse**: the "day move" band was a ~5-session trailing move (`chartPreviousClose` on `range=5d`), so a step-repricing held names on statics up to 5 trading days, not 1 | **FIXED** — true prior-day close from the daily bars; ≥3-name market-event circuit breaker (prices applied + review marker); loader records fallbacks; scorecard header discloses price basis | `price_refresh.py`, `loaders.py`, `scorecard.py` + tests |
| F-2 | P0 | confirmed — weights exact (0.25/0.45/0.18/0.12, all "Jun-9 POINT-IN-TIME"); no post-June-28 annotation anywhere | **OWNER DECISION PENDING** — reweight proposal drafted for sign-off (see `decisions/`) | `inputs/scenario_inputs.yaml` §13.3 discipline |
| F-3 | P1 | confirmed — blast radius **6 names** (BRUT, CAPT, CCEC, GSL, SB, TEN), not 3; bisection lower-bound residue 50/2^101 | **FIXED** — exact-zero sentinel; docs render "price justified by NAV alone" / "n/a"; committed-outputs guard | `breakeven.py`, `scenarios.py` + `test_outputs_hygiene.py` |
| F-4 | P1 | confirmed | **FIXED** — `outputs/book_scorecard.json`, schema_version 1, void-striking + NaN→null, lock-tested; governance repo must assert schema_version on ingest | `scorecard.py` + tests |
| F-5 | P1 | partial — spot_tce never feeds the strip; the REAL exposure is `ffa_forward_curve.yaml` (VLCC q1 $147.5k = 3.7× mean, **under** the 5× warning bar) + `twelve_month_tc.yaml`, all unrefreshed 2026-06-07 war vintage; `pareto_daily.csv` parsing stopped 06-11; `baltic_indexes_daily.csv` is consumed by nothing | **OPEN** — needs a dated rate refresh from a current Pareto Daily (pairs with the F-2 re-run) | `inputs/market_data/{spot_tce,ffa_forward_curve,twelve_month_tc}.yaml` |
| F-6 | P2 | confirmed — worse: an all-skip run also touched `decisions/*.md` | **FIXED** — quarter regex + abort-before-state-writes | `pipeline.py` + `test_pipeline_cli.py` |
| F-7 | P2 | confirmed — intra-commit staleness (scorecard rendered mid-edit within b5019cf) | **FIXED** — regenerated; TRMD carries `· basis-pending` | outputs regen commit |
| F-8 | P2 | confirmed — zero guard pinned TNK's state anywhere | **FIXED** — verdict prose derived from rows; forced-short test | `scorecard.py` + tests |
| F-9 | P2 | partial — README stale as claimed, but the audit's own count was wrong (460 collected, not 440) | **FIXED** — Status refreshed; counts guarded vs watchlist.yaml | `README.md` + `test_docs_stay_lean.py` |
| F-10 | P3 | confirmed — F-3 fix provably removes the whole text-diff surface | **FIXED** (via F-3) | — |
| F-11 | P3 | confirmed — worse: queues hand-edited in TWO files (provenance.py + duplicate guard-test literals), synced by an equality test | **OPEN** (no action per audit; YAML migration optional) | `provenance.py` |
| F-12 | P3 | confirmed — validate.py check is warn-only; same unguarded division in `dividend_strip.py` | **FIXED** — hard error at load | `loaders.py` + `test_validate.py` |

**Beyond the audit (local-only findings):** the July-1 18:30 price cron fired and wrote
July-1 closes; ~1h later the file was reverted to HEAD during the HAFN reconciliation
session (the "isolate price drift" discipline's revert step) and the separate re-ratify
never happened — the July-1 vintage survived only in `state/price_refresh.log`, and the
2026-07-02T04:32Z pipeline run priced 5 names on June-4 statics. Recovery + the amended
discipline (revert → drift commit in the SAME session) handled separately.

---

# Original audit text (verbatim)

**Date:** 2026-07-02 · **Auditor:** Claude (independent clone-and-run review) · **Commit audited:** `6749362` (HEAD, "baseline: re-ratify drift gate — TRMD P0 reconciliation")

**Scope:** Full clone from GitHub; static review of engine source, provenance/tier logic, drift gate, and documentation; dynamic verification via full test-suite execution, end-to-end pipeline regeneration, drift-gate execution, and diff of regenerated outputs against committed outputs. Out of scope (local-only): raw broker PDFs vs parsed CSVs, the harvester crawl cache, FFA screenshot ingest, and launchd job health.

## Executive summary

The repo is in materially better shape than most institutional research code. It reproduces end-to-end from a clean clone on a machine it has never seen: 440 tests pass, all 22 names regenerate, the drift gate returns 0 UNEXPLAINED, and the only content diffs against committed outputs were two known items (one of which is itself a finding). The epistemic posture — the prominent null-edge disclosure, the single-vendor mark-dependency disclosure, the xfail-as-audit-queue design, and the second-difference k_broker gate that structurally cannot pressure the tool toward broker consensus — is the strongest part of the system.

The findings that matter are operational, not architectural, and they cluster around one event: the June 30 sector-wide repricing (US–Iran stand-down, Doha talks, Brent back to pre-war levels). The price-sanity band rejected five fresh prices simultaneously on exactly the day a genuine market event occurred, so the current committed scorecard values the five most-affected names on June 4–10 prices. Separately, three names' scenario documents carry a degenerate ~10²⁹ value in a decision-relevant column, and the single handoff surface to the governance repo is a markdown table with no machine-readable contract.

## Findings register

| ID | Severity | Finding | Where |
|---|---|---|---|
| F-1 | **P0** | Sanity band rejects sector-wide repricing; scorecard EV% computed on pre-crash prices for 5 names | `price_refresh.py`, `loaders.py` |
| F-2 | **P0** | Crude scenario weights (45% Pre-MoU, 25% Escalation) now inverted vs the tape after the stand-down | `scenario_inputs.yaml`, §13 |
| F-3 | P1 | Degenerate breakeven → ~10²⁹ ratios printed in committed scenario docs for CAPT, SB, TEN | `scenarios.py:584` |
| F-4 | P1 | Governance handoff surface is a markdown table; no machine-readable, schema-versioned export | `scorecard.py`, seam |
| F-5 | P1 | Rate-level inputs carry war-spike vintage (VLCC spot $388,300/day) into the strip leg | `spot_tce.yaml` |
| F-6 | P2 | CLI takes raw `sys.argv[1]` as quarter; `--help` (or any typo) silently runs the pipeline | `pipeline.py:1050` |
| F-7 | P2 | Committed scorecard one commit staler than provenance code (TRMD `basis-pending` label missing) | `outputs/book_scorecard.md` |
| F-8 | P2 | Hardcoded per-name narrative in generated verdict prose ("TNK is VALIDATED-TIGHT and BUY but reads rich…") | `scorecard.py:293` |
| F-9 | P2 | README status block stale: says 20 tickers / 378 tests; actual 22 / 440 | `README.md` |
| F-10 | P3 | Float non-determinism across platforms at extreme magnitudes (last digits of F-3 values differ per run) | `scenarios.py` |
| F-11 | P3 | Tier/provenance state lives in hand-edited Python sets rather than data files | `provenance.py` |
| F-12 | P3 | `nav_per_share` division by `diluted_shares_outstanding` unguarded against zero | `nav.py` |

*(Full audit narrative — P0/P1/P2/P3 sections, "What holds up well", and residual local
scope — retained in the session transcript of 2026-07-02; the register above plus the
disposition table carry the durable content. Residual local items the auditor could not
check: parsed transaction/marks CSVs vs raw broker PDFs in the harvester cache; launchd
job health (done 2026-07-02, all green); FFA OCR spot-check vs source PNGs.)*
