import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
st = json.load(open(D + "state.json"))
DID, WID, EID = st["did"], st["wid"], st["ps_eid"]
PID = "JHD"
cands = [
    f"/api/partstudios/d/{DID}/w/{WID}/e/{EID}/bodydetails",
    f"/api/parts/d/{DID}/w/{WID}/e/{EID}/partid/{PID}/bodydetails",
    f"/api/parts/d/{DID}/w/{WID}/e/{EID}/partid/{PID}/boundingboxes",
    f"/api/parts/d/{DID}/w/{WID}/e/{EID}/partid/{PID}/massproperties",
]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    for c in cands:
        r = osx.api(page, "GET", c)
        b = r.get("body")
        tag = c.split("/e/")[1]
        if isinstance(b, dict) and b.get("status") in (404, 400):
            print(f"  {r.get('status')}  {tag}   -> {b.get('message')}")
        else:
            keys = list(b.keys()) if isinstance(b, dict) else f"list[{len(b)}]"
            print(f"  {r.get('status')}  {tag}   -> {keys}")
