# News digest — 2026-08-29

## Run header

- **Window swept:** **2026-08-24 → 2026-08-29** (6 days). Previous digest established by
  listing `outputs/` (not inferred): `news_digest_{2026-06-10, 06-21, 08-13, 08-16, 08-24}.md`
  are the five on disk; **08-24 is the head**, so this window opens where it closed.
- **Names swept:** 25/25 of `inputs/watchlist.yaml` —
  DHT · ECO · FRO · INSW · TNK · NAT · FLNG · CCEC · STNG · HAFN · TRMD · ASC · TEN ·
  CMDB · SBLK · GNK · CAPT · MPCC · GSL · BRUT · CMBT · SB · LPG · BWLP · 2343.
- **Depth weighting.**
  - **DEEP — non-US issuers** (no EDGAR sentinel; this sweep is their only channel):
    BRUT, MPCC, CAPT, BWLP (`.OL`), 2343 (`.HK`). Read at the **primary issuer feed** first.
  - **DEEP — APPROX-pNAV names** (`APPROX_PNAV_TICKERS` read live from
    `src/crude_tanker_fv/reconcile.py:69`, not hardcoded — currently
    `{NAT, ASC, CCEC, TEN, CMDB, MPCC, GSL, SB, 2343}`).
  - **DEEP — live-event names:** BRUT (demerger executing), FRO (open P1 print), GNK
    (post-withdrawal Diana), CMBT / TRMD / HAFN / BWLP / NAT (Q2 report dates falling
    inside the window).
  - **Lighter — broker-covered US remainder:** DHT, ECO, INSW, TNK, FLNG, STNG, ASC,
    SBLK, GSL, SB, LPG, TEN, CCEC, CMDB.
- **Sources searched.**
  - **Local issuer channel (read FIRST):** `state/edgar_manifest.jsonl`, `state/edgar_poll.log`,
    and every staged body under `inputs/filings/` new in the window — BRUT, BWLP (×2),
    CAPT, MPCC (×2) via `newsweb`; TRMD (×3), NAT, CMBT, FRO, HAFN, BWLP via EDGAR.
  - **Primary issuer feeds:** `mfn.se/all/a/{bruton-limited, mpc-container-ships,
    capital-tankers}.json` fetched directly. **BWLP's feed was NOT fetched separately** —
    its three in-window releases arrived complete through the local `newsweb` channel
    (same source), and I read those bodies instead. Stated so it is not read as a
    second independent confirmation.
  - **Broker archive:** `inputs/research_pareto/2026/08/` — Shipping Dailies **8/24,
    8/25, 8/26, 8/27, 8/28** (all five in-window business days), plus the
    **Frontline Company Comments Newsflash 8/28** and Container Weekly 8/28. Read
    locally with `pypdf`, which works fine on these (the "PDFs are binary" limit applies
    to WebFetch, not to local parsing).
  - **Web:** WebSearch sweeps on Frontline Q2, Genco/Diana, TEN/GSL/SB/2343, and
    DHT/INSW/TNK/STNG; WebFetch on the mfn feeds, the Manila Times GlobeNewswire mirror.
  - **Repo-side:** `state/{price_refresh.log, price_refresh.err, newsweb_poll.json,
    hkex_poll.json}`, `inputs/market_data/prices_daily.yaml`, `inputs/archive_gaps.yaml`,
    `decisions/*_log.md` heads, `src/crude_tanker_fv/loaders.py`.

### COVERAGE LIMITS — read before trusting any "nothing found" below

Measured **this run**, not copied from the last one:

- `globenewswire.com` — **`timeout of 60000ms exceeded`, twice** on the FRO Q2 release.
  Fell back to the **Manila Times GlobeNewswire mirror**, which returned the release text.
  FRO Q2 figures below are **mirror-sourced primary text**, not fetched from the issuer wire.
- `frontline.bm/press-releases/` — **HTTP 404** (that path does not exist).
- `stocktitan.net/news/FRO/` — **HTTP 404**. `marketscreener.com` quote-news page — **HTTP 403**.
- One Manila Times URL guessed by date returned **HTTP 502**; the correct 8/28 URL worked.
- **EDGAR was NOT enumerated directly this run.** I did not call `browse-edgar`/`efts`
  (documented 403). The US-name negatives rest on the **local EDGAR poller**, which is a
  real channel but a different claim — see the outage note immediately below.
- **The local channel had a 4-day outage inside this window.** `state/edgar_poll.log`
  shows hourly polls through **2026-08-25 18:20**, then **nothing until 2026-08-29 16:20**,
  when a catch-up run staged **7 filings (18 docs) + 5 releases** at once. Because the
  pollers are watermark-based, the backlog appears to have been **recovered, not lost** —
  every Q2 filing 8/26–8/28 is present. But **detection latency was 1–3 days**, so this
  digest is the first place these appear.
- `mfn.se`, the Pareto archive and the search lane all behaved. **No source in this window
  was silent-because-unreachable**, with the single exception that FRO's own wire had to be
  read through a mirror.

### Repo-side condition that shapes every item below

**Nothing in this window has reached the model.** The last pipeline run in every decision
log is **2026-08-25T22:33 UTC**; `inputs/market_data/prices_daily.yaml` carries
`fetched_at: 2026-08-25T22:01`; `state/price_refresh.log` shows
`SKIPPED: network not up` on 8/18–8/24, then `SKIPPED: dirty-tree` on **8/25** and again
on **8/29**. So prices are **4 days stale**, and **every item in this digest is UNREAD in
every decision log** — all ten logs I checked (`brut, bwlp, fro, cmbt, trmd, hafn, nat,
mpcc, lpg, gnk, capt`) head with the same 8/25 auto-run at `_[pending annotation]_`.
I state that once here rather than repeating it per item.

