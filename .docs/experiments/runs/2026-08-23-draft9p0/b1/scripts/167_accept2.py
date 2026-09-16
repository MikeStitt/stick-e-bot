import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
s = common.load(); did, wid, eid = s["did"], s["wid"], s["bs_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(1400, 860)
    page.wait_for_timeout(1800)
    print("cursor", gui.cursor(page))
    gui.tick(page)
    page.wait_for_timeout(2500)
    r = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/features")
    sk = [f["message"] for f in r["body"]["features"] if f["message"].get("name") == "slit profile"][0]
    for c in sk.get("constraints", []):
        cm = c["message"]
        if cm.get("constraintType") != "CIRCULAR_PATTERN":
            continue
        seeds = sorted({pm["message"]["value"] for pm in cm["parameters"]
                        if pm["message"].get("parameterId", "").endswith(",0")})
        insts = {pm["message"]["parameterId"].split(",")[1] for pm in cm["parameters"]
                 if "," in pm["message"].get("parameterId", "")}
        print("seed entities:", seeds)
        print("instances:", sorted(insts))
    page.screenshot(path=D + "bs45.png")
