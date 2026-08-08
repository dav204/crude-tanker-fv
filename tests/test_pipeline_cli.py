"""CLI entry-point guards (audit 2026-07-02, F-6).

A bogus quarter used to run the whole pipeline: every name skipped on missing
balance-sheet files, scenarios/xrefs still executed, and state/last_run.json
overwritten + decisions/*.md touched. `--help` was a valid quarter.
"""

import pytest

from crude_tanker_fv import pipeline


@pytest.mark.parametrize("arg", ["--help", "2026-Q5", "2026Q1", "help", "26-Q1"])
def test_main_rejects_non_quarter_arg(monkeypatch, arg):
    monkeypatch.setattr(pipeline.sys, "argv", ["pipeline", arg])
    with pytest.raises(SystemExit) as exc:
        pipeline.main()
    assert exc.value.code == 2


def test_main_aborts_before_state_writes_when_no_reports(monkeypatch):
    """A valid-format quarter with no populated inputs must stop before the
    scenario/xref/delta stages (which write state and decision logs)."""
    from crude_tanker_fv import loaders

    monkeypatch.setattr(pipeline.sys, "argv", ["pipeline", "2031-Q4"])
    # Stub the pair-coherence preflight — this test targets the LATER
    # zero-report abort; the preflight has its own coverage in
    # test_quarter_coherence (and correctly refuses 2031-Q4 on the real tree
    # whenever staged future sheets are present).
    monkeypatch.setattr(loaders, "preflight_pair_coherence", lambda q, *a, **k: [])
    monkeypatch.setattr(pipeline, "run_watchlist", lambda quarter, live_prices: [])

    def _must_not_run(*a, **k):
        raise AssertionError("pipeline continued past the zero-report abort")

    monkeypatch.setattr(pipeline, "run_scenarios_watchlist", _must_not_run)
    monkeypatch.setattr(pipeline, "_run_delta_and_decision_log", _must_not_run)
    with pytest.raises(SystemExit) as exc:
        pipeline.main()
    assert exc.value.code == 1


def test_main_preflight_refuses_a_torn_pair_before_any_writes(monkeypatch):
    """The all-names preflight (2026-08-08): ANY manifest↔sheet vintage
    mismatch refuses the run before run_watchlist's write loop can start —
    the in-loader guard alone would abort MID-loop and tear outputs/."""
    from crude_tanker_fv import loaders

    monkeypatch.setattr(pipeline.sys, "argv", ["pipeline", "2026-Q1"])
    monkeypatch.setattr(loaders, "preflight_pair_coherence",
                        lambda q, *a, **k: ["X: manifest as-of A vs vintage B"])

    def _must_not_run(*a, **k):
        raise AssertionError("pipeline ran past a failed pair-coherence preflight")

    monkeypatch.setattr(pipeline, "run_watchlist", _must_not_run)
    with pytest.raises(SystemExit) as exc:
        pipeline.main()
    assert exc.value.code == 2
