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
    gui.name_feature(page, "mouth")
    gui.tick(page)
    print("tree:", gui.tree(page))
    print("bbox:", common.bbox(page, api, s["did"], s["wid"], s["head_eid"]))
    v = common.volume(page, api, s["did"], s["wid"], s["head_eid"], "JHD")
    print("volume:", v, "removed:", round(264721.438 - v, 3), "expected 1135.619")
    faces = common.faces(page, api, s["did"], s["wid"], s["head_eid"], "JHD")
    print("faces:", len(faces), Counter(f["surface"]["type"] for f in faces))
    for f in faces:
        t = f["surface"]["type"]
        lo = [round(c*1000, 3) for c in f["box"]["minCorner"]]
        hi = [round(c*1000, 3) for c in f["box"]["maxCorner"]]
        if t == "cylinder" and round(f["surface"]["radius"]*1000, 3) == 5.0:
            print("  slot cap r5  y", lo[1], "..", hi[1], " z", lo[2], "..", hi[2])
        if t == "plane" and abs(lo[1] + 27) < 1e-6 and abs(hi[1] + 27) < 1e-6:
            print("  plane at y=-27  x", lo[0], "..", hi[0], " z", lo[2], "..", hi[2],
                  " area", round(f["area"]*1e6, 3))
