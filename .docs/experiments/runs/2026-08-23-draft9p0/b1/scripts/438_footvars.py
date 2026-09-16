import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
VARS = [
    ("#foot_l", "#torsoH"), ("#foot_w", "#torsoH / 2"), ("#ankle_h", "#torsoH / 4"),
    ("#plate", "12 mm"), ("#top_round", "8 mm"), ("#ball", "#torsoH / 8"),
    ("#wall", "#torsoH / 32"), ("#collar", "11 mm"), ("#grip", "3.6 mm"),
    ("#collar_r", "#ball / 2 + #wall"), ("#collar_down", "#collar - #grip"),
    ("#pedestal", "#plate - #collar_down"), ("#rib_w", "6 mm"), ("#rib_d", "2 mm"),
]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for n, v in VARS[lo:hi]:
        common.add_var(page, gui, n, v, settle=1200)
        print("added", n, v)
