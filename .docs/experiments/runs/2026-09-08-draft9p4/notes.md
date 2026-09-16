# draft9p4 — notes

## Where the work is

The reference is `stickbot-draft9p1p6`, `500752af84dc92deea53f9e4`, workspace
`f30bf96cfeece59f61e0e7b2`, read at version `80c22eb7b8b0342ac03f8a6d`, and it is read only. Its
construction is in [`reference/`](reference/README.md).

`stickbot-draft9p4` and `stickbot-draft9p4-check` were made on 2026-09-09; their ids are below,
under *Both documents exist*.

The probes below run in `stickbot-draft9p3-check`, `555033d6ce000bb44430dd6e`, workspace
`7786456e4391bf899e70d825`, Part Studio `74433d23ba8c3b718fe83b85`. It holds draft9p3's tutorial 1
and nothing else, and each probe puts it back where it found it.

## P0 reads five tabs at the version, not at the workspace

[`scripts/p0_read.py`](scripts/p0_read.py) wrote 13 files: every feature with every parameter, every
sketch entity with every constraint, and every face with its surface type, radius, axis and area.
101 features across the five tabs, 1062 faces, 15 sketches.

The workspace and the published version sit at different microversions, `1009393f43c6384ece39b921`
and `dd821b5b9c8498eb568aee67`. All five tabs' feature lists are identical across the two, so the
bump was not a change to the model, and reading the version gives a record a later edit cannot move.

**Twenty-four numbers in the whole reference are typed**, and everything else derives from one of
them. [`scripts/typed_numbers.py`](scripts/typed_numbers.py) finds them, and the count is only
believable because it reads each parameter through the switch that turns it on. A feature stores a
value for every parameter it could have: an extrude that is neither drafted nor offset still carries
`draftAngle 3 deg` and `offsetDistance 25 mm`, and a transform that moves a part onto a mate
connector still carries `distance 25 mm` and `angle 30 deg`. Counting those gives 248 typed numbers
instead of 24, which is a report that says nothing.

## A Variable feature cannot be renamed, so the naming rule is not a choice

draft9p4's plan says a Variable feature keeps Onshape's title, `###name = #value`, so its tree row
reads its own name and its value. That was read off stored titles. On Wed 9 Sep
[`scripts/variable_title.py`](scripts/variable_title.py) drove the box in
`stickbot-draft9p3-check`, adding one variable, framing it at each step, and deleting it. Frames are
in [`capture/variable-title/`](capture/variable-title/).

- **The title is computed, not stored.** It arrives reading `#? = 0`. Typing the name alone leaves
  it at `#? = 0 mm`; committing the value turns it into `#probe = 7 mm`. The dialog header and the
  tree row show the same string.
- **The dialog has no rename pencil.** `div.os-dialog-button-edit-name` is in the page and stays
  sized to nothing, whether the title is hovered, its 28 px hover area is hovered, the variable is
  empty, or the variable is complete. In the same session an `Extrude` dialog put its pencil at
  x 382, y 79 on the first hover, which is the slot the Variable dialog leaves empty.
- **The tree row has no Rename.** Its menu is *Edit…*, *Add selection to folder…*, *Suppress*,
  *Dynamic suppression*, *Add comment*, *Show dependencies…*, *Delete*. `torso block`'s menu carries
  *Rename* second and `torso outline`'s does too. `F2` on the selected row leaves the keyboard on
  the body.
- **A variable that already carries a typed name is no different.** `nose` in draft9p1p6's `hinge`
  is offered no Rename either.

So the thirteen typed titles in `hinge` and `ball and socket` cannot be put back by renaming. They
come back to the template by being built fresh, which is what every draft9p4 tutorial does anyway.
And the pages lose a sentence rather than gain one: a variable's step says nothing about naming,
because there is nothing the reader can do there.

**How the thirteen got typed is not answered.** They were renamed at draft9p1p4 and draft9p1p5 in
the GUI, so the route existed then and does not now. Nothing in this run turns on the reason.

## Three rows moved, and only the foot carries a feature that reads one

`robot sizes` went from eleven rows to twenty-three between `stickbot-draft9p1p1`, which is
draft9p3's reference for `head`, `body`, `foot`, `gripper` and the assembly, and
`stickbot-draft9p1p6`, which is this draft's reference for the joints. Twelve rows are new and
three moved:

| row | draft9p1p1 | draft9p1p6 |
| --- | ---------- | ---------- |
| `#wall` | `#torsoH / 32` | `#torsoH * 3 / 160` |
| `#collar` | `#ball / 2 + #wall` | `#stand` |
| `#grip` | `sqrt((#ball / 2 + #fit) ^ 2 - (0.48 * #ball) ^ 2)` | `sqrt((#ball / 2 + #fit) ^ 2 - (0.48 * #ball - #ballLoss) ^ 2)` |

Nothing was renamed and nothing was removed. `#torsoH`, `#torsoW`, `#torsoD`, `#limbCenter`,
`#ball`, `#limbD`, `#stand` and `#fit` all read exactly what they read before.

**Walking each moved row downstream through draft9p1p1's dependency graph answers the carry
question for three of the four tabs.** `head`'s thirty-one rows and `body`'s thirty-eight contain no
feature that depends on any of the three: the head's twelve locals are driven by `#headW` or typed,
and the body's eight are typed. So tutorials 2 and 3 carry, and so does everything in tutorial 6
ahead of `copy ball stud`. `torso shoulder profile` is retaken anyway, for the projected edge in
task #125, and that is a construction reason rather than a number.

**The foot does not carry, and the reason is that its two collar numbers are typed.**
`#collar_r = 9 mm` and `#collar_down = 9 mm` are locals with no upstream, and they feed
`pedestal outline` and `foot pedestal`, both of which sit five and four features ahead of
`add socket`. They are the settled `#ball / 2 + #wall` and `#collar` written out as constants at
draft9p1p1's values, so at the settled rows they are 7.8 mm and 10 mm, and `#pedestal`, which is
`#plate - #collar_down`, follows from 3 mm to 2 mm. Nothing turns red, because a typed number cannot
notice that the row it copied has moved, and `read_shape.py` reports the foot as exactly what
draft9p3 built.

So tutorial 8 is taken from `pedestal outline`, not from `add socket`, and
[`plan.md`](plan.md) § *What the joint change reaches, tutorial by tutorial* is corrected to say so.

**The gripper has the same defect and is retaken whole regardless.** It declares `#ball = 12 mm` and
`#wall = 3 mm` as locals, shadowing the studio's rows, and builds `#collarR = #ball / 2 + #wall` from
them. [`../../../build/plan/12-gripper.md`](../../../build/plan/12-gripper.md) already requires that
it read the studio's rows instead.

**The measurement half of this check waits for `stickbot-draft9p4`.** What is proved above is which
features can move; what `read_shape.py` proves is whether they did. It runs on `head` and `body`
against draft9p3's `log/head.faces.json` and `log/body.faces.json` once tutorial 1 has driven the
settled rows into the new document, and a face that moved takes `captured` off its step.

## Both documents exist, and the copy carries `u limb` one feature past the version

