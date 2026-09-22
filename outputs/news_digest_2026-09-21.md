# News digest — 2026-09-21

## Run header

**Run date:** 2026-09-21 (Monday).
**Scheduled for:** Saturday 2026-09-19. The run started 9/19 and the session clock rolled to
9/21 mid-run, so the digest is filed under 9/21 and the sweep window was EXTENDED to the
current date rather than truncated at 9/19. Two business days (9/18 close, 9/21 open) are
therefore inside this digest that a Saturday run would have missed — including the 9/21
Shipping Daily and the 9/21 MPCC ex-dividend. Stated so the next run's window starts from
9/21, not 9/19.

**Window swept:** **2026-09-12 → 2026-09-21** (inclusive). Previous digest established by
listing `outputs/news_digest_*.md`, not inferred: the newest is `news_digest_2026-09-12.md`
(8 digests on disk: 06-10, 06-21, 08-13, 08-16, 08-24, 08-29, 09-07, 09-12).

**Names swept — 25 watchlist names, from `inputs/watchlist.yaml`, nothing added:**

| Depth | Names | Why |
|---|---|---|
| **DEEP — APPROX-pNAV** (`reconcile.APPROX_PNAV_TICKERS`, read from source, not hardcoded) | NAT · ASC · CCEC · TEN · CMDB · MPCC · GSL · SB · 2343 | placeholder broker anchor; no Pareto NAV to catch a drift |
| **DEEP — non-US-listed** (by `yahoo_symbol` suffix) | BRUT .OL · MPCC .OL · CAPT .OL · BWLP (BWLPG.OL) · 2343 .HK | no EDGAR sentinel; this sweep is their only web channel |
| **DEEP — live-event** (from decision-log heads) | BRUT (uplisting due end-Sep; void re-armed to it) · CAPT (Stage-A void retired 9/18; 13-ship option expiring 12/31) · TEN (Q2 sheet build unblocked 9/18) · TRMD + HAFN (Oaktree secondary / stake build) · SBLK + SB (Athens listings) · CMBT (commitment-net landed 9/16) · BWLP (NB fork ruled 9/17) | pending or just-resolved transactions |
| **LIGHTER — broker-covered US-listed** | DHT · ECO · FRO · INSW · TNK · FLNG · STNG · HAFN · TRMD · SBLK · GNK · LPG · CMBT | EDGAR sentinel + daily filings triage already cover them |

**Not swept, and why:** OMC Tankers is **not in `inputs/watchlist.yaml`** — it is a sentinel-only
feed (`data_sources.yaml` `mfn_slug: omc-tankers`, added 8/31 so an OMC financing/fixture/uplisting
reaches the digest the day it happens). I read its feed as a channel check but did not sweep it as
a name. Nothing else expected was missing from the watchlist.

**Sources searched**

*Local, primary, read first (per the standing instruction):*
- `state/edgar_manifest.jsonl` — 125 rows; **16 arrivals filed ≥ 2026-09-11**, all read.
- `inputs/filings/**` — staged 6-K/8-K bodies and exhibits for TRMD (×4 accessions), SBLK (×4),
  SB (×2), HAFN, FRO, TEN, GSL, LPG, MPCC (newsweb), BRUT + CAPT (newsweb 9/10).
- `decisions/filings_triage_log.md` — the daily triage's own dispositions, 9/11 → 9/18.
- `decisions/<ticker>_log.md` heads for all 25 names; `decisions/geopolitics_weekly_check_2026-09-17.md`.
- `inputs/research_pareto/2026/09/**` — Shipping Dailies **9/14, 9/15, 9/21**; the
  **9/17 Energy Conference takeaways** (12pp, published 9/18); Container Weekly 9/12–9/18.
- `inputs/research_mb/tanker_weekly/2026/2026-09-18_Tanker_Weekly_38_2026.pdf` — **MB Shipbrokers
  Tanker Weekly W38 (12–18 Sep)**, staged by the 08:00 chain ON THIS RUN'S MORNING. Its Recent Sales /
  Recent Fixtures / asset-price tables extract only under pypdf `extraction_mode='layout'` — the
  default mode returns the column headers and drops every row. See M12.
- `inputs/archive_gaps.yaml`; `inputs/market_data/transactions/*.yaml` + `_scan_state.json`;
  `outputs/sp_print_candidates.md`; `inputs/fleet_manifests/*.yaml`; `inputs/balance_sheets/hafn_2026-Q2.yaml`.

*Web:*
- MFN issuer feeds (one fetch each, complete dated history): `bruton-limited`, `capital-tankers`,
  `mpc-container-ships`, `bw-lpg`, `omc-tankers`.
- Issuer newsrooms opened directly: `nat.bm` (+ the 9/15 release itself),
  `ardmoreshipping.investorroom.com`, `ardmoreshipping.com/fleet/ardmore-endeavour`,
  `ardmoreshipping.investorroom.com/2026-08-27-...`.
- **SEC EDGAR `browse-edgar`** (ASC CIK 0001577437, 6-K list) — see COVERAGE LIMITS, it **worked**.
- **splash247.com** — worked.
- HKEXnews advanced-search page (2343); WebSearch for NAT, CCEC, ASC, TEN, CMDB, GSL/GNK/CMBT,
  2343, BRUT, and a cross-name VLCC/suezmax S&P sweep.

---

### COVERAGE LIMITS — read this before trusting any "nothing found" below

**Fetch behaviour MEASURED THIS RUN (2026-09-21). Two of the 2026-08-16 blocks did NOT reproduce
— do not carry the old list forward without re-testing:**

| Source | 2026-08-16 measured | **2026-09-21 measured** |
|---|---|---|
| `sec.gov/cgi-bin/browse-edgar` | HTTP 403 | **WORKED.** Returned ASC's full dated 6-K list. EDGAR *can* be enumerated this way today. |
| `splash247.com` | HTTP 403 | **WORKED.** Article fetched with its date and body. |
| `globenewswire.com` | frequent 60s timeout | **404** on the organization-search URL form I tried. Not re-tested on an article URL — I had no globenewswire-only item this week. Treat as untested, not as working. |
| `capitalcleanenergycarriers.com/news-releases` | — | **timeout of 60000ms exceeded.** CCEC's own newsroom did not open; its negative below rests on WebSearch + the EDGAR lane, which is weaker. |
| `hkexnews.hk` advanced search | — | Fetched, but returns the **search form only** — no results without a form submission. 2343 **cannot be enumerated** this way. Its negative rests on WebSearch + the `hkex_poll` manifest rows, whose newest 2343 entry is **2026-08-31**. |
| `mfn.se/all/a/<slug>.json` | reliable | **reliable** — all five feeds returned complete dated histories in one fetch each. |
| Issuer IR pages (nat.bm, ardmoreshipping) | JS shells fetch empty | **WORKED** and returned real dated content. |

**What that means for the negatives below, honestly:**
1. **2343 (Pacific Basin) is the weakest negative in this digest.** No primary enumeration was
   possible and the local HKEX channel's newest row is three weeks old (8/31 Monthly Returns).
   A 2343 announcement in-window would plausibly have been missed. Do not read its NO-ACTION line
   as a primary-sourced silence.
2. **CCEC's negative is second-weakest** — its newsroom timed out; EDGAR shows nothing after 8/10.
3. **BRUT, CAPT, MPCC, BWLP, OMC negatives are PRIMARY-SOURCED** — the MFN feed is the issuer's
   own complete release history and I read all of it. When I say BRUT published nothing after 9/10
   I mean the issuer feed shows nothing after 9/10, not that I failed to find anything.
4. **Two watchlist names published releases in/near the window that NEVER REACHED EDGAR** (ASC 8/27,
   NAT 9/15) — see M6 and M7. Wherever a US-listed FPI's negative rests on the EDGAR lane alone,
   that negative is now demonstrably incomplete. This is a *new* structural finding this run.
5. Figures taken from a WebSearch summary rather than an opened primary are marked **LEAD-QUALITY**
   inline and must not be promoted.
6. One aggregator-vs-issuer date conflation was caught and is recorded at M7 rather than reported
   as news.
7. **A local-source extraction trap, recorded so it is not repeated.** The MB Tanker Weekly's data
   tables are invisible to a default pypdf text extract — a first pass on W38 returned only
   `Vessel | DWT | Built | Yard | Period | Rate | Charterer` with **zero rows**, which reads exactly
   like an empty week. `extraction_mode='layout'` returns all of it. Any earlier sweep that checked
   an MB weekly with the default mode and concluded "no prints" should be treated as unverified.

---

### Archive check (STEP 4) — **A FLAGGING, UNACCEPTED 3-DAY GAP, and the Friday pattern has fired**

`inputs/archive_gaps.yaml` sets `limit_business_days: 3` — a run of ≥3 missing business days flags.
Business-day map of `Periodical-ShippingDaily` over the window (and back to 8/01 for the pattern):

```
09-14 Mon YES   09-15 Tue YES   09-16 Wed MISSING   09-17 Thu MISSING   09-18 Fri MISSING   09-21 Mon YES
```

