# News digest — 2026-09-07

## Run header

- **Window swept:** **2026-08-29 → 2026-09-07** (10 calendar days; 6 business days —
  8/31, 9/01, 9/02, 9/03, 9/04, 9/07). Previous digest established by globbing
  `outputs/news_digest_*.md`: the newest is `news_digest_2026-08-29.md`, so the window
  opens the day that digest was written. No default lookback needed.
- **Names swept:** 25/25 of `inputs/watchlist.yaml` — 2343, ASC, BRUT, BWLP, CAPT, CCEC,
  CMBT, CMDB, DHT, ECO, FLNG, FRO, GNK, GSL, HAFN, INSW, LPG, MPCC, NAT, SB, SBLK, STNG,
  TEN, TNK, TRMD.
- **Depth weighting.**
  - **DEEP — APPROX-P/NAV set** (read from `reconcile.APPROX_PNAV_TICKERS`, not hardcoded):
    NAT, ASC, CCEC, TEN, CMDB, MPCC, GSL, SB, 2343.
  - **DEEP — non-US-listed** (identified from the `yahoo_symbol` suffix): BRUT, CAPT,
    MPCC, BWLP (.OL), 2343 (.HK).
  - **DEEP — live-event names** (from decision-log heads): CAPT (9/01 report-day print,
    prereg band breach accepted), BRUT (post-demerger carry ruling pending), SBLK (open
    governance legs), GNK (M&A regime ended, band boundary), BWLP (Q2 refresh executed,
    newbuild programme still off-manifest), LPG.
  - **LIGHTER — broker-covered US remainder:** DHT, ECO, FRO, INSW, TNK, FLNG, STNG,
    HAFN, TRMD, CMBT.
- **Sources searched.**
  - **Local issuer channel FIRST** (per the task's standing instruction):
    `state/edgar_manifest.jsonl` + the staged bodies under `inputs/filings/<ticker>/` —
    18 in-window arrivals read as primary text (NewsWeb/MFN releases and SEC 6-K/8-K
    exhibits). This is where most of the material below came from.
  - `mfn.se/all/a/mpc-container-ships.json` fetched directly (issuer feed, to state a
    primary-sourced negative rather than an inferred one).
  - `inputs/research_pareto/` — all six in-window Shipping Dailies read front-to-back
    plus three company reports (Frontline QR 8/30, Hafnia QR 8/30, Capital Tankers QR 9/02),
    extracted locally with `pdftotext`.
  - WebSearch/WebFetch for the names and events the local channels structurally cannot
    see (trade press, broker-reported S&P, TEN).

### COVERAGE LIMITS — read before trusting any "nothing found" below

- **The local channels were healthy all window, and that is what backs the negatives.**
  The EDGAR/HKEX sentinel staged filings on 8/29, 9/01, 9/02, 9/03, 9/04 and 9/07, and
  the NewsWeb poller staged on 9/01, 9/02, 9/04 and 9/07. Both were demonstrably alive
  every business day, so "no staged filing for name X" is a channel-backed negative,
  not silence of unknown cause. **The one exception is TEN — see M5; for TEN there is
  no local channel at all and the negative could not have been made.**
- **EDGAR was NOT enumerated directly.** I did not call `browse-edgar` or `efts` —
  they return HTTP 403 to WebFetch. I did not need to: the sentinel had already staged
  the in-window US filings locally, which is better evidence than an enumeration. But
  no claim below rests on my having independently walked EDGAR, because I did not.
- **`tenn.gr` returned an empty body to WebFetch twice** (both `/press-releases/` and
  `/investor-relations/press-releases/` — a JS shell, the pacificbasin/genco pattern).
  The TEN item in M5 is therefore sourced from the GlobeNewswire release itself, which
  fetched successfully — issuer-originated wire text, not an aggregator summary.
- **Two CMBT exhibits could not be read.** The 9/04 6-K's Ex-99.1 and Ex-99.2 (CMB.TECH
  H1-2026 half-year report) are staged but strip to whitespace — the HTM carries no
  extractable text. **CMBT's H1 report is in-window and effectively UNREAD**; see W6.
