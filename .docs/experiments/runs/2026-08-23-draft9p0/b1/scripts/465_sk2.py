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
    x, y = gui.row(page, "Top")
    page.mouse.click(x, y); page.wait_for_timeout(700)
    page.mouse.click(155, 58); page.wait_for_timeout(4000)
    page.keyboard.press("Shift+5"); page.wait_for_timeout(1200)
    gui.fit(page); page.wait_for_timeout(1500)
    names = []
    for tx in range(190, 1050, 1):
        pass
    page.screenshot(path=D+"tk56.png")
    from PIL import Image
    Image.open(D+"tk56.png").crop((180,42,1050,76)).resize((1740,68)).save(D+"tk56c.png")
