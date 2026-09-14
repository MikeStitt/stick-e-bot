import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(252, 410)
    page.wait_for_timeout(2500)
    gui.clear(page)
    page.wait_for_timeout(1000)
    for r in gui.tree(page):
        print(r)
    page.screenshot(path=F+"cad.assembly.fix_body.png")
    from PIL import Image
    Image.open(F+"cad.assembly.fix_body.png").crop((40,140,250,340)).resize((630,600)).save(D+"tk23c.png")
