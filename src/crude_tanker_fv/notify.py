"""Email notification (WO2 Phase 0.1, 2026-07-03) — the only outbound channel.

Design (plan §3.1): email to the OWNER ONLY (CRUDE_FV_SMTP_TO), stdlib
smtplib + STARTTLS, creds env-only from ~/.config/crude-tanker-fv.env.
Two routes, both defined in inputs/notify.yaml: PAGE (immediate) and DIGEST
(one daily status email, sent on OK days too). A send failure is RECORDED
(state/notify_down.log), never retried into a loop — the healthchecks ping is
withheld unless a run's email actually sent (invariant 2), so notifier death
pages through healthchecks' own independent channel.

  python -m crude_tanker_fv.notify --doctor          # secrets perms + config
  python -m crude_tanker_fv.notify --verify-notify   # one test send
"""

from __future__ import annotations

import argparse
import os
import re
import smtplib
import stat
import sys
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path

import yaml

from . import reauth
from .loaders import INPUTS_DIR

ENV_FILE = Path.home() / ".config" / "crude-tanker-fv.env"
REQUIRED_VARS = ("CRUDE_FV_SMTP_HOST", "CRUDE_FV_SMTP_USER",
                 "CRUDE_FV_SMTP_PASS", "CRUDE_FV_SMTP_TO")


def load_routes(inputs_dir: Path = INPUTS_DIR) -> dict:
    return yaml.safe_load((inputs_dir / "notify.yaml").read_text())


def load_env_file(path: Path = ENV_FILE, environ=None) -> dict:
    """The wrappers `source` the secrets file in shell; a scheduled-task session has no such
    wrapper, so the module loads it itself (KEY=VALUE, optional `export`, quotes stripped).
    Never overrides a variable already set; never prints a value. (2026-09-12, governor sends.)"""
    env = dict(os.environ if environ is None else environ)
    if not path.exists():
        return env
    for ln in path.read_text().splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#") or "=" not in ln:
            continue
        if ln.startswith("export "):
            ln = ln[len("export "):]
        k, _, v = ln.partition("=")
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and k not in env:
            env[k] = v
    return env


def smtp_status(environ=os.environ) -> dict:
    missing = [v for v in REQUIRED_VARS if not environ.get(v)]
    return {"configured": not missing, "missing": missing}


def route_flags(flags: list[str], routes: dict) -> "tuple[list[str], list[str]]":
    """Partition flags by leading tag into (page, digest). record_only tags are
    dropped here (they reach state via their writers). An UNKNOWN tag PAGES —
    a tag someone forgot to route must fail loud, not vanish into a digest."""
    digest_tags = set(routes["routes"]["digest"])
    record_tags = set(routes["routes"].get("record_only", []))
    # page_once tags are page-class here; sentinel.main demotes a repeat
    # sighting (same page_once_key) to the digest (2026-09-02).
    page, digest = [], []
    for f in flags:
        tag = f.split()[0]
        if tag in digest_tags:
            digest.append(f)
        elif tag not in record_tags:
            page.append(f)
    return page, digest


# What a PAGE asks of the owner (2026-09-11 ruling: a page means the owner's action is needed
# and the email must say what; agent-class work never pages). Keyed by tag; the page body
# prefixes each line with it. A tag with no entry here should not be routed to page.
PAGE_ACTIONS = {
    "FILING-QUEUE-INVALID": "OWNER — repair the malformed filing queue; pending work has not been discarded",
    "FILING-QUEUE-STALLED": "OWNER — restore the daily triage task; its pending queue is stalled",
    "SURFACE-INCOHERENT": "OWNER — a guard contradicted the published surface; the agent has halted. Read the named check and rule.",
    "FILING-OVERDUE": "OWNER — the issuer has not filed past its window and no sheet is on file. Decide: chase the issuer, or hold the name on its prior sheet.",
    "TRIGGER-DUE": "OWNER — an observable you registered is due. Record its outcome on the card (when this line names a DRAFT on file, read it first), or open a chat and say 'run the check'.",
    "FORK-OPENED": "OWNER (optional) — a recommendation was registered; it executes after the date shown unless you object in a chat. No action = it runs. A line marked NEEDS A CHAT is one the executor cannot land (code change): open a chat when you want it done.",
    "FORK-EXECUTABLE": "OWNER (optional) — the window closed; the executor runs it today (or a chat lands it, if marked). Nothing to do unless you object.",
    "DIRTY-TOO-LONG": "OWNER/AGENT — the working tree has been mid-surgery for days. Finish, stash, or say 'discard'.",
    "REAUTH-NEEDED": "OWNER — re-authenticate the named surface (a token or session expired); the agent cannot.",
    "TASK-PARKED": "OWNER — an unattended run is alive and blocked on a tool-permission prompt; only you can answer it. Answer or dismiss it, then check whether that task's grant belongs in the settings file in scope for its cwd — a prompt parks the run forever while the scheduler still reports it as running, and nothing it was going to write has landed.",
    "FETCH-FAILED": "OWNER — the fetch layer has been blind two runs in reporting season. Check the network or the credentials file.",
}


