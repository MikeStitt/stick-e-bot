import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
from PIL import Image
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for i, x in enumerate((436, 486, 382)):
        page.keyboard.press("Escape"); page.wait_for_timeout(400)
        page.mouse.click(x, 58); page.wait_for_timeout(900)
        page.screenshot(path=D+f"tk58_{i}.png")
        Image.open(D+f"tk58_{i}.png").crop((x-60,70,x+300,240)).resize((720,340)).save(D+f"tk58_{i}c.png")
