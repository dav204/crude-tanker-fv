All data is gathered and cross-reconciled. Here is the final report.

---

# CMB.TECH NV (NYSE: CMBT) — Bocimar Dry Bulk Fleet at Q1-2026 (2026-03-31)

## Sources
- **Q1-2026 6-K, Exhibit 99.1** (results/fleet/market) — accession 0000919574-26-003591, filed ~19 May 2026. URL: https://www.sec.gov/Archives/edgar/data/0001604481/000091957426003591/d12164570_ex99-1.htm — **on-water counts, avg ages, orderbook size, TCEs, sales.**
- **FY2025 20-F** (full per-vessel fleet table, built years, yards) — accession 0001604481-26-000004, filed 2026-04-21, body `eurn-20251231.htm`. URL: https://www.sec.gov/Archives/edgar/data/1604481/000160448126000004/eurn-20251231.htm — **per-vessel names/built/dwt/yard, capital commitments, newbuild program.**
- Golden Ocean Group Ltd standalone 20-F (CIK 0001029145, FY2024 acc. 0001029145-25-000012) located but **not needed** — the CMBT 20-F already carries every built year.
- Fetch path: SEC blocks bare UA; works with a descriptive User-Agent (`curl -A "crude-tanker-fv research dav204@gmail.com"`). The project `fetch_pdf.py` and plain WebFetch both return 403 on EDGAR because of UA `Mozilla/5.0`.

All counts below are **CONFIRMED** from the filings unless flagged ESTIMATED.

---

## 1. CONFIRMED on-water counts at 2026-03-31 (6-K, "Bocimar has…")

| Class | On-water 2026-03-31 | Avg age (6-K) | Model class |
|---|---|---|---|
| Newcastlemax | **38** (+8 NB) | 3.2 y | Cape |
| Capesize | **37** | 11.2 y | Cape |
| Kamsarmax/Panamax | **30** | 6.9 y | Pana |
| **Total dry bulk on water** | **105** | — | |

Verbatim (6-K): *"Bocimar has 38 (+8NB) Newcastlemaxes on the water (average age 3.2y), 37 Capesize vessels on the water (average age 11.2), and 30 Kamsarmax/Panamax vessels on the water (average age 6.9y)."*

**Cross-reconciliation (high confidence):**
- The FY2025 20-F DRY BULK rollforward gives **end-2025 on-water = 105, newbuildings on order = 10**. The 6-K's 38+37+30 = **105** on water at 2026-03-31 — identical.
- The 20-F per-vessel table lists **NCM 46 / Cape 37 / Kam 26 / Pana 4**. Splitting NCM by built year: **36 built ≤2025 + 10 built-2026 (the NB program)**. Two 2026-built NCMs (Mineral Malta, Mineral Europa) delivered in Q1-2026 → 38 on water, leaving **8 NB** — exactly the 6-K "38 (+8NB)". Capesize 37 and Kam+Pana 30 match exactly with no adjustment.
- The next NCM delivery, **Mineral Latvija, was 11 May 2026 (Q2)** per the 6-K newbuilding-deliveries table — correctly excluded from the Q1 on-water count.
- Sub-class split for "Kamsarmax/Panamax 30" = **26 Kamsarmax + 4 Panamax** (from 20-F table; ESTIMATED split but additively confirmed).

Note: 2 Capesizes sold in Q1-2026 — **Golden Magnum (2009) and Belgravia/"Battersea" (2009)** — were held-for-sale at YE2025 and delivered to buyers in January 2026. They are **already excluded** from the 37 on-water Capesize count (the count is internally consistent without them).

---

## 2. Age distribution per model class (delivered vessels, built-year basis, 20-F table)

**Cape class = Newcastlemax + Capesize (n=73 delivered):**

| Age band (at 2026) | Count |
|---|---|
| 0–4 y (2022–2026) | 18 |
| 5–9 y (2017–2021) | 24 |
| 10–14 y (2012–2016) | 27 |
| 15–19 y (2007–2011) | 4 |
| 20 y+ | 0 |