- **The SBLK appraisal aggregate below is my own extraction, not an issuer total.**
  The filing states explicitly that no en-bloc figure is given ("would be equal to the
  total of the individual valuations"), so treat my sum as arithmetic on scraped rows.
- No `globenewswire.com` timeouts this run (one fetch, succeeded). `splash247` and
  `hellenicshippingnews` were not fetched — search snippets only, and nothing below
  depends on them.

### Archive check (STEP 4)

**No gaps, accepted or otherwise, inside this window.** All six in-window business days
have a Pareto daily staged in `inputs/research_pareto/2026/{08,09}/` (8/31 · 9/01 · 9/02 ·
9/03 · 9/04 · 9/07), plus three dated company reports. `inputs/archive_gaps.yaml` carries
five accepted entries, all of them ending 2026-08-31 or earlier; none touches this window.
Nothing here is read from a hole. (The Friday-absence pattern the 8/21 entry flags —
"re-look only if a third Friday drops" — did **not** recur: 9/04 is present.)

---

## MATERIAL

### M1 · SBLK — an **Athens parallel listing with a 4.4m-share offering**, and, in the same filing round, **independent per-vessel appraisals of the entire fleet**

**Date:** 2026-09-04 (both 6-Ks filed after the Friday close).
**Source:** `inputs/filings/SBLK/0000950157-26-000982_6-K_ex99-1.htm` (the offering) and
`…-000983_6-K_ex99-1.htm` (the valuation reports); corroborated by the Pareto 9/07 daily,
"SBLK: Dual-listing in Athens with 4.4m share offering – small dilution".

**What happened — the corporate action.** Star Bulk is undertaking (i) admission to
parallel listing of all common shares on the Main Market of Euronext Athens, and (ii) an
offering of **up to 4,400,000 new common shares** (vs ~112m outstanding). Requisite Greek
regulatory approvals are already received; the New Shares trade under the same "SBLK"
ticker and are expected to be admitted on Nasdaq on the same basis. Per Pareto: maximum
price **$29.52/share**, total deal size at max **€112.2m (~$130m)**, related expenses
~€7.3m (~6.5%), CEO Petros Pappas and family investing up to €6m. **The price range is
announced 8 September and Athens trading starts 16 September** — both inside the coming week.

**What happened — the appraisals (the more valuable half).** Star Bulk engaged **Arrow
Research Limited** and filed two independent valuation reports in full:
- **Annex A** — dated 31 July 2026, **effective 30 June 2026**, covering the **133 owned
  vessels**, giving **vessel name, IMO, key particulars (scrubber) and a US$ value per
  hull** (e.g. MV Star Ayesha, IMO 9796315, scrubber, $74,250,000; MV Leviathan, IMO
  9702546, scrubber, $52,500,000).
- **Annex B** — dated and **effective 21 August 2026**, covering **five newbuildings**,
  including **MV Star Bella and MV Star Kyra, each delivered in August 2026**, and three
  vessels expected in Q4 2026.

My extraction finds **140 valued line items summing to US$4,338.2m** across both annexes.
That count exceeds 133 + 5, so the row-to-annex split needs verifying before anything is
promoted — flagged, not hidden.

**Model surfaces touched.** (a) `inputs/fleet_manifests/sblk.yaml` — two August deliveries
(Star Bella, Star Kyra) and three Q4-2026 deliveries are manifest/schedule facts. (b) The
share count and `inputs/balance_sheets/sblk_2026-Q*.yaml` — up to 4.4m new shares (~+3.9%
on the count; Pareto models ~1% NAV dilution, $33.3 → $33.1). (c) **Most importantly, the
per-vessel marks**: this is a dated, named, independent appraisal of a dry-bulk validator's
entire fleet at a quarter-end that matches the model's own NAV date convention.

**What I think it means.** The appraisal set is the rarer find. SBLK is one of three
Pareto-anchored dry-bulk validators (§11.7.2) and the tool's dry-bulk classes are
`dwt_scaled` per-class curves — a 133-hull independent mark file at 30-Jun-2026 is a direct
per-vessel test of those curves, on a name where the tool currently reads TRIM/SHORT with a
+2.1pp broker spread. The offering itself is small and, per Pareto, arguably not needed
(net debt ~$400–500m, 10% LTV).

**What I am NOT sure of.** (a) Whether Arrow's basis is comparable to the repo's
transaction-anchored marks — an appraiser's "willing buyer / willing seller" opinion is a
*third* object alongside tool marks and broker NAV, and §11.7.2 / the "don't back-solve
validator marks" rule both bear on how it may be used. That is a methodology decision, not
a data load. (b) Whether the offering will price at the $29.52 maximum. (c) My 140-row
aggregate, as above.

**Decision-log status: UNREAD.** `decisions/sblk_log.md` has no mention of Athens, the
dual listing, Arrow, or a valuation report; its newest entry is the 9/03 auto run.
**Note the position overlap:** the discretionary book carries an open SBLK leg and a GTC
that memory records as stale post-dividend. A named offering price and a dated listing
event next week bear on that directly.

---

### M2 · BWLP — a **$300m convertible bond placed**, explicitly to fund the 8-hull newbuild programme that the manifest still holds **off-book**

**Dates:** launched 2026-09-01, **placed 2026-09-02**, settlement expected 9 September 2026.
**Source:** `inputs/filings/BWLP/newsweb_2026-09-01_742eab58….txt` and
`newsweb_2026-09-02_da6ce467….txt` (issuer primary text, both also filed as 6-Ks:
acc 0001213900-26-096130 and -096420); Pareto 9/02 daily, "BWLPG: Raises $300m in
CB-offering – clever use of capital markets".

**What happened.** BW LPG placed **USD 300m of senior unsecured bonds due 9 September 2031**,
convertible into new shares. Final terms: **fixed coupon 2.25% p.a.** (semi-annual, from
9 March 2027); **initial conversion price USD 30.4870/share**, a **40% conversion premium**
over the reference price, adjusted down for the $0.95/share Q2 dividend (ex 7 Sept).
Issuer call from 30 Sept 2029 on a 20-of-30-day parity test; investor put at the third
anniversary and on change of control / free-float / delisting events. A **concurrent delta
placement of existing shares at NOK 212/share** was run by DNB Carnegie (the company
received no proceeds from it). 90-day company lock-up. Pareto acted as joint bookrunner —
**their read below is conflicted and is disclosed as such in their own note.**

**Stated use of proceeds, verbatim in both releases:** *"to partly finance the newbuild
program with Hyundai Heavy Industries for eight Panamax VLGCs, and for general corporate
purposes."*

**Model surfaces touched — and this is the point.**
- `inputs/fleet_manifests/bwlp.yaml` still carries **`vessels_under_construction: 0`**,
  with the header stating the 30-May-2026 eight-hull ~US$940M order is a subsequent event
  that is *"NOT in this snapshot — no commitment, no advance, no hull at 3/31/2026. Wire
  on-curve §9.6 at the Q2 refresh."*
- The **Q2 refresh has since happened** — `inputs/balance_sheets/bwlp_2026-Q2.yaml` exists,
  sourced from the 8/28 6-K, and it carries **`newbuild_capex_commitments: 0`** and
  **`newbuild_advances_paid: 0`**. So the manifest's own deferral instruction points at a
  refresh that has already run without wiring the programme in.
- `total_debt` on that Q2 sheet is **$814,248,000** as of 6/30. The $300m convertible is
  post-6/30 and correctly outside the snapshot — but it is a new, dated, sized, priced
  instrument sitting against a newbuild book the NAV currently treats as absent.

**What I think it means.** The financing is the confirmation that the eight-hull programme
is real, funded and progressing, and the model values BWLP with neither the hulls nor the
commitment. Whether that nets positive or negative to NAV depends on the §9.6 convention
(delivered market **less** remaining commitment, PV-discounted at `1.11^(−years)`) — with
2029–2030 deliveries the PV discount is heavy, so the sign is genuinely not obvious. BWLP
currently reads TRIM/SHORT at EV −39.6%.

**What I am NOT sure of.** (a) Whether wiring the programme raises or lowers NAV — it needs
the computation, not a guess. (b) Whether the correct treatment is a Q2-vintage amendment
or a Q3 event, given the snapshot-integrity rule that a post-quarter agreement stays out of
the quarter's snapshot: the *hulls* plainly stay out at 6/30, but the manifest header's own
instruction said to wire them at the Q2 refresh, and those two readings disagree. **That
disagreement is an owner call, not mine.** (c) Pareto's "~1.45x GAV" dilution framing is a
bookrunner's characterisation.

**Decision-log status: UNREAD.** `decisions/bwlp_log.md` contains no occurrence of
"convertible". The eight-hull order appears only as a subsequent-event exclusion.

---

### M3 · LPG (Dorian) — a **3-hull newbuild order at a stated per-ship price**, a **$368.4m refinancing**, and a **99%-covered Q3**

**Date:** 2026-09-04 (8-K acc 0001596993-26-000041, event dated 9/02).
**Source:** `inputs/filings/LPG/0001596993-26-000041_8-K_lpg-20260902xex99d1.htm` (issuer
primary text); Pareto 9/07 daily research note corroborates.

**What happened.**
- **Newbuild order:** agreement with **Hanwha Ocean** for **three 90,000 cbm dual-fuel
  Panamax VLGCs**, delivery **June, September and December 2030**, **total ~$345 million**
  (= **$115m/ship**). Dual-fuel LPG/LSFO, shaft generator, old-Panama-locks transit capable.
- **Financing:** on **2 September 2026**, a new **seven-year $368.4m credit facility** —
  **margin 140bp over SOFR**, age-adjusted profile 22 years, comprising a **$213.4m term
  loan + $155.1m revolver**, with a **$200m accordion**. It refinances the 2023 A&R
  Facility, the Cougar and Cresques Japanese financings, and the Commander tranche of
  BALCAP. $193.8m drawn at close; $16m drawn on the revolver to refinance the **Clermont**.
- **Disposal:** the Clermont is stated to be delivering **to new owners in October**.
- **Coverage:** **99% of Q3 (quarter ending 30 Sept 2026) calendar days fixed at in excess
  of $88,000/day**, excluding demurrage. Pareto notes Q2's ">$68k/day" guidance landed at
  ~$75k/day, and revises FY EPS to ~$3.2 (from $3.8) vs consensus $2.8.
- Fleet described as **25 modern VLGCs** (6 dual-fuel ECO, 17 ECO, 2 modern).

**Model surfaces touched.** `inputs/fleet_manifests/lpg.yaml` — three 2030 newbuilds
(commitment + delivery dates + the §9.6 PV discount, which at ~4 years out is severe);
the Clermont's departure. `inputs/balance_sheets/lpg_*.yaml` — the refinancing changes the
debt structure though not obviously the quantum. The LPG/VLGC curve inputs — an
issuer-stated 99%-fixed rate is a hard coverage number.

**What I think it means.** The $115m/ship contract price is a genuine, dated, per-unit
newbuild price for the Panamax VLGC class — and it lands in the same window as BWLP's
eight-hull HHI programme (M2) at a *broadly comparable* per-ship level (~$117.5m implied
from the ~$940M/8 figure the manifest carries). Two independent contract prints for the
same class in one window is a real datapoint for the newbuild-commitment leg.

**What I am NOT sure of.** (a) The **Clermont sale carries no disclosed price** — the log
already carries a cited **$53.6M residual** for it, but "delivery to new owners in October"
is not a print. **Not promotable as an S&P transaction.** (b) A newbuild *contract* price
is not a secondhand S&P print and must not be fed to the txn-anchored age curve as one —
§9.9 fits secondhand comparables. It belongs to the commitment leg. (c) Whether the Q3
99%-fixed figure supersedes a curve input or merely corroborates it.

**Decision-log status: UNREAD** for the order and the facility (`decisions/lpg_log.md` has
no "Hanwha", "345" or "368"). The Clermont is already known to the log as a residual-valued
hull, so its disposal is *anticipated*, not new.

---

### M4 · CAPT — Pareto **raises the target 26% to NOK 226 and re-pegs NAV to NOK 216**, superseding the NOK 180 the watchlist still carries

**Date:** 2026-09-02 (Quarterly Review), previewed in the 9/01 daily.
**Source:** `inputs/research_pareto/2026/09/2026-09-02_CapitalTankers-CompanyReport-QuarterlyReview-2026-09-02-528090.pdf`.

**What happened.** Pareto: **"BUY, TP NOK 226 (180); YE'26 NAV"**. They peg **NAV at NOK
216/sh** (NOK 211/sh using CAPT's own option surplus value), growing to **NOK 227/sh by
YE'26** — putting the shares at **0.73x NAV** versus BRUT / DHT / FRO / INSW / OET at
~1.3x. Q2 EBITDA $104m (marginally below PAS/cons $105–108m), EPS adj $0.70, **DPS NOK 3.00
ahead of the NOK 2.3–2.8 expected**. Q3 bookings: 71% of suezmax days at $130,240/day, 82%
of aframax at $105,765/day, **79% of total fleet days at $113,681/day** including the VLCC
on TC near $100,000/day. Pareto sees Q3 EBITDA/EPS $125m/$0.79 and the dividend rising to
**~NOK 3.5–4/sh** — roughly twice pre-report consensus.

**Two schedule/expiry facts worth pulling out:**
- **Deliveries:** an aframax and a suezmax **already delivered in August**; **two more
  suezmaxes** in Q3. Fleet days ~1,000 (Q2, 11 vessels) → ~1,300 (Q3) → ~1,530 (Q4);
  ~2,300 in Q4'27; full run-rate at 33 ships in late Q2'28.
- **The options on 13 additional ships EXPIRE 31 December 2026**, with a stated surplus
  value of **$253.7m** (shipbuilding contract cost less broker value), ~$19–20m/ship.

**Model surfaces touched.** `inputs/watchlist.yaml` CAPT — `analyst_target: 18.90` is
explicitly *"Pareto TP NOK 180 … / 9.5221"*, i.e. **the superseded target**. The
`consensus_pnav: 0.72` / `current_price: 16.06` pair is the 8/28 vintage; the **9/07 daily
prints CAPT at kr 172.9 and P/NAV 0.80x**. Also `inputs/dividend_policies/capt.yaml`, whose
header still reads *"Inaugural Q1-2026 dividend declared NOK 0.5/sh"* and models
`payout_ratio: 0.45` — against an actual NOK 3.00 declared and NOK 3.5–4 guided.

**What I think it means.** The watchlist's CAPT anchor is a stale broker target that has
since moved 26%, on a name that just breached its frozen prereg band and sits under
POSITION_UNRELIABLE. The dividend policy's stated basis is now visibly out of date. The
13-ship option expiry on 31 Dec 2026 is exactly the "anchor pinned to a live deal" that
goes stale the moment it resolves — it resolves within the model's own horizon.

**What I am NOT sure of.** (a) Whether the NOK 216 NAV, the NOK 211 option-adjusted NAV, or
the NOK 227 YE'26 NAV is the right anchor object — Pareto quotes three and the watchlist
convention wants the one paired with the printed P/NAV. (b) The 9/01 daily says NAV
NOK 217 / NOK 212 where the 9/02 review says 216 / 211 — a one-point drift between the
preview and the review, unexplained. (c) Whether the payout change warrants touching the
dividend policy at all, given the strip already runs 0.45 between the signal and the guide.

**Decision-log status: PARTLY READ.** The **NOK 3.00 dividend IS read** — `decisions/capt_log.md`
line 130 records it, and the 9/01 Q2 refresh is fully documented with the band breach
accepted. **The 9/02 Pareto review is UNREAD**: no occurrence of "226" or "216" anywhere in
the repo.

---

### M5 · TEN — a **two-Suezmax sale**, and the discovery that **TEN is the only watchlist name with no local filing channel at all**

**Date:** 2026-09-01.
**Source:** GlobeNewswire release 3354219, *"TEN Ltd. Announces Sale of Two First-Generation
Suezmax Tankers"* (issuer wire text, fetched directly — `tenn.gr` itself returned an empty
body twice).

**What happened.** TEN announced the sale of **two 2006-built Suezmax tankers**, releasing
**in excess of $100 million** to cash reserves, framed as fleet-modernity policy. The
release also restates: fleet of **81 vessels, ~10.5m dwt**; a **26-vessel newbuilding
programme with 7 delivered to date**; **$3.5bn of secured minimum future revenues**; and
the shuttle tanker **Anfield delivered from Samsung in July 2026**.

**The structural finding, which I think matters more than the sale.** TEN has a
`sec_edgar` URL configured in `inputs/data_sources.yaml` (line 201, CIK 0001166663), but:
- `state/edgar_manifest.jsonl` contains **zero** entries for TEN, all-time;
- there is **no `inputs/filings/TEN/` directory**;
- of the 25 watchlist names, **24 appear in the manifest and TEN is the only one that does
  not.**

So TEN is configured-but-unpolled. In this very window it published a material S&P release
that no local channel caught — **the same failure shape as the BRUT 7/07 miss this task
exists to prevent: not a lost file, but an absent channel.** It was caught here only
because the sweep went looking.

**Model surfaces touched.** `inputs/fleet_manifests/ten.yaml` (two hulls leaving, Anfield
arriving); the balance sheet (>$100m cash in); and the §15 governance-discount frame —
TEN is the §15 archetype where the tool OVERvalues, and a disposal that de-risks the
balance sheet is thesis-relevant. TEN also carries an APPROX `consensus_pnav: 0.34` whose
`as_of` is **2026-06-10**, by far the stalest vintage in the watchlist.

**What I think it means.** Two things, separable. The sale itself is modest and directionally
consistent with the known fleet-renewal programme. The channel gap is a standing hole that
will keep costing reads until it is closed, and it is cheap to close — the poller already
handles 6-K issuers.

**What I am NOT sure of.** (a) Whether TEN's absence from the poller is deliberate (TEN's
watchlist entry is unusual in several ways) or an oversight — I did not read the poller's
configuration, only its output. **That is the owner's to confirm.** (b) Whether any earlier
TEN releases were missed; I did not sweep back beyond this window.

