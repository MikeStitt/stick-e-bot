#!/usr/bin/env python3
"""A browser a person clicks in, that a recorder can watch.

The agent's browser (`tools/agent_browser.py`, port 9223) is headless on purpose: it
must not steal focus or catch stray keystrokes. This one is the opposite. A human
follows `robot-guide2` in it, so it has a window, it takes focus, and every key you
press is meant for it.

It gets its own port and its own profile so the other two browsers are untouched —
9222 stays the one you signed in to, 9223 stays the agent's. Nothing here borrows
cookies: you sign in by hand, once, and the profile keeps the session. That is
deliberate. Capture is not running yet at this stage, so no password is ever live
while a recorder is listening.

    python human_browser.py            # launch a window, and stay running
    python human_browser.py --video D  # ...and write a webm of the session into D
    python human_browser.py --status   # is it up, and who is signed in?

Video is a launch-time choice — Playwright cannot start one on a browser that is
already open — and it is off by default so that signing in is never filmed. The webm
is finalized when the window closes, so it is the watchable copy, not the record; the
record is what `recorder.py` writes.

Leave it running. The recorder attaches over CDP on 9224 from another process.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

HUMAN_PORT = 9224     # the window a person clicks in
PROFILE = Path.home() / ".cache" / "onshape-automation" / "human-profile"
ONSHAPE = "https://cad.onshape.com"

WHOAMI = """async () => {
    const r = await fetch('/api/users/sessioninfo', {credentials:'include'});
    if (r.status !== 200) return null;
    const j = await r.json();
    return j.name || j.id;
}"""


def connect(playwright, port: int = HUMAN_PORT):
    """Attach to the human's browser, on a CAD tab.

    Guarded the same way ``gui_steps.connect`` is, and for the same reason: 9222 is
    the user's own signed-in window and 9223 is the agent's. A recorder that attaches
    to the wrong one either records nothing or corrupts a run in progress, and neither
    announces itself. Passing any other port is refused rather than honored.
    """
    if port != HUMAN_PORT:
        raise ValueError(f"port {port} is not the human's browser; 9224 only")
    browser = playwright.chromium.connect_over_cdp(f"http://127.0.0.1:{port}")
    ctx = browser.contexts[0]
    for page in ctx.pages:
        if page.url.startswith(ONSHAPE):
            return browser, ctx, page
    page = ctx.new_page()
    page.goto(f"{ONSHAPE}/documents", wait_until="domcontentloaded")
    page.wait_for_timeout(4500)
    return browser, ctx, page


def status() -> int:
    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{HUMAN_PORT}")
        except Exception as exc:
            print(f"no human browser on port {HUMAN_PORT}: {str(exc)[:70]}")
            return 1
        ctx = browser.contexts[0]
        page = next((pg for pg in ctx.pages if pg.url.startswith(ONSHAPE)), None)
        who = page.evaluate(WHOAMI) if page else None
        if who:
            print(f"human browser is up; signed in as {who}")
        elif page:
            print("human browser is up on an Onshape tab, but not signed in")
        else:
            print("human browser is up; no Onshape tab open, so sign-in is unknown")
        browser.close()
        return 0 if who else 1


def main() -> int:
    if "--status" in sys.argv:
        return status()

    video = None
    if "--video" in sys.argv:
        video = Path(sys.argv[sys.argv.index("--video") + 1])
        video.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        PROFILE.mkdir(parents=True, exist_ok=True)
        try:
            ctx = p.chromium.launch_persistent_context(
                user_data_dir=str(PROFILE),
                headless=False,
                args=[f"--remote-debugging-port={HUMAN_PORT}", "--window-size=1600,1000"],
                no_viewport=True,   # the page fills the real window, not a fixed box
                record_video_dir=str(video) if video else None,
            )
        except Exception as exc:
            print(f"could not launch: {str(exc)[:200]}")
            print(f"if a window is already open on this profile, use that one "
                  f"({PROFILE}); two processes cannot share it")
            return 1

        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(f"{ONSHAPE}/documents", wait_until="domcontentloaded")
        page.wait_for_timeout(6000)

        who = page.evaluate(WHOAMI)
        print(f"human browser up on port {HUMAN_PORT}")
        if video:
            print(f"filming to {video} — the webm appears when this window closes")
        if who:
            print(f"signed in as {who} — the profile kept the session")
        else:
            print("not signed in. Sign in to Onshape in the window that just opened.")
            print("Nothing is recording, so your password is not being captured.")
            print("The profile keeps the session, so this is the only time.")

        print("leave this running; Ctrl-C closes the window")
        try:
            while True:
                time.sleep(5.0)
        except KeyboardInterrupt:
            print("\nclosing")
        finally:
            ctx.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
