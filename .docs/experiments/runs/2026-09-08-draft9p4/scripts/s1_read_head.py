"""What `stickbot-draft9p4`'s head tab holds before the spike touches it.

    uv run --project . python -u .docs/experiments/runs/2026-09-08-draft9p4/scripts/s1_read_head.py

Read only. Every call is a GET, except the FeatureScript evaluate, which writes nothing.

Answers three things the spike needs:
  - where the socket's cavity sphere is, and how big
  - what `head mate` and `socket mount point` were built with, parameter by parameter
  - where every mate connector in the tab actually sits, in millimeters
"""
import json
import sys
import time


from playwright.sync_api import sync_playwright

from stickbot import repo_root
from stickbot import onshape_gui as gui
from stickbot import onshape_session as api

DID = "fe052e606c96bb7cc5aaf59f"
WID = "0ff70e8921be572d630dd9cc"
HEAD = "95fe567f38e1c8c891bc94a3"
OUT = str(repo_root()) + "/.docs/experiments/runs/2026-09-08-draft9p4/log"

# Every mate connector body in the tab, with its origin and its z axis, in millimeters.
CONNECTORS = """function(context is Context, queries is map)
{
    var s = "";
    for (var b in evaluateQuery(context, qBodyType(qEverything(EntityType.BODY), BodyType.MATE_CONNECTOR)))
    {
        var cs = evMateConnector(context, { "mateConnector" : b });
        s = s ~ toString(cs.origin / millimeter) ~ "  z=" ~ toString(cs.zAxis) ~ "\\n";
    }
    return s;
}"""


def get(page, path):
    time.sleep(0.8)
    r = api.api(page, "GET", path)
    return r["status"], r["body"]


def show(param, indent="      "):
    """One parameter of a feature, in the form the difference shows up in."""
    pid = param.get("parameterId")
    t = param.get("btType", "")
    if "Queries" in t:
        qs = param.get("queries") or []
        ids = [g for q in qs for g in (q.get("geometryIds") or [])]
        return f"{indent}{pid:26s} {len(qs)} query, ids {ids}"
    if "Enum" in t:
        return f"{indent}{pid:26s} {param.get('value')}"
    if "Bool" in t:
        return f"{indent}{pid:26s} {param.get('value')}"
    if "Quantity" in t:
        return f"{indent}{pid:26s} {param.get('expression')!r}"
    return f"{indent}{pid:26s} {json.dumps(param.get('value'))[:60]}"


def main():
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        doc = api.Doc(DID, WID, HEAD)
        page.goto(doc.url, wait_until="domcontentloaded")
        page.wait_for_timeout(9000)
        print("signed in as:", api.require_signed_in(page))
        print("head tab:", doc.url)

        # --- the cavity sphere ------------------------------------------------
        st, bd = get(page, f"/api/partstudios/d/{DID}/w/{WID}/e/{HEAD}/bodydetails")
        print("\nbodydetails:", st)
        if st == 200:
            with open(f"{OUT}/p4.head.bodydetails.json", "w") as f:
                json.dump(bd, f, indent=1)
            for body in bd.get("bodies", []):
                sph = [f for f in body.get("faces", [])
                       if (f.get("surface") or {}).get("type") == "sphere"]
                print(f"  body {body.get('id')}  {len(body.get('faces', []))} faces,"
                      f" {len(sph)} spherical")
                for f in sph:
                    s = f["surface"]
                    o = [round(v * 1000, 4) for v in s.get("origin", [])]
                    print(f"    sphere  center {o} mm   radius"
                          f" {round(s.get('radius', 0) * 1000, 4)} mm"
                          f"   area {round(f.get('area', 0) * 1e6, 4)} mm2")

        # --- the two connectors' own parameters -------------------------------
        st, feats = get(page, f"/api/partstudios/d/{DID}/w/{WID}/e/{HEAD}/features")
        print("\nfeatures:", st)
        if st == 200:
            with open(f"{OUT}/p4.head.features.json", "w") as f:
                json.dump(feats, f, indent=1)
            rows = feats.get("features", [])
            print(f"  {len(rows)} features")
            for i, ft in enumerate(rows):
                ftype = ft.get("featureType") or ft.get("btType", "?")
                print(f"   {i:3d}  {ftype:28s} {ft.get('name')}")
            for ft in rows:
                if ft.get("featureType") != "mateConnector":
                    continue
                print(f"\n  --- {ft.get('name')}")
                for p in ft.get("parameters", []):
                    print(show(p))

        # --- where they actually sit ------------------------------------------
        print("\nmate connectors, read off the model:")
        try:
            print(api.eval_fs(page, doc, CONNECTORS) or "  (none)")
        except Exception as e:                                    # noqa: BLE001
            print("  featurescript refused:", str(e)[:200])


if __name__ == "__main__":
    main()
