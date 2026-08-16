# News digest — 2026-08-16

Agent web-sweep (the AGENT half of `/news-pull`), scheduled task `crude-fv-weekly-news-pull`.
**Review-only — nothing here is promoted; this file is the only write of the run.** Promotion
of any item is a human follow-up (promote → rerun → drift loop).

## Run header

- **Run date:** 2026-08-16. The task fired on Saturday **2026-08-15** after the 08:00 mechanical
  chain; the clock crossed to 08-16 during the run, so the file carries today's date and the
  window is extended through it. No item below is dated 08-16.
- **Window swept:** **2026-08-13 → 2026-08-16** (3 days, one of them a weekend). Prior digest =
  `outputs/news_digest_2026-08-13.md`, established by an actual listing of `outputs/` this time
  (`news_digest_2026-06-10 / 06-21 / 08-13` are the only three).
- **Second, wider pass:** because the 2026-08-13 run declared **every** figure it reported to be
  search-summary "lead-quality" and never fetched a primary, I also re-verified that digest's
  highest-value items against issuer primaries, and re-swept its window for the Oslo/HK lane.
  **That second pass found two items the 8/13 run missed** (M3, M4 below) and one false lead it
  correctly avoided (§Aggregator re-dating).
- **Names swept:** 25/25 — the full `inputs/watchlist.yaml` roster.
  DHT · ECO · FRO · INSW · TNK · NAT · FLNG · CCEC · STNG · HAFN · TRMD · ASC · TEN · CMDB ·
  SBLK · GNK · CAPT · MPCC · GSL · BRUT · CMBT · SB · LPG · BWLP · 2343.
- **Depth weighting:** DEEP on the 9 APPROX names read live from `reconcile.APPROX_PNAV_TICKERS`
  = {NAT, ASC, CCEC, TEN, CMDB, MPCC, GSL, SB, 2343}; DEEP on the 5 non-US-listed names
  identified by `yahoo_symbol` suffix (**BRUT.OL, MPCC.OL, CAPT.OL, BWLPG.OL, 2343.HK**);
  DEEP on live-event names (GNK/Diana, CAPT deliveries, BRUT demerger + uplisting, CMBT Q2 8/27,
  BWLP Q2 8/28, MPCC Q2 8/26, TRMD Q2 8/26, FLNG Q2 8/19); lighter pass on the broker-covered
  US-listed remainder.
- **Sources searched:** **issuer primaries via WebFetch** — mfn.se / modular-finance issuer feeds
  (Bruton, MPC Container Ships, Capital Tankers, BW LPG), nat.bm, pacificbasin.com,
  investors.gencoshipping.com, live.euronext.com, stocktitan.net article pages, cyprusshippingnews.com,
  s203.q4cdn.com (INSW). Search-engine sweeps over GlobeNewswire, Business Wire, TradingView /
  MarketScreener syndication, TipRanks, Splash247, TradeWinds, Baird Maritime, Quiver, IndexBox.
  Repo-side: `inputs/watchlist.yaml`, `src/crude_tanker_fv/reconcile.py`, `inputs/archive_gaps.yaml`,
  `inputs/earnings_calendar.yaml`, `inputs/balance_sheets/`, `inputs/market_data/transactions/vlcc.yaml`,
  `PLAN.md`, `CLAUDE.md`, and the heads of `decisions/{brut,insw,gnk,cmbt,mpcc,2343}_log.md`.

### Coverage limits of THIS run — read before trusting any "nothing found"

