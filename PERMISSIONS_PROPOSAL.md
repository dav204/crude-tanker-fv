# Claude Code permission allowlist — proposal (DRAFT, not yet applied)

Status: **proposal for review** — no settings file has been written.
Drafted 2026-06-12 from a full inventory of CLAUDE.md workflows, the
`/reconcile`–`/add-ticker`–`/news-pull` commands, `scripts/`, `pyproject.toml`,
the network-touching modules (`price_refresh.py`, `sp_scan.py`,
`rocketchat_api.py` / `ingest_rocketchat.py`), `inputs/data_sources.yaml`,
and `outputs/pareto_daily_links.json`.

Goal: long autonomous sessions where the constant, git-reversible,
read-only operations never prompt, while anything that leaves the
machine, touches credentials, or crosses a human-only promotion boundary
still does.

---

## 1. Operation inventory

### Shell commands (frequency per CLAUDE.md workflows)

| Command | Source | Frequency / nature |
|---|---|---|
| `PYTHONPATH=src .venv/bin/python -m pytest -q` | verification loop | Constant; read-only |
| `… -m crude_tanker_fv.reconcile <args>` | `/reconcile` (its `allowed-tools` line already permits this exact form) | Constant; writes `state/last_reconcile.json` |
| `… -m crude_tanker_fv.pipeline <QUARTER>` | verification loop | Every change-verify cycle; writes `outputs/**` (git-tracked) |
| `… -m crude_tanker_fv.refresh` | preflight | Frequent; read-only |
| `… -m crude_tanker_fv.sp_scan` (`--names`, `--since`, `--links`) | onboarding step 3, quarterly habit | Frequent; local PDF parsing only |
| `… -m crude_tanker_fv.sp_scan --fetch-links` | weekly chain | **Network** — downloads FactSet/BlueMatrix/urldefense tracked links |
| `… -m crude_tanker_fv.price_refresh` | daily refresh | Network GET to Yahoo; writes the automation-writable `prices_daily.yaml` |
| `… -m crude_tanker_fv.ffa_ocr` / `pareto_archive` | weekly chain | Occasional; local |
| `… -m crude_tanker_fv.ingest_rocketchat` | weekly chain | **Authenticated network** (PAT from `~/.config/crude-tanker-fv.env`) |
| `ruff check` | pyproject dev dep | Occasional; read-only |
| `git status/diff/log/show/add/commit/branch` | everywhere | Constant; local + reversible |
| `git push -u origin <branch>` | week-close checklist | Occasional; **leaves the machine** |
| `curl -sSL <url> -o /tmp/x.pdf` + `.venv/bin/python -c "from pypdf…"` | IR-PDF gotcha pattern | Recurring but ad-hoc URLs; `python -c` = arbitrary code |
| `launchctl` / plist install | scripts/*.plist | Rare; system state |

### External hostnames (exact, from code and data files)

- **In code:** `query1.finance.yahoo.com` (price_refresh CHART_URL),
  `rc.seekingalpha.com` (Rocket.Chat, authed), `parp.hosting.factset.com` +
  `urldefense.com` + BlueMatrix (sp_scan `--fetch-links` via
  `unwrap_tracked_url`).
- **WebFetch/curl research targets** (`data_sources.yaml` + CLAUDE.md):
  `www.sec.gov` (EDGAR), `compassmar.com`, and the IR sites —
  `www.dhtankers.com`, `www.okeanisecotankers.com` (TLS broken; curl only),
  `www.frontline.bm`, `www.intlseas.com`, `www.teekay.com`, `www.nat.bm`,
  `www.flexlng.com`, `www.capclnenrg.com`, `ardmoreshipping.com`,
  `www.hafniabw.com`, `www.torm.com`, `www.scorpiotankers.com`,
  `www.tenn.gr` (blocks agent fetching), `www.starbulk.com`,
  `www.gencoshipping.com`, `www.costamarebulkers.com`,
  `www.capitaltankers.com`; one `docs.google.com` tracking spreadsheet.

### Paths written

`outputs/**` (reports, digests, review queues — git-tracked),
`state/**` (cursors, OCR scratch — mostly gitignored), `inputs/**`
(the data layer), `decisions/*.md`, the root markdown docs, `src/`,
`tests/`. All inside the repo, all git-reversible. The one
read-sensitive path is `~/.config/crude-tanker-fv.env` (secrets,
deliberately outside the repo).

---

## 2. Classification

- **SAFE_REPEAT (allowlist):** pytest, reconcile, pipeline, refresh,
  sp_scan local modes, price_refresh, ruff, read-only git + add/commit,
  edits to repo artifact trees, WebFetch GETs to the sec.gov/IR/Compass
  set.
- **OCCASIONAL (leave to auto mode / normal prompting):** ffa_ocr,
  pareto_archive, the `scripts/*.py` diagnostics,
  `build_methodology_pdf.sh`, `python -c` pypdf one-liners, curl to
  ad-hoc URLs.
- **SENSITIVE (ask or deny):** `git push`, `sp_scan --fetch-links`,
  `ingest_rocketchat`, anything credential-shaped (read OR write),
  `launchctl`, `rm -rf`, edits to the three human-only promotion
  surfaces (watchlist vintage, `transactions/<class>.yaml`,
  `ffa_forward_curve.yaml`), and any brokerage-MCP order placement
  (see open question 4).

---

## 3. Proposed settings JSON (draft)

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
      "Bash(PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.sp_scan --fetch-links:*)",
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

Rule precedence is deny > ask > allow, which several rules below rely on.

---

## 4. Reasoning per rule group

**Python invocations are pinned to the exact documented form**
(`PYTHONPATH=src .venv/bin/python -m <module>`), matching the
`/reconcile` command's existing `allowed-tools` line and the CLAUDE.md
rule that pytest is never run without `PYTHONPATH=src`. This deliberately
does **not** match bare `python`, `python -c`, or `pip` — `python -c` is
arbitrary code execution and cannot be narrowed, so it stays in auto
mode (see open question 3 for the wrapper-script alternative).

**`sp_scan` exploits ask-over-allow precedence.** The allow covers the
local modes (base scan, `--names`, `--links`) that fire constantly
during onboarding and quarterly sweeps; the more-specific
`--fetch-links` ask rule wins over the allow, so the only
network-downloading mode still prompts. Same logic for
`ingest_rocketchat` — it authenticates with a PAT and should never fire
silently in an unattended session.

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

The permission prompt becomes a mechanical backstop for rules that are
currently discipline-only. `src/`, `tests/`, and the root markdown docs
are left to normal/auto mode — edited often, but a prompt there is cheap
relative to churn, and keeping the allow surface narrow was the brief.

**WebFetch allows are exactly the hostnames in `data_sources.yaml` +
CLAUDE.md** — all read-only GET research targets. Two deliberate
exclusions:

- `rc.seekingalpha.com` is **denied** for WebFetch so a fetch never
  carries the Rocket.Chat origin; all RC access goes through the ingest
  script, which sources credentials properly.
- `parp.hosting.factset.com` / `urldefense.com` are **not** allowlisted:
  those tracked-download URLs embed long-lived tokens (effectively
  credentials) and are fetched by `sp_scan --fetch-links`, which
  prompts.

**`git push` is ask, not allow** — it leaves the machine, and the
week-close checklist treats pushing as a deliberate event. Read-only git
plus `add`/`commit` are allowed since commits are local and reversible.

**Deny rules mirror the `.gitignore` secrets patterns** (`*_token*`,
`*_credentials*`, `*_secret*`, `.env*`) plus the actual secrets file at
`~/.config/crude-tanker-fv.env`. The rocketchat_token.rtf incident
(2026-06-09) says credential-shaped files are this repo's real risk
class; the deny makes the gate mechanical instead of discipline-only.

`Bash(rm -rf:*)` deny is a cheap backstop, not a security boundary
(trivially bypassed by other spellings); the real protection for the
data layer is git.

---

## 5. Open questions (decide before writing the file)

1. **Tracked vs local file.** The `.gitignore` comment says permission
   allowances live in `.claude/settings.local.json` (untracked) while
   only `commands/` is shared; the request was for `.claude/settings.json`
   (tracked, team-wide). Which scope — and if tracked, should the
   ask carve-outs (watchlist / transactions / FFA curve) ship as shared
   policy?
2. **`git push`: ask vs narrow allow.** In the remote-execution
   environment work pushes to `claude/...` branches, so an allow like
   `Bash(git push -u origin claude/:*)` plus ask on everything else is
   an option; on the local Mac the week-close push is `origin main`.
   Keep it ask everywhere for simplicity?
3. **The curl + pypdf PDF pattern can't be allowlisted narrowly** —
   `curl` to arbitrary URLs can also POST data out, and `python -c` is
   arbitrary code. If prompts annoy in long sessions, the clean fix is a
   small `scripts/fetch_pdf.py <url> <out>` wrapper that refuses hosts
   not in `data_sources.yaml`; then a single narrow Bash allow covers
   it. Build that as a follow-up?
4. **MCP servers.** The drafting session had a brokerage connector
   exposing `create_order_instruction` / `delete_order_instruction`
   (live order placement) and an email-draft server attached. For
   autonomous sessions the order tools should be hard-denied
   (`mcp__<server>__create_order_instruction`) and email drafts /
   GitHub writes put under ask — but those servers registered under
   session-specific UUID names, so stable rules need the names they use
   in the real setup. What do the brokerage and email servers register
   as locally? Leaving live order placement reachable in an unattended
   session is the single biggest risk on this list.
5. **`scripts/*.py` diagnostics and `build_methodology_pdf.sh`** look
   rare enough to leave to auto mode — confirm, or they can get narrow
   allows too.