def page_action(flag: str) -> str:
    tag = flag.split()[0] if flag else ""
    if tag == "TRIGGER-DUE":
        ev = trigger_event(flag)
        return TRIGGER_ACTIONS[ev[0]] if ev else PAGE_ACTIONS[tag]
    return PAGE_ACTIONS.get(tag, "OWNER — (no action text registered for this tag; treat as: read and rule)")


TRIGGER_EVENT_RE = re.compile(r"\[[^\]]*\] (DUE|FIRED|BREACHED)(?: (\d{4}-\d{2}-\d{2}))? — ")

TRIGGER_ACTIONS = {
    "DUE": PAGE_ACTIONS["TRIGGER-DUE"],
    "FIRED": "OWNER — a trigger you registered FIRED: the §13.3 reweight decision is owed. Record it "
             "(decisions/ note, card status, its `fired:` date), or open a chat and say 'run the reweight'.",
    "BREACHED": "OWNER — a deferred ruling's stage_a_deadline passed unpromoted: run the registered "
                "fallback today (Rider 2 is unconditional).",
}


def trigger_event(flag: str):
    """(kind, date) from a TRIGGER-DUE flag's detail head, or None when the head is not the
    shape refresh._trigger_event writes."""
    m = TRIGGER_EVENT_RE.match(flag.partition(" ")[2].partition(" ")[2])
    return (m.group(1), m.group(2)) if m else None


def page_once_key(flag: str) -> str:
    """What makes two sightings of a page_once flag the SAME event (2026-09-02):
    FILING-LANDED = ticker·form·accession (never the 48h-window repeat);
    EARNINGS-SWEEP-STALE = the stale sweep stamp; TRIGGER-DUE = label + event (DUE / FIRED /
    BREACHED + its date, the head of the detail refresh._trigger_event writes); DIRTY-TOO-LONG =
    the tag; otherwise tag + first token (ticker / surface)."""
    tag, _, rest = flag.partition(" ")
    if tag == "FILING-LANDED":
        return flag.split(" -> ")[0].split(" filed ")[0]
    if tag == "EARNINGS-SWEEP-STALE":
        m = re.search(r"last_date_sweep is (\S+)", flag)
        return f"{tag} {m.group(1) if m else ''}"
    if tag == "DIRTY-TOO-LONG":
        return tag
    first = rest.split()[0] if rest.split() else ""
    if tag == "TRIGGER-DUE":
        ev = trigger_event(flag)
        if ev:
            return f"{tag} {first} {ev[0]} {ev[1] or ''}".rstrip()
        # An unrecognised detail shape keys on its full text: over-paging is the safe failure.
        return f"{tag} {first} {rest.partition(' ')[2]}".rstrip()
    return f"{tag} {first}".rstrip()


def record_down(reason: str, state_dir: Path = Path("state")) -> None:
    state_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with (state_dir / "notify_down.log").open("a") as fh:
        fh.write(f"{stamp} NOTIFY-DOWN {reason}\n")


def _send_email(subject: str, body: str, *, environ=os.environ,
                smtp_factory=None, state_dir: Path = Path("state"), message_id=None, receipt=None) -> bool:
    """One email to the owner. True only on a completed SMTP send — callers
    (the wrappers' ping-withholding) treat False as 'do not ping'."""
    receipt = receipt if receipt is not None else {}
    st = smtp_status(environ)
    if not st["configured"]:
        receipt["failure_class"] = "configuration"
        record_down(f"unconfigured (missing {', '.join(st['missing'])})", state_dir)
        return False
    msg = EmailMessage()
    msg["From"] = environ["CRUDE_FV_SMTP_USER"]
    msg["To"] = environ["CRUDE_FV_SMTP_TO"]
    msg["Subject"] = subject
    if message_id:
        msg["Message-ID"] = message_id
    msg.set_content(body)
    factory = smtp_factory or smtplib.SMTP
    try:
        with factory(environ["CRUDE_FV_SMTP_HOST"],
                     int(environ.get("CRUDE_FV_SMTP_PORT", "587")), timeout=30) as s:
            s.starttls()
            s.login(environ["CRUDE_FV_SMTP_USER"], environ["CRUDE_FV_SMTP_PASS"])
            refused = s.send_message(msg)
            if refused:
                receipt["failure_class"] = "permanent"
                record_down("recipient refused", state_dir)
                return False
        reauth.clear("smtp", state_dir / "reauth")
        # Send ledger: a send that isn't ledgered didn't happen.
        state_dir.mkdir(parents=True, exist_ok=True)
        with (state_dir / "notify_sent.log").open("a") as fh:
            fh.write(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} "
                     f"SENT {subject}\n")
        receipt["status"] = "smtp_accepted"
        return True
    except smtplib.SMTPAuthenticationError as exc:
        # REAUTH-NEEDED (2026-09-02): the app password is dead, not the network —
        # the sentinel pages it once from state/reauth/ (it cannot page by email).
        receipt["failure_class"] = "authentication"
        reauth.mark("smtp", f"SMTP auth refused: {exc}", state_dir / "reauth")
        record_down(f"send failed (auth): {exc}", state_dir)
        return False
    except Exception as exc:
        receipt["failure_class"] = "transient"
        record_down(f"send failed: {exc}", state_dir)
        return False