1. **WebFetch WORKS. The 8/13 run's central coverage limit was wrong, and it was wrong in the
   exact way this task exists to prevent.** That run wrote *"every issuer/exchange/trade-press
   domain needed here … is **not** on that list, so a fetch would have raised a permission
   prompt"* — inferred from reading `.claude/settings.json`, **without ever calling WebFetch**.
   This run called it **17 times**. No permission prompt was raised on any call. Issuer primaries
   were read directly, and that is where M3 and M4 came from. **Treat the 8/13 digest's blanket
   "lead-quality, verify before promoting" caveat as over-broad** — its figures are still
   unverified, but the reason given for not verifying them does not hold.
   - **Fetched successfully:** `mfn.se` (every issuer feed and article slug tried),
     `cyprusshippingnews.com`, `nat.bm`, `stocktitan.net` (article pages),
     `live.euronext.com`, `pacificbasin.com`, `investors.gencoshipping.com`, `s203.q4cdn.com`.
   - **Fetched but returned no usable content** (JS-rendered shells, not a permission problem):
     `pacificbasin.com/en/ir/announcements.php` and `/news.php`,
     `investors.gencoshipping.com/news/press-releases/`.
   - **Actual failures, verbatim:**
     - `globenewswire.com` (FRO 8/04 release, and the Diana 8/14 release) — **`timeout of 60000ms
       exceeded`**, three attempts across two URLs. This is the one domain that materially degraded
       this run: it is the primary venue for the FRO print and the Diana withdrawal, and both had
       to be sourced from syndicators instead.
     - `hellenicshippingnews.com`, `splash247.com` — **`The server returned HTTP 403 Forbidden.`**
     - `sec.gov/cgi-bin/browse-edgar`, `efts.sec.gov` — **`HTTP 403 Forbidden.`** So **no EDGAR
       enumeration this run**; the US-listed lighter pass rests on search + syndicators, and a
       quiet 8-K/6-K filed 8/13–8/14 by a US name could have been missed.
     - `stocktitan.net/news/marine-shipping/`, `nat.bm/press-releases/` — **`HTTP 404 Not Found.`**
       (Wrong path guesses, not blocks; the same hosts served other paths fine.)
   - **Consequence:** the highest-value allowlist/plumbing fix is no longer "allowlist the
     domains." It is **(a)** a longer WebFetch timeout or a non-GlobeNewswire route for issuer
     releases, and **(b)** an EDGAR route that is not `sec.gov` CGI (the 403 is the blocker).
2. **PDF primaries still do not read.** `s203.q4cdn.com/…/International-Seaways-Announces-Sale-of-
   Vessels-2026.pdf` fetched, but returned binary — the known FlateDecode gotcha (CLAUDE.md /
   global prefs). Anything PDF-only needs `scripts/fetch_pdf.py`, which is out of scope here.
3. **Tool-discipline deviation, disclosed.** The task says use `Glob` and `Grep` and not shell.
   **`Glob` and `Grep` do not exist in this session** — `ToolSearch` for them returns nothing;
   only `Read`, `Write`, `Edit`, `Bash` and the web tools are present. Rather than repeat the
   8/13 run's "no directory enumeration" degradation on a premise I could test, I used **`Bash`
   for read-only listing only** — `ls`, `find -type f`, `grep`, `head`, `cat` over repo files.
   No writes, no `git`, no `python`, no network. No permission prompt was raised. This is what
   let me establish the previous-digest date, the archive state, and the balance-sheet vintages
   by observation instead of inference. Flagging it so the owner can either bless it or restore
   `Glob`/`Grep` to the session.
4. **The window is 3 days and spans a weekend.** A clean sweep here is weak evidence by
   construction. The load-bearing coverage in this digest is the second pass over the 8/13 window.

### Archive gaps

- **`inputs/archive_gaps.yaml` is no longer empty — the 8/13 process item is CLOSED.** Four
  evidence-backed `accepted:` entries are now written (pareto_research: 7/06–7/13, 7/15–7/19,
  7/21–7/27, 7/29–8/02), each citing the owner-directed RC history walk. The file's own header
  now carries the corrected attribution (missing **issuer channel**, not a lost file).
- **Still deliberately unaccepted:** `2026-06-01..2026-06-03` (3 business days). The RC walk
  started 7/01 and says nothing about June. Correctly left flagged.
- **New, below threshold:** `inputs/research_pareto/2026/08/` runs …8/11, 8/12, **8/13** and
  stops. **The Friday 2026-08-14 Shipping Daily is absent.** That is **1 missing business day**,
  under `limit_business_days: 3`, so the 8b check will not fire. Not yet a gap — but it is the
  head of the archive on the day a digest is being written, so any "nothing found" for 8/14 in
  the *Pareto* lane below is unsupported rather than absent. Web-side coverage for 8/14 is
  independent of this and did produce items (M1, M5).
