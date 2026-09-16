import sys, collections
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    r = api.api(page, "GET",
                f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}/partid/JHD/bodydetails")
    b = r["body"]["bodies"][0]
    print("faces:", len(b["faces"]), "edges:", len(b.get("edges", [])))
    kinds = collections.Counter(f["surface"]["type"] for f in b["faces"])
    print(kinds)
    bot = [f for f in b["faces"] if abs(f["box"]["maxCorner"][2] + 0.036) < 1e-9]
    for f in bot:
        print(" bottom-touching:", f["id"], f["surface"]["type"],
              round(f["area"] * 1e6, 2), "mm2",
              [round(v * 1000, 2) for v in f["box"]["minCorner"]],
              [round(v * 1000, 2) for v in f["box"]["maxCorner"]])
