import sys, math
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    fs = common.faces(page, api, s['did'], s['wid'], s['ps_eid'], "JMD")
    for f in fs:
        su = f["surface"]
        o = [round(v*1000, 4) for v in su.get("origin", [])]
        n = [round(v, 6) for v in (su.get("normal") or su.get("axis") or [])]
        ex = ("r=%.4f" % (su["radius"]*1000)) if "radius" in su else ""
        print("%-9s origin %-34s dir %-34s area %9.4f %s" % (su["type"], o, n, f["area"]*1e6, ex))
    print("volume", common.volume(page, api, s['did'], s['wid'], s['ps_eid'], "JMD"))
