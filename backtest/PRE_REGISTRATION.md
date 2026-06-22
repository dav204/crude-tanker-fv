# Crude backtest — PRE-REGISTRATION (locked before any result is computed)

**Committed:** 2026-06-14, before running `evaluate`. Git history is the proof
of order: this file lands in its own commit prior to any IC/return computation.
Nothing below is to be edited after results are seen — if the method has to
change, that is a new, separately-dated amendment with the reason, not a quiet
rewrite.

## The question

Does *cheap-on-P/NAV* predict forward relative returns within the crude
subsector? This is the precondition for the FV tool to be a stock-picker. If a
real, contemporaneous, published P/NAV does not rank forward winners, no amount
of NAV-engine sophistication can — so we test the cheap signal first (Test 0),
and only test the engine (Test 1) if Test 0 is non-zero.

## Universe & period

Names: **DHT, NAT, FRO, ECO, TNK** (the long-listed crude names with real price
history). TEN / CAPT / INSW deferred (too short or too complex). Period: the
window for which a **real published P/NAV** exists in-repo — the Pareto Shipping
Daily extract, **2024-08-22 → 2026-06-09** (~7 calendar quarters). There is NO
published P/NAV in-repo before 2024-08; the brief's 2018–2025 span is not
attainable from repo data (see REPORT data-ask).

## PRIMARY metric (one, locked)

> **Mean quarterly cross-sectional Spearman rank IC between the signal at
> quarter-end `t` and the 1-quarter-forward, equal-weight-crude-neutralized
> total return, averaged over quarters, with a t-stat on the time series of
> quarterly ICs.**

Exact construction:

1. **as-of dates** = calendar quarter-ends (Mar-31 / Jun-30 / Sep-30 / Dec-31).
2. **signal_i(t)** = the most recent Pareto published P/NAV for name *i* with
   `report_date ≤ asof(t)`, **only if** that print is within **45 calendar
   days** before `asof(t)` (staleness guard — this correctly drops a name once
   its feed stops, e.g. ECO after 2025-04; a stale P/NAV is not a
   contemporaneous signal). Otherwise the name-quarter is missing.
3. **total return_i(t→t+1)** = `adjclose_i(last trading day ≤ asof(t+1)) /
   adjclose_i(last trading day ≤ asof(t)) − 1`, using Yahoo adjusted close
   (adjusted close embeds dividends + splits → it is a total-return series).
   Both endpoints must exist or the name-quarter is dropped.
4. **relative return** = `return_i(t→t+1) − mean_j return_j(t→t+1)` over the
   names present at `t` (this is the equal-weight-crude neutralization the brief
   specifies).
