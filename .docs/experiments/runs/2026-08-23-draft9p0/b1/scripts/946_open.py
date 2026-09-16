import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
s = common.load()
URL = f"https://cad.onshape.com/documents/{s['did']}/w/{s['wid']}/e/{s['gr_eid']}"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    print("pages", [(pg.url[:60], pg.evaluate("window.name")) for pg in ctx.pages])
    page = ctx.new_page()
    page.set_viewport_size({"width": 1600, "height": 1000})
    page.evaluate(f"window.name = {common.MARK!r}")
    page.goto(URL); page.wait_for_timeout(25000)
    print("name", page.evaluate("window.name"))
    print("url", page.url[-40:])
    page.screenshot(path=D+"gr06.png")
