#!/usr/bin/env python3
"""Phase A0 — the ten tabs of `stickbot-draft9p5`, in Phase B's build order.

Nothing is copied and nothing is branched. The document is named by its id, not
found by search: Onshape's document search does not index a document for some
minutes after it is created, so `find_document` answers None for a document that
exists and a second run of a create-if-missing script makes a duplicate. One was
made and trashed on 2026-09-18.

The REST grant names `stickbot-draft9p5` and no other document, so the name is
read back from Onshape and nothing is written unless it matches.

What was measured on 2026-09-18, because the 2026-08-30 scripts' endpoints 404:

- a Variable Studio is created by `POST /api/variables/d/{did}/w/{wid}/variablestudio`.
- an element is renamed by a metadata write, `POST /api/metadata/d/{did}/w/{wid}/e/{eid}`,
  carrying the `Name` property's id read back from the matching GET.
- an Assembly cannot be deleted while its Bill of Materials exists; delete the BOM
  first, or the delete is a 409.
- the last element in a document cannot be deleted at all, also a 409.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/a0_create.py
"""

from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S
from stickbot import repo_root

DOC_NAME = "stickbot-draft9p5"
DID = "2f08b54d795df0ee6b72e321"
WID = "1d8e4c837228c90bab9ff062"
RESULTS = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/results"

# The ten tabs, in the order Phase B builds them, which is the order they sit in.
TABS = [
    ("robot sizes", "VARIABLESTUDIO"),
    ("ball and socket", "PARTSTUDIO"),
    ("hinge", "PARTSTUDIO"),
    ("body", "PARTSTUDIO"),
    ("head", "PARTSTUDIO"),
    ("foot", "PARTSTUDIO"),
    ("u limb", "PARTSTUDIO"),
    ("l limb", "PARTSTUDIO"),
    ("gripper", "PARTSTUDIO"),
    ("stickbot", "ASSEMBLY"),
]

CREATE_PATH = {
    "PARTSTUDIO": "/api/partstudios/d/{did}/w/{wid}",
    "ASSEMBLY": "/api/assemblies/d/{did}/w/{wid}",
    "VARIABLESTUDIO": "/api/variables/d/{did}/w/{wid}/variablestudio",
}


def elements(page):
    res = S.api(page, "GET", f"/api/documents/d/{DID}/w/{WID}/elements")
    if not res["ok"]:
        raise RuntimeError(f"could not list elements: {res['status']}")
    return res["body"]


def tabs_of(els):
    """The tabs, without the Bill of Materials an Assembly brings with it."""
    return [e for e in els if e["elementType"] != "BILLOFMATERIALS"]


def confirm_name(page):
    res = S.api(page, "GET", f"/api/documents/{DID}")
    if not res["ok"]:
        raise RuntimeError(f"could not read document {DID}: {res['status']}")
    name = res["body"]["name"]
    if name != DOC_NAME:
        raise RuntimeError(f"document {DID} is named {name!r}, not {DOC_NAME!r}")
    return name


def create(page, name, element_type):
    path = CREATE_PATH[element_type].format(did=DID, wid=WID)
    res = S.api(page, "POST", path, {"name": name})
    if not res["ok"]:
        raise RuntimeError(f"could not make {element_type} {name!r}: {res['status']}")
    return res["body"]["id"]


def rename_element(page, eid, name):
    """Rename through metadata, with the property id read rather than hardcoded."""
    meta = S.api(page, "GET", f"/api/metadata/d/{DID}/w/{WID}/e/{eid}")
    if not meta["ok"]:
        raise RuntimeError(f"could not read metadata for {eid}: {meta['status']}")
    prop = next(p for p in meta["body"]["properties"] if p["name"] == "Name")
    res = S.api(page, "POST", f"/api/metadata/d/{DID}/w/{WID}/e/{eid}",
                {"properties": [{"propertyId": prop["propertyId"], "value": name}]})
    if not res["ok"] or res["body"].get("status") != "SUCCEEDED":
        raise RuntimeError(f"could not rename {eid} to {name!r}: {json.dumps(res)[:200]}")


def main() -> int:
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        print("signed in as", S.require_signed_in(page))
        print(f"name read back from Onshape: {confirm_name(page)}")
        print(f"did={DID}\nwid={WID}")

        have = tabs_of(elements(page))
        if [(e["name"], e["elementType"]) for e in have] == TABS:
            print("the ten tabs are already in place")
        else:
            # The one element a document must keep becomes the first tab.
            if len(have) == 1 and have[0]["elementType"] == TABS[0][1]:
                if have[0]["name"] != TABS[0][0]:
                    rename_element(page, have[0]["id"], TABS[0][0])
                    print(f"  renamed the lone element to {TABS[0][0]!r}")
                    S.pace(page)
                todo = TABS[1:]
            else:
                todo = TABS
            present = {e["name"] for e in tabs_of(elements(page))}
            for name, element_type in todo:
                if name in present:
                    continue
                eid = create(page, name, element_type)
                S.pace(page)
                got = {e["id"]: e["name"] for e in elements(page)}
                if got.get(eid) != name:
                    rename_element(page, eid, name)
                    S.pace(page)
                print(f"  made {element_type:<15} {name:<16} {eid}")

        final = elements(page)
        print("\ntabs, in order:")
        for e in final:
            print(f"  {e['elementType']:<16} {e['name']:<18} {e['id']}")

        names = [(e["name"], e["elementType"]) for e in tabs_of(final)]
        if names != TABS:
            raise RuntimeError(f"tabs are not the ten the plan names, in order: {names}")
        print("\nread back: the ten tabs, in Phase B's build order")

        RESULTS.mkdir(parents=True, exist_ok=True)
        (RESULTS / "elements.json").write_text(
            json.dumps({"document": DOC_NAME, "did": DID, "wid": WID, "elements": final},
                       indent=2) + "\n")
        print(f"wrote {RESULTS / 'elements.json'}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
