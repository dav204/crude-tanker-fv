# Economic-method research

Start with [REVIEW.md](REVIEW.md). This is a frozen, blocked-adoption research package.
No installed automation reads these results and no method is enabled in production.
The implementation lives on local branch `codex/economic-method-review`.

The implementation commit follows the frozen baseline (`3b37f8c`) and preregistration
(`e533134`). `preregistration_hashes.json` is checked before every run; do not rerun
`prepare.py` over the existing freeze. Source changes require a new dated registration.

In an isolated checkout of that branch, with the existing producer venv:

```sh
PYTHONPATH=src /Users/dan_personal/Projects/crude-tanker-fv/.venv/bin/python research/economic-methods/run.py
PYTHONPATH=src /Users/dan_personal/Projects/crude-tanker-fv/.venv/bin/python research/economic-methods/verify.py
PYTHONPATH=src /Users/dan_personal/Projects/crude-tanker-fv/.venv/bin/python research/economic-methods/package.py
```

`run.py` fixes the valuation date and price-freshness clock to the accepted snapshot.
It fixes `PYTHONHASHSEED=0` before evaluation so the legacy engine's unordered class sums also replay deterministically. It never publishes or notifies. The real governor checker runs on shadow envelopes
against the frozen registry. Unknown hybrid cash cases remain null with reasons.
`verify.py` checks identities, unchanged inputs, ordinary drift thresholds and a real
committed research-publication rejection fixture. `package.py` renders the tables.
`regenerate.py` separately exercises the ordinary legacy production generator in the
isolated checkout; it writes ordinary outputs/logs there only.

For the full suite, reproduce the existing environmental fixtures: copy
`frozen/ffa_ocr_curves_test_fixture.json` to the isolated checkout's
`state/ffa_ocr_curves.json`, and place a clone of portfolio-governance at the sibling
path `../portfolio-governance` at the recorded governor commit. No credentials,
notifications or healthcheck configuration is required for the mocked governor tests.

Artifact interfaces: `assumptions.json` version 1; `results/*_handoff.json` retains
schema 2.9 and adds `economic_research.schema_version=economic-research-1`.
`ordinary_common_accounting_eps_v1` is used only for cash-strip EPS. Legacy EPS and
normalized justified-P/NAV earnings retain their labelled pre-depreciation proxy.
The study does not feed the legacy EPS consensus/reporting artifacts.

Ownership: the manually invoked research runner owns only this study directory's
results; the isolated legacy generator owns its usual checkout-local outputs/logs.
There is no scheduled node to register or permission manifest to widen. Production
publication, delivery and governor state ownership are unchanged.

Rollback: stop invoking the research commands; production already uses the old
methods. Keep the branch, committed evidence and previous accepted publication.
A later adoption requires a separate reviewed production change and baseline decision.
