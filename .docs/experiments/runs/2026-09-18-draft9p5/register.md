# draft9p5's register

What was built, what each ring caught, and what was done about it. The plan is
[`plan.md`](plan.md); the reads are in [`results/`](results/).

## Phase A0 — the document and its ten tabs, 2026-09-18

**Done.** `stickbot-draft9p5` holds the ten tabs the declaration names, in Phase B's build order,
and the workspace is in millimeters. The ids are [`results/ids.md`](results/ids.md).

- **The ten tabs were read back from Onshape after they were made**, by name and type and in order,
  and the script fails if the list is anything else. They were also seen in the tab bar in a frame
  of the open document.
- **The workspace length unit was read back from a dialog opened again**, not from the one it was
  typed into: millimeter, display decimals `0.12345`. A new document is in inches.
- **No feature was posted.** Every tab is empty.

### What moved since the scripts that last did this were written

Three endpoints the 2026-08-30 run used are gone or were never written down here. Each replacement
was measured on 2026-09-18 against this document.

- **A Variable Studio is created by `POST /api/variables/d/{did}/w/{wid}/variablestudio`.**
  `/api/variablestudios/...` and `/api/elements/.../variablestudio` are both 404.
- **An element is renamed through its metadata**, `POST /api/metadata/d/{did}/w/{wid}/e/{eid}`,
  carrying the `Name` property's id read back from the matching GET.
  `POST /api/elements/d/{did}/w/{wid}/e/{eid}/update`, which
  [`2026-08-30-draft9p1p2/build.py`](../2026-08-30-draft9p1p2/build.py) uses, is a 404.
- **There is no REST endpoint for workspace units.** Three candidate paths answered 404, so the
  unit is set by driving the dialog, which is the one dialog built from real `select` elements.

### Two documents were created, and one is in the trash

`find_document` answers `None` for a document that exists: Onshape's document search does not index
a new document for some minutes, and a search for `stickbot-draft9p5` returned zero items while two
documents of that name were open. A create-if-missing script run twice therefore made a second one,
`9b398e076ce2ea8a25710938`. It is trashed, nothing was built in it, and
[`scripts/a0_create.py`](scripts/a0_create.py) now names the document by id rather than finding it
by search.

### Two refusals worth knowing before deleting anything

- **An Assembly cannot be deleted while its Bill of Materials exists.** Delete the BOM first, or
  the Assembly's delete is a 409.
- **The last element in a document cannot be deleted**, also a 409. That is why `robot sizes` is
  the renamed survivor rather than a fresh element: the Variable Studio was the one element left,
  and renaming it put the first tab in the first position.

### What was noticed and not chased

- **This account's documents carry an education icon.** The document header renders
  `os-document-icon os-education-icon`. The plan's § *What we do not know yet* asks which Onshape
  plan this account is on, because `before-you-start.rst` describes a plan nobody here has used.
  This is one reading of one class name, not an answer, and Phase A0 did not chase it.
- **`robot sizes` arrived with *Insert into all Part Studios and Assemblies* already ticked**, seen
  in the same frame as the tab bar. That matches what
  [`onshape-gui-howto.md`](../../../onshape-gui-howto.md) § 3b measured for the first Variable
  Studio in a document, and it held for one created over REST.

## Phase A — the reads that settle what a record cannot answer, 2026-09-18

**Done.** All six items. Each wrote its answer into [`results/`](results/).

### `ninja brief-sheets` changes nothing, and every sheet has an owner

The four sheets re-rendered byte for byte identical, and `git status` on
[`../../build-briefs/`](../../build-briefs/) is clean. All 32 files in that folder's `images/` are
referenced by a brief; none is orphaned.

### Every variable's first reader, walked

[`results/variable-first-reader.md`](results/variable-first-reader.md). The walk reads every string
in every feature at any depth, because a sketch's dimensions live in `constraints`, a sibling of
`parameters` — scanning parameters alone reported tabs whose every length is driven as reading
nothing, which is how the first run of this walk was caught being wrong.

- **The variable counts agree with the plan's table**, tab by tab: `body` 8, `head` 12, `foot` 13,
  `gripper` 8, `ball and socket` 5, `hinge` 18, the two limbs none.
- **The walk reproduces the 2026-09-11 ruling from the record.** `#ear` and `#backlash` are read by
  nothing in `hinge`, which is why neither is declared. Nothing else in any tab is unread.
- **A Variable Studio has no geometry**, so `robot sizes`' 23 rows have no first reader in their own
  tab. draft9p4 walked those rows once; this walk is each tab's own, which is what the plan asked
  for.

### What each sketch stands on

[`results/sketch-planes.md`](results/sketch-planes.md). The default planes' geometry ids were
evaluated in draft9p5's own empty `ball and socket` tab rather than recalled: Front is the `JC`
family, Top `JD`, Right `JE`, Origin `IB` and `JBD`. `JCC` agreeing with the Front plane id
`onshape_session.py` already carried is the cross-check.

**Across the eight tabs, 22 of 28 sketches stand on a stock plane, and 17 of those had a face in the
tab already.** A tab's first sketch has no face to stand on and is not at issue; the 17 are. `hinge`
holds nine of them, `body` two, `head` two, `foot` two, `gripper` one, `ball and socket` one. Each
one needs a reason written beside it or a face to move to, and that is decided at its own tab in
Phase B against its brief, not here.

### The eye, and it is neither candidate

