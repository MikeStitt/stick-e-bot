import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

REST = [("stalk", "#ball / 2"), ("fit", "0.8 mm"), ("wall", "3 mm"),
        ("collar", "11 mm"), ("grip", "3.6 mm"), ("slit", "1.6 mm"),
        ("stud_len", "10 mm"), ("slit_in", "5 mm"), ("slit_out", "12 mm")]
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page); page.wait_for_timeout(1500)
    for name, val in REST:
        gui.clear(page)
        gui.search_tool(page, "Variable")
        ins = page.locator("#feature-dialog input")
        ins.nth(1).click(); ins.nth(1).fill(name); ins.nth(1).press("Tab")
        page.wait_for_timeout(500)
        ins.nth(2).click(); ins.nth(2).fill(val); ins.nth(2).press("Tab")
        page.wait_for_timeout(1500)
        print(name, "->", [l[0] for l in gui.labels(page)][0])
        gui.tick(page); page.wait_for_timeout(1500)
    print("tree:", gui.tree(page))
