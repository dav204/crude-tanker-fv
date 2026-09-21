# TEN — 2026-Q2 pair landed, and the two blockers ruled (2026-09-21)

Owner request, same day: *"resolve the two blockers on the TEN 2026-Q2 pair and promote it to live
… I am asking for those two to be ruled and the pair promoted — not for a particular answer. If the
honest outcome is that TEN still cannot be valued, say so and I will retire the candidate."*

Ruling: **TEN is computable, and the pair is landed.** But the promotion does **not** clear the
governance sizing gate, and that — not either blocker — is the honest reason to reconsider the
candidate. See §4.

---

## 1. BLOCKER 1 — `shuttle_contracted_book`: RESOLVED, and the gap is narrower than recorded

**The extension rate is $55,000/day.** Not an APPROX any more. It is derived from the issuer's own
non-cancelable minimum-future-charter-revenue schedule ("Charters-out"), differenced across two
statutory filings that were both already on disk:

| source | 2029 | 2030 | total |
|---|---|---|---|
| H1-2026 6-K Note 12 (`0001193125-26-394366`) | 143,169 | 135,684 | 1,535,014 |
| FY2025 20-F Note 12 (`ten_20f_fy2025.htm`) | 103,019 | 95,534 | 1,521,163 |
| delta | **+40,150** | **+40,150** | |

40,150,000 / 2 vessels / 365 days = **$55,000.00/day, exactly.** Three independent closures:

- the 2029 and 2030 deltas are exactly 730 vessel-days each and the 2031-2038 delta (+33,385) is
  exactly 607 vessel-days — all integers at $55,000, none at $60,000;
- 2 × 5 × 365.25 × $55,000 = $200.9M, matching the issuer's "more than $200 million in gross
  revenues" (Q1 ex-99.1) where $60,000 would give $219M;
- the 607 firm days expire Oct/Nov-2031, three of the "up to five" years, and 3/5 of $200.9M
  matches the schedule's firm total.

**Structural vs resolvable — the distinction the record had collapsed.** Two different things were
being carried as one:

- **RESOLVABLE, and now resolved: the contracted cash flows.** The issuer discloses this schedule in
  every 6-K and 20-F. It is a repeatable method, not a one-off — the same H1 release prices Anfield
  DP's 10-year employment at "approach $500 million", i.e. ≈$68.4k/day over 20 × 365.25, which is how
  that hull should be struck when it joins the book at Q3.
- **STRUCTURAL, permanent, and not to be re-litigated quarterly: the shuttle ASSET MARK.** There is
  no DP2/shuttle class in `vessel_value_curves.yaml`, no spot rate and no FFA. A sweep of 25 Pareto
  dailies and 12 MB tanker weeklies returns **zero** hits for "DP2" and **zero** for "Tsakos"; the
  five "shuttle" hits are Hormuz STS narrative. No source this repo can reach will mark these hulls.
  `LIMITATIONS.md` §2 already drew this line correctly and should now be the only place it lives.

**Two sized corrections, carried KNOWINGLY rather than silently fixed.** The figure below is not yet
re-struck (re-striking a $453.1M hand-computed NPV is its own change with its own gate):

| | overstatement |
|---|---|
| rate: $60,000 carried vs $55,000 derived | +$10.6M = +$0.35/sh |
| strike: as-of 2026-03-31, not re-struck at 6/30 | +$4.78M = +$0.159/sh |
| **combined** | **≈ +$15.4M ≈ +$0.51/sh, one-directional** |

That is ~14% of this pair's entire +$3.75/sh NAV advance. Not gate-moving (§4), but measured.

**A claim of record is struck.** The Q1 sheet and `LIMITATIONS.md` both assert this convention
"underweights the extension value, leaving upside if the disclosure resolves favorably". That is
**backwards**. The error is an overstatement, and the realised DP2 Suezmax TCE the 6-K prints
(H1-26 $52,089/day) is *below* the book's implied rates, not above.

**The "not honestly computable" language does not apply.** `ten_log.md` attaches it to revisit
criterion 1, a DP2 handling decision, satisfied 2026-06-05 when §11.6 was adopted;
`LIMITATIONS.md` records the architectural blocker as methodologically closed. Quoting it today
would be citing a dead rule.

