# News digest — 2026-08-16

> **This file carries TWO runs of the same day.** The scheduled task fired twice: once
> finishing **04:15 PDT** (Run 1, window 08-13 → 08-16) and again at **19:10 PDT** (Run 2,
> window 08-16 04:15 → 08-16 19:15). **Run 2 is written below; Run 1 is preserved verbatim
> underneath it, unedited.** Run 2 did not overwrite Run 1 — an overwrite would have
> destroyed 33 KB of the only channel record for the 8/13–8/16 window.

---

# RUN 2 — 2026-08-16 19:10 PDT (02:10 UTC 08-17)

## Run header

- **Window swept:** **2026-08-16 04:15 → 2026-08-16 19:15 PDT** — the back half of one
  **Sunday**. Prior digest = this same file's Run 1, established by listing `outputs/`
  (`news_digest_2026-06-10 / 06-21 / 08-13 / 08-16` are the only four).
- **A 15-hour weekend window is near-worthless on its own, and I did not pretend otherwise.**
  The load-bearing work of this run is therefore (a) a **primary-source liveness check on the
  three ingest lanes**, which is now the strongest coverage claim any of these digests has been
  able to make, and (b) **closing or verifying Run 1's open items** rather than re-reporting them.
- **Names swept:** 25/25, the full `inputs/watchlist.yaml` roster — but see the depth note.
  DHT · ECO · FRO · INSW · TNK · NAT · FLNG · CCEC · STNG · HAFN · TRMD · ASC · TEN · CMDB ·
  SBLK · GNK · CAPT · MPCC · GSL · BRUT · CMBT · SB · LPG · BWLP · 2343.
- **Depth weighting.** DEEP on the four Oslo issuer feeds (BRUT, MPCC, CAPT, BWLP) read at
  `mfn.se` primary; DEEP on NAT (`nat.bm` primary) and FRO (open promotable P1); DEEP on
  GNK (live event). The remaining names were covered **by the local ingest lanes rather than
  by individual web searches** — see the coverage note, which is a genuine upgrade, not a shortcut.
- **Sources searched.** Primary: `mfn.se/all/a/{capital-tankers,bruton-limited,mpc-container-ships,
  bw-lpg}.json`, `nat.bm`, `frontlineplc.cy`, `shippingtelegraph.com`. Search sweeps over Genco/
  Diana, FRO S&P, and general mid-August tanker tape. Repo-side: `state/edgar_manifest.jsonl`,
  `state/{edgar_poll.log,edgar_poll.err,newsweb_poll.json,hkex_poll.json}`,
  `scripts/edgar_poll_cron.sh`, `src/crude_tanker_fv/{newsweb_poll.py,reconcile.py}`,
  `inputs/{watchlist,archive_gaps,data_sources}.yaml`, `inputs/research_pareto/2026/08/`,
  and the heads of `decisions/{gnk,capt,mpcc,brut}_log.md`.

### Coverage limits of THIS run

1. **The US lane is, for the first time, swept PRIMARY — and not by WebFetch.** All three SEC
   hosts refuse WebFetch: `sec.gov/cgi-bin/browse-edgar` and `efts.sec.gov` **403** (as Run 1
   recorded), and **`data.sec.gov/submissions/CIK…json` also returns `HTTP 403 Forbidden`** —
   tested this run, a new data point. So EDGAR cannot be enumerated by fetch from any host.
   **But it does not need to be.** `state/edgar_poll.log` shows the repo's own poller running
   **hourly and clean** through **18:20 today** — `polled 22 names: 0 new filing(s)` on every
   pass — and `state/edgar_manifest.jsonl` ends at **CMDB 8/14**. The US-listed "nothing found"
   below is therefore machine-verified against EDGAR itself, not inferred from search silence.
   **This retires Run 1's caveat** ("a low-profile 8-K/6-K … would not have been caught" / "I
   would not call this lane fully swept") **and re-points its owner item 5a**: the fix was never
   an EDGAR fetch route, it is *reading the local manifest first*. Recorded so no future run
   spends effort on the 403 again.
   - The `state/edgar_poll.err` tail carries a `URLError: [Errno 54] Connection reset by peer`
     traceback, but that file's mtime is **06:28**, older than every clean run in the log. It is
     a historical failure from this morning, **not** a current one. Saying so explicitly because
     a stale `.err` is exactly the kind of thing that reads as a live outage.