[`results/eye.md`](results/eye.md). `eye profile` in `stickbot-draft9p4-check` dimensions the
ellipse's two diameters with the numbers the mouse landed on —`15.983648598194122*mm` and
`8.132031187415123*mm` — while the two dimensions that locate its center carry `#eyeX` and `#eyeUp`.
Half of each literal is the radius the sketch reports, and pi times those two is 102.0857 mm²,
which is the face area that started the question. The page is sound: `head.rst:510` says to type
`#eyeRx * 2` and `#eyeRy * 2`, and the paragraph after it says to read the number in the box first.

The cause is in neither the model's design source nor the page's words, so there is no line for the
register to rewrite. draft9p5 drives both diameters, and Ring 1 reads the sketch's constraints back
before the extrude runs.

### The six open numbers

[`results/open-numbers.md`](results/open-numbers.md). Four are already right in the parent and are
carried; #118 is a correction draft9p5 makes, building both `ball and socket` connectors on
CENTROID; #215, `sole groove`, is the defect draft9p5 has to build its way out of at the `foot` tab.

### The ten connector names

[`results/connector-names.md`](results/connector-names.md). Every old name the plan's rename table
lists was found in the parents' records, spelled as the plan spells it, and the 23 `mateConnector`
features across the eight tabs match the plan's count.

## Phase B tab 1 — `robot sizes`, 2026-09-18

**Built and through both rings.** 23 rows, the four drivers and the 19 the build plan's
*ones the rule brings up with them* table carries. The script refuses to write a row the build
plan does not ask for, because that table is the whole ask for what is a variable.

- **Ring 1.** All 23 read back with the expression they were sent, in the order they were sent.
  [`results/robot-sizes.variables.json`](results/robot-sizes.variables.json).
- **Ring 2.** Every row resolves, evaluated in the `ball and socket` tab rather than in the studio,
  to the number `make_plans.py` computes, imported and not copied, to within 1e-6 mm.
  [`results/robot-sizes.resolved.json`](results/robot-sizes.resolved.json). Asking a Part Studio is
  what also proves the Part Studios can see the studio at all: `robot sizes` arrived with *Insert
  into all Part Studios and Assemblies* ticked, and the eight Part Studios were created after it.
- **Recovery point.** Version `tab 1 - robot sizes`, `9d4f31e4d33a22c3d9a62fec`.

### A variables payload cannot reference a row it carries

The first write of all 23 rows in one POST was a 400, and it reproduces: into an empty studio, the
four literal drivers in one write are a 204, and the same four plus `#wall`, which reads `#torsoH`,
are a 400. Written as 23 growing prefixes all 23 are accepted, because each prefix's last row reads
only rows the previous write committed. The write replaces the whole table every time, so the
prefixes leave exactly the 23 rows and no duplicates.

**This belongs in [`../../../onshape-api.md`](../../../onshape-api.md), which this draft does not
own.** It is recorded here and named to Mike rather than written there.

## Phase B tab 2 — `ball and socket`, 2026-09-18

**Built, through Ring 1, and through Ring 2 except the section.** 14 features: the nine the brief's
*Recommended steps* names, and five variables each typed immediately above the first feature that
reads it.

- **Ring 1, after every one of the 14 writes.** Every feature read back with the parameters it was
  sent, every `featureStates` entry `OK`, and `rollbackIndex` equal to the feature count each time.
  [`results/ball-and-socket.ring1.json`](results/ball-and-socket.ring1.json).
- **Ring 2, the shape.** 22 faces on 2 bodies, and `diff_shape.py` against draft9p1p6's record says
  *the two parts are the same shape, face for face*. The construction changed; the shape did not.
- **Ring 2, what each feature was told.** `diff_features.py` reports two differences and no others,
  and both are this draft's own: the order, with the five variables interleaved instead of blocked
  at the top, and `stud connect to robot`. 13 of 14 features agree on every parameter.
- **Ring 2, the pictures.** The tab's isometric holds beside
  [`../../build-briefs/images/cad-ball-and-socket-iso.png`](../../build-briefs/images/cad-ball-and-socket-iso.png):
  same stalk, same ball seated in the same mouth, same four slits in the same places. The socket
  rendered on its own shows what the assembled view cannot — the spherical cavity, the mouth
  narrower than the cavity behind it, and the four slits running down from the rim. No frame was
  kept, so none is committed.
- **Recovery point.** Version `tab 2 - ball and socket`, `b0316a744f2ab1a752520744`.

### #118, made and measured

`stud connect to robot` is built CENTROID, and that is two changes rather than one: a CENTER
inference takes a second query to say what it is the center of, and a CENTROID takes one face and
nothing else, which is how `socket connect to robot` is built. Sent with the inference changed and
the second query left in place, the feature fails with *Failed to resolve mate connector coordinate
system*.

Measured after: the stud's connector is at `(0, 0, 10) mm` with z `+Z`, and the socket's at
`(0, 0, -10) mm` with z `-Z`. Those are `#stand` and `#collar`, and their being equal and opposite
is what `#collar = #stand` is for. CENTROID lands where CENTER did, as #118 said it would.

### Scoring the construction caught a defect the replay carried in

The parent types over all five of this tab's variable titles, and a feature replayed verbatim
carries that across. An untyped Variable feature's row reads the literal `###name = #value`, which
is what `robot sizes` holds and what a student gets, so the builder now writes that title on every
`assignVariable` whatever the parent called it. The tab was rebuilt: five rows of five now read
`###name = #value`, and all nine geometry features carry typed names.

**This is why the scoring is a step and not a formality.** Every ring before it passed on the tab
that still had the five typed titles: the faces matched, the parameters matched, the pictures
matched. Nothing measures a title.