**MISSING business days since 8/01:** 08-14 Fri · 08-21 Fri · **09-11 Fri** · **09-16 Wed** ·
**09-17 Thu** · **09-18 Fri**.

**(a) 09-16 → 09-18 is a 3-BUSINESS-DAY RUN — it hits the threshold exactly and is UNACCEPTED.**
Nothing in `archive_gaps.yaml` covers any September date; the newest accepted entry is 2026-08-21.
**News read from 9/16–9/18 is UNSUPPORTED, not absent.** Every "nothing found" below that would
have come from a Shipping Daily on those three days is a hole, not a silence.

**A plausible cause, offered as a lead and NOT as evidence — I did not accept the gap and must not:**
Pareto ran its 33rd Annual Energy Conference on **9/16–9/17** (>170 companies, >2,200 participants,
30+ shipping presenters) and published **"Key takeaways from our Energy Conference"** on 9/18 in
place of a daily. The lane is demonstrably *alive* across the hole — two Pareto products landed
9/18 (the takeaways and the Container Weekly). That is consistent with source-quiet-by-substitution,
but the file's own evidence standard requires a **channel-side** check (the Rocket.Chat history
walk), not an inference from the archive's emptiness. **Accepting this gap is the owner's call and
needs that walk.** I am flagging it, not closing it.

**(b) The Friday condition the owner wrote himself has now fired twice.** The 8/31 accepted entry
says verbatim: *"second consecutive FRIDAY absence (8/14, also accepted sub-threshold) — … re-look
only if a third Friday drops."* **A third Friday dropped (9/11, flagged by the 9/12 digest) and a
fourth dropped (9/18).** Four of the last six Fridays have no Shipping Daily. The re-look condition
is satisfied on its own terms; the "not systematic" reading recorded on 8/31 no longer holds.

`inputs/research_pareto/**` glob over the window: 9/14 daily · 9/15 daily · 9/18 Container Weekly ·
9/18 Energy Conference takeaways · 9/21 daily. No Pareto company reports in-window.

---

## MATERIAL

### M1 · ALL NAMES — the **9/17 Pareto Energy Conference takeaways** carry a full fresh price + P/NAV vintage pair for 16 watchlist names, and per-name management disclosure for 9 of them

**Date:** 2026-09-17 (report date), published 9/18.
**Source:** `inputs/research_pareto/2026/09/2026-09-18_Key takeaways from our Energy Conference.pdf`
— **local, primary, 12 pages**, analysts Haavaldsen / Klemp.

**What happened.** Pareto published its conference wrap with a valuation table covering the whole
coverage universe at 17 Sep, plus a one-page summary per presenting company. Sixteen watchlist names
appear in the table with a matched price **and** P/NAV from the same document:

| Name | 9/17 price | P/NAV | watchlist `consensus_pnav` (as_of **2026-08-28**) |
|---|---|---|---|
| BRUT | kr 50.4 | 1.17x | 1.03 |
| CAPT | kr 187.4 | 0.88x | 0.72 |
| DHT | $23.0 | 1.36x | 1.14 |
| FRO | $54.1 | 1.64x | 1.33 |
| INSW | $109.4 | 1.42x | 1.21 |
| TNK | $100.6 | 1.04x | 0.91 |
| STNG | $85.6 | 0.81x | 0.73 |
| TRMD | $36.8 | 1.15x | 0.92 |
| HAFN | $9.7 | 1.23x | 1.03 |
| BWLP | kr 241 | 1.13x | 1.27 |
| LPG | $57.9 | 1.25x | 1.06 |
| FLNG | $32.2 | 1.48x | 1.44 |
| CMBT | $19.7 | 0.93x | 0.86 |
| GNK | $27.4 | 1.01x | 0.95 |
| SBLK | $30.9 | 0.90x | 0.91 |
| MPCC | kr 27.9 | — (no P/NAV) | 1.04 APPROX |

**Model surface touched.** `inputs/watchlist.yaml` — every `current_price` / `consensus_pnav` /
`consensus_fwd_pe` triplet is stamped `as_of: 2026-08-28`. Sixteen names now have a **newer matched
pair available from a single document**, which is exactly the vintage-pair discipline the file's own
header demands ("update them TOGETHER … never the price alone"). The 9/21 daily carries an even
fresher pair (BRUT 1.14x · CAPT 0.86x · DHT 1.37x · FRO 1.74x · INSW 1.45x · TNK 1.05x · STNG 0.83x ·
TRMD 1.20x · HAFN 1.28x · BWLP 1.14x · LPG 1.25x · FLNG 1.49x · CMBT 0.96x · GNK 1.03x · SBLK 0.95x).

**What I think it means.** The 8/28 pair is now 3½ weeks stale into the sharpest tanker tape move in
the file's history, and the *direction* is uniform: broker P/NAV has re-rated **up** on almost every
crude name. Because `consensus_pnav` is a fixed ratio, broker NAV tracks the tape while tool NAV
holds — the k_broker drift the daily logs keep attributing to "the price leg" is partly a **stale
denominator**, and a refresh would move the reconcile gap on 16 rows at once.

**What I am NOT sure of, and it argues for waiting.** Pareto itself wrote on **9/21**: *"We expect to
update our estimates / NAVs / TPs shortly, with markets obviously moving extremely quickly these
days."* Its P/NAVs are computed off vessel values it repeatedly calls *"(too) conservative"* and
*"due for some positive revisions"*. So a refresh landed today would pin a denominator the publisher
has pre-announced it is about to change. I do not know whether the repo's convention prefers the
freshest pair or the most stable one — that is an owner ruling, not mine. I also cannot tell from the
table alone whether the 9/17 figures are close-based or intraday.

**Decision-log status: UNREAD as a vintage-pair event.** No `_log.md` references the conference
document, and no watchlist `as_of` has moved off 2026-08-28.

---

### M2 · BRUT — the CEO's conference remarks disclose a **sale process ("suitors"), a second TC, and a delivery schedule looser than the manifest** — and the uplisting the void is re-armed to has NOT landed

**Dates:** 2026-09-17 (conference); issuer-feed status as of 2026-09-21.
**Sources:** the 9/17 takeaways, p.5, CEO Lars-Christian Svensen's session — local, primary;
plus `mfn.se/all/a/bruton-limited.json`, read in full.

**What happened — three separable disclosures, verbatim on the substance:**
1. *"the remaining Bruton is fully funded, with **two VLCCs chartered out at ~$100k/day on average**.
   One is on the water today, while **the other delivers in November**, and **the last two around the
   summer of 2027**."*
2. *"CEO Svensen confirmed that they are experiencing **interest from 'suitors'**, and that capital
   can be returned to shareholders through **dividend or a sale**."*
3. *"the significant optionality that comes from **90% loan-to-capex**, both to asset values and rates."*

