> **RE-SCHEDULED 2026-09-07.** The 9/06 arm never happened: the Mac was dark all of 9/05–9/06, so
> the arm reminder fired late on Monday 9/07 and nothing was armed. New dates below — ARM Saturday
> 2026-09-12 after the 08:15 run, PAGE + RESTORE Monday 2026-09-14 ≈14:15 EDT — clear of TEN's
> 9/10 report. Both scheduled reminders were moved to match. Every 9/06 → 9/12 and 9/08 → 9/14
> substitution below is mechanical; the +54h arithmetic is unchanged.

# Healthchecks ping-gap drill — armed 2026-09-12, page expected 2026-09-14 (originally planned 9/06 → 9/08)

**Status:** SCHEDULED (dates picked by the agent at owner request 2026-09-02; owner arms and
restores — the mechanism edits `~/.config/crude-tanker-fv.env`, which no agent may touch).
**Authority:** owner ruling 2026-09-02 Q-10 ("accept all Q recs" → *yes — name the two days*);
the Stage-0 → Stage-A gate in `decisions/autopilot_authority_2026-09-02.md` §6.
**Supersedes:** the 2026-07-13 drill (`decisions/wo2_pinggap_drill_2026-07-13.md`, deleted in the
F6 write-off, recoverable at `git show c3c25ab^:decisions/wo2_pinggap_drill_2026-07-13.md`) —
armed 7/13, never completed, receipt `healthchecks_firing_demonstrated` sat null for seven weeks.
**This is the one control the repo claims and has never demonstrated.** README says notifier death
is "detectable by absence"; nothing on file proves the absence channel ever fired. Until it does,
every unattended lane rests on a watcher of unknown liveness.

## Why these two dates

| Constraint | Effect |
|---|---|
| CMBT 9/03 · Stage-B window closes 9/04 · R4 executes 9/04-05 (PLAN) | Drill must start **after** 9/05 — the dead-man is deliberately down during the gap, and three FV-moving events is the wrong week to lose the backstop |
| TEN reports 9/10 pre-open (confirmed, issuer PR) | Drill must be **restored before** 9/10; an open earnings window is when `FETCH-FAILED` promotes straight to a page |
| Mon 9/07 is US Labor Day (markets closed) | A page landing that day risks an owner who is away — criterion 2 needs a live ack |
| Page fires at last-ping + period + grace = **+54h** (Period 1 day, Grace 30h per the 7/13 record) | Arming Saturday morning puts the page on Monday afternoon, inside the free window |

**ARM: Saturday 2026-09-12, after that morning's 08:15 sentinel run has logged `PING-SENT`.**
(Arming *before* the run makes Saturday 08:15 the last ping and drags the page onto Labor Day.)
**PAGE + RESTORE: Monday 2026-09-14, page expected ≈ 14:15 EDT.**

Gap length ≈ 54 hours, entirely inside the 9/12–9/15 window (post-TEN). If R4 slips past 9/05, slip
both dates by the same number of days — the ordering constraint is what matters, not the dates.

## Do this first (it removes the drill's own risk)

Set the repo secret `SENTINEL_LITE_HC_URL` **before** arming. The GitHub Action `sentinel-lite`
runs the pure sentinel daily against pushed state and pings its own healthchecks check — but the
secret is unset, so that backstop is itself unmonitored (`sentinel-lite.yml` prints "ping skipped"
to the run log and nowhere else). Setting it means the drill window has an independent watcher
instead of none. This is a Stage-0 owner act already owed; doing it here is free.

## Mechanism (unchanged from 7/13 — it worked, it just was never finished)

Comment the `CRUDE_FV_HEALTHCHECK_URL` line in `~/.config/crude-tanker-fv.env` with a DRILL-GAP
marker. **The sentinel is NOT muted:** it keeps running at 08:15, keeps evaluating every check and
keeps emailing the daily digest. Only the dead-man ping is withheld (the run logs `PING-SKIPPED`).

```
# DRILL-GAP 2026-09-12 -> 2026-09-14 (decisions/healthchecks_pinggap_drill_2026-09-06.md)
# export CRUDE_FV_HEALTHCHECK_URL=...
```

Restore = delete the two marker lines, uncomment, then run the sentinel once and confirm
`PING-SENT` and the check back UP:

```
cd ~/Projects/crude-tanker-fv && PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.sentinel --log state/sentinel.log --notify --ping
```

## Success criteria

1. **Firing demonstrated** — the healthchecks "down" email arrives ≈ 2026-09-14 14:15 EDT. Record
   the ACTUAL arrival time below. A page that never arrives is the finding: the absence channel is
   not wired, and every "detectable by absence" claim in README must be struck.
2. **Ack latency** — owner acks; record page→ack. One-time channel-latency measurement, explicitly
   **not** a standing SLA.
3. **Restore** — `PING-SENT` and the check returns UP; record the time.

## Evidence is mechanical now (this is what changed since 7/13)

The 7/13 drill's receipt lived in a hand-edited YAML that was never filled. Since Stage 0
(2026-09-02) every ping outcome is written to `state/ping_status.json` (`status`, `detail`,
`consecutive_4xx`, timestamp), so the drill leaves its own trace: `SENT` before the arm,
`SKIPPED` through the gap, `SENT` again at restore. Two consecutive 4xx additionally mark the
`healthchecks` surface in `state/reauth/` and page `REAUTH-NEEDED` — so a dead check URL is now a
detected condition rather than a line in a cron log.

