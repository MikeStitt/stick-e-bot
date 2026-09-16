# 11. The lower limb

Starts from an upper limb. Ends with a limb carrying a ball stud at one end and a blade at the
other — the other half of both joints.

**The same eleven moves as [`10-u-limb.md`](10-u-limb.md), with the mating halves swapped.** The
upper limb takes the socket and the fork; this one takes the ball stud and the blade. That is the
whole difference.

## The steps

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.l_limb.blade.derive` | bring the blade in first, where it belongs | `add blade` |
| `cad.parts.l_limb.section_sketch` | the limb's circle | `limb section` |
| `cad.parts.l_limb.body` | extrude it `#limbCenter - #stand - #tab_free` long | `limb` |
| `cad.parts.l_limb.stud_connector` | where the ball stud goes, on the limb | `mate for ball stud` |
| `cad.parts.l_limb.stud.derive` | bring the ball stud in | `add ball stud` |
| `cad.parts.l_limb.stud.place` | onto its connector | `move ball stud` |
| `cad.parts.l_limb.combine` | union all three | `combine parts` |
| `cad.parts.l_limb.elbow_connector` | the end that mates to the elbow | `elbow end` |
| `cad.parts.l_limb.wrist_connector` | the end that mates to the wrist | `wrist end` |

**The blade is derived into place and only the ball stud is moved**, the same shape of chain as
[`10-u-limb.md`](10-u-limb.md), which says why. One difference is worth knowing before the take:
this tab's `limb section` is sketched on `Origin` and `Top` where the upper limb's is sketched on
the derived socket, so the two tabs are not built quite alike.
[`../../experiments/runs/2026-08-29-draft9p3/reference/l-limb.json`](../../experiments/runs/2026-08-29-draft9p3/reference/l-limb.json)
is the order this table now follows.

**Same two renames.** `Mate connector 1` and `Mate connector 2` become `elbow end` and
`wrist end`.

## What changes from stickbot, and what it costs

**draft9p0 sat its joints on the end faces, and the sheet buries them.** Its extrude was 48 long,
the blade then stood 44 off one end face and the ball stud 10 off the other, and the segment
measured **102** between centers where the sheet said 48.

**Stickbot has the same disagreement, about a twelfth the size.** Measured read-only on 2026-08-24,
its `l limb` is 37.91 long with **29.11** between centers, against a 1× sheet that said 24 — an
overshoot of 5.11. draft9p0 overshoots by 54.

**It is the upper limb's disagreement, and the same decision settles it**; see
[`10-u-limb.md`](10-u-limb.md). Here the stock is `#limbCenter - #stand - #tab_free`, **18 mm**:
the ball stud stands `#stand` 10 mm clear of one end face, and the blade's tongue is rooted
`#tab_free` 20 mm past the other. The rod stopping at the tongue's root rather than running on to
the pin is the thing every earlier build got wrong; a rod that reaches the pin fills the fork's
slot back in.

**It also decides the robot's height.** Stacked, at 100.4 and 102, the sole lands at −284.4 and the
robot stands about **422** tall, where the guide's plan page says around 320. Buried, at 48 and 48,
it stands **315.4**.

## The shots this tutorial needs by name

**Requirements in play.** `req.model.derive` — the joint is brought in from the studio that
owns it, never resketched here.

Fewer than the upper limb, deliberately, because the moves are the same ones.

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the hero | the limb, both joints on | `req.page.hero` |
| the two limbs side by side | the frame that shows what makes a chain: fork meets blade, socket meets stud | |
| each transform's two connectors, close-up with a ring | the medium view can be dropped if the upper limb's carried it | `req.shot.two_frame` |
| the tree, the version dialog | | |

**The side-by-side is the frame this tutorial exists to produce.** Two limbs whose ends match is
the picture that explains why the robot is built out of two limb parts and not one.

## What we do not know yet

**Whether this is a page or a section.** If the upper limb's page carries the moves, this could be
a short page that shows the swap and the side-by-side and points back. That decision is best made
after the upper limb's page is written and its length is known, not now.

**Whether `#limbCenter` should differ between the two limbs.** Stickbot has 35.42 and 37.91, which
looks like drift rather than intent. One variable for both is the plan — **48 mm** at draft9p0 —
and if the robot needs a longer forearm, that is a second variable and a reason for it.