---

## MATERIAL

### M1 · BRUT — the demerger **COMPLETED** in-window, the tape fell **−36.6%**, and the model is still valuing the **pre-demerger** company

**What happened.** The last digest caught the demerger as *resolved, ex-date tomorrow*.
It has now fully executed inside this window:

- **2026-08-25** — *"Ex distribution in kind today"*: BRUT traded ex the distribution of
  **61,923,808 OMC Tankers NDRs**, 1:1.
  Source: `https://mfn.se/a/bruton-limited/bruton-limited-brut-ex-distribution-in-kind-today`
  (also staged locally, `inputs/filings/BRUT/newsweb_2026-08-25_5a46204d-…txt`).
- Per the 8/20 timetable, **record date 8/26 · distribution 8/27 · OMC first trading day
  8/28** — all three now in the past. The issuer feed shows **no BRUT release after 8/25**
  (primary-sourced negative, `mfn.se/all/a/bruton-limited.json` fetched today).

**The price event, and why the model did not see it.** `prices_daily.yaml` caught the
ex-date move and **flagged it**:

```
BRUT: asof 2026-08-25T14:25:36Z  native NOK 43.0  price $4.6213
      prev_close $7.2866  day_change_pct -36.58
      flag: "day move -36.6% exceeds ±15% band"
```

`loaders.py:453` **rejects a flagged quote and falls back to the watchlist static**, so the
8/25 pipeline runs valued BRUT at **$6.32** — the Pareto **7-Aug** pre-demerger price —
and printed `Δprice: no change`, `BUY (undervalued)`, broker spread **−34.3pp**. The
quarantine is behaving as designed (an idiosyncratic −36.6% print *should* be held back);
the problem is that **this particular −36.6% is real and mechanical**, and the fallback
re-anchors to a price whose paired `consensus_pnav: 0.86` and `analyst_target: 7.13`
describe a **12-newbuild company that no longer exists**.

**What left the company** (issuer text, 8/20): four New Times VLCC contracts (deliveries
Jan/Mar/Jun/Aug **2029**, aggregate **USD 472m**, **USD 47.2m** paid), four Yantai CIMC
Raffles VLCC contracts (Jan/Mar/May/Jul **2028**, aggregate **USD 499m**, **USD 49.9m**
paid), plus **USD 50m cash**. No indebtedness transferred beyond ~USD 82k trade payables.

**The replacement anchor already exists.** Pareto has re-struck BRUT post-demerger inside
this window — this is the part that makes the item actionable rather than merely broken:

- **8/25 daily:** *"BRUT trades ex OMC-shares today, we believe a fair price should be
  between NOK 45 (our NAV) and 50 at this point."*
- **8/28 daily share-price table:** **BRUT kr 44.0, P/NAV 1.03x, 1Y-FWD P/E 14.4x** —
  a matched price+P/NAV pair on the **post-demerger** entity (was kr 60.0 / 0.86x / 22.6x
  at the 8/07 vintage the watchlist carries).
- Pareto's own read of OMC: 4× VLCC 2029 New Times with **$425m remaining capex**, 4× VLCC
  2028 CIMC Raffles with **$449m remaining capex**, 10% paid in both — which
  **reconciles to the issuer's $472m/$47.2m and $499m/$49.9m** net of deposits. Pareto pegs
  OMC **LTV ~78%** and warns *"there could be additional equity needed here."*

**Model surfaces touched.** `inputs/watchlist.yaml` BRUT `current_price` / `consensus_pnav`
/ `analyst_target` (all three, jointly — the TEN-$44 discipline in the file header applies
exactly); the vessel manifest (8 hulls leave, 2028/2029 delivery rows); the capex/commitment
schedule; and the `price_fallback` path in `loaders.py`.

**What I am NOT sure of.** (a) The 8/25 *"NOK 45 (our NAV)"* and the 8/28 table
(**kr 44.0 ÷ 1.03x ≈ kr 42.7 NAV**) do not agree exactly — I cannot tell from these two
artifacts whether Pareto re-struck NAV between 8/25 and 8/28 or whether one is rounded.
Do not treat NOK 45 and kr 42.7 as the same number. (b) Whether BRUT should be carried as
the post-demerger stub or as stub + OMC claim remains the **owner's methodology call** —
unchanged from the last digest, and I have no authority over it. (c) I did not verify the
post-8/25 BRUT.OL tape at all; the price feed has been dead since 8/25.

---

### M2 · FRO — Q2 landed **8/28**, three days earlier than the 8/31 the last digest had; it **partly resolves the open P1 print** and adds two promotable fixtures

The last digest registered FRO Q2 as the named venue for resolving the open 8/04
2×VLCC print, and recorded the date as **8/31**. It reported **8/28**. Filed locally as a
6-K cover (`inputs/filings/FRO/0000919574-26-005942_…6k.htm`) — **the exhibit was not
staged**, so the figures below come from the GlobeNewswire text via the Manila Times mirror
after two 60s timeouts on the wire itself.

- **Result / distribution:** best quarterly profit ever **$659.2m ($2.96/sh)**; adjusted
  **$580.2m ($2.61/sh)**; **cash dividend $2.61/sh** declared for Q2; **special one-time
  dividend $0.80/sh** on completion of the VLCC sales.
- **The open P1 print:** *"Entered into agreements to sell two VLCCs built in 2017 in July
  2026 for a total sales price of $270.0 million."* Net proceeds ~**$179.0m**, gain ~**$110m**
  in Q3. **Vessel names are still not disclosed** — the report does not supply the field the
  last digest was waiting on. Note the date nuance: agreements struck **in July**, announced
  **8/04**; the repo carries the print at 2026-08-04.
