"""A Part Studio's features as Onshape holds them, written to a file.

    uv run --project . python tools/read_features.py <did> <wid> <eid> <out.json>

The reference reads under a run's `reference/` were written this way, so a tab read now can be
diffed against one with [`diff_features.py`](diff_features.py). Read only: the route is a GET and
nothing on the page is touched.
"""
import json
import sys

from playwright.sync_api import sync_playwright

import onshape_gui as gui
import onshape_session as api


def main(did, wid, eid, out):
    doc = api.Doc(did, wid, eid)
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        gui.open_doc(page, doc)
        page.wait_for_timeout(4000)
        r = api.api(page, "GET", f"/api/partstudios/{doc.path}/features")
    if r["status"] != 200:
        raise SystemExit(f"the features route answered {r['status']}")
    json.dump(r["body"], open(out, "w"), indent=1)
    print(f"{len(r['body']['features'])} features -> {out}")


if __name__ == "__main__":
    main(*sys.argv[1:5])
