---
name: agent-browser-borrows-its-session
description:
  "9223's session is an in-memory copy that dies with the process; restart it on a 401, and only
  ask for a sign-in when the borrow itself reports no session"
metadata: 
  node_type: memory
  type: project
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-08-20T14:44:03.185Z
---

`tools/agent_browser.py` launches the headless browser on **9223** and copies the
Onshape cookies from the signed-in **9222** window over CDP (`borrow_session`). 9223's
session is a *copy*, so it expires on its own while 9222 stays signed in.

**It also dies with the process.** Onshape's `on-session-id` is a session cookie — no
expiry, memory only — so the durable profile directory never carries it and the borrow
runs on every launch. Restarting the agent browser is never free: it always costs a
fresh borrow, and a borrow only works while 9222 is still signed in. Leave it running.

**Why:** a 401 on 9223 was twice read as "the user must sign in by hand" and the run
stalled waiting for something the user cannot do — 9223 has no window to type into.

**How to apply:** on a 401 from 9223, restart the agent browser
(`pkill -f agent_browser.py`, then `uv run python tools/agent_browser.py`). It prints
which path it took. Only `the borrowed cookies carry no session` means 9222 itself is
logged out, and that is the one case that needs the user — it has happened, so do not
treat it as impossible. Check for duplicate `agent_browser.py` processes too: two
persistent contexts on the same profile directory serve a signed-out page.

Related: [[onshape-api-via-browser-session]].