- **A second, separate S&P item:** *"Delivered our two oldest Suezmax tankers built in 2014
  and 2015 in the second quarter of 2026, resulting in a gain on sale of $54.7 million."*
  **Gain only, no price → NOT promotable** on the repo's own standard.
- **Fixtures (promotable):** two VLCC newbuildings delivered **2026-06-22** and **2026-07-03**,
  each fixed on **1-year TC-out at $120,000/day**.
- **Q3 spot coverage:** VLCC **86% @ $156,900/day**; Suezmax **79% @ $117,400/day**;
  LR2/Aframax **70% @ $81,000/day**.
- **Fleet / newbuilds:** 40 VLCC · 19 Suezmax · 18 Aframax/LR2, average age 6.6 yrs;
  remaining newbuilding commitments **$601.1m** on 9 hulls from Hemen affiliates, with
  secured financing up to **$737m**. *(This block is search-summary sourced —* **LEAD-QUALITY**,
  *not read in the primary text.)*
- **Broker:** Pareto Newsflash 8/28 — **HOLD**, *"at ~1.2x our YE NAV … the shares at $44"*;
  VLCC break-even down $500/day to **$23,800/day** on new refinancings; several new
  **1–3 year TCs booked at $75–120,000/day**.

**Model surfaces.** The open P1 print record; the curve inputs (Q3 coverage + the $120k/day
1Y fixtures directly supersede assumed rates); the vessel manifest (2 NB deliveries, 2
Suezmax departures); FRO's watchlist anchor (8/07: 39.6 / 1.31x; 8/28 table: **$43.8 / 1.33x**).

**Not sure of.** Pareto's *"~1.2x YE NAV"* (→ YE NAV ≈ $36.7) and the table's **1.33x**
(→ current NAV ≈ $32.9) are **different NAV vintages, not a contradiction** — do not
average them. And the per-vessel price the last digest wanted still does not exist publicly:
$270m ÷ 2 = $135m each is an **inference**, not a disclosure.

---

### M3 · BWLP — a **three-vessel S&P programme** and Q2, with a broker NAV that has moved well above the watchlist's implied anchor

Two issuer releases plus a 6-K, all staged locally.

- **2026-08-25 — sale of BW Birch** (`newsweb_2026-08-25_1a1d8461…txt`): 2007-built,
  **net book gain ~US$37m**, **net cash proceeds ~US$64m** (100% basis), sold by the 52%-owned
  BW LPG India, currently on TC, **delivery to buyer by mid-November** at the latest.
- **2026-08-28 — Q2 2026 results** (`newsweb_2026-08-28_83ea98be…txt`) puts all three sales
  on one page as subsequent events:
  - **BW Elm** (2007) — gain ~$36m, net cash proceeds ~$64m, **delivered in July**.
  - **BW Birch** (2007) — gain ~$37m, proceeds ~$64m, delivery by mid-November.
  - **BW Levant** (2015, acquired in the 2024 Avance Gas transaction) — gain ~**$17m**,
    proceeds ~**$38m**, delivery by mid-November.
  - CEO framing: both 2007 sales at *"a value equivalent to a newbuilding price of
    approximately US$248 million."*
  - **A fixture:** a 2016-built LPG dual-fuel retrofit vessel fixed on a **five-year TC-out
    in the mid-high US$40,000s/day**, delivery end-2026.
- **Q2 numbers:** NPAT **$138m**, EPS **$0.79**, ROE 27%; TCE **$74,000/available day**;
  liquidity $773m; net leverage **23.5%** (from 26.3%). **Dividend $0.95/sh** = 100% of
  Shipping NPAT (record 9/8, ex 9/7 Oslo / 9/8 NYSE).
- **Q3 guidance:** **92% of available days fixed at ~$88,000/day**, including 41% TC
  coverage at $44,300/day.
- **Broker:** Pareto 8/28 — *"Recent asset sales imply NAV of NOK 200+"*; headline EBITDA/EPS
  ~20%/~30% below consensus but **dividend in line**. 8/28 table: **kr 226.4 / 1.27x / 11.8x**
  (watchlist 8/07: kr 206.6 / 1.13x / 11.6x).

**Model surfaces.** Vessel manifest (three departures, staggered July/November); the LPG
curve (a 5-yr TC at mid-high $40ks and a 92%-fixed Q3 at $88k/day); BWLP's watchlist pair.
The watchlist's implied broker NAV is 21.77 ÷ 1.13 ≈ **$19.3 ≈ NOK 183**; Pareto now says
**NOK 200+**, and the table implies 226.4 ÷ 1.27 ≈ **NOK 178** — *the flash NAV and the table
NAV disagree*, so treat "NOK 200+" as forward/asset-sale-implied, not the table's current NAV.

**Not sure of.** *"Net cash proceeds"* is **not a sale price** — it is post-debt, post-cost,
and BW Birch is on a **100% basis** for a **52%-owned** subsidiary. The $248m
"newbuilding-price equivalent" is a CEO comparison, not a transaction value. None of the
three is promotable as a priced S&P print without the actual contract price.

---

### M4 · TRMD — a **new MR newbuild order**, $217m of fresh financing, guidance raised, and a curve-relevant LR2 fixture

Q2 filed **8/26** (`inputs/filings/TRMD/0001628280-26-058979_…`). Best quarter in TORM's
history: TCE **$512m**, EBITDA **$416m**, net profit **$338m**; fleet-wide TCE
**$59,301/day** (Q2-25: $26,672).

