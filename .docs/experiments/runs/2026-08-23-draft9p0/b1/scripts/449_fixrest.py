import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
PAIRS = [("#? = 48 mm", "foot_w"), ("#? = 24 mm", "ankle_h"), ("#? = 12 mm", "plate"),
         ("#? = 8 mm", "top_round"), ("#? = 12 mm", "ball"), ("#? = 3 mm", "wall"),
         ("#? = 11 mm", "collar"), ("#? = 3.6 mm", "grip")]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for row, nm in PAIRS[lo:hi]:
        x, y = gui.row(page, row)
        page.mouse.dblclick(x, y); page.wait_for_timeout(1800)
        els = page.query_selector_all("#feature-dialog input")
        els[1].click(); page.keyboard.press("Meta+A"); page.keyboard.type(nm)
        page.keyboard.press("Tab"); page.wait_for_timeout(900)
        print(nm, "->", page.query_selector("#feature-dialog").inner_text().split("\n")[0])
        gui.tick(page); page.wait_for_timeout(1500)
