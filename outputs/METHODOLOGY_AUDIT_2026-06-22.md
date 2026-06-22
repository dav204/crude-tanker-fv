# Methodology audit — how sound is the Tanker FV tool?

**Date:** 2026-06-22. **Scope:** the full valuation methodology (METHODOLOGY.md, ~2,970 lines)
and the engine (`src/crude_tanker_fv/`, 20 names / 5 sectors / 286 tests green).
**Method:** first-hand read of the core engine (`nav`, `blend`, `dividend_strip`,
`marks`, `vessel_values`, `cycle`, `schemas`) + six adversarial read-only sub-audits
(architecture, marks, strip, overlays, validation/epistemics, code-vs-doc). The four
highest-leverage findings were re-verified directly against the files (flagged ✓-verified).

---

## Bottom line

**Conceptually sound, honestly documented, conservatively built — but it materially
over-claims its epistemic standing, and it carries a handful of concrete, fixable defects.**

The design (independent NAV from per-vessel age-curve marks + a forward dividend strip,
blended by cycle position) is the right shape for cyclical shipping equities, and the
project's documentation/process discipline is unusually good. Its real value is as an
**auditable, structured second opinion** that forces explicit reasoning about cycle
position, asset marks, and *why* a name's price differs from its value.

What it is **not**: an independently-validated signal. Every validation gate is defined
relative to one broker's (Pareto) NAV; ~76% of the transaction marks are mined from that
same broker; the "wide spreads are features" doctrine makes the marks effectively
non-falsifiable; and the tool has **never demonstrated a correct ex-post call** (the one
powered backtest returned a null, since reframed). Treat outputs as well-reasoned
hypotheses with error bands far wider than the point estimates imply — not as validated
buy/sell signals. The tool's own LIMITATIONS §6 says essentially this; on the evidence it
is right to.

**Verdict by use case:**
- *Per-name "is this cheap, and why" read* → **sound and genuinely useful**, within wide error bands.
- *Cross-sector cheapness ranking / pair trades* → **unsound as built** (incommensurable cycle anchors).
- *Mechanical signal you size positions off* → **not validated; do not use that way.**

---

## What's genuinely strong (independently affirmed by every sub-audit)

1. **Conservative by construction, in the right places.** Terminal locked at 1.0× (not >1),
   transaction-anchored marks that sit *below* broker, the new newbuild time-to-delivery PV
   discount, and a vessel-value clamp all resist the classic failure mode of cyclical
   valuation (extrapolating the peak). `dividend_strip.py:46`, `nav.py:31`, `transactions.py`.
2. **Per-name auditability is real and is the tool's best feature.** Every name has a decision
   log, a §6 methodology entry, and a documented `k_broker` with a stated thesis. Any FV
   traces to its marks, weights, and balance sheet. More transparent than a black-box score.
