# External audit 2026-07-14 — clean-clone re-review

**Date:** 2026-07-14 · **Auditor:** Claude (independent clone-and-run review) · **Commit audited:** `1d3db14` (HEAD, "baseline: re-ratify drift gate — 2343 onboarding + 2026-07-14 price vintage") · **Prior audit:** 2026-07-02 @ `6749362` (`outputs/EXTERNAL_AUDIT_2026-07-02.md`)

**Scope:** Full clone from GitHub ~30 minutes after the 2343 ratify landed. Static review of engine source, provenance queues, FX handling, CI workflow, packaging, and secret hygiene (including full 297-commit history). Dynamic verification: full test-suite execution, end-to-end pipeline regeneration for 2026-Q1 with byte-level diff against committed outputs, drift-gate execution, `/reconcile 2343`, `sentinel --pure`, the vendored harvester's own suite, scenario-weight and derived-curve identity checks. Environment: Python 3.12.3, pandas 3.0.2, numpy 2.4.4 (deliberately ahead of the pinned 3.9.6 stack, as a portability probe). Out of scope (local-only): launchd job health, raw broker PDFs vs parsed CSVs, FFA screenshot ingest vs source PNGs, the governance repo's consumer side.

## Executive summary

The repo is in better shape than at the 2026-07-02 audit, and that audit found it already better than most institutional research code. Every dynamic gate passed from a cold clone on an unpinned, newer Python stack: **580 tests pass** (0 failures; 16 xfails are the designed provenance audit-queue, 4 skips), the **full pipeline regenerates all 25 names byte-identical** to committed outputs (the only diffs are run-artifacts: the first-run delta report, the by-design decision-log prepends, xlsx binary timestamps, and the scorecard JSON's `generated_at`/`source_commit` metadata), the **drift gate reads 25 rows / 0 UNEXPLAINED** against the baseline ratified hours earlier, `/reconcile 2343` reproduces the PLAN-recorded −2.0% gap, and `sentinel --pure` correctly flags today's DHT 6-K, the 2343 static price, and four earnings-due windows. Secret hygiene is clean across the working tree **and the full commit history**. All five P0/P1 fixes from the prior audit are verified present in code and effective in committed outputs; F-2 closed through the pre-registered Doha trigger discipline rather than ad-hoc editing, which is exactly how the governance layer is supposed to work.

Nothing found rises above P2. The findings cluster around **packaging/CI drift** — the declared dependencies diverge completely from the imports, and two test surfaces (push-time CI, the harvester suite) are gaps a solo-operator workflow papers over — plus one **numerical-precision** issue introduced by the first sub-$1 listing.

## Prior-audit disposition verification (F-1 … F-12)

| ID | Prior status | Re-verified 2026-07-14 |
|---|---|---|
| F-1 | FIXED | **HOLDS.** True prior-day close from daily bars in `price_refresh.py`; `market_event` circuit-breaker path present; scorecard header discloses price basis (1/25 STATIC-FALLBACK: 2343, correctly). |
| F-2 | OWNER DECISION PENDING | **CLOSED via trigger discipline.** Post-stand-down recalibration ratified 07-02 (`d1544b4`); Doha STRIKE leg fired Jul-7/8 and the pre-registered Jun-9 war-tilt restore executed at owner go (`85453dc`); current weights 0.25/0.45/0.18/0.12 sum to 1.000. Successor decision (Hormuz re-tilt, LNG v4 + product war-shape) is PREPARED and staged for owner ruling — open owner work, not a defect. |
| F-3 | FIXED | **HOLDS.** Exact-zero sentinel in `breakeven.py`; "price justified by NAV alone" rendering in `scenarios.py`; grep of all committed outputs finds zero degenerate ~10²⁹ values. |
| F-4 | FIXED | **HOLDS.** `book_scorecard.json` at `schema_version: "2.3"`; content reproduces exactly after metadata strip. |
| F-5 | OPEN | **SUBSTANTIALLY ADDRESSED, residue disclosed.** `spot_tce.yaml` refreshed 2026-07-02 (VLCC $285.5k, war premium annotated); dry-bulk FFA re-anchored 2026-07-13 from the OCR widget (owner-ratified, all three classes); tanker forward curves HELD at the 2026-06-07 vintage by owner decision option (i) with the `tanker_forward_print_lands` trigger registered and the hold disclosed in the scorecard header. This remains the largest open valuation-quality item — the tanker strip leg is priced off a war-shaped curve now 37 days old — but it is a documented owner decision with a trigger, not silent staleness. |
| F-6 | FIXED | **HOLDS.** Quarter regex + abort-before-state-writes verified in `pipeline.py:main`. |
| F-7 | FIXED | Committed scorecard stamps `source_commit` one behind its regen commit (inherent — a commit cannot know its own hash); content at HEAD is byte-identical to regen, so no staleness in substance. |
| F-8 | FIXED | **HOLDS.** Verdict prose derived from rows; forced-short test present. |
| F-9 | FIXED | **HOLDS.** README says 25 tickers / 6 sectors, guarded by `test_docs_stay_lean` against `watchlist.yaml`. (See N-7 on the unguarded test count.) |
| F-11 | OPEN (accepted) | Unchanged: queues live as hand-edited sets in `provenance.py`, synced to guard-test literals by an equality test. Current queues: `NAV_FIGURE_ESTIMATE` = brut/cmbt/flng/hafn/ten; `OFF_CONVENTION` = CMBT/STNG/TEN; `OPERATING_SCRUBBER` = 8 names; `SCRUBBER_UNVERIFIED` = empty. |
| F-12 | FIXED | **HOLDS.** Hard `ValueError` at load for `diluted_shares_outstanding <= 0` in `loaders.py`. |

## New findings register

| ID | Sev | Finding | Where |
|---|---|---|---|
| N-1 | **P2** | `pyproject.toml` dependencies have fully diverged from reality: declares `pandas`, `numpy`, `jupyter` — **zero imports of any of them anywhere** (src, tests, even backtest/) — while omitting the three third-party packages the code actually imports: `pypdf` (filing/PDF paths), `pillow` (`ffa_ocr.py`), `requests` (`rocketchat_api.py`). A fresh `pip install -e .` builds a heavy, wrong environment in which the FFA OCR, Rocket.Chat ingest, and PDF paths `ImportError`. CI is green only because the workflow hand-lists the true deps (`pytest pyyaml openpyxl pillow pypdf requests`) — the packaging metadata and the CI install list are two divergent hand-maintained copies of the same fact. | `pyproject.toml` |
| N-2 | P3 | USD price stored at 2 decimal places quantizes sub-$1 names. 2343 converts HK$3.06 × 0.12759 → stored `0.390`: one HKD tick (0.33%) is invisible and price resolution is ~1.3% — the same order as the ±2pp drift band and larger than 2343's current −3% upside read. First name affected; PANL intake would not be, but any future low-priced HKEX/Oslo line would. Fix: round converted quotes to 4dp (or dynamic significant figures) in `price_refresh.py` and keep 2dp at render time only. | `price_refresh.py:161`, `watchlist.yaml` 2343 |
| N-3 | P3 | PLAN.md is stale at HEAD in a way that could misdirect a fresh agent: it still carries "**PENDING OWNER: baseline ratify** (cause: 2343 onboarding…)" and "the two drift-gate reds at HEAD… clear at ratify" — but that ratify **is** HEAD (`1d3db14`, RATIFY_LOG 16:41Z) and the gate reads 0 UNEXPLAINED. An agent following the CLAUDE.md → PLAN.md startup path could re-ratify (low harm: duplicate log row) or burn a session hunting for reds that no longer exist. The onboarding arc has a recurring last-mile gap: the ratify commit lands, the PLAN pending-marker doesn't get cleared in the same session. | `PLAN.md` ~L164 |
| N-4 | P3 | CI runs only on the daily 12:45 UTC cron + manual dispatch — no `push` trigger. A pushed regression sits invisible to the clean-clone guarantee for up to ~24h, during which the local verification loop is the only gate. The `ci` job costs ~4 minutes; adding `push: branches: [main]` is nearly free. | `.github/workflows/sentinel-lite.yml` |
| N-5 | P3 | The vendored `shipping_harvester` suite — 60 tests covering the parsers that produce the transaction prints anchoring **every mark in the system** — is outside `testpaths` and not run by CI. It passes here (60/60 on Python 3.12), but it runs in practice only when the owner remembers the `.venv310` invocation. A parser regression would surface as bad prints, not a red suite. Fix: third CI job (`pip install -r shipping_harvester/requirements.txt`, run its tests from that directory). | `shipping_harvester/`, CI |
| N-6 | P3 | `ruff` is configured in `pyproject.toml` but not enforced: 57 outstanding violations (23 unused imports F401, 14 empty f-strings F541, 9 ambiguous names E741, 5 E702, 4 unused vars F841 — all cosmetic, 37 auto-fixable, none functional). A `ruff check` CI step or pre-commit hook would hold the line. | src/tests/backtest/scripts |
| N-7 | P3 | The README "460+ tests" claim is accurate only as a floor — actual collection is 600 (580 pass / 16 xfail / 4 skip), a 26% understatement. `test_docs_stay_lean` guards ticker and sector counts strictly but not the test count, which is precisely the number whose rot motivated F-9. Consider asserting a parsed count within a tolerance band. | `README.md`, `tests/test_docs_stay_lean.py` |

## What holds up well (verified, not assumed)

- **Reproducibility is real.** Clean clone → 580 green → full 25-name pipeline → byte-identical markdown outputs and content-identical scorecard JSON, on a Python/pandas stack three years newer than the pinned one. The engine's true dependency surface is tiny (pyyaml, openpyxl, pypdf, pillow, requests + stdlib), which is why it ports so cleanly — the pandas-free design is an unsung robustness asset (and the reason N-1 is only P2, not P0).
- **The governance loop closed the last audit properly.** Every P0/P1 was fixed in code with regression tests, the one owner-judgment item (F-2) resolved through a pre-registered trigger that then *fired in the opposite direction* on Jul-7/8 and was executed at owner go — the discipline survived contact with a reversal. RATIFY_LOG carries 11 dated rows with causes; the Jul-13 accept-all documents per-flip eyeball rationale.
- **Secret hygiene is clean to the bottom.** Env-var pattern with a chmod-600 secrets file, `notify --doctor` perms check, gitignore patterns, no credential-shaped strings in the working tree, and — checked explicitly — no env/token/secret file ever committed across all 297 commits.
- **FX handling for the new listings is sound and auditable.** Yahoo `CUR=X` semantics used correctly (USD→CUR, divide); native price, native currency, and the applied fx rate are all recorded alongside the converted quote. The 2343 static in the watchlist carries the full conversion provenance in its comment. (N-2 is a precision nit on top of a correct design.)
- **The derived Handy-Bulk curve honors its locked identity.** Live `ffa_forward_curve.yaml` Handy-Bulk = Supra-Ultra × 0.90 at every tenor (rounded to $10), matching the §11.7.11 lock; scenario weights sum to exactly 1.000 in all six sectors, with the two 0.0-weight tail scenarios (LNG structural_reset, product structural_decline) sitting exactly where the pending Hormuz re-tilt ruling would move them.
- **The sentinel backstop works from nothing.** `--pure` on this clone flagged today's DHT 6-K landing, the 2343 static price, and the STNG/ASC/SB/2343 earnings windows, and returned rc=1 — the GitHub-issue pager path would have fired.
- **The xfail audit-queue design remains healthy:** all 16 xfails trace to the four provenance queues, none are rotting test debt.

## Residual scope this audit could not check

Launchd job health on the Mac (six plists; last verified 2026-07-02); parsed transaction CSVs vs raw broker PDFs in the harvester cache; FFA OCR output vs source PNGs; the governance repo's `schema_version` assertion on scorecard ingest (required by the F-4 disposition — worth confirming it actually asserts `"2.3"` now); whether the 2343.HK line entered `prices_daily.yaml` on tonight's cron as PLAN expects.

## Suggested disposition order

1. N-1 (ten-minute fix, removes a whole class of fresh-machine failure): rewrite `[project.dependencies]` to the real five, drop jupyter/pandas/numpy, and have CI install via `pip install -e .[dev]` so the two lists can never diverge again.
2. N-4 + N-5 together (one workflow edit): `push` trigger on `ci`, third job for the harvester suite.
3. N-2 before PANL/next sub-$1 intake: 4dp on converted quotes.
4. N-3: clear the PLAN pending-ratify marker; consider adding "clear the PLAN marker" as a step inside `ratify_baseline.sh`'s printed checklist so the last-mile gap can't recur.
5. N-6/N-7 opportunistically.

---

## DISPOSITION (same day, 2026-07-14 — all seven findings closed or accepted)

| ID | Disposition |
|---|---|
| N-1 | **FIXED.** `[project.dependencies]` rewritten to the real five (pyyaml/openpyxl/pypdf/pillow/requests; pandas/numpy/jupyter dropped); CI's ci job now installs `pip install -e ".[dev]"` — the package metadata and CI environment are one fact. |
| N-2 | **FIXED.** Converted quotes stored at 4dp in `price_refresh.py` (native price/currency/fx provenance unchanged; render stays 2dp). The 2343 watchlist static was left at 2dp deliberately — it is superseded by the live feed the same night. |
| N-3 | **FIXED + GUARDED.** PLAN pending-ratify marker cleared (the ratify executed at owner go 16:41Z, before this audit's clone — the marker was the stale artifact, not the ratify); `ratify_baseline.sh` now greps PLAN.md for the marker and prints a warning into its own checklist, so the last-mile gap self-surfaces at the next ratify. |
| N-4 | **FIXED.** `push: branches: [main]` trigger added; the sentinel job carries `if: github.event_name != 'push'` so the pager keeps its daily cadence (per-commit issue churn would break its semantics). |
| N-5 | **FIXED.** Third CI job `harvester`: installs `shipping_harvester/requirements.txt` on 3.12, runs its 60-test suite from its own directory. |
| N-6 | **FIXED (held-line).** The 37 auto-fixables applied (`ruff check --fix`, suite-verified); the 20 legacy remainders (E741/E701/E702/F841 — cosmetic, in working valuation code) accepted via dated `[tool.ruff.lint] ignore` rather than churned; CI now runs `ruff check` so new violations cannot accumulate. |
| N-7 | **FIXED + GUARDED.** README updated to "590+ tests"; new `test_readme_test_count_claim_tracks_the_suite` asserts the claimed floor against the suite's static test-function census (529 defs) within a [defs, 1.25×defs] band — the counter class that motivated F-9 is now fully covered. |

**Residual-scope answers:** the governance consumer (monitor/PROMPT.md §4a) asserts
`schema_version major == 2` with missing-file/wrong-major as a FLAG — the designed
semver contract (minor bumps are additive), confirmed as-designed rather than a gap.
The 2343.HK prices_daily entry lands at tonight's 18:30 cron; the sentinel's
STATIC-FALLBACK lane pages if it doesn't.