### `collar profile` keeps the Top plane, with a reason

It is one of the 17 sketches Phase A found standing on a stock plane with a face already in the
tab. The face that exists is the stud's, and there is no planar face anywhere near the ball's
center, because the stud there is a sphere. The socket is a separate part — `collar blank` is
`operationType NEW`, and the stud is only the tool `cavity from ball` hollows it with — so tying
the socket's first sketch to the stud's topology would make one half of the joint's tree depend on
the other half's. The Top plane carries the ball's center, which is what places the socket.

**Phase A's *a face existed* column means a solid was in the tab, not that a face was available
where the sketch has to be.** The other 16 are judged the same way, at their own tabs.

### Not done on this tab

**The section has not been held beside `brief-socket.svg`.** `shadedviews` renders no section, so
it is a GUI drive and it has not been performed. Until it is, this tab has not been through all of
Ring 2, and it is not claimed as finished.

### What replaying a parent's features takes

- **A feature's wrapper type has to be carried across.** A sketch posted as `BTMFeature` is refused
  with *must be of type BTMSketch* — and it is created anyway, after which the whole `/features`
  GET answers 400 and the tab cannot be read at all. The GUI tree row carries a `feature-id`
  attribute, which is how the one built here was found and deleted.
- **A query can name a feature, and that name has to be remapped.** A sketch region is a
  `BTMIndividualSketchRegionQuery` carrying the sketch's own `featureId`. Replayed verbatim it
  points at a feature this document has never had, and the extrude comes back *Select face or
  sketch region to extrude, 1 missing selection* while the geometry id beside it is perfectly
  valid.
- **Deterministic geometry ids need no remapping.** Built in the same order they regenerate the
  same: the stud came back as body `JHD` and `collar profile`'s region as `JJC`, which is what the
  parent's record calls them.

## The `/features` daily quota went, 2026-09-18

**Onshape refused `/api/partstudios/.../features` with `x-rate-limit-remaining: 0` and
`retry-after` reading 22.4 hours, until about 16:17 on Sat 19 Sep.** That is the quota mode, not
the burst mode: nothing this client does shortens it, so the plan changes rather than the delay.

**What still answers, tested rather than assumed:** `parts`, `sketches?includeGeometry=true`,
`bodydetails`, `massproperties`, `metadata`, `variables`, `documents` and `versions` all returned
200 with `/features` at 429. Only `/features` is spent, and a version's read paths answer too, so a
tab that has been published can still be measured.

### What spent it, and what changes

`ball and socket` was built five times: once to find that a sketch must be posted as `BTMSketch`,
once to find the `featureId` remap, once to find that #118 is two changes, once after the
construction scoring caught the typed variable titles, and once for the part names. Each build was
14 POSTs, 14 Ring 1 GETs and 14 deletes against that one family, and every probe of the tree cost
another. The whole robot is 187 features; the rebuilds cost more than the robot would have.

- **Ring 1 no longer reads the list back after a variable.** A variable cannot break geometry on
  its own, its expression is proved by the first feature that reads it, and the `featureId` it was
  given comes out of the POST's own answer. Sixty-seven of the 187 features are variables.
- **Every geometry feature still gets the full read**: parameters one by one, every `featureStates`
  entry, and `rollbackIndex` against the count.
- **A sketch's entities come from `sketches?includeGeometry=true`**, a family that kept answering.
- **The corrections are settled before the build, not found during it.** That is what the plan's
  unrolled checklist is for.

**This is a departure from the plan's § *Ring 1 — the feature, after every single `POST`*, and it
is Mike's to rule on.** It is written here rather than quietly done.

### Where `ball and socket` stands

The tab had been cleared for the rebuild that adds the part names when the quota went, so the
workspace holds a partial tab: two sketches and two bodies, no mate connectors. **The complete
14-feature build is in version `tab 2 - ball and socket`, `b0316a744f2ab1a752520744`**, and that
version can still be measured because its read paths answer.

Restoring that version into the workspace over REST was tried and is not available:
`/api/documents/d/{did}/w/{wid}/restore/{vid}` is a 404 and
`/api/documents/{did}/workspaces/{wid}/restore/{vid}` answers 500 with a support code. Nothing was
changed by either — the document still reads eleven elements, three versions and 23 rows. No
further document-level write was tried.

### What the rest of 2026-09-18 goes on

Building is blocked until the quota resets, so the work is everything that does not need
`/features`: the unrolled checklist, the derived build order for all nine tabs, the builder wired
to it, and `ball and socket`'s acceptance numbers measured against the published version.

## Writes answer while reads do not, 2026-09-18

**With `/features` GET at 429, a `POST` to the same `/features` answered 200.** Reads and writes
bill separately on that path, so the CAD is written now and Ring 1's feature read is owed. Mike
asked for exactly this split: do the steps that write the CAD, verify later.

What stands in for the read while it is owed, all on families that kept answering:

- **`bodydetails`, diffed against the parent face by face.** A feature that failed to regenerate
  shows up as missing geometry, and this is what caught both of the day's defects.
- **[`scripts/what_built.py`](scripts/what_built.py)** asks the model, over `featurescript`, how
  many faces and bodies each feature id created. A feature that made nothing and is not a variable,
  a mate connector or a plane is where to look. It named `blade wedges` and `copy ball stud`
  without a single `/features` call.
- **[`scripts/why_failed.py`](scripts/why_failed.py)** hovers the tree row and reads the sentence
  Onshape writes there. `featureStates` carries only `OK` or `ERROR`; the tree says *Error
  regenerating* or names the missing selection.