- **Newbuild ORDER (subsequent event):** *"TORM entered into an agreement to acquire six MR
  newbuilding vessels, with options for an additional two vessels. The six vessels are
  scheduled for delivery in **2029**, while the optional vessels are expected to be delivered
  in **2030** if exercised."*
- **Financing (subsequent event):** *"TORM secured financing for ten vessels for a total of
  **USD 217m**."* Separately, H1 borrowings +$73m mostly financing newly acquired secondhand
  vessels, offset by repayment of lease debt on the **repurchase of eight sale-and-leaseback
  vessels**.
- **Dividend:** interim **USD 2.40/share** for Q2.
- **Guidance RAISED:** FY26 TCE **$1,400–1,600m** (was $1,150–1,450m); EBITDA
  **$1,000–1,200m** (was $800–1,100m).
- **Coverage (as of 18 Aug):** Q3 **73% at $38,606/day** — LR2 83% @ $49,255, LR1 61% @
  $32,608, MR 71% @ $35,247.
- **Fixture (broker/third-party sourced, 8/25 Pareto):** VesselsValue picked up a **1-year TC
  for the 2018-built LR2 *Torm Herdis* to PetroChina at $51,500/day** — *"ahead of our
  H2'26–2027 estimates of around ~$40k/day."*
- **Broker:** Pareto 8/26 — Q2 in line, 8% dividend yield, **0.92x NAV**. 8/28 table:
  **$31.8 / 0.92x / 10.6x** (watchlist 8/07: 29.5 / 0.86x / 9.9x).
- The **8/24 board appointment** (Jann Brown, effective 1 Oct) was already reported in the
  last digest — **not re-counted here**.

**Model surfaces.** Newbuild schedule (6 MR 2029 + 2 options 2030 — new rows); debt schedule
($217m/10 vessels); the product curve (the $51,500/day LR2 fixture and the coverage table
both sit above modelled rates); TRMD's watchlist pair.

**Not sure of.** The order has **no disclosed price** — six MR hulls at an unstated contract
value; the capex line cannot be built from this release. The *Torm Herdis* rate is
**VesselsValue-via-Pareto**, not an issuer disclosure — **LEAD-QUALITY** for promotion.

---

### M5 · CMBT — **nine newbuild deliveries with exact dates**, four more sales, and a raised Pareto target

Q2 filed **8/27** (`inputs/filings/CMBT/0000919574-26-005821_…ex_99-1.htm`). Profit
**USD 364.4m** ($1.26/sh), EBITDA **$552.8m**, backlog stable at **$3.26bn**, intended
distribution **USD 0.64/share** (second consecutive quarter).

**Newbuilding deliveries — the release publishes the actual delivery table**, which is
directly a manifest input:

| Delivery date | Type | Name |
|---|---|---|
| 8 Apr 2026 | Suezmax | Cap Grace (2026, 156,000 dwt) |
| 27 Apr 2026 | Suezmax | Cap Joseph (2026, 156,000 dwt) |
| 4 May 2026 | CSOV | Windcat Haarlem (2026) |
| 11 May 2026 | Newcastlemax | Mineral Latvija (2026, 210,000 dwt) |
| 28 May 2026 | Newcastlemax | Mineral Eesti (2026, 210,000 dwt) |
| 8 Jun 2026 | Newcastlemax | Mineral Magyar (2026, 210,000 dwt) |
| 10 Jun 2026 | VLCC | Morini (2026, 319,000 dwt) |
| 29 Jun 2026 | Newcastlemax | Mineral Lietuva (2026, 210,000 dwt) |
| 14 Jul 2026 | CTV | FRS Windcat 65 |

**Sales** — every one is a **gain without a price**, so **none is promotable**:
Ilma (2012, 314k dwt) + Ingrid (2012) delivered Q2, gain ~$98.2m; Sienna (Suezmax, 2007,
150,205 dwt) delivered Q2, gain $29.2m; **Brest** (2023, 156,851) + **Brugge** (2023) to
deliver **Q3**, gain ~$100.2m; **Donoussa** (VLCC, 2016, 299,999) to deliver **Q4**, gain
~$74.3m; **Bristol** (2024, 156,851) to deliver **Q4**, gain ~$56.9m.

**Charter:** a milestone agreement with **Fortescue for up to 12 ammonia-powered
Newcastlemaxes** (210,000 dwt) — no rate or tenor disclosed.

**Broker (both in-window):** Pareto 8/27 — *"NAV ~NOK 200/sh, with 0.85x NAV among the lowest
in our Tanker and Drybulk coverage"*; **capex down to $0.9bn, only ~$120m unfunded**.
Pareto 8/28 — **reiterate BUY, TP raised to $22.5 / NOK 210**, *"in line with our
forward-NAV."* 8/28 table: **$18.3 / 0.86x / 10.3x** (watchlist 8/07: 16.4 / 0.85x / 10.2x;
`analyst_target` 16.59 is a MarketBeat consensus, now well below Pareto's $22.5).

**Model surfaces.** Multi-sleeve manifest (9 deliveries in, 7 vessels out across Q2–Q4);
capex schedule; CMBT's watchlist `analyst_target` and pair.

**Not sure of.** The sale gains are *"based on the net sale price and book values"* — the
book values are not given, so **no sale price can be backed out**. Do not attempt it.

---

### M6 · HAFN — the issuer publishes **its own NAV per share**, and Pareto **cut its target**

Q2 filed **8/28** (`inputs/filings/HAFN/0001140361-26-034767_…ex99-2.htm`).

- Net profit **USD 277.8m** ($0.56/sh); TCE **$372.9m**, average **$44,093/day**;
  adjusted EBITDA **$287.3m**.
