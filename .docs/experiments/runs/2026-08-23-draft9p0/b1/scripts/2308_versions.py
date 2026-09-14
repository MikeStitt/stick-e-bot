"""Every version of stickbot-draft9p0, oldest first, with its assembly tab id.

A version is read-only, so a page whose state the workspace has moved past can be
shot from one without touching the workspace at all.
"""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    vs = osx.api(page, "GET", f"/api/documents/d/{did}/versions")["body"]
    for v in vs:
        print(f'{v["name"]:<22} {v["id"]}  {v.get("createdAt","")[:19]}')
    print()
    for v in vs:
        if v["name"].startswith(("t1 ", "t2 ", "t3 ", "t4 ", "t5 ", "t6 ")):
            els = osx.api(page, "GET", f"/api/documents/d/{did}/v/{v['id']}/elements")["body"]
            print(v["name"], "->", [(e["name"], e["elementType"], e["id"]) for e in els])
