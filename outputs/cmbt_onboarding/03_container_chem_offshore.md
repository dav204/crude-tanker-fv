I have all the data I need. The CSOV table confirms 6 CSOVs total (2 on-water: Windcat Amsterdam 2025, Windcat Rotterdam 2025; 4 NB hull numbers 552207-552210, all Damen, 2026, all under "Owned Vessels" with no asterisk = 100% owned). The "MP-ASV" (CSOV XL) NB appears separately (2028). 

I now have complete, sourced, confidence-flagged data for all three segments. Let me compile the final markdown deliverable.

---

# CMB.TECH NV (NYSE: CMBT) — Container / Chemical / Offshore-Wind segments at Q1-2026 (2026-03-31)

**Sources (both SEC EDGAR, CIK 1604481):**
- **6-K Q1-2026 results**, Exhibit 99.1 (filed 19 May 2026): `https://www.sec.gov/Archives/edgar/data/1604481/000091957426003591/d12164570_ex99-1.htm`
- **FY2025 20-F** (filed 21 Apr 2026, vintage 2025-12-31; per-vessel fleet table + segment balance sheet + JV notes): `https://www.sec.gov/Archives/edgar/data/1604481/000160448126000004/eurn-20251231.htm`

**Vintage note:** The 6-K gives Q1-2026 (2026-03-31) segment *counts and charter terms* but only *consolidated* balance-sheet figures. Per-vessel built years/yards and per-segment book values come from the FY2025 20-F (2025-12-31) — the most recent per-vessel and per-segment disclosure. Where the two differ on count (one extra CTV, one extra CSOV delivered in Q1-2026), the 6-K Q1 count is used as headline and flagged.