**Why the shadow missed all of this.** It declared the 1.3MB inline-XBRL exhibit "UNREADABLE by the
Read tool" and worked from EDGAR R-renderings that are not on disk. A 12-line tag-stripper renders
it as ~5,100 lines of text, and the Charters-out schedule sits five lines below the $2,233,409 the
shadow *did* cite from that same note. This is CLAUDE.md's "absence isn't evidence" firing exactly
as written: a parser dropped the field and the absence was scored as data.

---

## 2. BLOCKER 2 — the $2,233,409 commitment: fork opened, recommending HOLD

The figure verifies to the dollar (Note 12: twenty hulls, legs 228,339 / 723,029 / 1,127,374 /
154,667, summing exactly; advances 470,050 at R2). $2,233,409K / 30,127,603 sh = **$74.13/sh** of
gross obligation this NAV does not net. TEN is **out** of `NAV_FIGURE_ESTIMATE_QUEUE`, so the §9.6
gate is procedurally open.

**What blocks netting is the asset half, not procedure.** §9.6 is delivered market LESS commitment —
both legs. Ten of the twenty hulls are DP2 shuttles, **62% of the $2,413M priced program**, and
there is no shuttle class to mark them on. So every executable variant books the obligation without
its asset:

| branch | ΔNAV/sh | NAV/sh | vs broker |
|---|---|---|---|
| naive commitment-net | −74.13 | 17.78 | −86.0% **SANITY FAIL** |
| on-curve, markable hulls only | −53.18 | 38.73 | −69.5% **SANITY FAIL** |
| on-curve at contract price, PV'd | −22.82 | 69.09 | −45.6% |
| same, undiscounted | −9.64 | — | — |

The last line is the tell: −$9.64 is *exactly* the unpriced-20th-hull residual, so at a zero discount
rate advances-only **is** contract-value-net. Holding is not ignoring the obligation; it is netting
it 1:1 against the asset it buys. The residual honest gap is time value (~$11.00/sh of PV asymmetry)
plus the contract-vs-market spread on hulls that cannot be marked — methodology work, not a sheet
flip. Separately, ~71% of the remaining commitment is already matched by arranged undrawn senior
secured bank loans (20-F: $1.403bn).

**All four branches cross the governance sizing gate.** `ev_pct_family_min` falls below the +5 BUY
edge at ΔNAV −$3.60/sh and sign-flips to conviction-zero at −$7.51/sh. There is no netting variant
that leaves the sizing input intact.

**So the fork recommends HOLD — and that choice is load-bearing, because silence executes.** Under
the 2026-09-10 policy a judgment fork runs at its recommendation after three business days. TEN has
**no SANITY gate** (§3) to catch a −$74/sh execution. Registering "net it" would let three days of
inattention run that unattended, against the standing "a wrong sheet is far worse than a late one".
Row `ten_commitments_convention`, opened 2026-09-21, `execute_after` 2026-09-24, status open. TEN
stays in `OFF_CONVENTION_QUEUE` and takes **no** `structural_exempt` line — the BWLP verifier's
ruling, and here it would be factually false, since 10 of 20 hulls *are* markable.

Exit condition, explicitly **not** this fork: a §11.6 newbuild-shuttle contracted-book leg, a TEN
`newbuild_specs.yaml` entry with cited scrubber/eco flags, and a disclosed price for the 20th hull.

**A source the shadow reported as absent does exist.** Both drafts state "no per-vessel contract
price is disclosed for any hull". True of the 6-K, false of the record: FY2025 20-F Item 4 gives
per-hull vessel / delivery / shipyard / dwt / purchase price for 19 of 20 hulls (total dwt
3,049,700, price 2,413).

---

## 3. What the reader is NOT warned about — three defects found while ruling

These do not block the landing and are recorded rather than fixed here.

