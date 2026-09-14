"""Does anything in `stickbot-draft9p4` still reach back into `stickbot-draft9p3`?

    uv run --project . python .docs/experiments/runs/2026-09-08-draft9p4/scripts/p_no_refs.py

A workspace copy is where this defect comes from: a derive that keeps pointing at the document
it was copied out of looks fine and moves when the other document moves. Two independent reads,
the way draft9p1p5 and draft9p1p6 did it -- `externalreferences`, and a text search of every
feature's JSON for the source document's ids. Read only.
"""
import json
import sys
import time

sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge/tools")
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")

from playwright.sync_api import sync_playwright

import onshape_gui as gui
import onshape_session as api

DOCS = json.load(open("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/"
                      "runs/2026-09-08-draft9p4/reference/documents.json"))
DID = DOCS["build"]["did"]
WID = DOCS["build"]["wid"]
SRC = DOCS["build"]["copiedFrom"]
PACE = 2.5

# every id that belongs to stickbot-draft9p3
NEEDLES = {SRC["did"]: "draft9p3 document", SRC["wid"]: "draft9p3 workspace"}
for e in json.load(open("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/"
                        "runs/2026-08-29-draft9p3/reference/documents.json")
                   ) if False else []:
    pass


def get(page, path):
    time.sleep(PACE)
    r = api.api(page, "GET", path)
    if r["status"] != 200:
        raise SystemExit(f"{path} answered {r['status']}: {str(r['body'])[:200]}")
    return r["body"]


def main():
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        parts = [e for e in DOCS["build"]["elements"] if e["type"] == "PARTSTUDIO"]
        gui.open_doc(page, api.Doc(DID, WID, parts[0]["id"]))
        print("signed in as:", api.require_signed_in(page))
        print(f"checking {DOCS['build']['name']} for {SRC['name']}'s ids\n")

        ext = get(page, f"/api/documents/d/{DID}/w/{WID}/externalreferences")
        for key in ("elementExternalReferences", "elementRevisionReferences"):
            block = ext.get(key) or {}
            n = sum(len(v) for v in block.values()) if isinstance(block, dict) else len(block)
            print(f"  {key}: {n} reference(s)")
            if n:
                print("   ", json.dumps(block)[:600])
        has_ws = ext.get("elementsToHasWorkspaceReferences") or \
                 ext.get("elementToHasWorkspaceReferences") or {}
        print(f"  hasWorkspaceReferences true for: "
              f"{[k for k, v in has_ws.items() if v] if isinstance(has_ws, dict) else has_ws}")
        print(f"  documents named: {[d.get('name') for d in ext.get('documents', [])]}")
        print(f"  versions named:  {[v.get('name') for v in ext.get('versions', [])]}\n")

        hits = 0
        for e in parts:
            body = get(page, f"/api/partstudios/d/{DID}/w/{WID}/e/{e['id']}/features")
            text = json.dumps(body)
            found = [what for nid, what in NEEDLES.items() if nid in text]
            print(f"  {e['name']:18} {len(body['features']):3} features, "
                  f"{'clean' if not found else 'HIT: ' + ', '.join(found)}")
            hits += len(found)
        print(f"\n{'no reference leaves the document' if not hits else str(hits) + ' HIT(S)'}")
        browser.close()


main()
