#!/usr/bin/env python3
"""Publish a named version of `elephant cup`, and read it back.

    uv run python .docs/experiments/2026-09-30-elephant-cup/version.py "<name>"
"""

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S

IDS = json.loads((Path(__file__).parent / "ids.json").read_text())


def main(name: str) -> int:
    did, wid = IDS["did"], IDS["wid"]
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        res = S.api(page, "POST", f"/api/documents/d/{did}/versions",
                    {"documentId": did, "workspaceId": wid, "name": name})
        if not res["ok"]:
            raise RuntimeError(f"could not publish {name!r}: {res['status']} "
                               f"{json.dumps(res.get('body'))[:200]}")
        S.pace(page)
        versions = S.api(page, "GET", f"/api/documents/d/{did}/versions")["body"]
        back = next(v for v in versions if v["id"] == res["body"]["id"])
        print(f"published {back['name']!r}  id {back['id']}  {back['createdAt']}")
        print(f"  https://cad.onshape.com/documents/{did}/v/{back['id']}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