1. **TEN has no bug gate at all.** `reconcile.py` puts TEN in `APPROX_PNAV_TICKERS`, so
   `sanity` is hardcoded `n/a`: `/reconcile TEN` can never report OK *and can never report FAIL*.
   `drift_gate.py` also skips the k_broker conjunct for approx names. The ±50% "you broke something"
   gate is disabled on the name that most needs it. **Any build waiting for SANITY = OK on TEN waits
   forever** — the correct expectation is `n/a` with the gap read as self-consistency.
2. **The tier cannot warn.** `tier_subreason` for TEN is `mixed`, which the registry defines as
   "structural LNGC sleeve + pending-anchor Handy/LR1" — neither of which is why this name is hard
   to value. Nothing in it mentions the shuttle book, the uncited rate, the un-netted $2.23bn or the
   judgmental 30%. Worse, both `figure_uncited` and `fixable_off_curve` are gated on `not
   structural`, and TEN's `nav_basis` is `structural-unavailable`, so the disclosure channel for "an
   FV-material figure that does not trace" is **disabled for this name by construction**.
3. **The leg is invisible in the artefact a reader audits.** `report.py`'s NAV breakdown omits
   `shuttle_contracted_book`, `preferred_equity` and `held_for_sale`, though `nav.py` includes all
   three. For TEN the printed rows sum to $2,536.0M against a printed total of $2,655.9M — a
   **$119.9M invisible plug**. Guard candidate: printed rows must foot to the printed total.

**The figure-provenance guard is green for an accidental reason**, and its green is not evidence.
`_nav_figure_estimate_flagged` is per-line: on the draft the money ($60,000/day) and the word APPROX
sit on different lines; on the live Q1 sheet they share a line but the context regex does not match
its words. Measured False on both. Separately, `CITATION_RE`'s bare-year branch matches the *vessel
names* "Brasil 2014" and "Rio 2016", so a line saying the rate "remains an [APPROX]" passes the
citation test.

---

## 4. The answer to the question actually being asked

The governance side sizes a GOVERNED-WIDE name off `ev_pct_family_min` under TRADE_PREREG #4, and
needs ≥ ~+20%.

**The promotion moves it from +9.6 to ≈ +14.5. It does not clear.** The whole pair is worth only
~4.8-5.2pp of EV; clearing needs a second mover of the same size — about +$4.0/sh more NAV, or a
price at or below ~$49.7 (−4.6% from 52.09). So G-TEN gate (iii) still fails on the fresh basis.

That is the useful answer. The blockers were not what was keeping TEN out; the size is not there.

**One certain trap, avoided.** `ev_pct` (25.9) is *exactly equal* to `ev_pct_family_max` (25.9) —
the adopted production set is the most favourable member of its own family. So **any** NAV-increasing
promotion pushes the point outside the recorded range and makes the containment guard withhold the
family fields, printing `ev_pct_family_min` as **null** and leaving the family maximum standing alone
on the surface. `scripts/regen.sh` only re-runs the sidecars with `--sidecars` or when
`scenario_inputs.yaml` is newer, and a sheet promotion touches neither. This regen therefore ran
**`scripts/regen.sh 2026-Q2 --sidecars`**. Without that flag the surface would have shipped a null
sizing cell and a +31 headline, 16.6pp above the honest floor.

---

## 5. Secondary questions

**The 30% §15 haircut — retained, relabelled, and now anchored for the first time.** E-1, the
derivation rule, was never derived; it was the label for a bullet in the 2026-06-22 methodology
audit, lived only in PLAN.md's Tier-4 backlog, and was **deleted by the 2026-09-18 PLAN rewrite**
(commit 50d5abc). It is currently recorded nowhere. Computing the §15.7 Step-2 anchor for TEN for
the first time, using CMDB's exact construction: gross related-party run-rate $80.6M/yr capitalised
at 10-12% = $672-806M = **24.3-29.1%** of Q2 equity NAV; net of a market-rate service cost
benchmarked to CAPT = **8.6-21.6%**. The 30% in force sits **at or above the top edge of both**,
where CMDB's 30% sat *inside* both of its. Fee load is ~1.2-1.6% of GAV, nearer CAPT's declined 0.4%
than CMDB's applied 4%. Every piece of H1 evidence points the haircut down or flat; the one thing
pointing up is H1-2026 management fees +43.5% annualised, which is rate-reset plus volume rather
than new extraction. **It moves no number in this landing** (0.30 on both sheets, contributing
exactly zero to the +$3.75/sh). It remains a stated bet, and the card should now say so with the
band attached rather than calling it a judgment between 0% and 47%.