- **[`scripts/tree_ids.py`](scripts/tree_ids.py)** reads every feature's id off the tree's
  `feature-id` attribute, so a tab can be cleared or resumed with the list route refused, and
  [`scripts/clear_tab.py`](scripts/clear_tab.py) deletes from that list.

**A feature that creates nothing is not always a failure.** `trim shoulder cut` creates no face
because it cuts the shoulder boss flush with the torso's top, and the tree says nothing about it.
The count is a place to look, not a verdict.

### Two spellings of the same idea, and both cost a tab

- **`featureIds`, not `featureId`.** A sketch region query carries `featureId`, a single string,
  and the remap handled it. A pattern or mirror set to repeat *features* carries a
  `BTMParameterFeatureList`, whose `featureIds` is a list; `blade wedges` names `blade wedge` that
  way. Left unmapped it names a feature this document has never had, and Onshape neither errors nor
  patterns anything. The hinge came back **29 faces against the parent's 510**, with the seed wedge
  present and all 24 copies missing. Every mirror and pattern in the robot goes through this.
- **`e` before the element id.** A derive names its source in the `partStudio` parameter's
  `namespace`, spelled `e<elementId>::m<microversion>`. Written as `<elementId>::m<microversion>`
  the feature is accepted and then fails to regenerate, saying only *Error regenerating*. The
  convention was read off draft9p1p6's own `add socket` and `add fork` and checked against that
  document's element ids rather than guessed.

**Both were invisible to every check except the shape diff.** The writes returned 200, the features
are in the tree, and nothing said a word until the faces were counted.

## Phase B tabs 2 and 3, 2026-09-18

- **`ball and socket` is whole and its parts are named.** The tab was resumed from index 6 —
  `#stalk` through `cavity from ball` had survived the quota — and `Ball stud` and `Socket body`
  were written and read back. 22 faces on 2 bodies, face for face with draft9p1p6.
  Its acceptance checks are [`results/ball-and-socket.acceptance.json`](results/ball-and-socket.acceptance.json):
  eleven measured against `make_plans.py` and passing, and the twelfth, `Ball stud` volume, needs
  `massproperties?massAsGroup=false`, which the first run did not ask for.
- **`hinge` is built: 44 features, 2 solids, 510 faces, face for face with draft9p1p6.** `#ear` and
  `#backlash` are not declared, as the ruling says. Ring 1's feature read is owed.

## The seventeen stock-plane sketches need a ruling, not a quiet rewrite

Phase A found 22 of 28 sketches standing on a stock plane, 17 of them with a solid already in the
tab. `ball and socket`'s one was answered at its tab: there is no planar face at the ball's center
because the stud there is a sphere, so `collar profile` keeps the Top plane with a reason.

**`hinge` holds nine of the remaining sixteen, and all ten of its sketches stand on a plane.**
`blade profile` is the tab's first and has nothing to stand on. The other nine — `stub axle
outline`, `blade wedge outline`, `blade rod outline`, `relief slit outline`, `fork outline`, `fork
blade top cut outline`, `pocket axle sketch`, `ear wedge outline` and `fork arm outline` — each had
a solid in the tab when they were drawn.

**Moving a sketch from a plane to a face is re-authoring, not replay.** It changes what the feature
is built on, so the deterministic ids downstream of it move, the replay of every later feature has
to be re-derived, and the tab stops being face-for-face with the parent until it is proved again.
That is a different job from the one this draft has done to the hinge today, and it is nine
judgments about what actually places each feature, not one rule applied nine times.

**So they are recorded and not moved.** The reasons that hold are written where they hold; the ones
that should move are named for Mike rather than rewritten tonight, because each move costs the
guarantee the tab currently carries and needs a verification pass that the `/features` quota will
not allow until it resets.

## Standing sketches on faces, 2026-09-18

**Mike ruled: move the sketches to the faces they belong on, and look at the result from several
angles as it goes.** The hinge was taken first, because it holds nine of the sixteen and derives
from nothing, so it could be worked while the derives were blocked.

### What the hinge's ten sketches actually are

Every one is fully constrained and anchored by `COINCIDENT` to the joint's axis — 5, 1, 8, 6, 5, 3,
5, 1, 8 and 6 anchoring constraints — and not one is placed by typed coordinates. The extrudes are
symmetric where symmetry is the intent: `blade blank` about the blade's mid-plane, `stub axle`
about the same plane to `#blade + 2 * #stub_proud`, `relief slit` and `pocket axle on fork` about
theirs.

**Measured: no plane through the origin carries a face.** The blade's own faces are at y ±5.0 mm,
the fork's seat at ±5.9 mm, the wedge rings at ±5.15 mm and ±5.75 mm. So eight of the ten sketches
have no face to stand on at all, and standing `stub axle outline` on one would replace a symmetric
cylinder with a one-sided one — the symmetry is what keeps the stub concentric when `#blade` moves.

**Two of the ten do fail the ruling, and they are the two the start offsets give away.**
`blade wedge` extrudes with `startOffsetDistance` `#blade / 2` and `ear wedge` with `#seat / 2`:
arithmetic reproducing the position of a face the model already has, which is exactly *never type a
number to place something a reference would have given you*.

### `blade wedge outline` now stands on the blade's face

