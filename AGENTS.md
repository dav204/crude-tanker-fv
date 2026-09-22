# AGENTS.md

**The operating rules for this repo live in [CLAUDE.md](CLAUDE.md). Read that, then
[PLAN.md](PLAN.md), then start.** This file exists only so agents that look for `AGENTS.md`
by convention find their way there.

Deliberately a pointer and not a copy. This file arrived on 2026-09-21 as a 199-line
find-and-replace of CLAUDE.md, which introduced two problems:

1. **Two routers drift.** Both opened with "read this first, every session", and nothing kept
   them in sync. The repo has already paid for that failure mode once — the scheduler prompt
   and its prompt of record ran three hunks apart for two months (`monitor/PROMPT.md` notes the
   2026-09-10 re-sync). A rule fixed in one copy and not the other is worse than no rule.
2. **The copy's paths were wrong.** The replacement had rewritten `.claude/` to `.Codex/`
   throughout, so the three lines telling an agent where permission settings live pointed at a
   directory that does not exist — in the one area where a wrong path is most expensive.

If a tool genuinely needs the full text under this name, generate it from CLAUDE.md at build
time rather than committing a second copy, and do not rewrite the `.claude/` paths: they are
real directories, not a vendor label.
