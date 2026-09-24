"""Human-readable presentation of recorded conditions; no routing or financial decisions."""
import re
from collections import Counter


def duration(days):
    minutes = float(days) * 1440
    if minutes < 60:
        return "%g minutes" % round(minutes, 1)
    if minutes < 2880:
        return "%g hours" % round(minutes / 60, 1)
    return "%g days" % round(minutes / 1440, 1)


def flag_summary(flag):
    tag, _, detail = flag.partition(" ")
    if tag == "FILING-QUEUE-STALLED":
        match = re.search(r"(\d+) pending; oldest ([^; ]+)", detail)
        if match:
            return ("Filing review has stalled: %s filings are waiting; the oldest arrived %s. "
                    "The agent handles the filings once the triage workflow is restored." %
                    (match[1], match[2][:10]))
    if tag == "FETCH-FAILED":
        match = re.search(r"([^:]+): heartbeat ([\d.]+)d old \(cadence limit ([\d.]+)d\)", detail)
        if match:
            return ("%s has not reported for %s (expected within %s). Its scheduled execution needs checking." %
                    (match[1], duration(match[2]), duration(match[3])))
    titles = {"PRICE-BASIS": "Price data", "FORK-OPENED": "Recommendation open for objection",
              "FORK-EXECUTABLE": "Recommendation's objection window has closed",
              "TASK-PARKED": "Scheduled task is waiting for permission",
              "SURFACE-INCOHERENT": "Valuation output failed a consistency check",
              "FILING-QUEUE-INVALID": "Filing queue could not be read",
              "DIRTY-TOO-LONG": "Unfinished changes are holding up automation",
              "REAUTH-NEEDED": "Sign-in needs renewal"}
    return titles.get(tag, tag.replace("-", " ").capitalize()) + ": " + detail


def filing_summary(flags):
    filings = [f for f in flags if f.startswith("FILING-LANDED ")]
    if not filings:
        return ""
    counts = Counter(f.split()[1].rstrip(":") for f in filings)
    return ("%d filings awaiting agent triage across %d companies.\nBy company: %s.\n"
            "These are pending reviews, not %d separate requests for you.\n"
            "The agent can retrieve the full queue and arrival dates from the filing ledger. "
            "Complete diagnostic list: state/sentinel.log." %
            (len(filings), len(counts), ", ".join("%s %d" % pair for pair in sorted(counts.items())), len(filings)))


def page_notice(page, digest, prefix, action):
    optional = [f for f in page if "OWNER (optional)" in action(f)]
    required = [f for f in page if f not in optional]
    summary = "%d action%s needed" % (len(required), "" if len(required) == 1 else "s")
    if optional:
        summary += "; %d optional objection%s" % (len(optional), "" if len(optional) == 1 else "s")
    lines = ["Your attention: " + summary + ".", "",
             "Open the crude-tanker-fv chat and name the item below to work through it."]
    for label, flags in (("Action needed", required), ("Optional objections", optional)):
        if flags:
            lines += ["", label]
        for index, flag in enumerate(flags, 1):
            lines += ["", "%d. %s" % (index, flag_summary(flag)), "Next step: " + action(flag),
                      "Reference: " + " ".join(flag.split()[:2])]
    if digest:
        filings = sum(f.startswith("FILING-LANDED ") for f in digest)
        lines += ["", "Routine work is in the daily digest (%d pending filings; %d other recorded conditions)." %
                  (filings, len(digest) - filings)]
    return prefix + " PAGE: " + summary, "\n".join(lines) + "\n"


def digest_notice(flags, prefix, dark_days=0, meta_note=None):
    filings = sum(f.startswith("FILING-LANDED ") for f in flags)
    other = [f for f in flags if not f.startswith("FILING-LANDED ")]
    label = ("%d filings awaiting triage; %d other conditions" % (filings, len(other))
             if filings else ("%d recorded conditions" % len(other) if other else "OK"))
    lines = ["Daily workflow summary", ""]
    if dark_days:
        lines += ["Monitoring resumed after a %d-day gap. This includes accumulated work." % dark_days, ""]
    if meta_note:
        lines += [meta_note, ""]
    if filings:
        lines += [filing_summary(flags), ""]
    if other:
        lines += ["Other recorded conditions (action requests are sent separately):", ""]
        for flag in other:
            lines += ["- " + flag_summary(flag) + " [" + " ".join(flag.split()[:2]) + "]"]
    if not flags:
        lines.append("All checks quiet.")
    lines += ["", "Detailed check results: state/sentinel.log. Queue membership and alert rules are unchanged."]
    return prefix + " daily digest — " + label, "\n".join(lines) + "\n"


def workflow_notice(active, changes, recovery):
    lines = ["Workflow follow-up", ""]
    owner = sum(active[key].get("resolver") == "owner" for key in changes)
    lines += ["%d changed item(s) need your decision; %d are assigned elsewhere. %d status issue(s) recovered." %
              (owner, len(changes) - owner, len(recovery)), ""]
    for key in changes:
        row = active[key]
        lines += [key.replace("_", " ").replace(":", " / "),
                  "Status: " + row["status"] + ". Responsible: " + str(row.get("resolver", "unassigned")) + ".",
                  "Next step: " + str(row.get("next_action") or "Not recorded; workflow repair is required.")]
        if row.get("blocking_decision_ids"):
            lines.append("Waiting on decisions: " + ", ".join(row["blocking_decision_ids"]))
        lines += ["Reference: " + key, ""]
    for key in recovery:
        lines += ["Status information restored: " + key + ". See work_items.yaml for its current disposition."]
    lines += ["", "Task details and evidence: work_items.yaml. Financial decisions remain with you."]
    return "\n".join(lines)


def operation_notice(receipt, failures):
    stages = {"auto_land": "accepting generated changes", "publication": "publishing the valuation update",
              "auto_push": "pushing the commit to the remote repository", "checks": "running checks",
              "generation": "generating valuations", "consumer_check": "checking the governor handoff"}
    lines = ["The scheduled valuation workflow did not finish successfully.", "",
             "Stopped stages: " + ", ".join(stages.get(k, k.replace("_", " ")) for k in failures) + "."]
    pub = receipt["publication"]
    if failures.get("publication"):
        lines.append("This run did not confirm a successful publication. Any earlier accepted valuation remains separate.")
    else:
        lines.append("Last recorded publication status: " + pub["status"] + ".")
    if pub.get("reason"):
        lines.append("Recorded publication blocker: " + pub["reason"])
    lines += ["", "Next step for you: open crude-tanker-fv and ask to inspect the stopped stages in this run. "
              "Any owner decision needed must be identified before proceeding.", "",
              "Run receipt: state/operations/runs/" + receipt["run_id"] + ".json",
              "Stage exit codes: " + ", ".join("%s=%s" % pair for pair in sorted(failures.items()))]
    return "\n".join(lines) + "\n"
