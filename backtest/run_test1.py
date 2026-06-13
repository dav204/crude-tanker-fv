"""Test 1 (engine) — GATED, designed but NOT run.

Gate (from PRE_REGISTRATION): runs ONLY if Test 0's naive −P/NAV IC is
non-zero and trustworthy. Test 0 returned INCONCLUSIVE (data-insufficient),
so the gate is shut. It also cannot execute in this container (no
numpy/pandas/scipy, no .venv), and the point-in-time fundamentals it needs
(historical fleet/balance-sheet vintages) do not exist on disk — only
2026-Q1 does.

Design, when the gate opens and PIT inputs exist (kept here so the
scaffolding is complete and honest about what Test 1 would do):

  for each quarter t in the backtest window:
      ci = load_vintage_company_inputs(name, t)        # PIT CompanyInputs
      assert no field in `ci` is dated after cutoff(t)  # no look-ahead
      rep = value_company(name, quarter=t, price=price_at(t), ...)
      signal[t][name] = rep.ev_pct                      # tool EV% signal
  ic_tool  = mean quarterly Spearman(signal_EVpct, fwd_market_neutral_return)
  ic_naive = mean quarterly Spearman(-pnav,        fwd_market_neutral_return)
  VERDICT: the tool earns its keep only if ic_tool reliably exceeds ic_naive.

This module must import the valuation core READ-ONLY (it values; it never
modifies nav/blend/cycle/dividend_strip/scenarios). It is intentionally a
stub until the gate opens.
"""

from __future__ import annotations

GATE_OPEN = False  # set True only when Test 0 returns a trustworthy non-zero IC


def main() -> None:
    raise SystemExit(
        "Test 1 is GATED and not run: Test 0 returned INCONCLUSIVE "
        "(data-insufficient), so the precondition fails. Test 1 also "
        "requires point-in-time CompanyInputs (historical fleet/balance-sheet "
        "vintages) that are not on disk, plus numpy/pandas/scipy + a .venv "
        "absent from this container. See backtest/README.md and "
        "outputs/backtest_test0_report.md."
    )


if __name__ == "__main__":
    main()
