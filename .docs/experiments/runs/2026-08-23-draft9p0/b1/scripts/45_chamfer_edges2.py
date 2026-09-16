import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

Z = -36.0
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    if page.locator("#feature-dialog").count():
        page.mouse.click(451, 93); page.wait_for_timeout(1800)
    gui.clear(page)
    s, cam = gui.px_per_mm(page)
    gui.search_tool(page, "Chamfer")
    for i, (name, pt) in enumerate([("front", (0, -30, Z)), ("back", (0, 30, Z)),
                                    ("left", (-36, 0, Z)), ("right", (36, 0, Z))]):
        px = tuple(round(v) for v in gui.project(page, *pt, cam=cam))
        gui.pick(page, px, name, add=(i > 0))
        print("   field now:", [l[0] for l in gui.labels(page) if " of " in l[0]])
    el = gui.number_fields(page)[0]
    gui.set_field(page, el, "6 mm")
    page.wait_for_timeout(1500)
    print("errors:", page.get_by_text("failed to regenerate", exact=False)
          .locator("visible=true").count())
    page.screenshot(path="hd19.png")