Moved onto `R+DC`, the blade's flat face at y +5.0 mm, area 442.763 mm², and `blade wedge`'s start
offset dropped. **The hinge reads 510 faces on 2 bodies, face for face with draft9p1p6**, so the
wedge ring came out exactly where it was and `#blade / 2` is gone from the placement. The isometric
was held beside
[`../../build-briefs/images/cad-hinge-iso.png`](../../build-briefs/images/cad-hinge-iso.png): same
fork, same blade, same relief slit, same axle bore.

### `ear wedge outline` was tried, failed, and is reverted

Moved onto `SMGyH`, the fork's seat face at y -5.9 mm, the tab came back **270 faces against 510**:
the sketch itself errors and the fork's whole wedge ring goes with it. Flipping the extrude's
direction changed nothing, so direction is not the cause. Reverted to the parent's plane and
offset, and the hinge reads 510 face for face again.

**The cause is not established, and the most likely one is the order of the tree.** `SMGyH` was
read off the finished model, and `two forks` mirrors the prong at step 37, three steps after the
sketch at 34. The face that carries that id at the end need not be the face that exists when the
sketch runs, and a sketch whose plane query resolves to nothing is a sketch that builds nothing.
Settling it means rolling the tree back to step 34 and reading the faces there, which is a write to
the feature list and waits for the quota.

**What this says about the other fourteen.** A move is one update to the sketch and one to its
extrude, and the shape diff says within a minute whether it held. The ones worth making are the
ones whose extrude carries a start offset that names a dimension the geometry already fixes; the
rest are sketches on the plane their part is symmetric about, and moving those would remove the
symmetry rather than add a reference.

## The parts are named, and two briefs were read too narrowly

**Mike caught that the parts were unnamed.** `ball and socket` had been named on 2026-09-18 and
reads back `Ball stud` and `Socket body`; `hinge` and `body` had not, and read `Part 1` and
`Part 2`.

**The names were in the briefs and this draft said they were not.** The first search looked only at
the *Acceptance checks* lists, where `ball-and-socket.md` happens to put them, and concluded that
`hinge.md` and `torso.md` name no parts. They do, in their step prose:
[`hinge.md:40`](../../build-briefs/hinge.md) — *The two parts are named `fork` and `blade`* — and
[`torso.md:150`](../../build-briefs/torso.md) — *Name it `Torso`*. A brief is read whole, not
grepped at one heading.

Named since, each found by the feature that made its body rather than by a part id, because a part
id is not stable across a metadata write:

| Tab | Part | Made by |
| --- | ---- | ------- |
| `ball and socket` | `Ball stud` | `revolve stud` |
| `ball and socket` | `Socket body` | `collar blank` |
| `hinge` | `blade` | `blade blank` |
| `hinge` | `fork` | `fork blank` |
| `body` | `Torso` | the one part the tab is left with |

`head`, `foot` and `gripper` take `Head`, `Foot` and `Gripper` when they are built; `limbs.md` says
only *name the part for the limb it is*, which is a question for those tabs.

**None of this needs `/features`.** Part metadata is its own endpoint family, so the naming was done
with the feature list still refused.

## The derive, and what was asserted without proof

**Mike asked why a derive blocks `body`, and the honest answer is that it may not.** This draft
wrote that every deriving tab was blocked because the derive makes Onshape read the source tab's
feature list, which is the rate-limited route. That was an inference from one POST that had not
returned inside 120 s, and it was recorded as if it were measured. It is being measured now, with a
ten-minute budget, and the register will say what the call actually did.

**What `body` derives is the ball stud, not the socket.** `copy ball stud` brings in `Ball stud`
from `ball and socket`, and three transforms and a mirror turn it into the five studs the torso
carries — neck, two shoulders, two hips. No socket enters the torso at all; the sockets are in
`head`, `foot` and `gripper`.

**The GUI is the route that cannot be rate limited**, which the onshape skill already says, and
draft9p3 has driven the Derived dialog before. Two findings from
[`../2026-08-29-draft9p3/notes.md`](../2026-08-29-draft9p3/notes.md) govern it:

- **Choosing the tab brings every part in it**, and narrowing to the one wanted has to be seen in
  the page's own feature list before the feature is ticked. `/api/parts` answers from the committed
  model and cannot see what a dialog is previewing: the panel read `Parts (3)` while the route
  still said one part.
- **`Transform by mate connectors` will take the origin instead of the connector.** The derived
  stud arrives with its ball on the origin and its connector a stud length up the stalk, ten
  millimeters apart; a pick aimed between them lands on the origin, the feature goes in green, the
  field reads back full, and the ball ends up half sunk in the torso's top face. The connector
  comes across under `copy ball stud` and is picked by name from that row.

## The GUI does what REST will not, and the parents' records are not all replayable

**Measured, with a ten-minute budget: a `POST` of an `importDerived` feature never returns and
creates nothing.** Every other feature type writes in well under a second. The GUI does the same
derive at once, which is what the onshape skill says to reach for and what Mike said to do.

So a deriving tab is built in three moves: REST up to the derive, the derive through
[`scripts/c_gui_derive.py`](scripts/c_gui_derive.py), REST from the next index. `b_build.py` takes
a start and a stop for exactly this.

- **`body` is complete: 20 faces on 1 body, face for face with draft9p1p1**, part named `Torso`.
- **`head` is complete: 47 faces on 1 body**, part named `Head`. It differs from draft9p1p1's head
  by 19 faces, and those 19 are the socket: draft9p1p1's `ball and socket` differs from
  draft9p1p6's by 19 faces each way, and the socket is 19 faces. The head's own 28 match. That is
  the plan's intent — the settled joint everywhere — not a defect.