| | did | ws | wid |
| --- | --- | --- | --- |
| `stickbot-draft9p4` | `fe052e606c96bb7cc5aaf59f` | `Main` | `0ff70e8921be572d630dd9cc` |
| `stickbot-draft9p4-check` | `86f40935a709a0748cdbb199` | `Main` | `075a86f5b8f922210c0a7317` |

Every element id is in [`reference/documents.json`](reference/documents.json). The build document
carries draft9p3's nine elements under the same names; the check document starts on Onshape's
default `Part Studio 1`, `Assembly 1` and `BOM : Assembly 1`, and each tab is renamed as the
tutorial that builds it reaches it. `stickbot-draft9p3` is untouched.

**`from` names `tutorial 10 - the upper limb`, `f94cbf2e4657300be13507d2`**, published
2026-08-30 09:04:49. It is the last of eleven versions, and draft9p3 published one per tutorial
after `Start`. draft9p3's run stopped after nine pages, so tutorial 10 is a tab that was built and
versioned and never written up; task #139 still holds that.

**The copy route copies a workspace, and this workspace is not that version.** The two microversions
are `0b0b73acb53b4a668128e150` and `1b003b9d14d8a624a722e2e1`, so the shortcut draft9p1p4 used does
not carry. [`scripts/p_ws_vs_version.py`](scripts/p_ws_vs_version.py) read the Variable Studio's
rows and every tab's feature names, types and statuses from both. Six of the seven tabs are
identical, feature for feature. `u limb` differs in one row, its tenth and last: the workspace has a
sketch, `elbow station`, where the version has a mate connector, `elbow end`. Work continued in the
workspace after the version was published and replaced the last feature.

The copy took the workspace, so `stickbot-draft9p4` starts with the sketch. Nothing turns on it:
tutorial 10 rebuilds `u limb` whole, so every feature in that tab is replaced before it is captured.

**Nothing reaches back into `stickbot-draft9p3`**, which is the defect a workspace copy creates.
[`scripts/p_no_refs.py`](scripts/p_no_refs.py) read it twice.
`GET /documents/d/{did}/w/{wid}/externalreferences` answers with no external reference and no
revision reference, names one document and that document is `stickbot-draft9p4` itself, and names no
version. Separately, all 152 features of the six Part Studios were fetched and their JSON searched
for draft9p3's document id and workspace id. No hit.

**The copy arrived with its own `Start`**, `d062792d2910ff01121c830d`, stamped at the moment of the
copy. It carries none of draft9p3's eleven versions, so the *Recovery point* gate has a named
version to start from and draft9p4's version list begins at one.

## The guide inherits 199 of draft9p3's 796 frames, and 15 of the ones it drops were never on a page

`instructions/stickbot-draft9p4/source/` is a copy of draft9p3's. Only `source/` is copied; `build/`
is generated and gitignored, and `.gitignore` and `build.ninja` gained `draft9p4`, `open-draft9p4`
and `clean-draft9p4` alongside draft9p3's three.

**597 frames were cleared, by what the step shows rather than by what tutorial it is in.** A frame
is kept only when the picture in it is unchanged.

| tutorial | had | kept | what went | why |
| -------- | --- | ---- | --------- | --- |
| 1 torso | 32 | 23 | `variables.sizes`, `version`, 4 orphans | the row list grows from eleven to twenty-three |
| 2 head | 62 | 58 | `version`, 2 orphans | the head's own shape does not move |
| 3 assembly | 21 | 17 | `version`, 2 orphans | two parts, both unchanged |
| 4 ball and socket | 81 | 0 | all of it | the tab is rebuilt whole |
| 5 head socket | 42 | 0 | all of it | the collar changes, so every frame of the head with one does |
| 6 torso joints | 152 | 79 | `torso shoulder profile`, then `copy ball stud` on | the shoulders and both connector sketches carry |
| 7 mate head | 19 | 0 | all of it | the head it mates has changed |
| 8 foot | 97 | 0 | all of it | `pedestal outline` is the tab's first feature, so nothing downstream survives |
| 9 hinge | 200 | 0 | all of it | the wedge ring |
| 10 u limb | 68 | 0 | all of it | the tab is rebuilt whole |
| toolbar | 22 | 22 | nothing | a close-up of a button is a picture of Onshape |

**A version dialog is cleared in every tutorial, including the two that carry.** It shows draft9p3's
version list under `Main`, which is a picture of a document that is not the one the reader is
building.

**Hashing every inherited frame found 778 distinct images under 796 names, and every repeat is an
orphan.** Fifteen images carry two or three names each, covering 33 names; `cad.hero`, `cad.tree`
and `cad.version` shot the same window in torso, head and assembly, and `parts.head.body-06`,
`parts.body.block-05`, `document.units-01` and `document.units-03` each got shot twice. Sphinx names
every missing image, and not one of the fifteen repeats appears: no page ever referenced them. They
were written by the take and never placed, so tutorials 2 and 3 do keep every frame they show, and
the plan's rule that a take refuses a second name for the same bytes has nothing to undo here. The
same fifteen files still sit in `instructions/stickbot-draft9p3/`.

**Sphinx warns 642 times and 60 of those are draft9p3's.** `arms`, `gripper`, `l-limb`, `legs` and
`plan` reference frames that were never taken, because draft9p3 stopped after nine tutorials. The
count on draft9p3 is 60 and it has not moved. The other 582 are frames cleared here, and 597 cleared
less the 15 orphans is 582.

**Six pages named `stickbot-draft9p3` in their prose and now name `stickbot-draft9p4`**, and
`conf.py` read `release = "draft9p2"`, which draft9p3 carried without noticing. It reads `draft9p4`.

**Task #169 is swept, and it is five files rather than nine pages.** The wrong instruction is *click
the name at the top of the dialog*; the box opens from a pencil that appears beside the title on
hover, and letters typed at the title itself reach the sketch as tool shortcuts. `torso.rst` teaches
it twice, `head.rst` twice, `head-socket.rst` and `foot.rst` once each, and `habits.rst` states the
rule for the whole guide; that last one told the reader to rename the row in the tree afterwards,
which works but is not the habit the rest of the guide teaches. Every other page says *rename the
feature* without saying how, and the `:alt:` texts describe a name sitting in a box, which stays
true. `lower-limb.rst` clicks the dialog title to move focus out of a variable box, which is not a
rename and is left alone.

## The free plan claim holds, and the page was short one condition

`before-you-start.rst` carries the guide's only Onshape link, `www.onshape.com`, and beside it the
claim *the free plan does everything in this guide*. The claim was read against Onshape's own
published pages on 2026-09-09.

