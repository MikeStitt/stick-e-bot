import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid = s["did"], s["wid"]
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.fill("input[type=text]", "t7 head mated")
    page.wait_for_timeout(500)
    page.click("textarea")
    page.keyboard.type("Tutorials 1-7 built at 2x: robot sizes, body with two shoulders and five "
                       "studs, head with its socket, ball and socket, and the head mated to the "
                       "neck by a ball mate.")
    page.wait_for_timeout(500)
    page.mouse.click(912, 322)
    page.wait_for_timeout(6000)
    r = api.api(page, "GET", f"/api/documents/d/{did}/versions")
    for v in r["body"][:5]:
        print(v["name"], v["id"])
