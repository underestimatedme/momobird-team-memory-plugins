"""Offer one memory capture pass for an explicitly opted-in local project."""
import json
import os
from pathlib import Path
import sys


def main():
    root = os.environ.get("MOMOBIRD_MEMORY_AUTO_PROJECT")
    if not root:
        return
    try:
        event = json.load(sys.stdin)
        if event.get("hook_event_name") != "Stop" or event.get("stop_hook_active"):
            return
        if event.get("background_tasks") or event.get("session_crons"):
            return
        cwd = event.get("cwd")
        if not cwd or Path(cwd).resolve() != Path(root).expanduser().resolve():
            return
    except (OSError, ValueError, TypeError):
        return

    guidance = (
        "This local project has opted into MomoBird memory capture. "
        "If the finished work produced a verified, reusable project lesson, follow the "
        "team-memory skill to check for duplicates and submit at most one proposal using "
        "the connected project. Skip if the tool is unavailable, you already submitted "
        "a proposal for this work, or the user declined capture. Never send raw logs, "
        "transcripts, credentials or customer data. Report a successful submission as pending review."
    )
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "Stop", "additionalContext": guidance}}))


if __name__ == "__main__":
    main()