5. **IC(t)** = Spearman( −P/NAV_i(t), relative_i(t→t+1) ) across names present.
   Sign convention: **positive IC = cheap (low P/NAV) predicts outperformance**
   (the direction the tool's thesis requires). A quarter is used only if
   **≥ 3 names** are present (a 2-name Spearman is degenerate, ±1).
6. **Primary statistic** = `mean_t IC(t)`; **t-stat** = `mean / (sd / sqrt(Nq))`
   over the Nq usable quarters. Quarters are non-overlapping → the quarterly ICs
   are treated as independent draws; plain t-stat. (Newey-West is used only for
   the exploratory overlapping-window reads below.)

## Benchmarks (pre-specified)

- **Equal-weight crude return** — the return the neutralization removes; reported
  alongside so the signal is judged on *relative* skill, not beta.
- **Naive published P/NAV** — in Test 0 the signal under test *is* naive
  published P/NAV, so "vs naive P/NAV" is the identity; the meaningful
  comparison for Test 0 is **vs zero IC**. The "must beat naive P/NAV" bar binds
  in **Test 1** (tool EV% IC vs this same naive-P/NAV IC).

## Pre-registered decision rule (verdict)

Against the PRIMARY metric:

- **EDGE (precondition met):** mean quarterly IC **> 0** AND **t-stat ≥ 2.0**.
- **NO EDGE:** point estimate near zero or wrong-signed with a reasonably tight
  SE — operationally `mean IC ≤ 0` with `|t| < 2`, i.e. no positive relationship
  detectable and the point estimate not encouraging.
- **INCONCLUSIVE:** a positive point estimate that does not clear t ≥ 2 — i.e.
  suggestive but underpowered. **Given Nq ≈ 7, this is the most likely outcome
  even if a true edge exists**, and we will say so rather than over-claim either
  way. Absence of significance at this N is NOT evidence of absence.

The verdict on the PRIMARY decides the freeze. The secondary/exploratory reads
below inform *what to do next* (extend data, or run Test 1), not the verdict.

## SECONDARY (pre-registered, lower-fidelity, NOT the verdict)

- **P/B proxy over the longest Yahoo-fetchable window** (~2020→2025): identical
  machinery with signal = −(price / book-value-per-share). This is the
  "depreciated-book NAV" proxy the brief sanctioned. **Fidelity caveat, stated
  before seeing it:** book value (depreciated historical cost) diverges from
  market NAV precisely across the shipping cycle, so the P/B-IC may say little
  about whether *P/NAV*-cheapness predicts returns. It buys N (≈20 quarters,
  meaningful t-stat) at the cost of signal fidelity. Reported, flagged, never
  used as the primary verdict.

## EXPLORATORY (researcher degrees of freedom; report, never headline)

Monthly horizon (overlapping → Newey-West SE), per-name time-series, sub-period
splits, NAT included via its APPROX band P/NAV, and a tangible
cheap-minus-rich quarterly spread-return portfolio readout. Any of these that
looks strong is a hypothesis for future pre-registration, not a result.

## Caveats locked up front (not added after)

- **Survivorship:** the universe is *today's* crude names. Names that delisted,
  were acquired at distress, or blew up are absent. A value signal looks better
  on survivors than it was in real time — this biases any positive finding
  upward and cannot be removed with repo data.
- **Tiny N:** ~7 quarters, 3–4 names. The primary is underpowered by
  construction; the t-stat bar is honest but hard to clear.
- **No look-ahead (asserted in code):** the loader asserts every signal row
  feeding `t` has `report_date ≤ asof(t)`; the run aborts otherwise.
- **Single data vendor** for the signal (Pareto) and returns (Yahoo). No
  cross-vendor validation of either.

---

# AMENDMENT 1 — wide shipping panel (2026-06-14, after Test 0 verdict)

Test 0 returned INCONCLUSIVE because a 4-name crude cross-section is
underpowered at any feasible sample (quarterly-IC sd ≈ 0.66; detecting IC 0.05–
0.10 needs decades–centuries). Per owner decision, we widen the universe to the
full shipping P/NAV panel to obtain a **powered** read on the precondition.
This is a NEW pre-registration (different universe), committed before its
results, same discipline. It does not retroactively change Test 0.

**Universe.** All shipping names with real published Pareto P/NAV **and** a
USD listing (returns must be currency-consistent; Yahoo adjusted close, USD).
The USD restriction drops Oslo/EUR-only names (AWILCO, BWLP, DIS, ODFB, SNI,
MPCC) — flagged as a second selection filter, not silently. NAT still excluded
(prints `na`). Each name carries a curated sector label (crude / product /
dry_bulk / lng / lpg), held in code, auditable.

**Why sector-neutral.** Cross-sector P/NAV *levels* are not comparable (LNG and
tanker NAV norms differ — the methodology says so), so a raw cross-sectional
P/NAV rank would partly pick *sectors*, not names. The tool's actual job is
peer-relative (is this name cheap vs its NAV/peers). So the PRIMARY is
sector-neutralized.

**PRIMARY metric (locked).**
> Mean over quarters of the **sector-neutral pooled cross-sectional Spearman
> IC**: for quarter `t`, within each (sector,`t`) cell with ≥2 names, rank names
> by cheapness (−P/NAV) and by 1q-forward total return as fractional in-cell
> ranks; pool all such names across sectors; IC(t) = Spearman(cheap-rank,
> return-rank) across the pooled set. Average IC(t) over non-overlapping
> quarters; t-stat on the quarterly series. Positive IC = cheap predicts
> outperformance vs sector peers.

Signal construction, staleness guard (45d), and the no-look-ahead assertion are
identical to the primary above.

**Decision rule (same thresholds):** EDGE = mean IC > 0 AND t ≥ 2.0;
NO-EDGE = mean IC ≤ 0 with |t| < 2; INCONCLUSIVE otherwise. This verdict, being
adequately powered, is the one that can actually move the freeze.

**SECONDARY (reported, not the verdict):** raw whole-panel per-quarter Spearman
of −P/NAV vs (return − equal-weight-panel return) — powered but cross-sector
confounded.

**EXPLORATORY:** per-sector ICs; sector-neutral cheap-minus-rich spread;
pooled-observation IC with a quarter-block bootstrap SE.

**Caveats (additional to the base set):** survivorship now spans all of
today's shipping names (stronger survivor bias than crude alone); the USD-
listing filter is itself a selection; LNG/LPG sectors are thin (≤2 names) and
contribute little after sector-neutralization; this answers "does cheap-on-
P/NAV predict peer-relative returns in (surviving, USD-listed) shipping," which
is broader than "crude subsector" — it is a precondition read, not a
crude-specific verdict.

---

# AMENDMENT 2 — P/B proxy, long history (2026-06-14, after Amend-1 verdict)

Amend-1 was still INCONCLUSIVE: widening fixed the cross-section but the binding
constraint became TIME (only 6 quarters of real P/NAV; archive starts 2024-08).
Per owner decision, build the sanctioned depreciated-book-NAV proxy to buy
quarters. New pre-registration, committed before its results.

**Signal source decided by data availability (probed before locking):** Yahoo
free fundamentals are too shallow (quarterly book value only to 2025-03, annual
to 2022) — they cannot reach 2018, so they are NOT used. **SEC EDGAR XBRL
companyfacts** (official, free, deep) IS used: us-gaap `StockholdersEquity`
(instant, USD) + `dei:EntityCommonStockSharesOutstanding`, with each fact's
`filed` date used for the no-look-ahead lag (signal at `t` uses only book values
**filed ≤ t** — stricter and more correct than period-end ≤ t, since financials
aren't public until filed).

**Realized universe (probed, locked here before results).** SEC XBRL book value
exists deep + current for **9 names**: crude **TNK, INSW**; dry-bulk **SBLK,
GNK, HSHP**; LNG **GLNG, FLNG**; LPG **LPG, NVGS**. It does NOT exist for the
20-F FPIs **DHT, FRO, ECO, STNG, TRMD, HAFN, CMBT** (no us-gaap XBRL), and FRO's
XBRL stops at 2022. **Consequences, stated up front:** the product sector is
absent (0 names); crude is only 2 names and excludes the canonical pure-plays
DHT/FRO/ECO; the panel is bulk/gas-heavy. History reaches ~2018 (~28 quarters).

**Signal:** P/B = price / book-value-per-share (BVPS = StockholdersEquity /
shares), as known at `t` (filed-date lag). Cheapness = low P/B.

**PRIMARY metric:** identical machinery to Amendment 1 — sector-neutral pooled
quarterly Spearman IC of cheapness (−P/B) vs 1q-forward USD total return, mean
over quarters, t-stat. Same EDGE / NO-EDGE / INCONCLUSIVE thresholds.

**Fidelity caveats locked up front (this is a PROXY, not the verdict on the
tool):**
- **Book ≠ market NAV.** Vessels sit at depreciated historical cost; across the
  cycle market NAV diverges hugely from book (e.g. TNK trades ~2× book but
  ~0.8× NAV). So P/B-cheapness rankings need NOT match P/NAV-cheapness
  rankings; a P/B result is evidence about a *value premium in shipping*, not a
  direct test of the P/NAV tool.
- **Narrow/biased universe** (no product, 2 crude, bulk/gas-heavy) — not a
  crude-subsector verdict.
- **Reporting lag + restatements:** latest-filed value per period-end; the
  filed-date lag means the proxy signal is intrinsically staler than daily P/NAV.
- Survivorship as before, amplified by the longer window.

This is the cheapest powered read available on real data; it speaks to the
*precondition* ("does cheap-on-a-NAV-proxy predict peer-relative shipping
returns at all"), and explicitly NOT to the crude P/NAV tool's edge per se.

---

# AMENDMENT 3 — Sharadar deep-history P/B proxy on the ACTUAL watchlist (2026-06-22)

**Committed before any result is computed** (git order is the proof — this
amendment lands in its own commit prior to writing `loaders_sharadar.py` /
`run_proxy_powered.py` and prior to any IC computation). Same discipline as
Amendments 1–2: locked method, locked decision rule, no post-hoc edits.

**Why a third amendment.** Amendment 2 bought quarters with SEC us-gaap XBRL,
but that source is **blind to the 20-F FPIs** — its realized 9-name panel
*excluded the canonical crude pure-plays DHT/FRO/ECO and the entire product
sector*, leaving a bulk/gas-heavy cross-section that is not the tool's universe.
**Sharadar standardizes the FPI 20-F/6-K filings** (verified offline:
`StockholdersEquity` + `EntityCommonStockSharesOutstanding` populated for all
the FPIs), so for the first time the powered proxy can run on **17 of the 20
actual watchlist names — including all five crude flagships and the full product
sector — over deep history**. This is the Amendment-2 idea on the *right*
universe. It remains a **proxy** (depreciated-cost book, not the engine's NAV);
it tests the *premise*, not the engine's marks.

## Universe (locked)

The 17 watchlist names with Sharadar coverage, curated sector labels held in
code (`backtest/loaders_sharadar.py:SHARADAR_PANEL`, auditable):

- **crude (7):** DHT, FRO, ECO, INSW, TNK, NAT, TEN
- **product (4):** STNG, HAFN, TRMD, ASC
- **dry_bulk (3):** SBLK, GNK, CMDB
- **lng (2):** FLNG, CCEC
- **containerships (1):** GSL — a sector **singleton**, so it enters the raw
  whole-panel secondary only and **never** the sector-neutral primary (cells of
  <2 carry no within-sector information; the existing machinery drops it).

**Dropped:** CAPT, BRUT, MPCC — Oslo-only, no US listing, no Sharadar/SEC filer
record (same exclusion the Amendment-1 USD filter would make). Names enter the
panel in the quarter they begin reporting (HAFN 2023, CMDB 2024, ECO 2022, …),
so the cross-section thickens over time; early quarters are crude-heavy.

## Data + no-look-ahead (locked)

- **Signal — P/B.** BVPS = `StockholdersEquity / EntityCommonStockSharesOutstanding`
  from **Sharadar SF1, dimension ARY (annual)**, read from factor-portfolio's
  committed cache (`~/Projects/factor-portfolio` branch `v2-validation-first`,
  `data/cache/sharadar/sec_<T>.csv`). For each fiscal `period_end` present in
  **both** fields, BVPS is stamped public at `filed = max(equity_filed,
  shares_filed)` — the date both legs were disclosed (strict). P/B =
  `adjclose / BVPS`; **cheap = low P/B**.
- **No-look-ahead (asserted in code, run aborts otherwise).** A signal at `t`
  uses only BVPS with `filed ≤ t` (reusing `loaders.bvps_at`'s `LookaheadError`
  guard) and a period not staler than **550 days** (annual cadence: this carries
  the most-recent annual book across the year incl. a late-filing Q1, and drops a
  name ~18 months after it stops reporting). Price at `t` uses only
  `adjclose` with `date ≤ t`.
- **Returns.** Sharadar SEP `adjclose` (= `closeadj`, split+dividend adjusted →
  a total-return series, same convention as the Yahoo `adjclose` the existing
  loaders use), uniform across all 17 names (single vendor for both legs — a
  caveat, below). 1q-forward total return = `adjclose(≤t+1) / adjclose(≤t) − 1`.

## Window (locked)

Calendar quarter-ends from **2008-01-01** through the last cached price date. A
quarter is **usable** iff it has **≥4 pooled names** in sector cells of ≥2
(identical filter to `run_proxy.py`). The realized usable-quarter count Nq is
data-determined and reported with the result; on the deep panel it is expected
to be large enough to be **powered against a moderate within-sector edge
(IC ≈ 0.15–0.20)**, the gain over Amendment 2 that motivates this amendment.

## PRIMARY metric (one, locked — identical machinery to Amendments 1–2)

> Mean over usable quarters of the **sector-neutral pooled cross-sectional
> Spearman IC**: within each (sector, `t`) cell of ≥2 names, average-rank by
> cheapness (−P/B) and by 1q-forward total return, center each rank by the cell
> mean, pool across sectors, take the correlation of the pooled centered ranks.
> Average that quarterly IC over **non-overlapping** quarters; t-stat on the
> quarterly IC series (`evaluate_wide.wide_quarter_ic` + `mean_t`, reused
> unchanged). Positive IC = cheap predicts peer-relative outperformance.

## Pre-registered decision rule (verdict)

- **EDGE (premise supported):** mean IC **> 0** AND **t-stat ≥ 2.0**.
- **NO-EDGE:** mean IC **≤ 0** with **|t| < 2** (no positive relationship, point
  estimate not encouraging) — evidence *against* a tradeable value premium in
  this universe.
- **INCONCLUSIVE:** a positive point estimate that does not clear t ≥ 2.

This is **adequately powered by construction**, so unlike Amendments 0–1 the
INCONCLUSIVE escape is not the pre-stated expectation — a genuine null here is
informative. The verdict updates the project's recorded **ex-post evidence
status** (LIMITATIONS §1 / README "no demonstrated ex-post cross-sectional edge")
and calibrates how much to trust **cheapness as a signal family** — it does NOT
by itself validate or refute the engine's specific P/NAV marks (the deferred
*powered engine EV% test* is the only thing that can, per
`outputs/test1_data_feasibility_memo_2026-06-22.md`).

## SECONDARY (pre-registered, reported, NOT the verdict)

- **Raw whole-panel IC** — per-quarter Spearman of −P/B vs (return − equal-weight
  panel return), pooled across all 17 incl. GSL; cross-sector confounded.
- **Quarter-block bootstrap 95% CI** on the primary mean IC: resample the
  quarterly IC series in **non-overlapping blocks of 4 quarters**, **B = 10000**
  draws, **seed = 20260622** (all locked here). Reported alongside the t-stat as
  a distribution-free robustness check on the SE.

## EXPLORATORY (researcher DoF; report, never headline)

Per-sector ICs; sector-neutral cheap-minus-rich spread portfolio; split-half
(early/late) stability; the same read with prices sourced from the cached Yahoo
`adjclose` (cross-vendor sanity for the 12 names that have both). Any of these
that looks strong is a hypothesis for future pre-registration, not a result.

## Fidelity caveats (locked up front — this is a PROXY, not the engine verdict)

- **Book ≠ market NAV — the load-bearing caveat.** Vessels sit at depreciated
  historical cost; across the cycle market NAV diverges from book (a name can
  trade ~2× book yet ~0.8× NAV). So P/B-cheapness rankings need not match
  P/NAV-cheapness rankings: a result here is evidence about a **value premium in
  shipping**, not about the engine's NAV marks.
- **Annual book leg.** BVPS updates ~annually (ARY), so within a calendar year
  the four quarterly P/B signals for a name move only via **price**. Standard for
  an annual-fundamental value test, but it means the signal is part valuation,
  part price-reversal — flagged, not the verdict.
- **Survivorship.** The universe is *today's* 17 names; deep history amplifies the
  survivor bias (delisted/distressed shipping names are absent), biasing any
  positive finding upward. Cannot be removed with this data.
- **Single vendor, both legs.** Sharadar supplies fundamentals *and* prices here;
  no cross-vendor validation (the Yahoo-price exploratory read partly mitigates).
- **Restatements / reporting lag.** Latest-known-at-`t` book via filed-date lag;
  the proxy is intrinsically staler than a daily P/NAV.
