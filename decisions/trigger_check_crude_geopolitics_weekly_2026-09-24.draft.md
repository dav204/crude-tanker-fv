# `crude_geopolitics_weekly`: trigger-check draft for due 2026-09-24

**DRAFT — agent-assembled 2026-09-24, unverified by the owner.** Evidence horizon: web through the
GlobalSecurity OPREP Day 209 (0800 ET 2026-09-24, cutoff 0500 ET) and outlets dated up to 9/24; repo
through Pareto Shipping Daily 9/23 and MB Tanker Weekly W38 (9/18).

**Proposed disposition:** HOLD 0.28 / 0.59 / 0.00 / 0.13. State: hostilities are still ongoing at sea,
and the week brought the first US–Iran contact since June 21 and a fatal attack on a merchant ship. No
pause or ceasefire has been announced, the US has announced no strike ashore for 17 consecutive
operational periods, and there has been no Iranian salvo on a host state for 15 days. The Houthi–Saudi
front was active (Riyadh and Yanbu targeted on 9/19).

## Ready to paste

`due:` line comment in `inputs/reweight_triggers.yaml` (re-arm to the same weekday):

```yaml
  due: 2026-10-01   # re-armed 2026-09-24: check EXECUTED on the due date. LEG 1 NOT FIRED -
                    # no schedule, no payments; Oman/Salalah meeting still sought "later this
                    # month", no date (GlobalSecurity D209). LEG 2 state CHANGED IN TEMPO, NOT
                    # KIND: first US-Iran contact since 6/21 (Witkoff/Kushner-Araghchi via Qatar,
                    # UNGA 9/22); Iranian offer to reopen Hormuz "within seven days" on conditions
                    # (unnamed senior official, ToI 9/22); written road map incl. up-to-60-day
                    # ceasefire reported 9/23 (GlobalSecurity, primary unopened) - NOTHING
                    # ANNOUNCED. No US strike ashore announced (D209 "seventeenth consecutive
                    # period"); no Iranian ballistic salvo on a host state for 15 days. At sea:
                    # >=5 tanker incidents since 9/16 incl. LR Stephanie (9/21, 2 injured); Cape Dao
                    # (9/23, off Musandam, 1 Indian crew killed, unattributed). Houthis targeted
                    # Riyadh + Aramco Yanbu 9/19 (intercepted per Saudi). Blockade 109 redirected
                    # (9/20). East-West pipeline pumping at low rate from 9/22. Escalation question
                    # RE-RUN -> HOLD 0.28/0.59/0.00/0.13. decisions/geopolitics_weekly_check_2026-09-24.md
```

Status-line note (append under the existing `status: armed` comment):

```yaml
                    # 9/24 check: both legs re-read, question re-run -> HOLD (see due comment).
```

Record filename: `decisions/geopolitics_weekly_check_2026-09-24.md`.

## LEG 1 — Hormuz fee regime (fires on SYSTEMATIC COLLECTION only)

| Dated fact | Source | Bearing |
|---|---|---|
| The US administration "is seeking a meeting between Iranian and Arab representatives in Oman, possibly at Salalah, later this month". GlobalSecurity: "No scheduled date confirmed by cutoff". | GlobalSecurity OPREP Day 209, 9/24 (opened) | The framework has **not convened**. The 9/14 postponement still stands. |
| 9/23 Rezaei: "We will force the United States to respect the rights of the Iranian people and comply with the conditions communicated to it; otherwise, the Strait of Hormuz will not be opened." Conditions: blockade lifted, frozen assets released, "an end to the war on all resistance fronts". **No fees, no Oman, no schedule** in the text. | PressTV 9/23 (opened) | Reopening is on conditions. No fee terms appear. |
| No fee schedule, no amounts, and no corroborated payments were found in any source opened this week. The last dated payment evidence remains ≤8/16 (per the 9/17 record). | all sources opened (see Verification) | No collection evidenced |

**Outcome: NOT FIRED.** Stays armed. Iran's conditions this week are about the blockade, assets and the
war, not fees. The Oman venue is again framed as a US-sought reconciliation meeting, not a
strait-management convening.

## LEG 2 — US–Iran strike state

