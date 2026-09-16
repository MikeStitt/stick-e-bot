import sys
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S
DID = "a1a859f4bfdfe42d372aff90"
with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    r = S.api(page, "GET", f"/api/documents/d/{DID}/versions")
    for v in r["body"]:
        print(f"  {v['name']:20s} {v['id']}  {v.get('createdAt')}")
        d = (v.get('description') or '').strip()
        if d:
            print(f"      {d[:150]}")
