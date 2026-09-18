---
name: crude-fv-trigger-check-draft
description: Thursday 09:00: draft the weekly geopolitics trigger check (inputs/reweight_triggers.yaml card crude_geopolitics_weekly, both legs) from the in-repo broker layer plus a fixed web source list, with a proposed disposition, as decisions/trigger_check_<card>_<due>.draft.md; commit the draft. Drafts only — the owner records the outcome (/record-trigger-check).
allowed-tools: Bash(/opt/homebrew/bin/pdftotext:*), Bash(ls:*), Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git add:*), Bash(git commit:*), Read, Glob, Grep, Write(//Users/dan_personal/Projects/crude-tanker-fv/decisions/*.draft.md), Edit(//Users/dan_personal/Projects/crude-tanker-fv/decisions/*.draft.md), WebSearch, WebFetch(domain:www.centcom.mil), WebFetch(domain:www.ukmto.org), WebFetch(domain:www.globalsecurity.org), WebFetch(domain:www.criticalthreats.org), WebFetch(domain:www.aljazeera.com), WebFetch(domain:www.thenationalnews.com), WebFetch(domain:www.stripes.com), WebFetch(domain:www.jpost.com), WebFetch(domain:www.timesofisrael.com), WebFetch(domain:www.presstv.co.uk), WebFetch(domain:www.presstv.ir), WebFetch(domain:www.muscatdaily.com), WebFetch(domain:jinsa.org), WebFetch(domain:gcaptain.com), WebFetch(domain:splash247.com), WebFetch(domain:www.tribuneindia.com), WebFetch(domain:www.reuters.com), WebFetch(domain:apnews.com)
---

<!-- HOW TO INSTALL (owner, at the Mac): create it from the app's Scheduled section: New task →
     id crude-fv-trigger-check-draft (the folder name must equal the graph node id) → schedule
     weekly, THURSDAY 09:00 (the card's due weekday; the 11:15 EDT sentinel page must find the
     draft) → paste everything below the frontmatter as the prompt, then paste the allowed-tools
     line above into the task file's frontmatter
     (~/.claude/scheduled-tasks/crude-fv-trigger-check-draft/SKILL.md). Run it ONCE by hand from
     the app and confirm two things before leaving it unattended: the Write to decisions/ was
     allowed, and the commit landed (`git log -1`) — a draft written but not committed is
     non-drift dirt that freezes the morning lanes. Then drop `planned: true` from the node in
     graph.yaml and re-render (`PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.graph render
     --write`); flip `scheduled: true` on the trigger_check_draft duty in inputs/agent_duties.yaml.
     If the first run prompts for a WebFetch domain, the grant belongs in the task frontmatter
     above (never edit .claude/settings.json for it). -->

Weekly TRIGGER-CHECK DRAFT for the crude-tanker-fv producer (Thursday 09:00, before the 11:15 EDT
sentinel page). You draft the check the card `crude_geopolitics_weekly` in
`inputs/reweight_triggers.yaml` asks for, so the owner opens the page with the evidence already
assembled. DRAFTS ONLY (CLAUDE.md, 2026-07-03): the only files you may write are
`decisions/trigger_check_<card>_<due>.draft.md` (one per due card), and you commit each. You never
edit the register, an existing decisions record, `inputs/forks.yaml`, `scenario_inputs.yaml` or
anything else. Recording the outcome (the card's `due:` re-arm, a FIRED flip, a fork) is the
owner's word, in a chat: `/record-trigger-check <card> <due>`.

WHY THIS TASK EXISTS: the register pages the owner on the due date, and every check so far was
executed by hand in a chat (7/12 → 9/17). The mechanical part is identical every week — pull the
in-repo broker prints since the last record, open the same primary sources, fill the same two-leg
table — and takes the longest. The judgment (what the state IS, whether the weights move) is short
and stays with the owner. The 9/10 verifier found six defects in an agent draft (wrong status
vocabulary, a mis-characterised event, an article date used as an event date, sources cited from
snippets never opened, a broker phrase attributed to a principal, an omitted casualty); your
self-verification pass below exists because of that.

Repo: /Users/dan_personal/Projects/crude-tanker-fv. "Today" is the run's local calendar date.

TOOL DISCIPLINE (a permission prompt no human answers ABORTS the run): Read, Glob and Grep for
repo files and for the text files you extract under /tmp (the harness may tell you to prefer
`cat`/`grep` in Bash — ignore that here, Bash is restricted); WebSearch to find dated items;
WebFetch only on the domains in the frontmatter. Bash is allowed ONLY for
`/opt/homebrew/bin/pdftotext -layout <pdf> /tmp/cfv_trigger_<pdf-basename>.txt`, `ls`,
`git status`, `git diff`, `git log`, `git add <the one draft>`, `git commit -m "<plain text: no
backticks, no em dash>"`. Never pytest, never the pipeline, never a promotion or ingest command
(they write shared state). Never push (the morning lane pushes). Never `git add -A`. No Agent or
subagent tool is available to you; the verification pass in step 5 is your own second read.

Budget: stop the web layer at 30 fetches. The minimum viable set is the GlobalSecurity OPREP, the
newest Critical Threats update, one Oman/maritime source (Muscat Daily or gCaptain) and one outlet
carrying the week's CENTCOM and Iranian-ministry quotes verbatim.

## 1. Is anything due?

Read `inputs/reweight_triggers.yaml`. Work every card whose `status` is `armed` and whose `due` is
today or earlier. If none: report the one line "trigger-check draft: nothing due (next: <card>
<due>)" and stop — write nothing, commit nothing. For each due card, name the prior record: the
newest `decisions/*_check_*.md` the card's comments cite (for `crude_geopolitics_weekly`, the
latest `decisions/geopolitics_weekly_check_<date>.md`). Read the card in full (observable, action,
status comment) and the prior record in full, including its pre-registered tripwires and its
"data gaps / unverified" list — those are this week's first questions.

