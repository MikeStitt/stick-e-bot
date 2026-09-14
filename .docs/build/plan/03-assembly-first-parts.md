# 3. The assembly, with two parts in it

Starts from a torso and a head in two Part Studios. Ends with an assembly named `stickbot`, on the
first tab, holding both.

**A student sees a robot here, three tutorials in.** Everything after this adds to something that
already looks like the thing being built.

## The steps

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.assembly.place_body_head` | insert the torso and the head from the workspace | `torso <1>`, `head <1>` |
| `cad.assembly.pose` | drag the head up 90 mm, so it floats clear above the torso | nothing |
| `cad.assembly.rename` | name the assembly `stickbot` | nothing |
| `cad.assembly.first_tab` | drag it to the first tab | nothing |

**Nothing is mated yet.** The head has no socket and the torso has no stud, so there is nothing to
mate to. Both parts float, and saying so out loud is better than a student wondering what they got
wrong.

**Insert drops both instances at the origin, which buries the head inside the torso.** No later
step depends on how far the head is dragged up; what matters is that the picture reads as a robot
before the page claims a student can see one. Dragging it is also the first time a student moves an
unmated instance, which is the thing tutorial 7 then takes away with a mate.
[`../drafts.md`](../drafts.md) § *The requirements* carries this as `req.model.posed`.

**The drag ends in a box, so the page names a number after all.** Letting go leaves a distance field
holding the free-hand figure, and typing over it moves the instance exactly that far. 90 mm is what
the page teaches, which leaves the head's underside 6 mm clear of the torso's top. A typed number is
easier to land than a released mouse button and it is what makes the acceptance row checkable.

**Insert from the workspace, and this is the page that teaches it.** The **Insert** dialog offers
the workspace and a version side by side, and the version reads like the safer pick. A workspace
reference names an element, so it follows the edit just made and a document copy re-points it; a
version reference names a document and a version, and a copy has no version of its own for that
reference to become, so the copy goes on showing the original's parts.
[`onshape`](../../../.claude/skills/onshape/SKILL.md) § *Insert from the workspace, and keep
every reference inside one document* is the rule. Tutorials 13 and 14 insert the same way and do
not re-teach it.

## The shots this tutorial needs by name

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the insert dialog, with the document's parts listed | this is the first time a student sees one tab reach into another | |
| both parts in the assembly, before the drag | the buried head is what the drag is for, and a page that skips it reads as if Insert placed them well | |
| both parts in the assembly, posed | the honest picture of an unmated assembly | |
| the tab, renamed | before and after | |
| the tab bar, before and after the drag | the drag itself has no dialog | |
| the distance box, with the typed number in it | the box is the whole reason the height is sayable | |

## Built

**Document `stickbot-draft9p4`**
([`fe052e60`](https://cad.onshape.com/documents/fe052e606c96bb7cc5aaf59f)), version
**tutorial 3 - the assembly** (`0dd51c03d74ff36806ada896`). Its `stickbot` assembly holds
`torso <1>` and `head <1>` and no mate feature, with the head 90 mm up the z axis and nothing off
in x or y. `stickbot` is the first tab on the strip.

**The end-of-tutorial-3 numbers are measured in `stickbot-draft9p4-check`**
([`86f40935`](https://cad.onshape.com/documents/86f40935a709a0748cdbb199)), at its own version
**tutorial 3 - the assembly**, because that document holds nothing past this page. Its tree reads
`stickbot`, `Origin`, `torso <1>`, `head <1>`, `Loads (0)`, `Mate features (0)`, and its strip reads
`stickbot`, `body`, `head`, `robot sizes`. The torso measures 72 × 48 × 96 mm and the head
72 × 63 × 72 mm, so a head 90 mm up stands 6 mm clear of a torso whose top face is at z 48.

**The Insert panel holds its work in a transaction, and only the tick commits it.** Every row click
raises the panel's own `Inserted:` counter and puts a row in the tree, but the assembly is unchanged
until the green tick: the red cross rolls all of it back, and so does reloading the page, which
reopens the panel with the same count still pending. A run that read the assembly over REST between
clicks saw an empty assembly each time and was reading the truth.

**A click at the middle of the head's face selects the origin.** The assembly's origin is drawn as a
point at dead center and sits in front of the face there. A point cannot be dragged, so the head
does not move however far the mouse goes. The pick has to land off to one side.

**Letting go of the drag leaves a distance field with the keyboard.** It arrives holding the
free-hand number, `90.1 mm` in this run, and typing `90` and pressing Enter set the occurrence to
exactly 90 mm. Pressing **f** while that field is up types the letter into it and opens an
expression list rather than zooming to fit.

## Captured

**`instructions/stickbot-draft9p4/source/assembly.rst`**, written from the 22 frames in
`instructions/stickbot-draft9p4/source/images/assembly/`. Sphinx builds the page with no warning;
every frame on disk is used and every frame the page names is on disk.

**The carried page named two frames that were not there and left one on disk unused.**
`assembly.rename-03.png` and `version-01.png` were referenced and missing, and
`assembly.first_tab-01.png` was on disk with nothing pointing at it. The whole page was recaptured
by following it into `stickbot-draft9p4-check`, so all 22 frames are this draft's.

**The pose step grew a fourth frame.** The drag's distance box is a step a reader has to take, and
it needs its own picture: a medium frame of where the drag starts, a held mid-drag frame, the box
with `90` typed into it, and the result.

**The frames are full windows, where draft9p3's Insert panel frame was cropped to the panel.** The
tree behind the panel is what the counter is checked against, so the crop hid half of what the
paragraph beside it claims.

## What we do not know yet

**Nothing this page needed is still open.** A mid-drag frame is capturable in both places it is
wanted: `assembly.pose-02` holds the head part way up with the mouse button down, and
`assembly.first_tab-02` holds the tab part way along the strip. Parts have to be inserted one row at
a time, and the panel stays open between them, so the two-frame answer is the only one available and
it is the one the page gives.
