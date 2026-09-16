"""Make `stickbot-draft9p4` and `stickbot-draft9p4-check`, and record every element id.

    uv run --project . python .docs/experiments/runs/2026-09-08-draft9p4/scripts/p_make_docs.py

The build document is a copy of `stickbot-draft9p3`'s workspace, which is where Onshape's copy
route works from: there is no version-copy route, and
`.docs/experiments/runs/2026-09-08-draft9p4/scripts/p_ws_vs_version.py` is what shows how far
the workspace has moved past the version the plan names. The check document starts empty.

Refuses to run a second time: if either name already exists, it reports the ids and writes
nothing.
"""
import json
import sys
import time


from playwright.sync_api import sync_playwright

from stickbot import repo_root
from stickbot import onshape_gui as gui
from stickbot import onshape_session as api

P3_DID = "50b2d87357670c07c2fbcb89"
P3_WID = "a49825ea9aa838bdfae7b78d"
BUILD = "stickbot-draft9p4"
CHECK = "stickbot-draft9p4-check"
OUT = (str(repo_root()) + "/.docs/experiments/runs/"
       "2026-09-08-draft9p4/reference/documents.json")


def call(page, method, path, payload=None):
    time.sleep(2.0)
    r = api.api(page, method, path, payload)
    if r["status"] != 200:
        raise SystemExit(f"{method} {path} answered {r['status']}: {str(r['body'])[:300]}")
    return r["body"]


def named(page, name):
    r = api.api(page, "GET", f"/api/documents?q={name}&filter=0&limit=20")
    return [i for i in r["body"].get("items", []) if i["name"] == name]


def elements(page, did, wid):
    return [{"id": e["id"], "type": e["elementType"], "name": e["name"]}
            for e in call(page, "GET", f"/api/documents/d/{did}/w/{wid}/elements")]


def main():
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        page.goto("https://cad.onshape.com/documents", wait_until="domcontentloaded")
        print("signed in as:", api.require_signed_in(page))

        for n in (BUILD, CHECK):
            hits = named(page, n)
            if hits:
                raise SystemExit(f"{n} already exists: {[h['id'] for h in hits]}. "
                                 f"Nothing written.")

        body = call(page, "POST", f"/api/documents/{P3_DID}/workspaces/{P3_WID}/copy",
                    {"newName": BUILD, "isPublic": False})
        b_did = body["newDocumentId"]
        b_wid = body["newWorkspaceId"]
        print(f"{BUILD}: did {b_did} wid {b_wid}")

        c = api.new_document(page, CHECK)
        print(f"{CHECK}: did {c.did} wid {c.wid}")

        out = {
            "build": {"name": BUILD, "did": b_did, "wid": b_wid,
                      "copiedFrom": {"name": "stickbot-draft9p3", "did": P3_DID,
                                     "wid": P3_WID},
                      "elements": elements(page, b_did, b_wid)},
            "check": {"name": CHECK, "did": c.did, "wid": c.wid,
                      "elements": elements(page, c.did, c.wid)},
        }
        with open(OUT, "w") as fh:
            json.dump(out, fh, indent=1, sort_keys=True)
            fh.write("\n")
        print("\n" + json.dumps(out, indent=1, sort_keys=True))
        print("\nwrote", OUT)
        browser.close()


main()