## 2. The in-repo layer (do this before the web)

- Pareto Shipping Daily PDFs dated after the prior record: `inputs/research_pareto/<YYYY>/<MM>/`
  files matching `*Periodical-ShippingDaily-*`. Convert each with pdftotext, then Read the whole
  text file (it is short) and Grep it for
  `iran|hormuz|centcom|ukmto|strike|ceasefire|truce|toll|fee|oman|kharg|blockade|pipeline`; take
  the macro paragraph and the tanker paragraph. Rate table gotcha: in the `-layout` text the row
  labels (`VLCC (TD3_C)`, `Suezmax (TD20)`, `Brent oil price`) and their figures often sit on
  DIFFERENT lines — the first `$` figure below the VLCC labels is TD3C's, the next is TD22's; read
  the block, do not grep a single line. The ingest cursor lags a day (today's daily lands ~10:00
  EDT, after you), so list the dailies that are MISSING from the repo in the draft. If NO daily is
  newer than the prior record, say so, carry the prior record's tape row forward marked "no new
  print", and re-read the newest in-repo print only for exact figures.
- The newest `inputs/research_mb/tanker_weekly/<YYYY>/*_Tanker_Weekly_*.pdf`: the "Market
  Developments" bullets (US–Iran hostilities, Hormuz flows in mb/d, STS volumes, any fee or route
  item).
