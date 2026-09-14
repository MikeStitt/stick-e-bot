import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(925, 265); page.wait_for_timeout(1200)
    page.mouse.wheel(0, -600); page.wait_for_timeout(1500)
    page.mouse.move(925, 265); page.wait_for_timeout(1500)
    from PIL import Image
    page.screenshot(path=D+"tk30.png")
    Image.open(D+"tk30.png").crop((700,100,1200,500)).resize((1000,800)).save(D+"tk30c.png")
