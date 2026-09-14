#!/usr/bin/env python3
"""Launch the signed-in Chromium that the capture pipeline drives.

Run this, sign in to Onshape in the window that opens, and leave it running. Everything
else attaches over the Chrome DevTools Protocol on port 9222 and never handles a
password.

Sign in once by hand so Chrome offers to save the credential. After that `--signin`
gets the session back without a person: it types the account email, which is not a
secret, and Chrome's own password manager fills the password field. This file never
reads, prints or stores a password — it looks at that field's length and nothing else.

The profile lives in a **durable** directory rather than a session scratchpad, so the
login survives between working sessions. Earlier runs kept it in a temp directory and
lost the session every time the scratchpad was cleared.

    python browser.py            # launch and stay running
    python browser.py --status   # is it up, and is anyone signed in?
    python browser.py --signin   # sign the running one back in, email from git config
    python browser.py --signin --email you@example.com
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

PROFILE = Path.home() / ".cache" / "onshape-automation" / "chrome-profile"
PORT = 9222
START_URL = "https://cad.onshape.com/documents"
SIGNIN_URL = "https://cad.onshape.com/signin"


def status() -> int:
    import onshape_session as osn

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{PORT}")
        except Exception as exc:
            print(f"no browser on port {PORT}: {exc}")
            return 1
        ctx = browser.contexts[0]
        page = ctx.pages[-1] if ctx.pages else ctx.new_page()
        try:
            print("signed in as", osn.require_signed_in(page))
            return 0
        except Exception as exc:
            print(exc)
            return 1
        finally:
            browser.close()


def account_email(argv) -> str:
    """The address to type into step one of the sign-in.

    An email address is not a credential, so it can live in a config file. Taking it
    from `git config user.email` keeps the account out of this file and off the command
    line; `--email` overrides it when the two differ.
    """
    if "--email" in argv:
        return argv[argv.index("--email") + 1]
    got = subprocess.run(
        ["git", "config", "user.email"], capture_output=True, text=True
    ).stdout.strip()
    if not got:
        raise SystemExit("no --email given and `git config user.email` is empty")
    return got


def signin(email: str) -> int:
    """Sign the already-running browser back in, letting Chrome supply the password.

    Onshape's sign-in is two pages: an email and **Continue**, then a second page whose
    password field Chrome autofills from the saved credential. Nothing here types into
    that field or reads it — `el.value.length` is the whole of what it asks.
    """
    import onshape_session as osn

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{PORT}")
        except Exception as exc:
            print(f"no browser on port {PORT}: {exc}")
            print("run `python browser.py` first and leave it running")
            return 1
        ctx = browser.contexts[0]
        page = ctx.pages[-1] if ctx.pages else ctx.new_page()
        try:
            print("already signed in as", osn.require_signed_in(page))
            return 0
        except osn.NotSignedIn:
            pass

        print(f"signing in as {email}")
        page.goto(SIGNIN_URL, wait_until="domcontentloaded")
        page.wait_for_selector("input[name=username]", timeout=30_000)
        page.fill("input[name=username]", email)
        page.click("button:has-text('Continue')")

        page.wait_for_selector("input[name=password]", timeout=30_000)
        page.wait_for_timeout(3000)
        filled = page.eval_on_selector("input[name=password]", "el => el.value.length")
        print(f"password field: {filled} characters, filled by Chrome")
        if not filled:
            print("Chrome has no saved password for cad.onshape.com.")
            print("Sign in by hand in the window once and let Chrome save it; this")
            print("command works from then on.")
            return 1
        page.click("button[type=submit]")
        page.wait_for_timeout(12_000)
        try:
            print("signed in as", osn.require_signed_in(page))
            return 0
        except Exception as exc:
            print(exc)
            print(f"the window is showing {page.url} — finish it by hand")
            return 1


def launch() -> int:
    PROFILE.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE),
            headless=False,
            args=[f"--remote-debugging-port={PORT}"],
            viewport=None,
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(START_URL)
        print(f"browser up on port {PORT}, profile at {PROFILE}")
        print("sign in to Onshape in the window, then leave this running")
        # Park until the window is closed. Closing it cleanly is what flushes cookies
        # to the profile directory; a hard kill can lose the session.
        try:
            page.wait_for_event("close", timeout=0)
        except Exception:
            pass
        ctx.close()
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    if "--status" in sys.argv:
        raise SystemExit(status())
    if "--signin" in sys.argv:
        raise SystemExit(signin(account_email(sys.argv)))
    raise SystemExit(launch())
