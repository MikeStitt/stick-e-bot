"""What `stickbot-draft9p3` has published, and what its workspace holds, before anything is copied.

    uv run --project . python .docs/experiments/runs/2026-09-08-draft9p4/scripts/p_docs_read.py

Read only. Every call is a GET.
"""
import json
import sys
import time

sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge/tools")
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")

from playwright.sync_api import sync_playwright

import onshape_gui as gui
import onshape_session as api

P3_DID = "50b2d87357670c07c2fbcb89"
P3_WID = "78e4bd5f5a5e2b2cbcbf6ba2"   # replaced below by the read
PACE = 1.0


def get(page, path):
    time.sleep(PACE)
    r = api.api(page, "GET", path)
    return r["status"], r["body"]


def main():
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        page.goto("https://cad.onshape.com/documents", wait_until="domcontentloaded")
        who = api.require_signed_in(page)
        print("signed in as:", who)

        st, doc = get(page, f"/api/documents/{P3_DID}")
        print("document:", st, repr(doc)[:400])
        if st != 200 or not isinstance(doc, dict):
            st, ws = get(page, f"/api/documents/d/{P3_DID}/workspaces")
            print("workspaces:", st, repr(ws)[:600])
            if st != 200:
                return
            wid = ws[0]["id"]
        else:
            wid = doc["defaultWorkspace"]["id"]
        print("workspace in use:", wid)

        st, vers = get(page, f"/api/documents/d/{P3_DID}/versions")
        print("\nversions:", st, len(vers) if st == 200 else vers)
        if st == 200:
            for v in vers:
                print(f"  {v['createdAt'][:19]}  {v['id']}  {v['name']}")

        st, els = get(page, f"/api/documents/d/{P3_DID}/w/{wid}/elements")
        print("\nelements:", st, len(els) if st == 200 else els)
        if st == 200:
            for e in els:
                print(f"  {e['id']}  {e['elementType']:12} {e['name']}")

        browser.close()


main()