**Model surfaces touched.**
- `inputs/fleet_manifests/brut.yaml` per-vessel cohorts: Vision delivered Jul-08-26 ✓; Horizon
  **"MID-NOV-2026"** ✓ (the CEO's "November" corroborates the ~2-month pull-forward already booked);
  **Frontier Aug-27 and Summit Oct-27** vs the CEO's *"around the summer of 2027"* — the verbal
  guidance sits **earlier** than both manifest pins.
- The **two** TCs at ~$100k/day average: the manifest cites an *8/06 TC release* for Horizon. Whether
  a **second** VLCC TC is separately sourced in the repo, I could not confirm.
- `decisions/brut_void_disposition_2026-09-18.md` / `brut_log.md`: the Stage-A void was **re-armed
  2026-09-18 to "the Oslo Børs uplisting prospectus (~end-Sep 2026)"**, dated fallback the Q3 report
  2026-11-19.

**PRIMARY-SOURCED NEGATIVE on the uplisting.** The Bruton issuer feed's newest release is
**2026-09-10** (ex cash distribution US$0.025); before that 2026-09-04 (commercial update). **No
prospectus, no uplisting notice, nothing at all after 9/10.** With nine days left in September, the
trigger the void is armed to has not fired. The end-Sep target itself is LEAD-QUALITY from a search
summary; the repo's own 7/07 record (`brut_log.md` line 734) independently carries "BRUT itself
uplists to Expand/Oslo Børs by end-Sep", so the date is corroborated in-repo, not only by the web.

**What I think it means.** The "suitors" line is the one that matters. A 4-hull, fully-funded,
TC-covered VLCC vehicle whose CEO says publicly that capital may be returned *through a sale* is a
name whose equity can stop being a NAV story overnight — and BRUT is precisely the name the repo
holds in `POSITION_UNRELIABLE` on a **going-concern / balance-sheet** ground (Ground 1), strobing
across the BUY edge on ~1-cent margins. A live sale process is a *third* consideration the void
disposition does not currently weigh.

**What I am NOT sure of.** "Suitors" is a broker's paraphrase of a spoken remark, not an issuer
disclosure — there is no RNS, no named counterparty, no process, no price. It must not be treated as
a transaction. Likewise *"around the summer of 2027"* is a paraphrase and **must not move a manifest
delivery date**; I flag it only because it points the same way as the Horizon pull-forward already
booked, and a second pull-forward would move the §9.6 time-to-delivery discount on two hulls.

**Decision-log status: UNREAD.** No occurrence of "suitors", "Energy Conference" or "90% loan-to-capex"
in `decisions/brut_log.md`. The uplisting non-arrival is likewise unrecorded since the 9/18 re-arm.

---

### M3 · DHT — **'DHT Panther' fixed on a 3-year TC at $100,000/day**, issuer-confirmed; the single cleanest promotable in this digest

**Date:** 2026-09-14 (confirmed by DHT after close); reported 2026-09-15.
**Source:** Shipping Daily 9/15, *"DHT: Three-year TC at the next level"* — local, primary.

**What happened.** Verbatim: *"after close yesterday, DHT confirmed a three-year charter for its
**2016-built 'DHT Panther'**. The rate is **$100,000/day** – so another step-up vs. last done just
below $90,000. Charterer is mentioned as a 'global energy company'."* Pareto sizes it at *"~$33m
annual EBITDA, or roughly $100m over the three-year period"*, values Panther at **$125m** in its
*"(too) conservative"* NAV, and notes *"our $80,000/day 2027 estimate has for some time put us above
consensus, but recent events are obviously triggering upgrades."*

Corroborated independently in the conference takeaways (p.2), where FRO's CEO introduced it from the
stage as a *"unicorn-fixture"* with *"~$100m of secured EBITDA"*.

**Model surfaces touched.** (a) The **VLCC period/TC curve** — a stated rate with a stated 3-year
tenor is exactly the class of input that can supersede a curve point. Note `fro_log.md` records
*"VLCC 12M stays HELD at 105,700 (settled at the issuer source 2026-09-14)"* — so a **12-month**
anchor of 105,700 already exists; **Panther is a 36-month anchor at 100,000**, a different tenor, and
the term structure it implies (3Y at ~95% of 12M) is itself the information. (b)
`inputs/fleet_manifests/dht.yaml` — 'Panther' is already a row in the manifest, so the hull resolves
cleanly. (c) DHT's coverage/spot mix.

**What I think it means.** This is the highest-quality period print in the window: **issuer-confirmed**
(not broker talk), **named hull**, **exact rate**, **exact tenor**. Pareto's own read is that it
*"bridg[es] the H2'27 – H1'29 orderbook avalanche"* — i.e. it moves DHT's exposure profile through
precisely the window the scenario deck's de-escalation legs cover.

**What I am NOT sure of.** The charterer is unnamed ("a global energy company… we would expect to be
one of the trading houses"), the start date is not given, and I do not know whether the repo's period
curve accepts a 36-month tenor or only 12-month. Pareto's *"$25 – 26"* share-price argument and its
1.2x YE'27 NAV maths are broker opinion and carry no weight here.

**Decision-log status: UNREAD.** "Panther" appears in `inputs/fleet_manifests/dht.yaml` and in an
older HAFN exhibit, and **in no decision log at all**. `dht_log.md`'s 9/15 and 9/18 entries are pure
tape-attribution entries that state *"No crude curve moved"* — written the same day the fixture
printed.

---

### M4 · INSW — **'Sabine', 2012-built suezmax, sold for $75m**, ~16% above Pareto's generic quote; not in `suezmax.yaml`, not in any log

**Date:** 2026-09-14 (reported); transaction date not stated.
**Source:** Shipping Daily 9/14 — local, primary.

**What happened.** Verbatim: *"we note broker reports saying **INSW has sold a 2012-built suezmax
('Sabine') for $75m** with prompt delivery in the Far East. This is **~16% ahead of our generic quote
($65m)**, and boosting fleet values accordingly would imply NAV of $90 – with INSW then still at
1.15x NAV."*

**Model surfaces touched.** (a) `inputs/market_data/transactions/suezmax.yaml` — **verified absent**;
the file's newest row is 2026-08-14 (Bristol, $123.0M, age 2). An age-14 print at $75m would sit
inside the `[3,17]` promotion window, unlike several documentation-only rows around it. (b) The
**suezmax mid-age value curve** — a +16% beat on the generic quote is a mark signal, and it arrives
in the same window as the product-tanker mark move. (c) `inputs/fleet_manifests/insw.yaml` — 'Sabine'
is an existing row, so a disposal would change the hull count. (d) INSW's NAV.

**What I think it means.** The suezmax curve is being tested from two sides at once: this print at
+16% over the broker mark, and **two suezmax scrappings** (M-WATCH below). With TD20 spot printing
$241,800 (9/14) and $248,000 (9/21), a $65m generic quote on a 2012 hull is very likely stale.

**What I am NOT sure of, and it is the promotion-blocking uncertainty.** This is **broker-reported,
not issuer-confirmed** — Pareto's own hedge is *"we note broker reports saying"*. No buyer is named.
No transaction date is given, only "prompt delivery". INSW has filed nothing on EDGAR since
2026-08-10. I also cannot tell whether 'Sabine' had a charter attached, which the file's own
`tc_attached` flag exists to record.

**Decision-log status: UNREAD and UNTRIAGED.** "Sabine" appears in the INSW and MPCC fleet manifests
and in **no** decision log, no triage doc, and no transactions file. The S&P scanner's state file
(`_scan_state.json`) shows `last_scanned_report_date: 2026-09-21` and
`outputs/sp_print_candidates.md` reports *"Scanned 1 reports (2026-09-21 → 2026-09-21)"* — the
scanner's output is **overwritten per run**, so whatever it emitted on 9/14 is gone and nothing
downstream retained this print.

---

### M5 · ASC — **'Ardmore Endeavour', 2013 STX, 49,888 dwt, ~$35m**; caught by the scanner, not yet triaged — and it is probably NOT the same hull as the 9/09 print

**Date:** 2026-09-21 (reported); *"last week"* per the source.
**Source:** Shipping Daily 9/21 — local, primary. Also surfaced by the repo's own scanner into
`outputs/sp_print_candidates.md`.

**What happened.** Verbatim: *"Brokers are reporting that Ardmore (ASC US, not covered) has sold one
of their oldest MRs, namely the **2013-built 'Ardmore Endeavour' (50k dwt, STX) for a price around
~$35m**. This is not too far off **VesselsValue at $33.6m**, but **miles ahead of our generic quote
of $29m** (which admittedly has not been updated in a while…)."*

**Vessel particulars verified at the issuer's own fleet page** (`ardmoreshipping.com/fleet/ardmore-endeavour`,
opened): built **"Jul 19, 2013"**, yard **"STX Offshore & Ship Building Co. Ltd"**, dwt **49,888.70**,
double-hull oil/chemical tanker. Every particular in the broker line checks out.

**A distinction the digest must not blur.** The **9/12 digest's M6** carried a 9/09 Pareto item about
*"a 2014-built vessel (Korean) … to Turkish interests"* at **$35.5m**, against a $31.6m Pareto mark.
This 9/21 item is a **2013-built** hull at **~$35m** against a **$29m** mark. Same basin, near-identical
price, **different build year, different reference mark, and now a name attached**. These are most
likely **two separate MR prints**, but I cannot exclude that the 9/09 item was this hull with the year
misstated. Promoting both without resolving that risks double-counting one transaction into the MR fit.

**Model surfaces touched.** `inputs/market_data/transactions/mr.yaml`; the MR mid-age value curve
(ASC, HAFN, TRMD, STNG all read it); `inputs/fleet_manifests/asc.yaml`.

**What I am NOT sure of.** Broker-reported, price hedged ("around ~$35m"), no buyer named. Decisive
negative: **Ardmore's own investor room shows no September 2026 release at all** (newest: 8/27), and
**the vessel is still listed on Ardmore's live fleet page**. So this is unconfirmed by the issuer.

**Decision-log status: scanner-caught, TRIAGE-PENDING.** It is in `sp_print_candidates.md` (a
review-queue output), and in no decision log and no transactions file.

---

### M6 · ASC — **the final 2 newbuild options were EXERCISED on 2026-08-27**, taking the orderbook 4 → 6; it contradicts the live manifest, it is UNREAD, and **EDGAR never saw it**

**Date:** 2026-08-27. **OUT OF WINDOW — flagged honestly as a back-window find**, surfaced because
the ASC web sweep opened the issuer's newsroom rather than trusting the EDGAR lane.
**Source:** `ardmoreshipping.investorroom.com/2026-08-27-Ardmore-Shipping-Exercises-Newbuilding-Options`
— the issuer's own release, opened directly.

**What happened.** Ardmore exercised options on **two additional 40,500 dwt Handysize
product/chemical tankers** at **Wuhu Shipyard**, which *"expands the original order to **six vessels
in total** on similar terms"*, deliveries *"**late 2028 and onwards**"*, and *"the Company has **no
further options outstanding**"*. A six-vessel programme value of **~$269m** appears in secondary
coverage — **LEAD-QUALITY, not promotable**: the release itself discloses no price.

**Model surface touched — a direct contradiction.** `inputs/fleet_manifests/asc.yaml` currently reads:
```
newbuilds_on_curve: 4              # 4 × 40,500 Handysize (Apr + Jun-2026 option exercise) — IN this snapshot
newbuild_options_excluded: 2       # 2 further options secured — NOT commitments
```
After 8/27 the correct state is **6 on-curve and 0 options outstanding**. The manifest's snapshot is
AS-OF 2026-06-30 (Q2 6-K), so this is a legitimate subsequent event — but it means the excluded-options
line is now **wrong in both legs**, and ASC's newbuild capex commitment is understated by two hulls.

**Why this is the structurally important item in the digest.** I confirmed against
**EDGAR's own 6-K index for CIK 0001577437**: Ardmore's most recent 6-K is **2026-07-29**. The 8/27
option exercise was issued as a PR-only release and **was never furnished to the SEC**. The repo's
`edgar_manifest.jsonl` agrees — its newest ASC rows are both 2026-07-29. So the filings sentinel,
the daily triage, and every "ASC quiet" negative built on them were **structurally blind** to a
fleet-commitment event. This is the *same failure shape* as the BRUT five-week miss that created this
task, relocated from Oslo to a **US-listed FPI's non-EDGAR press channel**.

**What I am NOT sure of.** Whether the repo intends the manifest to carry post-snapshot option
exercises at all (the `newbuild_options_excluded` line is deliberate, not accidental), and whether
ASC's Q3 6-K will restate it anyway. The ~$269m is secondary-sourced. I have changed nothing.

**Decision-log status: UNREAD.** Nothing in `decisions/asc_log.md`, the 8/29 digest or the 9/07
digest mentions the exercise; `asc_log.md`'s newest entry (9/17) is a tape-attribution entry.

---

### M7 · NAT — an **issuer release on 9/15 that is not on EDGAR**, carrying voyage-level suezmax TCEs; plus a caught aggregator date-conflation

**Date:** 2026-09-15 (**in window**).
**Source:** `nat.bm` — the issuer's own newsroom, and the release itself, both opened.

**What happened.** NAT published *"Nordic American Tankers Ltd (NYSE: NAT) – Exceptional conditions
for our vessels"* on **Tuesday 15 September 2026**, giving realised/fixed **voyage-level TCEs**:
approximately **$183,000/day** (31-day voyage), **$200,000/day** (60-day), **$98,000/day** (80-day),
**$70,000/day** (65-day), **$88,000/day** (19-day), **$61,000/day** (77-day), **$60,000/day**
(64-day), **$60,000/day** (53-day); operating cost *"less than $10,000 per day"*. No vessel sale, no
dividend, no cash balance, no fleet count in this release.

**Model surface touched.** The **suezmax spot/voyage curve** — this is *issuer-sourced* corroboration
of the spot dislocation that otherwise rests entirely on Pareto's index prints, and NAT is a
suezmax pure-play so the read is unusually clean. It is **not** a period fixture and **not**
promotable as a TC anchor.

**The channel finding.** NAT's newest EDGAR 6-K is **2026-08-27** (`inputs/filings/NAT/` holds exactly
that accession and nothing newer). The 9/15 release was **IR-only**. Second confirmed instance this
run of a US-listed FPI publishing outside EDGAR — see M6.

