#!/usr/bin/env python3
"""A private browser for an agent to drive.

The problem this solves: a headed Chromium on your desktop steals focus, and anything
you type while an agent is working can land in its window and corrupt the run. You end
up unable to use your own machine.

This launches a **headless** Chromium on its own port with its own profile. It has no
window, so it cannot take focus and cannot receive your keystrokes. Onshape renders
fine in it — WebGL comes from SwiftShader, which is slower than the GPU and perfectly
adequate for driving the UI.

The session is copied from the signed-in browser as **cookies over CDP**, not by
copying the profile directory: a running Chrome has not flushed its cookie database,
so a file copy silently produces a logged-out browser.

**The copy happens on every launch, and it has to.** Onshape's `on-session-id` is a
session cookie — no expiry, held in memory, never written to the profile — so the
agent browser's session dies with its process however cleanly it is shut down. Leave
this running; restarting it always costs a fresh borrow, and a borrow only works while
the signed-in browser is still signed in.

    python agent_browser.py                 # launch, and stay running
    python agent_browser.py --watch         # also serve a live view on :8900
    python agent_browser.py --status        # is it up, and who is signed in?

To watch without touching it, open http://localhost:8900 in your own browser. It is a
picture; there is no way to click into the agent's session from there.
"""

from __future__ import annotations

import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from playwright.sync_api import sync_playwright

LIVE_PORT = 9222      # the browser you signed in to
AGENT_PORT = 9223     # the one the agent drives
WATCH_PORT = 8900
PROFILE = Path.home() / ".cache" / "onshape-automation" / "agent-profile"
ONSHAPE = "https://cad.onshape.com"

GL_ARGS = [
    "--use-gl=angle",
    "--use-angle=swiftshader",
    "--enable-unsafe-swiftshader",
]

_latest = {"png": b"", "at": 0.0}


class Viewer(BaseHTTPRequestHandler):
    PAGE = b"""<!doctype html><title>agent browser</title>
<style>body{margin:0;background:#111;color:#ccc;font:13px system-ui}
img{width:100%;height:auto;display:block}
p{padding:6px 10px;margin:0}</style>
<p>Live view &mdash; look only. Your keyboard and mouse are not connected to this.</p>
<img id=v src="/frame.png">
<script>setInterval(()=>{document.getElementById('v').src='/frame.png?'+Date.now()},1000)</script>
"""

    def do_GET(self):
        if self.path.startswith("/frame.png"):
            png = _latest["png"]
            self.send_response(200 if png else 503)
            self.send_header("Content-Type", "image/png")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            if png:
                self.wfile.write(png)
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(self.PAGE)

    def log_message(self, *a):  # keep the console quiet
        pass


SESSION_INFO = """async () => {
     const r = await fetch('/api/users/sessioninfo', {credentials:'include'});
     if (r.status !== 200) return null;
     const j = await r.json();
     return j.name || j.id;
   }"""


def who(page) -> str | None:
    """Who Onshape thinks is signed in on this page, or None."""
    if ONSHAPE not in page.url:
        return None
    return page.evaluate(SESSION_INFO)


def borrow_session(playwright) -> list[dict]:
    """Take the cookies from the signed-in browser, without disturbing it."""
    browser = playwright.chromium.connect_over_cdp(f"http://127.0.0.1:{LIVE_PORT}")
    try:
        cookies = browser.contexts[0].cookies()
    finally:
        browser.close()
    keep = [c for c in cookies if "onshape" in c.get("domain", "")]
    print(f"borrowed {len(keep)} Onshape cookies from the signed-in browser")
    return keep


def status() -> int:
    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{AGENT_PORT}")
        except Exception as exc:
            print(f"no agent browser on port {AGENT_PORT}: {str(exc)[:70]}")
            return 1
        ctx = browser.contexts[0]
        page = next((pg for pg in ctx.pages if ONSHAPE in pg.url), None) or ctx.new_page()
        signed_in_as = who(page)
        print("agent browser is up;",
              f"signed in as {signed_in_as}" if signed_in_as else "not signed in")
        browser.close()
        return 0 if signed_in_as else 1


def main() -> int:
    if "--status" in sys.argv:
        return status()
    watch = "--watch" in sys.argv

    with sync_playwright() as p:
        PROFILE.mkdir(parents=True, exist_ok=True)
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE),
            headless=True,
            args=[f"--remote-debugging-port={AGENT_PORT}", *GL_ARGS],
            viewport={"width": 1600, "height": 1000},
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(f"{ONSHAPE}/documents", wait_until="domcontentloaded")
        page.wait_for_timeout(8000)

        # Ask before borrowing. A fresh launch has no session of its own — Onshape's
        # is a session cookie and does not survive the process — so in practice this
        # borrows every time. The check stays because writing a dead session over a
        # live one is not a thing worth being able to do, and because saying which
        # way it went is what told us the profile was never carrying one.
        signed_in_as = who(page)
        if signed_in_as:
            print(f"its own session is still good, signed in as {signed_in_as}")
        else:
            try:
                cookies = borrow_session(p)
            except Exception as exc:
                print(f"no session of its own, and no signed-in browser on port "
                      f"{LIVE_PORT}: {str(exc)[:70]}")
                ctx.close()
                return 1
            ctx.add_cookies(cookies)
            page.reload(wait_until="domcontentloaded")
            page.wait_for_timeout(6000)
            signed_in_as = who(page)
            if not signed_in_as:
                print("the borrowed cookies carry no session — sign in to Onshape in your "
                      "own browser, then run this again")
                ctx.close()
                return 1
            print(f"borrowed a session from the signed-in browser, {signed_in_as}")

        print(f"agent browser up on port {AGENT_PORT}, signed in as {signed_in_as}")
        print("it has no window, so it cannot take focus or receive your keystrokes")

        if watch:
            threading.Thread(
                target=lambda: HTTPServer(("127.0.0.1", WATCH_PORT), Viewer).serve_forever(),
                daemon=True,
            ).start()
            print(f"live view on http://localhost:{WATCH_PORT} — look only")

        try:
            while True:
                if watch:
                    try:
                        pages = [pg for pg in ctx.pages if not pg.is_closed()]
                        if pages:
                            _latest["png"] = pages[-1].screenshot(timeout=8000)
                            _latest["at"] = time.time()
                    except Exception:
                        pass  # the agent may be mid-navigation; try again next tick
                    time.sleep(1.0)
                else:
                    time.sleep(5.0)
        except KeyboardInterrupt:
            print("\nclosing")
        finally:
            ctx.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
