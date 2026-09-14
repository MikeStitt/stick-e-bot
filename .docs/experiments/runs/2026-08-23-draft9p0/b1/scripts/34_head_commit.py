import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page)
    gui.rename_row(page, "Part 1", "head")
    print("tree:", gui.tree(page))
    r = api.api(page, "GET",
                f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}/boundingboxes")
    print("bbox:", {k: round(v * 1000, 4) for k, v in r["body"].items() if k[0] in "lh"})