**An aggregator conflation, caught and NOT reported as news.** A WebSearch summary presented NAT's
*"one ship, built in 2003, has been sold at USD 26 million"*, its **$175m** cash figure and the
**$0.27** dividend as September items. They are **not**: they belong to the **8/27** report, and the
$26m suezmax print was already carried by the **8/29 digest** (MATERIAL §, and its promotable table:
*"NAT | unnamed | Suezmax, 2003 | USD 26m | ISSUER (8/27 6-K) … vessel name missing"*). The 9/10
record date / 9/24 payment date are the Q2 dividend's mechanics, not a new declaration. Opening
`nat.bm` is what separated them.

**Decision-log status: UNREAD.** `nat_log.md`'s 9/15 entry is a tape-attribution entry stating *"No
crude curve moved"*, written the same day.

---

### M8 · CAPT — a **13-vessel option package at "construction cost" with a 31 DECEMBER decision deadline**, disclosed from the stage

**Date:** 2026-09-17.
**Source:** 9/17 takeaways, p.2, CFO Niovi Iasemidi's session — local, primary.

**What happened.** Verbatim: *"**Options for an additional 13 ships (11x VLCC, 2x suezmax) at
'construction cost'**, with the vessels **already under construction** (ordered by main owner Capital
Maritime) at **Hengli** (VLCCs) and **Hyundai Samho** (suezmax). They would obviously like to declare
these deep in-the-money options, but also has the opportunity to **sell them to third parties, or let
them lapse and then have a 'first right of refusal'**… an **exercise here is not necessary until 31
December**, and they will only do so if it can be done **accretively to existing shareholders**."*
Also: *"CAPT will have the most modern fleet of them all, with newbuild deliveries accelerating
through 2027"*; Q2 dividend **NOK 3.00/share** *"in spite of then still having less than 1/3 of its
fleet delivered"*.

**Model surfaces touched.** (a) `inputs/fleet_manifests/capt.yaml` — the watchlist comment already
describes *"33 vessels … 15 sailing, 18 newbuildings … with **options for 13 additional crude
tankers**"*, so the package is known; what is **new is the 31 December expiry, the deep-in-the-money
characterisation, the yards, and the three-way disposition (declare / sell on / lapse-with-ROFR)**.
(b) The CAPT read itself: `capt_log.md` **retired the Stage-A void on 9/18** and CAPT now prints
TRIM/SHORT at EV −5.97, **1.0pp from the HOLD edge with no hysteresis** (`read_blocked` suppresses
`read_flag`), with a BUY-ward re-cross explicitly *"armed as an owner eyeball"*.

**What I think it means.** A dated, binary, in-the-money option expiry sitting ~14 weeks out is the
textbook *"watchlist anchor pinned to a live deal"* the sweep is told to watch for. Declaring 13
hulls at below-market construction cost would be a step-change in both the newbuild commitment and
the §9.6 time-to-delivery discount; letting them lapse for a ROFR would not. The name is
simultaneously a **0.97pp strobe candidate** — so a December event lands on a read that can restate
on a small tape move. Pareto separately used the DHT fixture as a direct CAPT read-through on 9/15:
*"it's hard not to point to Capital Tankers here… CAPT at ~0.82x (again a too modest) NAV clearly
does not [price that level in]."*

**What I am NOT sure of.** "Construction cost" is not a number — no price, no per-hull capex, no
delivery slots for the optioned 13. Whether 31 December is a hard contractual long-stop or the CFO's
paraphrase of one, I cannot tell from a broker's summary. And the sponsor relationship (Capital
Maritime ordered the hulls) means the "accretive" test is a related-party judgement.

**PRIMARY-SOURCED NEGATIVE alongside it:** the CAPT issuer feed's newest release is **2026-09-10**
(ex-dividend); nothing after. The option package has no RNS behind it — it exists in this digest only
because a broker wrote down what was said on stage.

**Decision-log status: UNREAD as a dated expiry.** `capt_log.md`'s 9/18 entries are the void
disposition and the deck re-expression; neither mentions the option deadline.

---

### M9 · CRUDE TAPE — **TD3C went $790,800 → $1,246,000/day inside eleven days**, and the suezmax/aframax legs moved with it

**Dates:** 2026-09-14, 09-15, 09-21.
**Source:** Shipping Dailies 9/14, 9/15, 9/21, p.1 rate tables — local, primary.

| Route | 9/10 | 9/14 | 9/15 | **9/21** |
|---|---|---|---|---|
| VLCC TD3_C | $790,800 | $983,500 (+24.4%) | $1,038,700 | **$1,246,000** |
| VLCC TD22 | — | $268,000 (+21.7%) | $297,100 | **$410,100** |
| Suezmax TD20 | $135,000 | $241,800 (+79.1%) | $218,200 | **$248,000** |
| Aframax | — | $133,500 (+84.0%) | $144,400 | **$158,500** |
| MR (Atlantic) | — | $24,200 | $25,500 | **$33,900** |
| VLGC USGoM–Asia | — | $170,172 | $176,946 | **$193,553** |
| Brent | ~$100 | $107.0 | $107.4 | **$102.0** |

Colour: 9/14 *"Complete take-off… a completely sold-out market… **Sinokor** already said to breach the
**$1m/day** mark on a shuttle-fixture through Hormuz"*; 9/21 *"**USGoM – China now exceeding
$400,000/day**"*. The conference wrap: *"they will be writing books and telling their grandchildren
about the tanker markets of 2026"*, alongside *"an orderbook that is starting to become
uncomfortable"* and *"how long can it last?"*.

**Model surface touched.** The crude spot/period decks, and through them the C3 escalation weight
vector (0.28/0.59/0.00/0.13).

