"""Diff two construction reads: order, and what each feature was built on.

    uv run --project . python tools/diff_construction.py <mine.json> <reference.json>

Prints one line per feature that differs, and the anchoring tally: how many sketches in
each document are placed on the model's own geometry rather than on a default plane and
some variables.
"""
import json
import sys

DEFAULTS = {"Origin", "Top", "Front", "Right", "Default geometry"}


def anchored(up):
    """Does this feature stand on geometry the model made, rather than on a default?"""
    return any(u not in DEFAULTS and not u.startswith("#") for u in up)


def main(mine_path, ref_path):
    mine = json.load(open(mine_path))
    ref = json.load(open(ref_path))
    a, b = mine["features"], ref["features"]

    for side, rec, path in (("mine", mine, mine_path), ("reference", ref, ref_path)):
        gaps = [n for n in rec["order"]
                if n not in DEFAULTS and n not in rec["features"]]
        if gaps:
            print(f"!! {side} lists {len(gaps)} feature(s) it never read a panel for: {gaps}")
            print(f"!! Every one is reported below as a feature {side} does not have."
                  f" Fill them in first: {path}")

    only_mine = [n for n in a if n not in b]
    only_ref = [n for n in b if n not in a]
    print(f"features: mine {len(a)}, reference {len(b)}")
    print(f"  only in mine     : {only_mine}")
    print(f"  only in reference: {only_ref}")
    order_a = [n for n in mine["order"] if n in b]
    order_b = [n for n in ref["order"] if n in a]
    print(f"  same order       : {order_a == order_b}")

    print("\nbuilt on -- differences only")
    same = 0
    for n in ref["order"]:
        if n not in a or n not in b:
            continue
        ua, ub = a[n]["upstream"], b[n]["upstream"]
        if ua == ub:
            same += 1
            continue
        print(f"  {n}")
        print(f"      mine     : {ua}")
        print(f"      reference: {ub}")
    print(f"\n{same} features built on the same things")

    print("\nanchoring -- a feature standing on the model's own geometry")
    for tag, d in (("mine", a), ("reference", b)):
        on_model = sorted(n for n, v in d.items() if anchored(v["upstream"]))
        floating = sorted(n for n, v in d.items()
                          if v["upstream"] and not anchored(v["upstream"]))
        print(f"  {tag:9s} on the model: {len(on_model)}   on defaults and variables only: "
              f"{len(floating)}")
        print(f"            floating: {floating}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
