# draft9p0 — where the run stopped

Written 2026-08-23 mid-run and brought current 2026-08-24, on branch `draft9p0`. Nothing is
pushed; the user chose to hold everything local.

Three files, in the order to read them:

- **[`register.md`](register.md)** — what was built, what it measures, what changed under the
  plan, and the requirements table. Start here.
- **[`b1/unmet.md`](b1/unmet.md)** — the three things that could not be done and what each one
  blocks.
- **[`b1/notes.md`](b1/notes.md)** — the long-form log, one section per tutorial. The last section
  ends with a **Where to pick up**.

## The document

`stickbot-draft9p0`, in the user's own Onshape account. Units are millimeter / 0.12345 / degree.

```
did  0f4b79a78707651ae20df5b2
wid  d7b87030a78288b62a42de72

body            Part Studio      02e4961f71e6767fb7d7d639
head            Part Studio      661eb771f054d4d12b351fbf
ball and socket Part Studio      f16153ba9741661febc6ba0a
foot            Part Studio      19accde64ded8a3a4e3cf429
hinge           Part Studio      d7401eebccc0e7c8681f5bac
u limb          Part Studio      a820d29c079b23a14a2b2385
l limb          Part Studio      454ab6f22f9df4f86778b537
gripper         Part Studio      614e820e82591f54aad4a4eb
robot sizes     Variable Studio  97046dd200d2da1151f9008b
stickbot        Assembly         546a5e79d793ec8ac2bc902e

version "t7 head mated"  acc35f11ec85129825dfdbee
version "t8 foot"        3d7b30559398005be8c9909f
version "t9 hinge"       dcb3dcc42e49e130ce163031
version "t10 u limb"     7d293115a90ebec16359ccf7
version "t11 l limb"     b5617bfbc551a3949f4cf02a   ← latest
```

The same ids are in [`b1/state.json`](b1/state.json), which every script in `b1/scripts/` reads.

**`stickbot` and `stickbot-for-bot-review` stay read-only.** Build only in `stickbot-draft9p0`.

## How far the run got

| Tutorial | Model | Frames | Page | Version |
| -------- | ----- | ------ | ---- | ------- |
| 1 torso | done | none | `torso.rst`, no figures | |
| 2 head | done | none | `head.rst`, no figures | |
| 3 assembly, two parts | done | none | `assembly.rst`, no figures | |
| 4 ball and socket | done | none | `ball-and-socket.rst`, no figures | |
| 5 head socket | done | none | `head-socket.rst`, no figures | |
| 6 torso joints | done | 10 | `torso-joints.rst` | |
| 7 assembly head | done | 4 | `mate-head.rst` | `t7 head mated` |
| 8 foot | done, measured | 15 | `foot.rst` | `t8 foot` |
| 9 hinge | done, measured | 17 | `hinge.rst` | `t9 hinge` |
| 10 upper limb | done, measured | 10 | `upper-limb.rst` | `t10 u limb` |
| 11 lower limb | done, measured | 12 | `lower-limb.rst` | `t11 l limb` |
| 12 gripper | eight variables and `copy socket` only | none | owed | |
| 13–14 | not started | | owed | |

The guide is [`instructions/stickbot-draft9p0/`](../../../../instructions/stickbot-draft9p0/), and
it builds with `ninja draft9p0`. Its three front pages — plan, before you start, habits — are
written; so are the eleven part pages above.

## The immediate next move

**Sign in to Onshape in the ordinary browser.** `agent_browser.py` borrows its cookies from there,
and it answers *"the borrowed cookies carry no session"* until somebody does. Then:

```
pkill -f agent_browser.py && uv run python tools/agent_browser.py
```

Reopen the `gripper` tab, delete the empty `Sketch 1` the timeout left behind, and start
`clip profile` again. After tutorial 12, the order is B2 — read the whole model back against
`make_plans.py` — then B3, then tutorials 13 and 14.

## The open decisions

**`#limbSeg` means two different things.** The model extrudes it as stock and stands each joint off
the end face; `make_plans.py` measures a segment joint center to joint center. A 48 segment needs
negative stock on both limbs. Full account under *Defects found* in [`register.md`](register.md).
It is one variable's meaning and it is the user's call.

**Which hinge tutorial 9 built.** Stub on the blade, hole through the fork, ear 6.4 mm, no slit —
settled at the CAD, which [`09-hinge.md`](../../../build/plan/09-hinge.md) says not to do. The slit
half was decided by the user on 2026-08-23 on the evidence that `stickbot-for-bot-review`'s joints
print and work without one, and `make_plans.py` and the sheets now match. **The stub-and-hole half
is still owed back** to `make_plans.py`, which draws it the other way round.

## Working notes that outlive this run

`b1/notes.md` carries the GUI lessons as they were paid for. The four that cost the most:

- **A mate connector with no owner part never reaches the assembly**, and the Part Studio gives no
  sign of it.
- **A concave sphere does not offer its center.** Every sphere center picked in this document was
  picked on the outside of a ball; the socket's cavity gives you the surface point instead.
- **`gui.row` matches the toolbar as readily as a tree row**, and `common.jrow` — which restricts
  to `rect.x < 250` — still returns a position for a row scrolled out of the feature list's own
  inner scroll box. Scroll first with `common.scroll_tree` (**negative n scrolls down**), then
  double-click.
- **Read the labels, screenshot the dialog, then click the checkbox.** `gui.labels` returns
  positions that are stale by a row right after a pick, and says nothing about tick state. That is
  how `blade blank` got a 3° draft instead of a symmetric extrude.

## The rules this run works under

Port **9223** only — 9222 is the user's own signed-in browser and is never driven. GUI for
geometry, REST read-only for verification. Every Bash call under 90 s with an explicit timeout.
Never `git add -A`; never stage `.ninja_log`; feature branches only; push only when asked.
