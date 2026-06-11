# PLAN.md — current sprint plan (Week 4)

Rewritten at each Week close (CLAUDE.md "Week-close checklist"). This file
is the handoff: a new agent starting the sprint reads CLAUDE.md first,
then this. Week 3 closed 2026-06-11 — see CLAUDE.md changelog for what
shipped (news-pull, daily price refresh, FFA-OCR Stage 1 + market-
consistency diagnostic, earnings readiness, CAPT, §15.7 + retro screen).

## Week 4 theme: containers — the last big sector with data in hand

Land `sectors.containerships` (§11.8) before Q2 earnings season so the
August refresh covers the full book. Follow the new-sector workflow
(CLAUDE.md "Onboarding a new sector"; §11.4 engine checklist; §11.7 dry
bulk is the template — first fully greenfield sector, same playbook).

### Step 0 — data freshness triage (do FIRST, half a session)

- The Pareto Container Weekly archive (42 PDFs at
  `inputs/research_pareto_other/container_weekly/`, 84 classified total)
  runs 2024-09 → **2026-04-01 and then stops**. Determine: did the feed
  die in Rocket.Chat (check the channel / `ingest_rocketchat --profile`),
  did Pareto stop publishing, or are newer issues sitting unfetched
  behind daily link annotations (`sp_scan --links` inventory)? A
  10-week-stale anchor source changes the §11.8 as_of choices.
- Skim 3-4 recent weeklies for the rate-table structure (TEU segments:
  feeder <2k, 2,000-3,500, Panamax ~4-5k, larger; charter PERIODS quoted
  — containers are a TC market, not spot).

### Step 1 — §11.8 methodology decision doc (time-boxed one session)

Decisions to make (write the doc BEFORE code, dry-bulk precedent):

1. **Vessel classes** — propose 3-class collapse: Feeder (≤2,000 TEU) /
   Intermediate (2,000-5,500) / Large (>5,500), subject to what the
   weekly's rate table actually segments and what validator fleets hold.
2. **The charter-book problem (the §11.8 core decision).** Container
   tonnage providers are TC-dominated with multi-year charters — the
   spot-convention dividend strip does not apply. Existing conventions
   to draw on: FLNG (TC-heavy book through the strip), TEN DP2
   (off-curve at contracted book, §11.6), CAPT (fleet_schedule ramp).
   Likely shape: strip earns CONTRACTED rates per vessel through charter
   expiry, re-fixes at scenario rates after; NAV stays curve-based with
   a charter-premium/discount adjustment (a vessel with an above-market
   charter attached is worth more than the bare curve value — decide
   whether v1 prices this or documents it as a limitation).
3. **Scenario family** — "Container Set A" (sector-namespaced), 4
   scenarios; demand tree differs from bulk/tankers: box-rate cycle,
   Red Sea/Suez routing normalization, fleet-growth overhang (record
   orderbook %), consumer-demand recession.
4. **Cycle anchors** — empirical from the weekly archive (dry-bulk
   precedent: 22-month median by class). ~19 months available.
5. **External NAV anchor** — verify Pareto coverage set from the
   archive (MPCC near-certain — Oslo, now easy with the NOK machinery;
   check ZIM/DAC/GSL/CMRE mentions). APPROX rules per CLAUDE.md if a
   validator lacks coverage.
6. **Transaction anchors: OUT of v1** (§9.9 scope discipline) — boxship
   S&P prints are charter-attached, not comparable without a charter
   adjustment. Register as backlog, do not build.

### Step 2 — engine wire-up + validators (2-3 sessions)

- `sectors.containerships` block + class map + cycle anchors YAML;
  `_load_all_sectors` + `SCENARIO_CLASS_MAP_BY_SECTOR`.
- Validator 1: **MPCC** (MPC Container Ships, Oslo/NOK — Pareto-anchored
  feeder pure-play; cleanest single-class validator, the "DHT of
  containers"). `/add-ticker MPCC containerships`.
- Validator 2: **DAC or GSL** (US-listed, charter-backlog-heavy — the
  stress test for the charter-book convention). Pick after Step 1.
- Defer CMRE (hybrid containers+bulk; CMDB parent) — note the §15.7
  screen will be interesting there, but hybrids cost more.
- Per-name: full onboarding workflow INCLUDING the new §15.7 screen
  (step 4) and earnings-calendar entries.
- v1 calibration lock: `≥70%/±10%` (new-sector bar), `/reconcile
  --calibration-lock containerships`.

### Step 3 — Week-close checklist (CLAUDE.md) — run it this time too

## Standing threads (not container work)

- **Sat Jun-13 + Jun-20**: weekly digests (`/news-pull` after the 08:00
  chain). Tripwires armed across TEN/CMDB/CAPT/TNK/CCEC — the digest
  watches them.
- **Jun-18 GNK AGM → Jun-26 tender deadline**: morning-after read is
  pre-planned in gnk_log; on lapse, price re-anchors and the deal-arb
  framing comes OFF.
- **FFA-OCR**: review the 16 flagged queue days (~10 min human pass);
  toward end of Week 4, assess the first diagnostic review cycle —
  decision: does the FFA curve stay diagnostic or start informing the
  dry-bulk strip? (Stage 2 backfill decision rides on this.)
- **Hormuz weight revisit trigger** — standing; preempts everything if
  physical-transit confirmation lands.
- **Deferred by owner**: orchestration of the /news-pull agent half
  (scheduled cloud agent); Task-3 weight adjuster; demand-destruction
  overlay; FFA Stage 2.

## Definition of done (Week 4)

§11.8 locked + wired; 2 container validators SANITY=OK with v1 lock
recorded honestly (FAIL-with-explanation acceptable, no back-solving);
earnings calendar covers the new names; tests grow from 243; Week-close
checklist run (docs audited, Appendix A entry written, PLAN.md rewritten
for Week 5); clean git state.