| Dated fact | Source | Bearing |
|---|---|---|
| Strikes ashore: "No American or coalition strike on Iranian territory ashore was announced". This is the **seventeenth consecutive period** without one (tenth on 9/17). The period counts are GlobalSecurity's arithmetic. GlobalSecurity also reports that CENTCOM "published no statement of any kind" for five days to 9/24. | GlobalSecurity D209 (opened) | **Ashore: unannounced lull, ~22 days since the 9/01–02 wave** |
| US kinetic action on Iranian vessels: no new US action announced in the D209 window. MB W38's "the US hits eight Iranian tankers in four days" recaps **9/05 (3) + 9/08 (5)**, which are already on the 9/10 and 9/17 records, so it is **not new**. | GlobalSecurity D209; MB W38 (in repo); Stars and Stripes 9/05 (search-level) | At sea (US side): quiet this week |
| CENTCOM, Adm. Brad Cooper, **9/19**: "Over one billion barrels of crude have been shipped from Gulf partners through the Strait of Hormuz, and Iran has exported zero barrels thanks to our ironclad blockade"; the fetch summary also reports more than 2,000 assisted transits. | Times of Israel liveblog 9/19 16:28 (opened) | Blockade: persistent, and CENTCOM's words |
| Blockade tally: "109 commercial vessels as published on 20 September" (103 on 9/15). | GlobalSecurity D209 | Blockade: persistent |
| Attacks on shipping: Critical Threats reports "Iran almost certainly launched two unspecified projectiles at two separate tankers in the Strait of Hormuz on September 16 and 17". gCaptain counts **≥5 incidents since 9/16**, including a tanker with a hull breach and fire (9/16–18). | Critical Threats 9/18 (opened); gCaptain 9/21 (opened) | Iranian attacks on shipping continue |
| **9/21** **LR Stephanie** (Isle of Man-flagged crude tanker per search snippet), struck by an unidentified projectile, 2 crew injured. **Al Maryah** (LPG carrier) hit by debris from unidentified projectiles, no casualties. Both continued. UKMTO attribution: unknown. **UKMTO warning numbers not recorded.** | gCaptain 9/21 + 9/23 (opened); GlobalSecurity D209 ("both incidents remain unattributed") | Unattributed |
| **9/23 (Wednesday)**: **Cape Dao** (Antigua & Barbuda bulk carrier), ~2.5 nm off Musandam, struck twice. Engine-room fire, **1 killed (Suraj Yadav, 26, Indian)**, 27 evacuated by the Royal Navy of Oman. Oman Maritime Security Center: "The attack resulted in a fire in the engine room and the death of one crew member". "Two torpedoes" is the **Forward Seamen's Union of India**'s claim, not an official finding. "Neither Iran nor the US claimed responsibility." | The National 9/23 (opened); gCaptain 9/23 (opened); Muscat Daily 9/24 (opened) | **Fatal. Unattributed.** First fatality on the weekly record since El Gaia's missing crewman |
| Host states: "Fifteenth consecutive day without Iranian ballistic launch at host state"; "Nineteenth consecutive day without Iranian drone attack on host state" (GlobalSecurity arithmetic). | GlobalSecurity D209 | **Host states: lull, 15 days** |
| Talks, **9/22**: Witkoff and Kushner "communicated indirectly" with Araghchi "through Qatari mediators", the first diplomatic contact since the 6/21 Bürgenstock talks. Trump, 9/22: "They had a very good meeting, a very productive meeting"; he spoke of a "big decision" between a deal and moving to "annihilate the Islamic Republic". Rubio: "there's no harm in engaging and talking to someone". | Critical Threats 9/23 (opened); Al Jazeera 9/23 (opened); Times of Israel 9/22 (opened) | Words. Contact resumed |
| **9/22** offer (an **unnamed senior Iranian official**, not the FM): "Iran could reopen the Strait of Hormuz to Gulf shipping within seven days if the US fulfilled Tehran's demands to ease military pressure and lift an American blockade on Iranian ports". Condition: "The US needs to announce that it wants to resolve the issue diplomatically, make that official, and then agree on a timeline". | Times of Israel 9/22 (opened) | A conditional offer, **not a pause** |
| **9/23** GlobalSecurity: Iran "presented the United States with a written road map to end the war, providing for a regionwide ceasefire of up to 60 days, a phased reopening of the Strait of Hormuz and an end to the American blockade". Also Rezaei: "Washington has four to five days to accept". | GlobalSecurity D209 only. The underlying wire was not opened. PressTV 9/23 (opened) carries Rezaei but **no deadline** | A proposal, not an announced ceasefire. The deadline rests on one source |
| 9/23 Rezaei: "Enough with negotiations. Take action." Critical Threats: Iran "will neither formally negotiate nor 'reopen' the strait until the United States first meets Iran's conditions". | PressTV 9/23; Critical Threats 9/23 (both opened) | Hard line alongside the offer |
| Wider Gulf, Houthi–Saudi: on **9/19** the coalition intercepted a ballistic missile fired at Riyadh and thwarted strikes on Bisha, Taif, Farasan and **Yanbu**. Houthi spokesman: "two successful military operations using a large number of ballistic and cruise missiles and drones", targeting Aramco facilities in Yanbu. Saudi authorities reported no casualties. Trump cut short Camp David. MBS pressed for direct US action; "Washington declined". On 9/24 The National's liveblog reports six Houthi ballistic missiles intercepted (targets/date not legible in the extract). | Times of Israel 9/19 liveblog (opened); The National 9/20 + 9/24 (opened); Al Jazeera 9/19 (search-level) | **Third-party fire at the bypass terminus.** This front predates the 9/10 re-arm (9/08: 73 wounded, Jazan/Abha; Houthi naval blockade of Saudi vessels since 7/22), but **neither prior record carries it** |
| East-West pipeline: "pumping at a low rate from 22 September, Aramco is seeking to restore throughput toward 4 million barrels a day", with full resumption "could take weeks" (GlobalSecurity). MB W38: "restore around half of the pipeline's capacity within days and full capacity in about six weeks" (broker paraphrase). | GlobalSecurity D209; MB W38 (in repo) | This settles the 9/17 "days vs 5–6 weeks" gap: **both** (partial in days, full ~6 weeks) |
| Flows are contested. GlobalSecurity cites IMF PortWatch at "a single commercial transit on 20 September" (vs ~85/day pre-war) and "396 vessels holding position" (9/23). Tanker Trackers (via Critical Threats 9/23) puts it at "approximately 13 million barrels of non-Iranian oil per day". US officials (via The National, via GlobalSecurity) say "60 and 70 percent of pre-war oil flow". MB W38: Hormuz "averaging around 8 mb/d since July"; ~6 mb/d crude + ~4 mb/d products offline; Iranian exports 210 kb/d in August. | GlobalSecurity D209; Critical Threats 9/23; MB W38 | Unresolved. Transit counts and barrel flows diverge by an order of magnitude |
| Tape (context only, not a weight input), "Average of key routes", ECO no-scrubber: TD3C $1,038,700 (9/15) → **$1,246,000 (9/21 print)** → $1,268,900 (9/22) → $1,262,200 (9/23). TD20 $248,000 → $243,400 → $244,600. Aframax $158,500 → $171,200 → $185,900. Brent (Pareto) $102.0 → $102.1 → $98.5. Pareto 9/23 (broker's phrase): "Brent dipped below $100/bbl yesterday after Iran said they could reopen SoH in a week if US eased military pressure"; tankers "in the crosshairs", several names down ~5%. | Pareto Shipping Daily 9/21, 9/22, 9/23 (in repo) | VLCC plateau >$1.2m; the equity tape reacted to the talks headline |

**State on the card, 2026-09-24:** HOSTILITIES ONGOING AT SEA. Unattributed attacks on merchant
shipping continue (≥5 since 9/16; LR Stephanie 9/21, 2 injured; Cape Dao 9/23, 1 killed). There has
been no announced US action on Iranian vessels this week, and the blockade stands at 109 (9/20).
**No pause or ceasefire has been announced.** The unannounced lulls continue: 17 periods with no US
strike ashore and 15 days with no Iranian salvo on a host state. **Diplomatic contact resumed 9/22**:
an Iranian conditional seven-day reopening offer and a reported written 60-day-ceasefire road map
(9/23), alongside Rezaei's "otherwise, the Strait of Hormuz will not be opened". The Houthi–Saudi
front is active, with Riyadh and Yanbu targeted 9/19. The East-West pipeline is restarting at a low
rate from 9/22.

**Did the state change since 9/17?** In tempo, not in kind. Contact moved from signalling to a
mediated meeting and a written proposal, and the sea war produced a fatality. The pipeline began
restarting. Nothing announced changes the state the legs encode.

## The escalation question, re-run

Rule quoted from `inputs/scenario_inputs.yaml` (escalation block): "scenario weights price persistent
states over the valuation horizon, not event frequency — fast-reverting flare-ups inside a holding
framework are evidence for the MoU-ineffective leg ... not for sustained war economics." Current crude
weights: escalation 0.28 · pre_mou_baseline 0.59 · mou_base 0.00 · mou_bear 0.13.

**Toward escalation**
- *For:* Houthi missiles at Riyadh and Aramco Yanbu (9/19). Yanbu is the Red Sea outlet of the only
  Hormuz bypass, so this is a candidate "third-party strike" with a wider-Gulf bearing. There was a
  fatal attack on Cape Dao (9/23), ≥5 tanker incidents in a week, Rezaei's "otherwise ... will not be
  opened", and Trump's "annihilate" alternative. TD3C is holding above $1.2m.
  *Against:* the Houthi–Saudi front was already live on 9/08 and 7/22, **before** the 9/10 re-arm set
  0.28, so it is not a new state. Its absence from the records is a recording gap (below), not a
  change. Saudi reports interceptions and no damage at Yanbu. The pipeline is restarting, not staying
  shut. "Third-party strike" is still undefined in the repo (9/10 record:180). No MEG closure has been
  announced, and no attack this week has been attributed by CENTCOM.

**Toward pre_mou_baseline / de-escalation**
- *For:* the first US–Iran contact since 6/21, Trump's "very productive meeting", a conditional
  seven-day reopening offer, a reported written road map with up to 60 days of ceasefire, 17 periods
  with no strike ashore, and 15 days with no host-state salvo.
  *Against:* **nothing is announced.** The offer is from an unnamed official and conditional. The road
  map is single-sourced (GlobalSecurity) and unopened at primary. Rezaei set a hard line the next day.
  The R5 / 8/09→8/30 lesson holds: an unannounced lull is not a pause. The sea war worsened (a
  fatality), and the flow state is unresolved (PortWatch 1 transit vs Tanker Trackers 13 mb/d).

**→ HOLD 0.28 / 0.59 / 0.00 / 0.13.** Neither direction has a dated primary that announces a change of
state. The talks track is now closer to tripwire 1 than at any check since 8/30. If a ceasefire or
pause is ANNOUNCED this week, the re-run will need a pre-registered proposal: predicted impact per crude
name, band, flip tripwires, and a fork in `inputs/forks.yaml` under the silence rule. This draft does not
write one.

## Tripwires for 2026-10-01

1. **Toward pre_mou_baseline / mou_base** (kept, sharpened): an ANNOUNCED US–Iran pause or ceasefire
   (CENTCOM / White House / Iranian FM, dated). This includes US **acceptance** of the reported 60-day
   road map, a US step back to Islamabad-MoU commitments, the blockade lifted, or the Oman route
   registered at the IMO. Watch the Rezaei "four to five days" window (≈9/27–9/28, if the deadline is
   real). Action: re-run with the 9/10 +3pp as the candidate donor back to pre_mou; pre-register per
   crude name.
2. **Toward escalation** (kept, amended): a resumed US campaign ashore; an Iranian salvo at a host state;
   a CENTCOM-confirmed strike on a US-flag or US-contracted vessel with a US kinetic response;
   **CENTCOM or Oman attributing the Cape Dao attack to Iran**; **US strikes on the Houthis (a US entry
   into the Saudi front)**; **Houthi damage (not interception) at Yanbu or the East-West line**; or
   Rezaei's deadline lapsing with an announced Iranian step. Dropped: "pipeline outage confirmed at
   weeks", which is now resolved as a partial restart from 9/22. Replaced by "restart reversed". Action:
   re-run; candidate donor pre_mou.
3. **LEG 1 fires** (kept): a published fee schedule, corroborated payments, or the Salalah/Oman
   framework convening. Action: as registered on the card.

## Data gaps and unverified

- CENTCOM and UKMTO pages returned 403; CENTCOM text below is quoted from outlets that carry it verbatim
  (Times of Israel liveblog 9/19 for Adm. Cooper). **No UKMTO warning numbers recorded** for LR
  Stephanie, Al Maryah or Cape Dao. The last number on file is still 124-26 (8/31). The El Gaia number
  (9/17 gap) is also still unrecorded.
- Pareto Shipping Daily **9/16, 9/17, 9/18 and 9/24 are missing** from the repo (the 9/24 print lands
  ~10:00 EDT). The 9/21 print's "yesterday" column is the 9/18 close. MB W39 (9/25) is not yet due.
- The **Cape Dao event date** is 9/23 per The National ("Wednesday"). The gCaptain extract read
  "September 19, 2026 (Wednesday)", which is internally inconsistent (9/19 was a Saturday), and the
  Muscat Daily extract gave 9/24 (its article date). The 9/23 date is carried; the owner may want one
  more primary.
- The **road map (60-day ceasefire)** and Rezaei's **"four to five days"** rest on GlobalSecurity D209
  alone. PressTV 9/23 (opened) has no deadline.
- The **17 September Security Council veto** is mentioned only in GlobalSecurity D209 ("survived the
  Security Council veto (17 Sept)"). A search found only the April 7 Russia/China veto. Unverified;
  not carried in the tables.
- The **US-contracted vessel** (Fox 9/16, 9/17 gap) remains unconfirmed by either government. No new
  source was found.
- Times of Israel 9/22 background says a ceasefire "has largely been in place since April". This is
  outlet framing that contradicts the dated 9/01–02 strike wave on the records. Not adopted.
- Correction MAY be owed on `decisions/geopolitics_weekly_check_2026-09-17.md`, LEG 2 "wider MEG" row:
  the record carries no Houthi–Saudi front, while dated sources show Houthi strikes on Saudi energy
  sites 9/08 (73 wounded; The National / Al Jazeera 9/08, search-level) and a Houthi blockade of Saudi
  vessels since 7/22 (Critical Threats 9/23). That is an omission, not a contradicted figure. The same
  omission is in `escalation_c3_rearm_2026-09-10.md`.
- Correction MAY be owed on `decisions/geopolitics_weekly_check_2026-09-17.md`, LEG 2 "attacks on
  shipping" row: the record lists El Gaia (9/12–13) and the unconfirmed US-contracted vessel only.
  Critical Threats 9/18 reports projectiles at two tankers on **9/16 and 9/17**, inside that record's
  window. This is an omission as well.
- Flow figures are unreconciled: PortWatch 1 transit (9/20), Tanker Trackers ~13 mb/d, US officials
  60–70% of pre-war, MB ~8 mb/d. None of these was opened at the original source.

## Verification

This is a second read of each cited extract against the table rows. Pages were not re-fetched, to stay
in budget. WebFetch returns model-summarised extracts, so quotation marks reproduce the extract's
quotation of the page. Corrections made:

1. MB W38 "US hits eight Iranian tankers in four days" was first read as new US action. It is the
   9/05 + 9/08 sequence already on record, so it is marked not new.
2. The Cape Dao date was corrected from the gCaptain extract's "September 19" to 9/23. The weekday is
   consistent across The National and gCaptain, and the conflict is logged in data gaps.
3. The seven-day reopening offer was attributed to an unnamed senior Iranian official (Times of Israel),
   not to Araghchi. The Pareto "Iran said" wording is labelled as the broker's phrase.
4. Rezaei's "four to five days" deadline and the 60-day road map were attributed to GlobalSecurity, not
   to Rezaei's own opened text, which lacks both.
5. "Two torpedoes" was attributed to the Indian seafarers' union, not to Oman or CENTCOM.
6. GlobalSecurity's consecutive-period counts are marked as its own arithmetic. The only CENTCOM words
   quoted are Adm. Cooper's from 9/19.
7. The 9/17 record's data gaps were all carried: CENTCOM/UKMTO 403, the El Gaia UKMTO number, the Fox
   single-source report, the transit-count single source (superseded by a contested four-source
   spread), and pipeline duration (resolved, and noted as resolved rather than dropped).
8. Status vocabulary: the card stays `armed`, and HOLD needs no `fired`. The disposition follows from
   the tables, since no row carries an announced change of state.