- **Issuer NAV: *"approximately USD 4.4 billion, or approximately USD 8.89 per share
  (NOK 88.47), at quarter end"*** — footnoted as *"calculated using the fair value of
  Hafnia's owned vessels, including joint venture vessels."*
- **Dividend USD 0.5003/share** (total $250.0m), **90% payout**; record 9/8.
- **Q3 coverage: 80% of earning days at $30,716/day** as of 17 Aug.
- **Broker:** Pareto 8/28 — EBITDA/EPS 5%/9% below consensus, dividend ahead;
  **HOLD, TP $8.2 (NOK 77)**. The watchlist comment records Pareto's prior stance as
  *"Hold $8.50"* — so this is a **target cut, $8.50 → $8.20**. 8/28 table:
  **$8.3 / 1.03x / 10.4x** (watchlist 8/07: 7.6 / 0.92x / 9.5x).

**Model surfaces.** An **independent, issuer-published NAV** is the strongest anchor
evidence available for HAFN: watchlist implied broker NAV is 7.6 ÷ 0.92 ≈ **$8.26**, the
issuer says **$8.89**, and Pareto's table now implies 8.3 ÷ 1.03 ≈ **$8.06**. Three NAVs
within ~10% — a genuine reproduction check on the HAFN anchor, and a rare one.

---

### M7 · NAT — a **priced Suezmax sale** (name withheld), a second sale still open, dividend up

Q2 filed **8/27** (`inputs/filings/NAT/…_ex-1.htm`). NAT is an **APPROX-pNAV** name, so this
is a deep-pass read; it is also the name the last two digests flagged for an aggregator
date-stamp trap, so everything here is from the issuer's own release.

- **The S&P print:** *"one, built in 2003, has been sold at USD 26 million."* Separately:
  *"During the first quarter we entered into sales agreements for two ships, a 2003-built and
  a 2005-built tanker. The first vessel was delivered to the new owners during the second
  quarter … The second vessel was delivered to the buyers at the beginning of the third
  quarter and … is still listed as held for sale."* Delivery was **delayed by the vessel
  being trapped inside the Strait of Hormuz**.
- **Dividend $0.27/share** for Q2 (up from $0.22), the 116th consecutive quarterly dividend;
  payable 9/24, record 9/10.
- Q2 net profit **$68.3m** (EPS $0.32), including a **$21.3m book profit on sale** and loss-of-hire
  insurance recoveries; adjusted EBITDA $67.6m including **$14.6m of loss-of-hire recoveries**
  for the three Hormuz-trapped vessels.
- **TCE $63,000/day** (Q1: $47,600); **~75% of Q3 booked at ~$54,000/day**.
- **Fleet: 17 Suezmaxes + 2 newbuildings for 2028 delivery.** Cash **$175m**; net debt
  **$215.8m** ($12.7m/ship). Financing: CLMG/Beal Bank $150m facility, $139m outstanding,
  secured on 7 vessels; Ocean Yield on 8 vessels, $270.7m outstanding.
- Operational colour: three ships freed through Hormuz after being stuck since 28 Feb; **a NAT
  vessel was attacked in the Black Sea** a month ago and got away.
- **8/28 Pareto table: $6.8, P/NAV "–", 1Y-FWD P/E 17.7x** — NAT still carries **no Pareto
  P/NAV**, confirming its APPROX basis is unchanged (see M10).

**Model surfaces.** A priced Suezmax S&P point ($26m for a 2003-built); the manifest (one
vessel out in Q2, one out in early Q3, 2 NB for 2028); NAT's balance-sheet legs.

**Not sure of.** **The vessel names are not given** — a 2003-built and a 2005-built Suezmax,
unnamed. Only the 2003-built has a price ($26m); **the 2005-built has no disclosed price**.
The $21.3m book profit spans the delivered vessel only.

---

### M8 · GNK — **Diana is now selling its Genco stake**, at roughly Pareto's NAV

From the Pareto daily **8/26**: *"DSX flagged 11.6% ownership in GNK after close, having sold
1.2m shares at ~$27/sh (equal to our NAV)."*

This is the first post-withdrawal move in the sequence. Diana withdrew its offer on
**2026-08-14** (pre-window, reported in the last digest); it is now **reducing** rather than
accumulating, and the **~$27/share execution is an independent market print** sitting almost
exactly on Pareto's NAV and just under the repo's `analyst_target: 28.40` (which the owner
ruled on 8/13 is a **broker NAV, not a price target**). 8/28 table: **$25.8 / 0.95x / 12.3x**.

**Still open from the last digest, unchanged:** the GNK watchlist comment still asserts
*"A NON-BINDING INDICATIVE PROPOSAL REMAINS LIVE."* **Diana withdrew on 8/14.** This has now
been flagged in two consecutive digests and remains factually wrong as written. It is a
watchlist comment, not a pipeline-loaded value, so nothing miscomputes — but the registered
"re-check" it describes has already fired.

**Not sure of.** This is **broker-desk colour**, not a filing. I did not open the underlying
DSX 13D/A or 6-K, so treat the 11.6% and the 1.2m/$27 as **LEAD-QUALITY** pending the filing.

---

### M9 · MPCC — Q2 with **no NAV statement**, and seven Maersk fixtures with rates and tenors

Q2 filed **8/26**, staged locally (`inputs/filings/MPCC/newsweb_2026-08-26_d9624eca…txt`)
plus the dividend key-information release.

- Backlog **USD 2.2bn**; coverage **99% (2026) / 85% (2027) / 60% (2028) / 39% (2029)**.
- Revenue **$116.9m** (Q2-25: $137.9m), EBITDA **$95.4m**, adjusted EBITDA **$65.0m**.
- Utilisation 98.8%; adjusted TCE **$24,951/day**. **Dividend USD 0.04/share** (ex 21 Sep,
  pay 28 Sep).
