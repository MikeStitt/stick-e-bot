#!/usr/bin/env python3
"""The report's isometric picture of the cup, and the workspace's name.

Rendered by `shadedviews` from the named version, so the picture is of the state
the report describes, then set on white with an even margin. Read only.

    uv run python .docs/experiments/2026-09-30-elephant-cup/iso.py
"""

import base64
import io
import json
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S

HERE = Path(__file__).parent
IDS = json.loads((HERE / "ids.json").read_text())
VERSION = "1f0631a4e8285baf2d33f860"
OUT = HERE / "report/source/cup-isometric.png"
SIZE = 1400


def main() -> int:
    did, wid, eid = IDS["did"], IDS["wid"], IDS["eid"]
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        S.require_signed_in(page)
        spaces = S.api(page, "GET", f"/api/documents/d/{did}/workspaces")["body"]
        print("workspaces:", [(w["name"], w["id"]) for w in spaces])
        res = S.api(page, "GET", f"/api/partstudios/d/{did}/v/{VERSION}/e/{eid}/shadedviews"
                                 f"?viewMatrix=isometric&outputHeight={SIZE}"
                                 f"&outputWidth={SIZE}&pixelSize=0&edges=show")
        # The render's background is transparent; the part is set on white with a margin.
        im = Image.open(io.BytesIO(base64.b64decode(res["body"]["images"][0]))).convert("RGBA")
        im = im.crop(im.getchannel("A").getbbox())
        pad = im.height // 12
        canvas = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), "white")
        canvas.alpha_composite(im, (pad, pad))
        im = canvas.convert("RGB")
        OUT.parent.mkdir(parents=True, exist_ok=True)
        im.save(OUT, optimize=True)
        print("wrote", OUT, im.size, f"{OUT.stat().st_size / 1024:.0f} KiB")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
