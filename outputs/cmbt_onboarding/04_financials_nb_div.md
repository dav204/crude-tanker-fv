I have all the data verified. Here is the report.

---

# CMB.TECH NV (NYSE: CMBT) — Q1-2026 Balance Sheet, Orderbook & Dividend

**Period end: 2026-03-31. CIK 1604481.**

**Sources (all retrieved 2026-06-26):**
- **[6-K Ex-99.1]** Q1-2026 results press release (filed 2026-05-19), the source for the 31-March balance sheet, P&L, equity, cash flow, share count and dividend intention: `https://www.sec.gov/Archives/edgar/data/1604481/000091957426003591/d12164570_ex99-1.htm`
- **[20-F FY2025]** Annual report (filed 2026-04-21), the source for the granular capital-commitments / newbuild orderbook note (Note 8) and the liquidity-facility detail — these are **31-Dec-2025** figures, flagged as such: `https://www.sec.gov/Archives/edgar/data/1604481/000160448126000004/eurn-20251231.htm`
- **[Transcript]** Q1-2026 earnings call (Ludovic Saverys, CFO), via Motley Fool: `https://www.fool.com/earnings/call-transcripts/2026/06/01/cmbtech-cmbt-q1-2026-earnings-transcript/` — the source for **end-April** capex figures (explicitly post-quarter-end).

All figures in **USD thousands** unless noted. Two-column figures are 2026-03-31 / 2025-12-31.

> **Fetch note for the project:** SEC EDGAR now returns **HTTP 403** to both WebFetch(www.sec.gov) and `scripts/fetch_pdf.py` because the fetcher sends a bare `User-Agent: Mozilla/5.0`. SEC requires a UA carrying contact info. The working path was `curl -A "crude-tanker-fv research dav204@gmail.com"`. The `data.sec.gov/submissions/CIK0001604481.json` index also works with that UA. **Recommend patching `scripts/fetch_pdf.py`'s `USER_AGENT` to include a contact string** before the next EDGAR-dependent run.

---

## 1. Liquidity — CONFIRMED (cash) / FY2025-dated (facilities)

| Item | 2026-03-31 | 2025-12-31 | Status |
|---|---:|---:|---|
| Cash and cash equivalents | **194,600** | 146,529 | CONFIRMED [Ex-99.1] |
| Short-term investments | 8,271 | — | CONFIRMED [Ex-99.1] |
| Restricted cash (separate line) | **none disclosed** | none | The balance sheet has no separate restricted-cash line. The 20-F notes "restricted cash balances" exist (cash pledged under bank borrowings) but they are **commingled within cash & equivalents** — not separately quantified in the interim statements. |
| Undrawn syndicated credit lines | n/a at 3/31 | 176,200 | FY2025 only [20-F] |
| Available committed secured revolving facilities | n/a at 3/31 | 392,300 | FY2025 only [20-F] |

**Total liquidity is not stated as a single figure** in the Q1 press release. The Q1-2026 6-K does **not** disclose undrawn-facility headroom at 31-March. The FY2025 components above (≈$176.2m syndicated + $392.3m revolver headroom + $146.5m cash = ≈$715m) are the most recent CONFIRMED data point; do not carry them as a 31-March number.

---

## 2. Debt — CONFIRMED [Ex-99.1], all 2026-03-31

| Line | 2026-03-31 | 2025-12-31 |
|---|---:|---:|
| **Non-current** Bank loans | 2,783,764 | 2,839,590 |
| **Non-current** Other borrowings | 1,902,228 | 1,876,815 |
| **Non-current** Lease liabilities | 4,565 | 3,368 |
| **Current** Bank loans | 180,717 | 351,170 |
| **Current** Other notes¹ | 200,327 | 203,287 |
| **Current** Other borrowings | 171,124 | 273,898 |
| **Current** Lease liabilities | 1,667 | 1,681 |
| **TOTAL interest-bearing debt (incl. leases)** | **5,244,392** | 5,549,809 |
| less: Cash and cash equivalents | (194,600) | (146,529) |
| **NET DEBT** (cash only) | **5,049,792** | 5,403,280 |
| *memo:* Net debt also netting short-term investments | *5,041,521* | — |

¹ **"Other notes" = the unsecured retail/sustainability notes due 2026** (20-F Note 17 — the FY2024 non-current "Other notes" of $198,887k has rolled to current as it nears 2026 maturity). It is interest-bearing and included in the total above.

**Caveat:** CMB.TECH does **not** print a "net debt" subtotal on the face of the statements; the 5,049,792 figure is my computation (total interest-bearing debt minus cash). "Other borrowings" is predominantly the sale-and-leaseback book — per the project's standing rule, CMB.TECH's lease-financing sits in *borrowings*, so the small separate "Lease liabilities" line (IFRS-16 operating leases) is additive, not a double-count.

---

## 3. Equity, total assets, vessels, AUC — CONFIRMED [Ex-99.1], 2026-03-31

