# Claude Code permission allowlist — decision record

Status: **APPLIED 2026-06-12** — `.claude/settings.json` (tracked) carries
the rules below. Drafted 2026-06-12 from a full inventory of CLAUDE.md
workflows, the `/reconcile`–`/add-ticker`–`/news-pull` commands,
`scripts/`, `pyproject.toml`, the network-touching modules
(`price_refresh.py`, `sp_scan.py`, `rocketchat_api.py` /
`ingest_rocketchat.py`), `inputs/data_sources.yaml`, and
`outputs/pareto_daily_links.json`; revised after owner review (all five
open questions resolved — see §6).

Goal: long autonomous sessions where the constant, git-reversible,
read-only operations never prompt, while anything that leaves the
machine, touches credentials, or crosses a human-only promotion boundary
still does.

---

## 0. Two caveats to read first (owner amendments, 2026-06-12)

**Bash permission rules are prefix matchers.** A rule like
`Bash(...sp_scan --fetch-links:*)` only matches when `--fetch-links` is
the first argument; `sp_scan --since X --fetch-links` slips past it into
any open-ended allow. This applies to BOTH allow and ask rules — carving
a network flag out of an allowed module is unreliable in either
direction. The fix applied here is structural: the network download was
moved out of `sp_scan` into its own module (`crude_tanker_fv.fetch_links`,
2026-06-12), so every `sp_scan` mode is local-only and `sp_scan:*` is
safe to allow. The general rule: never allowlist an open-ended prefix on
a module whose network behaviour is flag-gated — split the module.

**File rules only govern the agent's file tools.** The
`Read(~/.config/crude-tanker-fv.env)` deny stops the Read tool;
`Bash(cat ~/.config/crude-tanker-fv.env)` is a different tool and sails
past it. Same for the Edit carve-outs vs `sed -i`. These rules are
guardrails against drift — defense in depth on top of auto mode's
classifier, which is what actually watches the bash side — not security
boundaries. The same honesty applies to `Bash(rm -rf:*)`: a backstop,
trivially bypassed by other spellings. The real protection for the data
layer is git.

---

## 1. Operation inventory

### Shell commands (frequency per CLAUDE.md workflows)

