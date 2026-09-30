#!/usr/bin/env python3
"""Pictures of the cup, written to a folder outside the repository.

Renders from `shadedviews` in three views, then opens `cup profile` for edit in the
agent browser and takes the sketch square on, which is where an under-defined
entity shows blue. Leaves the sketch with Escape and changes nothing.

    uv run python .docs/experiments/2026-09-30-elephant-cup/look.py <out-dir>
"""

from __future__ import annotations

import base64
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from stickbot import onshape_gui as gui
from stickbot import onshape_screen as screen
from stickbot import onshape_session as S

HERE = Path(__file__).parent
IDS = json.loads((HERE / "ids.json").read_text())
DOC = S.Doc(IDS["did"], IDS["wid"], IDS["eid"])
VIEWS = ["isometric", "front", "bottom"]


def main() -> int:
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser, _ctx, page = gui.connect(p)
        S.require_signed_in(page)
        for view in VIEWS:
            res = S.api(page, "GET", f"/api/partstudios/{DOC.path}/shadedviews"
                                     f"?viewMatrix={view}&outputHeight=600&outputWidth=600"
                                     f"&pixelSize=0&edges=show")
            img = res["body"]["images"][0]
            path = out / f"cup-{view}.png"
            path.write_bytes(base64.b64decode(img))
            print("wrote", path)

        gui.open_doc(page, DOC)
        gui.no_banner(page)
        if not gui.planes_hidden(page):
            gui.planes(page, shown=False)
        xy = gui.row(page, "cup profile")
        page.mouse.dblclick(*xy)
        page.wait_for_timeout(3000)
        page.mouse.move(*screen.CENTER)
        page.keyboard.press("n")
        page.wait_for_timeout(1500)
        gui.fit(page)
        gui.still(page)
        path = out / "cup-profile-sketch.png"
        page.screenshot(path=str(path))
        print("wrote", path)
        page.keyboard.press("Escape")
        page.wait_for_timeout(1500)
        bad = {k: v for k, v in S.feature_states(page, DOC).items() if v != "OK"}
        print("states not OK after leaving the sketch:", bad or "none")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
