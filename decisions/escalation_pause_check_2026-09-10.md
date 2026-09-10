# Escalation-pause corroboration check — 2026-09-10 (trigger DUE 2026-09-01, 9 days late)

**Outcome: CONTRADICTED by SUPERSESSION.** The 8/09 "pause HOLDS" record was true on its date and
held through ~8/29; the pause ended 2026-08-30. Status on the card → `fired`: under the
register's own vocabulary an owed docket is `fired` (reweight decision OWED, stays red until
resolved), not `done`/retired. **The reweight is the owner's** — R5 stands on its 8/16 evidence;
C3's second ground (an uncorroborated pause) is now moot in the OPPOSITE direction. This docket is
deliberately NOT in `inputs/forks.yaml`: a reweight never executes by silence.

**Corrections applied to the agent's draft before recording** (verifier): (1) status `fired`,
not `done`/retired; (2) the 8/30 event is CENTCOM's "limited, precise action against IRGC
minelaying forces" on Larak Island — the broad radar/missile/mine-laying campaign is 9/01; (3)
UKMTO 124-26 is dated 8/31 (9/01 is the RFERL article date); (4) four primaries returned 403 and
the ABC entry could not be found — replaced by sources that open and quote CENTCOM verbatim
(Al Jazeera 8/31 and 9/01; JINSA 9/1-2); (5) "single largest attack of the war" is Pareto's
phrase (9/09), not the IRGC's; (6) added: Bahri SIDR, two crew killed in Hormuz 8/31 (JINSA).

**Owner item alongside:** prune-ledger F3 (fold the two geopolitics cards into one monthly card,
answered yes conditioned on WO5) would have caught 8/30 on 9/25 — re-decide F3 against this
outcome before it executes.

---
# APPENDIX A — the check (agent, read-only)

# TRACK ESC — `escalation_pause_corroboration` (due 2026-09-01, checked 2026-09-10)

## 1. The observable, as the card defines it

`inputs/reweight_triggers.yaml:39-66`. Question: does the 2026-08-09 record's claim "the US strike pause HOLDS" (`decisions/crude_pause_talks_watch_2026-08-09.md:11`, pause dated ~7/27 there; re-dated "post-8/01" by the 8/25 check) survive? Sources: "PRIMARY SOURCES ONLY: CENTCOM releases, the UKMTO incident log, dated wires. Aggregator syntheses do not settle this." Window: weekly cadence, re-armed 8/25 for 9/01 (card comment: "Weekly cadence kept (expired ceasefire + live tanker-attack tape, UKMTO 120-26 8/24)"). Two outcomes only: "If CONFIRMED: record and re-arm, escalation stays untouched at 0.25." / "If the 8/09 'pause HOLDS' record is CONTRADICTED: correction-annotate that record FIRST, then docket the escalation question against the corrected record — never re-base the escalation leg on an uncorrected premise." Registered by R5 (`decisions/crude_day60_toll_cliff_2026-08-16.md:198-201`): C3 "Exceeds the registered action; rests on one week's tape plus an uncorroborated pause status."

## 2. Evidence since 8/16 (verbatim, dated)

**Pause still holding through 8/28 (baseline, broker layer):**
- MB Tanker Weekly W34, 2026-08-21: "Iran continued attacking shipping in the Strait of Hormuz this week, triggering air defences in the UAE but no US military response."
- MB W35, 2026-08-28: "Brent ... set to fall 5.3% ... despite unresolved US-Iran tensions. On Monday, the US warned countries to cut financial ties with Iran or face secondary sanctions under its 'Economic D-Day,' but the Treasury stopped short of imposing penalties." No US strike reported.
- Pareto 8/27: "Trump said there is no timeline to resume talks with Iran, and called SoH 'a functioning strait'."

