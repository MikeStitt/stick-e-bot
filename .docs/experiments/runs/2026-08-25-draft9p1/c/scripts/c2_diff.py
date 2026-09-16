"""What moved between the C1 read and a driven read."""
import json, sys
SCRATCH = ("/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/"
           "c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/")
RAW = json.loads(open("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/"
                      "runs/2026-08-25-draft9p1/c/c1-raw.json").read())
base = {}
for name, studio in RAW["studios"].items():
    pn = {p["partId"]: p["name"] for p in studio["parts"]}
    for pid, bb in studio["partboxes"].items():
        base[f"{name}/{pn.get(pid, pid)}"] = {
            k: round(v * 1000, 4) for k, v in bb.items() if isinstance(v, (int, float))}
now = json.loads(open(SCRATCH + f"c2-{sys.argv[1]}.json").read())["parts"]
keys = sorted(set(base) | set(now))
same = 0
for k in keys:
    a, b = base.get(k), now.get(k)
    if a is None or b is None:
        print(f"  {k:34s} MISSING on one side")
        continue
    d = {j: (a[j], b[j]) for j in a if abs(a[j] - b.get(j, a[j])) > 1e-6}
    if not d:
        same += 1
        continue
    print(f"  {k:34s} " + "  ".join(f"{j} {v[0]} -> {v[1]}" for j, v in sorted(d.items())))
print(f"unchanged parts: {same} of {len(keys)}")