**Onshape's subscription FAQ settles it.** [`Subscriptions and Payment
FAQs`](https://cad.onshape.com/help/Content/plansfaqs.htm) says a Free subscription has *all of the
same CAD and data management functionality as the Professional subscription*, and names one
restriction: *unable to create any private documents*, so *all of your documents will be public to
all Onshape users*, who can view and copy but not edit. The
[pricing page](https://www.onshape.com/en/pricing) uses the same words, *unlimited public storage*
and *for non-commercial use only*. Version control is data management, so the version each tutorial
publishes is a free-plan operation, and so are the Variable Studio, the assembly and every derive.

**One marketing page disagrees with the FAQ and is wrong.** Onshape's upgrade page says Standard
adds *access to versions and history, branching and merging* over Free. The help FAQ and the
Standard subscription help page contradict it: the Standard page lists what Standard *excludes* and
the list is release management, custom properties, company material libraries, company sharing and
consolidated billing. Nothing about versions.

**The page named one condition and there are two.** It said *the one condition that your documents
are public*. Free is also non-commercial only. The sentence now names both, and says what public
means for a student: anyone can open it and copy it, and nobody but you can change yours.

**The export restriction does not reach this guide.** Free cannot use Onshape's *Email with file
download link* export. No page in the guide asks the reader to export anything; the printer is
named on `before-you-start.rst` as something needed *eventually*, and the ordinary right-click
export is on every plan.

**What is still untested is the sign-up itself.** Nobody in this run created a free account, so the
claim rests on Onshape's published wording rather than on a student's screen. That is the whole of
what *Links resolve* leaves open, and it is one sentence on one page.

## Phase P closes on a reread, and it finds two decisions filed under *settled*

draft9p3's `notes.md`, all 2094 lines of it, and draft9p1p6's register were read through on
2026-09-09. Most of what they hold is already carried: the GUI findings are in
[`onshape-gui-howto.md`](../../../onshape-gui-howto.md), the audit findings have tasks, and the
three construction differences draft9p3 closed with are tasks #119, #125 and #139. Four things came
out that this draft owed and did not have.

**Two open decisions were sitting under [`plan.md`](plan.md) § *What is settled before the take
starts***, whose own heading says none of them is a question for whoever is at the CAD. Both are.
They have moved to *What we do not know yet*.

- **`head mate` sits 0.8 mm off the sphere's center.** The socket's ball is concave and is picked
  down its own axis, so the rim rings the pointer at every zoom and comes along in
  `secondaryOriginQuery`. draft9p3 built the connector eleven times, tried nine pixels and three
  zooms, and got the rim every time; the connectors on the five convex balls in `body` take one
  entity and land clean. It is the robot's first joint. Carrying it costs the page a sentence
  saying the head hangs 0.8 mm off the plane of symmetry; curing it means building the connector
  somewhere with no rim near it, which is `socket mount point` slid down its own Z with the `Move`
  tick, and rewriting tutorial 5's step. Tutorial 5 is where it is spent.
- **The five joint connectors are spelled three ways.** `left shoulder connector` beside
  `r shoulder connector`, `l hip connector` and `r hip connector`. draft9p1p1 spells them that way,
  draft9p3 reproduced it rather than deciding, and this draft builds all five fresh in tutorial 6.
  Mike settled it on 2026-09-11: the name is the joint, `left shoulder` and `left hip`, with the
  word *connector* left off. The five, the hinge's two and the three that mark where a stud goes
  are listed in [`plan.md`](plan.md) § *What we do not know yet*.

**draft9p1p6's `hinge` naming question is closed by construction.** Its register leaves open that
ten of the tab's variables carry the GUI's `###name = #value` template and six carry a bare name.
Task #184 found that a Variable feature has no rename at all: no pencil, no menu entry, no `F2`. So
every variable this draft builds arrives with the template, the tab stops mixing conventions, and
nothing has to be renamed to get there.

**Two of draft9p1p6's open items are measured here rather than inherited.** Its
`req.model.anchored` is met but for the lower limb's rod, which offsets from a plane where a face
was available, and its `l limb`'s rod may reproduce volume the derived blade's arm already occupies,
unchecked for `u limb`. Both limbs are rebuilt whole in tutorials 10 and 11, so both are this
draft's to fix rather than to carry.

## The socket's own axis is what puts `head mate` 0.8 mm off center

The 0.8 mm was blamed on the wrong thing. `head mate` does hold the cavity sphere: `originQuery`
is `Jr6`, which `bodydetails` gives as a sphere centered on (0, 0, -45) mm with a radius of
6.08 mm. What drags the connector off that center is the second entity, `KrVB` in
`secondaryOriginQuery`, a circle of radius 6.0271 mm centered on (0, -0.8, -45) mm. Onshape places
the connector where the two together resolve, and the circle wins.

That circle is not the socket's mouth. The socket carries a cross slit 1.6 mm wide, and the four
planar faces it cuts sit at x = ±0.8 mm and y = ±0.8 mm. Where each one meets the cavity sphere it
leaves a circle, so the sphere carries eight of them, four of which are 6.0271 mm across:

| edge | center | what it is |
| --- | --- | --- |
| `Jr1`, `KrNB` | (0, 0.8, -45) mm | the slit's far wall, seen from inside the ball |
| `Jr9`, `KrVB` | (0, -0.8, -45) mm | the slit's near wall |
| `KrBB`, `KrhB` | (-0.8, 0, -45) mm | the cross slit's other pair |
| `KrJB`, `KrZB` | (0.8, 0, -45) mm | the same, on the far side |

All four traces run within 0.8 mm of the socket's axis. So a camera on that axis draws them
crossing in the middle of the cavity, and the middle of the cavity is the pixel the page tells the
reader to click. Nine pixels across the opening, three zoom levels and eleven rebuilds could not
get away from them, because on that view there is nowhere to get away to.

### Turning the view is what cures it

Four runs, each building one throwaway connector, reading it back through `/features` and
`evMateConnector`, and deleting it. `shift+7` then eight presses of the up arrow puts the camera
under the head; three presses of the left arrow turns the heading 45°.

| view | Shift | what the pick caught | where it landed |
| --- | --- | --- | --- |
| square on the axis | no | `socket connect to robot` | (0, 0, -36) mm |
| square on the axis | yes | `socket connect to robot` | (0, 0, -36) mm |
| turned 45° | yes | `Jr6` alone, inference `CENTER` | (0, 0, -45) mm |
| turned 45° | no | `Jr6` alone, inference `CENTER` | (0, 0, -45) mm |

Shift in those four runs was pressed before the hover rather than after it, so it locked nothing;
what the column records is a keystroke held down, not the technique. The runs that do hold it the
right way are below.

On the turned view the pick pixel meets the shell at (3.32, 2.76, -49.28) mm, which is 2.76 mm
clear of the nearest slit trace, out in a quadrant of the ball where the only thing under the
pointer is the sphere. Both runs there passed, and `secondaryOriginQuery` came back empty both
times.

### Shift is a lock, and the first four runs held it wrong

Shift does not filter what is under the pointer. It pins the reference to the face or edge already
hovered, so that face's inferred points stay alive while the cursor travels, even off the face.
The order is the whole technique: **hover the face, then press and hold Shift, then move to the
point, then click.** The first four runs pressed Shift before the hover, which locks nothing, so
they tested a different thing and the write-up first published here was wrong about the mechanism.

Two more runs, square on the axis, hovering the shell at (2.50, 2.50, -49.95) mm and then
travelling to the center:

| | the sphere's inferred points on arrival | what the click caught |
| --- | --- | --- |
| no Shift | gone; only the connector marker is drawn | `socket mount point`, at (0, 0, -36) mm |
| Shift held from the face | still drawn, the whole set | `socket mount point`, at (0, 0, -36) mm |

