import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.name_feature(page, "second eye")
    gui.tick(page)
    print("tree:", gui.tree(page))
    r = api.api(page, "GET",
                f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}/boundingboxes")
    print("bbox mm:", {k: round(v * 1000, 3) for k, v in r["body"].items() if k[0] in "lh"})
    b = api.api(page, "GET",
                f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}/partid/JHD/bodydetails")
    faces = b["bodies"]["JHD"]["faces"]
    from collections import Counter
    print("faces:", len(faces), Counter(f["surface"]["type"] for f in faces))
    cyl = sorted({round(f["surface"]["radius"] * 1000, 3) for f in faces
                  if f["surface"]["type"] == "cylinder"})
    print("cylinder radii:", cyl)
    gui.frame(page, D + "mi5.png")
