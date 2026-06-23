# Test 1 vintages

Historical point-in-time input snapshots consumed by `backtest/run_engine_test1.py`.
One directory per as-of quarter, e.g. `2024-Q1/`, each a partial mirror of the
live `inputs/` tree. **Format and per-component source/no-look-ahead rules:
`backtest/DATA_CONTRACT_TEST1.md`.** Method + decision rule:
`backtest/PRE_REGISTRATION_TEST1.md`.

Empty until the free-broker-weekly backfill runs (env-gated on a 3.10+
`shipping_harvester`). With no vintage dirs present the harness reports what to
populate and exits cleanly.
