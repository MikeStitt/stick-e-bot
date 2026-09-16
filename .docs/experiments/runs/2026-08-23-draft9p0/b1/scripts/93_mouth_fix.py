import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from collections import Counter
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.row(page, "mouth")
    page.mouse.dblclick(x, y); page.wait_for_timeout(2500)
    fields = gui.number_fields(page)
    print("fields before:", [f.input_value() for f in fields])
    el = fields[1]
    el.click(); page.wait_for_timeout(300)
    el.fill("30 mm"); el.press("Tab"); page.wait_for_timeout(2500)
    print("fields after:", [f.input_value() for f in gui.number_fields(page)])
    gui.tick(page); page.wait_for_timeout(2500)
    v = common.volume(page, api, s["did"], s["wid"], s["head_eid"], "JHD")
    print("volume:", v, "removed:", round(264721.438 - v, 3))
    faces = common.faces(page, api, s["did"], s["wid"], s["head_eid"], "JHD")
    print("faces:", len(faces), Counter(f["surface"]["type"] for f in faces))
    for f in faces:
        if f["surface"]["type"] == "cylinder" and round(f["surface"]["radius"]*1000, 3) == 5.0:
            lo = [round(c*1000, 3) for c in f["box"]["minCorner"]]
            hi = [round(c*1000, 3) for c in f["box"]["maxCorner"]]
            print("  slot cap r5  y", lo[1], "..", hi[1], " z", lo[2], "..", hi[2],
                  " x", lo[0], "..", hi[0])
