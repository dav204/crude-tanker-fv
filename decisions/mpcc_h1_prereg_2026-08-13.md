# MPCC H1-2026 report-day refresh — PRE-REGISTRATION (written 2026-08-13, 13 days before the print)

**Reports 2026-08-26** (MFN financial calendar 2025-12-30; half-yearly reporter, Oslo/Euronext).
Frozen now — not because the print is imminent, but because the 2026-06-25 event that dominates
this refresh was already public for seven weeks before we read it, and a band written *after*
absorbing an event we arrived at late is not a band. This is the BRUT pattern applied earlier
in the cycle.

## Why this file exists (the miss it answers)

MPCC's 2026-06-25 release sat unread for seven weeks. It surfaced in the first scheduled
news-pull digest (2026-08-13) as item M2 — the second instance of the same failure that hid
BRUT's demerger: an Oslo issuer with no EDGAR lane and, until 8/13, no issuer-release channel.
**The model was never wrong** — MPCC is a half-yearly reporter, its Q1 (2026-03-31) vintage is
correct, and the 6/25 events post-date that snapshot. Only our *awareness* lagged. So nothing is
promoted here; this file freezes what the 8/26 print should show.

## Basis (current committed state)

NAV $2.05/sh = fleet $1,538.2M (Ctr-Feeder 444.9 + Ctr-Intermediate 1,093.3) + cash 269.3
+ WC 85.9 − debt 462.9 − NB commitments 633.7 + NB advances 112.9 = $909.8M / 443,700,279 sh ·
tier GOVERNED-WIDE (structural-class) · position **`POSITION_UNRELIABLE`** ("unreliable read
(not actionable)") · sheet vintage 2026-Q1 · 51 on-water + 15 owned NB rows on-curve.

## Verified event facts (primary-sourced 2026-08-13, NOT from the digest)

Read from the issuer release as syndicated (mpc-container.com and newsweb.oslobors.no both
serve JS shells to a fetcher; the modular-finance syndication carries the release text).
**Two digest errors corrected here — this matters, because a prereg built on the digest's
version would have registered the wrong halt conditions:**

1. **Acquisition:** four **2023/2024-built, 7,000 TEU** eco-conventional vessels, **USD 340M
   total**, each on a **3-year fixed-rate TC to a top-5 liner** (USD 180M revenue / USD 140M
   expected EBITDA over the charter). **Delivery October–November 2026.** Funded by "a
   combination of bank debt and existing cash resources."
2. **USD 375M senior secured term loan — DOES NOT FUND THE ACQUISITION.** It finances **ten of
   the 16 newbuildings ordered last year**, 10-year tenor **as of delivery**, underwritten by
   Société Générale (BNP Paribas, Crédit Agricole, ING, KfW IPEX-Bank). A further USD 75M for
   two 4,500 TEU vessels is credit-approved. *(The 8/13 digest read this as acquisition
   financing. It is newbuild financing — a different balance-sheet lane entirely.)*
3. **Divestments — NAMED AND PRICED** *(the digest said "two non-strategic vessels", unnamed
   and unpriced)*: **AS Angelina USD 17M** (handover Q3 2026) and **AS Selina USD 24M**
   (handover Q4 2026 / Q1 2027).
4. **Forward-fixed:** AS Pamela (24–27 months, delivering Q4 2026) and AS Anne (30–32 months,
   delivering Q2 2027).
5. **Backlog** USD 2.2bn; coverage **99% (2026) / 74% (2027) / 48% (2028)**.

All four named vessels are already rows in `inputs/fleet_manifests/mpcc.yaml`.

## THE DOMINANT FORK — and it is a methodology call, not a data refresh

**The four acquired vessels are 7,000 TEU = class `Ctr-Large`. MPCC holds none today** (24
Ctr-Feeder + 42 Ctr-Intermediate rows). And `inputs/market_data/basis_status.yaml` marks
**`Ctr-Large: structural-unavailable`** — there is no container resale (age-0) mark.

That is precisely the GSL situation ruled at the 2026-08-08 Q2 refresh: GSL's 15-ship container
NB program entered **ADVANCES-ONLY (Group-B structural)** because "no Ctr resale mark §A1.4;
naive on-curve wiring reads −$200M-class PV-asymmetry artifacts." Wiring $340M of committed
Ctr-Large tonnage delivered-market-less-commitment against a class with no mark would reproduce
exactly that artifact, at a scale that dwarfs everything else in this refresh.

- **Fork A — ADVANCES-ONLY (the GSL precedent, my expectation):** the $340M enters as a
  commitment with advances-paid-to-date only; no Ctr-Large hull rows on-curve. NAV impact
  ≈ neutral-to-slightly-negative (deposits leave cash, the commitment offsets).
- **Fork B — on-curve:** requires a defensible Ctr-Large age-0 mark, which does not exist today.
  **NOT an agent default.** If taken, it needs a mark decision doc first.

**RULED BY OWNER 2026-08-13: FORK A — ADVANCES-ONLY.** The four Ctr-Large hulls enter as a
commitment with advances-paid-to-date only; NO Ctr-Large hull rows go on-curve at the 8/26
refresh. This extends the 2026-08-08 GSL Group-B disposition to a second name and, in doing so,
makes it the standing treatment for committed container tonnage on a structural-unavailable
basis rather than a one-off. Fork B is closed unless and until a defensible Ctr-Large age-0 mark
exists — which would need its own mark decision doc, not a refresh-day call.

**Consequence to carry into the refresh:** with the hulls off-curve, the $340M commitment
subtracts while no offsetting hull value is added, so the acquisition reads NAV-DILUTIVE on the
model surface even though it is economically accretive (3-year fixed charters, USD 140M expected
EBITDA). That asymmetry is the KNOWN COST of the structural basis, not a signal — record it
plainly in the refresh annotation so nobody reads the dilution as a deteriorating thesis. It is
the same artifact GSL carries, and it resolves only when containers get a resale mark.

## Registered band

**Point NAV ≈ $2.05/sh under Fork A; band [1.90, 2.30].** The band is deliberately wide on the
upside because H1 cash generation against a 99%-covered 2026 backlog is a real positive whose
magnitude we cannot pin without the cash-flow statement, and the two agreed sales ($41M combined)
land above scrap-adjacent feeder marks. Landing outside → HALT and investigate the INPUT.

Under Fork B the band does not apply — a Ctr-Large mark decision must precede any number.

## Halt/verification conditions

1. **Subsequent-events note FIRST.** Expected there and OUT of the 6/30 snapshot: the Oct–Nov
   acquisition deliveries, the AS Angelina Q3 handover, any term-loan drawdown.
2. **DEBT MUST NOT JUMP ~$375M at 6/30.** The facility is 10-year tenor *as of delivery* and
   finances newbuildings delivering 2026–2029, so it should be substantially UNDRAWN at the
   snapshot. A $375M debt line at 6/30 means either an early draw or that I have mis-read the
   structure — **halt and re-read the facility note before accepting any NAV.**
3. **Pair lands together:** `mpcc_2026-Q2.yaml` (provenance trio) + manifest `report_date` bump
   in ONE commit; the pair guard reds a half-applied snapshot.
4. **Forward invariance: the other 24 names delta exactly 0.0.**
5. **`prices_daily.yaml` reverted before the regen** (the 2026-07-26 rule).
6. **Fleet-list refresh:** the manifest header already registers "refine cohort ages from the
   issuer fleet list at the Q2 refresh (2026-08-26)" — ages are COHORT ESTIMATES today, AS Anne
   the widest. Do that here; it is the one scheduled opportunity.
7. **AS Angelina / AS Selina:** at 6/30 both are still owned (handovers Q3 / Q4-26–Q1-27) but
   committed to sell at stated prices. Treat per the GNK *Predator* precedent — a vessel leaves
   the manifest when it is **delivered to buyers**, not when the sale is agreed. Their agreed
   prices are S&P evidence; see below.
8. **Position stays VOID.** `POSITION_UNRELIABLE` holds through this refresh — MPCC is APPROX
   (no Pareto P/NAV) on structurally-unavailable container marks. Nothing here makes it
   actionable, and the tier stays GOVERNED-WIDE absent a separate ruling.

## S&P prints — flagged, NOT promotable, with an anomaly

AS Angelina (2,000 TEU feeder, manifest age 18.0) at **$17M**, and AS Selina (1,700 TEU feeder,
manifest age 18.5) at **$24M**. Both named, priced, dated — the fields a promotion needs.

**But there is no container transactions file** (`inputs/market_data/transactions/` holds only
tanker and dry-bulk classes) because containers have no §9.9 fit — the class rides broker-static
MB marks. So these are **cross-check evidence, not promotable prints**, and they do not run the
prints→rerun→drift loop.

**ANOMALY, flagged deliberately rather than averaged away:** Selina is *smaller* (1,700 vs
2,000 TEU; 23,800 vs 28,000 dwt) and *older* (18.5 vs 18.0) yet sold for **41% more**. On the
face of it the age/size curve inverts. Plausible explanations — an attached charter, spec or
survey position, different handover timing — are exactly that, plausible. **Do not use this pair
to infer a feeder level until the inversion is explained**; a two-print "curve" built across an
unexplained inversion is worse than no print at all. Candidate resolution: the H1 report's own
disposal note, or the MB container weekly.

---

# AMENDMENT (2026-08-18, 8 days before the print) — the 6/30–7/03 equity placement

Dated pre-print amendment, the BRUT 8/12 precedent. Trigger: news-digest 2026-08-16 M4 (Run 1)
+ M2 (Run 2) — a **completed private placement of 44,370,027 new shares at NOK 24.00**, gross
proceeds ~USD 107M, that this prereg as frozen 8/13 does not mention anywhere. Sequence:
"Contemplated" 6/30 16:39 → "Successfully Completed" 7/01 → "Registration of share capital
increase" 7/02 09:52 (share capital **NOK 488,070,306**) → settlement **DVP on/about 3-Jul**.
Six-month lock-ups (management/board/largest holders). Sources: mfn.se issuer feed (existence
+ dates, primary), modular-finance syndication + Reuters (terms).

## What the amendment CORRECTS about the plan, and what it does not

**PLAN 8/16 carried "the band is wrong as written" (+10.0% denominator). That is SUPERSEDED by
the settlement date:** DVP ~3-Jul is AFTER the 30-Jun period end, so under the AS-OF discipline
(the ASC/HAFN/TRMD subsequent-event pattern, applied in reverse) the H1 snapshot count is
**still 443,700,279** and the ~$107M is **not** in 6/30 cash. **The registered band [1.90, 2.30]
on the 443.7M denominator STANDS.** What was actually missing was the placement in the
subsequent-events expectations and the halt conditions — added below.

## Cross-foots that pin the count (resolves Run 2's NOK-par caveat as far as it can be)

- 44,370,027 = **exactly 10.000%** of 443,700,279 (the Oslo no-prospectus limit — a designed
  number, corroborating both figures).
- Registered capital NOK **488,070,306** = 443,700,279 + 44,370,027 exactly. For this to hold
  at any par other than NOK 1.00, the capital-to-count coincidence would have to hold **twice**
  (pre- and post-placement). Doubly corroborated; the residual owner-confirm is reading the par
  line in the H1 report itself, which lands 8/26 anyway.
- MPC Capital AG dilution 20.12% → 18.29% (7/01 flagging notice) implies a ~10.0% count
  increase independently. Folketrygdfondet 10.2M shares = 5.6% ⇒ ~488M total (10.2/0.056 ≈ 182M
  — NO: 5.6% of 488M = 27.3M ≠ 10.2M. The 5.6% must be of a DIFFERENT base or the stake is
  partly pre-existing — **do not use the Folketrygdfondet notice as a count cross-foot**; the
  other three legs suffice. Flagged rather than silently dropped.)

## Amended halt/verification conditions (ADDITIVE — conditions 1–8 above stand)

9. **Share count at 6/30 must print ~443.7M, NOT ~488M.** A ~488M count at the period end
   means settlement was booked pre-period-end or the equity note says something we have not
   read — **halt and read the equity/subsequent-events note before accepting any NAV/sh.**
10. **Cash at 6/30 must NOT carry the raise** (~$107M gross). A cash line ~$100M+ above the
    operating walk → same halt, same note.
11. **The Subsequent Events note is EXPECTED to carry (in addition to condition 1's list):**
    the placement (44,370,027 sh @ NOK 24.00, settlement 3-Jul, registered capital
    NOK 488,070,306) and any early term-loan drawdown. An H1 report whose subsequent-events
    note OMITS the placement contradicts the primary feed → halt, re-read the filing.
12. **Post-report forward walk (registered now so the next vintage is not hand-derived):**
    the FIRST post-H1 surface that carries the placement moves to **488,070,306 shares** and
    ~+$107M gross cash (less fees, gross-vs-net UNRESOLVED — syndicator figure). Issued at
    NOK 24 ≈ $2.41–2.53 vs model NAV $2.05 ≈ 1.2× NAV ⇒ accretive ≈ **+1.6% NAV/sh gross**
    (2.05×443.700 + 107)/488.070 = $2.083 — a DERIVED figure, fees excluded, and it must be
    co-modeled with the Fork-A acquisition treatment (which reads NAV-dilutive by construction)
    or the net is meaningless. Neither leg moves anything before the 8/26 refresh lands.
13. **Balance-sheet YAML discipline:** `diluted_shares_outstanding` in `mpcc_2026-Q2.yaml`
    follows the REPORT (condition 9), with the placement recorded in the YAML comment as the
    dated subsequent event and its registration figure cited — so the H2 vintage bump to 488M
    is a comment-anticipated move, not a surprise.