- **Fleet: 65 vessels, ~186,000 TEU, of which 17 are newbuildings on order. "One of the
  newbuildings was delivered in August"** — no name, no date.
- Financing: the **$375m senior secured term loan** (ten newbuildings) and the
  **$107m private placement** are both **restated from prior windows**, not new here.
- **Fixtures (Pareto 8/26, from the call):** *"7x new fixtures with Maersk starting gradually
  through H1'27. 4x / 3x 1,700 / 2,500 TEUs got **$20,850 / $25,850/day for 25–33 / 19–25
  months**"* — against Pareto's assumed ~$23k/$25k for 2027–28, so **slightly dilutive to
  2027–28 EBITDA (1–2%) but de-risking**.

**The APPROX anchor did not refresh.** MPCC's `consensus_pnav: 1.04` rests on the company's
**July-2025** statement that 1,300-TEU divestments *"imply NAV of NOK 25–26 per share"* —
now ~13 months stale. **This Q2 release states no NAV**, and the **8/28 Pareto table again
shows "–" for MPCC's P/NAV**. That is a **primary-sourced negative**: the anchor remains
genuinely unrefreshed, and the container sector remains APPROX-by-construction (§11.8.2).
8/28 table: **kr 27.2 / – / 8.4x** (watchlist 8/07: kr 24.2 / 1.04x APPROX / 8.1x).

---

### M10 · Pareto's **8/28 share-price table** is a full matched-vintage refresh of the watchlist's 8/07 anchors

The watchlist's price / `consensus_pnav` / `consensus_fwd_pe` triplets are all stamped
**Pareto 7 Aug 2026**. The **8/28 daily carries the same table**, three weeks fresher, and
the tape has moved hard. Because the file's own header requires these to be
**updated together**, this is one promotion, not twenty:

| Name | Watchlist (8/07) px / P/NAV / P/E | Pareto **8/28** px / P/NAV / P/E |
|---|---|---|
| DHT | 18.4 / 1.08 / 9.7 | **$19.4 / 1.14x / 9.9x** |
| ECO (Okeanis) | 63.8 / 1.34 / 10.9 | **$66.3 / 1.47x / 10.1x** |
| FRO | 39.6 / 1.31 / 9.9 | **$43.8 / 1.33x / 10.3x** |
| INSW | 93.2 / 1.17 / 12.8 | **$99.3 / 1.21x / 13.9x** |
| TNK (Teekay) | 77.1 / 0.80 / 8.9 | **$88.2 / 0.91x / 8.8x** |
| STNG (Scorpio) | 76.4 / 0.71 / 13.0 | **$77.4 / 0.73x / 14.0x** |
| HAFN | 7.6 / 0.92 / 9.5 | **$8.3 / 1.03x / 10.4x** |
| TRMD | 29.5 / 0.86 / 9.9 | **$31.8 / 0.92x / 10.6x** |
| CMBT | 16.4 / 0.85 / 10.2 | **$18.3 / 0.86x / 10.3x** |
| SBLK | 28.6 / 0.89 / 7.2 | **$30.4 / 0.91x / 7.1x** |
| GNK | 25.1 / 0.92 / 13.7 | **$25.8 / 0.95x / 12.3x** |
| FLNG (Flex) | 31.0 / 1.43 / 14.9 | **$31.3 / 1.44x / 14.6x** |
| LPG (Dorian) | 44.4 / 0.96 / 12.2 | **$49.3 / 1.06x / 12.9x** |
| BWLP | kr 206.6 / 1.13 / 11.6 | **kr 226.4 / 1.27x / 11.8x** |
| CAPT | kr 134.2 / 0.71 / 22.2 | **kr 150.4 / 0.72x / 25.5x** |
| **BRUT** | kr 60.0 / 0.86 / 22.6 | **kr 44.0 / 1.03x / 14.4x** ← post-demerger |
| NAT | 6.4 / 0.85 **APPROX** / 18.7 | **$6.8 / – / 17.7x** |
| CCEC | 22.8 / 0.90 **APPROX** / 7.9 | **$22.8 / – / 7.9x** |
| ASC (Ardmore) | 17.0 / 0.75 **APPROX** / 15.5 | **$17.7 / – / 10.6x** |
| MPCC | kr 24.2 / 1.04 **APPROX** / 8.1 | **kr 27.2 / – / 8.4x** |

**Two structural reads.** (1) **The APPROX set is confirmed, not refreshed** — NAT, CCEC,
ASC and MPCC still print **"–"** in Pareto's P/NAV column three weeks on, which is exactly
the condition `APPROX_PNAV_TICKERS` encodes. Their `sanity: n/a` treatment stands. (2)
**TEN, CMDB, GSL, SB and 2343 are absent from the table entirely**, consistent with their
documented no-Pareto-coverage status — an expected absence, not a miss.

---

## PROMOTABLE CANDIDATES

Candidates only — promotion is human-only, and each line states what it is missing.

**S&P prints**

