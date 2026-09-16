import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(1500)
    gui.clear(page)
    page.mouse.click(20, 95); page.wait_for_timeout(2500)
    el = page.query_selector("input[type=text]")
    el.click(); page.keyboard.press("Meta+A"); page.keyboard.type("t10 u limb")
    page.wait_for_timeout(400)
    ta = page.query_selector("textarea")
    if ta:
        ta.click()
        page.keyboard.type("Upper limb built at 2x in the brief's frame: socket derived at base origin so the "
                           "ball centre is the studio origin, limb hanging down #limbSeg from the collar's bottom "
                           "face, fork on the far end. shoulder end on Vertex of Origin, elbow end between the two "
                           "axle pockets. Segment 100.4, part 116 long.")
    page.wait_for_timeout(500)
    gui.frame(page, D + "frames/cad.parts.u_limb.version.png")
    page.mouse.click(912, 322); page.wait_for_timeout(6000)
    s = common.load()
    vs = api.api(page, "GET", f"/api/documents/d/{s['did']}/versions")["body"]
    for v in vs[:3]:
        print(v["name"], v["id"])
