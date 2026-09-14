"""The variable table as Onshape holds it."""
import sys, json
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S
DID = "a1a859f4bfdfe42d372aff90"; WID = "d3a590c94880f445e3c56902"
VS = "8e21e5ac45ee843a1c536e1b"
with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    r = S.api(page, "GET", f"/api/variables/d/{DID}/w/{WID}/e/{VS}/variables")
    print("status", r["status"], r["ok"])
    open("/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/"
         "c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/c2-vars.json", "w").write(
        json.dumps(r["body"], indent=1))
    for table in r["body"]:
        print("table:", table.get("name"))
        for v in table.get("variables", []):
            print(f"   {str(v.get('name')):16s} {str(v.get('type')):8s} "
                  f"{str(v.get('expression')):34s} {v.get('description', '')}")