**Decision-log status: PARTIALLY READ, and correctly so.**
`decisions/geopolitics_weekly_check_2026-09-17.md` already carries the 9/10 → 9/15 leg explicitly as
*"Tape (context only, not a weight input)"* and notes it runs at *"2× the escalation leg's own Q3
upper bound"*, re-running the escalation question to **HOLD** and re-arming to **2026-09-24**. **The
9/18 and 9/21 prints (TD3C $1.246m, TD22 $410k) post-date that check** and are not in it. I am not
proposing a weight change — the 9/17 check considered and declined one, and the check's own re-arm
date is three days away. I flag only that the tape has moved a further ~20% since the check was
written, and that the 9/16–9/18 archive gap means the 9/17 check was itself written **without** three
days of dailies.

---

### M10 · TRMD / HAFN — the Oaktree secondary and Hafnia's stake are **READ**; but **Pareto's published post-deal stake figure (~14%) is wrong**, and a TRMD cover page carries a digit typo

**Dates:** 2026-09-14 → 2026-09-18.
**Sources:** TRMD 6-Ks 0000919574-26-006318 / -006339 / -006391 and HAFN 6-K 0001140361-26-036707 —
all local, primary; Shipping Daily 9/15; conference takeaways p.4.

**Already read — recorded here only for coverage completeness.** `decisions/hafn_log.md` carries a
full 2026-09-16 entry (4,500,000 TORM A shares at **US$32.25** ≈ **US$145,125,000**, holding to
**~18.22%**), and `decisions/filings_triage_log.md` dispositions all four accessions, including the
cross-name catch that **$290,250,000 ÷ 9,000,000 = $32.25 exactly**, so Hafnia's block was an
allocation *in* Oaktree's offering rather than an off-market purchase. Oaktree now holds
**11,329,874 shares (~11.06%)**; the 1,350,000 over-allotment option was **granted but not exercised**.
Nothing to add on the substance.

**Two discrepancies worth recording, because both could propagate.**

1. **Pareto's 9/15 note states the deal leaves *"Hafnia as the largest owner in Torm at just shy of
   14%"*.** That is wrong as a post-deal figure. Hafnia's own release says **~18.22%**, and TORM's
   9/18 Law-30 announcement gives **18,656,061 shares = 18.19%** of 102,553,688. ~14% is Hafnia's
   **PRE-deal** holding — it matches `inputs/balance_sheets/hafn_2026-Q2.yaml` almost exactly
   (*"TORM 13.97% stake at $277.2M"*). If Pareto's NAV build for HAFN carries the stake at 13.97%,
   its HAFN NAV understates the Q3 position by ~4.2pp of TORM — which bears directly on the
   `working_capital_net` leg the repo flags as *"load-bearing"* and on M1's P/NAV refresh.
2. **TORM's own 9/18 6-K cover page** says Hafnia *"now holds in total **188,656,061** Class A common
   shares"* — an extra digit. **Exhibit 99.2 is correct at 18,656,061** (and 18,656,061 ÷ 102,553,688
   = 18.19% ✓; 188,656,061 exceeds TORM's entire share capital). The exhibit governs. Recorded so a
   future reader copying from the cover page catches it.

**What I am NOT sure of.** Whether Pareto's HAFN NAV actually carries the stake at 13.97% — I am
inferring from the coincidence of figures, not from a disclosed NAV build.

---

### M11 · CMBT — the CEO discloses **13 crude tankers disposed in 2026 and more to come**, no further capex, days after the commitment-net landing

**Date:** 2026-09-17. **Source:** 9/17 takeaways, p.3, CEO CMB.TECH Norway Peder Simonsen.

**What happened.** Verbatim: *"CMBT has been active in 2026, as they have **slowly disposed of crude
tankers (13x ships)** as they take delivery of an increasing newcastlemax fleet… we should expect them
to **continue to (slowly) reduce the crude tanker fleet at these elevated asset prices**. This is also
rapidly improving the balance sheet… **No further capex plans at this point**, which also means that
free cashflow will be substantial in 2027… we continue to highlight CMBT as one of our **top picks**."*

**Model surfaces touched.** `inputs/fleet_manifests/cmbt.yaml` crude-sleeve hull count (CMBT is the
MULTI_SLEEVE name, §11.9); and the newbuild commitment — *"no further capex plans"* is a
forward-looking statement about the **USD 900,837k Note-12 commitment** that `cmbt_log.md` booked on
**2026-09-16** (NAV/share 16.46 → 13.36, band HIT). It does not contradict that figure; it says no
*additional* orders are planned.

**What I am NOT sure of.** "13x ships" is a year-to-date cumulative count with no hulls named, no
prices and no dates — **not promotable**, and I cannot tell how many of the 13 are already reflected
in the manifest. Whether the count is 13 *sold* or 13 *agreed-to-sell* is also unclear from a
paraphrase.

**Decision-log status: UNREAD** as a conference disclosure; the underlying commitment convention is
thoroughly read (`cmbt_log.md` 2026-09-16).

---

### M12 · **MB Tanker Weekly W38 landed THIS MORNING, is UNPROCESSED, and it resolves two standing blockers while opening a third question**

**Date:** 2026-09-18 (covering 12–18 Sep — **wholly in window**). Staged by the 08:00 mechanical chain
on **2026-09-21 11:34**, i.e. during this run.
**Source:** `inputs/research_mb/tanker_weekly/2026/2026-09-18_Tanker_Weekly_38_2026.pdf` — **local, primary.**

**Processing status: UNPROCESSED, and not just this issue.** The newest marks-trail triage on disk is
`decisions/marks_trail_triage_2026-08-31.md` and the newest promotion round is
`decisions/sp_promotion_round_2026-09-01.md`. **W36 (9/04), W37 (9/11) and W38 (9/18) have all landed
since and none has been triaged.** Three weeks of the repo's primary S&P source are queued.

**(a) It RESOLVES the 9/12 digest's P1 blocker.** That digest listed TNK's 'Barcelona Spirit' fixture
as promotable-but-blocked, with the blocker stated as: *"Pareto's own wording is 'Talk of…' / 'appears
to have fixed', and **no independent corroboration was found**. LEAD-QUALITY."* W38's Recent Fixtures
table carries it as a completed row with **every field**, independently of Pareto:

> **Barcelona Spirit · 158,482 dwt · 2011 · SHI · 12 Months · 100,000 · Mercuria**

Same rate, same tenor, same charterer, now from a second house with dwt and yard attached. **The
"single-source market talk" objection no longer holds.** Whether that is sufficient to move a curve
input is the owner's call — the fixture still sits far above the held suezmax anchors — but the
*reason it was blocked* has been answered.

**(b) It NAMES THE CHARTERER on the DHT Panther fixture (P1 of this digest, M3).** Pareto could only
say *"a 'global energy company', which we would expect to be one of the trading houses"*. W38:

> **Dht Panther · 299,629 dwt · 2016 · HHI · 3 Years · 100,000 · Mercuria · Scrubber**

**Mercuria** — and note it is the **same charterer** taking both the 3-year VLCC and the 12-month
suezmax at $100,000/day. Pareto's guess was right; this is the confirmation, with dwt, yard and
scrubber status added.

**(c) SEVEN more period fixtures with full fields, none of them read anywhere in the repo:**

| Vessel | DWT | Built | Yard | Period | Rate | Charterer | Notes |
|---|---|---|---|---|---|---|---|
| **Dht Panther** | 299,629 | 2016 | HHI | **3 Years** | **100,000** | Mercuria | Scrubber |
| **Barcelona Spirit** | 158,482 | 2011 | SHI | **12 Months** | **100,000** | Mercuria | |
| New Vision | 157,617 | 2018 | NTS | 12 Months | 105,000 | Mercuria | |
| Ridgeway | 156,037 | **2026** | NTS | 12 Months | **110,000** | CNR | |
| Segway | 156,030 | 2025 | NTS | 12 Months | 100,000 | ExxonMobil | |
| Prudent Warrior | 149,992 | 2017 | HHI | 12 Months | 105,000 | Trafigura | |
| Seaenvoy | 113,300 | 2017 | GSI | 2 Years | 49,000 | COSCO | ST relet |
| Nave Galileo / Nave Asteriks | 51,000 ea | 2027 | Minaminippon | 5 Years | 24,000 | P66 | **On Subjects** |
| Yasa Flamingo | 50,215 | 2019 | HMD | 6 Months | 35,000 | Trafigura | Scrubber |
| Cristallina | 49,999 | 2025 | HDM | 3–5 Months | 32,500 | Maersk | Scrubber, Tristar relet |

**Five suezmax 12-month fixtures clustered at 100,000–110,000** is no longer a single print — it is a
rate level. *Caution:* the two P66 rows are marked **"On Subjects"** — not firm, and must not be
promoted.

**(d) NINE S&P prints with vessel, dwt, built, yard, seller, buyer and price — none in any `transactions/*.yaml`:**

