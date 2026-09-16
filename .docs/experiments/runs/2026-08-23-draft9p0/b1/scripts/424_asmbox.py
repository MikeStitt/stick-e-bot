import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid, a = s["did"], s["wid"], s["asm_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    r = api.api(page, "GET", f"/api/assemblies/d/{did}/w/{wid}/e/{a}/boundingboxes")
    print({k: round(v*1000, 3) for k, v in r["body"].items() if k[0] in "lh"})