- **Both eyes measure 100.531 mm², which is `math.pi * EYE_RX * EYE_RY` exactly.** The 1.5 %
  oversize that Phase A traced to a dragged dimension does not exist in this draft.

### The derive dialog, driven

The two traps draft9p3 recorded both held. Choosing the tab previews **every** part in it — the
panel went to `Parts (3)` — and picking the one wanted brought it to `Parts (2)`; the script reads
that count off the page before it ticks and refuses otherwise, since `/api/parts` answers from the
committed model and cannot see a preview. Every failure path presses the red cross, because the
dialog writes to the model as it goes: an earlier crash left a `Derived 1` behind.

### `foot` cannot be replayed from draft9p1p1's record

Four kinds of query came back from `/features` **empty** in that record, and each one is a feature
that builds nothing when replayed:

- **Sketch planes.** `pedestal outline`, `foot outline` and `groove profile` each carry a query
  with no geometry ids. Read live from draft9p3's own `foot`, all three stand on the Top plane, and
  supplying `JDC` fixes them.
- **Merge scopes.** `foot` and `sole groove` are an Add and a Remove with `defaultScope` false and
  an empty `booleanScope`, which is the *No merge scope selected* failure the memory names. The
  builder now gives any Add or Remove with an empty scope and no default a default one; these tabs
  end on one part, so merging with all is what they want.
- **Fillet edges.** `top round` names no edge at all, so there is nothing to round.
- **Pattern direction.** `sole ribs` names no direction, so the eight grooves never repeat.

The first two are fixed and the foot now cuts its groove. **The last two need selections the record
does not carry**, so they are picks to be made rather than parameters to be copied, and they are
the foot's outstanding work.

**`gripper` has the same shape of problem and worse:** its `clip profile` also carries an empty
plane query, and draft9p3's document no longer has a `gripper` tab to read the plane from.

## Phase B, the limbs, 2026-09-18

**`u limb` is complete: 270 faces on 1 body, face for face with draft9p1p6.** Both its derives went
through the GUI — `add socket` from `ball and socket` and `add fork` from `hinge` — and the six
features between and after them replayed over REST.

**`l limb` is built and one feature short of right.** 263 faces on 1 body, and it differs from
draft9p1p6 by 12 faces of mine and 9 of the reference's. The difference is named:

- **`move ball stud` did not move it.** The transform names the stud's body, the connector that
  came in with the derive, and the tab's own `mate for ball stud`, all by draft9p1p6's ids. A derive
  made in the GUI issues its own, so none of the three resolved and the stud sits at the origin —
  which is why mine carries a sphere r 6 mm and a stalk cylinder at the origin that the reference
  does not.
- **Two of the three can be resolved and one cannot, yet.** `qBodyType(qCreatedBy(...),
  BodyType.MATE_CONNECTOR)` finds both connectors — the stud's `RzGH` and the destination `RdGD`.
  The stud's solid body comes back empty, because `combine parts` downstream has already merged it,
  and the query is evaluated at the end of the tree rather than where the transform sits.
- **The fix is to read the id where the feature runs**, which means rolling the tree back to that
  step. That is a write to the feature list whose route this draft has not established, and after
  the 500 that a guessed document-level route returned, it is not being guessed at.

**A transform is the feature a replay cannot carry across a GUI-made derive**, and it is worth
saying plainly: `u limb`'s `move fork` replayed and `l limb`'s `move ball stud` did not, so this is
not a rule about transforms but about which ids happen to regenerate. Every transform downstream of
a derive is suspect and is checked by the shape diff, which is what caught this one.

## `l limb` is right, and what the two remaining tabs need, 2026-09-18

**`l limb` is complete: 260 faces on 1 body, face for face with draft9p1p6.** `move ball stud` was
the one feature short, and the fix did not need the feature list:

- The three features after it — `combine parts`, `elbow end`, `wrist end` — were deleted, which put
  the stud's own body back in the model where the transform could see it.
- `qBodyType(qCreatedBy(...), BodyType.SOLID)` then answered `RzGD` and
  `BodyType.MATE_CONNECTOR` answered `RzGH` and `RdGD`, so all three of the transform's queries
  were repointed at ids this document actually issues.
- The stud's ball came to rest at z -48 mm, which is `#limbCenter` at the wrist, and the three
  deleted features were rebuilt in their own order.

**A mate connector is a body type, not an entity type.** `EntityType.MATE_CONNECTOR` is an invalid
enum access; the query is `qBodyType(..., BodyType.MATE_CONNECTOR)`.

### Five picks the parents' records cannot supply

`foot` and `gripper` both come from draft9p1p1, and both lose queries that no parameter can stand
in for. These are selections to be made against the geometry, not numbers to copy:

| Tab | Feature | What is missing |
| --- | ------- | --------------- |
| `foot` | `top round` | the edges to fillet, r `#top_round` |
| `foot` | `sole ribs` | the direction the eight grooves repeat along |
| `gripper` | `plane to cut top of clip` | the face the construction plane offsets from |
| `gripper` | `remove top of clip` | the split's target and its tool |

**The gripper is built and wrong in a way the picture shows and the numbers nearly hide.** It reads
32 faces against draft9p1p1's 33, but its socket collar is sunk into the clip where the reference's
stands proud with its four slits at full height and the cavity open at the top. 25 of its faces and
26 of the reference's fail to match, and 19 of that is the socket difference every draft9p1p1
comparison carries. The rest is the cut that never happened, because the plane it cuts on has no
reference and the split has no target.