Note the external anchor has decayed: VIE Bullish $51.50 is dated 2026-06-03, and the last price
($52.09) is **above** it. A haircut originally sized "to bring tool PW FV into the neighborhood of
VIE Bullish" is anchored to a target the market has passed.

**The preferred characterisation — corrected, and R34 cannot settle it.** The claim is not in R34 at
all: that note has four subsections (TEM / TST / Argosy / AirMania) and says nothing about who holds
the preferred. The FY2025 20-F Item 7 settles it verbatim: affiliates of Nikolas Tsakos own 45,000
(0.95%) of Series E and 100,000 (1.5%) of Series F — about $3.6M par, **1.26%** of the $287.3M — with
no other affiliate, officer or director above 1%. Both series are NYSE-listed (TEN-PE / TEN-PF; the
note's "TEN.PRE / TNP.PRF" tickers are also wrong). The §15 driver is the **structural seniority** of
mandatory perpetual preferred over a discretionary common dividend, not affiliate ownership of it.
Corrected on this sheet; `METHODOLOGY.md` still carries the old wording.

**The Tsakos Columbia lead — do not use the undated claim; the filings already say more.** Nothing
in-repo dates a 2026 development: zero mentions of Columbia, Shipmanagement or TCM across all nine
news digests, MB and Pareto. But the FY2025 20-F Note 2(b) dates a JV unwind of exactly that shape to
**2023** — TST assumed all technical management in February 2023, TCM was renamed TSM on 2026-05-02,
and it charged TEN **$nil** in 2024 and 2025. The consequence is larger than the lead: the §15 first
case, and the framework's *generic* §15.1 illustration in `METHODOLOGY.md`, both name an entity that
has taken no fees from this issuer for two years. Corrected on this sheet; four other locations
(including the generic illustration) still carry it.

**The invariant nit is genuinely fixed.** `ev_pct` 25.9 vs `ev_pct_family_max` 25.9 — consistent. No
guard written; the equality is itself the §4 trap, which is worth a guard of a different kind.

---

## 6. Carried forward, open

- **63 vs 64 hulls — UNRESOLVED, not closed.** The statutory 6-K states verbatim: "As of June 30,
  2026, the Company operated a fleet of 64 vessels, compared to 63 vessels as of June 30, 2025." The
  manifest asserts 63 and dismisses the printed 64 as contradicted by its own dwt and average series
  — but that dismissal addresses the *release*, not the filing. Extracting every vessel name in the
  filing leaves none unaccounted for, and the dwt series (−301k = one VLCC) still supports 63. So 63
  is probably right on the economics, but it is stated as closed against the source of record. Worth
  ~$2.14/sh. Named path: the monthly data kit.
- **Re-strike the shuttle NPV at 6/30 on $55,000/day** — the −$0.51/sh above. Its own change, its own
  gate. If carried unchanged into Q3 the strike half doubles to $0.32/sh.
- **Rebase the watchlist consensus pair.** `current_price` is pinned at 44.32 (2026-09-09) with
  `consensus_pnav` 0.41, but broker NAV is computed live as price/pnav, so the anchor of record has
  walked from 109.24 to **127.05** with no rebase, and `gap_pct` is measured against the drifted
  anchor. This is the 2026-06-10 TEN $44 incident's exact shape. Not introduced here; its own commit.
- **E-1 is recorded nowhere.** Either retire the 2026-06-22 audit backlog explicitly in `decisions/`,
  or put E-1 and its siblings in `inputs/reweight_triggers.yaml` where the sentinel can page them.
  Leaving them in neither place is how this one went missing.
- **`METHODOLOGY.md` still carries both corrected claims** (the affiliate-preferred wording and TCM
  as the generic §15.1 illustration).