**Decision-log status: UNREAD** — `decisions/ten_log.md`'s newest entries are 9/01 auto
pipeline runs with no annotation of the sale.

---

### M6 · STNG — **three time-charter-out fixtures with named vessels, rates and tenors**, plus a full Q3 coverage table

**Date:** 2026-09-03 (6-K acc 0001628280-26-060459).
**Source:** `inputs/filings/STNG/0001628280-26-060459_6-K_stngexhibit991-09032026.htm`.

**What happened.** Scorpio announced Q3-2026 TCE rates to date and three TC-out agreements:
- **STI Gladiator** (LR2) — **3 years at $40,188/day**, commencing September 2026
- **STI Jermyn** (LR2) — **3 years at $42,500/day**, commencing September 2026
- **STI Pontiac** (MR) — **3 years at $23,900/day**, commencing Q4 2026

Q3-to-date, pool and spot: **LR2 $64,900/day (85% of days, 1,249 revenue days)**;
**MR $30,000/day (79%, 3,058 days)**; **Handymax $25,500/day (70%, 1,183 days)**.
Time charters out of the pool: LR2 $30,800, MR $28,000, Handymax $23,000. Bareboat MR
$12,986 (100% of days). Fleet: **75 product tankers** (25 LR2, 36 MR, 14 Handymax),
average age 10.2 years; newbuilds/LOIs for 5 MR (2027, 2030), 6 LR2 (2027, 2029) and
**2 VLCC (2028)**. Q3 fully diluted weighted-average shares estimated **54.5–55.5m**,
reflecting the 1.75% Convertible Senior Notes due 2031 issued in April/May 2026.

