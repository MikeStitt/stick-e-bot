"""Publish `Start` on `stickbot-draft9p4`, so the copy has a named point before any tutorial.

    uv run --project . python .docs/experiments/runs/2026-09-08-draft9p4/scripts/p_start_version.py
"""
import json
import sys
import time

sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge/tools")
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")

from playwright.sync_api import sync_playwright

import onshape_gui as gui
import onshape_session as api

DOCS = json.load(open("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/"
                      "runs/2026-09-08-draft9p4/reference/documents.json"))
DID, WID = DOCS["build"]["did"], DOCS["build"]["wid"]
NAME = "Start"


def main():
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        eid = next(e["id"] for e in DOCS["build"]["elements"] if e["type"] == "PARTSTUDIO")
        gui.open_doc(page, api.Doc(DID, WID, eid))
        print("signed in as:", api.require_signed_in(page))

        got = api.api(page, "GET", f"/api/documents/d/{DID}/versions")
        if got["status"] == 200:
            for v in got["body"]:
                print(f"  {v['createdAt'][:19]}  {v['id']}  {v['name']}")
        if got["status"] == 200 and any(v["name"] == NAME for v in got["body"]):
            print(f"'{NAME}' already published; nothing written.")
            browser.close()
            return

        time.sleep(2)
        r = api.api(page, "POST", f"/api/documents/{DID}/versions",
                    {"documentId": DID, "workspaceId": WID, "name": NAME,
                     "description": "the copy of stickbot-draft9p3, before any draft9p4 edit"})
        print("POST /versions:", r["status"], str(r["body"])[:200])
        if r["status"] != 200:
            raise SystemExit("version not published")

        time.sleep(2)
        vers = api.api(page, "GET", f"/api/documents/d/{DID}/versions")["body"]
        for v in vers:
            print(f"  {v['createdAt'][:19]}  {v['id']}  {v['name']}")
        browser.close()


main()
