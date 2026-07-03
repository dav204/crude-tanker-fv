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
import smtplib
import stat
import sys
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path

import yaml

from .loaders import INPUTS_DIR

ENV_FILE = Path.home() / ".config" / "crude-tanker-fv.env"
REQUIRED_VARS = ("CRUDE_FV_SMTP_HOST", "CRUDE_FV_SMTP_USER",
                 "CRUDE_FV_SMTP_PASS", "CRUDE_FV_SMTP_TO")


def load_routes(inputs_dir: Path = INPUTS_DIR) -> dict:
    return yaml.safe_load((inputs_dir / "notify.yaml").read_text())


def smtp_status(environ=os.environ) -> dict:
    missing = [v for v in REQUIRED_VARS if not environ.get(v)]
    return {"configured": not missing, "missing": missing}


def route_flags(flags: list[str], routes: dict) -> "tuple[list[str], list[str]]":
    """Partition flags by leading tag into (page, digest). record_only tags are
    dropped here (they reach state via their writers). An UNKNOWN tag PAGES —
    a tag someone forgot to route must fail loud, not vanish into a digest."""
    digest_tags = set(routes["routes"]["digest"])
    record_tags = set(routes["routes"].get("record_only", []))
    page, digest = [], []
    for f in flags:
        tag = f.split()[0]
        if tag in digest_tags:
            digest.append(f)
        elif tag not in record_tags:
            page.append(f)
    return page, digest


def record_down(reason: str, state_dir: Path = Path("state")) -> None:
    state_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with (state_dir / "notify_down.log").open("a") as fh:
        fh.write(f"{stamp} NOTIFY-DOWN {reason}\n")


def send_email(subject: str, body: str, *, environ=os.environ,
               smtp_factory=None, state_dir: Path = Path("state")) -> bool:
    """One email to the owner. True only on a completed SMTP send — callers
    (the wrappers' ping-withholding) treat False as 'do not ping'."""
    st = smtp_status(environ)
    if not st["configured"]:
        record_down(f"unconfigured (missing {', '.join(st['missing'])})", state_dir)
        return False
    msg = EmailMessage()
    msg["From"] = environ["CRUDE_FV_SMTP_USER"]
    msg["To"] = environ["CRUDE_FV_SMTP_TO"]
    msg["Subject"] = subject
    msg.set_content(body)
    factory = smtp_factory or smtplib.SMTP
    try:
        with factory(environ["CRUDE_FV_SMTP_HOST"],
                     int(environ.get("CRUDE_FV_SMTP_PORT", "587")), timeout=30) as s:
            s.starttls()
            s.login(environ["CRUDE_FV_SMTP_USER"], environ["CRUDE_FV_SMTP_PASS"])
            s.send_message(msg)
        # Send ledger (WO2 close): the acceptance compiler joins flags to
        # SENT emails — a send that isn't ledgered didn't happen.
        state_dir.mkdir(parents=True, exist_ok=True)
        with (state_dir / "notify_sent.log").open("a") as fh:
            fh.write(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} "
                     f"SENT {subject}\n")
        return True
    except Exception as exc:
        record_down(f"send failed: {exc}", state_dir)
        return False


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
    args = ap.parse_args(argv)

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