So the lock does what Onshape says it does, and the frames show it:
`capture/mate-center/nolock-02-arrived.png` has lost every white inference square by the time the
cursor reaches the middle, and `lock-02-arrived.png` still carries all of them. What beat it is
narrower than "inferencing": `socket mount point` is a mate connector body sitting on the exact
target pixel, and a click there selects the body rather than any inferred point. A lock on the
face cannot win a pixel another body already owns.

Holding Shift is worth teaching anyway, and worth teaching early. It is the answer to the ordinary
version of this problem — the reference jumping from a cylindrical face to the circular edge as
the cursor crosses it — which is most of the mate connectors in this guide. It is not the answer
to a marker parked on the point you want, and on this socket the camera angle is.

### What the square view actually catches

Not the slit, on this model. `socket connect to robot` is the socket's own mate connector, which
comes into the head inside `get socket`, and it sits at (0, 0, -36) mm — dead on the axis,
between the camera and the cavity. A click at the center of the opening lands on its marker and
the dialog reads `socket connect to robot`. Hiding `socket mount point`, which is what the page
tells the reader to do, does not hide it: that connector belongs to the derived feature, not to
the head.

### What tutorial 5's step becomes

The step loses its hide and gains a turn. Turning the view off the axis clears every obstacle at
once, and it was proved with nothing hidden at all: with `socket mount point` shown and the
socket's own connector shown, the turned pick still came back `Jr6` alone on (0, 0, -45) mm. The
one thing that does have to go is a `head mate` that already exists, and a reader building the
page for the first time does not have one.

The frames are in `capture/mate-center/`, and the four runs are
`scripts/s2_turn_view.py`, `s3_spike_pick.py`, `s4_square_on.py`, `s5_unhide_and_turn.py` and
`s6_shift_lock.py`. The head tab was left as it was found: 26 features, no `spike mate`, nothing
hidden.

Onshape dropped its websocket part way through and put up *Onshape is not connected. Your document
is saved.* The canvas freezes: no camera is reported, and a tree row's menu comes up without
**Hide** on it. Both read as ordinary script bugs. The banner's own *Click here to reconnect* link
fixes it.

## Tutorial 1 reproduces, and the page was wrong about which way `n` turns first

`torso.rst` was followed into `stickbot-draft9p4-check` on 2026-09-11, one block at a time, reading
only what the page says. The check document started on Onshape's own `Part Studio 1` and
`Assembly 1`, which is the arrival state the page describes, and ended holding `body`,
`robot sizes`, `Assembly 1` and `BOM : Assembly 1` with the version
`tutorial 1 - variables and torso` published. `robot sizes` reads `torsoH 96 mm`, `torsoW 72 mm`
and `torsoD 48 mm`; the torso's bounding box reads `lowX -36 / highX 36`, `lowY -24 / highY 24`,
`lowZ -48 / highZ 48` mm, which is 72 × 48 × 96 mm on the origin to within 0.001 mm; the tree reads
`Default geometry`, `Origin`, `Top`, `Front`, `Right`, `torso outline`, `torso block`, `Parts (1)`,
`torso`, with no error row. The audit is in [`log/torso.jsonl`](log/torso.jsonl).

**The page had the two square-on views backwards.** It told the reader that the first **n** from the
arrival camera looks at the sketch from behind. Pressed one at a time from `shift+7`, the first
**n** gives the near side: the plane's name reads the right way round and +X draws to the right. A
second **n** gives the far side, and a third comes back. The paragraph now says that, and it says
the camera you start from is what decides which side comes first, because a tab remembers its
camera and a reader who has been turning the model will not get the same first side.

**Which side you are on cannot be read off the view cube in the DOM.** The cube's face label is
drawn, not text, so a script that wants the answer has to project a known axis and look at where it
lands: +X to the right is the near side, +X to the left is the far one.

**Three frames the take made had nowhere on the page to sit, and two of them were the plan's.**
[`../../../build/plan/01-torso.md`](../../../build/plan/01-torso.md) asks for the insert-into-all
control on and off as a pair, and both frames existed and neither was placed. The third is the
Workspace units dialog as it arrives, on Inch with three decimals, which is the picture of the thing
the step is there to change. The page now shows all three.

**One frame was deleted rather than placed.** `document.units-05` is the screen after the dialog
closes, and it is the same screen as `document.units-01`, which is what the page already says out
loud: a unit change moves nothing you can see. It is recorded in the log as unpublished, with why.

**A freehand rectangle's corner snaps, so a pick computed from millimeters misses the line it
wants.** Both dimensions had to be driven off edges read from a screenshot instead. Worse, applying
`#torsoW` to the width scaled the rectangle uniformly — both sides shrank by the same ratio — so the
horizontal edges are somewhere new by the time the height dimension is picked, and they have to be
re-measured between the two.

**Two toolbar positions were found by hovering and are worth having.** In a sketch, **Dimension** is
at x 970 and x 634 is **Construction**, which clicks silently and leaves the next keystroke with
nowhere to go; the error it produces is `no field has focus`. In a Part Studio, the scan has to stop
before x 1210: hovering **Add custom features** raises a hint banner with no close button that
refuses every frame for about half a minute.

## The copy carried `head` and `body` exactly, and the settled half of the check has no reference

`read_shape.py`'s read of draft9p4 at its own `Start` version, diffed against draft9p3's
`log/head.faces.json` and `log/body.faces.json`: **47 faces and 20 faces, the same face in both,
face for face.** Neither tab is in error at that version and the studio holds draft9p1p1's eleven
rows. So the workspace copy carried draft9p3's geometry and nothing about the copy is what a later
difference would be blamed on. The reads are `log/start.head.faces.json` and
`log/start.body.faces.json`.

**In the live workspace both tabs are in error, and it is tutorial 1 doing what the plan said it
would.** Emptying the studio took eight rows out from under them. `head` has four errors, and all
four are tutorial 5's: `get socket`, `add socket to head`, `drop socket to neck` and `head mate`.
`body` has three, and all three are the `###name = #value` variable features that read the rows
that went, with warnings on `trim shoulder pattern`, `hip connector location` and
`torso shoulder profile` behind them. Nothing outside the retake lists is red, and a read of the
workspace measures a broken model rather than a moved one; the version is what the diff has to be
taken at until tutorials 4 and 6 type the rows back.

**The settled half of the check cannot be run against draft9p1p6, because draft9p1p6 has no `head`
and no `body`.** Its tabs at version `F done - Phase F proved` are `ball and socket`,
`ball with cylinder`, `hinge`, `l limb`, `robot sizes`, `socket with cylinder` and `u limb`. It is
the joints document, and [`plan.md`](plan.md) § *What we do not know yet* already says `head`,
`body`, `foot` and `gripper` have no model at the settled joint — the same fact, reached from the
other side.

So *whether tutorials 2 and 3 carry* is measured in draft9p4 and nowhere else, and the measurement
is the same diff run again once the studio holds the settled rows, which is after tutorial 6. The
walk through draft9p1p1's dependency graph says it will pass; nothing yet has measured it.

## Tutorial 2 reproduces, and four of the page's sentences were wrong about the clicks

