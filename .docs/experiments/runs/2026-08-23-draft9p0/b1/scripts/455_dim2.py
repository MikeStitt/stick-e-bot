import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.mouse.move(1010, 620); page.wait_for_timeout(700)
    page.mouse.click(1010, 620); page.wait_for_timeout(700)
    page.mouse.click(1010, 620); page.wait_for_timeout(1200)
    page.screenshot(path=D+"tk47.png")
    from PIL import Image
    Image.open(D+"tk47.png").crop((700,300,1200,760)).resize((750,690)).save(D+"tk47c.png")
