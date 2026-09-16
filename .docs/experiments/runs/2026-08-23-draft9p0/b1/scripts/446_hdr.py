import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for x in (155, 185, 215):
        page.mouse.move(x, 129); page.wait_for_timeout(1200)
        page.screenshot(path=D+f"tk_hdr{x}.png")
    from PIL import Image
    for x in (155, 185, 215):
        Image.open(D+f"tk_hdr{x}.png").crop((40,115,500,200)).resize((920,170)).save(D+f"tk_hdr{x}c.png")