| Item | 2026-03-31 | 2025-12-31 |
|---|---:|---:|
| Share capital | 343,440 | 343,440 |
| Share premium | 1,817,557 | 1,817,557 |
| Translation reserve | 4,662 | 9,502 |
| Hedging reserve | 499 | 90 |
| Treasury shares | (284,508) | (284,508) |
| Retained earnings | 1,059,646 | 737,239 |
| **Total equity (book, attributable to owners)** | **2,941,296** | 2,623,320 |
| Non-controlling interest | — | — |
| **TOTAL ASSETS** | **8,456,678** | 8,405,574 |
| **Vessels** (non-current) | **6,441,456** | 6,323,773 |
| **Assets under construction (AUC)** | **759,807** | 738,298 |
| Right-of-use assets | 5,563 | 4,847 |
| Goodwill | 190,689 | 177,022 |
| Investments (equity-accounted) | 132,308 | 111,346 |
| Non-current assets held for sale | 137,513 | 363,097 |

Note: NAV per share off book equity = 2,941,296 / 290,169,769 ≈ **$10.14/sh book** (not a market-NAV mark — flagged for the model only as the book floor).

---

## 4. Working-capital components — CONFIRMED [Ex-99.1], 2026-03-31

| Item | 2026-03-31 | 2025-12-31 |
|---|---:|---:|
| Inventory (bunkers/consumables) | 82,820 | 77,175 |
| Trade and other receivables (current) | 350,513 | 320,843 |
| Receivables (non-current) | 97,794 | 97,116 |
| Current tax assets | 3,417 | 4,912 |
| Trade and other payables (current) | (258,000) | (222,492) |
| Current tax liabilities | (9,351) | (8,288) |
| Other payables (non-current) | (1,983) | — |

**`working_capital_net` (model input), current operating items only, excluding cash/ST-investments/debt:**
Inventory 82,820 + trade-&-other receivables 350,513 + current tax assets 3,417 − trade-&-other payables 258,000 − current tax liabilities 9,351 = **+169,399** net current working capital.
*Note:* CMB.TECH reports a single combined "Trade and other receivables" / "Trade and other payables" line — pure trade vs. other is **not** separately split on the face. ESTIMATED granularity beyond that requires the 20-F Note 18 (FY2025) if the model needs it.

---

## 5. Share count — CONFIRMED [Ex-99.1], 2026-03-31

| Item | Value | Status |
|---|---:|---|
| Shares **issued** (incl. treasury), 31-Mar-2026 | **315,977,647** | CONFIRMED [Ex-99.1 footnote] |
| Treasury shares held (derived: 315,977,647 − 290,169,769) | **25,807,878** | CONFIRMED (by difference; treasury reserve = −$284,508k) |
| **Shares outstanding ex-treasury** (per-share denominator) | **290,169,769** | CONFIRMED [Ex-99.1 footnote] |
| Weighted-average shares — **basic** (Q1-2026) | 290,169,769 | CONFIRMED |
| Weighted-average shares — **diluted** (Q1-2026) | 290,169,769 | CONFIRMED (no dilution; basic = diluted) |
| EPS basic / diluted (Q1-2026) | $1.27 / $1.27 | CONFIRMED |

Use **290,169,769** as the per-share NAV denominator. The 96m YoY jump in weighted shares (vs 194.2m in Q1-2025) reflects the Golden Ocean acquisition share issuance.

---

## 6. Newbuild orderbook / capital commitments — FY2025-dated [20-F Note 8], as at **2025-12-31**

The Q1-2026 6-K does **not** carry a granular orderbook note. The only granular per-segment commitment table is in the FY2025 20-F (Note 8 – PP&E, Capital commitments), **dated 31-Dec-2025**. Use the transcript (§ below) for the end-April roll-forward.

**Total capital commitments at 31-Dec-2025: $1,647,446k (≈$1.6bn)** (was $2.4bn at 31-Dec-2024). By segment and payment year (USD thousands):

| Segment | Total | 2026 | 2027 | 2028 | 2029 |
|---|---:|---:|---:|---:|---:|
| Tankers | 441,186 | 373,866 | 67,320 | — | — |
| Dry bulk vessels | 525,887 | 515,754 | 10,133 | — | — |
| Container vessels | 37,670 | 37,670 | — | — | — |
| Chemical tankers | 377,100 | 102,750 | 34,100 | 159,650 | 80,600 |
| Offshore wind vessels | 253,804 | 148,857 | 95,136 | 9,811 | — |
| Other | 11,799 | 11,799 | — | — | — |
| **Total** | **1,647,446** | **1,190,696** | **206,689** | **169,461** | **80,600** |

**Newbuilding program composition [20-F Note 8]:**
- 4 eco-type VLCCs
- 2 eco-type Suezmaxes
- 10 Newcastlemax bulk carriers
- 7 chemical tankers (incl. 2 dual-fuel bitumen tankers)
- Offshore wind: 4 CSOVs + 1 MPASV + 3 CTVs
- 2 coasters of 5,000 dwt (counted under dry bulk)
- 1 ammonia-powered 1,400-TEU container vessel (Qingdao Yangfan, expected Q4-2026; CMA-CGM 6,000-TEU on 10-yr TC, Yara/NCL 1,400-TEU on 15-yr TC)
- Other: a multipurpose harbour vessel and hydrogen applications