2. **HK lane likewise primary:** `state/hkex_poll.json` polled **00:20 UTC 08-17**, 0 new.
3. **Oslo lane primary at the issuer feed** (all four `mfn.se` slugs fetched directly this run),
   **but see M1 — the local Oslo poller has never actually carried an arrival.**
4. **Measured fetch failures this run** (fresh results, not copied):
   - `globenewswire.com` — **`timeout of 60000ms exceeded`** on the FRO 8/04 primary. **Third
     consecutive run** this domain has timed out. Treat it as reliably unavailable, not flaky.
   - `data.sec.gov` — **`HTTP 403 Forbidden`** (new).
   - `marinelog.com` — **`HTTP 403 Forbidden`** (new).
   - Fetched fine: all four `mfn.se` slugs, `nat.bm`, `frontlineplc.cy`, `shippingtelegraph.com`.
5. **Tool note, unchanged from Run 1:** `Glob`/`Grep` are absent from this session; read-only
   `Bash` (`ls`, `find`, `grep`, `head`, `cat`, `wc`) was used for repo enumeration, per the
   task file's standing allowance. No writes, no `git`, no project code executed.

### Archive gaps

- **`inputs/research_pareto/2026/08/` still ends 2026-08-13.** The Friday **2026-08-14** Shipping
  Daily remains absent — **1 missing business day**, under `limit_business_days: 3`, so check 8b
  will not fire. 8/15–8/16 are a weekend, so **no new business days accrued since Run 1**; this is
  unchanged, not worsening. Any "nothing found" in the *Pareto* lane for 8/14 stays **unsupported
  rather than absent**. If the 8/17 daily lands and 8/14 does not, that is the point to decide
  backfill-or-accept.
- **`inputs/archive_gaps.yaml` gained its fifth accepted entry today** (mtime 15:00, after Run 1):
  `pareto_research 2026-06-01..2026-06-03`, accepted on its **own** channel-side walk to 2026-05-27
  (5,004 messages), including the sender's contemporaneous 6/02 message that Pareto had not
  published that week. **That was the last deliberately-open gap.** The file's own closing note
  records why it was held open for three days rather than inheriting July's evidence — the
  standard of evidence held. Nothing for me to do here; recorded as closed.

---

## MATERIAL — needs an owner decision or a model-input change

### M1 · PROCESS — the missing NewsWeb issuer channel **was built today**, is **live**, and has **never carried an arrival**
**What happened.** `src/crude_tanker_fv/newsweb_poll.py` exists (**18,129 bytes, mtime 06:43
today** — i.e. written *after* Run 1 finished at 04:15), is wired into `scripts/edgar_poll_cron.sh`
line 78 as `cron_lane newsweb ./.venv/bin/python -m crude_tanker_fv.newsweb_poll`, and is polling
**hourly**: `state/newsweb_poll.json` shows `last_polled: 2026-08-17T01:20:06Z` across all four
slugs, and `edgar_poll.log` logs `polled 4 names: 0 new release(s), 0 doc(s) staged` on every pass.
`inputs/data_sources.yaml` now carries `mfn_slug:` keys for all four Oslo names, each marked
**VERIFIED 2026-08-16** and pinned in `tests/test_newsweb_poll.py`.
**This closes, in mechanism, the gap named as load-bearing in all three previous digests** — the
one the 8/13 audit proved was the real cause of the BRUT five-week miss.
**The catch, and it is the whole reason this is MATERIAL rather than a footnote.** Every slug in
`state/newsweb_poll.json` reads **`"bootstrapped": true`** with `seen_ids` seeded from the full
existing history. Consequently:
- **0** records with `source: "newsweb"` in `state/edgar_manifest.jsonl` (52 lines, all
  `edgar`/`hkexnews`; newest is CMDB **8/14**).
