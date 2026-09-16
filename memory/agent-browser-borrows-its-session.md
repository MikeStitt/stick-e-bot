---
name: agent-browser-borrows-its-session
description:
  "A 401 from 9223 means restart the agent browser, not ask for a sign-in; only the borrow
  reporting no session needs a person."
metadata:
  node_type: memory
  type: feedback
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-08-20T14:44:03.185Z
---

**On a 401 from 9223, restart the agent browser.** Do not ask the user to sign in.

**Why:** a 401 on 9223 was twice read as *the user must sign in by hand*, and the run stalled
waiting for something the user cannot do — 9223 is headless and has no window to type into. The
session there is a copy borrowed from 9222 at launch, so it expires on its own while 9222 stays
signed in, and a restart is the whole fix.

**How to apply:** `pkill -f agent_browser.py`, then `uv run python -m stickbot.agent_browser`. It
prints which path it took. Only `the borrowed cookies carry no session` means 9222 itself is logged
out, and that is the one case that needs a person — it has happened, so do not treat it as
impossible; the way out is `uv run python -m stickbot.browser --signin`. Check for duplicate
`agent_browser.py` processes too: two persistent contexts on the same profile directory serve a
signed-out page.

How the borrow works and what it costs is in
[`.docs/browser-access.md`](../.docs/browser-access.md); this memory is only the failure mode,
which that file does not mention. Related: [[onshape-api-via-browser-session]].
