# CMBT 2026-Q2 refresh — EXECUTABLE PACKET (prepared 2026-09-07, nothing written yet)

**Status:** every figure sourced from the notes-bearing half-year report (accession
0000919574-26-006193, filed 9/04; 86 page images recovered from EDGAR because the staged
exhibits were image-only shells — see the FILING-UNREADABLE commit). Balance-sheet
extraction verified (all cross-foots reproduce, 14/14 citations); crude fleet bridge
verified (img_059 — the 31-AUGUST table — confirmed unused; counts tie to the 30-June page).

**Executes on three owner words** (C-1 held-for-sale off-curve · C-2 keep the FSO placeholder
with its debt · C-3 governance haircut stays 0) — recommendations YES / YES / YES.

## Corrections folded from the two verifications (none corrupting)

1. **AUC must move in the SAME commit** as the seven delivered hulls go on-curve:
   `newbuild_advances_paid` 759,807 → 532,660 (Note 12 AUC balance, img_025; 986,113
   transferred out). Landing the hulls without the AUC drop double-counts them.
2. **Held-for-sale double-count** ($0.758/share): Donoussa, Stella, Brest, Brugge (crude) and
   Golden Myrtalia (dry) must leave the on-curve manifest if HFS 219,985 enters working
   capital. Individually sourced: Donoussa 49.4M, Golden Myrtalia 25,166k. Brugge+Brest
   123.8M is a COMBINED figure — never split. Stella is a residual (~21.6M, DERIVED).
3. **Inherited Q1 error:** Stella and Golden Myrtalia have been HFS "since December 31, 2025"
   (Note 8, img_019) — the Q1 manifest carried both on-curve (~46.8M double-counted at Q1).
4. **FSO branch B is one-sided:** zeroing `shuttle_contracted_book` while the secured FSO loan
   (109,937, Note 16 img_032) stays in `total_debt` understates NAV ~$0.72/share. The lender
   advanced and fully drew 110,619 against the two FSOs — the $100M placeholder is
   conservative, not aggressive.