`head.rst` was rewritten to the variables ruling and then followed into `stickbot-draft9p4-check`
on 2026-09-12, one step at a time. The check document's `head` tab ends holding twenty-one rows in
the order the page lists them: `#headW`, `head profile`, `#headD`, `head body`, `#round`,
`upper rounds`, `#chamfer`, `lower head chamfer`, `#eyeX`, `#eyeUp`, `#eyeRx`, `#eyeRy`,
`eye profile`, `#face`, `eye`, `second eye`, `#mouthW`, `#mouthH`, `#mouthDn`, `mouth profile`,
`mouth`, with one part called `head` and no error row. Its bounding box reads x ±36 mm, y −33 mm to
30 mm, z ±36 mm, which is 72 × 63 × 72 mm; the part has 29 faces. The version
`tutorial 2 - the head` is published in both documents. The audit is in
[`log/head.jsonl`](log/head.jsonl) and the face read is [`log/t2.head.faces.json`](log/t2.head.faces.json).

**Every frame the page had was a picture of the old feature list, so the whole page was recaptured.**
The twelve numbers used to sit in one block at the top of the tab, and the shot of any dialog on
this page has the tree beside it. A frame of an ordering the page no longer teaches is a page
defect, not a stale-looking picture, so none of draft9p3's head frames carried.

**The Variable tool is not on the Part Studio toolbar, and it is not on the context menu either.**
Hovering x 1020 to 1320 at y 58 gives `Move face`, `Replace face`, `Plane`, `Frame`,
`Sheet metal model` and `Add custom features`, and `Default geometry`'s right-click menu has no
`Variable` on it. The route the page teaches is **Search tools**, or **alt/⌥+c**, then `variable`,
and a variable made that way lands at the end of the feature list, which is the ordering the
variables ruling asks for. Two frames of a toolbar button that does not exist were deleted rather
than shipped.

**The page said one Vertical relation was enough, and the model carries two.** `head profile` has
`VERTICAL ×2`: the arc's ends being level and the bottom line joining them does not tie one side's
lean to the other's. The page now says to pick both sides, and the two frames were retaken with
both picked.

**A fillet given a face rounds every edge of that face, so the two-arc pick has to be proven, not
assumed.** The first run of `upper rounds` landed on the arch's top face; `Entities to fillet` read
*Face of head body* and the result was the same 12-face head with both rims rounded at r 12 mm. The
shape being right is what makes the wrong pick silent. The step now reads the selected-pixel count
after each click and fails if the second click added nothing, and the page tells the reader what
the dialog should say.

**Measuring the mouth's drop to the line instead of to its end cannot be solved.** Picking the line
and the origin asks for the shortest distance from a point to a segment; Onshape takes the
constraint, refuses to solve the sketch, and leaves the line where it was with everything drawn
red. Both position dimensions now run from the origin to the line's left end, one out to the side
and one below.

**Slot makes its own pick, and a pre-selected line sends it past the pick.** With the line already
orange, arming Slot goes straight to setting the width, so the click meant for the line sets a
width of nothing and drops the tool: four runs drew no slot at all and left three dimensions on a
bare line. Clear the selection first and the tool takes the line, the width and the **Enter**. Its
own diameter dimension then parks four radii above a round end, exactly where the page says.

**A dimension's witness lines open it as readily as its label does.** The first attempt at the
slot's diameter double-clicked 15 mm out and 2 mm up and got the drop dimension's box, overwriting
18 mm with 10 mm. The driver now refuses a box that already holds an expression it typed.

**Three more click facts came out of the run.** `n` gets swallowed unless the pointer is moved back
to the middle of the canvas before each press; the head's profile needed three. A dimension label
dropped on the model makes a two-entity dimension instead of opening a box, and 30 mm below the
origin is where the head's bottom edge is drawn. And reloading a tab commits an open sketch dialog
rather than dropping it, so a step that dies mid-sketch leaves a committed sketch behind and the
next attempt has to delete it first.

## Tutorial 3 reproduces, and the carried page was two frames short

`assembly.rst` was followed into `stickbot-draft9p4-check` from an empty `Assembly 1` last on the
strip, which is where a reader stands when the page opens. The page came out of it at 22 frames,
from 17 carried; `ninja draft9p4` builds it with no warning, every frame on disk is used and every
frame the page names is on disk. The version **tutorial 3 - the assembly** is published in both
documents, and the build document's assembly was rebuilt to match what the page now teaches.

**The carried page was already broken and nobody had read it.** It pointed at
`assembly.rename-03.png` and `version-01.png`, neither of which existed, and left
`assembly.first_tab-01.png` on disk with nothing pointing at it. Sphinx does not fail on a missing
image; it warns, and the warning was one of hundreds from the eleven pages that have no frames yet.

**The Insert panel holds its work in a transaction and only the tick commits it.** Clicking a row
raises the panel's `Inserted:` counter and puts the instance in the tree, but the assembly itself
is unchanged until the green tick. The red cross puts all of it back, and so does reloading the
page, which reopens the panel with the same count still pending. Three runs read the assembly over
REST between row clicks, saw an empty assembly, and were reading the truth; `gui.tick` did not help
because the panel is not a `#feature-dialog`. Its buttons are `.ns-dialog-button-ok` and
`.ns-dialog-button-cancel`.

**A click at the middle of the head's face selects the assembly's origin.** The origin is drawn as
a point at dead center and sits in front of the face there, so the click lights 146 pixels instead
of 24 thousand and the head then sits still however far the mouse goes. The pick has to land on
plain face off to one side.

**Letting go of an instance drag leaves a distance field holding the keyboard.** It arrives with
the free-hand number in it, `90.1 mm` in this run, and typing `90` and pressing Enter set the
occurrence to exactly 90 mm. That is why the page can name a height at all. It is also why the
first attempt ended in an expression list: `f` for zoom-to-fit went into the field and offered
`false`, `floor(x)`, `floor(x,unit)` and `ft`.

**Onshape's Insert panel rows are `.os-select-item-insertable-name`, and the panel opens at
x 246.** The first driver looked for them to the right of x 700, which is where the draft9p3 frames
put them, because those frames were cropped to the panel and the crop reads like a position.

**A reload restores whatever was selected.** Both hero frames came out with the head orange and its
drag triad drawn over the face, because the pose step had left it picked and opening the tab again
brought the selection back. The tree and hero steps now clear the selection before they shoot.

**The tab strip's DOM order is the strip order, and it is not the order `/elements` returns.** The
build document's elements come back `body, head, ball and socket, robot sizes, stickbot, u limb,
hinge, foot`, while the strip reads `stickbot` first. The strip is what tutorial 3 is about, so the
strip is what was read.

## Tutorial 4 reproduces, and the carried page was five frames short and a socket out of date

`ball-and-socket.rst` was built and captured in `stickbot-draft9p4-check` across 21 steps and 95
frames, and the page was written from those frames. `ninja draft9p4` builds it with no warning,
every frame on disk is used, every frame the page names is on disk, and `page_sweeps.py`'s four
sweeps come back clean: no figure published twice, every picture with a sentence above it, and all
13 recorded keystrokes written into their own step blocks.

**The carried page named five frames that no longer exist and carried a socket two drafts old.**
`parts.ball_and_socket.variables-01`, `-03`, `-04`, `-05` and `-06` belonged to the single
`variables` step that task #213 broke up, and 20 frames on disk had nothing pointing at them. The
numbers were staler than the frames: the socket was written as 18 mm across where it is 15.6, the
stalk dimension as `#ball / 4` where the sketch takes `#stalk / 2`, `#grip` as 1.94648 where it is
2.2205, the slit ends as `#ball * 5 / 12` and `#ball` where they are `#slit_in` and `#slit_out`,
and the slit floor at 3 mm where it is 4. It also told the reader the joint grips by 0.24 mm a side
"however big you make the robot", which is the one claim that is wrong in principle rather than in
arithmetic: the interference is 2 % of the ball, so it grows with the robot.

