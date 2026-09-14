import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(246, 229); page.wait_for_timeout(1500)
    print(page.evaluate("""() => Array.from(document.querySelectorAll('#feature-dialog input[type=checkbox]')).map(e => e.checked)"""))
    gui.tick(page); page.wait_for_timeout(4000)
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['head_eid']}")
    for pt in r["body"]: print(pt["partId"], pt["name"])
    print(common.bbox(page, api, s['did'], s['wid'], s['head_eid']))
    page.screenshot(path=D + "hs26.png")
