import sys, math
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.name_feature(page, "cavity from ball")
    gui.tick(page); page.wait_for_timeout(3000)
    print("tree:", gui.tree(page)[-4:])
    for pid, name in [("JHD", "Ball stud"), ("JKD", "Socket body")]:
        v = common.volume(page, api, s["did"], s["wid"], s["bs_eid"], pid)
        print(name, "vol", v)
    print("cavity volume:", round(2799.159 - common.volume(
        page, api, s["did"], s["wid"], s["bs_eid"], "JKD"), 3), "expected 1132.649")
    for f in common.faces(page, api, s["did"], s["wid"], s["bs_eid"], "JKD"):
        t = f["surface"]["type"]
        lo = [round(c*1000, 3) for c in f["box"]["minCorner"]]
        hi = [round(c*1000, 3) for c in f["box"]["maxCorner"]]
        r = f["surface"].get("radius")
        print(" ", t, "r", round(r*1000, 3) if r else None,
              "x", lo[0], hi[0], "z", lo[2], hi[2], "area", round(f["area"]*1e6, 3))
