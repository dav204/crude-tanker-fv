# Crude backtest — Test 0 report & verdict

**Date:** 2026-06-14 · **Test:** 0 (naive published P/NAV, no engine) ·
**Metric:** the one pre-registered in `PRE_REGISTRATION.md` (committed before
any number below was computed — see git history, commit a1fd637).

---

## VERDICT (against the pre-registered primary metric): **INCONCLUSIVE**

Mean quarterly cross-sectional Spearman IC of published P/NAV vs 1-quarter-
forward, equal-weight-crude-neutral total return:

> **mean IC = +0.095, t-stat = +0.35, Nq = 6 quarters, 4 names/quarter.**

Against the locked decision rule: not EDGE (needs t ≥ 2.0), not NO-EDGE (the
point estimate is positive, not ≤ 0). It lands in the pre-registered
**INCONCLUSIVE** bucket — a faintly positive, wholly insignificant signal.
**This is the outcome the pre-registration warned was most likely regardless of
whether edge exists, and the power analysis below shows it was essentially
guaranteed by the design, not informative about edge.**

Do **not** read "+0.095, 4-of-6 quarters positive" as encouraging. At this N it
is noise. Do **not** read it as "no edge" either — the test cannot see an edge
of plausible size. Both over-readings are wrong; the honest word is
*inconclusive*.

---

## The numbers

Window: real published Pareto P/NAV exists **2024-08-22 → 2026-06-11**. Universe
with real published P/NAV: **DHT, FRO, ECO, TNK** (NAT prints `na` — Pareto does
not publish its P/NAV — so NAT is excluded from the primary, per pre-reg). Six
non-overlapping forward quarters (2024Q3→Q4 … 2025Q4→2026Q1).

| Signal quarter | n | published P/NAV (DHT/ECO/FRO/TNK) | next-q total return % | EW-crude % | Spearman IC |
|---|---|---|---|---|--:|
| 2024-09-30 | 4 | 0.94 / 1.19 / 1.15 / 0.77 | −13.9 / −33.6 / −36.4 / −31.3 | −28.8 | +0.60 |
| 2024-12-31 | 4 | 0.85 / 0.81 / 0.80 / 0.57 | +14.8 / +5.7 / +6.0 / −3.2 | +5.8 | −0.80 |
| 2025-03-31 | 4 | 1.07 / 0.92 / 0.93 / 0.63 | +4.3 / −0.3 / +11.6 / +12.0 | +6.9 | +0.40 |
| 2025-06-30 | 4 | 1.05 / 0.87 / 0.99 / 0.66 | +10.5 / +34.7 / +38.9 / +21.8 | +26.5 | +0.20 |
| 2025-09-30 | 4 | 1.13 / 1.11 / 1.26 / 0.73 | +2.2 / +15.6 / −4.3 / +5.7 | +4.8 | +0.80 |
| 2025-12-31 | 4 | 1.10 / 1.17 / 1.10 / 0.77 | +53.4 / +53.9 / +64.8 / +37.7 | +52.5 | −0.63 |

Sign convention: positive IC = cheap (low P/NAV) predicted outperformance.

**Benchmarks (pre-specified).**
- **Equal-weight crude** forward quarterly returns ranged **−28.8% to +52.5%**.
  The sector's common move dwarfs intra-sector dispersion — the cross-sectional
  picking the tool aims to do operates on a thin residual after a huge beta.
- **Naive P/NAV** *is* the signal under test here, so "beat naive P/NAV" is the
  identity at Test 0; that bar binds in Test 1 (tool EV% vs this same IC).

**Exploratory (not the verdict; researcher-DOF, reported for completeness):**
- Cheap-minus-rich quarterly spread (long below-median P/NAV, short above):
  **+2.6%/quarter, t = +0.44** — positive, insignificant.
- The signal was "right" (positive IC) in 4 of 6 quarters and badly wrong in 2.
  Suggestive in the most hand-wavy sense; meaningless at N = 6.

---

## Why it is inconclusive: the design is underpowered by the *universe*, not just the window

This is the most important finding, and it is structural:

- A **4-name** cross-section makes the quarterly Spearman IC take only 11
  discrete values (−1.0, −0.8, …, +0.8, +1.0). Its quarter-to-quarter standard
  deviation here is **0.66** — enormous relative to any realistic mean IC.