*Funded vs unfunded:* the 20-F note does **not** split funded/unfunded by segment — that split is only given verbally in the transcript (next section). Per-yard contract values and advances-paid by hull are **not** disclosed in either filing; advances paid are aggregated into the $759,807k "Assets under construction" line (§3). Yard names are disclosed only narratively (e.g. Qingdao Yangfan for the 1,400-TEU; segment chapters name builders loosely). **Per-hull yard/contract/advance granularity is NOT available from these public filings** — ESTIMATED only if reconstructed from per-deal press releases.

**Q1-2026 deliveries already taken (out of the orderbook) [Ex-99.1]:** VLCCs *Eburones* (12-Jan), *Menapii* (23-Mar); chemical tanker *Bochem Callao* (13-Jan). Q2-to-date: Suezmaxes *Cap Grace* (8-Apr), *Cap Joseph* (27-Apr); CSOV *Windcat Haarlem* (4-May); Newcastlemax *Mineral Latvija* (11-May).

---

## 6b. Transcript roll-forward — **END-APRIL 2026** (spoken, NOT a 31-March line)

CFO Ludovic Saverys, Q1-2026 call [Transcript]:
- *"We have a remaining CapEx **end of April** of **$1.2 billion**, from which roughly **$184 million is unfunded**."*
- *"2026 will be the last heavy newbuilding delivery year with the remaining **$740 million to be paid to the shipyard in the coming 3 quarters**."*
- *"with the vessel sales, this is more than double covered for the unfunded CapEx."*

**Flag:** the **$1.2bn / $184m unfunded / $740m to shipyards** figures are **end-April 2026**, post–quarter-end and post-delivery of several hulls — they are NOT reconcilable line-for-line to the 31-Dec-2025 $1.65bn table or to any 31-March balance-sheet line. The downward move from $1.65bn (Dec) → $1.2bn (end-Apr) is consistent with the Q1+early-Q2 deliveries above.

---

## 7. Dividend — Q1-2026 distribution CONFIRMED [Ex-99.1] / policy DISCRETIONARY [20-F + Transcript]

**Q1-2026 declared distribution: USD 0.64 per share total**, split:
- **(i) interim dividend USD 0.20/sh** — subject to 30% Belgian withholding tax (absent exemption/reduction).
- **(ii) USD 0.44/sh out of the share-premium reserve** — exempt from withholding tax.

Conditional on (a) approval by the General Shareholders' Meeting (scheduled 21-May-2026) of the share-premium distribution item, and (b) Belgian Companies Code procedures for the interim dividend. Payment/record dates to follow (then expected end-May 2026). [Ex-99.1, lines 187–197]

Cross-check: the Q1 statement of changes in equity shows **"Dividends to equity holders (46,427)"** charged to retained earnings in the quarter — that is the *prior* distribution paid in Q1, not the new $0.64 (which post-dates quarter-end). The new $0.64 × ~290.2m sh ≈ **$185.7m** prospective outflow.

**Go-forward policy — DISCRETIONARY, not a fixed commitment:**
- 20-F (FY2025): the company adopted a *"full discretionary dividend policy … this approach offers the required flexibility to manage the Company in light of its new strategy."* The Supervisory Board assesses distributions case-by-case against earnings, debt covenants, capex/commitments and Belgian law; *"We may stop paying distributions at any time."* Debt agreements bar distributions that would cause a default/covenant breach.
- Transcript: *"Historically … we've always paid between **50% and 60% of the net profit** distributed to shareholders"* and, on deleveraging, *"once the leverage targets are more into play like we are today, then we can start allocating more of the free dollars to shareholders."*

**Conclusion:** The "~50% of net profit" is a **historical/aspirational range stated by the CFO, NOT a contractual or board-locked payout ratio.** Model it as discretionary with a 50–60% guide, gated by leverage and covenants. (The $0.64 Q1 distribution = ~$185.7m on $368.8m Q1 net profit ≈ **50%**, consistent with the guide.)

---

### Caveats for the model
1. **Restricted cash, undrawn facilities, and total liquidity** are NOT cleanly disclosed at 31-March in the 6-K; only FY2025 facility headroom exists. Flag any 31-March "total liquidity" figure as ESTIMATED.
2. **Net debt** is my computation, not a printed subtotal.
3. **Orderbook per-segment table is 31-Dec-2025**, not 31-March; per-hull yard/contract/advance detail is not public. The 31-March advances are buried in AUC ($759,807k).
4. **Capex roll-forward ($1.2bn / $184m unfunded / $740m to yards) is end-April spoken guidance** — post-quarter-end.
5. Filing uses legacy **`eurn-`** XBRL roots (Euronav lineage); the entity is CMB.TECH NV, CIK 1604481. Combined fleet ~250 vessels across dry bulk / crude / chemical / container / offshore — a **multi-segment conglomerate**, so a single-sector sleeve will misvalue it; per-segment marks are required.