| Name | Vessel | Class / built | Price | Source quality |
|---|---|---|---|---|
| LPG | ***Clermont*** | VLGC, **2015** | **~$91m** | **BROKER-REPORTED** — Pareto 8/24: *"Dorian has reportedly sold the 'Clermont'… the price is said to be $91m."* Not issuer-confirmed. Pareto carries her at **$83m** in a **$46.4/sh NAV**; comparables **'Cobra'/'Constellation'** (same year) went **~$85–87m** earlier in 2026. |
| NAT | **unnamed** | Suezmax, **2003** | **USD 26m** | **ISSUER** (8/27 6-K). Price is firm; **vessel name missing**. |
| FRO | **unnamed ×2** | VLCC, **2017** | **$270.0m aggregate** | **ISSUER** (8/28 Q2, restating the 8/04 announcement). **Names still undisclosed**; per-vessel $135m is an inference, not a print. |
| BWLP | **BW Elm** | VLGC, **2007** | proceeds ~$64m | **ISSUER** — *net cash proceeds*, **not a sale price**. Delivered July. |
| BWLP | **BW Birch** | VLGC, **2007** | proceeds ~$64m | **ISSUER** — proceeds on a **100% basis for a 52%-owned** subsidiary. Delivery by mid-Nov. |
| BWLP | **BW Levant** | VLGC, **2015** | proceeds ~$38m | **ISSUER** — proceeds, not price. Delivery by mid-Nov. |

*Explicitly NOT promotable (gain disclosed, no price):* FRO's two Suezmaxes (2014/2015,
gain $54.7m); CMBT's Ilma, Ingrid, Sienna, Brest, Brugge, Donoussa, Bristol.

**Fixtures (rate + tenor)**

| Name | Asset | Rate | Tenor | Source quality |
|---|---|---|---|---|
| FRO | 2 × VLCC newbuildings (del. 22 Jun / 3 Jul 2026) | **$120,000/day** each | **1 year** | **ISSUER** |
| TRMD | LR2 ***Torm Herdis*** (2018) to PetroChina | **$51,500/day** | **1 year** | **VesselsValue via Pareto 8/25** — LEAD-QUALITY |
| BWLP | 2016 LPG dual-fuel retrofit vessel | **mid-high $40,000s/day** | **5 years**, del. end-2026 | **ISSUER** — rate is a range, not a number |
| MPCC | 4 × 1,700 TEU (Maersk) | **$20,850/day** | **25–33 months** | **Pareto 8/26, from the call** — LEAD-QUALITY |
| MPCC | 3 × 2,500 TEU (Maersk) | **$25,850/day** | **19–25 months** | **Pareto 8/26, from the call** — LEAD-QUALITY |
| FRO | several vessels | **$75–120,000/day** | **1–3 years** | **Pareto 8/28** — range only, no vessel/count |

**Anchor pairs** — the full **8/28** matched price / P/NAV / fwd-P/E vintage in **M10**,
replacing the 8/07 set. **BRUT's is the one that cannot wait**: it is the only post-demerger
pair in existence (**kr 44.0 / 1.03x / 14.4x**), and the current triplet describes a company
that no longer exists.

**Manifest / schedule inputs** — CMBT's nine dated newbuild deliveries (M5 table); FRO's two
VLCC NB deliveries (22 Jun, 3 Jul); TRMD's six MR newbuildings (2029) + two options (2030);
BRUT's eight hulls leaving to OMC (2028/2029); NAT's two newbuildings (2028).

---

## WATCH

- **The whole mechanical chain was down 8/25 → 8/29.** Price refresh last succeeded
  **8/25 22:01**; it logged `network not up` on 8/18–8/24 and **`dirty-tree` on 8/25 and
  again today**. The EDGAR/newsweb pollers stopped after **8/25 18:20** and only caught up
  **today at 16:20**. The last pipeline run in every decision log is **8/25 22:33**. Two
  distinct failure modes (network, then a dirty working tree) chained into one 4-day gap,
  and the `dirty-tree` skip is self-perpetuating: **this digest is itself an untracked file**,
  so it will block the next refresh the same way the 8/24 digest blocked the 8/25 one.
- **BRUT's flagged-price quarantine will not clear itself.** `loaders.py:453` will keep
  falling back to the static $6.32 for as long as the flag stands, and the flag is attached
  to a **correct** price. This needs a human decision, not another run.
- **GNK's watchlist comment remains factually stale** (*"proposal remains live"*; Diana
  withdrew 8/14) — open across two digests now.
- **Supply-side:** Pareto 8/25 notes the scrapping of the **1999-built aframax 'Bursa'** —
  *"the fourth aframax scrapped YTD vs. eight in 2025 (ex. LR2s)"*, with **33% / 5% of crude
  aframaxes aged 20Y+ / 25Y+ vs only 9% on order.**
- **Rate environment is at records and possibly turning.** USGoM VLCC past **$250,000/day**
  (8/24); Frontline with three ships on subs Brazil–East at **$200,000/day+** (8/25); by
  8/27–8/28 Pareto reads *"signs of VLCCs plateauing in the West"* and *"the Atlantic market
  appears to be peaking for now."* The Q3 coverage tables in M2/M3/M4/M6 lock much of this in.