**Model surfaces touched.** The product-sector curve inputs (§11.5) — three multi-year
fixtures at stated rates are exactly the object that can supersede a curve assumption;
`inputs/fleet_manifests/stng.yaml` charter_status/charter_rate/charter_end for the three
named hulls; the share count.

**What I think it means.** The three-year LR2 fixtures at $40–42.5k/day sit well below the
$64,900/day the LR2s are earning in the Q3 spot pool — the issuer is locking in term cover
at a large discount to the current spot strip. That is a coverage/derisking signal and
directly relevant to how the product strip is anchored (the §10 "TC anchors, not spot" rule
makes these the *right* kind of anchor).

**What I am NOT sure of.** Whether these three fixtures are large enough relative to a
75-ship fleet to move a class-level curve input, or whether they belong only in the manifest
as per-vessel charter status. That is a §10 judgment.

**Decision-log status: UNREAD** — no occurrence of "Gladiator", "Jermyn" or "Pontiac" in
`decisions/stng_log.md`.

---

### M7 · FRO and HAFN — **two Pareto target-price moves** on 30 August, both inside the window

**Source:** the two company reports staged 8/31.

- **FRO** (`…_Frontline-CompanyReport-QuarterlyReview-2026-08-30-527242.pdf`):
  *"We raise estimates again, but consider 1.2x YE'26 NAV fair. **HOLD TP up to $44 (40) /
  NOK 412 (373)**."* Framing: *"tailwinds from virtually every angle … but longer term that
  heavy orderbook will at some point start to worry the market."*