**Both mate connectors infer `CENTROID`, which closes task #118.** The stud's sits on
`Face of revolve stud` at z +10 mm on a Ø6 mm disc, the socket's on `Face of collar blank` at
z −10 mm on a Ø15.6 mm disc. Nothing had to be done to get `CENTROID` beyond clicking the middle of
a full circle, where the centroid and the center are the same point.

**A section view belongs to the tab it was made in.** `#fit` lives in `robot sizes`, so the
exaggerated frame means leaving the Part Studio; coming back, `section_is_on(page)` reads `False`
and the model is drawn whole. Nothing lands in the feature tree, nothing warns, and the frames of
the first attempt showed an uncut model with a caption about a gap. The stage now cuts again after
every trip, and the page tells the reader to do the same.

**The `Right` plane cuts through two of the four slits.** The slits sit at 0°, 90°, 180° and 270°
and the plane is x = 0, so it passes down the middle of the pair on ±y. At the mouth there is no
material for the cut to make a face out of on either side, and what shows is the far rim through
the slit void, drawn plain instead of hatched. The honest section is the frame that shows it, so
the page explains the grey rather than reshooting around it.

**The mouth is at a fixed height and `#grip` is not.** The mouth sits at
`y = 0.48 × #ball − #ballLoss = 5.66 mm` whatever the fit is, but its height above the middle of
the ball is `#grip`, which is 2.2205 mm at `#fit` 0.08 and 3.7689 mm at 0.8. A close-up centered
with the first number while the model stood at the second landed 198 px low and ringed empty collar
face. The close-up now takes the height it is centered at as an argument, read off the part's
bounding box rather than assumed.

**The view menu beside the view cube holds `Section view…`, and its rows are leaf elements.** The
button is at (1562, 232) and the row at (1427, 596); the canvas menu readers come back empty on
them, and pressing the button while the menu is open closes it, so the button is pressed until the
row is on the page. The panel that opens is not a `#feature-dialog`, so `gui.tick` and
`cancel_dialog` both walk straight past it, but it accepts and cancels at the same pixels a feature
dialog does. When a cut is already on, the row reads `Turn off section view` instead, which is also
how a stage asks whether the view carries one.

**`Take.pixels` started empty in every process, so the duplicate-frame guard only saw inside one
step.** A take driven one stage per run compares nothing across stages, and two pairs got through:
`part_list-01` and `tree-01` were one full window under two names, and `section.wide-04` was the
crop of the variable table that `collar.grip_variables-03` had already published, to the byte,
because the table really is in the same state at both moments. `page_sweeps.py`'s `blockcheck` is
what found them. `Take` now reads the digests of the frames already promoted into the guide when it
opens, and a frame whose twin is the frame of the same name is a retake rather than a duplicate.
Both pairs were retaken: `part_list-01` now has both parts picked, which lights each name against
its shape, and `section.wide-04` is ringed on the `fit` row.

**A profile drawn to a camera the view has left is a drawing that looks right at the wrong size.**
The build document drew the stud's profile with every click where it was asked to put it and came
out with a ball 0.86088 mm across instead of 12. Frame 03 has the origin ringed at (890, 556), which
is where `gui.zoom_to`'s reading of 20.49 px/mm says it is; frame 05, four clicks later, has the
origin at (923, 97) and the canvas reads 142.876 px/mm. The view moved while the arc was being
drawn, in the run where the arc tool had to be armed a second time, and the picks kept using the
camera from before. Nothing in the frames says so on its own: the profile is the drawing it should
be, at one seventh of the size, and only the radius dimension opening on 0.86088 gave it away. The
run where the arc drew on the first try kept the view and read 6.41194. `gui.px_per_mm` now takes
readings until two agree on the scale and on where the origin lands, which catches a view still in
flight; it does not catch a view that moves afterward, and what moved this one is not known.

**A dimension moves what it has not pinned, and the next pick has to be told.** Setting the arc to
`#ball / 2` from the 6.41194 mm it was drawn at dropped the line across the top by 8 px, and the
pick aimed at the pixel the line was drawn at selected nothing. The step now reads the row the line
is on off the screen with `screen.ink_rows` before each of the two dimensions that pick it. The
capture in `stickbot-draft9p4-check` never hit this because the arc there came out within a tenth
of a millimeter of 6.

## Tutorial 5 reproduces, and four of the page's sentences were wrong about the dialogs

`head-socket.rst` was built and captured in `stickbot-draft9p4-check` across 10 steps and 42
frames, and the page was written from those frames. The five rows draft9p3 had left inert in
`stickbot-draft9p4`'s `head` tab were taken back, and the build document was rebuilt by following
the written page. Both documents end with 26 features and one part `head` of 47 faces, a box from
z −48.2205 mm to +36 mm, a cavity sphere of radius 6.08 mm on (0, 0, −46) mm, `socket mount point`
inferring `CENTROID` on (0, 0, −36) mm and `head mate` inferring `CENTER` on (0, 0, −46) mm holding
one entity. `ninja check` is clean and `page_sweeps.py`'s sweeps come back clean.

**Boolean remembers what `Keep tools` was last left at.** It is not a per-feature default and it is
not off. It arrived ticked in the check document, because the reader's previous Boolean is tutorial
4's `cavity from ball`, which leaves it ticked; it then arrived unticked in the build document,
because the check run had just unticked it. The page tells the reader to untick it and says what
the parts list reads when they have not: three rows, `head`, `Socket body` and `Part 3`. The step
takes the frame of the click only when there was a click to photograph, and records a deviation
otherwise.

**Boolean's box is labeled `Tools`, not `Parts`.** The carried page named the wrong box.

**The Select Part Studio panel lists only the other Part Studios in the document**, never the open
one, and the caret at the left of a row is not the same click as the row's name. The caret opens
the studio and lists its parts and sketches; the name takes the whole studio, which would bring the
ball across as well as the socket. The button that opens the panel is named **Select Part Studio**,
and both tick boxes arrive ticked.

**Turning a section view off keeps its definition.** Reopening the panel shows
`Section plane 1 (Right)` still listed, and a second click on `Right` adds
`Section plane 2 (Right)` beside it. Cancelling the panel with its cross is what throws the
definition away. A stage that wants a clean cut cancels the panel and reopens it rather than
clicking `Right` again.

**Onshape has no pan key, and wheel zoom keeps the pixel under the pointer fixed.** A pan can
therefore be made out of two anchored zooms: zoom out by a factor about B, then in by the same
factor about A, and the scale comes back to where it was while the picture moves by
`(a − 1) × (B − A)`. `pan_point` does that in a few rounds and it is how the section close-up got
the hollow off the bottom edge of the frame.