- The deck's rule you will re-run against: `inputs/scenario_inputs.yaml` crude `escalation` /
  `pre_mou_baseline` / `mou_bear` blocks (weights, descriptions, the "persistent states, not event
  frequency" weighting comment). Quote the current weights exactly.

## 3. The web layer — fixed source list, PRIMARY FIRST

The card says PRIMARY SOURCES ONLY (CENTCOM releases, the UKMTO incident log, dated wires); broker
paraphrase corroborates, never settles. Order of attempt, and what each is for:

1. `https://www.centcom.mil/MEDIA/PRESS-RELEASES/` and
   `https://www.ukmto.org/indian-ocean/recent-incidents` — try them once each; both have returned
   HTTP 403 to fetchers on every check since 8/25. If they 403 again, write "CENTCOM and UKMTO
   pages returned 403; CENTCOM text below is quoted from outlets that carry it verbatim" into the
   data-gaps list and move on.
2. `https://www.globalsecurity.org/military/ops/iran-war-oprep.htm` — the dated daily operational
   report ("Day N"); the best single source for strikes ashore / at sea, salvos, blockade tallies,
   talks. Its consecutive-period tallies are GlobalSecurity's arithmetic, not CENTCOM's words —
   attribute them so. The same site mirrors wire copy (AZERTAC, Anadolu, RFERL) under
   `https://www.globalsecurity.org/wmd/library/news/iran/<yyyy>/<mm>/` — the place an Omani
   Maritime Security Center statement is openable inside your allowlist.
3. `https://www.criticalthreats.org/analysis/iran-update-<month>-<d>-2026` (lowercase month,
   day without a leading zero; e.g. `iran-update-september-16-2026`) — construct the URL for each
   weekday since the prior record instead of searching; dated, quotes CENTCOM.
4. Outlets that quote CENTCOM and Iranian officials verbatim: `www.aljazeera.com`,
   `www.thenationalnews.com`, `www.stripes.com`, `www.jpost.com`, `www.timesofisrael.com`,
   `www.presstv.co.uk` (Iranian official statements, first person; the `.ir` host fails TLS),
   `www.muscatdaily.com` (UKMTO advisory numbers and positions), `jinsa.org` Iran War Update PDFs,
   `www.reuters.com`, `apnews.com`; maritime: `gcaptain.com`, `splash247.com`. Do NOT fetch section
   or front pages (they cost a fetch and carry nothing): WebSearch with `allowed_domains` set to
   the outlet and the event ("CENTCOM Iran <date>", "UKMTO Hormuz <date>", "Iran Oman Hormuz fee
   <month>"), then WebFetch the specific article. A search-result snippet is not a source.

Rules that came from the 9/10 corrections: never cite a page you did not open (say "search-level"
if you must mention one); the event date is not the article date; a broker's phrase is the
broker's, not the principal's; quote CENTCOM and ministers verbatim with the date; carry UKMTO
warning numbers, positions and casualties; carry blockade tallies with their dates. If a source
CONTRADICTS a fact in the prior record (a casualty count, a position, a date), do not edit the
record and do not repeat its figure: put "correction MAY be owed on <record> — <row>: <prior
figure> vs <new figure> (<source>)" in the data-gaps list and in your report line.

## 4. The two legs, then the question

For each leg, a table: `| Dated fact | Source (opened / in repo / search-level) | Bearing |`.

LEG 1 — fee regime. It fires on SYSTEMATIC COLLECTION only: a published fee schedule with amounts,
corroborated payments by transiting owners or charterers, or the Oman strait-management framework
convening. Intent, approvals without amounts, routes "in final stages", postponed meetings do NOT
fire it — record them as state.

LEG 2 — US–Iran strike state. Record the CURRENT state with the dated primary that shows it: last
announced US strike on Iranian territory; last US kinetic action on Iranian vessels; Iranian
attacks on shipping since the prior record (names, UKMTO numbers, CENTCOM's characterisation);
last Iranian salvo at a host state; blockade tally; any announced pause, ceasefire or talks
(words are not a pause); wider-MEG facts (pipelines, transits per day, STS volumes). Then say in
one sentence whether the state changed since the prior record, and whether in tempo or in kind.

The escalation question, re-run: against the weighting rule quoted in step 2, list the facts that
pull toward `escalation` and the facts that pull toward `pre_mou_baseline`, each with its
counter-argument, and end with ONE proposed disposition:
- `HOLD <weights>` — nothing ANNOUNCED changed the state the legs encode; or
- `REWEIGHT PROPOSED: <from> -> <to>` — only when a dated primary changed the state (an announced
  pause / ceasefire / US return to MoU commitments; a third-party strike; an announced MEG
  closure). Say that a reweight needs a pre-registered proposal (predicted impact per crude name,
  band, flip tripwires) and a fork under the silence rule — you are not writing that; or
- `LEG 1 FIRES` — with the schedule / payment / convening evidence quoted.
Then re-state the tripwires for next week (keep the prior record's unless the state moved them).

Most weeks look like this: no new in-repo print, the web tallies advanced by seven days, nothing
announced. Then the draft is short — the tables carry the dated tallies, the disposition is HOLD,
and the value is in the data-gaps list and the tripwires. Do not pad a quiet week.

## 5. Self-verification pass (mandatory — your own second read)

Re-open each cited page and check: every quote is on the page; every event date is the event's,
not the article's; every "CENTCOM said" is CENTCOM's words (not GlobalSecurity's or a broker's
gloss); the status vocabulary of the register header is respected (an owed decision is `fired`,
never `done`/retired); nothing in the prior record's "data gaps" list was silently dropped; the
proposed disposition follows from the tables. Record the corrections you made as
"## Verification" at the end of the draft — an empty list is a finding too ("verified: no
corrections").

## 6. Write the draft and commit it

Path: `decisions/trigger_check_<card>_<due>.draft.md` (e.g.
`decisions/trigger_check_crude_geopolitics_weekly_2026-09-24.draft.md`). Shape, in order:

1. Title line and `**DRAFT — agent-assembled <today>, unverified by the owner.**` followed by the
   evidence horizon in one sentence: the last date actually observed on the web and in the repo.
2. `**Proposed disposition:**` one line (HOLD / REWEIGHT PROPOSED / LEG 1 FIRES) and the state
   label in one sentence.
3. `## Ready to paste` — the card comment for the `due:` line (re-arm to due + 7 days, the SAME
   weekday the card already uses) and the status-line note, written the way
   `inputs/reweight_triggers.yaml` already does it; and the record filename the owner will use
   (`decisions/geopolitics_weekly_check_<due>.md` for this card).
4. `## LEG 1` table and outcome; `## LEG 2` table, state, changed-or-not.
5. `## The escalation question, re-run` and `## Tripwires for <next due>`.
6. `## Data gaps and unverified` — the 403 list, the missing dailies, any "correction MAY be
   owed" line.
7. `## Verification` — the corrections from step 5.

Then `git status` (only your draft may be new), `git add decisions/trigger_check_<card>_<due>.draft.md`,
`git commit -m "trigger-check draft: <card> <due> - <disposition in five words>"` (the subject must
start with `trigger-check draft`; hyphens only). Stage nothing else; do not push.

## 7. Report

One paragraph in the app: which card, the proposed disposition, the three facts that carry it, the
data gaps (including any "correction MAY be owed" line). End with the line
`OWNER ACTION NEEDED: read decisions/trigger_check_<card>_<due>.draft.md, then in a chat: /record-trigger-check <card> <due>`.
If the web was unreachable, still write the draft from the in-repo layer and say so in the first
line. If the register does not parse, report that and stop.