- **HAFN** (`…_HafniaLtd.-CompanyReport-QuarterlyReview-2026-08-30-527243.pdf`):
  *"we find current ~NAV valuation fair, and maintain **HOLD. TP up marginally to $8.5 (8.4)
  / NOK 80 (79)**."* Note inside: **LTV now down to 13%, and the dividend accordingly bumped
  to 90% of reported EPS**; Q3 80% covered at $30,700/day.

**Model surfaces touched.** `inputs/watchlist.yaml` FRO `analyst_target: 30.50` and HAFN
`analyst_target: 10.00`; `inputs/dividend_policies/hafn.yaml` (a move to 90% of reported
EPS is a payout-policy fact, not just commentary).

**What I think it means.** FRO's $44 was already visible in the 8/28 Newsflash the previous
digest caught as prose; **this is the formal target change**. The HAFN payout step-up to 90%
is the more substantive of the two for a dividend-strip model.

**What I am NOT sure of.** Whether "dividend bumped to 90% of reported EPS" is Hafnia's own
declared policy or Pareto's modelling assumption — the sentence is Pareto's. **Verify at the
issuer before touching the dividend policy.**

**Decision-log status:** FRO's $44 is partly read via the 8/29 digest's M2; the formal QR
target change and the HAFN payout figure are **UNREAD**.