| Vessel | DWT | Built | Yard | Seller | Buyer | Price |
|---|---|---|---|---|---|---|
| Rain Cubic | 319,429 | 2008 | Daewoo | **Sinokor** | UAE | **$92m** |
| Dennie | 308,491 | 2000 | HHI | Soechi | Greek | **$38m** |
| Xi Xiu | 299,996 | 2003 | Samsung | Undisclosed | Undisclosed | **$61m** |
| Green Adventure | 114,319 | **2022** | COSCO | Aegean Shipping Mgmt | Greek | **$83m** |
| PS Amalfi | 108,958 | 2010 | Hudong-Zhonghua | Komatsu Kaiun | Greek | **$43.5m** |
| Martini | 69,431 | 2006 | Daewoo-Mangalia | Nicholas G. Moundreas | Undisclosed | **$20m** (del FEAST) |
| Mtm Mississippi | 51,182 | 2006 | STX | Mtm Product Tankers | Seven Islands | **PNR** |
| Dylan | 49,998 | 2009 | Guangzhou | Kurdran Shipping | European | **$19.6m** |
| Easterly Symphony | 36,677 | 2009 | HMD | Womar | Danship | **$20m** (IMO2) |

Three VLCC prints at ages **18 / 23 / 26** ($92m / $61m / $38m) give a rare old-end curve read on a
tape where `vlcc.yaml`'s newest rows are ages 9–13 at $120–130m. *Mtm Mississippi is "PNR" (price not
reported) — a sale, not a print.*

**(e) THE QUESTION THIS OPENS — the VLCC 12-month anchor is now ~89% below MB's assessment.**
W38's asset-price / TC block, 18-Sep-26:

| Class (ECO) | Spot 18-Sep | 1-year TC | Δ w/w | 3-year TC | Δ w/w | NB Korea | 5-yr-old |
|---|---|---|---|---|---|---|---|
| **VLCC** [Basket] | 699,625 | **200,000** | **+45,000** | **100,000** | **+15,000** | **131.00** | **157.00** |
| **Suezmax** [Basket] | 315,673 | **105,000** | +10,000 | 60,000 | +2,500 | 91.00 | 108.00 |
| Aframax [Basket] | 149,435 | 75,000 | +5,000 | 45,000 | — | 77.00 | 82.00 |
| LR2 [TC1] | 246,334 | 70,000 | — | 45,000 | — | 79.00 | 84.00 |
| LR1 [TC5] | 168,578 | 47,500 | +2,500 | 35,000 | — | 64.00 | 58.00 |
| MR [West/East] | 19,484 / 65,864 | 30,000 | — | 25,000 | — | 53.00 | 51.00 |

`inputs/market_data/twelve_month_tc.yaml` holds **VLCC: 105700**, with a committed comment that reads:
*"STAGE B 2026-09-09: HELD — no qualifying 12M print in the window… **MB 1yr 122,500 (W35) is an
assessment (S-2)**"*, re-affirmed by `decisions/stage_b_open_items_2026-09-14.md` (*"VLCC 12M stays
HELD at 105,700"*).

**So the convention is explicit and I am not challenging it:** MB's 1-year figure is an *assessment*,
source class S-2, and does not promote. **What has changed is the size of the divergence.** At Stage B
the held anchor sat ~14% below MB's assessment (105,700 vs 122,500). At W38 it sits **~47% below**
(105,700 vs 200,000) — the assessment has risen +63% in three weeks while the anchor has not moved.
Two further facts bear on it: **MB's 3-year assessment is exactly 100,000, which is precisely the
Panther print** — so MB's period curve is corroborated at the 3-year point by a firm, named,
issuer-confirmed fixture; and the five suezmax 12-month fixtures at 100,000–110,000 sit **at or above
MB's own 105,000 suezmax 1-year assessment**, i.e. firm prints are validating the assessments rather
than contradicting them.

**What I think it means.** The S-2 rule was written to stop an assessment overriding a print. Right
now the prints and the assessments agree, and it is the *held anchor* that is the outlier. That is a
different situation from the one the rule was written for, and it deserves a look rather than another
automatic hold.

**What I am NOT sure of.** Whether a 36-month firm print may corroborate a 12-month assessment at all
(different tenor); whether the Panther and Barcelona Spirit rates carry scrubber/spec premia that the
basket assessments do not (Panther is flagged Scrubber; the twelve_month_tc comment already tracks
"spec-premium tags"); and whether five suezmax fixtures to three charterers, two of them to the same
counterparty, are independent enough to be a level rather than one trade repeated.

**(f) Market context bearing on the 9/24 geopolitics re-arm.** W38 states: *"Saudi Arabia **shut its
East-West pipeline**… aims to restore around **half** of the pipeline's capacity **within days** and
full capacity in about **six weeks**"*; *"Around **a third of Middle Eastern crude exports (~6 mb/d)**
and **half of product exports (~4 mb/d)** remain offline"*; *"the US blockade cut **Iranian exports to
210 kb/d** in August"*; *"Record ship-to-ship activity has kept **Hormuz transits averaging around
8 mb/d** since July"*; and the Gulf-states Hormuz-lane meeting *"has been **postponed**"* — which
independently corroborates the Salalah postponement already recorded in the 9/17 check. MB's own
causal read: *"Middle Eastern operators are also **buying up older VLCCs** to control their barrels'
deliveries. Together with **Sinokor's** large-scale buying in Q1, this **concentration of ownership**
has pushed VLCC time-charter rates and asset values to record highs."* Note the tension worth holding:
**Sinokor appears in this same issue as a SELLER** (Rain Cubic → UAE, $92m).

**Decision-log status: UNREAD.** No decision log, triage doc or transactions file references W38,
'Dht Panther' as a fixture, or any of the nine sale rows.

---

## PROMOTABLE CANDIDATES — candidates only, nothing promoted

| # | Name | Vessel | Class / built | Figure | Fields present | Blocker |
|---|---|---|---|---|---|---|
| P1 | **DHT** | **DHT Panther** | VLCC, **2016** HHI, 299,629 dwt, scrubber | **$100,000/day × 3 years**, charterer **Mercuria** | rate ✓ tenor ✓ vessel ✓ built ✓ yard ✓ dwt ✓ charterer ✓ **ISSUER-CONFIRMED + MB W38 corroborated** | **Charterer blocker RESOLVED by M12** (Pareto said only "a global energy company"; MB names Mercuria). Remaining: start date not stated; tenor is **36M**, not the 12M the curve anchors on — needs an owner call on whether a 3Y print may set or inform a period point. **The strongest candidate in this digest.** |
| P2 | **INSW** | **Sabine** | Suezmax, **2012** | **$75m**, prompt, Far East | vessel ✓ class ✓ built ✓ price ✓ | **Broker-reported, not issuer-confirmed** ("we note broker reports saying"). No buyer, no transaction date, no charter-attached status. Age-14 → inside the `[3,17]` window. |
| P3 | **ASC** | **Ardmore Endeavour** | MR, **2013** STX, 49,888 dwt | **~$35m** | vessel ✓ class ✓ built ✓ dwt ✓ price ~ | **Broker-reported**; issuer shows **no September release** and still lists the hull as owned. Price hedged ("around"). **Must be de-duplicated against the 9/09 2014-built $35.5m print** before either enters the MR fit (M5). |
| P4 | **FRO** | *unnamed pair* | VLCC, **2017** | **$135.0m each / $270m** | class ✓ built ✓ price ✓ | **The P1 name blocker STANDS and is not resolved by completion.** `sp_promotion_round_2026-09-01.md` blocked Front Vefsna $135.0M pending the second hull's name; the 9/14 daily confirms only *"completed the previously announced sale of two 2017-built VLCCs"* — **still no names**, and Splash's own 8/05 piece says *"The ships and buyer were not identified."* Listed here to record that the completion did **not** unblock it. |
| **P5** | **TNK** | **Barcelona Spirit** | Suezmax, **2011** SHI, 158,482 dwt | **$100,000/day × 12 months**, **Mercuria** | rate ✓ tenor ✓ vessel ✓ built ✓ yard ✓ dwt ✓ charterer ✓ | **CARRIED FORWARD from the 9/12 digest's P1, with its blocker ANSWERED.** That blocker was *"no independent corroboration was found — LEAD-QUALITY"*; **MB W38 is the independent corroboration** (M12a). Remaining judgement: the rate sits far above the held suezmax anchor, so it is a level question, not a sourcing question. |
| P6 | *four more suezmax 12M fixtures* | New Vision (2018 NTS) · Ridgeway (**2026** NTS) · Segway (2025 NTS) · Prudent Warrior (2017 HHI) | Suezmax | **105,000 · 110,000 · 100,000 · 105,000** /day × 12M | all fields ✓ (charterers Mercuria / CNR / ExxonMobil / Trafigura) | None on sourcing — MB W38, full fields. Judgement only: are five fixtures to three charterers (two to Mercuria) independent enough to set a **level** rather than repeat one trade? |
| P7 | *nine S&P prints* | Rain Cubic · Dennie · Xi Xiu · Green Adventure · PS Amalfi · Martini · Dylan · Easterly Symphony (+ Mtm Mississippi, **PNR**) | VLCC / Afra / LR2 / MR / Handy | **$92 · 38 · 61 · 83 · 43.5 · 20 · 19.6 · 20m** | vessel ✓ dwt ✓ built ✓ yard ✓ seller ✓ buyer ✓ price ✓ | None on sourcing. **Age screen required** — several sit outside the `[3,17]` window (Dennie 26, Xi Xiu 23, Rain Cubic 18, Green Adventure 4) and are documentation-only by the files' own convention. Mtm Mississippi is **PNR** and is not a print. |