- Quarters required to reach |t| = 2 at a *true* mean IC of:

  | true IC | quarters needed | ≈ years |
  |--:|--:|--:|
  | 0.05 | ~699 | ~175 |
  | 0.10 | ~175 | ~44 |
  | 0.20 | ~44 | ~11 |
  | 0.30 | ~19 | ~5 |
  | 0.50 | ~7 | ~2 |

  Realistic equity cross-sectional ICs are ~0.03–0.10. Detecting that on a
  4-name universe needs **decades to centuries** of quarterly data. **Extending
  the history (the obvious next move) does not fix this — the binding constraint
  is that there are only four crude names to rank.** A crude-subsector-only,
  rank-IC precondition test is, in effect, not answerable with statistical
  confidence at any feasible sample size.

So "inconclusive" here is not "we need a bit more data." It is "this specific
test cannot resolve the question, and a longer crude-only history won't change
that."

---

## Caveats (locked in the pre-registration, restated)

- **Survivorship.** Universe = today's crude names. Names that delisted or
  failed are absent; any value signal looks better on survivors than it was in
  real time. Bias is upward on any positive finding.
- **Tiny N / narrow universe.** 6 quarters × 4 names. Underpowered by design
  (above).
- **Single vendor each side** — Pareto (signal), Yahoo (returns). No
  cross-vendor validation.
- **No look-ahead** — asserted in the loader and tested (`test_backtest.py`):
  every signal feeding quarter *t* is dated ≤ *t*; a 45-day staleness guard
  drops a name once its feed goes quiet (this is why a stale P/NAV never gets
  carried forward).

---

## What it would take to get a real verdict — and what I need from you

The crude-only rank-IC test is a dead end for *power* reasons. Three honest
ways forward, cheapest first. **None has been run — this is the decision point.**

1. **Widen the cross-section to the full shipping P/NAV panel (cheapest, no new
   data).** The extraction fixes made this run already pulled real published
   P/NAV for **~20 shipping names** (tankers, dry bulk, LNG, LPG, containers:
   DHT, FRO, ECO, TNK, INSW, STNG, HAFN, TRMD, SBLK, GNK, FLNG, GLNG, BWLP,
   LPG, MPCC, …). A 15–20-name cross-section per quarter is **adequately
   powered** and would answer the *real* precondition — "does cheap-on-P/NAV
   predict relative returns in shipping equities at all?" — with the same
   machinery. It is broader than "crude subsector," so it is a different
   (new) pre-registration, but it is the only cheap test that *can* return a
   confident yes/no. **Recommended next step.**
2. **P/B proxy over a longer window (more quarters, lower fidelity).** Yahoo
   fundamentals give book value back ~2020; price/book is the "depreciated-book
   NAV" proxy. It buys time-depth but **not** cross-section width, so for the
   crude-only universe it stays underpowered; it helps only if combined with (1)
   or run as a pooled (name + quarter) panel regression rather than rank-IC.
   Fidelity caveat stands (book ≠ market NAV across the cycle).
3. **Test 1 (the engine) — currently blocked on data.** The valuation core is
   pure and ready, but only **2026-Q1** vintage inputs exist in-repo. Running
   `value_company` as-of past quarters needs historical balance sheets +
   period vessel-mark / FFA / spot-TC vintages, which are not in the repo and
   must be supplied or reconstructed. **What I'd need from you:** for each name
   and quarter to test, the quarter-end balance sheet (cash, debt, leases,
   shares, NB commitments) and the period's market data — or authorization to
   reconstruct from SEC/6-K filings + broker archives. Without it, Test 1 cannot
   run honestly, and I will not fabricate vintages.

**I did not fabricate any data.** Signal = real Pareto prints; returns = real
Yahoo adjusted closes. Where data does not exist (pre-2024 P/NAV, NAT P/NAV,
historical engine vintages), the report says so rather than inventing it.

## Reproduce

```
PYTHONPATH=. .venv/bin/python -m backtest.fetch_prices     # refresh Yahoo cache
PYTHONPATH=. .venv/bin/python -m pytest backtest/test_backtest.py -q
PYTHONPATH=. .venv/bin/python -m backtest.run_test0
```
