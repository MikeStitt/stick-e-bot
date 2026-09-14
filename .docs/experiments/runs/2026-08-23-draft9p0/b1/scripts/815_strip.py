import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
KILL = ["shoulder end", "combine parts", "move fork", "add fork",
        "mate for fork", "move socket", "mate for socket", "limb", "limb section"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(1500)
    gui.clear(page)
    for n in KILL:
        common.delete_row(page, gui, n)
        page.wait_for_timeout(1800)
        print("deleted", n)
    page.wait_for_timeout(2500)
    print(gui.tree(page))
