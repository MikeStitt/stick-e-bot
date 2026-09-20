#!/usr/bin/env python3
"""Export every printed part as binary STL, and check each file is whole.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/c_export_stl.py

Ring 3 asks for the print files and for each part to be one solid. A binary STL
says the first part itself: the header holds a triangle count, and a whole file is
exactly `84 + 50 × count` bytes long, so a truncated download is arithmetic rather
than a guess.

**`/stl` needs a client the rest of this draft does not use.** It answers with a
redirect to another host, and every other call here is a `fetch` from inside the
Onshape page, which is same-origin: it dies with *Failed to fetch* and says
nothing about why. Playwright's own request context carries the browser's cookies,
follows the redirect and is not bound by CORS, so it fetches what the page cannot.

Written a second time because the first was a throwaway and the gripper changed
after it ran.
"""

from __future__ import annotations

import sys
from pathlib import Path

from stickbot import onshape_session as api

DID, WID = "2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062"
TABS = {"body": "5441067befc71f1e3b91482e", "head": "303898bd4ba38fc3957b0a21",
        "foot": "229aa0900e5a7e7aa4768c6f", "u limb": "fc89b8128993be73a0c9f092",
        "l limb": "be3bd8b485e32946c24ed799", "gripper": "a3a4fac68ffb7372a7803003"}
OUT = Path("/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-stick-e-bot"
           "/c3730b06-661a-42fb-887a-a5f90835fc73/scratchpad/stl")


def main(only: str | None = None) -> int:
    OUT.mkdir(exist_ok=True)
    with api.sync_playwright() as pw:
        browser, ctx, page = api.connect(pw)
        for tab, eid in TABS.items():
            if only and tab != only:
                continue
            base = f"/api/v10/parts/d/{DID}/w/{WID}/e/{eid}"
            parts = api._raw_api(page, "GET", base)["body"]
            for p in parts:
                url = (f"https://cad.onshape.com{base}/partid/{p['partId']}/stl"
                       "?mode=binary&units=millimeter&grouping=true")
                r = page.request.get(url)
                if not r.ok:
                    print(f"  {tab:<10} {p['name']:<12} -> {r.status}")
                    continue
                data = r.body()
                path = OUT / f"{p['name'].replace(' ', '-')}.stl"
                path.write_bytes(data)
                count = int.from_bytes(data[80:84], "little")
                whole = len(data) == 84 + 50 * count
                print(f"  {tab:<10} {p['name']:<12} {count:>7} triangles"
                      f"  {len(data):>9} bytes  {'whole' if whole else 'TRUNCATED'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