| Command | Source | Frequency / nature |
|---|---|---|
| `PYTHONPATH=src .venv/bin/python -m pytest -q` | verification loop | Constant; read-only |
| `… -m crude_tanker_fv.reconcile <args>` | `/reconcile` (its `allowed-tools` line already permits this exact form) | Constant; writes `state/last_reconcile.json` |
| `… -m crude_tanker_fv.pipeline <QUARTER>` | verification loop | Every change-verify cycle; writes `outputs/**` (git-tracked) |
| `… -m crude_tanker_fv.refresh` | preflight | Frequent; read-only |
| `… -m crude_tanker_fv.sp_scan` (`--names`, `--since`, `--links`, `--full`) | onboarding step 3, quarterly habit | Frequent; local-only by construction since 2026-06-12 |
| `… -m crude_tanker_fv.fetch_links` | weekly chain (was `sp_scan --fetch-links`) | **Network** — downloads FactSet/BlueMatrix/urldefense tracked links |
| `… -m crude_tanker_fv.price_refresh` | daily refresh | Network GET to Yahoo; writes the automation-writable `prices_daily.yaml` |
| `… -m crude_tanker_fv.ffa_ocr` / `pareto_archive` | weekly chain | Occasional; local |
| `… -m crude_tanker_fv.ingest_rocketchat` | weekly chain | **Authenticated network** (PAT from `~/.config/crude-tanker-fv.env`) |
| `.venv/bin/python scripts/fetch_pdf.py <url>` | IR-PDF workflow (replaces ad-hoc curl) | Recurring; host-validated against `data_sources.yaml` in code |
| `ruff check` | pyproject dev dep | Occasional; read-only |
| `git status/diff/log/show/add/commit/branch` | everywhere | Constant; local + reversible |
| `git push -u origin <branch>` | week-close checklist | Occasional; **leaves the machine** |
| `python -c "from pypdf…"` one-liners | PDF text extraction | Arbitrary code; stays in auto mode by design |
| `launchctl` / plist install | scripts/*.plist | Rare; system state |

### External hostnames (exact, from code and data files)

- **In code:** `query1.finance.yahoo.com` (price_refresh CHART_URL),
  `rc.seekingalpha.com` (Rocket.Chat, authed), `parp.hosting.factset.com`
  + `urldefense.com` + BlueMatrix (`fetch_links` via
  `unwrap_tracked_url`).
- **WebFetch/fetch_pdf research targets** (`data_sources.yaml` +
  CLAUDE.md): `www.sec.gov` (EDGAR), `compassmar.com`, and the IR sites —
  `www.dhtankers.com`, `www.okeanisecotankers.com` (TLS broken;
  fetch_pdf.py carries the audited exception), `www.frontline.bm`,
  `www.intlseas.com`, `www.teekay.com`, `www.nat.bm`, `www.flexlng.com`,
  `www.capclnenrg.com`, `ardmoreshipping.com`, `www.hafniabw.com`,
  `www.torm.com`, `www.scorpiotankers.com`, `www.tenn.gr` (blocks agent
  fetching), `www.starbulk.com`, `www.gencoshipping.com`,
  `www.costamarebulkers.com`, `www.capitaltankers.com`; one
  `docs.google.com` tracking spreadsheet.

### Paths written

`outputs/**` (reports, digests, review queues — git-tracked),
`state/**` (cursors, OCR scratch — mostly gitignored), `inputs/**`
(the data layer), `decisions/*.md`, the root markdown docs, `src/`,
`tests/`. All inside the repo, all git-reversible. The one
read-sensitive path is `~/.config/crude-tanker-fv.env` (secrets,
deliberately outside the repo).

---

## 2. Classification

- **SAFE_REPEAT (allowlisted):** pytest, reconcile, pipeline, refresh,
  sp_scan (all modes now local), price_refresh, fetch_pdf.py (the
  allowlist lives in its code), ruff, read-only git + add/commit, edits
  to repo artifact trees, WebFetch GETs to the sec.gov/IR/Compass set.
- **OCCASIONAL (auto mode / normal prompting):** ffa_ocr,
  pareto_archive, the `scripts/*.py` diagnostics,
  `build_methodology_pdf.sh`, `python -c` pypdf one-liners.
- **SENSITIVE (ask or deny):** `git push`, `fetch_links`,
  `ingest_rocketchat`, raw `curl` (can POST data out), anything
  credential-shaped (read OR write), `launchctl`, `rm -rf`, edits to the
  three human-only promotion surfaces (watchlist vintage,
  `transactions/<class>.yaml`, `ffa_forward_curve.yaml`). Live brokerage
  MCP access is handled by detachment, not rules — see §6 Q4.

---

## 3. The applied rules (`.claude/settings.json`)

```json
{
  "permissions": {
    "allow": [
      "Bash(PYTHONPATH=src .venv/bin/python -m pytest:*)",
      "Bash(PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.reconcile:*)",
      "Bash(PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.pipeline:*)",
      "Bash(PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.refresh:*)",
      "Bash(PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.sp_scan:*)",
      "Bash(PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.price_refresh:*)",
      "Bash(.venv/bin/python scripts/fetch_pdf.py:*)",
      "Bash(.venv/bin/ruff check:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(git show:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git branch:*)",
      "WebFetch(domain:www.sec.gov)",
      "WebFetch(domain:compassmar.com)",
      "WebFetch(domain:www.dhtankers.com)",
      "WebFetch(domain:www.okeanisecotankers.com)",
      "WebFetch(domain:www.frontline.bm)",
      "WebFetch(domain:www.intlseas.com)",
      "WebFetch(domain:www.teekay.com)",
      "WebFetch(domain:www.nat.bm)",
      "WebFetch(domain:www.flexlng.com)",
      "WebFetch(domain:www.capclnenrg.com)",
      "WebFetch(domain:ardmoreshipping.com)",
      "WebFetch(domain:www.hafniabw.com)",
      "WebFetch(domain:www.torm.com)",
      "WebFetch(domain:www.scorpiotankers.com)",
      "WebFetch(domain:www.tenn.gr)",
      "WebFetch(domain:www.starbulk.com)",
      "WebFetch(domain:www.gencoshipping.com)",
      "WebFetch(domain:www.costamarebulkers.com)",
      "WebFetch(domain:www.capitaltankers.com)",
      "WebFetch(domain:query1.finance.yahoo.com)",
      "Edit(outputs/**)",
      "Edit(state/**)",
      "Edit(decisions/**)",
      "Edit(inputs/**)"
    ],
    "ask": [
      "Bash(PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.fetch_links:*)",
      "Bash(PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.ingest_rocketchat:*)",
      "Bash(git push:*)",
      "Bash(curl:*)",
      "Bash(launchctl:*)",
      "Edit(inputs/watchlist.yaml)",
      "Edit(inputs/market_data/transactions/**)",
      "Edit(inputs/market_data/ffa_forward_curve.yaml)"
    ],
    "deny": [
      "Read(~/.config/crude-tanker-fv.env)",
      "Read(.env*)",
      "Read(**/*_token*)",
      "Read(**/*_credentials*)",
      "Read(**/*_secret*)",
      "Bash(rm -rf:*)",
      "WebFetch(domain:rc.seekingalpha.com)"
    ]
  }
}
```

Rule precedence is deny > ask > allow.

---

## 4. Reasoning per rule group

**Python invocations are pinned to the exact documented form**
(`PYTHONPATH=src .venv/bin/python -m <module>`), matching the
`/reconcile` command's existing `allowed-tools` line and the CLAUDE.md
rule that pytest is never run without `PYTHONPATH=src`. This deliberately
does **not** match bare `python`, `python -c`, or `pip` — `python -c` is
arbitrary code execution and cannot be narrowed, so it stays in auto
mode.

**`sp_scan:*` is allowed because it is now structurally network-free**
(§0, first caveat). The download step is its own module under ask. The
original draft's flag-based carve-out was order-sensitive and is
documented here as an anti-pattern.

**`scripts/fetch_pdf.py` is the curl replacement** — an allowlist
controlled in code rather than config. It refuses any host not in
`inputs/data_sources.yaml` (+ Compass) before connecting, enforces
https, restricts output to /tmp or the repo, and carries the single
audited TLS-verification exception for `www.okeanisecotankers.com`.
Raw `curl` stays under ask: it reaches arbitrary URLs and can POST data
out, so it prompts.

**`price_refresh` is allowed despite touching the network and a
pipeline-loaded YAML** because it is GET-only to a single Yahoo endpoint
and its own design (sanity flags; >15%-day-move / >30%-vs-static quotes
written but never applied; the vintage rule) makes `prices_daily.yaml`
the one automation-writable input by explicit owner decision
(2026-06-10).

**Edits:** `outputs/`, `state/`, `decisions/` are pure artifact/log
trees — trivially git-reversible and written on every pipeline run.
`inputs/**` is allowed broadly **except** three ask carve-outs that map
one-to-one onto the repo's human-only promotion rules:

- `inputs/watchlist.yaml` — the vintage-rebase rule (the TEN $44
  incident: a price must never move without rebasing `consensus_pnav` /
  `consensus_fwd_pe` from the same vintage);
- `inputs/market_data/transactions/**` — print promotion is
  human-classified and triggers the prints→rerun→drift loop;
- `inputs/market_data/ffa_forward_curve.yaml` — promotion is HUMAN-ONLY
  per CLAUDE.md.

The permission prompt becomes a mechanical backstop for rules that were
previously discipline-only (subject to the §0 second caveat: it guards
the file tools, not `sed` via Bash). `src/`, `tests/`, and the root
markdown docs are left to normal/auto mode — edited often, but a prompt
there is cheap relative to churn.

**WebFetch allows are exactly the hostnames in `data_sources.yaml` +
CLAUDE.md** — all read-only GET research targets. Two deliberate
exclusions:

- `rc.seekingalpha.com` is **denied** for WebFetch so a fetch never
  carries the Rocket.Chat origin; all RC access goes through the ingest
  script, which sources credentials properly.
- `parp.hosting.factset.com` / `urldefense.com` are **not** allowlisted:
  those tracked-download URLs embed long-lived tokens (effectively
  credentials) and are fetched by `fetch_links`, which prompts.

**`git push` is ask everywhere** — it leaves the machine, and the
week-close push is a deliberate ritual; one prompt a week costs nothing
(owner decision; the branch-pattern allow alternative was rejected as
complexity buying almost no friction reduction). Read-only git plus
`add`/`commit` are allowed since commits are local and reversible.

**Deny rules mirror the `.gitignore` secrets patterns** (`*_token*`,
`*_credentials*`, `*_secret*`, `.env*`) plus the actual secrets file at
`~/.config/crude-tanker-fv.env`. The rocketchat_token.rtf incident
(2026-06-09) says credential-shaped files are this repo's real risk
class; the deny makes the gate mechanical instead of discipline-only —
within the limits stated in §0.

---

## 5. Post-write verification checklist (run in a live interactive session)

Five minutes of red-teaming the config before the first long run — same
spirit as the 11-query validation suite. Each of these should PROMPT
(or be refused):

1. `git push` → ask.
2. Edit `inputs/watchlist.yaml` via the Edit tool → ask.
3. `PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.fetch_links` → ask.
4. `curl -sSL https://example.com` → ask.
5. Read `~/.config/crude-tanker-fv.env` via the Read tool → denied.
6. `.venv/bin/python scripts/fetch_pdf.py https://evil.example/x.pdf` →
   allowed to RUN but the script refuses the host (code-level gate).

And each of these should NOT prompt:

7. `PYTHONPATH=src .venv/bin/python -m pytest -q`.
8. `PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.sp_scan --since
   2026-06-01 --names DHT` (the reordered-flags case that motivated the
   module split — safe now because no sp_scan mode touches the network).
9. Edit `outputs/delta_report.md`.
10. WebFetch `https://www.sec.gov/...`.

Note: the historical reorder probe `sp_scan --since X --fetch-links` now
errors out in argparse (unknown flag) — the right failure mode.

---

## 6. Resolved questions (owner decisions, 2026-06-12)

1. **Tracked vs local → TRACKED.** One-person repo; the ask carve-outs
   are policy and deserve version history alongside CLAUDE.md.
   `.claude/settings.local.json` (gitignored) is for ephemeral
   "don't ask again" accumulation only.
2. **`git push` → ask everywhere.** The week-close push is a deliberate
   ritual; the branch-pattern allow was rejected as complexity for
   negligible friction reduction.
3. **fetch_pdf.py wrapper → built** (`scripts/fetch_pdf.py`). Also
   motivated the fetch_links module split and absorbed the Okeanis
   broken-TLS handling into one audited place.
4. **Brokerage MCP → detach, don't deny.** Owner decision, stronger than
   the draft: the shipping repo needs zero live brokerage access (prices
   come from Yahoo, positions from YAML), so `create_order_instruction`
   being *reachable* in an unattended session is a capability that
   shouldn't exist in this context, not a risk to mitigate with rules.
   **Owner action, outside this repo:** check `/mcp` in a session; if
   the IBKR connector is configured at user scope, scope it out of this
   project. Same logic, softer, for email-draft servers. No MCP rules in
   settings.json — rules would mask the real fix and the server names
   are deployment-specific anyway.
5. **Diagnostics scripts → auto mode.** Rare prompts are fine.
