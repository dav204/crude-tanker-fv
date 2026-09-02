# Healthchecks ping-gap drill — armed 2026-09-06, page expected 2026-09-08

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
| Page fires at last-ping + period + grace = **+54h** (Period 1 day, Grace 30h per the 7/13 record) | Arming Sunday morning puts the page on Tuesday afternoon, inside the free window |

**ARM: Sunday 2026-09-06, after that morning's 08:15 sentinel run has logged `PING-SENT`.**
(Arming *before* the run makes Saturday 08:15 the last ping and drags the page onto Labor Day.)
**PAGE + RESTORE: Tuesday 2026-09-08, page expected ≈ 14:15 EDT.**

Gap length ≈ 54 hours, entirely inside the 9/06–9/09 calendar hole. If R4 slips past 9/05, slip
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
# DRILL-GAP 2026-09-06 -> 2026-09-08 (decisions/healthchecks_pinggap_drill_2026-09-06.md)
# export CRUDE_FV_HEALTHCHECK_URL=...
```

Restore = delete the two marker lines, uncomment, then run the sentinel once and confirm
`PING-SENT` and the check back UP:

```
cd ~/Projects/crude-tanker-fv && PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.sentinel --log state/sentinel.log --notify --ping
```

## Success criteria

1. **Firing demonstrated** — the healthchecks "down" email arrives ≈ 2026-09-08 14:15 EDT. Record
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
- Page received (actual): _______  (expected 2026-09-08 ≈14:15 EDT)
- Ack: _______
- Restored + PING-SENT: _______
- Verdict: _______  → if PASS, this closes the Stage-0 → Stage-A gate item; if FAIL, the absence
  channel is not real and README's detectability claim gets struck before Stage A ships.