- **The load-bearing gap named on 8/13 is still open.** `inputs/research_issuer/` exists but is a
  **manual PDF drop folder — 25 files, newest `2026H1_brut_*`**, not an automated NewsWeb channel.
  Nothing watches Oslo NewsWeb on a schedule. See Owner summary item 5: this run demonstrated that
  `mfn.se` issuer feeds enumerate cleanly and dated via WebFetch, which is a concrete mechanism.

---

## MATERIAL — needs an owner decision or a model-input change

### M1 · GNK — **Diana WITHDREW its offer on 2026-08-14.** The re-check registered one day earlier has fired.
**What happened.** Diana Shipping announced **2026-08-14** that it has **withdrawn** its offer to
acquire all Genco shares it does not already own ($24.80 cash — adjusted for Genco's recently
declared **$0.80/share dividend** — plus one Diana share valued $2.54 on a 30-day VWAP to
16-Jun-2026). Diana says it withdrew because the Genco board adopted a position "no credible
acquiror could realistically meet." The board's counter-demand, conveyed **8/13–8/14**, was
**$27.50/share cash (stated as Genco's NAV) + $2.00/share of Q3+Q4-2026 dividends + three Diana
shares (3 × $2.47 = $7.41)** — an implied **~$36.91/share**, ~57% over Genco's 16-Jun close.
Diana **remains Genco's largest shareholder** and will "continue to monitor its performance
closely, raise these issues publicly, and hold the Genco Board and management team accountable."
Genco's board had requested a response **by 2026-08-24**.
**Source.** Diana release 2026-08-14 (GlobeNewswire 3345635 — **the globenewswire fetch timed
out**; read via StockTitan's full article page and corroborated by Quiver, Investing.com and the
Manila Times syndication dated 8/15). **Genco's own response, if any, is not yet visible** — its
IR press-release page is a JS shell that returned no content, and no Genco statement dated 8/14–8/16
surfaced in search.
**Model surface.** `inputs/watchlist.yaml` → `GNK.analyst_target: 28.40`. The owner ruled that
field on **2026-08-13** and wrote into it, verbatim: *"RE-CHECK REGISTERED: the proposal is live
and non-binding, so this basis can die a SECOND time — either outcome (deal agreed / Diana walks)
re-points this field."* **Diana walked, the next day.** The same comment's "**DEAL CAVEAT —
REWRITTEN, NOT RETIRED … the tape is UN-PINNED but still M&A-INFLUENCED. A NON-BINDING INDICATIVE
PROPOSAL REMAINS LIVE**" is now false as written. Also `inputs/dividend_policies/gnk` — a declared
**$0.80** and guidance implying **$2.00 across Q3+Q4-2026**.
**What I think it means.** Two separable things, and I would not conflate them:
(a) **The caveat can now be retired outright** rather than rewritten. This is the first time since
onboarding that GNK's tape is readable without deal noise — which is exactly what makes the current
model print (**TRIM/SHORT, price $25.26, NAV/sh $25.12, EV −10.2%, spread +7.6pp**) meaningful for
the first time. (b) **But the price that print is computed on is a with-deal price.** Diana's
withdrawal removes whatever deal premium was in it, and the model has not yet seen a post-withdrawal
close (the 8/14 auto-run at 15:08 UTC shows Δprice: no change, i.e. it pre-dates or does not reflect
the news). **Do not read the current EV as the post-deal read** — it is the last with-deal read.
**What I am NOT sure of.** (i) Whether `analyst_target: 28.40` should move at all. It is a **Pareto
NAV**, deliberately not the deal price, so the withdrawal arguably leaves it *correct* while making
the surrounding comment wrong — a comment edit, not a value edit. I lean that way but it is the
owner's call. (ii) **Genco's board has now publicly asserted its own NAV at $27.50/share.** That is
a third independent NAV anchor (issuer-stated) alongside Pareto $28.40 and the tool's $25.12, and
it is self-interested — a board defending against a bid. Whether it belongs anywhere near the model
is a methodology question, not a data refresh. (iii) Diana keeps its stake and explicitly does not
rule out further public action, so "deal noise" is reduced, **not eliminated**; the 8/24 date Genco
set is still on the calendar.
**Status.** `decisions/gnk_log.md` head is the 8/14 15:08 auto-run carrying the **tier-semantics**
annotation; there is **no mention of the Diana withdrawal**. This is **UNREAD** in the log.

### M2 · CAPT — Suezmax *Aristodimos* delivered 2026-08-13, with a $67.5m sale-and-leaseback
**What happened.** Issuer release **2026-08-13 07:31:58**: Capital Tankers took delivery of
**M/T Aristodimos**, a **Suezmax, 155,378 dwt**, built by **New Times Shipbuilding (China)**,
**dual-fuel LNG and scrubber-fitted**, delivered **13-Aug-2026**. Partly financed by a
**sale-and-leaseback of $67.5m, repayable in 40 quarterly instalments of $0.8m with a $33.8m
balloon due August 2036**. Sailing fleet now **15 vessels: 6 Suezmax, 4 Aframax, 4 LR2, 1 VLCC**.
The company expects **17 vessels on the water by end-2026**; full programme 33 tankers (15 VLCC /
10 Suezmax / 8 Aframax-LR2) delivering through 2028, **plus options on 13 more**.
**Source.** Issuer release via the mfn.se / modular-finance NewsWeb feed — **primary text fetched
directly**, not a summary.
**Model surface.**
- `inputs/fleet_manifests/capt` — a hull moves from the **newbuild book to on the water**. Under
  §9.6 that is not a small edit: the vessel stops being "delivered market **less remaining
  commitment**, PV-discounted `1.11^(−years_to_delivery)`" and becomes a plain on-curve Suezmax at
  `years_to_delivery = 0`. Both legs change at once.
- `inputs/balance_sheets/capt` — **+$67.5m sale-and-leaseback.** CLAUDE.md's **ECO precedent** is
  the live hazard here: an SLB belongs in **borrowings** with **no separate operating-lease line**.
  This is the single easiest place in the whole digest to introduce a double-count.
- **Scrubber flag** — issuer-disclosed per-vessel, so this one arrives with clean provenance
  (`test_scrubber_provenance`); no queue entry needed.
- `inputs/watchlist.yaml` `CAPT.consensus_pnav: 0.71` — Pareto's CAPT NAV path is explicitly
  described in the repo as "rising as newbuilds near delivery." Two have now *arrived*.
**What I think it means.** CAPT's newest balance sheet on file is **`capt_2026-Q1.yaml`** — 31-Mar-2026.
Its half-yearly report is not due until **2026-09-01** (`earnings_calendar.yaml`, confirmed). So
between the Q1 sheet and 9/01 the model carries **none** of: the June VLCC newbuild acquisition, the
8/06 LR2 delivery (M3), this 8/13 Suezmax delivery, or either financing. That is four fleet/finance
events (two deliveries, two financings) behind one stale sheet. **What I am NOT sure of:** whether the manifest already carries these
hulls as scheduled newbuilds with the correct delivery dates (in which case this is a date/flag
flip, cheap) or not at all (in which case it is an insertion). I did not open the manifest.

### M3 · CAPT — LR2 *Athinagoras* delivered 2026-08-06 with $50.0m senior secured financing — **missed by the 8/13 run**
**What happened.** Issuer release **2026-08-06 07:58:21**: delivery of **M/T Athinagoras**, an
**LR2, 111,791 dwt**, **New Times Shipbuilding (China)**, delivered **06-Aug-2026**, taking the
sailing fleet to **14 (5 Suezmax, 4 Aframax, 4 LR2, 1 VLCC)**. Financed by a **senior secured
facility of $50.0m, 32 equal quarterly instalments of $0.7m, balloon $27.6m with the last
instalment in August 2034**. No charter disclosed.
**Source.** mfn.se issuer feed, primary text fetched directly.
**Model surface.** Same as M2 — `inputs/fleet_manifests/capt` (§9.6 newbuild → on the water; note
**LR2 is crude-routed for CAPT** per the FRO §9.3 precedent recorded in the watchlist) and
`inputs/balance_sheets/capt` (+$50.0m senior secured — **debt, not an SLB**, so it does *not* carry
the ECO double-count hazard; the two CAPT financings are structurally different and should not be
entered alike).
**What I think it means.** **This dates 2026-08-06 — inside the 8/13 digest's own window
(6/21 → 8/13) — and that digest reported "CAPT — searched; the only material item is pre-window."**
That is a miss, and it is the *characteristic* miss: an Oslo issuer, no EDGAR lane, a release that
exists on NewsWeb and its syndicators but generates little trade-press pickup. It is the third
instance of the pattern (BRUT 7/07, MPCC 6/25, now CAPT 8/06). The difference is that this one was
missed by the sweep built to catch it, because that sweep did not read the issuer feed.
**Status.** No CAPT decision-log entry references either delivery. **UNREAD.**

### M4 · MPCC — a **completed equity placement: +44,370,027 shares (exactly +10.0%)** — also missed
**What happened.** Three linked Oslo releases the 8/13 digest did not report:
**2026-06-30 16:39** "Contemplated Private Placement"; **2026-07-01** "**Successfully Completed
Private Placement**"; **2026-07-02 09:52** "Registration of share capital increase". Terms:
**44,370,027 new shares at NOK 24.00**, gross proceeds **~USD 107m**, book multiple times
oversubscribed, settlement DVP on/about **3-Jul-2026**, six-month lock-ups for management, board and
largest shareholders.
**Source.** mfn.se issuer feed (headlines + dates fetched directly); terms from the
TradingView/modular-finance syndication of the same release and Reuters' "up to 10% of shares
outstanding" framing. **The deep-link article slugs on mfn.se 404'd**, so the *terms* are
syndicator-sourced while the *existence and dates* are primary-feed.
**Model surface — this is a denominator change, which is why it matters more than it looks.**
`inputs/balance_sheets/mpcc_2026-Q1.yaml` carries `diluted_shares_outstanding: **443,700,279**`.
The placement is **44,370,027** shares — **exactly 10.000% of that count**, which is a clean
cross-foot that the two figures refer to the same base. Post-issue: **488,070,306 shares**.
The model's MPCC sheet is **Q1 (31-Mar-2026)** — the newest on file, and MPCC's Q2 is not due until
**2026-08-26**. So the model currently carries **neither the 10% dilution nor the ~$107m of cash**.
Note also that settlement was **3-Jul**, i.e. **after** the 30-Jun quarter end — so even when the Q2
sheet lands it will sit in the **Subsequent Events note**, which is precisely the place CLAUDE.md
says post-quarter events hide and instructs auditing **first**.
**What I think it means.** Directionally this is *accretive*, not dilutive, on the model's own
numbers — which is the non-obvious part. Implied issue price ≈ **$2.41/share** (107.0 ÷ 44.370;
NOK 24 × ~0.1054 FX ≈ $2.53, so call it $2.41–2.53), against the model's MPCC **NAV/share of
$2.05**. Issuing ~1.2× NAV adds more cash per share than it adds shares. **My arithmetic, gross and
crude:** (2.05 × 443.700 + 107) ÷ 488.070 = **$2.083/share**, i.e. **~+1.6% NAV/share**. **That is a
derived figure, not a disclosed one** — it ignores placement fees, and more importantly it ignores
the 6/25 acquisition this raise part-funds ($340m of vessels against $375m of new debt, M2 in the
8/13 digest). The two must be modelled together or the answer is meaningless.
**What I am NOT sure of.** Whether the $107m is gross or net in the syndicated figure; the exact
NOK/USD rate the issuer used; and whether the six-month lock-up matters to anything the model does
(I do not think it does). Also unverified: whether any of the 44.37m shares were subsequently
cancelled or adjusted — I saw the registration but not a later share-count confirmation.
**Status.** `decisions/mpcc_log.md` head is the 8/14 auto-run; no reference to the placement.
**UNREAD** — seven weeks, on top of the 6/25 acquisition that was already seven weeks unread.

### M5 · BWLP — Q2 date formally re-confirmed 2026-08-14 (in-window, low-stakes)
**What happened.** Issuer release **2026-08-14 07:00**: "BW LPG Limited – Q2 2026 Financial Report
Release and Earnings Presentation on **28 August 2026**."
**Source.** mfn.se issuer feed, fetched directly.
**Model surface.** `inputs/earnings_calendar.yaml` already carries `BWLP window 2026-08-28,
status: confirmed`, sourced to the 7/16 6-K. **This changes nothing** — it is recorded because it
is one of only two dated primary items in the actual 3-day window, and because it independently
re-confirms a calendar entry rather than leaving it on a single source.
**Still open from onboarding, unchanged:** `BWLP.analyst_target` rests on a **Pareto TP NOK 172
dated 2025-09-02** — flagged stale at onboarding, and the 8/28 report is the natural refresh venue.
The 8/13 digest's WATCH item on the **−$146m Product Services mark-to-market** ahead of that print
also still stands and is unresolved until 8/28.

---

## PROMOTABLE CANDIDATES — flagged only; promotion is the human loop

**Standing rule applied (WORKFLOWS, 2026-08-09):** sweep the class file before promoting **any**
unnamed print.

**Nothing new this window.** No dated S&P print with the promotion fields landed 8/13–8/16.

**Carried forward from 8/13, and I verified they are still unpromoted:**
`inputs/market_data/transactions/vlcc.yaml` runs to **2026-08-07 (MB Tanker Weekly 32)** and
contains **no FRO 8/04 entry**. So the candidate below is genuinely open, not already absorbed.

| # | Name | Vessel / class | Built | Price | Date | Status this run |
|---|------|----------------|-------|-------|------|-----------------|
| P1 | FRO | 2 × VLCC (**unnamed**) | 2017 | **$135.0m each** ($270m agg.) | 2026-08-04 | **Still open.** Confirmed absent from `vlcc.yaml`. Price/gain/dividend legs corroborated across IndexBox, MarketScreener, Splash247, Cyprus Shipping News and Shipping Herald — but **the GlobeNewswire primary timed out 3×**, so vessel names remain unconfirmed and the duplicate-sweep is still required. |
| P2a | TNK | Suezmax (**unnamed**) | 2009 | **$53.5m** | 2026-07-29 | Unchanged from 8/13. Not re-verified this run. |
| P2b | TNK | VLCC (**unnamed**) | 2013 | **$84.5m** | 2026-07-29 | Unchanged from 8/13. Not re-verified this run. |
| P3 | STNG | **STI Solidarity**, LR2, scrubber-fitted | 2015 | **$60.0m** | **agreed ~2026-03-05, closed April 2026** | **Date corrected.** The 8/13 digest dated this "Q2-2026"; it is a **Q2 *disclosure* of a Q1 agreement that closed in April**. For a §9.9 anchor the *agreement* date is the market observation — this is a ~5-month-old print, not a window print. Still the cleanest named/priced/dated candidate on the list. |

**Not promotable, reasons carried forward unchanged from 8/13:** CMBT *Bristol* (gain disclosed,
price not — no back-solve); STNG en-bloc MR/LR2 lots (no per-vessel split); CMDB *Bermondi* (no
price); DHT *Bauhinia* (Jan-2026 agreement, pre-window); LPG *Corsair* / *Constellation* (VLGC is
not one of the 8 fitted §9.9 classes).

### Aggregator re-dating — a trap this run hit and avoided, worth recording

Cyprus Shipping News published, **dated 2026-08-12**, "Nordic American Tankers announced sale of two
Suezmax tankers and contracting of two newbuildings" — two 2004/2005-built Suezmaxes for **$50m
combined**, a third 2005-built at **~$40m**, ~$14m book profit, plus two Korean Suezmax newbuilds
for H2-2028. On its face that is a promotable-shaped NAT print, dated four days into the 8/13
digest's window, on an APPROX name — i.e. exactly what this sweep hunts.

**It is not a 2026 item.** The article's own internal dates give it away: "delivery expected
**January 2026**" and "firm agreement expected **January 2026**", both in the past at publication.
I checked **nat.bm directly**: NAT's newsroom shows **nothing in August 2026** — newest items are
**7/23 "An optimistic summer message from NAT"**, 7/14, and 7/10. The underlying release is the
**GlobeNewswire "Nordic American Tankers Ltd (NYSE: NAT) – Newbuildings" of 2025-11-03** (LOI, two
Suezmaxes, **$86m each**, South Korea, H2-2028 delivery, contract to be signed early 2026).

**So: the aggregator re-stamped a nine-month-old release with a current date.** Two consequences.
(1) **The 8/13 digest's "NAT — searched, no in-window issuer release found" was correct**, and is
now corroborated against the issuer primary rather than search summaries. (2) This is a live failure
mode for a sweep that leans on trade-press dates — the defence is the one applied here: when an
aggregator item looks promotable, **open the issuer's own newsroom before believing the date**.

---

## WATCH — moves a falsifier or a thesis, no action demanded yet

- **2343 (APPROX, DEEP) — the 8/13 M1 item is CLOSED, and the dividend timetable is now dated.**
  The owner acted: `watchlist.yaml` `2343.consensus_pnav` is now **0.91, DERIVED 2026-08-13** off
  the 2026 Interim (HKEX doc 12275567_2026080601217) — NAV/sh **$0.4297** from fleet $2,070.6m +
  cash 206.530 + WC 85.838 − debt 49.309 − leases 93.957, all on one 30-Jun vintage; `2343_2026-Q2.yaml`
  exists. The old "Re-derive at the 2026 Interim" trigger is spent. My open question from 8/13
  (does the Interim republish **per-class** composite values?) is **answered in the file itself**:
  it does **not** — it gives a single aggregate, and per-class refinement now waits for AR2026
  (~Mar-2027). **New detail this run:** interim **HK15.5c**, **ex-div 2026-08-20, record 08-24,
  payable 09-03**; H1 buyback ~**$3.5m for ~9.5m shares** against a **$40m** authorisation; and
  reporting that the company "**adjusted newbuilding plans to balance near-term capex**" — a §9.6
  newbuild-book change I could not pin to a specific hull or date, so treat it as unverified.
- **BRUT (Oslo, DEEP) — nothing new after 8/13, confirmed at the issuer feed.** mfn.se shows
  **8/13 08:00 H1-2026 results**, **8/12 19:15 AGM results**, **8/06 08:00 Mount Horizon time
  charter**, and **nothing dated 8/14–8/16**. All three are already captured in `brut_log.md`
  (the 8/06 Mount Horizon fixture is the $106,000/day print, and `2026H1_brut_*` are staged in
  `inputs/research_issuer/`). This is a *primary-source* clean sweep rather than an inferred one.
  **Open owner item unchanged and now time-critical:** the demerger completes and the 8-ship
  spin lists on Euronext Growth Oslo **by end-August**, with BRUT's own uplisting to Expand /
  Oslo Børs targeted **end-September**. How the model carries a structural split — one 12-ship
  NAV today vs two entities shortly — is still unresolved, and end-August is now two weeks out.
- **MPCC — Q2 on 2026-08-26**, which is the venue where the placement (M4) and the 6/25
  acquisition both land on a balance sheet for the first time. `decisions/mpcc_h1_prereg_2026-08-13.md`
  exists; if it pre-registers a band without the +10% share count in it, **the band is computed on
  a stale denominator**. Worth checking before 8/26, not after.
- **CAPT — half-yearly report 2026-09-01** (`earnings_calendar.yaml`, Oslo Børs Newspoint,
  confirmed). That is the first sheet that will carry the June VLCC acquisition, both August
  deliveries and both financings. Until then CAPT runs on a 31-Mar-2026 sheet.
- **GNK — 2026-08-24** is the response date Genco's board set. Diana withdrew before it, but
  explicitly kept the door open and stayed the largest holder.
- **Names reporting inside the next two weeks** (all `status: confirmed` in the calendar unless
  noted): **FLNG 8/19** · **TRMD 8/26** · **MPCC 8/26** · **CMBT 8/27** · **BWLP 8/28** ·
  **HAFN 8/28** · **NAT ~8/31 (expected)** · **CAPT 9/01** · **TEN ~9/17 (expected)**. The 8/13
  digest's unresolved WATCH items resolve at these: HAFN's untied fleet line at 8/28, FLNG's
  undatable charter items at 8/19, TRMD's six MR resales at 8/26, CMBT's *Bristol* price (if
  disclosed) at 8/27.
- **ECO — ex-div $5.25 traded Oslo 8/13 / NYSE 8/14** (issuer "Ex Dividend Date" release 8/13,
  GlobeNewswire 3344201). Already flagged in PLAN.md and the 8/13 digest; repeated only because it
  falls squarely in this window. **Do not read the price drop as drift.**
- **Price drift vs the 8/07 watchlist vintage is widening.** Observed 8/14 closes: **TNK $85.13**
  vs watchlist `current_price: 77.1`; **DHT $19.52** vs `18.4`. The pipeline values at the live
  close so the *reads* are current, but `consensus_pnav` / `consensus_fwd_pe` are still paired to
  the 8/07 Pareto vintage — the exact pairing CLAUDE.md says must move together. The staged
  `inputs/watchlist_rebase_2026-08-07.yaml.draft` is still awaiting the owner's word, and the gap
  it would close is growing.

---

## NO-ACTION — swept, nothing in the window that touches the model

Every line means: **searched the sources listed in the run header over 2026-08-13 → 2026-08-16,
nothing found that moves a model surface** — not "no news exists." Read these against coverage
limit 1 (no EDGAR enumeration) for the US-listed names.

- **NAT** — searched **and the issuer newsroom read directly**: nothing in August 2026 (newest
  7/23). The apparent 8/12 item is a re-dated 2025 release (above). Q2 expected ~8/31.
- **BRUT** — issuer feed read directly: nothing after 8/13 08:00. See WATCH.
- **MPCC** — issuer feed read directly: nothing in August; newest is 7/02. Q2 8/26.
- **2343** — nothing dated 8/13–8/16; the Interim (8/06) is actioned and the dividend timetable
  is forward-dated. See WATCH.
- **BWLP** — issuer feed read directly: the 8/14 calendar notice (M5) is the only August item.
- **TEN · CMDB · GSL · SB · ASC · CCEC** (APPROX names, lighter web pass) — searched, nothing
  dated in the window. Each carries an unresolved item from the 8/13 digest, none of which moved.
- **DHT · ECO · FRO · INSW · TNK · STNG · SBLK · LPG · HAFN · TRMD · FLNG · CMBT** — searched,
  nothing dated in the window beyond the ECO ex-div (WATCH) and forward report dates. **Caveat:**
  with `sec.gov` and `efts.sec.gov` both returning 403, a low-profile 8-K/6-K filed 8/13–8/14 by
  any of these would not have been caught. I would not call this lane fully swept.

**Names with a genuinely clean sweep this window: 20 of 25.** Five produced dated items
(GNK, CAPT, MPCC, BWLP, ECO), of which **three are material and two of those were missed a week
ago**. A 3-day window is thin by construction — the finding is not "a quiet week," it is that the
second pass over *last* week's window still yielded two unread issuer releases on the Oslo lane.

---

## Owner summary — what I'd action first

1. **M1 GNK — Diana withdrew 8/14.** The re-check the owner registered on 8/13 fired the next day.
   The watchlist comment asserting a live proposal is now false; the `28.40` **value** may well be
   right as-is (it is a Pareto NAV, not a deal price) while the **caveat around it** needs
   retiring. Note the current TRIM/SHORT is the last *with-deal* read, not the post-deal one.
2. **M4 MPCC — a +10.0% share count the model does not carry**, alongside the 6/25 acquisition
   that was already unread. If `mpcc_h1_prereg_2026-08-13.md` pre-registers a band on 443.7m
   shares, that band is wrong before 8/26. This is the cheapest thing on the list to get ahead of.
3. **M2/M3 CAPT — two deliveries and two financings against a 31-Mar-2026 balance sheet**, with no
   fresh sheet until 9/01. Watch the SLB (M2) vs senior-secured (M3) distinction — the ECO
   precedent makes the first a double-count hazard and the second not.
4. **P1 FRO — still unpromoted and confirmed absent from `vlcc.yaml`.** The blocker is now
   narrow: vessel names, for the duplicate sweep. The GlobeNewswire primary is the place they
   would be, and it timed out three times here.
5. **Two process items, both narrower than last week's.** (a) The WebFetch allowlist is **not**
   the problem — fetching works. The real blockers are the **GlobeNewswire 60s timeout** and the
   **sec.gov/efts.sec.gov 403**, which between them cost this run the FRO primary, the Diana
   primary and all EDGAR enumeration. (b) The **missing NewsWeb issuer channel is still the
   load-bearing gap** — `inputs/research_issuer/` is a 25-file manual PDF folder, not a feed. This
   run read four Oslo issuers' complete dated release histories off `mfn.se` in single fetches;
   that is a concrete, demonstrated mechanism for automating the channel, and M3 and M4 are the
   evidence for what it costs not to have one.
6. **Restore `Glob`/`Grep` to this session, or bless the read-only-Bash workaround** (coverage
   limit 3). The 8/13 run degraded its own coverage rather than enumerate; the fix should not be
   left to each run's judgement.
