"""Does `stickbot-draft9p3`'s workspace still hold what its last version holds?

    uv run --project . python .docs/experiments/runs/2026-09-08-draft9p4/scripts/p_ws_vs_version.py

The copy route copies a workspace, and the plan asks for the version, so the two have to be
shown to be the same model before the copy stands in for the branch. Compares the Variable
Studio's rows, every tab's feature names and types in order, and every feature's status.
Read only.
"""
import json
import sys
import time


from playwright.sync_api import sync_playwright

from stickbot import onshape_gui as gui
from stickbot import onshape_session as api

DID = "50b2d87357670c07c2fbcb89"
WID = "a49825ea9aa838bdfae7b78d"
VID = "f94cbf2e4657300be13507d2"          # tutorial 10 - the upper limb
PACE = 2.5

TABS = [
    ("robot sizes", "b37a5f099dea8bdd5f622931", "variables"),
    ("body", "931b7af8544d60df904361c3", "part"),
    ("head", "7784299f6eae122ff3283974", "part"),
    ("ball and socket", "45e967b1779a75776404e8e0", "part"),
    ("foot", "4b3cf11d89bf019f9d416b77", "part"),
    ("hinge", "965ca787810d0eb0f3aefcf1", "part"),
    ("u limb", "a9f1f5d3718ed1746fdf0e47", "part"),
]


def get(page, path):
    time.sleep(PACE)
    r = api.api(page, "GET", path)
    if r["status"] != 200:
        raise SystemExit(f"{path} answered {r['status']}: {str(r['body'])[:200]}")
    return r["body"]


def digest(page, scope, eid, kind):
    if kind == "variables":
        body = get(page, f"/api/variables/d/{DID}/{scope}/e/{eid}/variables")
        studios = body if isinstance(body, list) else [body]
        return [(r["name"], r["expression"])
                for s in studios for r in s.get("variables", [])]
    body = get(page, f"/api/partstudios/d/{DID}/{scope}/e/{eid}/features")
    out = []
    states = {s["key"]: s["value"]["message"]["featureStatus"]
              for s in body.get("featureStates", [])}
    for f in body["features"]:
        m = f["message"]
        out.append((m["featureType"], m["name"], states.get(m["featureId"], "?")))
    return out


def main():
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        gui.open_doc(page, api.Doc(DID, WID, TABS[1][1]))
        print("signed in as:", api.require_signed_in(page))

        ws = get(page, f"/api/documents/d/{DID}/w/{WID}/currentmicroversion")
        vm = get(page, f"/api/documents/d/{DID}/v/{VID}/currentmicroversion")
        print(f"workspace microversion: {ws.get('microversion')}")
        print(f"version   microversion: {vm.get('microversion')}")
        print(f"same: {ws.get('microversion') == vm.get('microversion')}\n")

        bad = 0
        for name, eid, kind in TABS:
            a = digest(page, f"w/{WID}", eid, kind)
            b = digest(page, f"v/{VID}", eid, kind)
            same = a == b
            bad += not same
            print(f"{name:18} {len(a):3} in workspace, {len(b):3} in version -- "
                  f"{'same' if same else 'DIFFER'}")
            if not same:
                for i, (x, y) in enumerate(zip(a, b)):
                    if x != y:
                        print(f"    row {i}: workspace {x}\n            version   {y}")
                if len(a) != len(b):
                    print(f"    workspace has {len(a)}, version has {len(b)}")
        print("\nall tabs agree" if not bad else f"\n{bad} tab(s) differ")
        browser.close()


main()
