import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.rename_row(page, "Part 2", "Socket body")
    for pid, name in [("JHD", "Ball stud"), ("JKD", "Socket body")]:
        faces = common.faces(page, api, s["did"], s["wid"], s["bs_eid"], pid)
        zs = [(round(f["box"]["minCorner"][2]*1000, 3), round(f["box"]["maxCorner"][2]*1000, 3))
              for f in faces]
        print(name, "z extents:", zs,
              "vol", common.volume(page, api, s["did"], s["wid"], s["bs_eid"], pid))
        for f in faces:
            if f["surface"]["type"] == "cylinder":
                print("   cyl r", round(f["surface"]["radius"]*1000, 3))
