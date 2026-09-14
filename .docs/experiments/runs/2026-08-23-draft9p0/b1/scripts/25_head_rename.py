import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
common.save(head_eid="661eb771f054d4d12b351fbf")
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.rename_row(page, "Part Studio 1", "head")
    r = api.api(page, "GET", f"/api/documents/d/{s['did']}/w/{s['wid']}/elements")
    print([e["name"] for e in r["body"]])