- **0** files matching `inputs/filings/*/newsweb_*` — I checked by `find`, not by inference.

That is **correct bootstrap behaviour** (seed the seen-set, don't re-stage history). It is also
exactly the state in which a new watchdog looks green and has proven nothing: **no release has
ever travelled this channel end-to-end.** The task file already instructs future runs to "READ THE
LOCAL ISSUER CHANNEL FIRST … they are primary text, already local" — today that instruction would
have returned an empty directory, and a run that trusted it *instead of* fetching `mfn.se` would
have swept the Oslo lane with nothing at all.
**Model surface.** None directly — this is the sweep's own plumbing. But it governs whether the
next Oslo release is read on the day or five weeks late, which is the failure this task exists for.
**What I think it means.** The **first live test is dated and close**: MPCC Q2 **8/26**, BWLP
**8/28**, CAPT half-year **9/01**, plus the BRUT demerger completion **by end-August**. If a
`newsweb_*` file and a `source: "newsweb"` manifest line do not appear within hours of MPCC's
8/26 release, the channel is built but not working, and the 8/29 sweep must go back to fetching
`mfn.se` directly. Until one arrival lands, **`mfn.se` remains the Oslo lane of record and the
next sweep should still fetch all four feeds**, not substitute the local channel for them.
**What I am NOT sure of.** Whether the bootstrap watermark is set such that a release published
*between* the 06:43 bootstrap and the first arrival could fall into the seen-set unstaged; I did
not read the poller's watermark logic, only its state file. The HKEX poller's state carries an
explicit `"watermark": "2026-06-30"` field and the NewsWeb state, as far as the head I read shows,
does not — that asymmetry may be nothing or may be the gap. Worth an owner eyeball before 8/26.
**Status.** Not referenced in any decision log — it is infrastructure, not a name. **UNREAD** in
the sense that no digest has yet recorded the channel exists.

### M2 · MPCC — Run 1's derived post-issue share count is now **confirmed at the issuer primary**
**What happened.** Run 1 derived a post-placement count of **488,070,306 shares** from
443,700,279 + 44,370,027, and flagged it as *its own arithmetic*. The issuer's **2026-07-02 07:52**
release, "MPC Container Ships ASA: Registration of share capital increase," states the registered
share capital is **NOK 488,070,306** — read directly off the `mfn.se` feed this run.
**Two further releases surfaced that Run 1 did not report**, both **2026-07-01**, both flagging
notices confirming the dilution from the other side: **MPC Capital AG-affiliated holdings fell
20.12% → 18.29%**, and **Folketrygdfondet acquired 10.2m shares for a 5.6% stake**.
**Source.** `mfn.se/all/a/mpc-container-ships.json`, primary feed.
**Model surface.** `inputs/balance_sheets/mpcc_2026-Q1.yaml` →
`diluted_shares_outstanding: 443,700,279`. The denominator Run 1 flagged as stale is now
**primary-sourced rather than derived**, which is the difference between a lead and an input.
**What I think it means.** The 20.12% → 18.29% dilution of MPC Capital cross-foots independently:
a holder diluted by that ratio implies a share count increase of ~10.0%, matching the placement
exactly. Three independent legs (issuer share capital, two flagging notices, Run 1's arithmetic)
now agree on 488,070,306. Run 1's accretion estimate (~+1.6% NAV/share) rested on that count and
survives unchanged.
**What I am NOT sure of.** That NOK 488,070,306 of share *capital* equals 488,070,306 *shares*
requires a **NOK 1.00 par value**, which I inferred from the exact numeric match rather than read
in the release. It is a strong inference — the coincidence is otherwise absurd — but it is an
inference, and it is the one thing an owner should confirm before the count is typed anywhere.
**Status.** `decisions/mpcc_log.md` head is the **8/16 20:06 UTC** auto-run (price $2.72); still
**no reference to the placement**. **UNREAD**, now eight weeks.

### M3 · BRUT — the AGM approved a **$226,039,548 share premium account reduction**, unreported until now
**What happened.** The **2026-08-12 17:15** AGM-results release records shareholder approval of
board composition, amended bye-laws, auditor reappointment, **and a reduction of the share premium
account of $226,039,548**. Run 1 read this release and reported it only as "AGM results."
**Source.** `mfn.se/all/a/bruton-limited.json`, primary feed.
**Model surface.** `inputs/balance_sheets/brut` — the equity block. A share-premium reduction is
customarily a Bermuda-law step to **create distributable reserves**, which is a **dividend-capacity**
change, and BRUT's forward dividend strip is half of what this tool values.
**What I think it means.** For a pre-operational VLCC vehicle that has just reported **H1 net
income of $0.3m** and is about to demerge, converting a quarter-billion of share premium into
distributable reserves is a *preparatory* act — most plausibly for the **demerger** (distributing
the 8-ship spin to shareholders needs distributable reserves) rather than for a cash dividend.
That reading makes it a **structural** item, not a payout signal, and it lines up with the
end-August demerger completion already on the watch list.
**What I am NOT sure of — and this is a real limit.** I have the *amount* and the *approval*, from
a feed summary. I have **not** read the release body or the AGM notice, so I do not know the stated
**purpose**, whether it is conditional on court or shareholder confirmation, or its effective date.
**Do not enter this on a balance sheet from this digest.** It is total equity-neutral in any case
(a transfer between equity lines, not a change in equity), so the NAV effect is plausibly zero and
the real question is the dividend-policy one. Treat as a lead requiring the primary.
**Status.** `decisions/brut_log.md` head is the 8/16 auto-run. **UNREAD.**

### M4 · BRUT — a **rate discrepancy** on the Mount Horizon fixture: $105,700/day here vs **$106,000/day** in Run 1
**What happened.** The **2026-08-06 06:00** release reads, per the issuer feed: a **12–15 month**
time charter for **Mount Horizon** at **$105,700 per day**, delivery **mid-November 2026**, taking
the average charter rate for BRUT's first two VLCCs to **$101k/day**. Run 1 recorded the same
fixture as "the **$106,000/day** print."
**Source.** `mfn.se/all/a/bruton-limited.json` (this run) vs Run 1's own reading of the same release.
**Model surface.** A **charter fixture with a stated rate and tenor** is precisely the class of item
the task lists as able to **supersede a curve input** — and BRUT is a pre-operational name whose
entire near-term revenue picture is two fixtures. A $300/day error is ~0.3%, immaterial to NAV, but
it is **load-bearing for provenance**: an uncited or mis-transcribed figure that moves a value is
the exact failure `test_manifest_provenance` exists to red.
**What I think it means.** Most likely one of the two readings rounded. I would not guess which:
$105,700 is the more specific figure and came from the feed this run, but I read it through a
fetch summary, not the release body, so I cannot claim it as verbatim.
**What I am NOT sure of.** Which figure is the issuer's. **Neither number should be promoted until
someone opens the 8/06 release body**, which is now the single cheapest verification on this list —
and which the NewsWeb channel (M1) will stage automatically once it is carrying arrivals.
**Status.** `brut_log.md` records the fixture; the discrepancy is new and **UNREAD**.

### M5 · GNK — the model **has now seen a post-withdrawal price**; Run 1's central caveat is spent
**What happened.** No new Genco or Diana news 8/15–8/16 (searched; Diana's withdrawal release of
**8/14** and Genco's 8/14 board letter remain the newest items). What changed is the **model**:
the **8/16 20:06 UTC** pipeline run carries **price $26.34, NAV/sh $25.12, PW FV $22.67,
EV −13.9%, broker spread +10.9pp, TRIM/SHORT**.
**Model surface.** `decisions/gnk_log.md`; `inputs/watchlist.yaml` → `GNK.analyst_target: 28.40`.
**What I think it means.** Run 1 warned, correctly at the time, that its TRIM/SHORT print
(price $25.26, EV −10.2%) was "the last **with-deal** read." **That warning is now spent** — the
price has moved **+$1.08 (+4.3%)** and EV has widened to **−13.9%** on an unchanged NAV. So the
market repriced GNK **upward** after the acquirer walked, which is the opposite of the deal-premium
unwind one might have assumed, and the overvaluation signal **strengthened** rather than softened.
That is worth an owner eyeball precisely because it inverts the intuitive read.
**What I am NOT sure of.** Whether $26.34 is a **8/14 close** carried forward across the weekend or
a later mark — the pipeline values at the live close, and 8/15–8/16 are non-trading days, so it is
almost certainly Friday 8/14's close, i.e. **the first and only post-withdrawal close so far**. One
close is thin evidence for "the market repriced upward"; the 8/17 close is the confirmation.
**Status.** `decisions/gnk_log.md` has **no annotation of the Diana withdrawal** — the newest
Diana-related text in the file is the pre-withdrawal tender/proposal block. Still **UNREAD**,
now two days, against a board-set **8/24** response date that Diana pre-empted.

---

## PROMOTABLE CANDIDATES

**Nothing new this window.** No dated S&P print or fixture with the promotion fields landed
8/16 04:15 → 19:15.

**P1 · FRO 2×VLCC — the blocker is now identified, and it is not ours to fix.**
Run 1 left P1 open with "vessel names remain unconfirmed … the GlobeNewswire primary is the place
they would be." I chased that this run. The GlobeNewswire primary **timed out again** (third
consecutive run), **but the names are not there to find**: Splash247, IndexBox, Cyprus Shipping
News, Shipping Herald, iMarine, Argus and Marine Log all cover the 8/04–8/05 release and **none
names the vessels or the buyer** — the consistent phrasing is that the ships and buyer were **not
identified**, with delivery expected during **Q3**. **This is issuer non-disclosure, not a fetch
failure.** Consequence for promotion: the duplicate-sweep required by the 2026-08-09 standing rule
**cannot** be run on vessel names for this print. Either promote on class/built/price alone with
the non-disclosure recorded as the reason, or wait for FRO's Q3 report to name the hulls. **That is
an owner call, and it is now a clean one** — the missing information has a known cause.
*(Legs unchanged: 2 × VLCC, built 2017, $135.0m each / $270m aggregate, 2026-08-04. Confirmed
absent from `inputs/market_data/transactions/vlcc.yaml`, which still ends 2026-08-07 / MB Week 32.)*

**P2a / P2b (TNK Suezmax 2009 $53.5m; TNK VLCC 2013 $84.5m, both 2026-07-29) and P3 (STNG
*STI Solidarity*, LR2 2015, $60.0m, agreed ~2026-03-05)** — carried forward from Run 1 unchanged.
Not re-verified this run; no new information surfaced on any of them.

### Aggregator re-dating — **two more traps caught this run**

Run 1 recorded the NAT re-dating trap. A general FRO search this run surfaced **two more**, both of
which look like current August news in a search framed on August dates:

1. **"Frontline sells eight older VLCCs and buys nine newbuilds"** (Marine Log; also Splash247,
   gCaptain, Seatrade, Globe and Mail) — **8 VLCCs built 2015–2016 for $831.5m** against **9
   scrubber-fitted ECO VLCC newbuildings from a Hemen Holding affiliate for $1,224.0m**, 6 at
   Hengli / 3 at Dalian, 7 delivering 2026 Q3-onwards. A ~$2bn transaction, and on its face
   enormously material. **It is dated 2026-01-08.** Confirmed at the issuer's own page
   (`frontlineplc.cy`, "FRO – Strategic Fleet Renewal and Expansion", **January 8, 2026**).
   **Seven months pre-window.**
2. **"Frontline's fleet renewal push rolls on as sells oldest suezmax pair"** (Shipping Telegraph)
   — 2 Suezmaxes built 2014/2015 for **$140m**, ~$106m net proceeds, ~$55m gain. Promotable-shaped
   for a §9.9 Suezmax anchor. **Published 26/05/2026**, agreement reached **April 2026**.
   **Pre-window.**

Both were killed by the task file's own rule — open the issuer page and read the internal dates
before believing the aggregator's. Recording them because the pattern is now **three instances in
two runs**, always on an APPROX or high-interest name, and always surfaced by a date-framed search:
**a search engine's notion of "recent" is not a publication date.** The 7-month-old FRO item is the
sharpest example yet — it would have been reported as the largest event in the digest.

---

## WATCH

- **The first live test of the NewsWeb channel (M1) is MPCC Q2 on 2026-08-26.** Check for a
  `source: "newsweb"` line in `state/edgar_manifest.jsonl` and a file under
  `inputs/filings/MPCC/newsweb_*` within hours of the release. Green-on-`edgar_poll.log`
  is **not** evidence the NewsWeb lane works — the log prints `0 new release(s)` identically
  whether the lane is healthy-and-quiet or silently broken.
- **BRUT demerger completes by end-August**, 8-ship spin listing on Euronext Growth Oslo, with
  BRUT's own uplisting to Expand / Oslo Børs targeted **end-September**. **Two weeks out and still
  unresolved:** how the model carries one 12-ship NAV today vs two entities shortly. The M3 share
  premium reduction is plausibly a step in this. This is the largest unmodelled structural event
  on the book.
- **Reporting inside two weeks:** **FLNG 8/19** · **GNK 8/24 (Diana response date)** ·
  **2343 ex-div 8/20, record 8/24, payable 9/03** · **TRMD 8/26** · **MPCC 8/26** · **CMBT 8/27** ·
  **BWLP 8/28** · **HAFN 8/28** · **NAT ~8/31** · **CAPT 9/01**.
- **MPCC 8/26 is doing double duty** — first NewsWeb test *and* the first balance sheet to carry
  both the placement (M2) and the 6/25 acquisition. Run 1's point stands: if
  `decisions/mpcc_h1_prereg_2026-08-13.md` pre-registers a band on **443.7m** shares, the band is
  wrong before it is run. Cheapest thing on the list to get ahead of, and now confirmed at primary.
- **CAPT runs on a 31-Mar-2026 balance sheet until 9/01** while carrying, unmodelled: the June
  VLCC acquisition, the 8/06 LR2 delivery + $50.0m senior secured facility, and the 8/13 Suezmax
  delivery + $67.5m sale-and-leaseback. The **SLB-vs-senior-secured distinction (ECO precedent —
  SLB into borrowings, no separate operating-lease line) is the double-count hazard**; the model
  print today reads BUY, EV +9.1%, broker spread +32.8pp, on that stale sheet.
- **Pareto 8/14 daily still absent** — 1 business day, below threshold. Decide at the 8/17 daily.
- **Watchlist price drift vs the 8/07 vintage keeps widening.** Today's run: **GNK $26.34** vs
  `current_price: 25.1`; **CAPT $14.68** vs `14.14`; **MPCC $2.72** vs `2.55`. Reads are current
  (pipeline values live), but `consensus_pnav` / `consensus_fwd_pe` stay paired to 8/07. The staged
  `inputs/watchlist_rebase_2026-08-07.yaml.draft` is still awaiting the owner.

---

## NO-ACTION — swept, nothing in the window

Every line means: **searched over 2026-08-16 04:15 → 19:15 PDT, nothing found that moves a model
surface.** For the US-listed names this is now backed by the hourly EDGAR poller (0 new filings
since 8/14), not by search silence — a stronger claim than Run 1 could make.

- **BRUT · MPCC · CAPT · BWLP** — all four issuer feeds fetched directly at `mfn.se`. Newest items
  are **BRUT 8/13 06:00** (H1 results), **CAPT 8/13 05:32** (Suezmax delivery), **BWLP 8/14 05:00**
  (Q2 date notice), **MPCC 7/02** (share capital registration). **Nothing dated 8/15–8/16 on any
  of them.** Primary-sourced negative. *(Note: each release appears twice in these feeds — an `ob`
  Oslo Børs mirror titled `TICKER: …` and an `mfn` issuer copy. Counted as one event each.)*
- **NAT** — `nat.bm` read directly again: **nothing in August 2026**; newest are 7/23, 7/14, 7/10.
  Independently re-confirms Run 1's finding against the re-dated Cyprus Shipping News item. Q2 ~8/31.
- **2343** — HKEX poller clean at 00:20 UTC; nothing new since the 8/06 Interim. Dividend timetable
  forward-dated (see WATCH).
- **GNK** — searched; no Genco or Diana release dated 8/15–8/16. The model moved, not the news (M5).
- **FRO** — searched deeply for the P1 vessel names; nothing new in-window, and the two apparently
  fresh items proved to be January and May (above).
- **DHT · ECO · INSW · TNK · STNG · SBLK · LPG · HAFN · TRMD · FLNG · CMBT · ASC · CCEC · TEN ·
  CMDB · GSL · SB** — no new EDGAR filing since **CMDB 8/14**, verified against
  `state/edgar_manifest.jsonl` and hourly poller logs through 18:20 today. No web search was run
  per-name for these; the manifest is the stronger check and I am naming that substitution rather
  than implying 17 individual sweeps.

**A genuinely quiet 15-hour Sunday window — and that finding is supported**, not assumed: three
ingest lanes polled clean through 18:20, four Oslo feeds read at primary, one issuer newsroom read
directly. The substance of this run is M1 through M5 and the two re-dating catches, none of which
came from the window itself.

---

## Owner summary — what I'd action first

1. **M1 — the NewsWeb channel is built and live but has never carried an arrival.** Verify the
   bootstrap watermark before **8/26**, and treat MPCC's Q2 as its first real test. Until one
   release lands end-to-end, the next sweep must keep fetching `mfn.se` directly rather than
   trusting the local channel — the task file's "read the local channel first" instruction would
   have returned an empty directory today.
2. **M2 — MPCC's +10.0% share count is now primary-confirmed** (issuer share capital NOK
   488,070,306, plus two flagging notices that cross-foot). The only open question is the NOK 1.00
   par assumption. If the 8/13 H1 prereg carries 443.7m shares, fix it before 8/26.
3. **M5 — GNK repriced UP after Diana walked** ($25.26 → $26.34, EV −10.2% → −13.9%), which
   inverts the expected deal-premium unwind and *strengthens* the TRIM/SHORT. The log still has no
   Diana-withdrawal annotation. Confirm on the 8/17 close before reading much into one print.
4. **M3/M4 — two BRUT items needing the release body, both cheap.** The $226,039,548 share premium
   reduction (purpose and conditionality unknown; likely demerger plumbing, equity-neutral) and the
   **$105,700 vs $106,000/day** Mount Horizon rate discrepancy. The second is a fixture figure that
   could reach a curve input, so pin it before anything uses it.
5. **P1 FRO — the blocker is issuer non-disclosure, not a failed fetch.** No source names the
   vessels or buyer. Promote on class/built/price with the non-disclosure recorded, or wait for
   FRO's Q3 report. A decision is now possible; it was not last week.
6. **Process, and narrower again than Run 1's.** (a) **Stop trying to reach EDGAR by fetch** — all
   three SEC hosts 403, including `data.sec.gov` tested this run; the local manifest is complete,
   current, and the better check. (b) **`globenewswire.com` has timed out on three consecutive
   runs** — treat as unavailable and route to syndicators immediately rather than burning three
   attempts. (c) Aggregator re-dating has now produced **three** false in-window items in two runs;
   the issuer-page date check should be considered mandatory, not a nicety.

---
---

# RUN 1 — 2026-08-16 04:15 PDT (preserved verbatim, unedited)

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