**This is the *Model inspected* gate earning its place.** Face-for-face agreement on `body`,
`head`, `hinge`, both limbs and `ball and socket` was found by measurement; the gripper's fault was
found by holding the render beside
[`../../build-briefs/images/cad-gripper-iso.png`](../../build-briefs/images/cad-gripper-iso.png)
and seeing a collar that was not there.

## The four picks, made, 2026-09-18

**`foot` is complete: 60 faces on 1 body, and the 19 that differ from draft9p1p1 are the socket.**
Its own 41 faces match.

- **`top round` fillets four edges, not five.** The plate's top face is the plane at z -12 mm,
  area 3378.66 mm², and it is bounded by five edges: the heel arc r 16 mm, the toe arc r 24 mm, two
  straight sides, and the collar's own base circle at r 7.8 mm. The last is not a top edge and must
  not be rounded. The four chosen reproduce draft9p1p1's result exactly — two cylinders from the
  lines and two tori from the arcs, all r 8 mm.
- **`sole ribs` repeats along its own groove.** The foot's side edges are consumed by the fillet,
  so the direction is taken from the `groove profile` sketch's own `#rib_w` edge, which is the
  geometry the pattern's 2 × `#rib_w` step belongs to. It also needed `defaultScope`: a feature
  pattern of a Remove is refused a scope the same way a Remove is.
- **The foot passes task #215's check**, measured: the sole at z -24 mm is nine faces, eight groove
  floors stand at z -22 mm, and no face stands at z -20 mm.

**`gripper` is cut correctly now.** The brief settles it at
[`gripper.md:153`](../../build-briefs/gripper.md) — *a construction plane offset zero from the
socket's root, then Split part and delete the crown above it*.

- **`plane to cut top of clip` stands on the socket's root face**, `JaC`, the Ø15.6 mm disc at
  z -10 mm, which is `#collar` below the ball's centre. Offset zero, as the brief says.
- **`remove top of clip` takes the plane's face, not its first entity.** A construction plane
  creates a family of ten entities and the face is the one the split wants; given the family's
  first, the split ran and removed nothing.
- **The clip's top now sits at z -10 mm** with the collar standing proud, its four slits at full
  height and the cavity open at the top. Held beside
  [`../../build-briefs/images/cad-gripper-iso.png`](../../build-briefs/images/cad-gripper-iso.png)
  it is the same part; before the cut it was a block with the collar sunk into it.

**A trial loop left the wrong half kept.** `keepFront` was tried both ways to find which half the
split keeps, and the loop's last pass left `False` in the model — the dialog is not the only thing
that writes as you go. The clip came back six faces with its hook gone, and the next read was taken
as the tab's real state. Set back to `True`, which is what the parent carries.

## Phase B tab 10 — the `stickbot` assembly, 2026-09-18

**The robot stands, and nine of its thirteen joints resolve.** The assembly route is a different
endpoint family from `partstudios/features`, so it was built with that one still refused.

- **Fourteen instances, in draft9p1p1's own insertion order**, so the `<n>` its mates name line up
  index for index: `Torso`, `Head`, four `upper limb`, four `lower limb`, two `Gripper`, two `Foot`.
- **Thirteen mates replayed**, each with two things remapped: the `path`, which is the instance, and
  the `featureId`, which is the mate connector inside that instance's Part Studio. The parent's
  connector ids are matched to names through its own records, and the names to this document's ids
  through the tree — with the plan's rename table applied, since the parent calls them
  `neck connector` and this draft calls them `neck`.
- **Nine resolve: the neck, both shoulders, both hips, both elbows and both knees.** The figure
  hangs together, the head sits on the neck and the limbs articulate.

### The four that do not, and why

`left wrist`, `right wrist`, `left ankle` and `right ankle` all report *Mate cannot resolve mate
connectors*. The cause is not the mate and not staleness:

**`mate to robot` creates no mate connector at all, in either `foot` or `gripper`.**
`qBodyType(qCreatedBy(...), BodyType.MATE_CONNECTOR)` returns 0 for both, and 1 for `l limb`'s
`wrist end` beside them. Neither tab shows a warning; an inert connector looks exactly like a
working one in the tree.

**Their records carry no queries whatsoever.** Both are `originType` `ON_ENTITY` with
`entityInferenceType` `PART_ORIGIN`, and `originQuery`, `ownerPart`, `secondaryOriginQuery` and
`attachTo` are all empty — the same loss that cost the foot its fillet edges and the gripper its
cutting plane. Pointing all three queries at the tab's one body did not revive them, so what the
inference wants is a pick this draft has not yet worked out, not simply a body id.

**So the robot measures 300.0 mm against `make_plans`' `HEIGHT` of 318.0 mm.** The 18 mm is the two
feet: with the ankles unmated the legs end at their ball studs and the soles never reach the floor.
The height is a symptom of the four mates, not a separate fault.

**What is owed here:** author those two connectors — the foot's ankle and the gripper's wrist — so
each produces a connector at its part's origin, then remake the four mates and measure the height
again. The brief's acceptance is 317.00 mm and `make_plans` computes 318.0 mm; that 1 mm disagreement
is itself unresolved and belongs to whoever closes this check.

## Correcting the connector finding, 2026-09-18

**The earlier entry said `mate to robot` creates no mate connector, and measured it wrongly.**
It counted `qCreatedBy(makeId(featureId), EntityType.BODY)` filtered to `BodyType.MATE_CONNECTOR`,
which returns nothing for a connector however healthy. The lens that works is counting every
connector body in the tab, `qBodyType(qEverything(EntityType.BODY), BodyType.MATE_CONNECTOR)`, and
it checks out against tabs whose answer is known: `body` reports 9 for its 8 connectors plus the
one its derive brings, `l limb` 6, `u limb` 5.