**The same pixel does not always catch the same entity.** At the hollow's middle the pick sometimes
caught `Edge of lower head chamfer`, inferring `MID_POINT`, instead of `Face of get socket`
inferring `CENTER`. Both stages that pick a face now scout: pick, commit, read the inference and
the origin back off the model, drop, and hand the winning offset to the captured pass.

**From below, the eyes draw over the head's underside.** A pick aimed at (12, 0, −36) mm caught an
eye's center and inferred `POINT` at (12, 0, 8) mm, which is `#eyeX` across and `#eyeUp` up. The
underside scout tries a short list of spots and (12, 12) mm answers with `CENTROID` on
(0, 0, −36) mm.

**Onshape prints a near-zero coordinate in scientific notation.** A hollow on the axis reads
`3.0286066742237234e-15`, and a regex that stops at the `e` reads that as two numbers, so a
three-number origin came back as five. The number pattern has to carry the exponent.

**The `Right` section plane cuts down one of the four relief slits**, so the close-up of the hollow
shows a white slot through its middle. The caption says so, the same way tutorial 4's does for the
pair of slits at the mouth.

## Tutorial 6 reproduces, and a shown sketch cost the build two picks

`torso-joints.rst` was built and captured in `stickbot-draft9p4-check` across 31 steps and 169
frames, and the page was written from those frames. Everything draft9p3 had left in
`stickbot-draft9p4`'s `body` tab after `torso block` was taken back, and the build document was
rebuilt by following the written page. Both documents end with 39 features and one part `torso` of
20 faces, a box x ±55.5509 mm, y ±24 mm, z ±64 mm, five spheres of radius 6 mm on (0, 0, 58) mm,
(±24, 0, −58) mm and (±49.5509, −7.8236, 19.2355) mm, and nine mate connectors whose origins agree
to the last place. `ninja check` is clean and `page_sweeps.py`'s sweeps come back clean.

**The pivot line and the torso's own outline are the same pixels.** `pivot lines` draws its line up
the torso's side at `#shoulder_half`, which is `#torsoW / 2`, so it lies on top of the right edge of
the `torso outline` sketch. Which one a click catches depends on whether that sketch is shown. In
the check document it has been hidden since tutorial 1 extruded it, and both picks caught the line.
In the build document it was shown, and both picks caught the edge: the Plane dialog read
`Edge of torso outline`, and `Use` projected the whole 96 mm side rather than the 8 mm line.

**A line-angle plane forgives that, and a projected edge does not.** The plane holds the whole
infinite line either way, so `plane for shoulder` came out in the same place and only its reference
was wrong. The profile is different: the page hangs the rectangle's midpoint off the projected
line's lower end, which is the pivot point at (36, 0, 40) mm on the short line and the torso's
bottom corner at (36, 0, −48) mm on the long one. The cure was to hide `torso outline`, swap the
plane's entity in place, and draw `torso shoulder profile` and `shoulder` again. The plane keeps its
id through an entity swap, so nothing downstream had to be rebuilt for its sake.

**Reading a feature list row's hidden state off its class did not work.** A probe for
`ns-list-item-hidden` on the row whose text matches the feature name came back `None` for every row,
shown or hidden. The row menu answers instead: it offers `Hide` on a shown sketch and `Show` on a
hidden one, so asking for `Hide` and treating its absence as already hidden is the reliable test.

**The same pick missed once and then landed.** `mate for shoulder stud` aims at a point three
millimeters off the middle of the boss's end, projected through the camera the view arrived with.
The first pass selected nothing there; the second, after the profile was redrawn, selected the face
and put the connector on (44.339, −4.8145, 27.2218) mm, the boss's end to the last place. Nothing
about the stage changed between the two, so a pick that close to a small round face is worth a
retry rather than a diagnosis.

**A dialog that dies mid-step leaves its feature behind.** The connector stage raised on its pick
and the tree kept `Mate connector 1`, unresolved, because a feature dialog writes to the model as it
is filled and only its × takes that back. The repair drops the row by name before it starts.

**All five assembly connectors set `Attachment` to `None`.** The dialog arrives on `To selection`
with the ball's face in `Attach to`; left there, the five would stop resolving the moment a later
Boolean takes that face away, which is how stickbot's five came to report
`Cannot resolve entities`. Each of the five reads back on its ball's center.

## Tutorial 7 reproduces, and the mate's first pick is the part that moves

**Both documents agree on the whole assembly.** `stickbot-draft9p4-check` holds version
`79b42d425f9024fcc7cd99ea` and `stickbot-draft9p4` holds `7f355cc3e40efbf26d248705`. Read back side
by side they agree on the assembly tree, the instance list, which instance is fixed, the mate count,
the mate's name and type, and both occurrence transforms. The head lands at (0, 0, 104) mm in both.

**draft9p3's 0.8 mm is gone.** Its `head mate` inferred a centroid and put the head at
(0, 0.8, 103) mm. draft9p4's infers the ball's center, so the head's middle lands 58 plus 46 above
the torso's and sits on the middle line.

**A fixed instance is an icon, not a word.** The row carries no title and no text; the mark is an
`<svg><use>` whose href reads `#svg-icon-Fix_Icon_Default`. An unfixed instance reads
`#svg-icon-unconstrained-assembly` in the same place, and the assembly's own top row reads
`#svg-icon-Fix_Within_Icon`, which is a different icon and not an answer about any instance.

**The caret that opens an instance is 28 px left of where its name starts.** It carries no text of
its own, so it is reached by offset. Twelve and twenty pixels land on the part's icon and select the
row instead.

**An assembly toolbar button has no `title` and no `aria-label`.** Nothing in the DOM says which of
the eleven mate buttons is which, and the only thing that answers is the tooltip the pointer brings
up. Hovering along `y = 58` and reading the tooltip found `Ball mate (m)` at `x = 492`.

**A right-click menu row is wider than its word.** The center of the `Fix` row is blank space to the
right of the text, and a ring drawn there circles nothing. Taking the narrowest leaf whose text
matches, and ringing 24 px in from its left edge, puts the ring on the word.

**The first selection is the part that moves.** Onshape's own tooltip says so. Driven with nothing
fixed and `neck` picked first, the **torso** traveled 14 mm down to meet the head. With the torso
fixed the reversed order put the head at (0, 0, 104) mm, the same place the right order does,
because a fixed part cannot move.

**Deleting a mate leaves the parts where the mate put them.** The first reversed-order probe left
the torso 14 mm low after its mate was deleted, and the next probe read that as a result rather than
as leftover state. An assembly with no mates is not the same thing as an assembly nothing has
happened to, and the stage now refuses to start unless the head is where tutorial 3 parked it.

**The mate's two connectors have no id over REST.**
`/api/assemblies/d/{d}/w/{w}/e/{e}?includeMateFeatures=true` answers with the feature's name and
`mateType: BALL`, and returns `null` for both `matedEntities` ids. The names come off the dialog:
`head mate of head <1>` and `neck of torso <1>`.

**A click in the graphics area fills the box with `Mate connector of torso <1>`.** Onshape makes a
connector of its own where the click lands rather than using a named one. The neck ball cannot be
clicked at all before the mate, because the head hangs over it; the face that answered was the
torso's front.

