import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from collections import Counter
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
def head_faces(page, pid="JHD"):
    b = api.api(page, "GET",
        f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}/partid/{pid}/bodydetails")["body"]
    return b["bodies"][0]["faces"]

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    faces = head_faces(page)
    print("faces:", len(faces), Counter(f["surface"]["type"] for f in faces))
    for f in faces:
        if f["surface"]["type"] == "cylinder":
            o = [round(c*1000, 3) for c in f["surface"]["origin"]]
            print("  cyl r", round(f["surface"]["radius"]*1000, 3), "origin", o,
                  "area", round(f["area"]*1e6, 3))
    m = api.api(page, "GET",
        f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}/partid/JHD/massproperties")["body"]
    print("volume mm3:", round(m["bodies"][0]["volume"][0]*1e9, 3))