Mean age ≈ 7.7 y. (Two distinct cohorts: a young NCM book, avg ~3 y, vs an older ex-Golden-Ocean Capesize book clustered 2014–2018, avg ~11 y.)

**Pana class = Kamsarmax + Panamax (n=30 delivered):**

| Age band (at 2026) | Count |
|---|---|
| 0–4 y (2022–2026) | 10 |
| 5–9 y (2017–2021) | 10 |
| 10–14 y (2012–2016) | 8 |
| 15–19 y (2007–2011) | 2 |
| 20 y+ | 0 |

Mean age ≈ 7.4 y.

**Per-class built-year histograms (delivered only):**
- **Newcastlemax (36):** 2016×2, 2017×1, 2019×2, 2020×10, 2021×3, 2023×2, 2024×8, 2025×8 (+10 NB built-2026)
- **Capesize (37):** 2010×3, 2011×1, 2013×1, 2014×11, 2015×8, 2016×5, 2017×3, 2018×5
- **Kamsarmax (26):** 2011×2, 2012×3, 2013×1, 2014×1, 2015×1, 2020×5, 2021×3, 2023×6, 2024×4
- **Panamax (4):** 2013×2, 2017×2

### Per-vessel table (from FY2025 20-F; name | class | dwt | built | yard). Charter/employment in source.