## Tutorial 8 reproduces, and the sole pattern fails four ways with nothing turning red

**Both documents hold the same foot.** `stickbot-draft9p4-check` holds version
`72b2929e96c17844bb44f7b9` and `stickbot-draft9p4` holds `7d52c006c01d272fd24cd706`. Read back side
by side they agree on all 31 tree rows, the part's name, the bounding box, the face count, the count
of each kind of face, the five radii, the eight groove roofs and both connector origins.

**Reapply features arrives unticked, and unticked the pattern makes one groove.** Every copy after
the first errors, because a copy has to cut into what the copies before it left. Nothing turns red
and the sole comes back with the slot it started with, which reads exactly like a pattern that went
the wrong way.

**Feature pattern is on a dropdown under Part pattern.** `Linear pattern` opens on **Part pattern**,
and nothing on the dialog says the other choices exist until the label is clicked.

**The Direction box has to be clicked before the plane is picked.** The Features box stays live after
the feature is picked, so clicking `Front` in the feature list adds the plane to the features being
patterned rather than filling **Direction**. The stage clicks the label and then asserts
`Front plane` is in the dialog's words before it goes on.

**The pattern also needs its Opposite direction arrow.** Pointed at the toe the eight copies land
past the end of the foot, where there is nothing to cut, and the sole again comes back with one
groove. Four ways to get one groove, and three of them look the same.

**Every dimension moves what it has not pinned yet, so a circle is read off the screen rather than
computed.** Dimensioning the heel relocated and resized the under-defined toe circle, and the
model-computed pick landed inside the circle's shaded region, which answers a pick the way the rim
does; the dimension then went to the canvas instead of to a field. `circle_on_axis` scans a column
beside the sketch's vertical axis for the two crossings and gives back the circle's middle and radius
in pixels, and every dimension on the outline sketch is placed from that.

**A rectangle's vertical sides read black, not sketch blue.** `is_sketch_blue` sees under-defined
geometry only, and by the time the groove rectangle is measured its sides are held. `rect_edges`
scans for any dark line at all and takes the outermost pair, which is the rectangle's, because it is
the only thing in the sketch wider than the foot.

**Trim cuts what the pointer is over, and the pointer has to be seen to arrive.** Clicking the trim
spot straight away cut nothing. Moving to `EMPTY` first, then to the spot, then waiting 900 ms before
the click, cuts the half circle every time.

**A tree caret's state survives between attempts.** Toggling `Default geometry` blind left it open on
one attempt and shut on the next, and the two tree frames came out byte identical to the two hero
frames. `fold` reads the caret and sets it, and both tree frames are cropped to the left panel, which
is what makes them a picture of the tree rather than a picture of the window.

**`mate to robot` is read through featurescript, not `/features`.** That route was rate limited for
the rest of the run, and `connector_origins` answers with the connector's origin off the model, which
is what the verdict needed.

**The page reproduces, and the two stages that needed a second go are not steps the reader takes.**
Twenty of the 22 build stages stood on the first attempt, including the outline sketch that took six
attempts when it was first driven. The two exceptions were a screenshot that would not settle and the
tree caret.

## The foot has no tread, and every frame that would have shown it is a top view

Found by rendering the sole of `stickbot-draft9p4-check`, `stickbot-draft9p4` and
`stickbot-draft9p3` side by side with `shadedviews?viewMatrix=bottom`. draft9p3's sole carries eight
open notches. Both draft9p4 soles are one smooth face.

**The grooves are inside the foot, 2 mm above the ground.** They are eight tunnels running across
the foot's width with a 2 mm skin of material under them. From the side they read as windows. The
sole at z −24 mm is a single unbroken face, and there are faces at z −22 mm and at z −20 mm where
draft9p3 has faces at z −22 mm and nine land strips at z −24 mm.

**`sole groove` has two Opposite direction arrows and only one was turned.** `parts.foot.groove-06`
shows the **Starting offset** arrow lit and the **Depth** arrow not. The cut starts 22 mm below the
sketch, which is right, then runs 2 mm back up toward the sketch instead of down onto the sole. The
page's sentence already says to turn both; the driver turned one.

**The pattern is right.** The eight grooves sit at y −61 to −55, −49 to −43, −37 to −31, −25 to −19,
−13 to −7, −1 to 5, 11 to 17 and 23 to 29, in both documents, which is 8 copies at 12 mm along
`Front` with 3 mm of land at the toe and 3 mm at the heel. `groove profile` is the same rectangle in
draft9p3 and draft9p4. Only the depth direction is wrong.

**`shift+5` gives the Top view, not the bottom one.** The page says "Press **shift+5** to look from
underneath" and the frame it takes reads `Top` on the view cube. `hero-02`, `parts.foot.groove-09`
and `parts.foot.ribs-01` are all top views of a foot whose sole is not in the picture, captioned as
the sole with grooves across it. The page never shows the sole once, which is why nothing caught
this. The key that does give the bottom view has to be found before the retake.

**Every measurement agreed while the shape was wrong.** Both documents matched on 31 tree rows, the
part name, the bounding box, 60 faces, the count of each kind of face, the five radii, the eight
groove roofs at z −22 mm and both connector origins. Tunnels and notches carry the same face count
by coincidence: eight notches give a roof, two walls and nine land strips, which is 33 faces at the
bottom, and eight tunnels give a roof, a floor, two walls and one sole, which is also 33.

### What the foot needs

- **Edit `sole groove` in `stickbot-draft9p4-check` and turn the Depth arrow.** `sole ribs` follows
  it. Then do the same in `stickbot-draft9p4` and publish `tutorial 8 - the foot` again in both.
- **Find the key that gives the bottom view**, and correct `shift+5` where the page names it: the
  hero at line 23, the two sentences in the groove and ribs steps, and the measure table's last but
  one row.
- **Rewrite the alt text that describes grooves nobody photographed**, on `hero-02`,
  `parts.foot.groove-09` and `parts.foot.ribs-01`.
- **Add the check that would have caught it**: the sole at z −24 mm is nine faces, not one, and no
  face stands at z −20 mm. Render the sole and look at it beside draft9p3's, which is now what the
  _Model inspected_ gate asks for.
- **Amend `.docs/build/plan/08-foot.md`.** `## Built` says "Eight groove roofs stand at z −22 mm",
  which is the sentence that passed while the sole stayed smooth, and `## Captured` says the page
  reproduces.

### What has to be retaken

- **The 15 frames from `parts.foot.groove-06` through `parts.foot.ribs-11`.** `groove-06` is the
  dialog whose preview changes, `groove-08` and `groove-09` are the foot with one slot, and the
  eleven `ribs-*` frames show the sole through the pattern. None of them shows a state the model
  will have.
- **`hero-02`**, which is the page's picture of the finished tread.
- **The 28 frames from `parts.foot.socket.derive-01` to the end**, wherever the foot's lower edge is
  in the picture. The slot mouths show along the side of the foot from a corner view, so most of the
  derive, combine, rename and connector frames are pictures of the old shape. Check each one rather
  than assuming; the panel crops and the version dialogs are likely to stand.
