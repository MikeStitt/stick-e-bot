# draft9p2 — the register

**This draft is superseded by draft9p3 and stops at tutorial six.** It built the first six tutorials
from an empty document, captured 442 frames, wrote six pages and audited every step, part, block and
page it produced. It is closed early because the thing its audits measured was the shape, and the
shape was never what was wrong.

## Where the work is

| | |
| --- | --- |
| document | `stickbot-draft9p2`, `ff43b9ee37b87e04445bb573` |
| workspace | `Main`, `2625a774fd32dc519c24dce4` |
| live | [the workspace](https://cad.onshape.com/documents/ff43b9ee37b87e04445bb573/w/2625a774fd32dc519c24dce4) |
| guide | `instructions/stickbot-draft9p2/` |
| log | `log/*.jsonl`, one file per page |
| branch | `audited-draft9p2-plan`, never pushed |

Element ids: `stickbot` assembly `07f503bad249441d4bb50461`, `body` `58e1fb096c6bb30ae8b5b407`,
`ball and socket` `01adb5e9a6777b267092ffd1`, `head` `cc90b445312b47afa59be534`, `robot sizes`
`aff03e845eec7317f0897333`.

Versions, in the order they were published:

| Version | Id |
| ------- | -- |
| Start | `61d383999b5e0486ff04b2f9` |
| tutorial 1 - variables and torso | `eff91b1604bb06e7caeb2c21` |
| tutorial 2 - the head | `af4c551fe20bb18a6ce85d07` |
| tutorial 3 - the assembly | `2de8ffa3b95c5beb61a015a6` |
| tutorial 4 - the ball and socket | `ca77895be80646c0d88f2f88` |
| tutorial 5 - the head gains its socket | `14d5ee90fdec48f3a7677eab` |
| tutorial 6 - the torso gains shoulders and studs | `bb63723e6350821be57b9bd5` |

Tutorial 7 was probed and not taken. The assembly stands where tutorial 3 left it: two instances,
nothing fixed, no mates.

## What was built and written

| Page | Steps | Frames | `audit.step` | `audit.part` | `audit.block` | `audit.page` |
| ---- | ----- | ------ | ------------ | ------------ | ------------- | ------------ |
| `torso` | 10 | 40 | 11 | 1 | 9 | 1 |
| `head` | 14 | 81 | 14 | 1 | 14 | 1 |
| `assembly` | 6 | 17 | 5 | 1 | 5 | 1 |
| `ball-and-socket` | 18 | 83 | 18 | 1 | 36 | 2 |
| `head-socket` | 10 | 41 | 10 | 1 | 9 | 1 |
| `torso-joints` | 29 | 158 | 32 | 1 | 29 | 1 |

A step re-audited after a retake gets a second record, which is why two pages carry more
`audit.step` records than steps, and why `assembly` carries one fewer. The audits recorded 254
findings, of which fourteen were blocking. **Every blocking finding was
about a frame or the sentence describing it** — a crop that cut off the row its alt text named, a
dialog that opened on Add previewing four solids the alt never mentioned, a mirror the log said was
pushed back to New when it opened there and stayed. Not one blocking finding was ever against the
geometry.

## Why it is superseded

**The model reaches `stickbot-draft9p1p1`'s shape by a construction 9p1p1 does not use.** The
`pivot lines` block of `torso-joints.rst` says it in its own words:

> Dimension it from the sketch's vertical axis with `#shoulder_half`. That is the torso's own half
> width, so the line stands exactly on the side face. Dimension the line's top end from the
> horizontal axis with `#torsoH / 2`, which is the top of the torso.

The side face and the top face are in the model already. That block re-derives both by arithmetic
and lands on them by agreement rather than by reference, against
[`../../../../.parts/onshape.md`](../../../../.parts/onshape.md) § *Anchor each sketch to the
geometry that gives it meaning*. A page is written from the construction, so a page written from
that build teaches it.

**No measurement this draft ran could have caught it.** `audit.part` compared every face over
`bodydetails`, the volume, the surface area, the bounding box and a driven variable table against
9p1p1, and matched on all of them, because two constructions of the same solid measure the same.
`sketches?includeGeometry=true`, read afterwards, returns the body tab's six sketches with the same
names, the same entity counts, the same planes and coordinates identical to four decimal places.
The difference lives in the constraints and in each feature's parameters, and nothing this draft ran
read either.

**The plan asked for the check and the audit substituted a weaker one.** `plan.md` § *`audit.part`*
says *"Match the sketches and features to `stickbot-draft9p1p1`'s, one for one."* The audit compared
the GUI tree's names and order, recorded that `/api/partstudios/.../features` was rate limited, and
argued that a row which matched by name must be the same feature. That argument covers the shape and
not the construction.

## Gates

| Gate | Claimed | Evidence |
| ---- | ------- | -------- |
| Names are real | yes, for six pages | every tool, menu and field name in the six pages was read off a frame taken at the CAD |
| Model inspected | yes | every tab turned and sectioned; `audit.part` measured each against 9p1p1 |
| Recovery point | yes | six named versions, one per tutorial |
| Prose style | yes | `ninja check` clean for wrap and spelling; `page_sweeps.py` clean on all six pages |
| Spelling | yes | `ninja check-spell` clean |
| Steps reproduce | **no** | `stickbot-draft9p2-check` was never created, so no page was ever followed to a part by a reader without the build in front of them. `req.audit.reproduced` is unmet on all six pages |
| Reading level | tracked | 143 paragraphs above grade 8, unadjudicated |
| Links resolve | out of scope | declared out of scope before the run |
| Floor & ceiling | out of scope | declared out of scope before the run |

## What is carried into draft9p3

**Kept.** The six pages' words, their order and the four conventions draft9p2 established —
`req.page.instruction_first`, `req.page.step_tag`, `req.shot.toolbar` and `req.page.video`.
`tools/page_sweeps.py`, which was written here after mechanical sweeps found a byte-identical figure
pair, twenty-two pictures with no instruction above them and eleven unrecorded keystrokes on a page
two close readings had already passed. The `req.audit` family and the audit log record. The
twenty-two toolbar close-ups.

**Thrown away.** Every frame of the model, and every construction paragraph inside the six pages.

**Carried as open.** The reading-level backlog. `req.page.video`, unmet guide-wide because no clip
was ever recorded. The retakes owed at the point this run stopped: `tb-create-version.png`'s crop,
`socket.connector-02`'s ring, and tutorial 5's duplicate `cad.part_list` frame.

## What draft9p2 proved that is worth keeping

**A page of 157 figures is not readable, and mechanical sweeps find what two close readings miss.**
That is why `page_sweeps.py` exists and why draft9p3 runs it before every `audit.page`.

**The log is not an answer key.** Two `shows` records written at the CAD with the frame on screen
were wrong where the page was right, so `altdiff` prints differences rather than passing or failing.

**An audit that can only measure will only ever check what it can measure.** This is the finding
that ends the draft, and `req.model.same_structure` in [`../../../build/drafts.md`](../../../build/drafts.md)
is what it turned into.
