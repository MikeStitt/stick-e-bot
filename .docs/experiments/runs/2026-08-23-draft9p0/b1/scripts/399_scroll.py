import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(140, 400)
    for _ in range(10):
        page.mouse.wheel(0, 300); page.wait_for_timeout(120)
    page.wait_for_timeout(1200)
    print(gui.row(page, "neck connector on torso"))
    from PIL import Image
    page.screenshot(path=D+"tk17.png")
    Image.open(D+"tk17.png").crop((40,140,250,700)).resize((420,1120)).save(D+"tk17c.png")
