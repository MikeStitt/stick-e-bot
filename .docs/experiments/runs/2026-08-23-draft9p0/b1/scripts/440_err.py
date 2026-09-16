import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    els = page.query_selector_all("#feature-dialog input")
    for i, e in enumerate(els):
        print(i, repr(e.get_attribute("value")), e.get_attribute("title"))
    page.mouse.move(370, 205); page.wait_for_timeout(1500)
    page.screenshot(path=D+"tk41.png")
    from PIL import Image
    Image.open(D+"tk41.png").crop((240,80,900,400)).resize((1320,640)).save(D+"tk41c.png")
