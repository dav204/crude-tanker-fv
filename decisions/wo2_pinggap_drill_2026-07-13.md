# WO2 Phase-0 drill — deliberate dead-man ping gap (healthchecks firing demonstration)

**Started:** 2026-07-13 ~10:00 ET (owner: "Run the drills"). **Mechanism:** the
`CRUDE_FV_HEALTHCHECK_URL` line in `~/.config/crude-tanker-fv.env` is COMMENTED with a
DRILL-GAP marker — the sentinel keeps running and emailing on its 08:15 schedule (runs log
PING-SKIPPED), only the dead-man ping is withheld. The sentinel is NOT muted during the drill.

**Last successful ping:** 2026-07-13 09:52 ET (the PING-SENT receipt run).
**Expected page:** check `crude-fv-sentinel` (Period 1 day, Grace 30 h) goes DOWN and emails
dav204@gmail.com at ~**Wed 2026-07-15 15:52 ET** (09:52 + 24h period + 30h grace).

**Success criteria (→ `wo2_acceptance_receipts.yaml`):**
1. `healthchecks_firing_demonstrated` — the page email arrives ≈ on schedule (record actual time).
2. `page_ack_demonstrated` — owner acks the page; record page→ack timestamps (one-time channel-
   latency demo, NOT a standing SLA).
3. RESTORE: uncomment the env line, re-run the sentinel, confirm PING-SENT + check back UP.
   Record the restore time here.

**Risk accepted for the window:** a REAL sentinel death during the gap would be masked by the
drill (both look like silence). Mitigation: the sentinel's daily flag digests keep arriving by
email during the drill — a missing daily digest during the window IS the real-failure tell.

**Outcome:** _pending — fill at page + restore._
