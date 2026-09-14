import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(585, 777)   # Delete
    page.wait_for_timeout(1500)
    dlg = page.locator("div[role='dialog']:visible")
    print("dialogs:", dlg.count())
    if dlg.count():
        print(dlg.first.inner_text()[:300])
        for name in ["Delete", "OK", "Yes"]:
            b = dlg.first.get_by_role("button", name=name, exact=True)
            if b.count():
                print("clicking", name); b.first.click(); break
        page.wait_for_timeout(2000)
    page.screenshot(path="tabstrip2.png", clip={"x": 0, "y": 940, "width": 900, "height": 60})