3. **Honest self-documentation.** METHODOLOGY §9 item 9 openly retracts an earlier circular
   validation ("the DHT-pricing-close-to-broker observation did NOT validate against
   transaction reality"); the backtest was pre-registered (git-verifiable) before results;
   LIMITATIONS §5/§6 state plainly that no ex-post signal validation exists.
4. **Process discipline that demonstrably works.** The no-back-solve rule was enforced (SBLK
   incident caught and logged); the SANITY gate caught real bugs (BRUT +116%, TEN $44 price,
   TEN missing-Suezmax miscount); cross-foot test machine-enforces manifest totals; 286 tests
   green with **high code-vs-doc fidelity** — the engine computes what the docs describe.

---

## Weaknesses, by theme and severity

### A. Epistemic — the "independence" claim is overstated  *(CRITICAL — structural, manage don't "fix")*

- Every validation gate (Sanity ±50%, one-time calibration-lock ±5/10%, drift >2pp) is
  defined **relative to a Pareto-derived broker NAV** (`reconcile.py:133`, `broker_nav =
  price / consensus_pnav`). The marks the gates check are themselves anchored to prints
  **mostly mined from the same broker** (per-class single-source share: MR 90%, Cape 88%,
  Supra-Ultra 86%, LR2 82%, Pana 80%; lower for crude). So the "independent" diagnostic and
  the calibration target share a source. The "wide spreads are features" doctrine means *no*
  spread can falsify a mark — agreement validates, disagreement is "the call." This is a
  documented *doctrine*, not an architectural independence.
- **No ongoing accuracy gate and no ex-post validation.** Calibration-lock is one-time at
  sector launch; drift is a soft alert against a **gitignored** baseline (`state/last_run`,
  no committed history). Between launch and forever, only the ±50% SANITY floor constrains
  accuracy — a name can be 40% wrong and pass. There is zero evidence any BUY/SELL has been
  right ex-post (LIMITATIONS §5; no test references forward returns).
- **The one powered backtest was a null, then reframed.** Amendment-2 (P/B proxy, N_q=31)
  returned a clean sector-neutral null (t=−0.42); the project's own REPORT calls it "meaningful
  evidence against the tool functioning as a cross-sectional stock-picker," then demotes the
  whole exercise to "expected small-sample, a recorded diagnostic." The reframing is *half*
  honest (a 4-name crude-only IC genuinely can't be powered; absence of significance ≠ no edge)
  and *half* motivated (it leans on the underpowered tests to dilute the one powered null).
  **No live falsification test currently exists** — Test 1 (the engine's own EV% predicting
  forward relative returns) was never run (data-blocked).

> Honest framing for a position-taker: your basis for trust is (1) a fully auditable per-name
> NAV build you can inspect line-by-line, and (2) rough agreement with — or a documented,
> reasoned divergence from — Pareto. That is a legitimate *second opinion*; it is not evidence
> the tool is *right*.

### B. Statistical foundation of the marks is thinner than claimed  *(HIGH)*

- **Load-bearing anchors are extrapolated.** The transaction fit runs on the age window [3,17]
  and is read off at ages 5 and 10, but prints cluster *old*: **LR2 has 11 in-window prints,
  none younger than age 10** (age-5 anchor is pure extrapolation); **Pana has 5 prints
  (eff. N≈3.5), none at age 5**; **Aframax 13 prints, 8 of them age 14–17**. A negative-slope
  line through old-age prints sets the age-5 value that modern fleets depend on, with unknown
  error sign. (`transactions.py:165-214`; per-class counts from `transaction_anchor_comparison.md`.)
- **Duplicate prints inflate effective N** (exact date/age/price triples: Cape ~4, MR ~5,
  LR2 ~3), letting a single en-bloc deal double-weight a thin WLS — worst where N is smallest.
- ✓-verified: **the "uniform k_broker ~1.12–1.14 / band 1.05–1.25" validation does not hold
  at live prices.** The live sweep shows **DHT 1.30 and FRO 1.27 — above the 1.25 ceiling** —
  ECO 1.20, INSW 1.64. By the tool's own two-regime rule, the canonical single-class validator
  (DHT) currently sits *outside* its "mark-validated" band. The `test_marks` pin (`uniformity
  < 0.05`) passes on fixtures while live reality is a ~0.10 spread. The band is a vintage-fit
  narrative, not a live invariant. (`marks.py:33-41`, `outputs/broker_nav_sweep.md`.)
- **The 11% newbuild PV-discount rate is borrowed, not derived** (`nav.py:31`, "matches the
  11% strip rate," which is itself "chosen heuristically," §9.5). It is now *decisive*: BRUT
  swings +116% (FAIL) → +30.6% (OK) on this one un-calibrated constant; on a 100%-newbuild
  book ±2% on the rate is unbounded.

### C. Cycle-blend fragility  *(HIGH)*

- ✓-verified: **dual-source cycle anchor — a live data-integrity bug.** Aframax's "10-year
  mean" is **27,600** in `historical_tce_means.yaml` (the per-name FV path, `cycle.py` /
  `pipeline.py`) but **36,483** in `scenario_inputs.yaml:380` (the scenario path) — a 32%
  discrepancy for the same class (VLCC and Suezmax agree across both). Every Aframax-exposed
  name (TNK, TEN, INSW, HAFN, STNG) gets its cycle position computed two different ways on two
  output surfaces, and the gap can straddle a band boundary. Looks like an un-reconciled edit.
- **The step-band map is discontinuous and its breakpoints are unjustified** (`cycle.py:32-38`).
  A ratio of 1.49 vs 1.51 swings `w_nav` 0.60→0.70 — a discrete FV jump from a rounding-error
  TC move. The breakpoints (1.5/1.2/0.8/0.5) and weight pairs (0.70/0.30 … 0.30/0.70) have **no
  empirical derivation** — round numbers. And in the *current* deep-peak regime (crude ratios
  ~2.0–2.8×) every crude name pins at exactly 0.70/0.30 regardless, so the framework has no
  resolution where it's actually operating; the level of the weights is pure assertion.
  (§9 item 1 concedes step-vs-logistic is unresolved but ships the step.)
- **Cross-sector comparability is broken; the MIXED-ANCHOR-BASIS flag is a band-aid.** Three
  non-composable denominators — `tc_10yr_mean`, `archive_22mo_median` (dry bulk; doc admits
  *elevated*), `fy_calendar_avg` (containers; doc admits *boom-tilted*). A dry-bulk "1.4×" and
  a crude "1.1×" aren't on the same scale, yet the **pair-trade sheet still emits cross-sector
  pairs** (tagged, but emitted). For dry bulk the bias is directional and known (elevated
  anchor → understated ratio → too much `w_earn` at a possible peak) — a valuation error, not
  just a labeling nuisance. (`scenarios.py:209-269, 668-697`, §10.)

### D. Strip / terminal — doc claims mechanisms the engine doesn't implement  *(HIGH)*

- ✓-verified: **the terminal is NOT depleted by dividends, and does NOT mean-revert** —
  contradicting the docs. METHODOLOGY:2115 says "the terminal NAV at q9 is **depleted by the
  dividends paid out**"; :824 says "the model assumes **mean reversion in the terminal value**."
  Code (`_terminal_nav_per_share`, `dividend_strip.py:142-159`) holds the balance sheet
  **constant** and only ages the hulls — no cash depletion, no price-level reversion.
  - *Nuance (correcting the sub-audit's "double-count" framing):* for a ~100%-payout-of-earnings
    name this is roughly self-consistent (NAV embeds future earnings; strip = near-term earnings
    + aged-NAV terminal ≈ NAV), so it is **not** a naive same-dollars-twice error. The real
    consequences are (i) a genuine **doc-vs-code contradiction**, and (ii) **peak-protection is
    weaker than documented**: at a peak both legs ride the elevated marks (terminal price level
    is held flat, only depreciated), so the blend's claimed mean-reverting safety (§2.2/§10) is
    not delivered by the engine — protection comes *only* from `w_earn` down-weighting + the
    conservative marks. The §12 "value extraction / NAV-floor" narrative rests on a depletion
    mechanism the code doesn't have.
- **The terminal is ~half the strip's value (47–52% for high-payout names; 78% for low-payout
  FLNG)** and ≈ aged NAV — so the "two independent lenses" overlap more than the §2.1 framing
  implies; a mark error contaminates both legs, not just `w_nav`.
- **Horizon truncation:** the 8-quarter strip drops contracted charter premium/discount past q8
  for any non-container name with multi-year coverage; the "12q vs 10q" interpretation is still
  flagged "pending owner ratification" (§11.8.6.4).

### E. Judgmental overlays — auditable in intent, anchored/unenforced at the edges  *(MEDIUM)*

- **The §15 governance haircut is anchored at 30%, not independently derived per name.** TEN
  was sized to a VIE-implied ~36% (a real external anchor); CMDB was then set "TEN-equivalent"
  (CLAUDE.md changelog verbatim) with **no external anchor**, and the post-hoc capitalized-fee
  calc ($28M/yr ÷ 10–12%) is wide enough (≈25–45%) to ratify any round figure. Two names landing
  on an identical 0.30 is the tell; a third will likely "come out around 30%" too. The
  application point itself is correct (blend NAV term + strip terminal, **not** `compute_nav` —
  ✓ verified in `blend.py:45`, `nav.py:67`), which keeps the asset-side k_broker diagnostic clean.
- ✓-verified: **the §16 overlay ledger is documentation, not a control.** Nothing imports
  `overlay_ledger`; nothing reads `overlays.yaml` except the standalone renderer. The "an
  overlay is ACTIVE only when its ledger row exists" discipline is convention-only — for §15 the
  row auto-populates faithfully, but every other overlay type (§12, §14.4) is a hand-maintained
  markdown file no automated check reconciles.
- **§12 "treat tool FV as a NAV floor" is a one-way bullish escape hatch.** It fires precisely
  when the tool says TRIM a high-payout name and instructs you not to act on the signal — with
  no quantitative trigger and no symmetric "when would §12 be wrong" condition. Combined with
  §13/§14 (also overwhelmingly "direction: up"), the overlay layer has a structural long bias,
  and there is no §14.4-style double-count warning guarding §12 against the `w_earn` peak
  down-weight it partly duplicates.
- **Report presentation bug:** for §15 names the printed blend line shows `w_nav × raw_NAV +
  w_earn × strip = FV_post-haircut`, which doesn't foot (the FV uses haircut NAV). Math is right;
  the surface meant to make the overlay legible is internally contradictory. (`report.py:196-198`.)

### F. Data staleness / proxy exposure  *(MEDIUM)*

- **7 of 20 names (35%) are APPROX-anchored** with no real broker NAV: NAT/ASC/CCEC (no Pareto
  coverage), TEN (VIE-stale), CMDB (P/BV proxy), MPCC (company-implied NAV ~11 months stale),
  GSL (depreciated-cost P/B, self-flagged "WEAK"). For these, "validation" is partly circular
  against a number the tool helped construct.
- **Two of five sectors rest on stale anchors:** the containership cycle anchors/marks are frozen
  since 2026-04-01 (~12 weeks, MB feed stopped, LIMITATIONS §3); the whole watchlist
  `consensus_pnav` vintage is 2026-06-04.

### G. Minor code-rigor gaps  *(LOW)*

- **Crude scenario weights are not value-pinned** — only sum-to-1 is tested; LNG/product weights
  *are* individually pinned. A silent edit to a crude weight that preserves the sum passes green,
  so the "Crude Set A locked weights" claim is only partly machine-enforced. (`test_scenarios.py`.)
- **Silent class-drop in the market-data loader** (`loaders.py:195-201`): a partially-null FFA
  curve is dropped entirely rather than flagged, masking a data-entry error as "class not covered."
- **Two decoupled `0.11` constants** (`nav.py:31`, `dividend_strip.py:44`) the comments claim are
  linked but aren't — tuning one silently breaks the documented intent.
- Degenerate empty-fleet path returns a silent trough-band rather than raising (low real-world risk).

---

## Recommended actions

**Concrete bugs — cheap, unambiguous, fix soon:**
1. Reconcile the Aframax 10-year-mean (27,600 vs 36,483) to a single source of truth; add a test
   asserting `historical_tce_means` and each sector's `ten_year_mean` agree per class. *(C)*
2. Resolve the terminal doc-vs-code contradiction: either implement dividend-depletion / a
   mean-reverting terminal, or correct METHODOLOGY:2115 and :824 to describe what the engine does
   (age-only, level-flat) and move the peak-protection claim onto `w_earn` + conservative marks. *(D)*
3. Value-pin the crude scenario weights like LNG/product. *(G)*
4. Fix the §15 report blend line to print effective (post-haircut) NAV, or show both terms. *(E)*
5. Re-derive or restate the "uniform k_broker" band against live output, or pin the test to a
   declared vintage so the fixture pin can't read as a live invariant. *(B)*

**Structural limits — manage, don't pretend to fix:**
6. Stop presenting one-time calibration-lock hit-rates (1/2, N/A-by-construction) as evidence of
   accuracy; they're n=2. Commit the drift baseline so drift has a real history.
7. Either build *one* genuine ex-post test (engine EV% vs forward relative returns, even on the
   ~6 quarters available) or state in the headline docs that the tool is unvalidated ex-post and
   is a hypothesis-generator. Don't let the backtest null be quietly demoted without a successor test.
8. Independently size each §15 haircut (or adopt an explicit rule that maps observable fee-load /
   payout / control to a discount), so the next case isn't anchored to 30% by default.
9. Suppress cross-sector pair-trades until the anchor bases are made commensurable, or convert all
   sectors to a common long-run-mean basis (the deferred "Q3" fix).

**None of these undermine the core design.** They tighten a fundamentally reasonable framework and,
more importantly, right-size the *confidence* attached to its outputs.
