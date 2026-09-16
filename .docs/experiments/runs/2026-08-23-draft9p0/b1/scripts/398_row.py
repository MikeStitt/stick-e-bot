import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    print(gui.row(page, "neck connector on torso"))
    print(gui.row(page, "copy ball stud"))
    from PIL import Image
    page.screenshot(path=D+"tk16.png")
    Image.open(D+"tk16.png").crop((40,140,250,700)).resize((420,1120)).save(D+"tk16c.png")
