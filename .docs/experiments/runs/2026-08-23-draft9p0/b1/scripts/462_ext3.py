import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(276, 313); page.wait_for_timeout(1500)
    f = gui.number_fields(page)
    print("fields", len(f))
    if len(f) > 1:
        gui.set_field(page, f[1], "#collar_down")
    page.mouse.click(453, 230); page.wait_for_timeout(1500)   # flip direction
    page.screenshot(path=D+"tk54.png")
    from PIL import Image
    Image.open(D+"tk54.png").crop((240,80,470,450)).resize((690,1110)).save(D+"tk54c.png")