**NEWCASTLEMAX — delivered (36):**
Mineral Belgie (210,204; 2023; Qingdao Beihai); Mineral Nederland (210,204; 2023; Qingdao Beihai); Mineral France (210,000; 2024; Qingdao Beihai); Mineral Luxembourg (210,197; 2024; Qingdao Beihai); Mineral Deutschland (210,000; 2024; Qingdao Beihai); Mineral Italia (210,000; 2024; Qingdao Beihai); Mineral Eire (210,000; 2024; Qingdao Beihai); Mineral Espana (210,000; 2024; Qingdao Beihai); Mineral Danmark (210,000; 2024; Qingdao Beihai); Mineral Hellas (210,000; 2024; Qingdao Beihai); Mineral Portugal (210,000; 2025; Qingdao Beihai); Mineral Cesko (210,000; 2025; Qingdao Beihai); Mineral Slovenija (210,000; 2025; Qingdao Beihai); Mineral Osterreich (210,000; 2025; Qingdao Beihai); Mineral Sverige (210,000; 2025; Qingdao Beihai); Mineral Suomi (210,000; 2025; Qingdao Beihai); Mineral Polska (210,000; 2025; Qingdao Beihai); Mineral Slovensko (210,000; 2025; Qingdao Beihai); Golden Champion (208,391; 2019; NTS); Golden Comfort (208,385; 2020; NTS); Golden Earl (207,999; 2020; NTS); Golden Spirit (210,866; 2020; Bohai); Golden Spray (210,667; 2021; Bohai); Mineral Angola (208,400; 2019; NTS); Mineral Cabo Verde (211,112; 2016; Bohai); Mineral Comoros (211,135; 2016; Bohai); Mineral Guinea (208,395; 2020; NTS); Mineral Madagascar (211,138; 2020; Bohai); Mineral Malawi (208,397; 2020; NTS); Mineral Mauritius (210,896; 2020; Bohai); Mineral Mozambique (208,399; 2020; NTS); Mineral Namibia (207,999; 2020; NTS); Mineral Shougang International (dwt n/d; 2020; NTS); Mineral Walcott (207,999; 2017; Dalian); Mineral Zambia (207,999; 2021; NTS); Mineral Zimbabwe (207,999; 2021; NTS).
*(Yards: Qingdao Beihai = CMBT's own super-eco series, China; NTS = New Times Shipbuilding, China; Bohai = Bohai Shipbuilding, China; Dalian, China.)*

**NEWCASTLEMAX — NB / built-2026 (10, all Qingdao Beihai, 210,000 dwt):** Mineral Malta, Mineral Europa, Mineral Latvija, Mineral Kypros, Mineral Eesti, Mineral Lietuva, Mineral Magyar, Mineral Romania, Mineral Balgariya, Mineral Hrvatska. *(Of these, Malta+Europa delivered in Q1-2026, Latvija on 11 May 2026; the remaining ~7 are the residual orderbook — see §4.)*

**CAPESIZE (37):** Golden Beijing (175,820; 2010; JHI); Golden Future (175,861; 2010; JHI); Golden Zhejiang (175,837; 2010; JHI); Golden Myrtalia (177,979; 2011; SWS) — *held for sale*; KSL China (179,109; 2013; Orient); Mineral Jindeok (179,189; 2014; Sungdong); Golden Houston (181,214; 2014; Imabari); Mineral Ajisai (180,600; 2014; Imabari); Mineral Kevin (180,958; 2014; SWS); Mineral Romelu (181,066; 2014; SWS); Mineral Marouane (181,020; 2014; SWS); Mineral Nacer (181,055; 2014; SWS); Mineral Eden (180,960; 2014; SWS); Mineral Axel (181,015; 2014; SWS); Mineral Dries (181,062; 2014; SWS); Mineral Jan (181,009; 2014; SWS); Mineral Seondeok (179,337; 2015; Sungdong); Mineral Kiku (182,472; 2015; JMU); Mineral Sakura (182,481; 2015; JMU); Mineral Kaede (182,486; 2015; JMU); Mineral Thibaut (181,062; 2015; SWS); Mineral Toby (181,010; 2015; SWS); Mineral Thomas (181,003; 2015; SWS); Mineral Vincent (181,043; 2015; SWS); Mineral Pohang (180,355; 2016; DH Shipbuilding); Mineral Dangjin (180,491; 2016; DH); Mineral Yeosu (180,229; 2016; DH); Mineral Sumire (182,610; 2016; JMU); Mineral Kwangyang (180,513; 2016; DH); Mineral Nimbus (180,503; 2017; NTS); Mineral Yannick (181,044; 2017; SWS); Mineral Youri (181,046; 2017; SWS); Mineral Arcus (180,478; 2018; NTS); Mineral Calvus (180,521; 2018; NTS); Mineral Cirrus (180,487; 2018; NTS); Mineral Cumulus (180,499; 2018; NTS); Mineral Incus (180,512; 2018; NTS).
*(Yards: JHI, SWS = Shanghai Waigaoqiao, Orient, NTS, DH Shipbuilding = China; Sungdong, JMU = Japan Marine United, Imabari = Japan/Korea.)*

**KAMSARMAX (26):** Golden Arion (82,188; 2011; Tsuneishi); Golden Jake (82,188; 2011; Tsuneishi); Golden Daisy (81,507; 2012; SPP); Golden Ginger (81,487; 2012; SPP); Golden Rose (81,585; 2012; SPP); Golden Sue (84,943; 2013; Sasebo); Golden Deb (84,970; 2014; Sasebo); Golden Kennedy (84,978; 2015; Sasebo); Golden Fellow (81,135; 2020; Dalian); Golden Fortune (81,210; 2020; Dalian); Golden Forward (81,130; 2020; Dalian); Golden Friend (81,206; 2020; Dalian); Golden Frost (80,558; 2020; Dalian); Golden Fast (80,573; 2021; Dalian); Golden Freeze (80,578; 2021; Dalian); Golden Furious (80,595; 2021; Dalian); Golden Frozen (84,505; 2023; Dalian); Golden Hope (84,986; 2023; Dalian); Golden Fridge (84,508; 2023; Dalian); Golden Lion (84,967; 2023; Dalian); Golden Soul (84,988; 2023; Dalian); Golden Star (84,988; 2023; Dalian); Golden Frigo (84,520; 2024; Dalian); Golden Faith (84,987; 2024; Dalian); Golden Tide (84,996; 2024; Dalian); Golden Wave (84,984; 2024; Dalian).

**PANAMAX (4):** Golden Fraiche (74,500; 2013; Pipavav); Golden Frio (74,300; 2013; Pipavav); Golden Fris (74,754; 2017; Pipavav); Golden Opal (74,232; 2017; Pipavav). *(Pipavav = India.)*

20-F table aggregate dwt: NCM 9,436,781 (46 incl NB) | Cape 6,673,936 (37) | Kam 2,159,260 (26) | Pana 297,786 (4).

---

## 3. Scrubber-fitted % per class

**NOT DISCLOSED.** Neither the Q1-2026 6-K nor the FY2025 20-F fleet table includes a scrubber/EGCS column (0 "scrubber" mentions in the 6-K; the 2 in the 20-F are unrelated to the fleet roster). CMBT describes the dry bulk book as **"very modern and super eco"**; the own-built Qingdao Beihai NCM series are super-eco / ammonia-ready designs, but per-vessel scrubber fitment is **not in any SEC filing** — would need an external fleet database (Clarksons/VesselsValue) to fill. Flag as a known gap for the manifest.

---

## 4. Dry-bulk NEWBUILD orderbook

**CONFIRMED (FY2025 20-F, Note "Capital commitment", 2025-12-31):**
- Newbuilding program includes **10 Newcastlemax bulk carriers** (210,000 dwt, Qingdao Beihai) + 2 coasters of 5,000 dwt (in dry-bulk line).
- **Dry bulk capital commitments: $525.887 million total** — $515.754 M due 2026, $10.133 M due 2027. (Group total commitments $1.6 bn.)

**At Q1-2026 (6-K):** the remaining dry-bulk NB book is **8 Newcastlemax** ("+8NB"), after Mineral Malta + Mineral Europa delivered in Q1-2026 (Mineral Latvija followed 11 May 2026). Several of the 10 carry signed long-term charters (e.g. one to **Fortescue**, dual-fuel ammonia-powered, ~end-2026 delivery; nine ammonia-powered vessels under a March-2025 MOL/MOLCT agreement spanning NCM bulkers + chemical tankers, deliveries 2026–2029).

**Per-vessel NB contract price / advances paid: NOT separately disclosed.** The 20-F gives the dry-bulk commitment in aggregate ($525.9 M) and the program count (10 NCM), not a per-ship contract price or installments-paid schedule. "Vessels under construction" appears on the balance sheet but is not broken out by ship/class. ESTIMATED implied price ≈ $50–55 M/NCM if the ~$526 M dry-bulk commitment is spread over the ~10 NCM + 2 coasters, but treat as a rough back-of-envelope, not a disclosed figure.

---

## 5. Model-mapping summary & confidence

| Model class | Vessels (on water 2026-03-31) | Source |
|---|---|---|
| **Cape** (NCM 38 + Cape 37) | **75** | 6-K — CONFIRMED |
| **Pana** (Kam 26 + Pana 4) | **30** | 6-K — CONFIRMED |
| Cape NB book | 8 NCM | 6-K — CONFIRMED |

- Counts (§1) and orderbook size (§4): **CONFIRMED**, two independent SEC sources cross-tie to 105 exactly.
- Per-vessel built years/yards (§2): **CONFIRMED** from 20-F table. One missing dwt (Mineral Shougang International — dwt not printed in source; built 2020, NTS). Kam-vs-Pana split within the 6-K's "30" is ESTIMATED 26/4 from the 20-F table (additively confirmed).
- Built-2026 NCM delivery timing into Q1: Mineral Malta + Mineral Europa = ESTIMATED as the two Q1 deliveries (the arithmetic 36+2=38 is forced by the 6-K; the 20-F does not date each 2026 NCM delivery individually, but the 6-K names Mineral Latvija as the next post-quarter delivery on 11 May 2026, confirming only two preceded it in Q1).
- Scrubber % (§3) and per-vessel NB price/advances (§4): **NOT DISCLOSED** in SEC filings.

Useful temp artifacts on disk: `/tmp/cmbt_q1_text.txt` (6-K text), `/tmp/cmbt_20f_text.txt` (20-F text, full per-vessel fleet table at lines 234–370, dry-bulk rollforward at 562–569, capital-commitment note at 1806–1817).