---

### M8 · BRUT — **August TCE $95,073/day**, the monthly distribution, and a published financial calendar

**Dates:** 2026-09-04 and 2026-09-07.
**Source:** `inputs/filings/BRUT/newsweb_2026-09-04_7a85c536….txt` and
`newsweb_2026-09-07_349fe45a….txt` (issuer primary text).

**What happened.** For **August 2026** Bruton achieved average TCE of **~US$95,073/day, net,
for the Company's vessel trading on fixed rate time charter** (note the singular — consistent
with the owner's Option A ruling that post-demerger BRUT is the 4-hull entity, 1 on the
water). Board approved a cash distribution of **US$0.025/share** for August from Contributed
Surplus: approved 9/03, last day inclusive 9/09, **ex-date 9/10**, record 9/11, payment on or
about 9/18. Separately, the **financial calendar**: Q3 report **19 Nov 2026**, Q4 report
**18 Feb 2027**, Annual Report **23 Mar 2027**. Signed by **Lars-Christian Svensen, contracted
interim CEO** — the interim arrangement is still in place.

**Model surfaces touched.** The BRUT dividend/distribution policy and strip; a dated Q3
report date for the event calendar; the TCE figure as a check on the fixed-rate charter
assumption for the single operating hull.

**What I think it means.** Low-drama confirmation that the post-demerger entity is behaving
as the Option A ruling assumed. The $95,073/day is a *realised* fixed-rate TC number, which
is a cleaner input than a spot proxy.

**What I am NOT sure of.** Whether the $0.025/share monthly distribution is intended as a
run-rate — three data points would settle it and I have one.

**Decision-log status: UNREAD** — no occurrence of "95,073" or "financial calendar" in
`decisions/brut_log.md`.

---

## PROMOTABLE CANDIDATES

Candidates only. Nothing here is promoted; promotion is human-only.

| # | Name | Item | Fields present | Fields MISSING |
|---|---|---|---|---|
| P1 | **STNG** | STI Gladiator, LR2, TC-out | vessel · class · rate **$40,188/day** · tenor **3 yrs** · start Sep-2026 | built year |
| P2 | **STNG** | STI Jermyn, LR2, TC-out | vessel · class · rate **$42,500/day** · tenor **3 yrs** · start Sep-2026 | built year |
| P3 | **STNG** | STI Pontiac, MR, TC-out | vessel · class · rate **$23,900/day** · tenor **3 yrs** · start Q4-2026 | built year |
| P4 | **SBLK** | Arrow Annex A appraisals | **133 hulls**: name · IMO · scrubber · US$ value, effective **30-Jun-2026** | not an S&P print — appraised values, basis needs a methodology ruling |
| P5 | **SBLK** | Arrow Annex B appraisals | **5 newbuildings** incl. Star Bella + Star Kyra (**delivered Aug-2026**), effective 21-Aug-2026 | as P4 |
| P6 | **LPG** | Hanwha 3× Panamax VLGC order | class · count · **$345m total / $115m per ship** · deliveries Jun/Sep/Dec **2030** | hull names/IMOs — **newbuild contract price, NOT a secondhand comparable (§9.9)** |

**Explicitly NOT promotable, and why:**
- **TEN's two Suezmaxes** — "in excess of $100 million" is a *proceeds-to-cash* figure, and
  **no vessel names and no sale price are disclosed**. A gain or a proceeds number without a
  price is not a print.