5. **Dry yaml fragment is not cross-foot consistent** (42 NMax in rows vs the page's 40) —
   fix before landing. Lead: Note 12 says "six Newcastlemax bulk carriers" under construction
   at 30 Jun vs the bridge's 8−4 = 4 → two NMax may have left the program (UNVERIFIED).
6. **DHT precedent is realized net price** (Bauhinia $51.0M, dht_2026-Q2.yaml:26-28), not
   carrying value — bears on which basis C-1 uses for HFS hulls.
7. **Litigation (Note 23, img_045):** Antwerp 30 Mar 2026 rejected FourWorld in full; Bermuda
   21 May 2026 rejected the $14.49 immediate-cash claim, appraisal only, "no material delta"
   — under appeal, pleaded November 2026. Both fire the Q1 sheet's own governance tripwire.
8. **Q1 label error:** the Investments line is mostly FVTPL stakes (Anglo-Eastern, SwissMarine),
   not "equity-accounted JV" — relabel; amount convention carries (154,217).
9. The auditor's report (img_051, 2 Sep 2026) is an ISRE 2410 REVIEW, not an audit.

---
# APPENDIX A — balance-sheet extraction (verified)

## 0. BLOCKING FILING-FORMAT FINDING — read this first

**The three staged `.htm` files contain zero financial text.** Both exhibits are image-only wrappers: every page is a `<IMG SRC="img_NNN.jpg">` tag and nothing else.

- `..._ex99-1.htm` (23KB) = 33 `<IMG>` tags, `img_053.jpg`–`img_085.jpg`, plus 54 characters of text ("Exhibit 99.1").
- `..._ex99-2.htm` (36KB) = 53 `<IMG>` tags, `img_000.jpg`–`img_052.jpg`, plus 54 characters of text.
- Total text recoverable from the staged files: **0 figures**. The "SMALL files — read them fully" premise in the task is wrong; the files are small *because* the content is not in them.

The 86 page images are separate EDGAR objects that were not staged. I fetched them from the filing directory (`https://www.sec.gov/Archives/edgar/data/1604481/000091957426006193/`, `www.sec.gov` is on the WebFetch allowlist) into scratchpad and read them:

```
/private/tmp/claude-501/-Users-dan-personal-Projects-crude-tanker-fv/af60674a-ad0c-4045-bedc-1c5dabfccbc6/scratchpad/pages/img_000.jpg … img_085.jpg
```

No repo file was created or modified. **Whatever fetcher stages CMBT filings drops image-only exhibits silently** — this is exactly the "absence isn't evidence" failure mode in the global rules, and it should be fixed before the next image-rendered filing lands. Citations below are `img_NNN` (page number printed on the page in brackets). Exhibit 99.2 (`img_000`–`img_052`) is the notes-bearing financial report; Exhibit 99.1 (`img_053`–`img_085`) is the narrative half-year report.

---

## 1. SUBSEQUENT EVENTS — audited first

**Note 26 — Subsequent events** (`img_049`, p.50) is the complete formal note. Three events:

| # | Event | Quote | IN / OUT of 30-Jun snapshot |
|---|---|---|---|
| 1 | CTV FRS Windcat 65 delivered | "On July 14, 2026, the CTV FRS Windcat 65 was delivered." | **Fleet: OUT.** Its advances **ARE IN** `assets under construction` 532,660 at 30 Jun. Do not add the hull to the Q2 manifest. |
| 2 | VLCC **Donoussa** (2016, 299,999 dwt) sale announced, gain ~USD 74.3M, delivers Q4-2026 | "On August 3, 2026, the Company announced the sale of the VLCC Donoussa… gain of approximately USD 74.3 million… delivered to its new owner in the fourth quarter of 2026." | **Split.** The **asset is IN** — Note 8 says HFS criteria "were met as at June 30, 2026… carrying value of USD 49.4 million", and the MoA "subsequently signed on July 15, 2026, confirming management's assessment as at the reporting date." The **gain is OUT** (Q4-2026). |
| 3 | Suezmax **Bristol** (2024, 156,851 dwt) sale announced, gain ~USD 56.9M, delivers Q4-2026 | "On August 11, 2026, the Company announced the sale of the Suezmax Bristol… gain of approximately 56.9 million USD… delivered to its new owner in the fourth quarter of 2026." | **OUT entirely.** Bristol is absent from Note 8. At 30 Jun it is a normal on-the-water Suezmax inside the count of 18. |

**A fourth post-period fact is disclosed outside Note 26** and is the one most likely to be mis-swept: Note 6 (`img_015`, p.16) states of Brest/Brugge — "**The vessels have been delivered in the third quarter of 2026** and will generate a gain of approximately USD 100.2 million to be recognised in the third quarter of 2026." So at 30 Jun both are **IN** as held-for-sale at carrying value; their delivery and the 100.2M gain are **OUT**.

**Trap flag:** the 8/27 press release fleet paragraphs are as-of **27 August**, not 30 June ("Bocimar has 40 (+6NB) Newcastlemaxes… Euronav has 2 FSOs…, 4 (+1NB) VLCCs and 15 Suezmaxes on the water", `pr827.txt:532,611`). Using them for a 2026-Q2 manifest breaks snapshot integrity. Use the 30-June fleet page (§4).

---

## 2. Sourced-figures table

All Q2 values are as-of **30 June 2026**, in USD thousands unless noted. Q1 values from `inputs/balance_sheets/cmbt_2026-Q1.yaml`.

| Field | Q1 (31-Mar-26) | **Q2 (30-Jun-26)** | Citation |
|---|---|---|---|
| `cash_and_equivalents` | 202,871,000 | **159,845,000** | Cash 151,574 + short-term investments 8,271 — `img_001` p.2 |
| `total_debt` (excl. leases) | 5,238,160,000 | **5,447,060,000** | `img_002` p.3 + Note 16 `img_031` p.32 |
| `lease_liabilities` | 6,232,000 | **5,601,000** | 4,014 non-current + 1,587 current, `img_002`; Note 16 total 5,601 `img_031` |
| `newbuild_advances_paid` | 759,807,000 | **532,660,000** | Assets under construction, `img_001` p.2 / Note 12 `img_025` p.26 |
| `newbuild_capex_commitments` | 0 (convention) | **900,837,000 sourced** (see §3c) | Note 12 Capital commitment, `img_027` p.28 |
| `diluted_shares_outstanding` | 290,169,769 | **290,169,769 (unchanged)** | Note 15 `img_030` p.31 |
| `preferred_equity` | 0 | **0** | Equity section `img_002` — share capital/premium/reserves/treasury/retained only; no preferred, no NCI line |
| `working_capital_net` | 912,136,000 | **1,252,711,000** or **1,427,211,000** (fork, §5) | components below |
| `shuttle_contracted_book` | 100,000,000 APPROX | **still un-sourced** (§3a) | — |

**Debt itemisation and cross-foot** (Note 16, `img_031` p.32; face amounts `img_002` p.3):

```
Bank loans        non-current 2,869,323 + current 195,082 = 3,064,405  ✓ Note 16
Other borrowings  non-current 1,998,055 + current 180,981 = 2,179,036  ✓ Note 16
Other notes       current only                             =   203,619  ✓ Note 16
                                            total_debt     = 5,447,060
Lease liabilities non-current 4,014 + current 1,587        =     5,601  ✓ Note 16
                          Note 16 grand total 5,452,661    = 5,447,060 + 5,601  ✓
```
This is the identical convention the Q1 sheet used (borrowings incl. the sale-and-leaseback book, IFRS-16 leases separate). Q1→Q2 debt **+208,900**.

**Operating working capital** (`img_001`/`img_002`, Q1 convention):
```
inventory 120,674 + trade & other receivables 415,688 + current tax assets 2,828
  − trade & other payables 235,139 − current tax liabilities 2,807 = 301,244   (Q1: 169,399)
```

**Off-curve segment books — now CURRENT-VINTAGE.** The Q1 sheet used FY2025 20-F segment values (Dec-25, one quarter stale, flagged as such). **Note 7 carries a 30-June-2026 segment balance sheet** (`img_017` p.18):

| Segment | Vessels | AUC | HFS |
|---|---|---|---|
| Euronav | 1,360,841 | 35,887 | 194,819 |
| Bocimar | 4,731,683 | 241,505 | 25,166 |
| Delphis | 205,450 | 10,608 | — |
| **Bochem** | **312,680** | 62,401 | — |
| **Windcat** | **264,585** | 175,597 | — |
| Other | 180 | 6,662 | — |
| **Total** | **6,875,419** ✓ | **532,660** ✓ | **219,985** ✓ |

Bochem 276,374 (Dec-25) → **312,680**; Windcat 196,542 (Dec-25) → **264,585**. The staleness caveat in the Q1 yaml is now retired.

**Investments line** (Note 25, `img_047` p.48): `154,217 = 89,825 FVTPL non-current + 64,392 equity-accounted`. The note: FVTPL total USD 98.1M = 10% Anglo-Eastern Univan 45.0 + 15.92% SwissMarine 44.8 (= 89.8 non-current) + 8.3 short-term. Equity-accounted = JVs 28,320 + associates 36,072. **Note: the Q1 yaml labelled the whole 132,308 Investments line "equity-accounted JV investments" — that label is wrong** (most of it is FVTPL equity stakes). The amount convention (whole line) carries to 154,217.

**Full-balance-sheet cross-foots, all verified:** total assets 7,908,869 + 919,020 = 8,827,889; equity 3,120,994 + 4,887,666 + 819,229 = 8,827,889; every sub-line of both sides foots exactly (script run, 14/14 OK). Cash-flow ties: 146,529 + 6,036 − 991 = **151,574** = BS cash.

---

## 3. THE THREE BLOCKERS

### (a) FSO $100M — **owned-vs-JV RESOLVED; the $100M value NOT resolved**

**The FSOs are consolidated, not equity-accounted.** Three independent citations:

1. **Note 16 bank-loan schedule** (`img_032` p.33) carries a line item inside CMB.TECH's *consolidated* bank loans: "**Secured FSO loan 161.1M** | USD | SOFR + 2.05% | 2030 | facility 110,619 | drawn 110,619 | carrying value **109,937**" at 30 Jun 2026 (Dec-25: 123,593 / 122,736). A consolidated secured loan on the FSOs means the FSOs sit on balance sheet.
2. **Fleet overview 30 June 2026** (`img_073` p.21) lists under Euronav/TANKER: "**FSO 2**", marked OWNED (no newbuilding marker).
3. **Note 25 discloses the full composition of the equity-accounted investees** (`img_047`, `img_048` pp.48–49): total only **64,392** — JVs 28,320 (acquisitions relate to 25% Jiangsu Andefu) and associates 36,072 (TFG Marine +5%). **No FSO appears, and the total is far too small to carry two FSOs.**

**So the Q1 yaml's own conditional instruction — "if the FSOs sit inside the equity-accounted investments, zero this" — does NOT fire. Do not zero it.**

**But the $100,000,000 figure remains un-sourced and stays a house-rule RED.** The report discloses no FSO carrying value, no charter counterparty, and no charter expiry. What is *newly* citable: **FSO average time charter rate USD 88,540/day** for H1-2026 (H1-2025: 86,423) — `img_074` p.22 — and average age 24y (`pr827.txt:610`). A rate without a term does not produce a contracted residual.

**What would settle it:** the FY2025 20-F FSO service-contract note (term/expiry of the FSO Africa and FSO Asia contracts), or the segment PP&E disclosure that splits Euronav vessels between tankers and FSOs. **Second, and more urgent: check for double-count.** The FSOs being consolidated means their book value is inside `Vessels` 6,875,419 (Euronav segment 1,360,841). `shuttle_contracted_book` is only safe if the two FSOs are absent from the Q2 crude fleet manifest — verify that before the run.

### (b) Held-for-sale 219,985 — **composition RESOLVED; per-hull values 3 of 5 sourced**

Note 8 (`img_019` p.20) names every hull still HFS at 30 June and gives carrying values for the two groups that have MoAs:

- **Brugge (2023, 156,851 dwt) + Brest (2023, 156,851 dwt)** — MoAs signed 12 June 2026, "combined net sales price of USD 224.0 million… **combined carrying value of USD 123.8 million**. The net gain… amounts to USD 100.2 million… upon delivery… expected during the third quarter of 2026."
- **Donoussa (VLCC, 2016, 299,999 dwt)** — "accounted for as an asset held for sale as at June 30, 2026 and had a **carrying value of USD 49.4 million**."
- **Stella (Suezmax, 2011, 165,000 dwt) and Golden Myrtalia (Capesize, 2011, 177,979 dwt)** — "have been classified as an asset held for sale since December 31, 2025, and this status remains unchanged as at June 30, 2026… continue to be classified as an asset held for sale as at June 30, 2026." **No carrying value given for either.**

The earlier attempt failed because it worked from the aggregate alone. The **Note 7 segment split closes it one level further**: HFS = Euronav 194,819 + Bocimar 25,166 (`img_017`).

```
Bocimar HFS = 25,166 — and Golden Myrtalia is the ONLY Bocimar hull in Note 8
  → Golden Myrtalia carrying value 25,166  (SOURCED at segment granularity)
Euronav HFS 194,819 − Brugge/Brest 123,800 − Donoussa 49,400 = 21,619
  → Stella carrying value 21,619  (DERIVED, single-vessel residual — NOT disclosed)
Check: 123,800 + 49,400 + 21,619 + 25,166 = 219,985 ✓
```

Four of five hulls are sourced or segment-pinned; **Stella's 21,619 is a derived residual and must be flagged as such, not typed as a sourced figure.** Settled by: the FY2026 20-F Note 8, which historically gives the per-vessel HFS table.

### (c) Newbuild capital commitments — **RESOLVED, with full maturity split**

Note 12, "Capital commitment" (`img_027` p.28): "**As at June 30, 2026 the Group's total capital commitment amounts to USD 0.9 billion (December 31, 2025: USD 1.6 billion).**" Full schedule, both cross-foots verified:

| Commitments in respect of | Total | 2026 | 2027 | 2028 | 2029 |
|---|---|---|---|---|---|
| Tankers | 78,540 | 78,540 | — | — | — |
| Dry bulk vessels | 283,559 | 273,716 | 9,843 | — | — |
| Container vessels | 29,570 | 29,570 | — | — | — |
| Chemical tankers | 334,250 | 59,900 | 34,100 | 159,650 | 80,600 |
| Offshore wind vessels | 166,361 | 64,414 | 92,416 | 9,531 | — |
| Other | 8,557 | 8,557 | — | — | — |
| **Total** | **900,837** ✓ | **514,697** | **136,359** | **169,181** | **80,600** ✓ |

The Q1 comment's "~$1.2bn remaining commitment" (a tilde = a RED under house rules) is now replaced by a cited 900,837 with a year-by-year split, plus a cited Dec-25 comparative of 1.6bn. Note 12 also states 25 vessels under construction for **an aggregate USD 526.0 million**, and lists the programme (foots to 25 exactly).

---

## 4. Fleet reconciliation — **NO per-vessel table. Class counts settled; the Q1→Q2 bridge is UNVERIFIED.**

**There is no per-vessel fleet table anywhere in the 86 pages.** What exists is a class-level fleet overview (`img_073` p.21), headed "Fleet overview on 30 June 2026 — On 30 June 2026, CMB.TECH owned and operated 236 vessels", with owned and newbuilding marked separately:

- Dry-bulk 115: **Newcastlemax 40 owned + 6 NB**, Capesize 37, Kamsarmax 26, Panamax 4, Coasters +2 NB
- Tanker 26: Suezmax 18, VLCC 5 + 1 NB, **FSO 2**
- Chemical 16 / Container 5 / Offshore energy 70 / Port vessels 4 — total **236 ✓** (every sub-tally foots)

**The 40 (+6NB) count is corroborated twice inside the financial statements**: Note 12's newbuild programme lists "six Newcastlemax bulk carriers" under construction (`img_025`), as does the Note 12 capital-commitment box (`img_027`).

**The 38+4=42≠40 bridge does not close from this filing.** Note 12 dates all four H1 Newcastlemax deliveries — Mineral Latvija (11 May), Mineral Eesti (28 May), Mineral Magyar (8 June), Mineral Lietuva (29 June) (`img_015` p.16; delivery table `pr827.txt:409–427`) — so all four are Q2, and 38 + 4 = 42 owned / 8 − 4 = 4 NB, against a reported 40 owned / 6 NB. Owned is −2 and NB is +2, netting to 46 either way, which points at a reclassification or a wrong Q1 basis rather than a missing hull. **The Q1 "38 (+8NB)" figure cannot be verified — no Q1-2026 filing is staged** (`inputs/filings/CMBT/` holds only Aug-2026 accessions). **Settled by:** the Q1-2026 6-K (filed 2026-05-19, cited in the Q1 yaml header) fleet paragraph.

**Two internal inconsistencies to record:**
1. The narrative fleet page says "The company had **26** vessels under construction on 30 June 2026"; Note 12 says "**twenty-five** vessels under construction at June 30, 2026, for an aggregate amount of USD 526.0 million" and its own itemisation foots to 25. The difference traces to CTV newbuilds — Note 12 says "two Hydrocat CTVs", the fleet page marks CTV +3 NB. **Per house rule the report/notes govern: 25.**
2. The 8/27 press-release counts ("4 (+1NB) VLCCs and 15 Suezmaxes on the water") reconcile to the 30-June page **only if held-for-sale hulls are excluded**: 18 − Brest − Brugge − Stella = 15; 5 − Donoussa = 4. That is arithmetically consistent but not stated anywhere — treat as a derived reading, and do not mix the two bases.

---

## 5. Now sourceable vs. still an owner fork

### Now sourceable (was blocked or stale)
1. **Every balance-sheet field** for `cmbt_2026-Q2.yaml` — cash 159,845; total_debt 5,447,060 (itemised, cross-footed to Note 16); leases 5,601; NB advances 532,660; shares 290,169,769; preferred 0.
2. **Newbuild capital commitments 900,837** with a 2026–2029 maturity split and a category split — blocker (c) closed.
3. **FSO ownership status: consolidated, not JV** — blocker (a)'s *structural* half closed; the Q1 "zero this" trigger does not fire.
4. **Held-for-sale composition**: five named hulls, 123.8 + 49.4 sourced, Golden Myrtalia 25,166 pinned by segment — blocker (b) closed except Stella.
5. **Off-curve segment books at current vintage** (Bochem 312,680, Windcat 264,585) — the Q1 stale-Dec-25 caveat retires.
6. **Newcastlemax 40 owned + 6 NB at 30 June**, triple-cited.
7. **TCE anchors** for §10 work (`img_074`): VLCC spot 92,403 / TC 64,853; Suezmax spot 96,108 / TC 35,204; Newcastlemax spot 37,960 / TC 24,114; Capesize spot 32,656; FSO TC 88,540.
8. **No impairment triggers**, with "independent broker valuations… indicate that the fair market value of the fleet exceeds its carrying value" (`img_027`) — a clean §6 footnote.

### Still an owner fork

**Fork 1 — `shuttle_contracted_book` (the FSO $100M).** The uncited placeholder survives because ownership, not value, was what the report settled.
- *Branch A — hold 100,000,000 as-is.* Carries an uncited NAV driver worth **$0.345/share** into another quarter, against the standing rule that an uncited figure is a RED, not data.
- *Branch B — zero it pending the 20-F charter terms.* Removes **−$0.345/share** and puts the name's FSO sleeve in the figure-provenance queue. Note this is *not* the same as the Q1 yaml's zeroing trigger, which was conditional on JV status and has now been disproven.
- Either branch requires first confirming the two FSOs are absent from the Q2 crude manifest, or the sleeve double-counts against `Vessels`.

**Fork 2 — held-for-sale valuation basis.** The Q1 yaml states its convention explicitly: "HFS at agreed price per the DHT-Bauhinia convention". IFRS 5 carrying value is *not* agreed price, and at Q2 the gap is large.
- *Branch A — carrying value 219,985* → `working_capital_net` = 301,244 + 312,680 + 264,585 + 154,217 + 219,985 = **1,252,711** (Q1: 912,136; +340,575).
- *Branch B — agreed price, consistent with the stated Q1 convention* = Brugge+Brest **224,000 sourced** + Donoussa **123,700** (49,400 carrying + 74,300 gain, derived from "gain… based on the net sale price and book values") + Stella 21,619 + Golden Myrtalia 25,166 (no MoA, so carrying stands) = **394,485** → `working_capital_net` = **1,427,211** (+515,075 vs Q1).
- Spread: **174,500k = $0.601/share.** Branch B is what the Q1 convention says; Branch A is what the balance sheet says. This needs an owner ruling, not a silent pick.

**Fork 3 — newbuild convention now that commitments are sourced.** Q1 set `newbuild_capex_commitments: 0` on the §3.1/§9.6 reasoning that the remaining commitment buys delivered vessels of equal value, so net NB NAV = advances paid. That reasoning is unchanged and the figure is now citable either way.
- *Branch A — keep 0*, and move the 900,837 into the comment as sourced provenance. Net NB NAV = advances 532,660 = **$1.84/share**.
- *Branch B — populate 900,837* and mark the newbuilds at delivered market. That requires per-hull delivered marks for 25 vessels across six asset classes (VLCC, Newcastlemax, chemical, CSOV/CTV/MPASV, coasters, 1,400 TEU container), four of which have no §9.9 fit. **Not deliverable this quarter** — the offshore and chemical classes have no comparable sample, and §9.9 forbids adding classes without one.
- Independent of the fork, `newbuild_advances_paid` falls **759,807 → 532,660 (−227,147, −$0.783/share)** on the H1 deliveries, which is itself a >2pp drift-gate candidate and needs a dated annotation in `decisions/cmbt_log.md`.

**Fork 4 — the Newcastlemax 2-hull bridge** (§4). Branch A: accept the report's 40 (+6NB) as authoritative and annotate the Q1 basis as superseded. Branch B: hold the Q2 dry-bulk manifest until the Q1-2026 6-K is pulled and the reclassification is identified. Branch B is the house default under "trust the report, but verify the run's own NAV breakdown before attributing a band miss" — the two hulls are ~2% of the Newcastlemax book.
---
# APPENDIX B — extraction verification

## VERDICT: **WRITE WITH THE CORRECTIONS BELOW**

The balance-sheet primitives are sound — I re-footed every cross-foot independently off the page images and all reproduce. But the extraction has **one corrupting omission (a second fleet table at a different as-of date), one incoherent fork branch, and a manifest-scope gap that would double-count $219,985k ($0.758/share)** if the sheet is written as presented.

---

## 1. Figures re-footed — ALL reproduce

Verified off `img_001`/`img_002` (pp.2–3), not OCR (OCR renders cash as "191,574" — noise):

| Cross-foot | Result |
|---|---|
| Non-current assets → 7,908,869 | ✓ (9 lines) |
| Current assets → 699,035; +HFS 219,985 → 919,020; TOTAL 8,827,889 | ✓ |
| Equity 343,440+1,689,882+5,146+1,044−284,508+1,365,990 → 3,120,994 | ✓ |
| Non-current liabilities → 4,887,666; current → 819,229 | ✓ |
| 3,120,994+4,887,666+819,229 → 8,827,889 | ✓ |
| cash 151,574 + STI 8,271 → **159,845** | ✓ |
| bank 3,064,405 + other borr. 2,179,036 + notes 203,619 → **5,447,060** | ✓ |
| leases 4,014+1,587 → **5,601**; 5,447,060+5,601 = **5,452,661** printed in Note 16 | ✓ `img_031` |
| Note 16 roll-forward 5,549,789 → 5,452,661 | ✓ (1k rounding) |
| Operating WC → **301,244** | ✓ |
| Note 12 commitments: all 6 rows + all 5 columns → **900,837** | ✓ `img_027` |
| Note 12 PP&E roll-forward, all 4 columns → 6,875,419 / 532,660 / 4,935 / 48,002 | ✓ `img_025` |
| Note 7 segment: vessels → 6,875,419; AUC → 532,660; HFS → 219,985 | ✓ `img_017` |
| Note 15: 315,977,647 − 25,807,878 = **290,169,769** | ✓ `img_030` |
| Note 25: 28,320+36,072 = 64,392; +89,825 = 154,217; 45.0+44.8+8.3 = 98.1 | ✓ `img_047` |
| Fork 2 Branch A 1,252,711 / Branch B 1,427,211 / spread 174,500 = $0.601 | ✓ |
| Q1 debt itemisation → 5,238,160; Δ +208,900 | ✓ vs `inputs/balance_sheets/cmbt_2026-Q1.yaml` |

**Two corroborations the extraction missed that *support* it:**
- Note 12 "Transfer to assets held for sale **(173,196)**" ≈ Brugge+Brest 123,800 + Donoussa 49,400 = 173,200. Independently confirms Stella+Golden Myrtalia = 219,985 − 173,196 = **46,789** (extraction: 46,785; 4k rounding). The residual method is corroborated, not just asserted.
- Marine AUC **525,998** (Note 7) = Note 12's "aggregate amount of USD **526.0 million**" for 25 vessels. Ties the vessel count to the money.

**§0 blocking finding VERIFIED:** `ex99-1.htm` = 33 `<IMG>` tags, 235 chars of text; `ex99-2.htm` = 53 tags, 337 chars. Zero financial text. The staging gap is real and should be fixed.

---

## 2. Citations spot-checked — 14 of 14 VERIFIED, 2 imprecise

| # | Claim | Verdict |
|---|---|---|
| 1 | Note 26 three events, `img_049` | **VERIFIED** verbatim |
| 2 | Note 8 Donoussa "carrying value of USD 49.4 million… MoA subsequently signed on July 15, 2026, confirming management's assessment as at the reporting date", `img_019` | **VERIFIED** verbatim |
| 3 | Note 8 Brugge/Brest MoA 12 June, 224.0M price, 123.8M combined carrying, 100.2M gain | **VERIFIED** verbatim |
| 4 | Note 8 Stella/GM HFS since Dec 31 2025, no carrying values | **VERIFIED** |
| 5 | Note 6 "The vessels have been delivered in the third quarter of 2026… USD 100.2 million", `img_015` | **VERIFIED verbatim** — and it is a genuine Note 6 vs Note 8 ("expected") tense conflict; IN/OUT call correct either way |
| 6 | Note 12 "USD 0.9 billion (December 31, 2025: USD 1.6 billion)", `img_027` | **VERIFIED** verbatim |
| 7 | Note 12 "twenty-five vessels under construction… aggregate amount of USD 526.0 million", `img_025` | **VERIFIED** verbatim |
| 8 | Note 12 "two Hydrocat CTVs" | **VERIFIED** — appears on `img_025` (extraction gave no page; it is not on `img_027`) |
| 9 | Impairment: "independent broker valuations which indicate that the fair market value of the fleet exceeds its carrying value", `img_027` | **VERIFIED** verbatim |
| 10 | Note 16 "Secured FSO loan 161.1M / SOFR + 2.05% / 2030 / 110,619 / 110,619 / **109,937**" (Dec-25: 123,593/122,736), `img_032` p.33 | **VERIFIED** verbatim |
| 11 | Fleet page "FSO 2" owned, `img_073` p.21 | **VERIFIED** |
| 12 | Note 25 equity-accounted total 64,392, no FSO; TFG Marine +5%; Jiangsu Andefu 25% (`img_048`) | **VERIFIED** |
| 13 | Note 15 shares unchanged 290,169,769 | **VERIFIED** |
| 14 | TCE rates VLCC 92,403/64,853, Suezmax 96,108/35,204, NMax 37,960/24,114, Cape 32,656, FSO 88,540 (2025: 86,423), `img_074` | **VERIFIED** |

**Imprecise (not wrong):**
- **Newcastlemax delivery dates.** Extraction cites "Mineral Latvija (11 May), Mineral Eesti (28 May), Mineral Magyar (8 June), Mineral Lietuva (29 June) (`img_015` p.16)". `img_015` (Note 6) says only "During the month May" / "During June" and Note 12 (`img_025`) only *names* them. The dates live on the narrative timeline `img_067`–`img_069`, which reads **1 May** for Mineral Latvija, not 11 May. Bridge conclusion (all four in Q2) is unaffected.
- **89,825 FVTPL non-current** is not printed; it is 154,217 − 64,392. Presented as sourced.

**No back-solving violation.** Golden Myrtalia 25,166 is genuinely segment-pinned (sole Bocimar hull in Note 8). Stella is a residual and the extraction says so. Nothing was split out of an en-bloc into per-vessel marks.

---

## 3. Subsequent events — audited first, calls correct, one addition

Note 26 was audited first and all three IN/OUT calls are right (Windcat 65 advances IN / hull OUT; Donoussa asset IN at 49.4M, gain OUT; Bristol OUT entirely, on-water Suezmax at 30 Jun). The "fourth fact outside Note 26" (Brest/Brugge in Note 6) is a real and well-made catch.

**One post-period item not swept: the auditor's report is dated "Antwerp, 2 September 2026" (`img_051`), and it is an ISRE 2410 *review*, not an audit** — "we do not express an audit opinion." The extraction never characterises the assurance level of the figures feeding NAV.

---

## 4. The three blockers

- **(c) Newbuild commitments — GENUINELY RESOLVED.** I re-footed every cell of the Note 12 table both ways. 900,837 is cited, split by year and category. The `~$1.2bn` RED is retired.
- **(b) Held-for-sale — RESOLVED except Stella, but overstated.** "Four of five hulls are sourced or segment-pinned" is not right: **123.8M is a *combined* Brugge+Brest figure**, so neither hull is individually sourced. Only Golden Myrtalia (25,166) and the two aggregates are. Splitting 123.8 in half for per-hull marks would be a back-solve — flag it before anyone does.
- **(a) FSO — ownership resolved, value not.** Consolidation is well-supported by the three-way triangulation (the FSO loan line alone would not be dispositive; a consolidated borrowing can fund an on-lend). But see Finding 2 — the resolution has a consequence the extraction did not follow through.

---

## 5. What it missed

**Finding 1 — `img_059` "Key figures on 31 August 2026" is a second fleet table at the wrong vintage, and the extraction never mentions it. CORRUPTING.**
Ex-99.1 p.7 carries a full class-level fleet breakdown headed **"Key figures on 31 August 2026 ** Including newbuildings"**: DRY BULK 115 (46 Newcastlemax, 37 Capesize, 26 Kamsarmax, 4 Panamax, 2 Coasters), **CRUDE OIL TANKERS 24 (16 SUEZMAX, 6 VLCC, 2 FSO)**, CHEMICAL 16, CONTAINER 5, OFFSHORE 70, PORT 4.

This looks exactly like the 30-June table (`img_073`) but is **two months later and on a different basis** (totals incl. newbuildings): Suezmax **16** vs **18**, VLCC **6** vs **5+1NB**. The −2 Suezmax is Brest+Brugge delivering in Q3. The extraction flagged the *press release* as an as-of-27-August trap while missing the identical trap **inside the filing it was reading**. This is the repo's named recurring failure (snapshot integrity, CLAUDE.md), in the one document the sheet is being written from.

`img_059` also carries **"SHARE PRICE AT 31 AUGUST 2026 — CMBT NYSE 18.28 USD"**. Do not let that reach `watchlist.yaml`: a `current_price` never moves without rebasing `consensus_pnav`/`consensus_fwd_pe` from the same vintage.

**Finding 2 — Fork 1 Branch B ("zero the FSO") is incoherent as written. CORRUPTING; and I can close the precondition the extraction left open.**

Two corrections:

*(a) The double-count precondition RESOLVES — the extraction could have closed it with one grep.* `inputs/fleet_manifests/cmbt.yaml` line 15: `#   - 2 FSO (service contracts) -> shuttle_contracted_book`, and line 122 `off_curve_note: "2 FSO + 8 chemical + 47 owned Windcat + 3 HFS held at the balance-sheet level (§11.9)"`. The FSOs are **not** in the crude manifest, and `working_capital_net` never touches Euronav segment vessels. **No double-count exists.** Branch A is safe on that axis.

*(b) Branch B is not neutral — it is one-sided.* The **FSO's own secured debt, 109,937 ($0.379/share), is inside `total_debt` 5,447,060** (bank loans, Note 16 `img_032`). Zeroing `shuttle_contracted_book` while leaving that loan in place makes the FSO sleeve contribute **−109,937** to NAV — assets removed, debt retained. That is a ~$0.72/share understatement versus Branch A, in the *conservative-looking* direction, which is how it would pass unnoticed. Branch B is only coherent if the FSO loan is stripped from `total_debt` at the same time.

Note also the placeholder now has an external check the extraction didn't draw: a lender advanced and fully drew **110,619** against two 2002-built FSOs maturing 2030. That is evidence the $100M placeholder is *conservative*, not aggressive — which weakens the case for zeroing it further.

**Finding 3 — HFS values were resolved but never connected to manifest scope. This is the double-count that actually bites. CORRUPTING, $0.758/share.**

`inputs/fleet_manifests/cmbt.yaml` currently carries as **on-curve** rows:
```
line 39  CMBT_VLCC_Donoussa   class: VLCC     dwt: 299999  age: 10.25
line 46  CMBT_SUEZ_Stella     class: Suezmax  dwt: 165000  age: 15.25
line 55  CMBT_SUEZ_Brest      class: Suezmax  dwt: 156851  age: 3.25
line 56  CMBT_SUEZ_Brugge     class: Suezmax  dwt: 156851  age: 3.25
line 57  CMBT_SUEZ_Bristol    class: Suezmax  dwt: 156851  age: 2.25
```
Writing `working_capital_net` with HFS 219,985 inside it while those rows stand marks **Donoussa, Stella, Brest and Brugge twice** — once at an age-curve mark, once at HFS value. Euronav HFS alone is 194,819 = **$0.671/share**; with Golden Myrtalia (in the 37-Capesize cohort) it is 219,985 = **$0.758/share**. The extraction lists `working_capital_net` under "now sourceable" with no manifest caveat at all.

**Bristol correctly stays on-curve** (sale announced 11 Aug, not HFS at 30 Jun).

**Sub-finding — a Q1 error the extraction had the evidence to catch.** Note 8 states Stella and Golden Myrtalia "have been classified as an asset held for sale **since December 31, 2025**". The Q1 manifest header lists only **3** off-curve HFS (Ilma, Ingrid, Sienna) and carries Stella on-curve. So the Q1 sheet mis-scoped two hulls, and the Q2 refresh inherits it. Correct Q2 crude scope is **4 VLCC + 15 Suezmax on-curve**, with 4 crude hulls + 1 Capesize moved off-curve.

**Finding 4 — the entire crude Q1→Q2 bridge is absent.** The extraction spends §4 on a 2-hull Newcastlemax discrepancy (~2% of one dry-bulk cohort) and never reconciles the crude sleeve — the repo's core sector. Note 12 (`img_025`) states verbatim: *"During the first half of 2026, the Company took delivery of four Newcastlemax vessels…, **three VLCCs (Eburones, Menapii and Morini), two Suezmax vessels (Cap Grace and Cap Joseph)**, one chemical tanker (Bochem Callao), and one CSOV (Windcat Haarlem)."* Cap Grace (8 Apr) and Cap Joseph (27 Apr) and Morini (June) are **Q2** additions to the crude manifest. Priority inversion.

**Finding 5 — Note 23 litigation is unmentioned, and it fires a tripwire the Q1 sheet itself set.** `img_045` p.46 discloses three litigations. The Q1 yaml sets `governance_discount_pct: 0.0` with the explicit tripwire *"GOGL Bermuda appraisal / FourWorld Antwerp claim outcomes"*. Both moved inside H1:
- Antwerp, **30 March 2026**: court "rejected in full FourWorld's requests" for document production and preliminary measures.
- Bermuda, **21 May 2026**: court rejected the dissenting shareholders' claim to immediate cash at USD 14.49/share; recourse limited to Section 106(6) appraisal; court confirmed consistent methodology "will result in no material delta being owed". **Under appeal, pleaded November 2026.**
- Oceania/Black Swan: judgment reserved to end-2026, final judgment "towards the end of 2028".
- Management: *"not more likely than not that an outflow of resources will be required… no provision needs to be accounted for at the moment."*

The extraction's fork list has four forks and none is governance. This needed to be surfaced, not because the answer changes but because the Q1 sheet conditioned on it.

**Finding 6 — Note 20 (`img_041` p.42) unmentioned; two NAV-adjacent items.** Total 98,018 = shareholders loans to JVs 21,129 + derivatives 557 + cash guarantees 57,303 + other 19,029 (re-footed ✓).
- **Cash security USD 51.4M** ($0.177/share) lodged with the High Court of Malaysia, "estimated realisation period of approximately two years" — a recoverable asset excluded from both `cash_and_equivalents` and `working_capital_net`. Convention-consistent with Q1, but it is a known exclusion that should be stated.
- **19,029 "advancement for the development of ammonia-powered engines for its new bulk carriers… may be recovered through future engine deliveries"** — a newbuild-programme cost sitting *outside* `newbuild_advances_paid`.

**Finding 7 — the reclassification footnote makes Fork 3's drift number not clean. UNVERIFIED.** Both `img_002` and `img_025` carry: *"The current year presentation reclassified prepayments to assets under construction. To align with this reclassification, the Group re-presented the comparative information."* The extraction presents 759,807 → 532,660 (−227,147, −$0.783/share) as a clean delivery-driven >2pp drift candidate. Part of that may be presentation. Note 12 opens at AUC 739,373 on the re-presented basis; whether the Q1 6-K's 759,807 is on the same basis is **not verifiable from staged files**. *Settled by:* the Q1-2026 6-K (filed 2026-05-19) — the same document Fork 4 needs. Pull it once, close both.

**Finding 8 — `newbuild_advances_paid` 532,660 contains 6,662 of non-vessel AUC.** Note 7 splits marine 525,998 / Other 6,662 (port vessels, R&D, H2 infra, holding). Using the full line overstates the vessel newbuild book by **$0.023/share**. Q1 did the same, so it is convention-consistent — but Note 7 now permits precision.

**Finding 9 — minor, unmentioned:** *"All vessels financed with bank loans are subject to a mortgage to secure bank loans"* (`img_027`) — fleet-wide encumbrance. And the TCE table is headed **"First semester 2026"** — H1 averages, not Q2 marks; relevant to §10 vintage, not stated.

**Finding 10 — Stella 21,619 is false precision.** It is a residual of inputs rounded to 0.1M (123.8, 49.4), so it carries roughly ±70k. Write it as ~21.6M `[DERIVED]`, never as a sourced thousand-level figure.

---

## 6. Direction of error

| Figure | If wrong | Why |
|---|---|---|
| cash 159,845 / debt 5,447,060 / leases 5,601 / shares 290,169,769 / preferred 0 | **RECOVERABLE** | Re-footed from the statement of financial position, which cross-foots to 8,827,889; any error is visible on the next run |
| commitments 900,837 | **RECOVERABLE** | Fully cited + double-cross-footed; Fork 3 Branch A keeps it in a comment anyway |
| **HFS 219,985 into WC while 4 hulls stay on-curve** | **CORRUPTING** | Silent $0.758/share double-count; NAV rises and looks like a market move, not an error |
| **`img_059` 31-Aug counts used for a 30-Jun manifest** | **CORRUPTING** | Wrong-vintage fleet is invisible in outputs; exactly the failure mode CLAUDE.md names |
| **Fork 1 Branch B (zero FSO, keep FSO loan)** | **CORRUPTING** | One-sided; understates by ~$0.72/share in the direction that reads as prudence |
| NB advances 532,660 vs the reclass | **RECOVERABLE** | Drift gate catches it; annotation just needs the reclass caveat |
| Stella ~21.6M | **RECOVERABLE** | ±70k = ±$0.0002/share |
| 6,662 non-vessel AUC | **RECOVERABLE** | $0.023/share, convention-consistent with Q1 |
| Note 23 governance tripwire | **RECOVERABLE** | Judgmental, stored auditably per §15 |
| Note 20 exclusions | **RECOVERABLE** | Convention-consistent; disclosure gap only |

---

## Before writing

1. Move **Donoussa, Stella, Brest, Brugge** off-curve in `inputs/fleet_manifests/cmbt.yaml`; keep **Bristol** on-curve; move **Golden Myrtalia** out of the Capesize cohort. Crude on-curve becomes 4 VLCC + 15 Suezmax.
2. Add H1 crude deliveries **Morini** (VLCC), **Cap Grace**, **Cap Joseph** (Suezmax).
3. Ignore `img_059` entirely for manifest purposes; use `img_073` (30 June) only. Keep the 18.28 USD price out of the watchlist.
4. Fork 1: the double-count precondition is **closed** (FSOs are off-manifest). If Branch B is chosen, strip the 109,937 FSO loan from `total_debt` in the same edit or the sheet is internally inconsistent.
5. Label Stella `[DERIVED ~21.6M]` and Brugge/Brest `[COMBINED 123.8M — per-hull NOT sourced]`.
6. Pull the Q1-2026 6-K (filed 2026-05-19) — it closes Fork 4 *and* the reclassification question for Fork 3.
7. Surface Note 23 as a §15 tripwire update and Note 20's 51.4M / 19,029 as known exclusions.
---
# APPENDIX C — crude fleet bridge Q1→Q2 (verified)

# TRACK C — CMBT crude fleet bridge Q1→Q2 (as-of 2026-06-30)

**Scope note.** "C-1" is not defined anywhere in the repo (grep across `decisions/`, `PLAN.md`, `outputs/` returns only the unrelated 2026-07-02 crude-reweight "C-1" and a METHODOLOGY_AUDIT item). I treat it as the orchestrator's label for the owner's held-for-sale ruling (off-curve move + carrying-vs-agreed basis, `cmbt_1.md` §5 Fork 2; `cmbt_verdict.md` "Before writing" items 1 and 5). The manifest diff below is identical under either valuation branch; only the balance-sheet line differs (Track B).

Age convention: the Q1 header says `Ages = 2026.25 − built_year` (`inputs/fleet_manifests/cmbt.yaml:26`); every Q2 manifest in the repo uses `Ages = 2026.5 − built` (`dht.yaml:13`, `sb.yaml:25`, `stng.yaml:20`, `cmdb.yaml:6`). So built-2026 → **0.5**, and every surviving row rolls **+0.25**.

## 1. Adds — the nine H1 deliveries

Master list, Note 12 `img_025` p.26, verbatim: "During the first half of 2026, the Company took delivery of four Newcastlemax vessels (Mineral Latvija, Mineral Magyar, Mineral Eesti and Mineral Lietuva), three VLCCs (Eburones, Menapii and Morini), two Suezmax vessels (Cap Grace and Cap Joseph), one chemical tanker (Bochem Callao), and one CSOV (Windcat Haarlem)."

| Hull | Class → value class | Delivery date (citation) | Qtr | Built / dwt (citation) | Age @2026.5 | eco | scrubber | charter_status |
|---|---|---|---|---|---|---|---|---|
| Eburones | VLCC | "On January 12, 2026, the Company took delivery of the VLCC Eburones (2026 – 319,000 dwt)" — Note 6 `img_015` p.16 | **Q1** | 2026 / 319,000 (same) | 0.5 | true | false (default) | spot — **already in manifest**, `cmbt.yaml:41`; age roll only |
| Menapii | VLCC | "On March 23, 2026 … VLCC Menapii (2026 – 319,000 dwt)" — `img_015` | **Q1** | 2026 / 319,000 | 0.5 | true | false | spot — **already in manifest**, `cmbt.yaml:42`; age roll only |
| **Morini** | VLCC | "10 June 2026 — CMB.TECH took delivery of the VLCC Morini (2026 – 319,000 dwt)" — Ex-99.1 p.16 `img_068`; Note 6 `img_015`: "During June 2026 … as well as the VLCC Morini (2026 – 319,000 dwt)" | **Q2 ADD** | 2026 / 319,000 | 0.5 | true | not stated on any page read → default false per header `cmbt.yaml:26` | **UNVERIFIED** — 20-F rows are unnamed TK300K-4/5; sisters Eburones/Menapii are Spot (`outputs/cmbt_onboarding/01_crude_fleet.md:70-71`). Draft `spot`. Strip-only field: `nav.py` never reads `charter_status` (grep empty) → NAV-neutral |
| **Cap Grace** | Suezmax | "On April 8, 2026, the Company took delivery of the Suezmax Cap Grace (2026 – 156,000 dwt)" — `img_015`; "8 April 2026" — Ex-99.1 p.15 `img_067` | **Q2 ADD** | 2026 / 156,000 | 0.5 | true | not stated → false | `time_charter`: 20-F "Our Fleet" TC + Q1 6-K 1-yr extension to 10-yr with profit split (`01_crude_fleet.md:92,94`); rate undisclosed |
| **Cap Joseph** | Suezmax | "On April 27, 2026 … Suezmax Cap Joseph (2026 – 156,000 dwt)" — `img_015`; "27 April 2026" — `img_067` | **Q2 ADD** | 2026 / 156,000 | 0.5 | true | not stated → false | `time_charter`, same sources |
| **Mineral Latvija** | Newcastlemax → Cape | "11 May 2026 … Mineral Latvija (2026 – 210,000 dwt)" — `img_067`; Note 6 `img_015`: "During the month May … Mineral Latvija (2026 – 210,000 dwt) and Mineral Eesti (2026 – 210,000 dwt)" | **Q2 ADD** | 2026 / 210,000 | 0.5 | true | not stated → false | spot (cohort convention `cmbt.yaml:84`) |
| **Mineral Eesti** | Newcastlemax → Cape | "28 May 2026 … Mineral Eesti (2026 – 210,000 dwt)" — `img_068` | **Q2 ADD** | 2026 / 210,000 | 0.5 | true | false | spot |
| **Mineral Magyar** | Newcastlemax → Cape | "8 June 2026 … Mineral Magyar (2026 – 210,000 dwt)" — `img_068`; Note 6: "During June 2026 … Mineral Magyar … and Mineral Lietuva" | **Q2 ADD** | 2026 / 210,000 | 0.5 | true | false | spot |
| **Mineral Lietuva** | Newcastlemax → Cape | "29 June 2026 — CMB.TECH took delivery of the Newcastlemax bulk carrier Mineral Lietuva (2026 – 210,000 dwt)" — Ex-99.1 p.17 `img_069` | **Q2 ADD** (one day before NAV date — IN) | 2026 / 210,000 | 0.5 | true | false | spot |

Notes. (a) Build year and dwt for all seven Q2 adds are stated **in the H1 filing itself** — no fallback to the 20-F needed; the Q1 manifest carried none of them as newbuild rows (grep: only Eburones/Menapii). (b) Scrubber: none of the pages read (Notes 6/8/12/26, timeline, fleet page) mentions scrubbers; the header already records "Scrubber UNDISCLOSED in the SEC filings (default false)". Ice: no field exists (`vessel_values.py:28` "ice-class: not modelled"). (c) The verdict (§2) says `img_067` reads "1 May" for Mineral Latvija — **my read of `img_067` is "11 May 2026"**; `cmbt_1.md`'s date stands. Q2 either way. (d) 210,000 dwt is load-bearing for the Cape curve (dwt-scaled, CLAUDE.md) — it is filing-stated, not rounded.

## 2. Off-curve moves — CONDITIONAL on the C-1 ruling

| Hull | Q1 row | Filing identity | Age @2026.5 | HFS status (Note 8 `img_019` p.20, verbatim) | Carrying value at 30 Jun |
|---|---|---|---|---|---|
| Donoussa | `cmbt.yaml:39` VLCC 299,999 dwt age 10.25 | "Donoussa (2016 – 299,999 dwt)" | 10.5 | "accounted for as an asset held for sale as at June 30, 2026"; MoA "subsequently signed on July 15, 2026"; gain 74.3M "expected during the fourth quarter" | **USD 49.4M — INDIVIDUALLY sourced** ("had a carrying value of USD 49.4 million") |
| Brest | `cmbt.yaml:55` Suezmax 156,851 age 3.25 | "Brest (2023 – 156,851 dwt)" | 3.5 | MoAs "on June 12, 2026, for a combined net sales price of USD 224.0 million … combined carrying value of USD 123.8 million"; delivered Q3 (Note 6 `img_015`: "have been delivered in the third quarter of 2026") | **123.8M COMBINED with Brugge — no per-hull figure exists.** Do not halve it (back-solve, CLAUDE.md) |
| Brugge | `cmbt.yaml:56` same | "Brugge (2023 – 156,851 dwt)" | 3.5 | same | same aggregate |
| Stella | `cmbt.yaml:46` Suezmax 165,000 age 15.25 | "Suezmax Stella (2011 – 165,000 dwt)" | 15.5 | "classified as an asset held for sale since December 31, 2025, and this status remains unchanged as at June 30, 2026" | **NOT disclosed. RESIDUAL ~21.6M [DERIVED]**: Euronav HFS 194,819 (Note 7 `img_017` p.18) − 123,800 − 49,400 = 21,619; cross-check via Note 12 `img_025` "Transfer to assets held for sale (173,196)": 219,985 − 173,196 − 25,166 = 21,623. ±0.1M rounding — never write it at thousand precision |
| Golden Myrtalia (dry) | `cmbt.yaml:68` `CMBT_CAPE_2011` count 1, dwt 180000, age 15.25 — the sole 2011 Capesize, already flagged "held for sale" in `02_drybulk_fleet.md:78` ("Golden Myrtalia (177,979; 2011; SWS)") | "Capesize vessel Golden Myrtalia (2011 - 177,979 dwt)" | 15.5 | HFS "since December 31, 2025" | **25,166k — segment-pinned**: Note 7 `img_017` "Assets held for sale" Bocimar column 25,166 (Euronav 194,819; total 219,985), and Golden Myrtalia is the only Bocimar hull in Note 8 |

Foot: 49,400 + 123,800 + 21,619 + 25,166 = 219,985 = balance-sheet HFS (`img_017` Total). The Q1 mis-scope is real: Stella and Golden Myrtalia were HFS at 31 Dec 2025 yet on-curve at Q1, while the Q1 sheet's 137,513 HFS line (attributed to Ilma+Ingrid+Sienna, `inputs/balance_sheets/cmbt_2026-Q1.yaml:23-24`) necessarily contained them too — a ~46.8M [DERIVED] Q1 double-count to annotate in `cmbt_log.md`.

Where the value lands is Track B's: the Q1 convention folds HFS into `working_capital_net` (`cmbt_2026-Q1.yaml:12-30`); the schema also has a dedicated `held_for_sale` field (`nav.py:72,121`, `loaders.py:183`); the DHT Q2 precedent kept `working_capital_net` plus a `fleet_summary.held_for_sale` count (`dht_2026-Q2.yaml:19-29`, `dht.yaml:248`). Basis fork for the ruling: carrying 219,985 vs agreed (224.0M Brugge+Brest sourced; Donoussa 49.4 + 74.3 = 123.7M derived; Stella/Golden Myrtalia have no MoA → carrying either way).

## 3. Removals / sold-and-delivered in Q2

**No on-curve hull vanished.** Q1 16 Suezmax (`cmbt.yaml:44-59`) + Cap Grace + Cap Joseph = 18 = fleet page; Q1 4 VLCC + Morini = 5 = fleet page. Departures were all already off-curve at Q1: Ilma + Ingrid (Note 6 `img_015`: "delivered to their new owners in the second quarter of 2026, generating a gain of USD 98.2 million") and Sienna (Note 8: "delivered to its new owner on June 2, 2026 … USD 29.2 million") → drop from `off_curve_note` line 18 and from the sheet's HFS line. **Bristol stays on-curve** at age 2.5: sale announced post-NAV-date (Note 26 `img_049` p.50: "On August 11, 2026, the Company announced the sale of the Suezmax Bristol (2024 - 156,851 dwt)") and absent from Note 8. Windcat 65 (Note 26, 14 July) is not crude.

## 4. Count check against the 30-June fleet page (`img_073` p.21 — NOT `img_059`, which is 31 August)

Page: TANKER 26 = SUEZMAX 18 + VLCC 5 (+1 NB) + FSO 2 ✓; DRY-BULK 115 = NEWCASTLEMAX 40 (+6 NB) + CAPESIZE 37 + KAMSARMAX 26 + PANAMAX 4 + COASTERS (+2 NB) ✓; CONTAINER 5 = 4 + 1 NB.

- VLCC: 4 (Q1) + 1 Morini = **5 = page ✓** → − Donoussa = **4 on-curve**.
- Suezmax: 16 (Q1) + 2 = **18 = page ✓** → − Brest − Brugge − Stella = **15 on-curve**.
- Crude on-curve **19** (was 20). Agrees with the 8/27 PR's "4 (+1NB) VLCCs and 15 Suezmaxes on the water" (`cmbt_1.md` §1) — a derived corroboration, different basis.
- Capesize: 37 = page ✓ → − Golden Myrtalia = **36 on-curve**. Newcastlemax: 38 + 4 = **42 vs page 40** — Fork 4 stays OPEN (`cmbt_1.md` §4); the four adds are individually cited so they go in, but the cohort total is not settled until the Q1-2026 6-K is pulled.
- `on_curve_total`: 19 + 4 Ctr + 30 Pana + 36 + {40|42} = **129 (page basis, coincidentally = Q1) | 131 (bridge basis)**.

Guards that fire on this diff: `tests/test_cmbt.py:24-34` pins VLCC 4 / Suezmax 16 / Cape 75 / total 129 and loads `"2026-Q1"` — must be re-pinned with the ratified counts; the pair guard (`tests/test_quarter_coherence.py:244-247` lists CMBT as the Q1-lagging specimen) requires `balance_sheets/cmbt_2026-Q2.yaml` in the same commit as `report_date: 2026-Q2`.

## 5. Drafted manifest diff (yaml fragment — DRAFT ONLY, nothing written)

```yaml
# report_date: 2026-Q1 -> 2026-Q2  (lands WITH balance_sheets/cmbt_2026-Q2.yaml — pair guard)
# header L26: "Ages = 2026.25 − built_year" -> "Ages = 2026.5 − built_year"; every surviving row age += 0.25
# header L10: "4 VLCC + 16 Suezmax = 20" -> "4 VLCC + 15 Suezmax = 19"
# header L18: "3 held-for-sale (Ilma, Ingrid VLCC + Sienna Suezmax)" -> "5 held-for-sale (Donoussa VLCC; Stella,
#   Brest, Brugge Suezmax; Golden Myrtalia Capesize) — Ilma/Ingrid/Sienna DELIVERED Q2 (Note 6 img_015, Note 8 img_019)"
vessels:
  # ---- VLCC (4): −Donoussa +Morini ----
  # DELETE [C-1 CONDITIONAL]: CMBT_VLCC_Donoussa (Q1 L39) — HFS at 30 Jun, Note 8 img_019 p.20 "carrying value of USD 49.4 million"
  - {id: CMBT_VLCC_Atrebates, class: VLCC, dwt: 319000, age: 1.5, scrubber: false, eco: true, charter_status: spot, charter_rate: null, count: 1}  # age roll only
  - {id: CMBT_VLCC_Eburones,  class: VLCC, dwt: 319000, age: 0.5, scrubber: false, eco: true, charter_status: spot, charter_rate: null, count: 1}  # Q1 hull, dely 12 Jan 2026 (Note 6 img_015); age roll only
  - {id: CMBT_VLCC_Menapii,   class: VLCC, dwt: 319000, age: 0.5, scrubber: false, eco: true, charter_status: spot, charter_rate: null, count: 1}  # Q1 hull, dely 23 Mar 2026 (Note 6 img_015); age roll only
  - {id: CMBT_VLCC_Morini,    class: VLCC, dwt: 319000, age: 0.5, scrubber: false, eco: true, charter_status: spot, charter_rate: null, count: 1}
    # ADD Q2 — dely 10 June 2026, Ex-99.1 p.16 img_068 "VLCC Morini (2026 – 319,000 dwt)"; Note 6 img_015 "During June 2026"; Note 12 img_025.
    # age 2026.5−2026; eco = built ≥ 2015; scrubber not stated in H1 report -> default false (header L26).
    # charter_status UNVERIFIED (20-F rows unnamed TK300K-4/5; sisters spot, 01_crude_fleet.md:70-71) — strip-only, NAV-neutral.
  # ---- Suezmax (15): +CapGrace +CapJoseph −Brest −Brugge −Stella ----
  # DELETE [C-1 CONDITIONAL]: CMBT_SUEZ_Stella (Q1 L46) — Note 8 "held for sale since December 31, 2025 … unchanged as at June 30, 2026"; value RESIDUAL ~21.6M [DERIVED]
  # DELETE [C-1 CONDITIONAL]: CMBT_SUEZ_Brest (Q1 L55), CMBT_SUEZ_Brugge (Q1 L56) — Note 8 MoA 12 Jun 2026, "combined carrying value of USD 123.8 million" — NO per-hull split
  # KEEP, age +0.25 only: CapTheodora 18.5, Fraternity 17.5, CaptainMichael 14.5, Maria 14.5, CapCorpusChristi 8.5, CapPembroke 8.5,
  #   CapPortArthur 8.5, CapQuebec 8.5, Cedar 4.5, Cypres 4.5, Bristol 2.5, Helios 2.5, Orion 2.5
  #   Bristol STAYS: sale announced 11 Aug 2026 (Note 26 img_049), absent from Note 8 -> on the water at 30 Jun.
  - {id: CMBT_SUEZ_CapGrace,  class: Suezmax, dwt: 156000, age: 0.5, scrubber: false, eco: true, charter_status: time_charter, charter_rate: null, count: 1}
    # ADD Q2 — Note 6 img_015 "On April 8, 2026 … Cap Grace (2026 – 156,000 dwt)"; Ex-99.1 p.15 img_067 "8 April 2026".
    # TC: 20-F Our Fleet + Q1 6-K 1-yr extension to 10-yr w/ profit split (01_crude_fleet.md:92,94); rate undisclosed.
  - {id: CMBT_SUEZ_CapJoseph, class: Suezmax, dwt: 156000, age: 0.5, scrubber: false, eco: true, charter_status: time_charter, charter_rate: null, count: 1}
    # ADD Q2 — Note 6 img_015 "On April 27, 2026 … Cap Joseph (2026 – 156,000 dwt)"; img_067 "27 April 2026". TC as Cap Grace.
  # ---- DRY BULK, Cape class ----
  # DELETE [C-1 CONDITIONAL]: CMBT_CAPE_2011 count 1 (Q1 L68) = Golden Myrtalia, sole 2011 Capesize (02_drybulk_fleet.md:78);
  #   Note 8 img_019 "Golden Myrtalia (2011 - 177,979 dwt) … held for sale since December 31, 2025"; carrying 25,166k = Bocimar HFS column, Note 7 img_017.
  - {id: CMBT_CAPE_2026, class: Cape, dwt: 210000, age: 0.5, scrubber: false, eco: true, charter_status: spot, count: 6}
    # was count 2 (Q1 L84, Mineral Malta + Europa). +4 Q2: Latvija 11 May (img_067), Eesti 28 May (img_068), Magyar 8 Jun (img_068),
    # Lietuva 29 Jun (img_069) — each "(2026 – 210,000 dwt)"; Note 6 img_015; Note 12 img_025. dwt load-bearing (dwt_scaled), filing-stated.
    # NMax bridge OPEN: 38 + 4 = 42 vs fleet page 40 (+6 NB) img_073 — Fork 4; house default HOLD the dry sleeve until the Q1-2026 6-K is pulled.
fleet_summary:
  on_curve_total: 129            # page basis (19 + 4 + 30 + 40 + 36); 131 on the 42-NMax bridge basis — settle Fork 4 first; re-pin test_cmbt.py:24-34
  VLCC_count: 4
  Suezmax_count: 15
  Cape_count: 76                 # 40 NMax + 36 Capesize (78 if 42 NMax)
  Pana_count: 30
  Ctr_Large_count: 4
  held_for_sale: 5               # DHT precedent dht.yaml:248 — Donoussa, Stella, Brest, Brugge, Golden Myrtalia (values on the sheet, Track B)
  off_curve_note: "2 FSO + 8 chemical + Windcat owned (Q1 '47' — re-derive, Haarlem CSOV dely 4 May) + 5 HFS held at the balance-sheet level (§11.9)"
```

**UNVERIFIED / open:** Morini charter status (settled by the FY2026 20-F "Our Fleet" row, or the Q1-2026 6-K fixture list); Newcastlemax 42-vs-40 (settled by the Q1-2026 6-K, filed 2026-05-19, not staged — `inputs/filings/CMBT/` holds only Aug–Sep accessions); per-hull Brest/Brugge and Stella values (settled only by the FY2026 20-F Note 8 per-vessel HFS table). Everything else above traces to a page image or a repo line.
---
# APPENDIX D — bridge verification

**VERDICT: USE WITH CORRECTIONS** — the crude bridge (−Donoussa −Stella −Brest −Brugge +Morini +Cap Grace +Cap Joseph; Bristol stays; 4 VLCC + 15 Suezmax) is correct and every load-bearing figure traces to a page image I re-read. `img_059` (31 Aug) was not used anywhere (all counts match `img_073`: Suezmax 18 / VLCC 5+1, not 16 / 6; no 18.28 price leaked). Corrections are to the dry-bulk fragment's internal consistency and to a few labels; none corrupt the crude deliverable.

## 1. Citation spot-checks (14)

| # | Claim | Result |
|---|---|---|
| 1 | Eburones 12 Jan / Menapii 23 Mar 2026, 319,000 dwt — Note 6 `img_015` p.16 | VERIFIED (page footer "16") |
| 2 | Morini 10 June 2026 — `img_068`; Note 6 "During June 2026 … VLCC Morini" | VERIFIED |
| 3 | Cap Grace 8 Apr / Cap Joseph 27 Apr, 156,000 dwt — `img_067` p.15 + Note 6 | VERIFIED (image read) |
| 4 | Mineral Latvija **11 May** (work refutes verdict's "1 May") | VERIFIED — image `img_067` reads "11 May 2026"; the verdict's "1 May" is an OCR artifact (`ocr/img_067.txt`). Independently corroborated by the 8/27 PR delivery table `scratchpad/pr827.txt:412-414` and the repo's own `02_drybulk_fleet.md:76`. The work missed both corroborations. |
| 5 | Eesti 28 May / Magyar 8 Jun / Lietuva 29 Jun, 210,000 dwt — `img_068`/`img_069` | VERIFIED (OCR + `pr827.txt:415-427`) |
| 6 | Donoussa HFS at 30 Jun, carrying 49.4M, MoA 15 Jul, gain 74.3M Q4 — Note 8 `img_019` p.20 | VERIFIED verbatim |
| 7 | Brest/Brugge MoA 12 Jun, 224.0M combined, 123.8M combined carrying, delivered Q3 — `img_019` + Note 6 | VERIFIED; no per-hull split exists on the page |
| 8 | HFS split Euronav 194,819 / Bocimar 25,166 / total 219,985 — Note 7 `img_017` p.18 | VERIFIED from the image. Note: OCR reads "194,319" (`ocr/img_017.txt`); the work used the image figure, which is the one that foots. |
| 9 | Note 12 `img_025` p.26 delivery list + "Transfer to assets held for sale (173,196)" | VERIFIED verbatim |
| 10 | Bristol sale announced 11 Aug 2026 — Note 26 `img_049` | VERIFIED (page number p.50 inferred from the img+1 pattern confirmed on 015/017/019/025 — not read off the page) |
| 11 | Fleet page `img_073` p.21: Suezmax 18, VLCC 5 (+1), FSO 2; NMax 40 (+6), Cape 37, Kam 26, Pana 4, Coasters +2 | VERIFIED |
| 12 | Repo lines `cmbt.yaml:10,18,26,39,41-42,44-59,46,55,56,68,84,116`; `test_cmbt.py:24-34`; `test_quarter_coherence.py:244-247`; `nav.py:72,121`; `loaders.py:183`; `dht.yaml:13,248`; `dht_2026-Q2.yaml:19-29`; `sb.yaml:25`; `stng.yaml:20`; `cmdb.yaml:6`; `vessel_values.py:28`; `01_crude_fleet.md:70-71,92,94`; `02_drybulk_fleet.md:78` | ALL VERIFIED |
| 13 | "`nav.py` never reads `charter_status` → NAV-neutral" | VERIFIED, and understated: the only consumer is `dividend_strip.py:95`, which reads it **only when `charter_rate is not None`**. With `charter_rate: null` Morini's `charter_status` is fully inert (strip included); loader default is `"spot"` (`loaders.py:82`). The UNVERIFIED flag is harmless. |
| 14 | "Ex-99.1 p.16 `img_068`" exhibit attribution | UNVERIFIED — the staged `0000919574-26-006193_…ex99-1.htm` / `ex99-2.htm` are 56-character stubs (no text); I cannot tell which exhibit the narrative Half Year Report vs the Financial Report sits in. Non-load-bearing (page image + verbatim quote is the citation); settle by opening the accession index `scratchpad/idx.html`. |

## 2. Recomputations — all foot

- 224.0 − 123.8 = 100.2 ✓ (Note 8 gain). 49.4 + 74.3 = 123.7 ✓ (Donoussa agreed, derived).
- 49,400 + 123,800 = 173,200 vs Note 12 transfer 173,196 ✓ (4k rounding).
- 194,819 − 123,800 − 49,400 = 21,619; 219,985 − 173,196 − 25,166 = 21,623; 194,819 + 25,166 = 219,985 ✓. Stella residual is correctly [DERIVED]; it additionally assumes no H1 impairment on the two legacy HFS hulls (IFRS 5 stops depreciation, so the two routes agreeing to ±4k is a real cross-check).
- Q1 double-count 21,619 + 25,166 = 46,785 ≈ 46.8M ✓ [DERIVED — assumes Mar-31 carrying = Jun-30 carrying; Q1 6-K not staged].
- Q1 manifest rows: Cape 75 (NMax by dwt ≥208k = 38, Capesize 37), Pana 30 ✓. VLCC 4+1 = 5 = page; Suezmax 16+2 = 18 = page; 18−3 = 15; 5−1 = 4 ✓. Tanker 26 = 18+5+1+2 ✓; Dry 115 = 40+6+37+26+4+2 ✓. 129/131 and 76/78 ✓.
- Ages: every surviving row +0.25; 2026.5−2026 = 0.5; Bristol 2.5; Donoussa 10.5; Stella 15.5 ✓.

## 3. Snapshot integrity

- As-of 30 Jun throughout: Brest/Brugge IN (delivered Q3), Bristol IN (sale 11 Aug), Ilma/Ingrid/Sienna OUT (delivered Q2), Donoussa HFS per the filing's own reporting-date assessment despite the 15 Jul MoA ✓. Lietuva 29 Jun correctly IN.
- `img_059` untouched ✓. No price typed ✓.
- One wrinkle the work glosses: `img_073` reads "Our fleet (including newbuildings **& vessels on charter**)" — the page basis is not strictly owned. It foots to owned for VLCC/Suezmax anyway, but this is one more reason the page's NMax "40" cannot arbitrate against per-hull-cited deliveries.

## 4. Findings

1. **Draft yaml fragment is not cross-foot consistent (RECOVERABLE, must fix before landing).** Rows encode 42 NMax (`CMBT_CAPE_2026 count: 6`, minus `CAPE_2011`) = Σ rows 131, while `fleet_summary.on_curve_total: 129` / `Cape_count: 76` encode the page's 40. `cmbt.yaml:116` says `on_curve_total` "MUST equal Σ vessel-row counts (cross-foot gate)". The only citable draft is 131/78: all four deliveries are individually dated in the filing (Note 6, Note 12, `pr827.txt`), the Q1 38 is reconciled to the 20-F table (`02_drybulk_fleet.md:28-30`), and "40" has no per-hull support. Write 131/78 and carry Fork 4 as an annotation, or hold the whole dry sleeve — not a 129 summary over 131 rows.
2. **Missed dependency (RECOVERABLE, cross-track):** putting 7 delivered hulls on-curve requires `newbuild_advances_paid` to fall 759,807 → 532,660 in the same commit (Note 12 AUC balance `img_025`; transfers 986,113 out of AUC), else the delivered hulls are double-counted (on-curve + still in advances). `cmbt_1.md` Fork 3 has the number; the manifest diff should name it as a pair condition alongside the balance-sheet pair guard.
3. **DHT precedent mis-characterised (RECOVERABLE, bears on the C-1 basis fork):** `dht_2026-Q2.yaml:26-28` carries Bauhinia at the **realized** $51.0M net ("supersedes the agreed $51.5M"), not "agreed". The precedent is realized/agreed net price, not carrying — relevant to which branch of Fork 2 is "the house convention".
4. **Label nit (RECOVERABLE):** "the nine H1 deliveries" — Note 12 lists eleven (adds Bochem Callao + Windcat Haarlem); nine is the tanker+dry subset.
5. **Uncited corroboration left on the table:** the 8/27 PR (`inputs/filings/CMBT/0000919574-26-005821_…ex_99-1.htm`, `pr827.txt:404-427`) dates all seven Q2 adds and would have closed the 1-vs-11 May dispute with a second source; it also gives Q2 actual / Q3-QTD fixed cover (VLCC 83%, Suezmax 73%) — the manifest's `spot_coverage_pct` comment (`cmbt.yaml:105-107`) is Q1-6-K vintage (strip-side only).
6. **Fork 4 lead, not a resolution:** Note 12 itself says "six Newcastlemax bulk carriers" under construction at 30 Jun, agreeing with the page's 6 NB and disagreeing with the bridge's 8−4 = 4. Since 20-F NB program = 10 and Q1 = 8, six NB at 30 Jun implies either two NMax left the on-water fleet in Q2 (Note 12 "Disposals and cancellations (81,498)" is the only candidate line, likely drydock derecognition) or two were added to the orderbook. The 8/27 PR's unchanged "average age 3.2y" after four 0-year deliveries suggests stale boilerplate. Settled only by the Q1-2026 6-K + the Q2 newbuild table.
7. Golden Myrtalia's Q1 row dwt 180,000 vs filing 177,979 (`img_019`) — pre-existing rounding in a dwt-scaled class; removal moots it.

Nothing found is CORRUPTING. The crude sleeve of the diff can be landed as drafted (subject to the C-1 ruling); the dry sleeve fragment needs item 1 fixed first.