**Pause ENDED ~8/30 (broker layer, six consecutive dated Pareto dailies + MB W36):**
- Pareto Shipping Daily 2026-08-31: "US forces struck two of Iran's rocket launchers yesterday with Teheran responding with attacks on US bases in Jordan. Trump has again threatened to blow up Kharg Island. Brent up 1.5% this morning; once again exceeding $90/bbl."
- Pareto 9/02: "Brent up almost 5% yesterday and exceeding $95/bbl this morning. US and Iran continued their tit for tat strikes."
- Pareto 9/03: "some reports that Trump is considering declaring the war with Iran over."
- Pareto 9/04: "at least no further flare-up between the US and Iran (and tanker traffic seemingly moving)."
- MB W36, 2026-09-04: "Brent (USD 95.4/bbl) ... rose 6.6% ... week-on-week ... as the US resumed strikes on Iran for the first time in a month, targeting radar, missile and mine-laying sites as it sought to secure control of the Strait of Hormuz. Iran retaliated by striking US bases in Jordan, Bahrain and Kuwait. Despite President Trump's prediction of a short campaign, both sides intensified their attacks, leaving the six-month conflict caught between a ceasefire and all-out war." Also: "Attacks on tankers in the Persian Gulf and near the Red Sea have intensified, with at least six confirmed incidents over the past 10 days ... the US naval blockade has substantially constrained Iranian oil exports for seven weeks."
- Pareto 9/07: "Brent approaching $98/bbl this morning after US missiles hit three Iranian tankers on Saturday."
- Pareto 9/09: "the US attacking five Iranian vessels – and sinking one of them (an aframax) ... Brent ... now at $99/bbl." Tanker section: "reports of Iran's IRGC saying it carried out 'the single largest attack in the Strait of Hormuz of the war', with eight vessels that were attempting to pass through struck, in addition to two US destroyers. This came in retaliation to the US striking three Iran-related tankers earlier this week (which Iran also met by striking six ships), and then another five last night."

**News digests 8/24, 8/29, 9/07:** per-name sweeps only; no macro US–Iran strike line (grep for iran/strike/centcom/ukmto returns only Hormuz-trapped-vessel and Dynacom-resale items). **Geopolitics cards in `inputs/*.yaml`:** only `scenario_inputs.yaml` and `reweight_triggers.yaml` match; neither records a post-8/25 event. **In-repo primary captures since 8/26:** none (grep CENTCOM/UKMTO in decisions/, outputs/, inputs/ → no hits after the 8/25 check).

**Primary layer (web probe, snippet-level — I read search-result summaries, not the full pages; the settling step is opening these texts):**
- Axios, 2026-08-30 ("U.S. strikes Iran to prevent Hormuz mine threat"): CENTCOM "said U.S. forces began striking Islamic Revolutionary Guard Corps targets in Iran at noon ET after recent attempted attacks on commercial shipping in the Strait of Hormuz and U.S. personnel ... IRGC forces were observed preparing to launch rockets with sea mines into the Strait."
- CNBC 2026-09-01 / Al Jazeera 2026-09-01 ("US military says launching new attacks on Iran"; "Iran claims attacks on Bahrain, Jordan, Iraq after US strikes kill 11"): targets "air defence sites, radar systems, maritime assets, mine-laying capabilities and communications infrastructure"; ~100 IRGC sites per Axios/Channel 12.
- UKMTO Warning 124-26 (RFERL via GlobalSecurity, 2026-09-01): "a tanker completing an outbound Hormuz transit was struck by three unknown projectiles approximately 17NM east of Khasab."
- ABC live (undated snippet): "on 8 September, U.S. forces struck multiple IRGC-linked oil tankers roughly four nautical miles off Kharg Island."

