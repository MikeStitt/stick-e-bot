#!/usr/bin/env python3
"""Publish a named version of `stickbot-draft9p5`, and read it back.

Ring 2 ends each tab with one, so the next tab derives from something that
cannot move. That is also what the *Recovery point* gate asks for.

    uv run python .../scripts/publish_version.py "tab 1 - robot sizes"
"""

from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S

DID = "2f08b54d795df0ee6b72e321"
WID = "1d8e4c837228c90bab9ff062"


def main(name: str) -> int:
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        res = S.api(page, "POST", f"/api/documents/d/{DID}/versions",
                    {"documentId": DID, "workspaceId": WID, "name": name})
        if not res["ok"]:
            raise RuntimeError(f"could not publish {name!r}: "
                               f"{res['status']} {json.dumps(res.get('body'))[:200]}")
        made = res["body"]
        S.pace(page)
        versions = S.api(page, "GET", f"/api/documents/d/{DID}/versions")["body"]
        back = next((v for v in versions if v["id"] == made["id"]), None)
        if back is None:
            raise RuntimeError(f"version {made['id']} is not in the document's list")
        print(f"published {back['name']!r}  id {back['id']}")
        print(f"  https://cad.onshape.com/documents/{DID}/v/{back['id']}")
        print(f"  the document now holds {len(versions)} versions")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