- **LPG's Clermont** — "delivery to new owners in October" with **no price**.
- **The ~$200m VLCC resale** in the 9/07 daily — a **rumour**, no named vessel, no confirmed
  price, and explicitly premium-distorted (see W1).

---

## WATCH

**W1 · A VLCC resale rumour at ~$200m, against a curve the repo marks at $184.2m.**
Pareto, 9/07: rumours of a **~$200m prompt-resale VLCC**, which TradeWinds suggests may be a
Dynacom (Procopiou) vessel bought by *"entities from Iraq"*, with **delivery inside Hormuz —
which the note says obviously requires a premium**. Dynacom has two VLCCs due from New Times
and CSS Tianjin at a reported **~$115m/each yard price**. Pareto: *"The last 'clean' resale
transaction was ~$163m paid by Trafigura back in May … We currently use $175m in our NAVs"*,
and says they do not believe it is *"completely relevant"*. For reference, the repo's own
VLCC age-0 curve mark is **$184.2M** (cited in `decisions/capt_log.md`), and Pareto reckons
DHT / FRO / INSW / OET are pricing in ~$210m / $233m / $219m / $252m. **This is a falsifier
moving, not an input** — a rumoured, premium-distorted, unnamed transaction must not touch
the txn-anchored curve. Worth watching for a clean print behind it.

**W2 · The whole watchlist price/P-NAV block is a week stale, and the tape moved hard.**
Every name carries `as_of: 2026-08-28`. The 9/07 daily prints (price · P/NAV · 1Y-FWD P/E):
BRUT kr 46.0 · 1.07x · 14.6x · **CAPT kr 172.9 · 0.80x · 8.4x** · DHT $20.9 · 1.23x · 9.8x ·
FRO $46.1 · 1.40x · 10.5x · HAFN $9.2 · 1.11x · 11.7x · INSW $104.5 · 1.27x · 12.7x ·
NAT $7.3 · **–** · 13.6x · ECO $71.4 · 1.58x · 9.1x · STNG $82.4 · 0.78x · 14.8x ·
TNK $93.4 · 0.97x · 8.4x · TRMD $35.2 · 1.02x · 11.7x · CMBT $19.5 · 0.92x · 10.7x ·
GNK $27.7 · 1.02x · 13.2x · SBLK $32.4 · 0.97x · 7.6x · BWLP kr 233.4 · 1.22x · 12.7x ·
LPG $55.2 · 1.19x · 12.8x · MPCC kr 27.5 · **–** · 8.5x. That is **+4% to +9% in a week
across the complex and +15% for CAPT**. Two confirmations worth noting: NAT and MPCC still
print "–" in the P/NAV column, so their APPROX flags remain correct; CCEC, TEN, CMDB, GSL,
SB and 2343 remain absent from Pareto's table entirely, as the APPROX documentation says.
**This is the mechanical rebase chain's job, not a news item — flagged so it is visible, and
the pair rule (price + pnav + fwd_pe together, never the price alone) applies.**

**W3 · HAFN — accelerated vesting of the outgoing CEO's awards.** 9/03 6-K: the board
resolved on 9/02 to accelerate vesting of Mikael Skov's **2,159,127 unvested options and
60,974 RSUs**, leaving him with vested rights over **2,220,101 shares**. Share-count/dilution
relevance only. The **CEO transition itself (Skov → Søren Steenberg Jensen, effective 9/01)
is already read** — `decisions/hafn_log.md` line 1514 records it. An **EGM on 23 September
2026** will appoint Skov as a Director.

**W4 · TRMD — small capital increase.** 9/02 6-K: **22,666 Class A shares** issued on RSU
exercise (nominal USD 226.66), subscribed at DKK 139.90 and DKK 195.50. Immaterial to NAV;
noted for share-count hygiene only.

**W5 · 2343 — nothing new from the issuer.** The HKEX channel staged one in-window document:
the **Monthly Return for the month ended 31 August 2026** (`12308484_2026083101113.pdf`),
a routine share-movement return. Web search surfaced the **interim dividend of HKD 0.155/share
paid 3 September 2026** — but that was **declared at the 8/21 interim report** (ex 20 Aug,
record 24 Aug), so the payment falling in-window is not a new event. **Per the aggregator-date
rule I am flagging that the HKD 0.155 figure is aggregator-sourced (TipRanks) and not verified
against the issuer's own announcement — LEAD-QUALITY.** Note the standing rider in the
watchlist: verify whether 5,165.247803M shares is the post-buyback 30-Jun count before the
next P/NAV re-derivation. The August Monthly Return is exactly the document that would settle
it, and it is now on disk.

**W6 · CMBT's H1-2026 report is in-window and effectively unread.** The 9/04 6-K
(acc 0000919574-26-006193) attaches the CMB.TECH half-year 2026 report as Ex-99.1 and the
financial half-year report as Ex-99.2. **Both strip to whitespace** — no extractable text in
the staged HTM. CMBT is the multi-sleeve hybrid (§11.9) reading TRIM/SHORT at EV −25.7%, and
a half-year report is a balance-sheet and fleet event. **This needs a rendered fetch (the
LibreOffice/pdftoppm or fetch_pdf route) before anyone can say what is in it.** I am recording
it as *not read*, not as *nothing found*.

