#!/usr/bin/env python3
"""Create the `elephant cup` document, once, and record its ids.

Onshape's document search does not index a new document for some minutes, so a
second run cannot find the first one's document and would make a duplicate. The
ids file is the guard: if it exists, this reads the document back and writes nothing.

    uv run python .docs/experiments/2026-09-30-elephant-cup/create.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S

DOC_NAME = "elephant cup"
TAB_NAME = "cup"
IDS = Path(__file__).with_name("ids.json")


def read_back(page, did, wid):
    name = S.api(page, "GET", f"/api/documents/{did}")["body"]["name"]
    els = S.api(page, "GET", f"/api/documents/d/{did}/w/{wid}/elements")["body"]
    return name, [(e["name"], e["elementType"], e["id"]) for e in els]


def rename_element(page, did, wid, eid, name):
    meta = S.api(page, "GET", f"/api/metadata/d/{did}/w/{wid}/e/{eid}")["body"]
    prop = next(p for p in meta["properties"] if p["name"] == "Name")
    res = S.api(page, "POST", f"/api/metadata/d/{did}/w/{wid}/e/{eid}",
                {"properties": [{"propertyId": prop["propertyId"], "value": name}]})
    if not res["ok"]:
        raise RuntimeError(f"could not rename {eid}: {json.dumps(res)[:300]}")


def main() -> int:
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        print("signed in as", S.require_signed_in(page))
        if IDS.exists():
            ids = json.loads(IDS.read_text())
            print("already created:", read_back(page, ids["did"], ids["wid"]))
            return 0

        doc = S.new_document(page, DOC_NAME)
        name, els = read_back(page, doc.did, doc.wid)
        print("created:", name, els)
        if name != DOC_NAME:
            raise RuntimeError(f"document {doc.did} reads back as {name!r}")
        S.pace(page)
        rename_element(page, doc.did, doc.wid, doc.eid, TAB_NAME)
        name, els = read_back(page, doc.did, doc.wid)
        print("read back:", name, els)
        IDS.write_text(json.dumps({"document": name, "did": doc.did, "wid": doc.wid,
                                   "eid": doc.eid, "elements": els}, indent=2) + "\n")
        print("wrote", IDS)
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