**Re-measured properly, the conclusion stands and the evidence is now real.** `foot` and `gripper`
each hold exactly one connector body, and it is the one their derived socket brings across, not
`mate to robot`. Deleting that feature leaves the count at one; adding it back leaves it at one.

**Five formulations were tried and none made a connector**, each measured by the count before and
after:

- the part's body in `originQuery`, inference `PART_ORIGIN`, which is what the record asks for;
- the same with `ownerPart` set, and again with `attachTo` set as well;
- the default `Origin` entity, both of its ids, with inference `POINT`;
- the socket's cavity face with inference `CENTROID` and `attachmentOption` `TO_SELECTION` — which
  is exactly how `socket connect to robot` is built in `ball and socket`, where it works.

So the fault is not the query and not the inference as such. What is different about these two tabs
is that their one part is the *result* of a union whose surviving body is the derived socket's, and
that is the next thing to test rather than a sixth formulation.

**The assembly, as it stands:** thirteen mates, nine resolving — the neck, both shoulders, both
hips, both elbows, both knees — and four failing, both wrists and both ankles. The robot measures
300.0 mm against `make_plans`' `HEIGHT` of 318.0 mm, and the 18 mm is the two feet, which with the
ankles unmated never reach the floor.

**Assembly mate features cannot be deleted by the id `/features` reports.** A delete answers 200
once and 404 for the next, and a loop over a single listing leaves duplicates behind — this draft
made 26 mates out of 13 that way, twice. The reliable reset is to delete the assembly element and
recreate it, which is safe here only because `stickbot` is the last tab and the order survives. The
per-name delete in [`scripts/b_assembly.py`](scripts/b_assembly.py) should not be trusted until
that is understood.

## Looking at it said in one frame what six queries had not

**Mike's advice: hide what you are not working on and look at it off axis.** Done on `foot`, with
the planes hidden, it answered two questions at once.

**The foot is right.** Rounded plate, heel and toe arcs, eight tread notches along the sole, the
ankle socket standing proud with its slits — and a mate connector triad at the collar's centre.

**And opening `mate to robot` said exactly what is wrong with it**, which no amount of querying
around it had: the dialog reads *Origin entity: **Missing Item***, *Select owner entity: **Missing
Item***, *Attach to: **Missing Entity***, over the message *mate to robot [Mate connector] did not
regenerate properly: Cannot resolve entities. **3 missing selections***. The triad in the model is
the one the derived socket brings, not this feature's.

**So the union hypothesis is dropped.** It was a guess with no evidence and it was wrong to name it
as the next thing to test. The feature has three empty selections, in draft9p1p1's record and here,
and that is the whole of it.

**And the six REST formulations failed for a reason now obvious:** a body's id in `geometryIds` is
not what those three fields take. Every write was accepted and every field stayed empty, which is
why the count never moved.

**What is owed:** fill three selections on two features — `foot`'s and `gripper`'s `mate to
robot` — with entities that put the connector at the part's origin, which is the ball's centre, and
then remake the four mates. Two GUI attempts have not yet landed a pick: clicking the part's row in
the Parts list does not fill an armed selection field, and one click into the graphics area missed.
The next attempt should arm the field deliberately and pick a face whose own frame gives the part
origin under `PART_ORIGIN` inference.

**Not the cause, each ruled out by test rather than by argument:** stale connector ids — the mates
were rebuilt against ids read after the last change and failed the same way; the assembly's
instances — they insert and name correctly; and the mates themselves — the other nine resolve.

## The robot stands, 2026-09-18

**All thirteen mates resolve, and the figure measures 318.0 mm — `make_plans`' `HEIGHT` exactly,
to the millimetre.** Head, torso, both arms ending in grippers, both legs ending in feet on the
ground.

**Recovery point: version `the robot, all ten tabs`, `f4d70e962e78725ca6ad1758`.**

### What the three missing selections actually were

Mike's *hide what you are not working on and look at it off axis* is what found it. Opening
`mate to robot` showed Onshape's own words — *Cannot resolve entities. 3 missing selections* — and
the fields named themselves:

- **`foot`: all three empty.** Origin entity takes the **Origin's vertex**, picked from the tree,
  which puts the connector at the part's origin, and that is the ball's centre the ankle mates on.
  Owner and attachment take the part, picked from the Parts list.
- **`gripper`: one empty, and not the one expected.** Its owner already read `Gripper` and its
  attachment was already *To owner*, so it needed no third pick; its origin entity read
  *Missing Part of remove top of clip* — a reference to a part the split had replaced. The Origin's
  vertex fixed it.

Each feature's connector count went 1 to 2 the moment it was ticked, which is the measurement that
says it worked: the 1 was always the connector the derived socket brings.

**The height was a symptom the whole time.** 300.0 mm with the ankles unmated, 318.0 mm with the
feet on the floor; the 18 mm was never a separate fault.

### What this cost, and the lesson

Six REST formulations, two false hypotheses — staleness, then the union — and a wrong measurement
that reported a healthy connector as absent. Every one of them was an attempt to reason about the
feature from the outside. The dialog said what was wrong in one sentence, the first time it was
opened.

**A selection is not a parameter.** Writing a body's id into `originQuery` is accepted and does
nothing, because those fields take a picked entity. Where a parent's record carries an empty
selection, the pick has to be made, and the place to make it is the dialog.