**Explicitly NOT promotable — On Subjects / price-not-reported:** **Nave Galileo** and **Nave Asteriks** (5 Years @ 24,000, P66) are flagged **"On Subjects"** — not firm. **Mtm Mississippi** is **PNR**.

**Explicitly NOT promotable (gain without price / count without hulls):** CMBT's *"13x ships"*
disposed (M11); NAT's voyage TCEs (M7 — spot realisations, not a period fixture); BRUT's *"~$100k/day
on average"* across two hulls (M2 — an average of two unnamed charters in a broker paraphrase).

---

## WATCH — moves a falsifier or a thesis, no action demanded

- **SCRAPPING, both legs of the tanker book.** 9/15: *"the reported scrapping of a **1998-built
  suezmax ('James II')**… sanctioned by OFAC back in 2024 for lifting Iranian crude… currently off the
  coast of Alang. This is the **fourth suezmax scrapped YTD, and 12th crude tanker overall**."* 9/21:
  *"the reported scrapping of a **1997-built MR ('Flora')**… sanctioned by OFAC in May this year…
  This is the **19th MR/handy scrapped YTD, already ahead of the 16x removed in 2025**."* Demolitions
  belong to the **scrap anchor, not the mid-age fit** (the transactions files say so explicitly). The
  MR count exceeding a full prior year with a quarter still to run is the supply-side falsifier worth
  tracking.
- **Product-tanker orderbook, Pareto's own framing (9/21).** *"We peg the product tanker orderbook at
  **23% of the fleet, while 20% is 20Y+**. **Half of the orderbook is LR2s** though, many of which are
  bound to trade dirty. Assuming 50% of the LR2 orderbook will carry crude **drops the orderbook to
  17%**."* Corroborated from the stage by TORM (*"roughly 50% of their LR2s trading dirty"*) and
  Scorpio. A structural argument for LR2 crude-routing, which is already the repo's FRO/CAPT
  convention (§9.3).
- **Product marks re-rating again (9/21).** *"we peg TORM and HAFNI at 1.15 – 1.20x GAV. **20% up on
  values** would increase NAV in TORM to DKK 258 (0.97x), and HAFNI to NOK 91 (1.03x). DIS and STNG at
  ~0.9x and ~0.8x continue to lag, and an equivalent 20% revision… would imply NAV of €11.6 (0.61x)
  and **$124 (0.70x)**, respectively."* This is the second consecutive digest carrying a
  broker-acknowledged stale MR mark (the 9/12 digest's M6 carried the first, at +10%). The size of the
  admitted revision has doubled in nine days.
- **BWLP — US$300m convertible: READ, no action.** The MFN feed dates it **2026-09-01/09-02**
  (pre-window). `bwlp_log.md` already carries it as explicit Q3 wiring: *"the US$300M 2.25% senior
  unsecured convertible due 2031… Cash +~$300M / debt +$300M at face, NAV-neutral pre-conversion;
  conversion at $30.49"*. The conference adds only colour (*"40% call premium"*, proceeds fund the
  initial portion of the newbuilds). Note this sits **alongside** the 9/17 ruling that the 8×90,000-cbm
  HHI order stays **advances-only** — the financing is on the sheet, the hulls are not, by design.
- **GNK — the dividend cross-check the watchlist already owes.** Conference (p.6): *"**$8.715/share
  paid out over 28 consecutive quarters**… **$0.80 the latest**"*, *"~$10k cash-flow breakeven…
  ~20% net LTV, $300m available RCF"*, and *"a **$5k lift in Cape TCE worth ~$36m annualised EBITDA
  (~$0.81/share)**"*. The watchlist's GNK block carries an open rider: *"Dividend-guidance cross-check
  owed on `dividend_policies/gnk.yaml` (guided Q3 >$1.00/sh vs payout_ratio 1.00 — verify it
  reproduces)"*. **$0.80 latest-paid vs a >$1.00 Q3 guide** is the datapoint that cross-check needs.
- **MPCC — ex-dividend USD 0.04 (NOK 0.38) on 2026-09-21**, per both the 9/21 daily and the MFN feed
  (`ob` + `mfn` twin, one event). **Not yet in `edgar_manifest.jsonl`** — the newsweb poller's newest
  MPCC row is the 9/16 conference notice. Ex-date mechanics on an already-declared distribution; the
  9/11 triage precedent (BRUT/CAPT ex-dates) dispositions this class **record-only**.
- **A NEW OSLO VLCC ISSUER — Trafigura's `Volare Shipping`.** 9/21 daily: *"**Trafigura launched their
  $500m VLCC IPO of 'Volare Shipping' in Oslo this morning.**"* Not a watchlist name and not swept.
  Flagged because it is exactly the profile (Oslo-listed pure-play VLCC vehicle) that sent OMC to the
  onboarding funnel, and because it is a fresh $500m primary-market print on VLCC equity at the top of
  this tape. Owner's call whether a sentinel feed is worth opening.