- **CMBT capex** down to **$0.9bn with only ~$120m unfunded** ($0.5bn falling in H2'26) —
  the unfunded-newbuild falsifier is weakening materially.
- **OMC Tankers** (not a watchlist name) begins trading 8/28 at **~78% LTV** on Pareto's
  estimate, *"there could be additional equity needed."* Relevant only as the other half of
  the BRUT split.
- **CAPT reports Q2 on 2026-09-01** (issuer release 8/26, before the Euronext Growth Oslo
  open) — the next window's first scheduled event. No CAPT deliveries in this window; the
  8/06 *Athinagoras* and 8/13 *Aristodimos* deliveries are prior-window and already recorded.

---

## NO-ACTION — swept clean

Each line states the channel actually checked. "Nothing found" here means *searched, found
nothing* — never *did not look*.

- **DHT** — no EDGAR arrival in window (poller caught up today); present in the Pareto 8/28
  table with **no commentary item** in any of the five in-window dailies; targeted web search
  surfaced only the **Q2 (~8/10)** results and the **Jan-2026** *DHT Bauhinia* agreement, both
  pre-window and previously recorded. Nothing in 08-24→08-29.
- **ECO (Okeanis)** — no filing, no release, no Pareto commentary; table row only. Nothing found.
- **INSW** — no filing in window; search returned only the **8/10** Q2 (7 vessels ~$216m,
  ~$88m gains, $5.05 dividend), pre-window and prior-covered. Nothing new.
- **TNK** — no filing in window; search returned only the **7/29** Q2 (2 Suezmax NB contracts
  $190m, 2 vessels sold $138m), pre-window. Nothing new.
- **STNG** — no filing, no release, no Pareto commentary; searched vessel-sale and
  charter announcements, newest found are Jan–Apr 2026. Nothing in window.
- **ASC (Ardmore)** — no filing; table row only (P/NAV still "–"). Nothing found.
- **SBLK** — no filing, no release, no commentary. Nothing found.
- **FLNG** — no in-window filing (its 6-Ks are **8/19**, prior window); table row only.
  Nothing found.
- **CCEC** — no filing; table row only (P/NAV still "–"). Nothing found.
- **CAPT** — issuer feed fetched directly; **one** in-window release, the **8/26 Q2 date
  notice** (WATCH). No transactions, no deliveries, no financing in window.
- **CMDB** — no in-window filing (its 6-K is **8/18**, prior window); **absent from Pareto's
  table by construction** (no coverage). Searched, nothing found.
- **GSL** — no filing, no release; no Pareto coverage. Searched, nothing found.
- **SB (Safe Bulkers)** — no filing, no release; no Pareto coverage. Searched, nothing found.
- **TEN** — no filing, no release; no Pareto coverage. Search surfaced only Q1-2026 and
  Feb-2026 LNG-newbuild-talks items, both well pre-window. Nothing found.
- **2343 (Pacific Basin)** — HKEX poller alive (`last_polled 2026-08-29T20:21`), **watermark
  2026-06-30**; its three 8/21 documents (Interim Report + 2 circulars) are **prior-window**
  and were read in the last digest. **No HKEX arrival 08-24→08-29.** Searched, nothing found.

---

## Archive gaps (Step 4)

**No unaccepted gap in this window.** `inputs/research_pareto/2026/08/` holds a Shipping
Daily for **every business day** 8/24 · 8/25 · 8/26 · 8/27 · 8/28, plus the Frontline
Newsflash (8/28), a Golar company report (8/24) and the Container Weekly (8/28). Nothing to
backfill, and I have added nothing to `inputs/archive_gaps.yaml` — accepting a gap needs
channel-side evidence and is the owner's call.

The accepted entries in that file remain the July/August Pareto cadence windows
(2026-07-06→07-13, 07-15→07-19, 07-21→07-27, 07-29→08-02), all dated 2026-08-13.

**A different kind of hole did occur this week** and is recorded in WATCH rather than here,
because it is a *collection* outage, not a *publication* gap: the EDGAR/newsweb pollers and
the price refresh were down 8/25→8/29. The filings were recovered by the catch-up run; the
prices were not.

---

## OWNER SUMMARY — what I would action first

1. **BRUT — re-anchor the whole triplet, or explicitly decide not to.** This is the only item
   where the model is currently producing a **confident wrong answer**: `BUY, −34.3pp broker
   spread` computed from a **pre-demerger price against a pre-demerger NAV**, while the tape
   is 36.6% lower and eight hulls plus $50m of cash have left. Pareto's **8/28 kr 44.0 / 1.03x**
   is the matched post-demerger replacement, and the 8/25 daily gives the NAV read (NOK 45)
   independently. Decide the carry (stub vs stub+OMC) and move price, P/NAV and target
   together.
2. **Unblock the mechanical chain.** The `dirty-tree` skip is now self-perpetuating —
   this digest will block the next price refresh exactly as the 8/24 one blocked the 8/25 run.
   Prices are 4 days stale across all 25 names, and nothing since 8/25 has reached the model.
3. **Promote the 8/28 Pareto vintage (M10).** One matched-vintage refresh clears three weeks
   of drift across ~20 names and is the cleanest, lowest-risk promotion available this week.
4. **FRO — close or re-scope the open P1 print.** The named venue has now reported. The
   $270m/2×VLCC-2017 is confirmed by the issuer, but **the vessel names still do not exist
   publicly**; decide whether the print promotes without them or the item stays open.
5. **The three genuinely new fixtures** — FRO's 2 × VLCC at **$120,000/day × 1yr** (issuer),
   TRMD's *Torm Herdis* at **$51,500/day × 1yr** (VesselsValue), BWLP's **5-year at mid-high
   $40,000s** (issuer). All three sit **above** the corresponding modelled rates.
6. **HAFN's issuer-published NAV ($8.89/sh)** — a rare independent triangulation, landing
   within ~10% of both the watchlist-implied and the Pareto-implied NAV.
7. **TRMD's newbuild order** (6 MR 2029 + 2 options 2030) and **CMBT's nine dated deliveries**
   — pure manifest/schedule inputs, no valuation judgement needed.
8. **LPG *Clermont* at ~$91m** — the highest-value S&P lead of the week (named vessel, year,
   price, and two same-year comparables), but **broker-reported**; worth one confirmation
   attempt at Dorian's own newsroom before it is treated as sourced.
9. **GNK** — record that Diana is now a **seller** at ~$27, and fix the watchlist comment
   that still calls the proposal live. Third digest carrying this.

*Review-only run. One file written: this digest. No pipeline, no promotion, no ingest, no
git, no edits to any YAML, decision log or market-data file.*
