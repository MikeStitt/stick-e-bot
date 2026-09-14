import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    parts = osx.api(page, "GET",
        f"/api/parts/d/{did}/w/{wid}/e/{s['bs_eid']}")["body"]
    for pt in parts:
        pid = pt["partId"]
        b = osx.api(page, "GET",
            f"/api/parts/d/{did}/w/{wid}/e/{s['bs_eid']}/partid/{pid}/boundingboxes")["body"]
        print(pt["name"], "|", {k: round(v*1000, 4) for k, v in b.items()
                                if isinstance(v, (int, float))})
