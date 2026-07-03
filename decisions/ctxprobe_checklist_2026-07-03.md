# Execution-context probe — 7-day owner checklist (WO2 0.5)

**Why:** the whole fetch layer rides launchd on a shared family MacBook. Before the
schedules freeze (Phase 1/2), we MEASURE — not assume — what launchd actually does
under the machine's real usage: lid closed, another family profile switched in,
logged out, asleep at fire time. The load-bearing unknown is **fast-user-switching**
(does a background profile's agent still run, with network and secrets?). The
expected rule to confirm: **fast-user-switch, never log out; the dead-man covers
logged-out** — but the log decides, not the expectation.

## Install (owner, once — ~1 minute)

```
cp ~/Projects/crude-tanker-fv/scripts/ctxprobe/com.crude-tanker-fv.ctxprobe.plist ~/Library/LaunchAgents/
cp ~/Projects/crude-tanker-fv/scripts/ctxprobe/com.crude-tanker-fv.ctxprobe-load.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.crude-tanker-fv.ctxprobe.plist
launchctl load ~/Library/LaunchAgents/com.crude-tanker-fv.ctxprobe-load.plist
tail -2 ~/ctxprobe.log
```

The load twin fires immediately — the tail should show one fresh line. Hourly lines
follow at :07. Fields per line: `initiator console_user me switched_in
secs_since_wake default_route http_ok secrets_readable power`.

## The seven scenarios (any order; note the date you ran each)

| # | Scenario | Do | Assert in ~/ctxprobe.log | Observed (date + verdict) |
|---|----------|----|--------------------------|---------------------------|
| 1 | Baseline | Normal use, lid open, your profile active | Hourly lines, `switched_in=yes http_ok=yes secrets_readable=yes` | |
| 2 | Lid closed | Close the lid across ≥3 firing times (e.g. overnight on AC), then wake | **ONE coalesced line** shortly after wake (small `secs_since_wake`), not N backfilled lines | |
| 3 | Fast-user-switched | Switch to a family profile (don't log yours out) across ≥2 firing times | Lines KEEP COMING with `console_user=<other> switched_in=no`; check `http_ok`/`secrets_readable` — **this gates the schedule design** | |
| 4 | Logged out | Log your profile fully out across ≥2 firing times, log back in | **ZERO lines** during the gap, **no replay burst** after login (the -load twin fires once at login — expected) | |
| 5 | Shutdown | Full shutdown across a firing time, boot next morning | Zero lines while off; -load line at boot; hourly resumes | |
| 6 | Wake-race | Open the lid at ~:06 and watch the :07 firing | Line appears; if `default_route=no` or `http_ok=no` on that line, the 3×/30s fetch preamble (invariant 9) is confirmed necessary | |
| 7 | Untouched day | A day nobody opens the machine (lid closed, AC) | What arrives? (Darwin may fire on DarkWake/PowerNap or not at all) — this calibrates the DARK-digest expectation | |

## Close-out (owner + agent, after day 7)

1. Paste/summarize the log findings into the **measured-semantics note** below —
   this note is the design input that freezes the Phase 1/2 schedules.
2. Uninstall the harness:
   ```
   launchctl unload ~/Library/LaunchAgents/com.crude-tanker-fv.ctxprobe.plist
   launchctl unload ~/Library/LaunchAgents/com.crude-tanker-fv.ctxprobe-load.plist
   rm ~/Library/LaunchAgents/com.crude-tanker-fv.ctxprobe*.plist ~/ctxprobe.out ~/ctxprobe.err
   ```
3. Keep `~/ctxprobe.log` until the WO2 acceptance artifact is compiled (it is the
   ctxprobe appendix), then delete.

## Measured semantics (FILL AFTER THE WINDOW — committed before schedules freeze)

- Lid-closed firing behavior: _pending_
- Fast-user-switched: runs? network? secrets? — _pending_ ← **gates schedule design**
- Logged-out: _pending_
- Wake coalescing (N missed → how many fired): _pending_
- Wake-race window (secs after wake until net up): _pending_
- Confirmed operating rule: _pending_ (expected: fast-user-switch, never log out;
  the dead-man covers logged-out)
