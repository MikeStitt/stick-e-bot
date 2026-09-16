import sys, collections
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    print("tree:", gui.tree(page))
    r = api.api(page, "GET",
                f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}/partid/JHD/bodydetails")
    b = r["body"]["bodies"][0]
    print("faces:", len(b["faces"]),
          collections.Counter(f["surface"]["type"] for f in b["faces"]))
    page.screenshot(path="hd23.png")