**Fetch method that works (the prompt's fetcher/WebFetch both 403 on a generic UA):** `curl -sSL -A "crude-tanker-fv research <email>" <sec.gov url>` — SEC requires a descriptive UA. The 301→200 redirect must be followed (`-L`).

---

## (a) DELPHIS — Container

**Count: 4 vessels on the water + 1 newbuild. All 100% owned** (FY2025 20-F fleet table, all under "Owned Vessels", no JV asterisk). CONFIRMED.

| Vessel | TEU | Built | Yard | Charter status |
|---|---|---|---|---|
| CMA CGM Masai Mara | ~6,000 (75,830 dwt) | 2023 | Yangfan (Qingdao Yangfan) | Time Charter — CMA-CGM, 10-yr TC |
| CMA CGM Zingaro | ~6,000 (75,830 dwt) | 2024 | Yangfan | Time Charter — CMA-CGM, 10-yr TC |
| CMA CGM Etosha | ~6,000 (77,000 dwt) | 2024 | Yangfan | Time Charter — CMA-CGM, 10-yr TC |
| CMA CGM Dolomites | ~6,000 (77,000 dwt) | 2024 | Yangfan | Time Charter — CMA-CGM, 10-yr TC |
| **NB:** Yara Eyde | 1,400 | 2026 (NB, exp. Q4-2026 delivery) | Qingdao Yangfan | Time Charter — Yara/NCL (North Sea Container Line), 15-yr TC. World's first dual-fuel ammonia container ship; operated by NCL Oslofjord AS |

- 6-K Q1-2026 prose (CONFIRMED): "CMB.TECH's 4 x 6,000 TEU (average age 1.8y) and 1 NB 1,400 TEU container vessels are all employed under 10 to 15-year time charter contracts."
- **Charter rate:** not disclosed per-vessel (only tenor + counterparty). The 6-K reports a Container segment "Average time charter rate" of **USD 29,378/day** (Q1-2026). CONFIRMED for the segment, ESTIMATED as a per-vessel proxy.
- The 4x6,000 TEU are "ready to be fitted with ammonia engines." TEU figure is CONFIRMED (6-K prose "6,000 TEU"); the dwt values (75,830 / 77,000) are the table's stated capacity.

**Delphis segment book value (2025-12-31, FY2025 20-F segment balance sheet) — CONFIRMED:**
- Vessels: **USD 210,530k** · Assets under construction: **USD 5,147k** · Total non-current assets: **USD 215,677k**

---

## (b) BOCHEM — Chemical Tankers

**Count: 8 vessels on the water + 6 chemical NB + 2 product/bitumen NB. All 100% owned** (all under "Owned Vessels", no JV asterisk). CONFIRMED.

All built at **CMJL Dingheng** = China Merchants Jinling Shipyard (Weihai). All **stainless steel** (20-F: "high quality and modern stainless steel chemical tankers"; "ammonia-ready"). IMO class not stated explicitly per-vessel in the filings (ESTIMATED: 25k-dwt stainless STJS-pool chemical tankers are typically IMO II).

| Vessel | dwt | Built | Stainless/coated | Charter |
|---|---|---|---|---|
| Bochem Houston | 26,000 | 2023 | Stainless | STJS Pool (Stolt) |
| Bochem Rotterdam | 26,000 | 2023 | Stainless | STJS Pool (Stolt) |
| Bochem Casablanca | 25,000 | 2024 | Stainless | Time Charter |
| Bochem Shanghai | 25,000 | 2024 | Stainless | Time Charter |
| Bochem New Orleans | 25,000 | 2024 | Stainless | Time Charter |
| Bochem Brisbane | 25,000 | 2024 | Stainless | Time Charter |
| Bochem Santos | 25,000 | 2025 | Stainless | Time Charter (sale-and-leaseback, 15-yr bareboat) |
| Bochem Callao | 25,000 | 2026 (delivered 13 Jan 2026) | Stainless | Time Charter |

**Newbuild orderbook (8 NB):**
- 6 × 25,000–26,000 dwt stainless chemical, CMJL Dingheng: CMYZ0189/0190/0191/0192 (25,000 dwt, 2028) + CMYZ0193/0194 (26,000 dwt, ammonia-powered, 2029).
- 2 × 17,000 dwt dual-fuel **bitumen/product tankers**, CMJL Dingheng, 2026 ("Product Tanker CMJL #1/#2") — the 20-F lists these in a separate "PRODUCT TANKER" block, but the Q1-2026 6-K rolls them into Bochem's "8 NB."

- 6-K Q1-2026 (CONFIRMED): "Bochem's 25,000 DWT chemical tankers fleet comprises out of 8 delivered vessels, and 8 NB vessels (average age <1y). They are employed under a 10-year time charter (6 vessels), under a 7-year time charter (6 vessels), and in a spot pool (2 vessels)."
- Charter rate: 6-K "Chemical Tankers" Average spot rate **USD 21,458/day** (Q1-2026, Stolt/STJS pool, 33% fixed). 2 vessels in STJS Pool; remainder on TC. CONFIRMED at segment level.

**Bochem segment book value (2025-12-31) — CONFIRMED:**
- Vessels: **USD 276,374k** · Assets under construction: **USD 62,112k** · Total non-current assets: **USD 338,486k**
- (Off-curve-at-book treatment is well-supported: this is the segment carrying value.)

---

## (c) WINDCAT — Offshore Wind (CTV + CSOV)

### Headline counts — Q1-2026 6-K (CONFIRMED)
- **CSOV: 3 on the water (+4 NB)** · **CTV: 59 on the water (+4 NB)**, average age 10.4y.
- FY2025 20-F (2025-12-31) had **2 CSOV + 4 NB** and **58 CTV + 5 NB** — Q1-2026 added one CSOV (Windcat Haarlem delivered 4 May 2026 — actually post-quarter; the "3" reflects a Q1 delivery) and one CTV; NB counts step down as deliveries roll in. Use the 6-K Q1 counts as headline.

### ★ CRITICAL: OWNED vs JV/50%-owned split (the ~250-vessel reconciliation)

The FY2025 20-F per-vessel fleet table carries a footnote: **"* = 50% owned vessel."** Every asterisked CTV is a **JV vessel held 50%** (equity-accounted, NOT line-by-line consolidated). The JVs are named in the notes:
- **FRS Windcat Offshore Logistics** — JV that **owns 8 CTVs** (German market; plus a *dormant* Polish entity FRS Windcat Polska). (20-F note, CONFIRMED.)
- **TSM Windcat** — JV that **owns 7 CTVs** (French market). (20-F note, CONFIRMED.)
- 8 + 7 = **15 JV CTVs on the water**, matching exactly the 15 asterisked on-water CTV rows.

**CTV ownership at FY2025 (2025-12-31, per-vessel table) — CONFIRMED:**
| | On water | NB | Total |
|---|---|---|---|
| 100%-owned CTV | 43 | 3 | 46 |
| 50%-owned (JV) CTV | 15 | 2 | 17 |
| **Total CTV** | **58** | **5** | **63 rows** |

**CSOV ownership — CONFIRMED:** All CSOVs are 100% owned (no asterisks). FY2025 table: 2 on water (Windcat Amsterdam 2025, Windcat Rotterdam 2025, both Damen, ~2,000 dwt) + 4 NB (hull 552207–552210, Damen, 2026). Plus 1 NB **MP-ASV ("CSOV XL")** ordered 2025, delivery Q1-2027 (listed separately). The 6-K's "3 CSOV" reflects one additional Q1-2026 delivery.

**For NAV (the number you asked for):** of the **59 CTV** headline, only ~**44 are 100%-owned** (43 FY2025 + the one net Q1 addition); **~15 are 50%-owned JV** (FRS Windcat 8 + TSM Windcat 7) and sit in CMBT's accounts as an **equity stake, not as owned vessels**. All **3 CSOVs are 100% owned.** So owned-for-NAV ≈ **44 CTV + 3 CSOV on the water**, with the 15 JV CTVs at 50% economic interest (best modeled via the equity-method carrying value, not full vessel marks).

This resolves the "~250 vessel" reconciliation: the fleet-count headline includes JV/equity-accounted CTVs whose hulls are **off** the consolidated balance sheet.

### Windcat per-vessel CTV table (FY2025, on the water — built years CONFIRMED)
JV vessels (50%-owned) carry the FRS/TSM/`*` prefix. Yards: AF Theriault (Canada), D&S Woudsend / Neptune / Bloemsma (NL), South Boats / Island Boats (UK).

100%-owned (43): Windcat 1 (2004); 2,3,4 (2005); 10,7 (2007); 11,16,19 (2008); 14,15,17,18,20 (2009); WC Dorothea, 21,22,23,24,25 (2010); 101,26,27,29 (2011); 30 (2012); 31,32,33 (2013); 36 (2014); 37,38 (2015); 39 (2016); 40 (2017); 41 (2018); 45 (2019); 46,47 (2020); Hydrocat 48 (2021); 50,51 (2022); 57 (2024); 58 (2025); Hydrocat 60 (2025).
50%-owned JV (15): FRS Windcat 28 (2012); FRS Windcat 34 (2013); FRS Windcat 35 (2014); FRS Windcat 42, 43 (2018); TSM Windcat 44 (2019); TSM Windcat 49 (2021); TSM Windcat 52,53,54 (2022); FRS Hydrocat 55 (2023); TSM Windcat 56 (2024); TSM Windcat 59 (2025); FRS Windcat 61, 62 (2025).
CTV NB (5, all 2026): Windcat 63, 66, 67 (100%); FRS Windcat 64, 65 (50% JV). (6-K reports +4 NB at Q1, one having delivered.)

### Windcat segment book value (2025-12-31) — CONFIRMED
- Vessels: **USD 196,542k** · Assets under construction: **USD 160,065k**
- **Investments in equity-accounted investees (the 50% JVs): USD 3,464k** — this is the *only* balance-sheet representation of the 15 JV CTVs (their hulls are not in the USD 196,542k vessel line).
- Right-of-use 412k; receivables 10,283k; **Total non-current assets: USD 371,023k**; bank/other loans 235,123k.
- JV structure note also flags shareholder loans to TSM Windcat and FRS Windcat Offshore Logistics.

---

## Segment book-value summary (FY2025 20-F, 2025-12-31, USD '000) — CONFIRMED

| Segment | Vessels | AUC (NB) | Equity-acct JV | Total non-current assets |
|---|---|---|---|---|
| Delphis (container) | 210,530 | 5,147 | — | 215,677 |
| Bochem (chemical) | 276,374 | 62,112 | — | 338,486 |
| Windcat (offshore wind) | 196,542 | 160,065 | 3,464 | 371,023 |

**Q1-2026 consolidated (6-K, 2026-03-31) — CONFIRMED but NOT segment-split:** Vessels USD 6,441,456k (was 6,323,773k at YE2025); Assets under construction USD 759,807k; Investments USD 132,308k; Total assets USD 8,456,678k. Segment-level Q1 splits are not disclosed in the 6-K — the FY2025 segment table above is the latest segment breakdown.

---

### Confidence flags / caveats
- **CONFIRMED:** all per-vessel built years/yards/dwt/TEU, ownership-asterisk legend, the two named JVs and their 8+7 CTV counts, all three segment book values, and the 6-K Q1 segment counts/charter tenors/rates.
- **ESTIMATED:** Bochem IMO class (II vs III) — not stated per-vessel; inferred IMO II for 25k stainless STJS-pool hulls. Per-vessel charter *rates* (only segment averages and tenor+counterparty are disclosed). The exact 2026 per-vessel JV split among the +4 CTV / +4 CSOV NBs at the Q1 vintage (FY2025 table shows 5 CTV NB of which 2 are JV; 6-K shows +4 after one delivery).
- **Owned-for-NAV bottom line:** Delphis 4 owned (+1 NB); Bochem 8 owned (+8 NB); Windcat ~44 CTV + 3 CSOV owned on the water (+NB), with ~15 CTV at 50% JV economic interest carried at an equity stake of USD 3.46M, not as owned hulls.