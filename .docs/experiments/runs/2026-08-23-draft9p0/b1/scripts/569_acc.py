import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    els = gui.number_fields(page)
    print("depth field =", repr(els[0].input_value()))
    gui.tick(page)
    page.wait_for_timeout(4000)
    print(common.bbox(page, api, s["did"], s["wid"], s["hinge_eid"]))
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['hinge_eid']}")
    print("parts", [(x["partId"], x["name"]) for x in r["body"]])
    pid = r["body"][0]["partId"]
    print("vol", common.volume(page, api, s["did"], s["wid"], s["hinge_eid"], pid))