Read the trace at any point with:

```
cd ~/Projects/crude-tanker-fv && cat state/ping_status.json && ls state/reauth/ 2>/dev/null
```

## Risk accepted for the window

A REAL sentinel death during the gap would be masked by the drill — both look like silence.
Three mitigations: (a) the daily digest keeps arriving, so a **missing digest during the window IS
the real-failure tell**; (b) the `sentinel-lite` Action keeps running off-machine, and with its
secret set it has its own dead-man; (c) the window is 54 hours and contains no earnings event.

## Outcome

_pending — fill at page + restore._

- Armed (actual): _______
- Page received (actual): **2026-09-13 13:15:09 EDT** (2026-09-13T17:15:09Z), subject `DOWN |
  crude-fv-sentinel` — a full day EARLIER than the 2026-09-14 ≈17:15 EDT expectation, because the
  grace is 2h, not the 30h the 7/13 record claimed. See the Drill log entry below.
- Ack: _______
- Restored + PING-SENT: _______
- Verdict: _______  → if PASS, this closes the Stage-0 → Stage-A gate item; if FAIL, the absence
  channel is not real and README's detectability claim gets struck before Stage A ships.

## Drill log

- ARMED 2026-09-12T14:07:54-04:00 — last SENT ping 2026-09-12T15:15:09+00:00 (11:15 EDT); page
  expected ≈ +54h (Period 1d + Grace 30h) ≈ Monday 2026-09-14 17:15 EDT. (The ≈14:15 EDT above
  assumed an 08:15 EDT sentinel run; the launchd sentinel actually pings at 11:15 EDT / 15:15Z,
  so the page lands three hours later than the doc's estimate. Still inside the Monday window.)
- RESTORE task moved 2026-09-12 to Monday 18:45 EDT (was 15:20 EDT, which would have run BEFORE the
  ≈17:15 EDT page and recorded a false NOT RECEIVED); the task now also commits its own doc line.
- **PAGE RECEIVED 2026-09-13T17:15:09Z (Sun 13:15:09 EDT)** — "The check `crude-fv-sentinel` has
  gone down. Reason: success signal did not arrive on time, grace time passed." Body: Period 1 day,
  Last ping 1 day 2 hours ago, "Status changed to down at: Sun, 13 Sep 2026 13:15:09 -0400".
  Criterion 1 PASSES: the absence channel fires. Firing is demonstrated for the first time; the
  README "detectable by absence" claim stands.
- **The +54h arithmetic did NOT hold — it was 26h.** Last SENT ping 2026-09-12T15:15:09Z → page
  2026-09-13T17:15:09Z is exactly **26h00m** = Period 1d + Grace **2h**. The doc's "Grace 30h per
  the 7/13 record" was wrong (30h ≠ the check's live setting), so every date in this plan was built
  on a 28-hour overestimate. Consequence: the page landed Sunday afternoon, not Monday — one day
  inside the window rather than at its end, and the whole Labor-Day-avoidance reasoning above was
  solving a constraint that never bound. **Anyone reusing this drill: read Grace off the check
  itself, do not inherit it from a prior record.** The practical rule going forward is
  last-ping + ~26h, i.e. a withheld ping pages the NEXT day, not the day after.
- Gap was real from the repo's own trace: `state/ping_status.json` read
  `{"ts":"2026-09-14T15:15:12+00:00","status":"WITHHELD","detail":"drill armed"}`, and
  `state/automation_runs.log` shows the sentinel RAN on both gap days —
  `2026-09-13T15:15:03Z job=sentinel outcome=flags rc=2` and `2026-09-14T15:15:05Z job=sentinel
  outcome=flags rc=2`. The checks kept evaluating; only the ping was withheld, exactly as designed.
  The 2026-09-12 run pinged normally (it preceded the 14:07 arm) — that ping is the one healthchecks
  counted down from.
- **RESTORED 2026-09-15 morning EDT** (marker `state/drill_armed` deleted; evidenced between the
  last logged run `2026-09-15T13:30:39Z` and that day's 15:15Z sentinel — the commit timestamp of
  this line is the exact record). The restore ran ~15h after its scheduled Monday 18:45 EDT slot:
  the Mac was dark from 2026-09-14T22:20Z to 2026-09-15T13:30Z (log gap), so the task fired on wake.
  No ping was forced by hand; the next scheduled sentinel (2026-09-15 11:15 EDT / 15:15Z) resumes
  pinging and healthchecks recovers on its own. Total withheld-ping gap ≈ 72h (2026-09-12 15:15Z →
  2026-09-15 15:15Z), of which the check was DOWN for ~46h.
- Ack: not recorded by this task — the page arrived Sunday; owner ack latency (criterion 2) is
  unmeasured and stays open.
- Verdict: **PASS on criterion 1 (firing demonstrated) and criterion 3 (restore), with a correction
  to the timing model.** The one control the repo claimed and had never demonstrated is now
  demonstrated. Two residual items for the owner: (a) criterion 2 (ack latency) was not captured;
  (b) the page body reported "dav204@gmail.com: **2 checks down**" — only one of those is this
  drill, so a second healthchecks check (plausibly the `sentinel-lite` check whose
  `SENTINEL_LITE_HC_URL` secret is still unset per "Do this first" above) has been sitting down
  outside the drill. Worth a look; it is not a drill failure.
