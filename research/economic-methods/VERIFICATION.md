# Verification receipts

All execution used the isolated checkout `/private/tmp/fv-economic-20260922` and
Python 3.9 from the existing producer venv. Governor tests used the isolated sibling
`/private/tmp/portfolio-governance`, with mocked notification and healthcheck paths.

- Producer full suite: **1,021 passed, 4 skipped, 12 expected failures**, one existing
  urllib3/LibreSSL warning. `receipts/producer-suite.log`.
- Governor seam, delivery and quarterly suite: **23 passed**.
  `receipts/governor-tests.log`.
- Following scenario-ledger export and stronger risk propagation assertions:
  **92 passed** in affected scenario, carveout, publication and research tests.
  `receipts/followup-tests.log`.
- Final reference-contract validation and loss/floor cases: **94 passed**; see
  `receipts/final-focused-tests.log` and `receipts/verification.json` for the result.
- Baseline research replay matches all 25 headline FVs and the complete governed
  comparison contract. Ordinary legacy pipeline regeneration also reproduced
  **every per-name scorecard field exactly**; only generation/source metadata changed.
  `results/legacy_regeneration_receipt.json`.
- Reconciliation: 25 names, **zero sanity failures**. APPROX names remain n/a rather
  than being relabelled validated. Its empty isolated previous-drift snapshot says
  first-run; the separate committed drift gate supplies the meaningful drift check.
- Legacy committed drift check: **25 stable, zero unexplained, zero missing**.
- Research identity audit: **3,792 ledger rows**, no cash/depreciation identity failure;
  exact independent NAV invariance, fixed scenario probabilities and unchanged input
  hashes; zero handoff-coherence flags in all nine experiments.
- FFA-only +20% tests cover every name, sector/class map and hybrid sleeve under fixed
  reference snapshots. Separate SB ±10% and vessel-mark-pair rejection tests pass.
- Real committed shadow fixture: publication validation **HELD**, reason
  `economic research is not an accepted production publication`. The checker is
  exercised on explicit shadow envelopes, not an actual accepted research publication.
- Production snapshot preservation: all frozen inputs, outputs and drift baseline,
  accepted pointer and governor review registry were byte-identical before metadata
  landing. Final landing is restricted to review artifacts, navigation and registry;
  no source/input/output determinant is adopted.

The initial baseline suite had two environmental failures: the untracked OCR fixture
was absent in the clone and a sibling governor evidence checkout was missing. Both
were restored locally, then the complete suite passed. The source fixture is now
archived for replay. A final test run caught a reference-validation error-message
ordering mismatch; calendar validation was moved before class-shape validation and
that affected suite was rerun. No expectation or valuation threshold was widened. An unseeded replay also
exposed legacy floating-sum ordering differences at machine precision; the research
launcher now fixes Python's hash seed before evaluation. Numerical gate thresholds
were unchanged. See `receipts/reproducibility.json` for the final repeat-run check.

Commands (run from the isolated producer checkout):

```sh
PYTHONPATH=src /Users/dan_personal/Projects/crude-tanker-fv/.venv/bin/python -m pytest -q
PYTHONPATH=src /Users/dan_personal/Projects/crude-tanker-fv/.venv/bin/python research/economic-methods/regenerate.py
PYTHONPATH=src /Users/dan_personal/Projects/crude-tanker-fv/.venv/bin/python -m crude_tanker_fv.reconcile --all
PYTHONPATH=src /Users/dan_personal/Projects/crude-tanker-fv/.venv/bin/python -m crude_tanker_fv.drift_gate
PYTHONPATH=src /Users/dan_personal/Projects/crude-tanker-fv/.venv/bin/python research/economic-methods/verify.py
```

The study runner never calls publication, landing, SMTP, healthchecks, or baseline
ratification. Publication validation in tests does not publish. The current methods
remain installed in production; rollback requires no economic action.
