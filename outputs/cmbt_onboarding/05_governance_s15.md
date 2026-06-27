I have sufficient sourced material. The Management Board Saverys members were named explicitly in the risk-factor text I already captured (Alexander, Michael, Ludovic Saverys, Benoit Timmermans, Maxime Van Eecke also serve on CMB's board; Patrick De Brabandere on the Supervisory Board). Let me compose the final §15.7 screen.

---

# §15.7 GOVERNANCE SCREEN — CMB.TECH NV (NYSE/Euronext Brussels: CMBT, ex-Euronav)

**Controlled company. Controller: Saverys family via CMB NV (ultimate parent Saverco).** Screen date 2026-06-26. Primary source = SEC EDGAR CIK 1604481 (FY2025 20-F filed 2026-04-21; Q1-2026 6-K filed ~Apr-2026). All EDGAR docs fetched via `curl` with an SEC-compliant UA (the bare-`Mozilla/5.0` allowlisted path 403'd under rate-limit; see note at end).

---

## 1. CONTROL & SHARE STRUCTURE

| Item | Value | Status |
|---|---|---|
| Controller | CMB NV (ultimate parent **Saverco**, Saverys family) | CONFIRMED |
| Economic ownership (CMB) | **56.56% of equity** at 31-Dec-2025 | CONFIRMED (20-F Note 22) |
| Voting rights (CMB) | **61.59% of voting rights** at 31-Dec-2025 | CONFIRMED (20-F Note 22) |
| Dual class / loyalty voting | **None.** "We may not give [major shareholders] different voting rights from any of our other shareholders" (Belgian law + org docs) | CONFIRMED (20-F Item 7.A) |
| Shares issued | 315,977,647 at 31-Mar-2026; ex-treasury 290,169,769 | CONFIRMED (Q1-2026 6-K) |
| Free float | ~38% economic (≈100% − 56.56% − treasury); the brief notes ~64.74% group voting — reconcilable with the 61.59% CMB-alone figure plus Saverco/other group entities | CONFIRMED control, group-aggregate % ESTIMATED |

**Why voting (61.59%) exceeds economic (56.56%):** treasury shares held by CMB.TECH carry no vote, so the same CMB block is a larger share of the *voting* base. There is **no loyalty/double-voting structure** — the voting premium is purely the treasury-share mechanical effect. This is materially cleaner than a French-style `droit de vote double` controlled name.

**Board composition (CONFIRMED, 20-F Item 6):**
- **Supervisory Board: 6 members.** NYSE-independent: De Brabandere, Molis, Steen, Bøe, Janssens, Scheers (i.e. all six independent under NYSE rules; four under the stricter Belgian test — Steen, Molis, Janssens, Scheers). Chair **Patrick De Brabandere also sits on CMB's board** (affiliated despite NYSE-"independent" label).
- **Management Board: Saverys-controlled.** CEO **Alexander Saverys**, CFO **Ludovic Saverys**, plus **Michael Saverys, Benoit Timmermans, Maxime Van Eecke** — *all five also serve on the board of CMB*, the controller (20-F risk factor, verbatim). The executive layer is the controlling family; the Supervisory Board is the check.
- Audit & Risk Committee: 3 independent (De Brabandere chair, Scheers, Molis). Related-party transactions are reviewed by this committee (20-F Note 22).

**Read:** classic controlled-company concentration. The mitigant is a genuinely NYSE-independent Supervisory Board with an independent-chaired Audit & Risk Committee that vets related-party deals; the aggravant is that the entire executive Management Board is the controlling family and also sits on the controller's board (self-disclosed conflict-of-interest exposure on "corporate opportunities, inter-company agreements, newbuilding acquisitions").

---

## 2. RELATED-PARTY FEE LOAD

All from 20-F **Note 22** (CONFIRMED). The structure is **light and arm's-length-benchmarked**, not the heavy external-manager drag the §15 mechanism is built to catch.

| Agreement | Counterparty (CMB group) | Basis | 2025 cost | Status |
|---|---|---|---|---|
| Office rental | MCA Facilities (100% CMB sub) | Indexed lease, 3-yr tacit renewal | **$0.638m** (2024 $0.533m; 2023 $0.335m) | CONFIRMED |
| Warehouse lease | MCA Facilities | Lease, no expiry | (within above bucket) | CONFIRMED |
| **Auxiliary services** — general mgmt, strategic advisory, accounting, legal, corporate admin | **CMB NV** | Cost-recharge at hours-spent + **5% true-up**, reviewed annually | combined ↓ | CONFIRMED |
| **Shipping services** — chartering, operational, technical mgmt | CMB NV | **1.25% of shipping revenue** (stated as "industry standard") | combined ↓ | CONFIRMED |
| Items ii+iii combined | CMB NV | — | **$14.6m charged in 2025** (outstanding $6.9m) | CONFIRMED |
| Suezmax sales (5 vessels, 2024) | wholly-owned CMB sub | "at market rate at date of transaction" | n/a (asset sale) | CONFIRMED |
| **Commercial agreements** | — | **"Not applicable"** | — | CONFIRMED (Item 7.A) |

**Fee load as % of gross asset value:** Total related-party operating fees ≈ **$14.6m + $0.64m ≈ $15.2m/yr**. Against gross assets of **$8,456.7m** (total assets, Q1-2026 6-K) that is **≈0.18% of GAV per year**. Even measured against the ~$7.2bn vessel + AUC book ($6,441m vessels + $760m AUC, 20-F), it is **≈0.21%/yr**. This is a *thin, cost-plus* arrangement, not a 1.5–2% AUM-style external-manager skim. The 1.25%-of-revenue shipping-services fee is the only revenue-linked component and is benchmarked to market.

**Read:** the fee load is **not** a realisation-impairment driver. No external IPO-vehicle promote, no incentive fee on NAV, no leasing-back of the controller's vessels into the company at above-market rates disclosed. The only sharp edge is *relationship density* — CMB runs management, leases the offices, and buys/sells vessels to itself — but pricing is disclosed as cost-plus / market, and an independent Audit & Risk Committee reviews it.

---

## 3. DISTRIBUTION BEHAVIOR

The controller's distribution record is **shareholder-friendly when cash is present, then deliberately redirected to a capital program — not starved.**

- **2022 (Euronav era):** ~$1.10–1.22/sh returned (dividend + share-premium repayment, withholding-optimised). CONFIRMED via 6-K coverage.
- **2023:** ~$4.57/sh proposed for FY (USD 0.27 dividend + **USD 4.30 share-premium repayment**) — i.e. a **large special distribution** as the tanker up-cycle peaked. CONFIRMED.
- **2024:** ~$5.72/sh paid across the year (tail of the up-cycle + tender period). REPORTED (broker/dividend aggregators; consistent with 6-K cadence).
- **2024-2025 REDIRECT:** under the CMB.TECH strategy the board moved to a **fully discretionary** policy and **redirected cash into the newbuild / decarbonization orderbook** (the "convert market strength into longer-term charters" language, CEO Saverys, Q1-2026 6-K). Payout compressed versus the 2023 special-dividend peak. CONFIRMED direction.
- **Now (resuming):** Dec-2025 interim **$0.05/sh**; **$0.64/sh** declared with Q1-2026 ($0.20 interim dividend + $0.44 from share premium), explicitly framed as **~50% of the period's profit** ("the Board decided to pay 50% on the whole profit of Q1"; historical practice 50–60% of net profit). CONFIRMED (Q1-2026 6-K + earnings call).

**Read:** the controller has **historically shared cash with minorities generously** (the 2022-23 specials went *pro-rata to all shareholders*, no controller-only carve-out), and the dividend cut was a **capital-allocation pivot to a funded orderbook**, not a squeeze-out starve. The resumption at 50% of net profit is a credible, recently-honoured commitment. This is the *opposite* of the TEN value-trap archetype where cash never reaches minorities.

---

## 4. NATURAL-EXPERIMENT COMP — the 2021-2024 Euronav saga

This is the strongest evidence in the file, and it cuts **both ways**.

**The sequence (CONFIRMED via 20-F history + contemporaneous press):**
1. **Apr-2022:** Euronav/Frontline announce a stock-for-stock merger. The Saverys family (via CMB) opposes it and **builds a ~25% blocking stake** to kill it.
2. **Jan-2023:** Frontline withdraws. Strategic/structural **deadlock** between the two reference holders.
3. **Oct-2023:** CMB and Frontline settle. **Frontline buys 24 VLCCs from Euronav for ~$2.35bn**; **CMB buys Frontline's ~26% Euronav stake at $18.43/sh**; CMB crosses 30% → triggers a **mandatory takeover bid to minorities at the same $18.43/sh**.
4. **2024:** CMB completes the mandatory tender; strategy pivots from a VLCC pure-play to a diversified, decarbonization-focused fleet (acquisition of CMB.TECH Enterprises from CMB; later the ~40.8% Golden Ocean stake and 2025 GOGL merger at 0.95x).

**How were minorities treated?**
- **Compensated:** minorities got a **mandatory bid at the same $18.43 price the controller paid Frontline** — equal treatment at the reference-block price, which is the fair-treatment baseline Belgian takeover law enforces (Art. 5 Takeover Law). Those who wanted out got cash; the specials in 2022-23 had already returned substantial capital.
- **Strategy-switched-against-their-will:** minorities who stayed were carried from a high-payout VLCC pure-play into a **capital-intensive, lower-payout diversified/hydrogen-and-newbuild strategy they did not vote for** — the core grievance.
- **Live litigation (CONFIRMED, 20-F Legal Proceedings):** **FourWorld** and other dissenters are suing in Antwerp (seeking annulment of the 24-tanker sale to Frontline, the Frontline arbitration termination, and the CMB.TECH Enterprises drop-down) — earlier US (SDNY) and Brussels Markets Court attempts to block the mandatory offer were **rejected (2024)**. Separately, **Golden Ocean dissenters** are litigating in **Bermuda** claiming **$14.49/sh cash** or appraisal — judgment pending (heard Jan-2026). The company calls FourWorld's claims "nuisance" and estimates merits "low."

**Read:** the controller used hardball tactics (a blocking stake to defeat a merger the minorities' own board had endorsed) and then **converted control into a strategy pivot**. But at every transfer point minorities received **equal-price exits** (the $18.43 mandatory bid; the GOGL exchange ratio). The dissenter litigation is the **tripwire to watch** — appraisal/cash claims that *settle above tender price* would be evidence of impaired fair-value realisation; dismissals (the pattern so far) would confirm the equal-treatment defence holds.

---

## 5. EXTERNAL ANCHOR

| Anchor | Value | Status |
|---|---|---|
| Current price (CMBT) | ~$17.26 NYSE / €12.96–13.00 Brussels (Jun-2026) | REPORTED (aggregators) |
| **Fearnley Securities** | **Buy**, maintained 8-Dec-2025 (brief cites ~$12.43 PT vintage) | CONFIRMED rating, PT REPORTED |
| Consensus PT | ~$16.59 (14 analysts) / €14.43 (high €17.04, low €11.08); ~81% buy | REPORTED (MarketBeat/ChartMill, Jun-2026) |
| Stated discount-to-NAV | Multiple notes describe CMBT as trading **"at a significant discount to NAV"** | REPORTED, no single clean current NAV/sh figure surfaced |
| Pareto coverage | Not confirmed in this sweep; CMBT not currently in the project's Pareto-P/NAV watchlist vintage. **APPROX-flagged like NAT/ASC/CCEC** | NOTED |

**Caveat (per the "absence isn't evidence" rule):** I did not surface a single clean, current broker **NAV/sh** with attribution in this web sweep — the 2026 NAV-discount claims are qualitative. A primary-broker NAV (Pareto/Clarksons/Fearnley full note) should be pulled before any P/NAV gate read is treated as hard. Net-asset proxy from the filing: **total equity attributable to owners** is the cleaner internal anchor; gross assets $8,456.7m, vessels+AUC ~$7,201m (20-F / Q1-2026 6-K, CONFIRMED).

---

## RECOMMENDATION — per §15.7 doctrine

**Stance: DECLINE the haircut — do NOT apply a `governance_discount_pct`. Carry CMBT as a controlled name with NAMED TRIPWIRES.**

**Rationale.** §15.7 doctrine: *"haircuts price EVIDENCE of realisation impairment; the mechanism generates TRIPWIRES."* On the evidence:

1. **Fee load is immaterial** — ~0.18–0.21% of GAV/yr, cost-plus and market-benchmarked, independent-committee-reviewed. No external-manager promote, no incentive-on-NAV, no above-market vessel leasebacks. This is not the TEN-archetype fee drain.
2. **Distribution record is pro-minority** — large 2022-23 specials went pari-passu to all holders; the cut was a *funded capital-allocation pivot*, not a starve; payouts have *resumed* at 50% of net profit and been honoured ($0.64/sh on Q1-2026).
3. **The natural experiment shows equal-price treatment** — minorities got the *same $18.43 the controller paid the exiting block*, court-tested and upheld (US + Brussels attempts to block were rejected). That is the single best governance datapoint and it is favourable.
4. **No structural minority-extraction mechanism** — single share class, no loyalty voting, mandatory-bid law binding.

The §15 gate is **multi-year median P/NAV ≥ 0.85**. CMBT has **<1 year of clean post-rebrand market history at the current strategy** and trades (per qualitative broker reads) at a *discount* to NAV — meaning the **gate is not yet measurable / is effectively N/A-gated** on history. Per doctrine, a haircut prices *evidence*; the evidence here points to **fair, if hard-nosed, treatment**, so a discount would be unsupported speculation against the rule "haircuts price evidence."

**The genuine governance risk is qualitative, not extractive:** the controlling family *is* the executive board and pivoted strategy under the minorities; the risk is **strategy/agency drift** (capital sunk into a hydrogen/ammonia decarbonization bet, related-party drop-downs from CMB), not cash siphoning. That risk is better expressed through the **NAV marks and the forward strip** (mark the orderbook conservatively, PV-discount newbuilds per the §3.1/§9.6 rule) than through a governance multiplier.

### TRIPWIRES to monitor (any one → re-open the §15 haircut question)

1. **Dissenter litigation outcomes** — if the **GOGL Bermuda appraisal/cash claim settles materially above the merger value** ($14.49/sh claim), or the **FourWorld Antwerp claim succeeds** in unwinding the Frontline/drop-down transactions, that is *direct evidence* of impaired minority realisation → apply haircut.
2. **Related-party fee creep** — the auxiliary-services charge moving off cost-plus, the **1.25%-of-revenue shipping fee rising**, or new above-market vessel drop-downs from CMB without independent fairness opinions.
3. **Distribution backsliding** — failure to hold the stated ~50% of net profit through the next down-leg of the cycle (i.e., cash retained for controller-favoured M&A while minorities get nothing).
4. **P/NAV gate, once measurable** — if a multi-year median P/NAV settles **below 0.85** *and* coincides with any of 1–3, the discount becomes evidence-backed, not speculative.
5. **Independent-board erosion** — loss of the genuinely-independent Audit & Risk Committee majority that currently vets related-party deals.

---

### Sources
- FY2025 20-F (CIK 1604481, filed 2026-04-21): main doc `eurn-20251231.htm` — Item 6 (board), Item 7.A (major shareholders/voting), Note 22 (related parties), Legal Proceedings. Index: https://www.sec.gov/Archives/edgar/data/1604481/000160448126000004/0001604481-26-000004-index.htm
- Q1-2026 6-K Exhibit 99.1: https://www.sec.gov/Archives/edgar/data/1604481/000091957426003591/d12164570_ex99-1.htm (total assets $8,456.7m; vessels $6,441m + AUC $760m; Q1 profit $368.8m / $1.27 EPS; 315,977,647 shares; $0.64/sh distribution)
- Euronav/Frontline saga + $18.43 mandatory bid + 24-VLCC sale: https://maritime-executive.com/article/frontline-and-cmb-complete-deal-to-divide-euronav ; https://www.offshore-energy.biz/cmb-breaks-deadlock-as-frontline-sails-away-with-2-35-billion-vlcc-bounty-in-euronav-deal/ ; en.wikipedia.org/wiki/CMB.TECH
- Dividend policy / 50% payout / Q1-2026 distribution: https://www.theglobeandmail.com/investing/markets/markets-news/Motley%20Fool/2241529/cmb-tech-cmbt-q1-2026-earnings-transcript/ ; https://cmb.tech/investors/share-information/dividend
- Fearnley Buy / consensus PT: https://www.nasdaq.com/articles/fearnley-securities-maintains-cmbtech-cmbt-buy-recommendation ; https://www.marketbeat.com/stocks/NYSE/CMBT/

**Local files written:** `/tmp/cmbt_q1.htm` (Q1-2026 6-K), `/tmp/cmbt_20f.htm` + `/tmp/cmbt_20f.txt` (FY2025 20-F).

---

**Fetcher note for CLAUDE.md (recurring gotcha):** Both `WebFetch(www.sec.gov)` and `scripts/fetch_pdf.py` 403'd on EDGAR this session — SEC's fair-access policy rejects the bare `Mozilla/5.0` UA under load and requires a UA containing a contact. The working path was `curl -sSL -A "crude-tanker-fv research dav204@gmail.com" "<url>"` (with `-L` to follow EDGAR's 301 to the un-zero-padded CIK path). Recommend updating `fetch_pdf.py`'s `USER_AGENT` to an SEC-compliant contact string so the allowlisted path stops failing on EDGAR.