"""Crude-subsector edge backtest (freeze-time diagnostic).

Self-contained, separate from ``src/``. MUST NOT import or modify the
valuation core (nav / blend / cycle / dividend_strip / scenarios). The core
is pure over ``CompanyInputs``; this package adds only:

  - vintage_loader : point-in-time signal/price panels with a hard
                     no-look-ahead assertion.
  - returns        : forward (price-only) returns + equal-weight crude
                     market-neutralization.
  - evaluate       : Spearman rank IC, mean-IC t-stat, Newey-West SE.
  - run_test0      : driver — naive -P/NAV IC vs 1q-forward relative return.
  - run_test1      : GATED engine test (designed, not run; see README).

Deliberately dependency-free (Python stdlib only) so it runs in a bare
container with no numpy/pandas/scipy. See backtest/README.md for the
verdict and the data the owner must supply to make Test 0 conclusive.
"""
