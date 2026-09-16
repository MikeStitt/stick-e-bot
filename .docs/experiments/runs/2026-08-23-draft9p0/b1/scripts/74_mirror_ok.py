import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from collections import Counter
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api
s = common.load()
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page); page.wait_for_timeout(2500)
    b = api.api(page, "GET",
        f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}/partid/JHD/bodydetails")["body"]
    faces = b["bodies"][0]["faces"]
    print("faces:", len(faces), Counter(f["surface"]["type"] for f in faces))
    for f in faces:
        if f["surface"]["type"] == "cylinder" and round(f["surface"]["radius"]*1000, 3) == 10.0:
            print("  eye disc origin", [round(c*1000, 3) for c in f["surface"]["origin"]])
    print("tree:", gui.tree(page))
    gui.frame(page, D + "mi9.png")