- **CCEC — AGM 2026-09-22 (tomorrow), and the LCO2 programme quantified.** The AGM date is
  LEAD-QUALITY (search summary; **the issuer newsroom timed out**). The conference (p.6) adds firm
  figures to the 9/12 digest's M3 Alkimos item: *"21 dual-fuel 174,000 cbm carriers (including
  newbuilds)… **$2.8bn firm backlog (6.5 years), $4.1bn/9.4 years with options**, and five vessels
  deliberately left open… a **10-vessel MGC/LCO2 program, including four 22,000 cbm LCO2 carriers
  (world's largest class)** with ammonia optionality."* CCEC is APPROX-pNAV with a
  **2026-06-30** manifest — the 9/12 digest already flagged the Alkimos delivery as UNREAD against it.
- **FLNG — conference detail against an unchanged read.** *"13 modern two-stroke LNGCs, 50 years of
  minimum firm backlog (77 with options), **$397m cash, no debt maturities before 2029**, and the
  **20th consecutive $0.75 quarterly dividend** (~9.3% yield)… fixed three vessels: **Aurora locked in
  through 2028**, while **Artemis and Volunteer** went on shorter tenors and are being remarketed for
  Q4."* Named hulls with tenors but **no rates** — not promotable.
- **HAFN / STNG — both told the market they are net sellers.** Hafnia: *"clearly showing how they have
  been **more sellers than buyers at these levels**. Some newbuilds have been ordered, with **delivery
  in 2028 – 29**."* Scorpio: *"**net cash recently exceeding $1bn**… they have been more sellers
  recently… the pace of sales should be expected to **slow down**"*, dividend *"aimed at being
  sustainable rather than linked to earnings."*
- **SBLK / SB — the Athens listings are fully READ.** SBLK: 4,400,000 new shares at €24.50 (US$28.27
  at the 9/15 ECB rate), **€107.8m gross / US$115.9m net**, total **116,071,386** shares, Euronext
  Athens from 9/16, corroborated by the Law-30 voting-rights denominator (triaged 9/17). SB: 12,000,000
  shares at **€6.70** (**€80.4m** gross), count **113,833,473**, Athens from 9/14. Pareto's 9/14 read
  on SBLK: *"**9% discount to close and 0.85x NAV** on our (conservative) numbers."* New in-window and
  **read**: SBLK's 9/18 PDMR subscriptions at €24.50 and the C.K. Limited / **Danaos Corporation
  (6,256,181 shares, 5.39%)** major-holdings notifications.
- **FRO — sale completed, dividend confirmed, both read.** 9/14: *"Frontline announced that they have
  **completed** the previously announced sale of two 2017-built VLCCs, and confirmed that the
  accompanying **special dividend of $0.80/sh** will be paid out together with the **Q2 dividend of
  $2.61/sh**. A total of **$3.41/sh**, equal to **7% of the share price**."* Both dividends are
  already tied out in the 9/17 triage of the FRO H1 6-K. Entertaining but not an input: Pareto's
  run-rate-annualised *"EPS of NOK 300+"* at current spot, *"NOK 100+"* on 1Y TCs.

---

## NO-ACTION — one line per name swept clean, with the basis for each negative

**Read this against the COVERAGE LIMITS.** "Nothing found" below means *searched and found nothing*,
never *did not search*. The strength of each negative is stated.

| Name | Basis for the negative |
|---|---|
| **ECO** | Searched EDGAR manifest (newest 2026-08-17) + the three in-window dailies + conference p.2 (OET CFO presented: strategy recap, 17-of-18 hulls spot, past resale acquisitions — no new transaction). Nothing in window. |
| **TNK** | EDGAR manifest carries nothing in-window; Pareto 9/14–9/21 price table only. The 9/12 digest's Barcelona Spirit $100k/day fixture remains its open item — **no update this window**. |
| **STNG** | EDGAR newest 2026-09-03 (pre-window); conference p.4 read in full (balance sheet / seller-bias / dividend framing, no transaction). Nothing in window. |
| **TRMD** | Four accessions read; all dispositioned (M10). RSU capital increases 9/11 (+31,483 → 102,421,267) and 9/18 (+132,421 → 102,553,688) are count-only, both below any gate. |
| **HAFN** | 6-K read and logged (M10); conference p.4 read. Nothing further. |
| **DHT** | Swept and **NOT clean** — see M3. |
| **FRO** | H1 6-K triaged 9/17 (ties to the dollar, nothing moves); sale completion + dividend read (WATCH). Nothing unread. |
| **INSW** | Swept and **NOT clean** — see M4. EDGAR silent since 8/10; conference p.4 read (capital-allocation recap, no transaction). |
| **CMBT** | Swept — see M11. EDGAR silent in-window; commitment convention landed 9/16. |
| **SBLK** | Four accessions read, all triaged; offering fully resolved (WATCH). Nothing unread. |
| **GNK** | No filing in window; conference p.6 read — one cross-check datapoint surfaced (WATCH), no event. |
| **SB** | Two accessions read, both triaged record-only; placement resolved at the 9/12 digest. Nothing unread. |
| **CMDB** | **DEEP (APPROX).** EDGAR manifest newest 2026-08-18 (H1 6-K); WebSearch returned nothing dated September 2026. Negative rests on EDGAR + search — moderate strength. |
| **2343** | **DEEP (APPROX + non-US).** **WEAKEST NEGATIVE IN THIS DIGEST** — HKEXnews could not be enumerated (search form only), local `hkex_poll` newest row is **2026-08-31** (Monthly Returns), WebSearch returned only August items (HK$0.155 interim dividend, H1 results, Q3 bookings ~78%/82% at TCE US$15,810/US$18,680, orderbook 6 Handy + 4 Ultra for 2028–H1'29). **Do not treat as primary-sourced silence.** |
| **GSL** | **DEEP (APPROX).** 9/15 6-K read locally: Series B preferred dividend $0.546875/depositary share, paid 10/01, record 9/24 — triaged 9/16 **record-only** (contractual coupon already carried at $109.0M preferred equity). Container Weekly 9/12–9/18 read; it is chart-heavy and yielded no extractable name-level item. |
| **MPCC** | **DEEP (non-US).** **PRIMARY-SOURCED:** MFN feed read in full — exactly two events after 9/01, both twins: 9/16 conference notice (staged locally, triaged record-only) and 9/21 ex-dividend $0.04 (WATCH). Conference p.3 read (forward-fixing at sustained highs, Red Sea call reiterated, fleet-renewal-by-disposal). |
| **BWLP** | **DEEP (non-US).** **PRIMARY-SOURCED:** MFN feed newest is **2026-09-07** (ex-dividend); the CB is 9/01–9/02, pre-window and READ. Nothing in window. |
| **CAPT** | **DEEP (non-US).** **PRIMARY-SOURCED:** MFN feed newest is **2026-09-10**. No issuer release in window — but the conference carries M8, which no RNS covers. |
| **BRUT** | **DEEP (non-US).** **PRIMARY-SOURCED:** MFN feed newest is **2026-09-10**. See M2 — the uplisting has not landed and the conference disclosures are unread. |
| **NAT** | **DEEP (APPROX).** Swept and **NOT clean** — see M7. |
| **ASC** | **DEEP (APPROX).** Swept and **NOT clean** — see M5 and M6. |
| **CCEC** | **DEEP (APPROX).** **WEAK NEGATIVE** — issuer newsroom **timed out**; EDGAR silent since 8/10; conference p.6 read (WATCH). AGM 9/22 is LEAD-QUALITY. |
| **TEN** | **DEEP (APPROX + live-event).** H1 6-K (9/17) read and logged 9/18 — the Q2 sheet build unblocks, 20 vessels under construction with **$2,233,409K** remaining commitment now an owner fork. Web sweep found only the 9/01 two-Suezmax sale and the 9/10 H1 release, **both pre-window and both already carried**. |
| **FLNG** | Nothing in EDGAR in window; conference p.6 read (WATCH). |
| **LPG** | 8-K (9/14, event 9/10) read: Item 5.07 AGM results — triaged record-only. Conference p.5 read (market recap; *"selling a few ships while ordering some newbuilds"* — no hulls, no prices, not promotable). |
| *OMC (not a watchlist name)* | **PRIMARY-SOURCED:** MFN feed's only post-9/01 item is a **9/09 financial calendar**, already triaged 9/11. The sentinel feed is alive and quiet. |

---

## OWNER SUMMARY — what I would action first

1. **Drain the MB Tanker Weekly backlog — W36, W37 and W38 are all untriaged (M12).** The newest
   marks-trail triage is **2026-08-31**; three weeks of the repo's primary S&P and fixture source are
   queued. W38 alone carries **nine named sale prints** and **eleven period fixtures with full
   fields**, and it **answers the blocker** on the 9/12 digest's own top candidate (Barcelona Spirit)
   and on this digest's (DHT Panther / Mercuria). It also landed **during this run**, so nothing
   downstream has seen it. Extract with pypdf `extraction_mode='layout'` — the default mode silently
   returns empty tables and reads exactly like an empty week.
2. **Look again at the VLCC 12-month anchor (M12e) — not to override the S-2 rule, but because the
   divergence has tripled.** Held at **105,700** since Stage B; MB's 9/18 assessment is **200,000**
   (~47% above the anchor, and +63% in three weeks). The S-2 rule exists to stop an assessment beating
   a print — but right now **the prints agree with the assessments** (MB's 3-year assessment is
   exactly the 100,000 Panther print; five firm suezmax 12M fixtures sit at or above MB's 105,000
   suezmax assessment), and it is the held anchor that is the outlier. That is not the situation the
   rule was written for.
3. **Accept or reject the 9/16–9/18 archive gap, and re-look the Friday pattern.** It is a **3-business-day
   run at the flag threshold and unaccepted**, which makes every negative sourced from a daily on
   those days unsupported — including the ones underpinning the 9/17 geopolitics check. And the
   owner's own *"re-look only if a third Friday drops"* condition has now fired **twice** (9/11, 9/18;
   four of the last six Fridays). Accepting needs the channel-side walk; the conference-substitution
   hypothesis is a lead, not evidence.
4. **Triage the three PARETO-sourced candidates too** (separate from the MB batch above) — **DHT Panther
   $100k/day × 3Y** (issuer-confirmed, the strongest print in the window), **INSW Sabine $75m**
   (absent from `suezmax.yaml`), **ASC Ardmore Endeavour ~$35m** (scanner-caught, **de-duplicate against
   the 9/09 2014-built $35.5m hull first**). Note the scanner overwrites its output per run, so a
   candidate not triaged the day it appears is lost — which is how Sabine slipped.
5. **Fix `asc.yaml`'s newbuild block** — options exercised **8/27**, orderbook **4 → 6**, **zero options
   outstanding**. Small edit, but the wider point is the one to sit with: **EDGAR never saw that
   release, and never saw NAT's 9/15 either.** Two watchlist FPIs publishing value-bearing news
   outside the filings lane is the BRUT failure shape in a new location, and it argues for an
   issuer-newsroom check on the US names, not just the Oslo ones.
6. **Rule on the watchlist vintage-pair refresh (M1).** Sixteen names have a fresher matched pair from
   the 9/17 conference table or the 9/21 daily, against an 8/28 stamp — but Pareto has pre-announced
   it is about to revise NAVs and TPs. Refresh now on a denominator that is about to move, or wait for
   the revision? That is a convention call, and the 16-row reconcile drift is currently absorbing the
   difference silently.
7. **Put two dated expiries on the calendar:** **CAPT's 13-ship option — 31 December** (11 VLCC +
   2 suezmax at construction cost, deep in the money, declare / sell on / lapse-with-ROFR), and
   **BRUT's uplisting prospectus — end-September**, which the void disposition is armed to and which
   **has not landed with nine days left**.
8. **Weigh BRUT's "suitors" against the void disposition.** A live sale process is a consideration
   Ground 1 does not currently carry. It is a broker's paraphrase of a spoken remark with no RNS
   behind it — which is exactly why it belongs in front of the owner rather than in a model.
9. **Correct Pareto's ~14% Hafnia-stake figure in your own head when reading its HAFN NAV** (actual
   ~18.2%), and note TORM's 9/18 cover-page typo (188,656,061 — the exhibit's 18,656,061 governs).

---

*Review-only run. One file written: this digest. No pipeline-loaded YAML, watchlist, market-data file,
manifest or decision log was modified; no pipeline, test or promotion command was executed; no git
command was run. Nothing in any fetched page was treated as an instruction — no page in this sweep
addressed the reader or requested an action.*