def send_email(subject, body, *, environ=os.environ, smtp_factory=None, state_dir=Path("state")):
    from .delivery import enqueue, attempt
    path = enqueue(subject, body, state_dir)
    return attempt(path, environ=environ, smtp_factory=smtp_factory)["status"] == "accepted"


def doctor(environ=os.environ, inputs_dir: Path = INPUTS_DIR,
           env_file: Path = ENV_FILE) -> list[str]:
    problems: list[str] = []
    if not env_file.exists():
        problems.append(f"{env_file} missing (create chmod 600; wrappers source it)")
    else:
        mode = stat.S_IMODE(env_file.stat().st_mode)
        if mode & 0o077:
            problems.append(f"{env_file} mode {oct(mode)} — must be 0o600")
    st = smtp_status(environ)
    if not st["configured"]:
        problems.append(f"env missing: {', '.join(st['missing'])}")
    try:
        routes = load_routes(inputs_dir)["routes"]
        overlap = set(routes["page"]) & set(routes["digest"])
        if overlap:
            problems.append(f"notify.yaml routes a tag both ways: {sorted(overlap)}")
    except Exception as exc:
        problems.append(f"inputs/notify.yaml unreadable: {exc}")
    return problems


def main(argv: "list[str] | None" = None) -> int:
    ap = argparse.ArgumentParser(description="owner-only email notification")
    ap.add_argument("--doctor", action="store_true",
                    help="check secrets file perms, env vars, routing config")
    ap.add_argument("--verify-notify", action="store_true",
                    help="send one test email to CRUDE_FV_SMTP_TO")
    ap.add_argument("--send", choices=["page", "digest"],
                    help="send one email from --body-file (first line = subject); "
                         "the governor's monitor/notify.sh uses this (2026-09-12)")
    ap.add_argument("--body-file", type=Path)
    ap.add_argument("--prefix", default=None,
                    help="subject prefix, e.g. '[portfolio]' (default: inputs/notify.yaml)")
    ap.add_argument("--state-dir", type=Path, default=Path("state"),
                    help="where notify_sent.log / notify_down.log are written")
    args = ap.parse_args(argv)

    if args.send:
        if not args.body_file or not args.body_file.exists():
            print("FAILED: --body-file missing")
            return 2
        first, _, body = args.body_file.read_text().partition("\n")
        subject_line = first.strip().lstrip("#").strip()
        prefix = args.prefix or load_routes()["subject_prefix"]
        if args.send == "page":
            subject = f"{prefix} PAGE: {subject_line}"
            body = ("This page means YOUR action is needed. Each line says who acts and what.\n\n"
                    + body.strip() + "\n")
        else:
            subject = f"{prefix} digest: {subject_line}"
            body = body.strip() + "\n"
        ok = send_email(subject, body, environ=load_env_file(ENV_FILE), state_dir=args.state_dir)
        print("SENT" if ok else f"FAILED (see {args.state_dir}/notify_down.log)")
        return 0 if ok else 1

    if args.doctor:
        problems = doctor()
        for p in problems:
            print(f"DOCTOR: {p}")
        print("DOCTOR: ok" if not problems else f"DOCTOR: {len(problems)} problem(s)")
        return 1 if problems else 0
    if args.verify_notify:
        prefix = load_routes()["subject_prefix"]
        stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
        ok = send_email(f"{prefix} verify-notify",
                        f"Test send from crude_tanker_fv.notify at {stamp}. "
                        "Receiving this closes the channel check.")
        print("SENT" if ok else "FAILED (see state/notify_down.log)")
        return 0 if ok else 1
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
