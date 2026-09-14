import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(276, 360); page.wait_for_timeout(3000)
    page.screenshot(path=D+"tk89.png")
    gui.tick(page); page.wait_for_timeout(4000)
    s = common.load()
    for name, fid, st in common.features(page, api, s["did"], s["wid"], s["foot_eid"])[-2:]:
        print(f"{st:8} {name}")
    pid = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['foot_eid']}")["body"][0]["partId"]
    print("vol", common.volume(page, api, s["did"], s["wid"], s["foot_eid"], pid))
    lev = {}
    for f in common.faces(page, api, s["did"], s["wid"], s["foot_eid"], pid):
        su = f.get("surface", {})
        if su.get("type") == "plane":
            n = su.get("normal") or []
            if n and abs(n[2]) > 0.99:
                z = round(su["origin"][2] * 1000, 3)
                lev[z] = lev.get(z, 0) + 1
    print("z levels:", dict(sorted(lev.items())))