Sources: [Axios 8/30](https://www.axios.com/2026/08/30/us-iran-strike-hormuz-mines), [CNBC 9/01](https://www.cnbc.com/2026/09/01/us-strikes-iran-after-new-hormuz-strait-shipping-attacks-centcom.html), [Al Jazeera 9/01](https://www.aljazeera.com/news/2026/9/1/us-military-says-launching-new-attacks-on-iran), [UKMTO 124-26 via GlobalSecurity](https://www.globalsecurity.org/wmd/library/news/iran/2026/09/iran-260901-rferl07.htm), [ABC live](https://abcnews.com/International/live-updates/iran-live-updates-centcom-targeted-iranian-forces-posed/?id=136080582), [JINSA 9/1-2 update](https://jinsa.org/wp-content/uploads/2026/09/Iran-War-Update-9.2.26.pdf).

## 3. Outcome: CONTRADICTED — but by SUPERSESSION, not error

The 8/09 record and the 8/25 CONFIRMED check were true on their dates: the broker layer shows no US strike 8/01→8/29 (W34 "no US military response"; W35 silent on strikes). The pause **ended 2026-08-30** with a CENTCOM-announced campaign, and the state has since intensified (tankers struck 9/05, five vessels/one sunk 9/08, IRGC's "largest attack of the war" 9/09, Brent $89→$99). This is not the July conflation the card warned about: every source is dated post-8/29 and internally consistent across seven broker prints and three wire/UKMTO items. It is not "fast-reverting within days" (`scenario_inputs.yaml:131-136`): day 12 of a widening campaign. The card's own vocabulary settles at CONTRADICTED; the parent's "superseded" is the precise sub-form.

**Record to write on the card (status → `done`, dated 2026-09-10, 9 days overdue):**

> Checked 2026-09-10. The 8/09 "pause HOLDS" record is CONTRADICTED by supersession: the post-8/01 pause held through ~8/29 (MB W34 8/21 "no US military response"; W35 8/28) and ENDED 2026-08-30 with a CENTCOM-announced strike campaign on IRGC air-defence/radar/mine-laying targets after an attempted Hormuz mining (Axios 8/30; CNBC/Al Jazeera 9/01; Pareto 8/31 "US forces struck two of Iran's rocket launchers yesterday"; MB W36 "resumed strikes ... for the first time in a month"). Iran retaliated on US bases in Jordan/Bahrain/Kuwait; US struck 3 Iranian tankers 9/05 and 5 vessels 9/08 (one aframax sunk); IRGC claims 8 vessels + 2 US destroyers struck 9/09 (Pareto 9/07, 9/09). UKMTO 124-26 (9/01) tanker struck 17nm E of Khasab. Primary texts read at snippet level only — full CENTCOM/UKMTO text to be opened and filed before any weight moves. Per the registered action: correction-annotate `crude_pause_talks_watch_2026-08-09.md` and `escalation_pause_check_2026-08-25.md` ("true as of date; pause ended 8/30") FIRST; escalation question DOCKETED against the corrected record; weights UNTOUCHED (0.25/0.62/0.00/0.13). Trigger retired (its question is answered); successor = the docket.

## 4. What it implies for the declined C3

R5 declined C3 on two grounds. Ground 2 (uncorroborated pause) is now moot in the **opposite** direction: the premise C3 rested on (blockade + attacks + 17% traffic + a *paused* US campaign) has been replaced by a materially stronger escalation fact. C3 does **not** "re-arm" — it was a candidate at the 8/16 venue, not a registered trigger, and its number (+3pp) was sized to the 8/16 state, not this one. The card's action is explicit: **docket** the escalation question against the corrected record, not reweight. What the docket must decide is the §13.3 question the escalation leg's own comment poses (`scenario_inputs.yaml:131-136`): persistent state vs event frequency. Facts for the sitting: 12 days and intensifying (W36 "both sides intensified"), yet MEG visible exports 10 mb/d and Hormuz ~7 mb/d via STS (W35/W36) — the tape sits between `mou_bear`'s "Strait mostly OPEN ... episodic-spike" and `escalation`'s "wider MEG closure". The 8/16 sim showed a +3pp tilt breaches the gate broadly (~+7pp BRUT, `toll_cliff:122`), so any move is annotate+ratify work.

## 5. Does this flip a prior ruling? Who writes what

- **R5 stands** — a ruling on the 8/16 evidence; nothing here flips it retroactively. The 8/09 and 8/25 records get a dated supersession annotation, not a retraction. **Agent records** all of §3 (precedent: the 8/25 check was agent-authored).
- **The reweight is OWNER's**: the card stops at "docket". Hazard: under `inputs/forks.yaml` policy (ruled 2026-09-10, "EXECUTES after 3 business days of silence"), a docket entered as a fork WITH a weight recommendation executes by silence — a de facto reweight the card never authorised. Docket it as a queue item with the facts and the gate sim, recommendation "owner sitting required; no number by silence".
- **F3** (fold the two geopolitics cards into one monthly card, answered **yes** `prune_ledger:163`, conditioned on WO5): a monthly cadence would have caught 8/30 on 9/25. Owner should re-decide F3 against this outcome before it executes.
- **`hormuz_fee_collection_watch`** unaffected (no collection evidenced; Iran–Oman corridor talks only, W35).

**UNVERIFIED / settles it:** exact CENTCOM release text and UKMTO 124-26 log entry (open the pages; CENTCOM 403s to fetchers per 8/25); the "~100 IRGC sites" figure (single-attributed Channel 12/Axios).
---
# APPENDIX B — verification

**VERDICT: RECORD WITH CORRECTIONS.** The CONTRADICTED outcome is sound and inside the card's vocabulary; no ruling flips and no weight moves. Three corrections before recording: (1) the trigger must NOT be retired — under the register's own status vocabulary an owed docket is `fired`, not `done`/retired; (2) the 8/30 event is mis-characterised (limited Larak Island strike, not the air-defence/radar campaign — that is 9/01); (3) UKMTO 124-26 is dated 8/31, not 9/01, and four of the six cited primary links were never opened (403) and should be replaced by the sources that do open.

## 1. Observable as the card defines it — VERIFIED, not re-defined

`inputs/reweight_triggers.yaml:39-66` read verbatim: observable = does the 8/09 "US strike pause HOLDS" record survive on "PRIMARY SOURCES ONLY: CENTCOM releases, the UKMTO incident log, dated wires"; two branches, CONTRADICTED → "correction-annotate that record FIRST, then docket the escalation question against the corrected record"; CONFIRMED → "record and re-arm, escalation stays untouched at 0.25". R5 quoted verbatim at `decisions/crude_day60_toll_cliff_2026-08-16.md` ("Exceeds the registered action; rests on one week's tape plus an uncorroborated pause status") — VERIFIED. The work's "supersession" gloss is outside the card's two-word vocabulary but lands on the CONTRADICTED branch and executes exactly that branch's action; it does not soften the outcome. Acceptable. The 8/09 claim sits at `crude_pause_talks_watch_2026-08-09.md:11` — VERIFIED.

## 2. Sources re-read verbatim

| Cited | Status |
|---|---|
| MB W34 8/21 "Iran continued attacking shipping ... but no US military response" | VERIFIED (`inputs/research_mb/tanker_weekly/2026/2026-08-21_Tanker_Weekly_34_2026.pdf`) |
| MB W35 8/28 "Economic D-Day ... Treasury stopped short"; Hormuz ~7 mb/d via STS | VERIFIED |
| MB W36 9/04 "resumed strikes on Iran for the first time in a month, targeting radar, missile and mine-laying sites"; Jordan/Bahrain/Kuwait; "both sides intensified"; "six confirmed incidents over the past 10 days"; MEG 10 mb/d | VERIFIED |
| Pareto 8/27, 8/31, 9/02, 9/03, 9/04, 9/07, 9/09 (all quoted phrases incl. "single largest attack", aframax sunk) | VERIFIED (`inputs/research_pareto/2026/08–09/`) |
| Al Jazeera 9/01 (targets list; 11 killed; Bahrain/Jordan/Iraq/Kuwait; "on Sunday ... struck Larak Island") | VERIFIED, page opened |
| Axios 8/30, CNBC 9/01, GlobalSecurity/RFERL 9/01, UKMTO 124-26 PDF | **NOT OPENABLE (HTTP 403)** — the work admits snippet-level; these cannot carry the record |
| ABC live "8 September ... four nautical miles off Kharg" | **NOT FOUND on the page** — the fetched page shows only 9/05 entries (CENTCOM "permanently disabled" two tankers, "completely destroyed" another). UNVERIFIED as cited |
| JINSA 9/1–2 update | VERIFIED (parsed locally): 9/01 CENTCOM X-page target list; ~100 sites single-attributed to Channel 12/Axios; 59 missiles/drones overnight 9/02 at Jordan/Bahrain/Kuwait/Iraq; 8/30 Hawkins "preparing to launch rockets with sea mines" |

Substitute primaries that DO open and quote CENTCOM verbatim: [Al Jazeera 8/31](https://www.aljazeera.com/news/2026/8/31/can-iran-use-rockets-to-mine-the-strait-of-hormuz-as-us-claims) ("broke a one-month lull ... striking military targets on Larak Island on Sunday"; "limited, precise action"); [defconalerts 8/31](https://www.defconalerts.com/p/centcom-refutes-irgc-claim-says-it) (CENTCOM statement text: "limited, precise action against IRGC minelaying forces posing an imminent threat in the Strait of Hormuz"); [JPost 9/01](https://www.jpost.com/middle-east/iran-news/article-907267) (CENTCOM: "air defense sites, radar systems, maritime assets and facilities, mine-laying capabilities, and communications sites"; wave completed "early on Wednesday" 9/02); [investinglive 9/01 22:43 GMT](https://investinglive.com/commodities/centcom-confirms-hits-iranian-air-defence-and-naval-sites-after-hormuz-mine-attempt/); [Muscat Daily 9/01](https://www.muscatdaily.com/2026/09/01/tanker-struck-by-3-unknown-projectiles-near-khasab/) (UKMTO 124-26: "Aug 31 at 2000UTC", "17NM east of Khasab", "3 unknown projectiles", outbound); [Al Jazeera 9/09](https://www.aljazeera.com/news/2026/9/9/us-destroys-five-iranian-tankers-iran-retaliates-with-attacks-on-jordan-base) (CENTCOM: Kaviz, Charminar, Horizon 1, Riesco in the Gulf of Oman, Derya near Kharg; Riesco sinking on video; IRGC claims 8 tankers + DDG-119/DDG-53). The 8/24–8/29 gap is closed by [CNN 8/30](https://www.cnn.com/2026/08/30/politics/us-iran-strikes-larak-island) ("first US strikes on Iran since July 29") — the 8/25 CONFIRMED verdict survives.

## 3. Findings

**F1 — Status `done` + "Trigger retired" is WRONG under the register's own vocabulary. CORRUPTING if recorded as written.** `reweight_triggers.yaml:10-13`: "fired (observed — reweight decision now OWED, stays red until resolved) / done (decision recorded ...) / retired (superseded)". The CONTRADICTED branch dockets a decision = owed → status is `fired` until the owner sitting resolves it. Retiring makes the preflight stop paging on the exact question that is live — the F-2 failure the file header exists to prevent ("Prose cannot page anyone"). "Successor = the docket" names no register entry, so nothing pages. It also partially pre-executes F3 (fold to monthly, `prune_ledger_2026-09-02.md:163`) before the monthly card exists. Fix: status `fired`, dated 2026-09-10, pointing at the docket; leave cadence to the owner.

**F2 — 8/30 event mis-characterised. RECOVERABLE.** The proposed record says the pause "ENDED 2026-08-30 with a CENTCOM-announced strike campaign on IRGC air-defence/radar/mine-laying targets". CENTCOM's 8/30 action was "limited, precise action against IRGC minelaying forces" — two rocket launchers on Larak Island (defconalerts 8/31; Al Jazeera 8/31; Pareto 8/31 "two of Iran's rocket launchers"). The air-defence/radar/maritime/comms wave is 9/01, completed early 9/02 (JPost; JINSA; investinglive). Record: pause ended 8/30 (Larak, limited); campaign widened 9/01. The end date stands.

**F3 — UKMTO 124-26 dated 9/01: WRONG. RECOVERABLE.** Warning dated 8/31 (file `20260831-ukmto_warning_124-26.pdf`; incident 8/31 2000 UTC per Muscat Daily). 9/01 is the RFERL article date.

**F4 — Four of six primary citations never opened (403) and one (ABC) does not show the cited entry. RECOVERABLE.** Replace with the §2 substitutes; keep the "CENTCOM/UKMTO own pages 403" limitation noted, as the 8/25 record did.

**F5 — IRGC "single largest attack of the war" rests on Pareto 9/09 alone.** Al Jazeera 9/09 does not carry the phrase (it carries "8 tankers" + two destroyers). Attribute to Pareto, not to the IRGC directly.

**F6 — Omitted environment-leg fact:** Bahri SIDR, two crew killed in Hormuz 8/31 (JINSA 9/1–2). Belongs beside UKMTO 120-26/124-26 in the record.

## 4. Vocabulary / ruling checks

- Weights 0.25/0.62/0.00/0.13 confirmed at `scenario_inputs.yaml:142,226,307,371`; untouched — correct. `:131-136` mean-reversion comment, `toll_cliff:122` (~+7pp BRUT), `prune_ledger:163` F3 = yes, `forks.yaml` policy ruled 2026-09-10 — all VERIFIED.
- R5 stands; annotating the two agent-authored records is agent-writable and card-mandated. The docket's number is the owner's; the work's refusal to enter it as a silence-executing fork is correct and should be kept verbatim.
- Owner word is needed only for (a) the docket's resolution and (b) F3 re-decision — both already routed to the owner by the work. No owner word needed to record the corrected check.

**UNVERIFIED / what settles it:** CENTCOM's own release text and the UKMTO 124-26 PDF (both 403 to fetchers — open in a browser and file); the "~100 IRGC sites" figure (Channel 12/Axios only, per JINSA); the "noon ET" start time (attributed to CENTCOM in search synthesis, source page 403 — drop it from the record unless opened).