**W7 · CAPT's 13-ship option block expires 31 December 2026.** Stated surplus value
**$253.7m** (~$19–20m/ship). An anchor pinned to a live deal goes stale the moment the deal
resolves; this one resolves inside the strip horizon, in either direction.

---

## NO-ACTION

One line per name swept clean, so coverage is visible rather than inferred. In every case
below the basis is: the EDGAR/HKEX sentinel and (where applicable) the NewsWeb poller ran
every business day of the window and staged nothing for the name, **and** the name did not
appear with a stance change, print or fixture in any of the six in-window Pareto dailies.

- **DHT** — searched the local EDGAR channel + all six dailies + web (VLCC S&P) over
  8/29–9/07; nothing found. Appears in the 9/07 daily only as a valuation reference point.
- **ECO** — same sources, same window; nothing found beyond the 9/07 price-table row.
- **FRO** — no *new* issuer event; the in-window item is the 8/30 broker target change (M7).
- **INSW** — same sources; nothing found. (The $185m five-vessel programme surfaced by web
  search is **January 2026**, well out of window — a re-publication trap avoided.)
- **TNK** — same sources; nothing found.
- **NAT** — same sources; nothing found. Still no Pareto P/NAV (prints "–"), APPROX intact.
- **FLNG** — same sources; nothing found in-window. (Pareto's Golar company report is 8/24,
  before the window.)
- **CCEC** — same sources; nothing found in-window. The AGM set for **22 Sept 2026** was
  announced **7 Aug**, outside the window.
- **ASC** — same sources; nothing found. Still no Pareto P/NAV.
- **CMDB** — same sources; nothing found. Absent from Pareto's table, as documented.
- **GSL** — same sources; nothing found. Absent from Pareto's table, as documented.
- **GNK** — same sources; nothing found. The M&A regime remains ended (Diana withdrew 8/14,
  pre-window); no new proposal, no tender. Prints $27.7 / 1.02x on 9/07.
- **SB** — same sources; nothing found. Absent from Pareto's table, own-basis lane.
- **MPCC** — **primary-sourced negative**: I fetched `mfn.se/all/a/mpc-container-ships.json`
  directly and the issuer feed's most recent release is **2026-08-26** (Q2 results + dividend
  key information). Nothing after 8/26. This is the issuer's own feed, not an inference from
  our archive.
- **CMBT** — swept, but **not clean and not clear**: see W6. Do not read this as silence.
- **2343** — swept; one routine Monthly Return, no substantive event. See W5.

---

## OWNER SUMMARY — ranked

1. **SBLK, this week, twice over (M1).** The Athens offering prices **8 Sept** and lists
   **16 Sept**, at a stated maximum of $29.52 — and there is an open SBLK leg and a
   post-dividend-stale GTC in the discretionary book. Separately, the same filing round
   dropped a **133-hull independent per-vessel appraisal at 30-Jun-2026**, which is the most
   valuable single dataset this sweep has ever turned up for a dry-bulk validator. The
   calendar half is time-critical; the appraisal half is a methodology decision to schedule,
   not to rush.
2. **BWLP's newbuild programme is now financed and still off the model (M2).** A $300m
   convertible has been placed explicitly to fund eight hulls that the manifest carries as
   `vessels_under_construction: 0` with a "wire at the Q2 refresh" note — and the Q2 refresh
   has already run with commitments and advances at zero. Whichever way the §9.6 treatment
   goes, the current state is one the manifest header itself did not intend.
3. **Close the TEN channel gap (M5).** TEN is the only one of 25 names with no local filing
   channel, it has a configured EDGAR URL that nothing polls, and it published a material
   sale on 9/01 that only this sweep caught. This is the BRUT failure shape, found before it
   cost anything. Cheap to fix; expensive to keep.
4. **CAPT's watchlist anchor is superseded (M4).** `analyst_target: 18.90` is the NOK 180
   target Pareto replaced with **NOK 226** on 9/02, on a name that just breached its frozen
   prereg band. The dividend policy's stated basis (NOK 0.5 inaugural, 0.45 payout) is
   likewise behind a NOK 3.00 declaration.
5. **Read the CMBT half-year report (W6).** It is in-window, it is staged, and it is
   unreadable as staged. Until someone renders it, CMBT's line in the NO-ACTION list is a
   hole, not a clean sweep.
6. **STNG's three fixtures (M6, P1–P3)** are the cleanest promotable items in the window —
   named vessels, stated rates, stated tenors — and they lock term cover well below the
   current LR2 spot pool.
7. **Dorian's order and refinancing (M3)** need wiring at the next LPG refresh; the
   $115m/ship Panamax VLGC contract price pairs usefully with BWLP's HHI programme.
8. **The rebase chain has a week of drift to absorb (W2)** — +4–9% across the complex,
   +15% CAPT. Mechanical, but the pair rule applies.

---

*Review-only run. This digest is the only file written. No pipeline, no promotion, no
ingest, no git. Nothing here has reached the model — every item above requires a human
promotion decision.*
