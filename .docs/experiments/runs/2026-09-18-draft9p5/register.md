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
ellipse's two diameters with the numbers the mouse landed on; `15.983648598194122*mm` and
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

- **`ball and socket` is whole and its parts are named.** The tab was resumed from index 6;
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

Every one is fully constrained and anchored by `COINCIDENT` to the joint's axis; 5, 1, 8, 6, 5, 3,
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

## Ring 3, what is measured and what is not

**Every printed part is one solid, and carries its name.** Measured on each tab: `body` `Torso`,
`head` `Head`, `foot` `Foot`, `gripper` `Gripper`, `u limb` `upper limb`, `l limb` `lower limb` —
one body and one part each. `ball and socket` and `hinge` hold two apiece and are scaffolding the
robot derives from rather than parts anyone prints.

**The assembly reads 14 instances and 13 mate features, none in error.** Seen in the tab itself:
every mate connector triad is placed, every mate row is clean, and the figure stands on its feet.

**Degrees of freedom: what Onshape reports here is per instance, not a number.** Each of the
fourteen carries the figure icon that marks an instance free to move, which is what a posable robot
should show. No total appears on screen, so no total is written down.

**The interference check has not been run, and the tool is not called *Interference* here.**
Onshape's *Search tools* answers *No items match your search* for that word in this assembly.
Rather than invent a name, this is left open: find what the tool is called by reading the assembly
toolbar, then run it.

**Still open in Ring 3:** every joint moved through its range, the interference check, and the
print files exported.

**Still owed on every tab:** Ring 1's feature read — the parameters compared one by one, every
`featureStates` entry, and `rollbackIndex` against the count — which waits on the `/features`
quota, about 19 hours out at this tick.

## Ring 2 acceptance on `body` and `head`, and two numbers that disagree

**`body` passes its stations exactly.** Five balls at Ø12.000 mm, and their centres measured off
the model: hips at `(±24, 0, -58)` mm and the neck at `(0, 0, 58)` mm, which is what
[`torso.md`](../../build-briefs/torso.md) asks for. The shoulders sit at
`(±49.551, -7.824, 19.235)` mm.

**Its 72 × 48 × 96 check cannot be taken as it stands.** The brief wants that box *before the studs
are added*, and the finished tab measures 111.102 × 48.000 × 128.000 mm with them on. Taking it
needs the tree rolled back to before `copy ball stud`.

### The head's socket sits 46 mm down, not 45, and the model is right

`head.md` calls the socket centre 45.000 mm below the head centre *the one number the assembly
needs*. This draft measures **46.0 mm**, and draft9p1p1 measures **45.0 mm**, so the difference is
real and it is one millimetre.

**It is the collar, and it is the settled design.** draft9p1p1's socket root face stands at
z -9.0 mm with an area of 254.469 mm²; draft9p1p6's — the one this draft builds and derives — stands
at z -10.0 mm with an area of 191.1345 mm². `make_plans` has `COLLAR_L` equal to `STAND` at 10 mm,
which is the ruling that *a socket reaches back from the ball's centre exactly as far as a stud
stands its ball clear of its own face*. The head's underside is at z -36 mm and the socket hangs
`#collar` below it, so 46 mm follows.

**So the brief's 45.000 is stale, not the model.** It was written against the 9 mm collar. The
number belongs to `head.md`, which this draft does not own, so it is named here and not edited.

### The head is 63 mm deep and the design source says 60

Both this draft and draft9p1p1 measure 63.000 mm fore and aft; `make_plans` computes `HEAD_D` as
`TORSO_D * 5 / 4` = 60, and `head.md` asks for *60.000 deep*. Two drafts of the model disagree with
the design source by 3 mm, and nothing in this run's records says which was intended.

**This one is not settled here.** Unlike the socket, no ruling explains the 3 mm, so it is a
question for Mike rather than a call this draft makes: either the head was built deeper than the
number that names it, or `HEAD_D` no longer describes the head.

## Ring 2 acceptance on `foot` and `gripper`

**`foot` passes every number its brief can be held to.** Length 96.000 mm and width 48.000 mm off
the bounding box; the ground at z -24.000 mm and the ankle ball's centre on the origin, so the
ankle height is 24.000 mm; the heel and toe arcs read r 16 mm and r 24 mm, which are `#heel_r` and
`#toe_r`; the collar is r 7.8 mm and the two fillet cylinders are r 8 mm, which is `#top_round`.
Volume 38013.328 mm³.

**`gripper` passes its four measured numbers.** Clip bore Ø3.300 mm and outer Ø10.000 mm, read off
the two cylinders at r 1.65 mm and r 5.0 mm; the top is a flat square 18.000 mm both ways; and the
gripper is 24.000 mm from the wrist centre — the ball's centre, on the origin — to its lowest
point. Volume 4363.829 mm³.

### Two more brief numbers that the settled joint has moved past

Both are the same shape of thing as the head's 45 mm, and both are named rather than edited,
because the briefs are not this draft's to change.

- **`foot.md` asks for a socket mouth of Ø11.520 mm; the joint gives Ø11.320 mm.** 11.520 is
  `0.96 × #ball` exactly, and `#mouth` is `0.96 × #ball - 2 × #ballLoss`, which is 11.320. The
  brief's figure is the mouth before the printed ball's loss was taken off it.
- **`gripper.md` calls it *the Ø18 collar*; the collar is Ø15.600 mm**, which is `2 × #collar_r`.
  The 18.000 mm in that sentence is the clip's square top, which this tab measures exactly, so the
  number is right and the thing it is attached to is not.

**So three of the briefs' numbers trail the model and one does not.** The head's 45 mm, the foot's
Ø11.520 mm and the gripper's *Ø18 collar* each follow from a ruling settled after the brief was
written. The head's 60 mm depth does not: nothing explains why two drafts measure 63 mm, and that
one stays a question.

## Ring 2 acceptance on `hinge` and the two limbs

**The hinge's step is 15.0°, measured.** Each body carries 96 cone faces — four to a wedge — so the
blade and the fork each hold 24 wedges and the step is 360/24. That is
[`hinge.md`](../../build-briefs/hinge.md) § *What it should measure when it is right*'s **15°**.

**The rest of that section is mechanical, not geometric**, and the brief says so itself: pinch
force, leaf stress, detent hold, twist-off. It also says to use
[`hinge_spring.py`](../../../../src/stickbot/hinge_spring.py) rather than re-derive them with a
formula, so they are not this draft's to measure off the model and are not claimed here.

**Both limbs measure exactly 24.000 mm across, and nothing lies outside it.** `u limb` runs
`(-10.4494, -12, -60)` to `(10.4494, 12, 2.2205)` mm and `l limb` `(-10.4494, -12, -54)` to
`(10.4494, 12, 12)` mm. The ±12 mm is `#limbD / 2` and the ±10.4494 mm is `#flat`, which
`make_plans` computes as `sqrt((#limbD / 2)² - (#seat / 2)²)` — the two faces the fork is cut on.
[`limbs.md`](../../build-briefs/limbs.md) asks for it in exactly those words: *nothing anywhere
lies outside Ø24*.

## `ball and socket`'s acceptance list, finished

The three checks left open when `massproperties` was first asked without
`?massAsGroup=false` are now taken, and each matches
[`ball-and-socket.md`](../../build-briefs/ball-and-socket.md) exactly.

- **Cavity volume 717.14 mm³.** A full sphere at the measured cavity radius of 6.08 mm is
  941.455 mm³, and the cap standing above the rim at `#grip` is 224.314 mm³.
- **The slits are 6.2205 mm deep and leave a 6.0 mm floor**, read off the model rather than
  computed: the socket's horizontal planes stand at z 2.2205 mm (the rim), z -4.0 mm (the slit
  floors) and z -10.0 mm (the root). Rim to floor is 6.2205 mm, which is `#grip + #ball / 3`, and
  floor to root is 6.0 mm.
- **`Ball stud`'s volume is unchanged by the slits**, which the face count settles: the stud holds
  three faces — one sphere, one cylinder, one plane — and no slit cut any of them. Volumes measured
  1028.9682 mm³ for `Ball stud` and 1535.8824 mm³ for `Socket body`.

**`massproperties` answers per body only with `?massAsGroup=false`.** Asked without it, and asked
with `partId` repeated, it returns a single `-all-` entry, which is what made the first pass report
the stud's volume as missing.

**So every Part Studio has now had its brief's measurable acceptance numbers taken**, and they
pass. What the briefs ask for that this draft has not taken is named where it belongs: the torso's
box before the studs, which needs a rollback; the hinge's mechanical figures, which its own brief
sends to `hinge_spring.py`; and the thinnest-wall checks, which nothing here has measured.

## The interference check has no tool in this assembly

The assembly's toolbar was read rather than searched: fifty controls carry a title, and they are
insert, the mate connector, the nine mates, group, snap mode, show mates, replicate, replace
instance, the three assembly patterns, four relations, display states, Part Studio in context, and
six loads. **None of them is an interference check**, which is consistent with *Search tools*
answering *No items match your search* for the word.

So Ring 3's *nothing interferes at rest* cannot be taken the way the plan assumes, and this draft
does not know where that check lives — or whether this account's plan carries it. It stays open,
and the next step is to ask Mike rather than to hunt further.

## The account is an education subscription, and that closes an open question

The document header carries the tooltip **"This document was created by an education subscriber."**

[`2026-09-14-move-to-stick-e-bot.md`](../../../2026-09-14-move-to-stick-e-bot.md) § *What we do not
know yet* asks exactly this: *which Onshape plan this account is on. If it is an Education or team
license rather than Free, then no draft has ever been built under the constraint students face, and
`before-you-start.rst` describes a plan nobody here has used.*

**It reads on the document, not on the account**, so it says what created this document rather than
what the account is today; and it does not say what a student's own account would be. But it is the
first evidence either way, and it points at the answer the question feared: the drafts have been
built under an education subscription.

**This is not draft9p5's to act on.** It is recorded here and belongs to whoever closes that
question, along with the second half of it — what a free plan actually allows.

## The section, held beside `brief-socket.svg`

**Sheet used: [`brief-socket.svg`](../../build-briefs/images/brief-socket.svg), *THE SOCKET, IN
SECTION, IN A LIMB*.** The section was cut on the Front plane at version `the robot, all ten tabs`
and looked at along that plane's normal with `Shift+1`, which is the procedure
[`onshape-gui-howto.md`](../../../onshape-gui-howto.md) § *Section: the GUI does it and
`shadedviews` does not* sets out. It also says why there is no other way: `cutPlane` and
`sectionPlane` were both passed to `shadedviews` and the image came back byte for byte identical,
so Onshape ignores them.

**What the section shows:** the ball with its stalk rising out of it, seated in the socket's
cavity, the collar hatched below it and the fingers standing either side of the mouth.

**What was compared on the sheet, and it is the same part.** The sheet draws the socket's outline
as `-7.8,-10` up to `2.22054`, in to `5.66`, an arc of `6.08`, out to `7.8` and down to `-10`.
Every one of those is a number this draft measured off the model: root at z -10 mm, rim at
z 2.2205 mm, mouth half-width 5.66 mm, cavity radius 6.08 mm, collar radius 7.8 mm. Its dimensions
read ball Ø12, mouth Ø11.320, cavity Ø12.16, wall 1.8, collar Ø15.6, grip 2.22054 and the four
slits 1.6 mm wide running 6.2205 mm down — and each matches.

**The sheet also settles the foot brief's odd number.** `brief-socket.svg` says **mouth Ø11.320
mm**, which is what the model measures; `foot.md`'s prose asks for Ø11.520. So the design source's
own drawing agrees with the model, and it is that one sentence of prose that trails.

**An SVG sheet is read, not rendered.** Its text carries the geometry and every dimension, which is
a more exact comparison than looking at a picture of it, and it needs no conversion step.

## The other three sheets, compared as numbers

**`brief-fork.svg`, *THE FORK, SEEN DOWN THE LIMB*.** Its `20.8988 mm across the flats` is measured
on the model: `u limb`'s two flats stand at x ±10.4494 mm, so 20.8988 mm across, and that is
`2 × #flat`. Its `Ø24 mm` is the limb, measured 24.000 mm. Its `fork prong 6.1 mm`, `gap 0.9 mm`,
`blade 10 mm` and `fork span 24 mm` are `EAR`, `GAP`, `BLADE` and `LIMB`, and each matches.

**`brief-detent.svg`, *THE WEDGE*.** `proud 0.75 mm`, `clearance 0.15 mm` and `gap 0.9 mm` are
`WEDGE_H`, `WEDGE_C` and `GAP`, and each matches. The rest of that sheet — the wedge 4.4494 mm
long, the crest 2.2217 mm, pitch 2.5393 mm, climb 0.6 mm — is `hinge_spring.py`'s geometry, which
the hinge's brief says to take from that file rather than re-derive.

**`brief-roots.svg`, *WHERE EACH ROD ROOTS*.** `fork free 21 mm` is `EAR_FREE` and `blade free
20 mm` is `TAB_FREE`, and its claim that both sides reach `pin to rod end 38 mm` holds:
`TAB_FREE + ROD_BLADE` is 38.0 and `EAR_FREE + ROD_FORK` is 38.0.

**What this is and is not.** The numbers on all four sheets have now been compared against the
model and the design source, and they agree. A section *picture* has been taken for `ball and
socket` only. `hinge`, `u limb` and `l limb` still owe theirs, and the technique for taking one is
settled: section on the plane at a version, look along its normal, do not zoom to fit.

**A sheet is more exact read than rendered.** Its text carries the geometry path and every
dimension, so the comparison is number against number rather than eye against picture — and a
number is what a shape diff can be held to.

## The other three sections, taken

All four tabs that have a sheet have now been sectioned at version `the robot, all ten tabs`, by
the howto's procedure: section on the plane, look along its normal, no zoom to fit.

- **`hinge`, cut on Top and seen down the limb** — which is what
  [`brief-fork.svg`](../../build-briefs/images/brief-fork.svg) draws, *THE FORK, SEEN DOWN THE
  LIMB*. The section shows the Ø24 circle cut flat top and bottom where the flats are, the fork's
  two prongs hatched either side, the blade between them and the axle bore on the centre. The
  flats are the sheet's `20.8988 mm across the flats`, measured on the model at x ±10.4494 mm.
- **`l limb`, cut on Front** — the blade at one end with its axle bore, the rod hatched along the
  middle, the ball stud at the other end. That is
  [`brief-roots.svg`](../../build-briefs/images/brief-roots.svg)'s subject, *WHERE EACH ROD ROOTS*:
  `blade free 20 mm` then `blade rod 18 mm`, reaching the 38 mm the sheet gives both sides.
- **`u limb`, cut on Front**, for [`brief-detent.svg`](../../build-briefs/images/brief-detent.svg).
  That sheet is a detail of one wedge rather than a section of the limb, so the section stands
  beside it as the part the wedge sits on rather than as the same drawing.

**So Ring 2's sheet comparison is done on all four**, numbers and picture both, and what each
comparison rests on is written down rather than asserted.

## The construction, scored against the rulings

[`scripts/c_score.py`](scripts/c_score.py) reads each tab's own tree rows — what the GUI shows a
student — and counts the three things a row can answer. **Every tab passes, and the counts are the
ones the build order says they should be.**

| Tab | Geometry | Variables | Titles typed over | Default names | Names saying *connector* |
| --- | -------: | --------: | ----------------: | ------------: | -----------------------: |
| `ball and socket` | 9 | 5 | 0 | 0 | 0 |
| `hinge` | 28 | 16 | 0 | 0 | 0 |
| `body` | 25 | 8 | 0 | 0 | 0 |
| `head` | 14 | 12 | 0 | 0 | 0 |
| `foot` | 11 | 13 | 0 | 0 | 0 |
| `u limb` | 9 | 0 | 0 | 0 | 0 |
| `l limb` | 9 | 0 | 0 | 0 | 0 |
| `gripper` | 7 | 8 | 0 | 0 | 0 |

**Against the plan's own survey of the parents**, which counted five typed titles on `ball and
socket`, eight on `hinge`, and ten connector names still carrying the word — eight on `body` and
two on `hinge` — all three are now nil.

**`hinge` holds 16 variables where its parent holds 18**, which is `#ear` and `#backlash` dropped
because nothing reads either, and the walk that found that is
[`results/variable-first-reader.md`](results/variable-first-reader.md).

**What a row cannot answer, and where its answer is.** That each variable sits immediately above
its first reader is true by construction: the order came from that same walk and
[`results/build-order.json`](results/build-order.json) is what the builder writes from. That each
sketch stands on a face or has a reason is
[`results/sketch-planes.md`](results/sketch-planes.md) and
[`results/sketch-moves.md`](results/sketch-moves.md), and one sketch was moved — `blade wedge
outline`, onto the blade's own face, with `#blade / 2` dropped from its extrude. That `relief slit`
is the last feature on the blade is the brief's step order, which the build order is derived from.

## Each tab held beside its parent's frame

The *Model inspected* gate asks for the part the new one was built from, rendered in the same
views, and the two put side by side. The briefs' `cad-*-iso.png` frames are those renders of the
parents, so each tab's isometric is held against its own.

- **`ball and socket`** — same stalk, same ball seated in the same mouth, same four slits in the
  same places.
- **`hinge`** — same fork and blade, same relief slit, same axle bore on the fork's side.
- **`gripper`** — after the cut was fixed: same slab, same collar standing proud with its four
  slits at full height and the cavity open. Before the fix this was the comparison that showed the
  fault, when 32 faces against 33 had nearly hidden it.
- **`body`** — same block, same neck stud, same shoulder boss and its ball, same hip ball, and the
  same flush-cut scar where the boss was trimmed at the top face.
- **`head`** — same rounded box, the same two elliptical eyes and slot mouth, same arch rounds,
  same chamfer.

**Still to hold beside their frames: `foot`, `u limb` and `l limb`.** All three are rendered. The
foot has been looked at off axis with the planes hidden, and both limbs have been sectioned, so
none is unexamined — but none has yet been put beside its parent's frame, which is the part of the
gate that catches what a single render cannot.

## All eight tabs are now held beside their parents' frames

The three that were outstanding are done, and each matches.

- **`foot`** — same plate with its heel and toe arcs, same top round, same ankle socket standing
  with its slits and open cavity, same eight tread notches along the sole's edge.
- **`u limb`** — socket at the top with its slits, rod below, fork at the far end with the
  twenty-four wedge ring and the axle bore through both prongs.
- **`l limb`** — blade at the top with its wedge ring and stub axle, rod below, ball stud at the
  far end.

**So the *Model inspected* gate's harder half is satisfied for every Part Studio**: the part this
draft built and the part it was built from, rendered in the same view and put side by side. It is
the comparison that found the gripper's sunken collar when a face count of 32 against 33 had
nearly hidden it, and it is the reason to take it on the tabs that agree as well as the one that
did not.

## Every feature accounted for, by what it made

[`scripts/c_feature_effect.py`](scripts/c_feature_effect.py) asks the model what each feature is
responsible for — `qCreatedBy` over its id, counting faces and bodies — across all eight tabs. The
answers are [`results/feature-effect.json`](results/feature-effect.json).

**Sixty-three features build geometry and every one of them made some.** `ball and socket` 6,
`hinge` 24, `body` 12, `head` 10, `foot` 9, each limb 4, `gripper` 4.

**One feature makes nothing and should:** `trim shoulder cut`. It is silent because it cuts the
shoulder boss flush with the torso's top face rather than leaving a new face behind, which
[`torso.md`](../../build-briefs/torso.md) asks for in those words — *the shoulder boss is cut flush
at z = +48 and nothing stands proud of the top face* — and the tree says nothing about it either.

**The rest of the silence is by kind, not by fault.** A boolean rewrites bodies and a transform
moves one, so neither is credited with a face; variables, mate connectors and planes make no
geometry at all. Counting those as failures is what made an earlier pass report
`combine fork parts` and `move ball stud` as broken when only the second one was.

**What this is worth.** It is the half of *Model inspected* that a picture cannot give: a render
shows the part, and this shows that no feature in the tree is sitting there doing nothing. Held
with the face-for-face diffs against the parents, every feature is both present and effective.

## The ball joint's swing, from the model's own geometry

Every input is measured on this draft: the stalk Ø6.000 mm, the cavity sphere r 6.080 mm and the
rim at z 2.2205 mm. Put through `make_plans`' derivation — `acos(stalk/2 / cavity) − asin(grip /
cavity)` — the joint this model builds allows **39.0132° per side**, which is `BALL_SWING` exactly
and the ±39.013° [`assembly.md`](../../build-briefs/assembly.md) states, so 78.0° of cone.

**This is the geometry's limit, not a posed measurement, and the brief asks for the posed one.**
*Every ball joint's actual swing, measured by posing it until it stops* means driving the mate to
its stop in the assembly, which this draft has not done. What is established is that the socket and
stalk it built leave room for the swing the design derives; whether the ball mate reaches it is the
brief's own follow-up question and is still open.

**The neck is excluded on the brief's own instruction.** It says the head's underside binds on the
torso's top face well inside the joint, so that angle is measured rather than assumed from the
socket — and it has not been measured here.

**The hinge's range is its 15° step**, which is measured: 96 cone faces on each body, four to a
wedge, twenty-four wedges, 360/24.

## The print files export, and each one is a whole part

**All six printed parts export as binary STL**, and each file is well formed: its header's triangle
count times fifty, plus the eighty-four byte preamble, is exactly the file's length.

| Part | Triangles | Bytes |
| ---- | --------: | ----: |
| `Torso` | 23038 | 1151984 |
| `Head` | 7682 | 384184 |
| `Foot` | 6822 | 341184 |
| `lower limb` | 6770 | 338584 |
| `upper limb` | 6306 | 315384 |
| `Gripper` | 4110 | 205584 |

**The export needed a client the rest of this draft does not use.** `/stl` answers with a redirect
to another host, and every other call here is a `fetch` from inside the Onshape page, which is
same-origin: it dies with *Failed to fetch* and says nothing about why. Playwright's own request
context carries the browser's cookies, follows the redirect and is not bound by CORS, so it fetches
what the page cannot.

**Each part being one solid was already measured** on the tabs themselves — one body and one part
each — so what the export adds is that the file comes out and comes out whole.

**The files are not committed.** The *Capture is out* gate refuses a tracked binary outside
`instructions/*/source/images/`, and a print file is not a figure; they are written to the session
scratchpad, which is where a thing built to find something out belongs.

## Interference at rest, as far as a box test can settle it

With no interference tool in this assembly, the pairs were tested by geometry instead: each
instance's Part Studio bounding box, carried through that instance's own transform, and every pair
of the resulting boxes checked for overlap.

**Of 91 pairs, 76 are proved clear.** Their boxes do not touch, so those parts cannot interfere
whatever their shape. That is a one-way proof and it is the strong direction.

**Fifteen pairs overlap, and thirteen of them are the joints.** Each foot with its lower limb, each
gripper with its lower limb, the head with the torso, and each lower limb with its upper limb —
parts that mate are supposed to meet.

**The other two are `Torso <1>` with each arm's `lower limb`**, and they are exactly the pair
[`assembly.md`](../../build-briefs/assembly.md) says to watch: *the shoulder interferes again, and
this check is now the interesting one* — the arm first crosses the body at 33.38° while the joint
now opens to 41.76°, *so the margin is gone and what stops the arm is the torso rather than the
socket*.

**What this test cannot do.** An overlapping box does not mean the solids touch, and these boxes
are axis-aligned, so an arm hanging beside the torso overlaps it in a box while standing clear in
fact. The brief's instruction for those two is to *drive the shoulder to its stop, run
interference* — both of which need the posing and the tool this draft does not have. So the two
pairs are named, not judged.

# Ring 4 — the record

## What was built

**One document, `stickbot-draft9p5`, holding ten tabs built from empty.** `robot sizes` carries the
23 rows the build plan's Variables table asks for and nothing else. Eight Part Studios build the
robot's parts, and the `stickbot` assembly holds fourteen instances on thirteen mates.

**Six tabs came out face for face with their parents**: `ball and socket` 22 faces, `hinge` 510,
`body` 20, `u limb` 270, `l limb` 260, `foot` 60. `head` differs from draft9p1p1 by 19 faces and
those 19 are the socket, which is the plan's intent — the settled draft9p1p6 joint everywhere.
`gripper` differs by its socket the same way.

**The robot stands at 318.0 mm**, which is `make_plans`' `HEIGHT` to the millimetre.

## What each ring caught

**Ring 1 caught nothing on the tabs it ran on, and is owed on all ten.** It ran per feature on
`ball and socket` until the `/features` quota went on 2026-09-18; since then every tab has been
written with the feature read deferred. What stood in for it — the shape diff against the parent —
caught three defects the writes themselves reported as fine.

**Ring 2 caught five things.** The hinge's missing wedge ring, 29 faces against 510, from a pattern
naming its features in `featureIds` where the remap only rewrote `featureId`. The gripper's collar
sunk into its clip, which 32 faces against 33 had nearly hidden and the render beside the brief's
frame showed at once. `l limb`'s ball stud left at the origin by a transform whose three queries
named the parent's ids. The five typed variable titles a verbatim replay carried in. And the
`foot`'s whole lower half failing silently for want of a merge scope.

**Ring 3 caught the four mates that could not resolve**, which were two mate connectors with three
empty selections between them — and it caught them as a height: 300.0 mm against 318.0 mm, the
18 mm being two feet that never reached the floor.

**Ring 4 is this file.**

## What was skipped, and why

- **Ring 1's feature read on every tab.** The `/features` GET has answered 429 since 2026-09-18
  with a quota that does not clear until about 16:17 on 2026-09-19; the last probe read
  `retry-after: 20157` with `x-rate-limit-remaining: 0`. Writes to the same route kept working,
  which is why the CAD exists at all. `diff_features.py` waits on the same route.
- **The thinnest wall where the closest approach falls on a face's edge.**
  [`scripts/c_thinnest_wall.py`](scripts/c_thinnest_wall.py) answers every pair whose surfaces
  face each other, and refuses the rest rather than reporting a number it cannot stand behind.
  `evDistance` is the instrument for those, and `featurescript` shares the feature route's quota.
- **Driving the joints in the assembly.** Two of the questions that asked for it are answered from
  the geometry instead, and both are recorded above: the neck reaches the torso at 45.240° nodding
  and 36.870° sideways, and the shoulder's arm fouls at 33.2722°. **Neither was posed.** Onshape
  reports degrees of freedom per instance here rather than as a total, so no total is written down.
- ~~**The interference check.**~~ **Run on 2026-09-19: `No interferences`,
  with all fourteen instances selected.** It is not a toolbar tool, which is why the toolbar and
  *Search tools* both came up empty; it opens from **Show analysis tools** at the bottom right of
  the graphics area. Onshape's own help said so and I had not read it.

## The two gates the declaration claims

**Model inspected.** Every tab rendered and held beside its parent's own frame from the briefs;
`ball and socket`, `hinge`, `u limb` and `l limb` sectioned at a version against their sheets;
every feature accounted for by the faces and bodies it made; and every brief's measurable
acceptance number taken. The evidence is [`results/`](results/) and the sections named above.

**Recovery point.** The document's versions, in order:

| Published | Name | Id |
| --------- | ---- | -- |
| 2026-09-18T20:04:05 | `Start` | `68a3591a2d407ead830d8bdf` |
| 2026-09-18T20:26:02 | `tab 1 - robot sizes` | `9d4f31e4d33a22c3d9a62fec` |
| 2026-09-18T20:37:21 | `tab 2 - ball and socket` | `b0316a744f2ab1a752520744` |
| 2026-09-19T00:45:37 | `the robot, all ten tabs` | `f4d70e962e78725ca6ad1758` |
| 2026-09-19T13:10:56 | `before the gripper wall fix` | `77d651aa4e43e369c93abb9b` |
| 2026-09-19T13:14:09 | `gripper reads the studio's wall` | `4102df8544b8b185f6eb07c7` |

**The one to start from is `gripper reads the studio's wall`.** `the robot, all ten tabs` holds the
gripper with its 18.000 mm clip body, which is the defect § *Fixed: the `gripper` tab no longer
declares* records; the two versions after it bracket that change so either side can be reached.

**The per-tab versions Ring 2 asks for were not published past tab 2**, and the checklist says so
on each line. A version in Onshape is document-wide, so one published now and named for a single
tab would hold all ten and say it held one.

## What the briefs and the design source owe

**Written when four numbers were outstanding; all four are closed and the briefs carry the
corrections.** `head.md`'s socket centre, `foot.md`'s mouth, `gripper.md`'s collar and the head's
apparent 63 mm depth are each settled in § *The design's defects, in one place*, which is the list
to read. The head's depth was never a disagreement: it was a bounding box read as a dimension, and
the 3 mm is the eyes standing proud.

**What is actually owed now** is two things, both in that list's *Open* section and neither of them
a number: the collar's radius being computed again in each tab rather than taken off the socket's
own geometry, and the arms reaching 13.875 mm past mid-thigh where `assembly.md` reasons they
should reach it exactly.

## Ring 3, measured on the assembly: the feet touch

**The feet are symmetric and on their legs.** Their centres sit at x +24.0 mm and -24.0 mm, which
is `FOOT_X` equal to `LEG_X`, exactly as [`assembly.md`](../../build-briefs/assembly.md) says.

**But they touch.** Each foot spans 48.000 mm across — `FOOT_W`, which is `2 × FOOT_H` and what
[`foot.md`](../../build-briefs/foot.md) asks for and this draft measures — so a foot centred on
x 24 runs from x 0 to x 48. The two inner edges meet at x 0.000 and the gap is **0.000 mm**.

`assembly.md` expects *the feet do not touch, and the gap is 16*, with *their inner edges land on
x ±8*. That needs a foot 32 mm across at those centres. **The two briefs disagree with each
other**: `foot.md`'s 48 mm foot centred on its own leg at ±24 cannot leave a 16 mm gap, and the
model follows `foot.md`.

**The brief's reasoning for 16 does not survive either.** It calls it *the half-size robot's 4 mm
doubled*, but a foot whose width is `2 × FOOT_H` scales with the robot, so the gap it leaves scales
to zero, not to 16: at half size the centres are ±12 and the foot is 24 across, which also meets at
x 0.

**Fixed in `assembly.md` on 2026-09-19, on Mike's word.** It was written up here as a design
decision needing his call, and the reading was wrong: every other source already says the feet
touch. [`../../../robot-build-plan.md`](../../../robot-build-plan.md) line 141 says **The feet are
not handed, and they are allowed to touch**, and gives the reason; `make_plans.py` sets
`FOOT_X = LEG_X` under the comment *the sole is centered on its own leg, so the two feet meet at
x 0 when the legs hang straight*; `foot.md` line 154 closes the question with **They do, and that
is the decision rather than a coincidence**; and `assembly.md`'s own bullet above the broken one
says the source gave the 8 mm outboard offset up on 2026-08-26. One acceptance check survived that
withdrawal and nothing else did. The bullet now reads **The feet touch, and the gap is 0 mm**, and
keeps the measurement as the check that a foot is on its own leg.

## The arms reach past mid-thigh

The gripper's lowest point sits at z -204.765 mm. The thigh — `upper limb <3>` — spans
z -222.0 mm to -159.779 mm, so its middle is z -190.9 mm. **The arms reach about 14 mm below
mid-thigh**, not to it.

## The three symmetry checks, and one of them nearly reported a phantom

Three briefs ask for symmetry and each says to check rather than assume:
[`torso.md`](../../build-briefs/torso.md) about the YZ plane,
[`foot.md`](../../build-briefs/foot.md) about the foot's own fore-and-aft centreline, and
[`gripper.md`](../../build-briefs/gripper.md) about the clip's left-right centreline. For these
parts all three are the plane x = 0.

**All three are symmetric.** Every face has its mirror: `body` 20 of 20, `foot` 60 of 60, `gripper`
30 of 30, matched on surface kind, area, radius and the mirrored centre of the face's own box.

**The first run of the check reported the body as unsymmetric, and it was the check that was
wrong.** Four faces came back unmatched — the two shoulder cylinders and the two side planes. Their
boxes mirror exactly, `-51.1665..-36.0` against `36.0..51.1665` and planes at x ∓36.0; what
differed was the area's last digit, 717.7415 against 717.7416 and 4287.9092 against 4287.9091.
Rounding the area to four places made a mesher's rounding look like an asymmetry.

**So the tolerance is part of the measurement.** A check tight enough to see the last digit of an
area will find a difference in every mirrored pair, and reporting that as a defect is how a sound
model gets called broken.

## A batch of per-tab numbers, taken from the records

**`body`: the shoulder boss is cut flush and nothing stands proud.** The part has exactly two
horizontal faces, at z -48.0 mm and z +48.0 mm, so nothing rises above the top. That top face
measures 3513.459 mm² where a plain 72 × 48 rectangle is 3456 mm², and the 57.46 mm² difference is
the two elliptical scars the cut leaves — which [`torso.md`](../../build-briefs/torso.md) says to
expect.

**`foot`: the ankle socket has its relief slits and the boss stands right.** Eight slit walls —
four slits — and the boss stands `#grip + #plate` = 14.2205 mm proud of the plate's top, which is
the brief's figure exactly. Its horizontal planes read z -24.0 (nine, the grooved sole), -22.0
(eight groove floors), -12.0 (the plate top), -4.0 (four slit floors) and 2.2205 (four rim arcs).

**`gripper`: the clip's bore axis is parallel to X**, read off the model as `(-1, 0, 0)`, and its
three cylinders are r 1.65, r 5.0 and r 7.8 mm.

**`head`: the rim is four arcs, and the cavity sits 2.2205 mm above it.** Four faces stand at
z -48.2205 mm, which is the rim broken by the slits — the check
[`head.md`](../../build-briefs/head.md) says proves the slits actually opened the mouth — and the
cavity's centre at z -46.0 mm is 2.2205 mm above that, *above and not below*, which is the other
check it asks for.

**My first reading of the head was wrong and the model was not.** I took the rim as the highest
horizontal plane and got nonsense — a collar 35 mm proud and a cavity 33 mm below its rim. The
head's socket points **downward**, so its rim is the lowest face, not the highest. Read that way
every number falls out.

**Two more head numbers move with the collar, like the socket centre before them.** The collar
stands 12.2205 mm proud where `head.md` says 10.947, and the slits are 6.2205 mm deep where it says
4.947. Both are `#collar` at 10 mm and `#grip` at 2.2205 against draft9p1p1's 9 mm and 1.947;
the same one ruling, showing up in a third and fourth place.

## The socket's wall is 1.72 mm, measured, in all four tabs that carry one

A wall between two curved faces that share a centre or an axis is their radius gap, and that is a
measurement rather than an estimate.

| Tab | Wall | Between |
| --- | ---: | ------- |
| `ball and socket` | **1.72 mm** | the collar's outside to the cavity |
| `head` | **1.72 mm** | the same pair, in the socket it derives |
| `foot` | **1.72 mm** | the same |
| `gripper` | **1.72 mm** | the same |

That is the figure [`ball-and-socket.md`](../../build-briefs/ball-and-socket.md) gives — *the
thinnest wall in the socket is 1.72 mm, from the collar's outside to the cavity*. The same tab
yields two design numbers as a by-product: the cavity sphere to the ball is **0.08 mm**, which is
`#fit`, and the collar's outside to the ball is **1.8 mm**, which is `#wall`.

**What this does not answer.** The briefs ask for *the thinnest wall anywhere in the part*, and a
wall between faces that are neither concentric nor coaxial is not a radius gap; finding it needs
`evDistance` over `featurescript`. So this is the thinnest wall of the kind a face dump can measure
exactly, and the general question is still open on all four.

## `measure_walls.py` cannot read today's `bodydetails`

The repo already has a tool for this and it finds nothing. It filters surfaces on `CYLINDER` and
`SPHERE` where the route now answers `cylinder` and `sphere`, and it reads each vector as an
`{x, y, z}` map where the route now answers a list. On every tab it prints *pairs found: 0* and
then raises on the minimum of an empty sequence.

**Mike said to fix it, so it is fixed.** `vec` now reads a point either way it is spelled, the
surface filter compares on case, and a dump with no pair says so instead of raising on the minimum
of an empty sequence. Two fields had moved under the tool and it had not moved with them.

**It reports the briefs' own numbers now.** On `ball and socket` it finds the cavity sphere against
the ball, **0.0800 mm**, which is `#fit`. On `gripper` it finds the clip's bore against its outside,
**3.3500 mm** — and [`gripper.md`](../../build-briefs/gripper.md) names that figure in as many
words, *not the clip wall: 3.35 is the thickest thing in the part*. `head` and `foot` hold no
coaxial or concentric pair at all, and it now says that rather than failing.

**What it still does not do is find the socket's 1.72 mm**, because that wall lies between a
cylinder and a sphere whose axes meet rather than between two faces sharing an origin and an axis.
That is the tool's stated scope, not a defect, and
[`scripts/c_walls.py`](scripts/c_walls.py) measures the wider case for this run.

## Ring 2's acceptance, taken off the face dump while `/features` was refused

2026-09-19. `features` GET answered `retry-after: 29124` with `x-rate-limit-remaining: 0`, and
`featurescript` `29020`, so both reset about 16:15 that afternoon. `parts`, `bodydetails`,
`boundingboxes`, `sketches`, `assemblies` and `documents` all answered throughout.

[`scripts/c_accept_faces.py`](scripts/c_accept_faces.py) takes every acceptance number a face dump
can reach: a sphere's centre and radius, a cylinder's axis, a planar face's position, and an arc's
radius from three points on it. It reads both shapes the route answers in; the per-part path gives
`PLANE` with `{x, y, z}` maps where the element path gave `plane` with lists, which is the split
`measure_walls.py` was fixed for and here they turned up in one session.

**What passed, and what differs.**

| Tab | Check | Measured | The brief asks |
| --- | ----- | -------: | -------------: |
| `ball and socket` | collar outside to the cavity | 1.7200 mm | 1.72 mm |
| `ball and socket` | step around the collar's foot in a Ø24 limb | 4.2000 mm | 4.2 mm |
| `ball and socket` | cavity radius at the slit floor | 4.5789 mm | 4.5789 mm |
| `ball and socket` | the slit's inner edge, as a radius | 4.5789 mm | inside the cavity |
| `body` | the block, off its own faces | 72.000 × 48.000 × 96.000 mm | the same |
| `body` | both shoulder bosses end at | z 48.000 mm | z +48 |
| `head` | socket centre below the head centre | 46.000 mm | 45 mm |
| `head` | collar proud of the underside | 12.2205 mm | 10.947 mm |
| `head` | cavity centre above the rim plane | 2.2205 mm | 2.2205 mm |
| `head` | rim faces | four | four arcs |
| `head` | slit depth from the rim | 6.2205 mm | 4.947 mm |
| `head` | floor left above the slit | 6.000 mm | 6.000 mm |
| `head` | mouth diameter, off a rim arc | Ø11.320 mm | Ø11.520 mm |
| `foot` | sole, ankle ball centre, ankle height | z -24.000 mm, origin, 24.000 mm | the same |
| `foot` | groove floors, and their depth | eight at z -22.000 mm, 2.000 mm | one per rib |
| `foot` | ankle boss proud of the plate | 14.2205 mm | 14.2205 mm |
| `foot` | cavity volume | 717.140 mm³ | 689.06 mm³ |
| `gripper` | mouth across the opening | 2.600 mm | 2.600 mm |
| `gripper` | bore axis | (-1.000, 0.000, 0.000) | parallel to x |

Each row that differs is one of the two rulings already settled, or the cavity volume below.

**The step around the collar's foot needed two tabs.** `ball and socket` holds the collar and no
limb, so the Ø24.000 mm comes from the limb tabs and the 4.200 mm is the half-difference. Both
faces are cylinders, which is the *if either is square, stop and say so* half of that check.

**The slit's inner edge and the cavity meet at the same radius.** At the slit floor the cavity is
4.5789 mm across the axis and the slit's inner corner measures 4.5789 mm, because the slit face
ends where the cavity surface starts. That is the check passing: the bottom of the cut opens into
the hollow rather than closing into the ring.

**The gripper carries one sliver face.** `Jem`, on the clip's top at y 4.828 mm to 5.000 mm, is
0.171957 mm wide where the flat top nearly runs tangent to the Ø10 outside. **It is not the
0.16624 mm** left unexplained below, and the two cannot be reconciled from here: that measurement
was taken against a 36-face gripper and the part now reports 30 faces, so the face indices it names
no longer resolve. Re-taking it needs `featurescript`.

## The slit sketch, opened and looked at

`slit profile` was opened for edit on 2026-09-19, looked at, and escaped. Three things came off
the one frame.

- **Its sketch plane reads `Face of collar blank`.** That is the plane ruling passing on this
  sketch: a face of the part, not a stock plane.
- **The entities render dark, not blue.** Over the grey collar the lines and their points are
  black; the blue in the frame is the shaded cavity underneath. Its dimensions are on screen:
  `#slit_in` 3.67891 mm, two 0.8 mm halves of `#slit`, and the `4x` that marks the pattern.
- **The drag test was not run.** Dragging an entity and watching whether it moves is the
  definitive test, and a sketch dialog applies to the model as it is changed, so a drag on an
  under-defined entity would edit the deliverable. The eye is what this line asks for; the drag is
  what `featurescript` would replace.

**`#slit_in` is 3.67891 mm, and that is the number `ball-and-socket.md` names for the slit's
inner edge.** § *Ring 2's acceptance* above measures the slit face's inner corner at 4.5789 mm;
those are not in conflict. The slit is cut to 3.67891 mm and the cavity, which is 4.5789 mm across
at that depth, gets there first, so the face ends on the cavity. That is the check passing.

## The two tangency checks, measured off the profile rather than the whole part

`head.md` and `foot.md` each ask that a profile be tangent throughout, with no crease where an arc
meets a line. [`scripts/c_tangency.py`](scripts/c_tangency.py) walks the extrude's end cap around
its outer loop and reports the angle at each corner: the direction the one curve leaves by against
the direction the next arrives by, which is zero where they run into each other smoothly.

**`head`: both line-to-arc joins measure 0.0000 deg.** They are where the vertical sides meet the
domed top, and they are the joins the check is about. The profile's other two corners are the
bottom ones, at 90.0000 deg, line to line; an arch is meant to have those.

**`foot`: all four corners measure 0.0000 deg.** Heel arc to line to toe arc to line, tangent the
whole way round.

**`src/stickbot/measure_tangency.py` was already there and I did not read it first.** It does
the every-edge half off the tessellation, and its docstring says facet normals lag the surface by
about 1.15 deg so the exact figure belongs to `bodydetails`. The run script reads `bodydetails`
and adds the profile walk; the duplication is the every-edge part, and it is named in the script's
own docstring so the next reader finds both.

**The first two attempts at this measured the wrong thing**, and are worth naming because the
numbers looked plausible both times. Comparing surface normals at every shared edge reports the
eyes and the socket as creases, which they are and which no brief objects to. Narrowing that to
edges running along the extrude still caught the socket's slit walls, because a slit cut down the
collar has walls parallel to the extrude too. Only the end cap's own loop is the profile.

## A model defect: the gripper's clip body is 18.000 mm square and should be 15.600 mm

**This is the first fault in the model this acceptance pass has found, and it is not a brief's.**

`make_plans.py` sets `CLIP_W = 2 * COLLAR_R`, 15.600 mm, with the reason in the comment beside it:
*the one dimension in the robot that another part sets; it is the collar's own diameter, so the
socket standing on it is flush all the way round*. `plan-parts.svg` prints **platform 15.6 × 15.6
mm**. [`gripper.md`](../../build-briefs/gripper.md) § *Settled* says the same and says why it was
made an expression: *it was a typed number, and it went stale twice.*

**Measured: the clip body is 18.000 mm across the bar and 18.000 mm fore and aft**, so the Ø15.600
collar stands on it with a **1.200 mm ledge** at each mid-edge where the source wants tangency.
The chamfer follows the same error: its leg measures 4.000 mm, which is the body's half-width less
the clip's radius, where `CLIP_CHAM` is `COLLAR_R - CLIP_R` = 2.800 mm. One wrong number makes
both.

**The cause is a shadowed variable, and the first diagnosis written here was wrong.** This
section first said *the clip profile carries 18 as a number instead of `2 * #collarR`*, and that
`#collarR` resolves to 7.800 mm in the tab. Neither is so. I took the 7.800 mm from
`make_plans.COLLAR_R` rather than from the tab, which is the assumption the contract's *never claim
a verification you did not perform* exists to stop, and the number I should have read is the one
the tab computes.

**The `gripper` tab redeclares `#wall`.** `robot sizes` holds `#wall = #torsoH * 3 / 160`, which is
1.800 mm. The tab declares its own `#wall = #torsoH / 32`, which is 3.000 mm, and that shadows the
row. So `#collarR = #ball / 2 + #wall` resolves to **9.000 mm** there, and the clip body, which
really is written as `2 × #collarR`, comes out 18.000 mm. The chamfer follows the same variable:
`#collarR − #clipR` is 4.000 mm at 9.000 and 2.800 mm at 7.800, and the model measures 4.000 mm.

**The collar is Ø15.600 because it is derived, not computed here.** `copy socket` brings the socket
in from `ball and socket`, which reads the studio's `#wall` and so built a collar of radius
7.800 mm. That is why the part has a Ø15.600 collar sitting on an 18.000 mm square: the two halves
were sized by two different `#wall`s, one of them the studio's and one the tab's.

**Mike settled it on 2026-09-19: the socket's 7.800 mm collar radius is correct.** So the tab's
`#wall` is the defect and the fix is to stop the tab declaring it, which makes `#collarR` 7.800 mm,
the body 15.600 mm and the chamfer 2.800 mm in one change.

**Nothing turned red, and nothing was going to.** This is the hazard the `onshape` skill names in
as many words: *the local shadows the studio's row, the tab goes on using its own value, the row
moves without it, and nothing turns red.*

**`gripper.md`'s acceptance check is stale with it, and the checklist had taken the check's side.**
Line 183 asks for *one flat square face, 18.000 both ways, with the Ø18 collar standing on it*,
and goes on to name a 4.000 mm chamfer leg and a thinnest wall of *2.92, which is 9.0 - 6.08*.
Every one of those figures is `COLLAR_R` at 9.0, the value before Ø15.6. The measured thinnest wall
is 1.720 mm, which is 7.800 less 6.080, and § *Ring 2's acceptance* above already has it. The
checklist line is un-marked and now says the face measures 18.000 and that the check is written
against a collar the part does not have.

**Not fixed here, and why.** The fix is the tab's `#wall`, not a dimension, and it reshapes the
part: the renders held beside the parent go stale with it, and the assembly's own measurements are
taken again. Every feature in this draft is added over REST, and the `/features` POST is at zero
until about 16:17 on 2026-09-19. It is queued for then, with Ring 1's owed feature read.

## The thinnest wall in each part, taken without `featurescript`

Four briefs ask for the thinnest wall anywhere in a part, and `gripper.md` says outright that *a
throttled `featurescript` is not a reason to skip this one*. `bodydetails` gives each face's
surface exactly, so between two of them the distance is arithmetic rather than search:
[`scripts/c_thinnest_wall.py`](scripts/c_thinnest_wall.py) takes plane to plane, plane to cylinder,
plane to sphere, and coaxial or concentric pairs.

**Wall or gap comes off the outward normals, not off the size of the number.** A face's outward
normal is its stored normal when `orientation` is true and the opposite when it is false; the
head's front and back faces both store `-y` and only that flag separates them. For a curved pair
the same flag says which surface is a cavity: the socket's cavity sphere is false and its collar
cylinder is true, so material lies between them, where the ball stud's sphere and stalk are both
true and are simply the outside of a solid.

| Tab | Thinnest wall | Where |
| --- | ------------: | ----- |
| `ball and socket` | **1.7200 mm** | the collar's outside to the cavity |
| `head` | **1.7200 mm** | the same, in the derived socket |
| `foot` | **1.7200 mm** | the same |
| `gripper` | **1.7200 mm** | the same |
| `body` | **9.0000 mm** | the torso's side face to a hip stud's stalk |

**`gripper.md` predicted that shape of answer and this confirms it.** It says to expect the
thinnest wall at the socket collar and that it *is the same number on every socketed part in the
robot*. It is: 1.7200 mm on all four. The figure the brief printed was 2.92 mm, which is
`9.0 − 6.08` from the Ø18 collar; at `#collarR` 7.800 mm the same subtraction gives 1.720 mm, and
that brief is now written as the expression.

**The close approaches that are not walls, which the briefs ask to be separated out.** In every
socketed part the four nearest pairs are the relief slits at **1.6000 mm**, and they are gaps: the
two faces look at each other across air. On `body` the two nearest pairs are 2.0000 mm between a
shoulder boss and its ball and 4.0000 mm from a face to a ball, neither of which is a wall either.
**`body` is a solid part**, so its 9.0000 mm is the least material between two features rather than
a wall in the sense the socketed parts have one.

**The gripper's four tangencies at 0.0000 mm are the wall fix, seen a third way.** `Ja2`, the
collar, meets `JgG`, `JgK`, `JgS` and `JgO`, the clip body's four sides, at zero distance. Tangency
is not a thin wall and is reported apart from the walls; it is the same fact as the platform's four
corner lobes and the top view.

**What the method does not reach**, and it is why `featurescript` is still owed one thing: two
curved faces that are neither coaxial nor concentric, and any pair whose closest approach falls at
the edge of a face rather than across it. The second case bites in this very part. The chamfer
plane extended would pass 0.9663 mm from the clip's bore, but the chamfer face stops about 4 mm
short of where that happens, so the material there is thicker than the plane arithmetic suggests
and the pair is refused rather than reported. A tool that searched the faces themselves would give
the real figure.

**The gripper's unexplained 0.16624 mm is still unexplained**, and this did not find it. That
measurement named faces 22 and 29 of a 36-face gripper; the part has 33 faces now and had 30 an
hour ago, so the indices do not resolve, and nothing here comes near 0.16624 mm. It stays a
measurement nobody has identified.

## Fixed: the `gripper` tab no longer declares `#wall` or `#ball`

2026-09-19, on Mike's word, with a version published either side.

| | Version | Id |
| - | ------- | -- |
| before | `before the gripper wall fix` | `77d651aa4e43e369c93abb9b` |
| after | `gripper reads the studio's wall` | `4102df8544b8b185f6eb07c7` |

**Both rows deleted from the feature tree**, `#ball` first and `#wall` second.
[`scripts/c_drop_shadow_vars.py`](scripts/c_drop_shadow_vars.py) does it by the route
[`onshape-gui-howto.md`](../../../onshape-gui-howto.md) line 238 gives, right-click a variable row
→ Delete, because the `/features` DELETE shares its quota with the writes and the menu does not.
`#ball` went first on purpose: it resolves to the same 12.000 mm either way, so the row vanishing
with the shape unchanged is what proved the delete worked before the one that does change the shape
ran.

**`#collarR` read 9 mm before and reads 7.8 mm after**, off the tree row itself, with nothing else
touched.

**What the part became.**

| | Before | After | The source asks |
| - | -----: | ----: | --------------: |
| clip body, across the bar | 18.000 mm | **15.600 mm** | `2 × #collarR` = 15.600 mm |
| clip body, fore and aft | 18.000 mm | **15.600 mm** | the same |
| chamfer leg | 4.000 mm | **2.800 mm** | `#collarR − #clipR` = 2.800 mm |
| full-width run above it | 3.700 mm | **4.900 mm** | `#gripperL − #collarR − #mouth / 2 − #collar` = 4.900 mm |
| ledge under the collar | 1.200 mm | **0.000 mm** | tangent on all four sides |

**The tangency shows up as topology, which is the check worth keeping.** The platform was one face
of 132.866 mm²; it is now **four corner lobes of 13.0564 mm² each**, 52.2255 mm² together, which is
a 15.6 mm square less a circle of radius 7.8 mm exactly. A circle inscribed in a square touches all
four sides and cuts what is left into four disconnected corners, so the face count going 30 to 33
is the tangency arriving. A width measurement alone would not have told the two apart, and
[`counts-catch-what-dimensions-miss`](../../../../memory/counts-catch-what-dimensions-miss.md) is
the memory that says to count the patches.

**The top view says the same thing.** The collar's circle meets the square's four edges and the
corners are the only material outside it.

**Everything else in the part is where it was.** One part, bore Ø3.300 mm on an axis of
(-1.000, 0.000, 0.000), mouth 2.600 mm across the opening, lowest point z -24.000 mm, and the
collar still Ø15.600 mm at z -10.000 mm to 2.2205 mm.

**The assembly did not move**, which was the prediction and is now the measurement: 318.000 mm
sole to the top of the head, feet centred at x ±24.000 mm touching at 0.000 mm, and the grippers
reaching z -204.765 mm against a mid-thigh of z -190.890 mm. Nothing in the assembly reads the clip
body's width.

**The gripper now differs from draft9p1p1 on purpose, in a second place.** It already differed by
its socket, which is the plan's intent. It now also differs by the clip body, which is this
correction; the parent's frame shows the collar standing on a block with a ledge all round, and the
new render has it meeting the edge.

**The frames were retaken.** The gripper's renders are the part as it is now, and the ones of the
18.000 mm body are kept beside them only as the before.

## The arms' reach: nothing scaled wrongly, and the premise was never true

[`assembly.md`](../../build-briefs/assembly.md): *The plan sets shoulder-to-gripper equal to the
distance from the shoulder to mid-thigh, both 120. This is a pure ratio, so it should survive the
doubling exactly; check it on the assembly, because if it does not, something scaled that should
not have.*

**It survived the doubling exactly. The two were never equal.**

| | At this size | At half size | Ratio |
| - | -----------: | -----------: | ----: |
| the arm, `2 × #limbCenter + #gripperL` | **120.000 mm** | 60.000 mm | 2.0000 |
| shoulder ball down to mid-thigh | **101.235 mm** | 50.618 mm | 2.0000 |

Both doubled to the digit, so the test the brief proposed passes and its conclusion does not
follow. **For the two to be equal, the shoulder ball would have to sit 96.000 mm above the hip; it
sits 77.235 mm above it**, and did at half size too.

**So the arm passes mid-thigh by 18.765 mm**, measured joint to joint, and the figure has always
done so.

### Three numbers, and which one to quote

**This register said 13.875 mm and that depended on an unstated choice.** The differences are worth
naming because each is defensible and they are not the same measurement.

- **18.765 mm**, the arm's reach against mid-thigh taken as halfway from the hip joint to the knee
  joint. This is the one that matches how the brief describes both quantities, and it is the figure
  to quote.
- **13.875 mm**, which this register carried, takes mid-thigh as the middle of the thigh *part's*
  bounding box, z -190.890 mm. That box runs from z -222.000 mm to -159.779 mm, past both joints,
  because the socket and the fork stand proud of the centres they turn about.
- **9.422 mm**, what `make_plans` itself draws, because its arm is posed: `GB_Z` puts the gripper
  110.658 mm below the shoulder with the arm at 33.13 deg and the elbow bent 45 deg.
  `plan-assembly.svg` says so on its face; *elbows bent 45 deg for the picture; the assembly is
  saved at rest*. At rest the arms hang straight and the drop is the full 120.000 mm, which the
  assembly measures.

**Nothing here is a model defect.** The arm is the length the design gives it and the leg stations
are where the design puts them. What is wrong is one sentence in a brief, and the decision it
invites — whether the arms should reach mid-thigh, and which of the shoulder height, the limb
length or the hip station moves if they should — is Mike's.

## The interference check, run: no interferences at rest

**It was never a toolbar tool, and I looked for it in the wrong place for a day.**
[`onshape-gui-howto.md`](../../../onshape-gui-howto.md) has nothing on it, *Search tools* answers
*No items match your search* for the word, and the assembly's toolbar carries none. I recorded that
as *what the tool is called here is a question for Mike* and left it blocked across several ticks.

**[`trust-the-user-or-read-the-docs`](../../../../memory/trust-the-user-or-read-the-docs.md) names
three steps and I stopped at the second.** Grep the how-to, then ask the user, **then look it up**.
Onshape's own help has it: [Analysis Tools](https://cad.onshape.com/help/Content/View/analysis_tools.htm)
and [Interference Detection](https://cad.onshape.com/help/Content/View/interference_detection.htm)
say it opens from a **Show analysis tools** menu at the bottom right of the graphics area.

**Verified in this assembly rather than taken from the page.** The control is the middle of three
icons at the bottom right, at (1543, 952) in a 1600 x 1000 window; it carries no `title`, so it is
found by hovering and reading the tooltip, which is what the how-to already says about the rail
icons. Its menu holds **Interference detection**, *Zebra stripes* and *Reflection analysis*. The
menu item's own text cannot be matched as `Interference detection...`, because the ellipsis is one
character rather than three.

**The result, with all fourteen instances selected: `No interferences`.** Read off the dialog and
photographed. That is the robot at rest, which is the state every measurement in this register was
taken in.

**The shoulder does not interfere at rest either**, which is consistent with the geometry: the arm
clears the torso by +1.5509 mm at the zero pose and does not reach it until 33.2722 deg of tilt.
[`assembly.md`](../../build-briefs/assembly.md) asks to *drive the shoulder to its stop, run
interference, and report which face it lands on and at what angle*; the angle and the face are
measured off the geometry above, and the driving is still not done, for the reason the section
above gives.

## Posing cannot measure a stop in this assembly, and the record says why

[`assembly.md`](../../build-briefs/assembly.md) asks for *every ball joint's actual swing, measured
by posing it until it stops*, and Ring 3 for *every joint moved through its range, and what stops
it*. Both assume the joint stops. **In this assembly nothing does.**

Read off the saved assembly features, every one of the thirteen mates carries
**`limitsEnabled: False`**, with `limitEulerConeAngleMax` 0 and every other limit 0. Nine are
`BALL` and four are `REVOLUTE`. Onshape solves rigid bodies and an unlimited mate turns freely, so
dragging the head does not stop it at the torso; it drives the head through it. The assembly's own
brief says the same thing about the detent: *in CAD a revolute mate turns freely; the detent is a
print-time feature.*

**So the geometry is the answer, not a pose**, and it is already taken: the neck reaches the torso
at 45.240 deg nodding and 36.870 deg sideways, and the shoulder's arm fouls at 33.2722 deg, each
against the 39.0132 deg `BALL_SWING` the socket allows. Posing would have produced a number, and
the number would have been whatever the drag stopped at.

**What would make a pose mean something.** Setting `limitsEnabled` true and
`limitEulerConeAngleMax` to `BALL_SWING` on the nine ball mates puts the socket's own limit into
the assembly, so a drag stops where the joint stops. **It still would not find the collisions**,
which are what the interesting checks are about: a cone limit is one number per joint, and the
neck's two limits differ by direction, 45.240 deg fore and aft against 36.870 deg sideways. A
single cone cannot express that, and the tighter of the two is the torso rather than the joint.

**Not done, because it is a change to the model and nobody asked for it.** It is recorded here as
the shape of a fix.

## The gripper's 0.16624 mm, identified

It was measured on 2026-09-18, written down as *not yet a finding* because the faces it named had
never been read, and carried as open ever since.
[`scripts/c_close_pairs.py`](scripts/c_close_pairs.py) takes it with `evDistance` and names both
faces.

**0.16624 mm is the gap between the clip's Ø10.000 mm outer cylinder and the 45 degree chamfer on
its +y side.** The cylinder is r 5.000 mm with an area of 245.044 mm²; the chamfer is a plane of
61.773 mm² spanning y 5.000 mm to 7.800 mm at z -17.700 mm to -14.900 mm. The chamfer necks the
body down to the clip's own diameter and lands on the mouth's upper lip, and on the way it passes
the clip circle without touching it.

**It is a feather edge, not a wall.** Both faces are the part's outside, and the material caught
between them near that approach is the 0.171957 mm sliver `Jem` that `bodydetails` had already
found. At 0.4 mm to a nozzle, neither figure prints as drawn; what comes out is a rounded corner.
[`draw-it-and-print-it`](../../../../memory/draw-it-and-print-it.md) says to print it and let the
part correct the model rather than refusing the shape, so it is named here and nothing is changed
for it.

**The clip body fix did not move it.** It measured 0.16624 mm before the 18.000 mm body became
15.600 mm and measures 0.16624 mm after, which follows: the chamfer's landing on the mouth's lip
is what sets it, and that holds at either width.

### Two things about the instrument, both of which produced a wrong answer first

**`qEverything(EntityType.FACE)` is not the part.** In `gripper` it returns 39 faces: the solid's
33, plus 6 belonging to five surface bodies the Part Studio also holds. The first run of this
measurement was against all 39 and named a plane at x = 0 that is on none of the part, which sent
me looking for a body that does not exist. The query has to be `qOwnedByBody` over the solids, and
the script now is.

**A FeatureScript that will not parse answers HTTP 200.** The complaint arrives in `notices` with
`level` `ERROR`, and a client reading only the status sees a result with nothing in it. `box` is a
reserved word; using it as a variable produced *mismatched input 'box' expecting ID*, a 200, and a
script that appeared to find no close pairs at all. Both run scripts now read `notices` and refuse
a 200 that carries an error.

### The closest approach in each of the other parts

Measured the same way, on the solids alone. **The faces are identified by position; what each
approach *is* has not all been worked out**, and saying so is the point of recording them.

| Tab | Closest | Between |
| --- | ------: | ------- |
| `ball and socket` | **0.0800 mm** | the ball's sphere to four planes of the socket; 0.08 mm is `#fit` exactly, so this is the joint's clearance and the studio holds both parts |
| `head` | **1.6000 mm** | four plane pairs, which are the four relief slits |
| `foot` | **0.42857 mm** | a plane at y = -37.000 mm, 2 mm tall off the sole, against two planes running up the foot's sides |
| `body` | **1.51145 mm** | the torso's +x side face against a 172.79 mm² plane out at the shoulder, x 37.511 mm to 51.167 mm |
| `gripper` | **0.16624 mm** | named above |

**`foot` and `body` are both thinner than the wall
[`c_thinnest_wall.py`](scripts/c_thinnest_wall.py) reported**, 1.7200 mm and 9.0000 mm, and that is
the analytic method behaving as documented rather than disagreeing with itself: it answers pairs
whose surfaces face each other and declines the rest, and both of these are pairs it declines.

**`evDistance` gives the two points, which settles what each one is.**

- **`foot`, from (23.754, -37.000, -22.000) to (23.754, -36.571, -22.000).** Both points sit at
  z = -22.000 mm, which is the tread groove's floor, and at x = 23.754 mm, which is within a
  quarter of a millimetre of the sole's outer edge. So it is **a sliver of the foot's flank left
  beside one tread groove**, where a groove running straight across meets an outline that curves
  away. 0.42857 mm is about one nozzle width, so it will not come out as drawn; the render of the
  sole shows the grooves running clean out to the outline with no visible land.
- **`body`, from (36.000, -6.285, 23.320) to (37.511, -6.285, 23.320).** The two points differ
  only in x, so this is the perpendicular gap from the torso's side face to where the trimmed
  shoulder's flat face begins. **Air, not material**: both are the part's outside. It is a step,
  not a wall, and it is not the same measurement as the +1.5509 mm an arm clears the torso by,
  though the two numbers are close enough to be mistaken for each other.

## Ring 1, taken on every tab once the quota opened

The `/features` GET came back at 16:17 on 2026-09-19, to the minute the `retry-after` header had
been counting down to since the day before.
[`scripts/b_ring1.py`](scripts/b_ring1.py) fetched each tab once and wrote it to disk, so every
question after that is asked of the saved copy and a second opinion costs no call.

**The three checks the plan asks for, on all nine Part Studios and the assembly.**

- **Every `featureStates` entry is `OK`.** No `ERROR` and no `WARNING` anywhere. It arrives as an
  array of `{key, value}` wrappers with the status at `value.message.featureStatus`, which is the
  shape [`onshape-api-via-browser-session`](../../../../memory/onshape-api-via-browser-session.md)
  warns about.
- **`rollbackIndex` equals the feature count on every tab.** No bar is parked, so nothing
  downstream was being read short.
- **`robot sizes` has no `/features` at all.** A Variable Studio answers 404 on that route; its
  Ring 1 is the variables read, which was taken on 2026-09-18.

**`gripper` reads 13 features where the plan says 15**, which is `#wall` and `#ball` deleted that
morning.

### What `diff_features.py` could and could not compare

**The parent records' geometry queries are empty.** `foot`'s `pedestal outline` has its sketch
plane as `geometryIds: []` in the reference, against `["JDC"]` here. A sketch plane that picks
nothing cannot build, so that is a property of the export rather than a difference between the
models, and **entity counts are not comparable between these two records**. Naming it matters: it
is the difference on most of the rows, and reading them as findings would have buried the five
that are real.

**Five parameter differences in all, across eight tabs.**

| Tab | Feature | Mine | The parent | |
| --- | ------- | ---- | ---------- | - |
| `foot` | `foot`, `sole groove`, `sole ribs` | `defaultScope` **True** | False | the merge-scope correction this run made |
| `hinge` | `blade wedge` | `startOffset` **False** | True | the parent's is ticked with distance 0 and no entity |
| `ball and socket` | `stud connect to robot` | `entityInferenceType` **CENTROID** | CENTER | settled below, by measuring where it lands |

**The `foot`'s three are the defect this run already recorded** — the missing merge scope that
silently lost the foot's whole lower half.

**The `hinge`'s is a box ticked for nothing.** The parent carries `startOffset` true with
`startOffsetDistance` 0, `startOffsetBound` BLIND and no `startOffsetEntity`, so it offsets by
nothing; the hinge measured 510 faces face for face either way.

**Everything else the diff reports is this draft's own doing**: `hinge`'s renames and its dropped
`#ear` and `#backlash`, `body`'s ten connector renames, `gripper`'s two deleted rows, and the order
difference on every tab, which is the ruling that a variable is typed immediately above its first
reader rather than stacked at the top.

### Where every mate connector actually lands

The one difference left was how `stud connect to robot` infers its origin, and the way to settle
that is to measure where it ends up.
`evMateConnector` over `qBodyType(qEverything(EntityType.BODY), BodyType.MATE_CONNECTOR)`, which is
the lens that works where `qCreatedBy` finds nothing.

| Tab | Origins, in millimetres |
| --- | ----------------------- |
| `ball and socket` | (0, 0, 10) and (0, 0, -10) |
| `hinge` | (0, -8, 0), (0, 0, 38), (0, 0, -38) |
| `body` | the five ball centres, plus (44.339, -4.8145, 27.2218), (24, 0, -48), (0, 0, 48) twice |
| `head` | (0, 0, -36) twice, and (0, 0, -46) |
| `foot` | (0, 0, 0) and (0, 0, -10) |
| `u limb` | (0, 0, 0), (0, 0, -48), and three at (0, 0, -10) |
| `l limb` | (0, 0, 0), (0, 0, -48), (0, -8, 0), and three at (0, 0, -38) |
| `gripper` | (0, 0, 0) and (0, 0, -10) |

**`stud connect to robot` lands at (0, 0, 10) and `socket connect to robot` at (0, 0, -10)**, which
is `#collar` = `#stand` = 10 mm each way from the ball's centre.
[`ball-and-socket.md`](../../build-briefs/ball-and-socket.md) says exactly that: *the ball's center
to the bottom of the socket, which is exactly what the stud reaches the other way, so both halves
of the joint give up the same length of limb to it.* **So CENTROID puts the connector where the
design wants it**, and the difference from the parent is in how it is specified, not in where it
ends up.

**Every other tab reads the same way.** `body`'s five joint connectors sit on the five measured
ball centres, (0, 0, 58) and (+/-49.5509, -7.8236, 19.2355) and (+/-24, 0, -58). `head mate` is at
(0, 0, -46), which is the one number the assembly needs from that part. `u limb`'s two ends are
48.000 mm apart, which is `#limbCenter`, and so are `l limb`'s. `foot` and `gripper` both put their
joint end on their own ball centre at the origin.

**The counts are higher than the feature lists because a derive carries connectors with it.**
`body` has eight `mateConnector` features and nine connectors; the ninth arrives with
`copy ball stud`. The head's third is the derived socket's own root, at (0, 0, -36) rather than
(0, 0, -56), which is the socket sitting upside down on purpose.

## The arm against the torso, across the shoulder's whole swing

[`torso.md`](../../build-briefs/torso.md) calls this *the check the 26 mm stud length exists to
pass, and the only one here that can fail while every dimension measures correctly*, and asks for
the least clearance, the angle it occurs at, and the angle contact begins.

[`scripts/c_arm_clearance.py`](scripts/c_arm_clearance.py) takes the stud's axis and its ball's
centre off the torso's own face dump, runs a Ø24.000 mm arm `#limbCenter` from the ball to the
elbow, and sweeps it over the cone of `BALL_SWING` about that axis. The torso is its own block;
the Ø16 boss is left out because it is coaxial with the stud, which is what that brief says makes
it free.

**The stud axis reproduces from the model.** The boss roots at (36.000, 0.000, 40.000) on the side
face with an axis of (0.5212, -0.3009, -0.7986), and 26.000 mm along it lands on
(49.5509, -7.8236, 19.2355), which is the shoulder ball's measured centre.

| | Measured | `torso.md` expects |
| - | -------: | -----------------: |
| clearance at the zero pose | **+1.5509 mm** | +1.551 mm |
| the arm first touches the torso at | **33.2722 deg** | 33.38 deg |
| the joint allows | 39.0132 deg | 41.76 deg |
| so the arm fouls before the socket stops it, by | **5.7410 deg** | 8.4 deg |
| least clearance anywhere in the cone | **-4.7739 mm** | *contact inside the cone* |

**The zero pose reproduces exactly**, and it is worth saying where it comes from: the ball sits
13.5509 mm outside the torso's side face, so a Ø24 arm clears by 1.5509 mm at the ball itself,
before the arm goes anywhere. That is the 26 mm stud doing its job.

**The brief's conclusion holds and its two premises are stale.** It reasoned from a joint of
41.76 deg, which was draft9p1's `BALL_SWING`; this model's is 39.0132 deg. And it put the fouling
angle at 33.38 deg where the geometry gives 33.2722 deg. Both moves shrink the overshoot from
8.4 deg to 5.7410 deg, and neither changes the answer: **the torso stops the arm, not the socket**,
which is what the brief said the interesting part was.

**Where it lands, which the brief asks for.** At first contact the arm's axis is at
(48.00, -24.15, -25.88), 48.0 mm down the arm and 236 deg round the cone, which is the arm swung
down and across the body. It is 12.00 mm clear of the side face and 0.15 mm past the front face,
so what it reaches is **the vertical edge between the torso's +x side and its front**, not a face
flat on.

**The least clearance is at the cone's edge**, -4.7739 mm at the full 39.00 deg, so the deepest
fouling is at the joint's own limit.

**This is the geometry, not a driven assembly.** `assembly.md` asks to *drive the shoulder to its
stop, run interference, and report which face it lands on and at what angle*; the angle and the
face are here and the driving is not.

## The neck's real tilt limit, and what stops the head

[`head.md`](../../build-briefs/head.md) left this open: *the two-flat-plates model gives 21.8 deg
and is wrong, because the head's underside is 6 mm deeper fore-and-aft than the torso's top face
and its corners swing past that face rather than onto it. Drive the joint in the assembly, report
the angle, and name the face that stopped it.*

[`scripts/c_neck_tilt.py`](scripts/c_neck_tilt.py) turns the head's own points about the neck ball
and finds the angle at which one of them first enters the torso's block. **It is the geometry
answering, not the assembly driven**; posing the assembly is still owed, and this needs no quota
and leaves the robot at rest.

| Direction | The torso is reached at | On what | Against `BALL_SWING` 39.0132 deg |
| --------- | ----------------------: | ------- | -------------------------------- |
| nod forward | **45.240 deg** | the top-front **edge**, at (24.00, -24.00, 48.00) | the joint stops it first |
| nod back | **45.240 deg** | the top-back edge, at (24.00, 24.00, 48.00) | the joint stops it first |
| tilt right | **36.870 deg** | the **top face**, at (30.00, -18.00, 48.00) | the torso stops it first |
| tilt left | **36.870 deg** | the top face, at (-30.00, 18.00, 48.00) | the torso stops it first |

**The brief's reasoning is confirmed and its number was low.** Nodding, the head's corner does
swing past the top face; what it reaches is the edge between the top face and the front face, and
not until 45.240 deg, which the joint's own 39.0132 deg never lets it reach. So **fore and aft the
head never touches the torso at all**, and the limit is the stalk meeting the mouth.

**Sideways is the other way round, and nothing had noticed.** The head is 72 mm across and so is
the torso, so a corner coming down lands **on** the top face rather than beside it, at 36.870 deg.
That is 2.143 deg inside `BALL_SWING`, so side to side **the torso is what stops the head**, and
the joint does not reach its own limit. The two-flat-plates model's 21.8 deg is wrong in both
directions, and wrong by different amounts and for different reasons.

**36.870 deg is arctan(3 / 4)**, which is what a 72 mm head tilting about a ball 10 mm above a
72 mm torso gives; it is not a coincidence of this measurement.

**What this does not close.** The brief asks for the joint driven in the assembly, and Ring 3 asks
for every joint moved through its range. This is one joint, computed rather than posed. Both lines
stay open and carry the number.

## The robot's height is restated in four briefs, and every copy is stale

Mike asked on 2026-09-19 why so many component briefs mention the robot's height, since few of
them need it to build anything. They do not, and the copies have gone wrong.

**Where it belongs, and these are fine.**

- [`assembly.md`](../../build-briefs/assembly.md) line 40 and line 140: the deliverables row and
  the acceptance check. The assembly is where a whole-figure height exists, and one place measures
  it.
- [`README.md`](../../build-briefs/README.md) line 70: the stations table all the briefs read the
  frame from, so the total sits there once.
- [`ball-and-socket.md`](../../build-briefs/ball-and-socket.md) line 86, on why the collar is
  measured from the ball's centre: *the fit moves the hollow and leaves the robot's height alone*.
  **This is the shape the others should have.** It names the height because the height is the
  reason for the definition, and it carries no figure, so there is nothing in it to go stale.

**Where it is a copy, and the copy is wrong.**

| Where | It says | It should say |
| ----- | ------- | ------------- |
| `head.md` line 101 | top of the head +139.00, the figure **317.00** | +140.00, 318.00 |
| `head.md` line 98 | collar rim +56.05 | +55.7795, the ball centre less `#grip` 2.2205 |
| `head.md` line 99 | head underside +67.00 | +68.00 |
| `head.md` line 100 | head centre +103.00 | +104.00 |
| `head.md` line 109 | *makes the figure 317.00 rather than 317.05* | the rule is right, the figure is a copy |
| `head.md` line 115 | *that 317.00 is round is a coincidence* | the same point `torso.md` also makes |
| `head.md` line 237 | the whole part is **82.947** tall, −46.947 to +36.000 | 84.2205, −48.2205 to +36.000 |
| `torso.md` line 78 | the figure's height is **317.00 mm** | the sentence is fair, the number is a copy |
| `torso.md` line 81 | *came out at 317.05* | the same |
| ~~`README.md` line 70~~ | `HEAD_T` +137.4, `HEIGHT` **315.4** | **deleted 2026-09-19** |
| ~~`foot.md` line 164~~ | *a 96 mm foot on a 315.4 mm figure* | **deleted 2026-09-19** |

**`head.md` contradicts itself two lines apart.** Its station table gives the underside at +67.00
and the top at +139.00; the prose immediately below says *the underside is at +68.00 rather than
+58.05 and the top of the head at +140.00*. The prose is current and the table is not.

**`README.md` does everything right and is still stale**, which is the interesting part. It names
`make_plans.py` as the source, it labels its own table *a printout, not a source; where it
disagrees with the file, the file is right*, and it ships the command that regenerates it. Running
that command gives `-178.0 -154.0 -106.0 -58.0 19.235476738770387 58.0 140.0 318.0`, so six rows
still match and `HEAD_T` and `HEIGHT` do not. A printout pasted into prose has to be pasted again
by hand, and nobody did. That is
[`derive-dont-maintain`](../../../../memory/derive-dont-maintain.md) with the derivation written
down beside it and still not run.

**Two of them went the same day, and by deletion rather than by correction.** Mike removed
`README.md`'s stations table, taking `HEAD_T` +137.4 and `HEIGHT` 315.4 with it, and `foot.md`'s
proportion question. Deleting beats correcting for both: the table was a printout of something
`make_plans.py` computes, and the surviving sentence still says to import it rather than copy it;
the proportion question was a judgement that had already been made. **A copy that has to be
maintained is better gone than right**, which is what
[`derive-dont-maintain`](../../../../memory/derive-dont-maintain.md) says and what these two now
show.

**`head.md` and `torso.md` were done on 2026-09-19, by the same rule Mike gave: tend to delete the
text that does not define what the brief's own part should be designed to.**

- **`head.md`'s global station table is gone**, with the paragraph under it and the round-figure
  passage. Where the head lands in the robot is the assembly's, and the brief's own line above the
  table already said *model the head about its own center; the assembly places it*. What was kept
  is the rule that does define the head: **the underside is placed off the ball's center, not off
  the rim**, so the fit cannot reach the head's placement.
- **Two rows went out of `head.md`'s numbers table**, the socket collar's Ø18.0 and its length
  9.0. Both were `ball-and-socket.md`'s, both were the pre-ruling figures, and the brief says four
  lines later that *the collar rows come from `ball-and-socket.md` and are not this brief's to
  change*.
- **Two rows in that table were corrected rather than deleted**, because they are the head's own
  frame and are what it is built to: the socket centre reads `36 + #collarL`, z = -46.0, where it
  said `36 + #collarL − #grip`, z = -45.05; and the collar rim reads `36 + #collarL + #grip`,
  z = -48.2205, where it said `36 + #collarL`, z = -47.0. **Both formulas were wrong, not only
  the values**: the rim's was the socket centre's.
- **The head's own height was corrected**, from 82.947 to `36 + 36 + #collarL + #grip`, 84.2205,
  which is what the part measures. A part's own extent is its brief's business.
- **`torso.md` keeps the discipline and loses the figure.** The height is still *whatever those
  stations add up to, printed by the plan rather than aimed at*, and *do not adjust anything to
  reach a total* still stands; the 317.00, the 317.05 and the 158.15 are gone, and it points at
  `assembly.md` for what the sum comes to.

**Nothing in the briefs now prints the robot's height except `assembly.md`**, which measures it,
and the two withdrawal notes that say what a reader meeting an old number is looking at.

## A defect in how the whole robot is built: the collar's radius is computed again in each tab

**Mike raised this on 2026-09-19, and it is the general fault the gripper's 18.000 mm is one
instance of.** In his words, we recompute `#collarR` in several places rather than having sketches
that use the geometry of the socket; that is CADing like a computer rather than like a person.

**Where the same radius is written out.** `robot sizes` has no collar-radius row at all, so every
tab that needs one makes its own.

| Where | Written as | Name |
| ----- | ---------- | ---- |
| `make_plans.py` line 100 | `BALL / 2 + COLLAR_WALL` | `COLLAR_R` |
| the `gripper` tab | `#ball / 2 + #wall` | `#collarR` |
| the `foot` tab | `#ball / 2 + #wall` | `#collar_r` |

The design source is entitled to hold it; the two tabs are each a second copy of a fact, which is
[`derive-dont-maintain`](../../../../memory/derive-dont-maintain.md) in geometry rather than in
prose. **And the two tabs spell the name differently**, `#collarR` against `#collar_r`, so a search
for one does not find the other. That is part of why the gripper's went wrong without being seen.

**The socket is right there, in every one of those tabs.** `copy socket` and `add socket` bring it
in as a derived body, so the collar is a real cylindrical face with a real circular edge in the
same Part Studio as the sketch that wants its size. A person builds the square by projecting that
edge and constraining the four sides tangent to it; the square is then the collar's size because
it is the collar's edge, and it follows the socket whatever the socket becomes. Nothing recomputes
and nothing can disagree.

**The model passes the letter of the rule and misses its point.** `cad-models-need-design-intent`
and the `modeling-practice` skill ask for constraints and variables rather than magic coordinates,
and the tabs do use variables. But a variable recomputed in a second place is not a relationship;
it is a typed number with an expression's face on it, and it goes stale exactly the way a typed
number does. The `onshape` skill says the same thing from the other side: *never type a number to
place or size something a reference would have given you.*

**Mike's second point: the briefs ask for dimensions where the design intent is tangency.**
`gripper.md` § *Settled* states the intent outright; the body's top is *a square of the collar's
diameter, coaxial with the socket and tangent to it on all four sides*. Then its numbers table
gives **body width `2 × #collarR` = 15.6** and its acceptance check measures a width. What gets
built is what the table says, so the tangency lives in a sentence nobody builds from and the
number is what reaches the CAD. `foot.md` does the same at its ankle boss: *stands `#grip +
#plate` = 14.2205 proud*, where the intent is that the boss's top and the socket's rim are the
same face.

**What that implies for the briefs, and it is not this draft's to do.** A step table that names the
reference and the constraint builds the intent; one that names the length builds a number that was
right once. Neither the briefs nor `make_plans.py` is draft9p5's to change, so this is registered
and not acted on; it is the shape of the fix rather than the fix.

## Every Part Studio variable that shadows a `robot sizes` row

[`scripts/c_shadowed_vars.py`](scripts/c_shadowed_vars.py) compares the studio's row names against
each tab's own, over `/api/variables`, which answers while `/features` is refused. **Both
redeclarations in the document are in `gripper`, and no other tab has one.**

| Tab | Name | The tab says | `robot sizes` says | |
| --- | ---- | ------------ | ------------------ | - |
| `gripper` | `#wall` | `#torsoH / 32`, 3.000 mm | `#torsoH * 3 / 160`, 1.800 mm | **disagrees** |
| `gripper` | `#ball` | `#torsoH / 8` | `#torsoH / 8` | agrees today |

**Both are defects, and Mike said to register them as such.** The second is the same trap with its
spring unsprung: `#ball` carries the studio's own expression, so it gives 12.000 mm today and will
go on giving whatever `#torsoH / 8` gives even after the studio's row is changed to something else.
A redeclaration that agrees is not a redeclaration that is safe; it is one whose damage has not
been triggered yet, and it reads to a student as the way to get at a studio row.

**`#collarR` is not one of them.** The tab declares it and the studio does not, and the skill says
a local computed from studio rows is a different thing and is fine. What makes it wrong here is
that one of the rows it computes from is the shadowing `#wall` rather than the studio's.

**The other seven tabs declare 54 local rows between them and none clashes.** `ball and socket`,
`hinge`, `body`, `head` and `foot` each carry their own names; `u limb` and `l limb` declare none.

**This was a Phase A item and it was read too narrowly.** Phase A confirmed that `#wall` reads
`#torsoH * 3 / 160`, and it confirmed it on the studio. Nothing asked whether a tab had a `#wall`
of its own, so the one that had did not come up.

## The head has no shell, and its brief asks for one twice and omits it once

[`head.md`](../../build-briefs/head.md) carries two build orders that disagree.

- § *Suggested build order*, item 9: **Shell** last, thickness 1.2, **opening the back face**.
- § *Acceptance checks*: **Shell thickness 1.200** at three places, one of them next to a cut.
- § *Recommended steps*, the table: fourteen rows ending at `head mate`, with no shell in it.

The plan's Tab 5 was derived from that table, and so was the model. The parent record
[`head.features.json`](../2026-08-29-draft9p3/reference/head.features.json) has no shell either, so
no head in this project has ever been shelled.

**Measured: the head is solid, 263588.0 mm³.** The brief predicts the shell's effect itself; its
§ *The idea being tested* works out *roughly 23200 mm³ of wall inside a 266720 mm³ solid; about
91%*. The solid it predicted is the part that exists, to within the rounding of its own arithmetic,
and the wall it predicted is not there.

**This is a design decision, not a correction.** Shelling the head removes about nine tenths of its
plastic and changes what the socket sits in; the brief's own § *Why the shell opens the back* says
the underside was refused four ways by run 3 and that the diagnosis was made against a part the
brief no longer describes. Nothing in the model is wrong against the table it was built from.

## Two briefs give the socket's cavity two volumes

It is one socket, derived into `head`, `foot`, `gripper` and both limbs, so it has one cavity.

- [`ball-and-socket.md`](../../build-briefs/ball-and-socket.md) line 255: **717.14 mm³**, with the
  arithmetic beside it; a Ø12.16 sphere is 941.455 mm³, less the 224.314 mm³ cap above the mouth
  plane.
- [`foot.md`](../../build-briefs/foot.md) line 110 and
  [`limbs.md`](../../build-briefs/limbs.md) line 122: **689.06 mm³**.

**Measured 717.140 mm³**, from the cavity sphere's own radius of 6.0800 mm and the rim plane
2.2205 mm above its centre. The model agrees with `ball-and-socket.md` and with that brief's shown
working. 689.06 mm³ needs the rim about 1.95 mm from the centre instead of 2.2205 mm, which is the
`#grip` the collar ruling moved.

## The assembly's element id had moved, and `results/ids.md` had not

`/api/assemblies/.../e/599b6d255571795de9383404` answers **Element not found.** That element was
deleted and rebuilt on 2026-09-18, when its mates would not delete reliably by id and it ended up
holding twenty-six mates made from thirteen. The live ids, read back from the document's own
element list, are `c81b630354bd0739d788a42d` for the assembly and `cc25ef6cbcdced6c0877d72b` for
the Bill of Materials that comes with it. [`results/ids.md`](results/ids.md) is corrected and says
why they changed.

**Reading a point in the assembly works, and it is two steps.** The assembly returns fourteen
occurrences, each with a 4 × 4 row-major transform, alongside the thirteen mate features; a part's
own `bodydetails` gives every vertex as a point and every edge as start, mid and quarter points,
so a point in assembly space is the part's point through its occurrence's transform. Mike asked
whether this was easy; it is, and it survives the 429 that stops `featurescript`.

# The design's defects, in one place

Ring 4's *What the briefs and the design source owe* was written before most of these were found.
This is the whole list. Most of it is a place where a brief and the geometry disagree rather than a
fault in the model; every model fault this run made while building was fixed and is recorded where
it happened. **One was a fault in the model as built**, the gripper's clip body, found on
2026-09-19 by holding the part beside `plan-parts.svg` and fixed the same day.

**The briefs named in § *Settled* were corrected on 2026-09-19, on Mike's word.** Settled used to
mean only that we knew which side was right; the stale sentences stayed in the briefs. They no
longer do. Each row below says what the brief now reads and what the withdrawn figure was, so a
reader meeting an old number in an older record can place it.

## Settled: the model is right and the words trail a ruling

Each of these follows from `#collar` becoming `#stand` at 10 mm, or from the printed ball's loss
being taken off the mouth — both settled after the brief that states the old number.

| Where | It said | It now reads | The withdrawn figure was |
| ----- | ------- | -----------: | ------------------------ |
| `head.md` | socket centre 45 mm below the head centre | `36 + #collar`, **46.000 mm** | the same, at `#collar` 9 |
| `head.md` | collar stands 10.947 mm proud | `#collar + #grip`, **12.2205 mm** | the same, at `#collar` 9 and `#grip` 1.9465 |
| `head.md` | slits 4.947 mm deep | `#grip + #ball / 3`, **6.2205 mm** | the same, at `#grip` 1.9465 |
| `head.md`, `foot.md`, `limbs.md` | socket mouth Ø11.520 mm | `#mouth − 2 × #ballLoss`, **Ø11.320 mm** | the mouth before the ball's loss |
| `foot.md`, `limbs.md` | cavity volume 689.06 mm³ | **717.14 mm³** | the cavity at `#grip` 1.9465 |
| `foot.md` | thinnest wall 2.20 mm, `9.0 − 6.8` | `#collar_r − (#ball + 2 × #fit) / 2`, **1.72 mm** | the same, at the Ø18 collar |
| `head.md`, `assembly.md` | the figure stands 317.00 mm | **318.00 mm** | the height at `#collar` 9 |
| `gripper.md` | *the Ø18 collar*, 18.000 mm both ways | `2 × #collarR`, **15.600 mm** | the width at the Ø18 collar |

**Every one is written as its expression now, not as the number it currently gives.** That is the
point of the exercise: the figures went stale because they were literals, and three of them had
gone stale twice.

`brief-socket.svg` settles the fourth on the model's side: the sheet itself says **mouth Ø11.320
mm**, so the design source's drawing and the model agree and one sentence of prose does not.

**The head's 3 mm was a bounding box read as a dimension, and nothing disagrees.** This entry stood
under *Open* saying no ruling accounted for the head measuring 63 mm fore and aft against `HEAD_D`
60. The head's own front face is at y = -30.000 mm and its back face at y = +30.000 mm, so the head
is 60.000 mm deep, face to face, exactly as `HEAD_D` computes. Each eye's end face is at
y = -33.000 mm, which is the whole of the 3 mm: the eyes are in the box and the box is not the
head. `head.md:67` says it outright; **The eye stands 3 proud; the mouth cuts 3 in**, and the
mouth's floor measures y = -27.000 mm to match. Measured 2026-09-19 off the head's `bodydetails`,
on Mike's question about how far the eyes protrude.

**The feet touch, and only one line anywhere said otherwise.** `assembly.md` asked for a gap of
16 mm with the inner edges at x ±8; the model measures 0.000 mm with them at x 0. The design
source, the generator, `foot.md` and `assembly.md`'s own preceding bullet all say the feet meet,
because the 8 mm outboard offset that produced x ±8 was withdrawn on 2026-08-26. The brief was
fixed on 2026-09-19; § *The feet touch* above carries the sources and the wording.

**The same dump settles the eye's size on this build.** Each eye's end face is 100.531 mm², which
is `math.pi * EYE_RX * EYE_RY` with `EYE_RX` 8 mm and `EYE_RY` 4 mm; the centres are at x +/-12.000
mm and z +8.000 mm. The 102.0857 mm² that `stickbot-draft9p4-check` reproduces from
[`head.rst`](../../../../instructions/stickbot-draft9p4/source/head.rst) is that page's defect and
is not in this model.

## Open: nothing explains these, and they are decisions rather than corrections

- **The robot's height is restated in four briefs and every copy is stale**, at 317.00 mm in
  `head.md` and `torso.md` and 315.4 mm in `README.md` and `foot.md`, against a measured and
  computed 318.0 mm. `head.md`'s station table disagrees with its own next paragraph. Only
  `assembly.md` and `README.md` have a reason to carry it, and `ball-and-socket.md` shows the
  right shape by naming the height without a figure. Raised by Mike on 2026-09-19; § *The robot's
  height is restated* above lists every line.
- **The collar's radius is computed again in each tab that needs it, rather than taken off the
  socket's own geometry.** `make_plans.py` has `COLLAR_R`, the `gripper` tab has `#collarR` and the
  `foot` tab has `#collar_r`, all spelling `#ball / 2 + #wall`, while `robot sizes` has no row for
  it and the socket is a derived body in both tabs with the collar as a real face. Raised by Mike
  on 2026-09-19 as CADing like a computer rather than like a person; § *A defect in how the whole
  robot is built* above carries it, with the part the briefs play in causing it.
- ~~**The `gripper` tab redeclares `#wall` and `#ball`.**~~ **Fixed on 2026-09-19.** `#wall` was
  `#torsoH / 32`, 3.000 mm, against the studio's `#torsoH * 3 / 160`, 1.800 mm, so `#collarR`
  resolved to 9.000 mm and the clip body came out 18.000 mm with a 4.000 mm chamfer leg and a
  1.200 mm ledge under the Ø15.600 collar. `#ball` carried the studio's own expression and shadowed
  the row all the same. Both rows deleted; the body is 15.600 mm, the chamfer 2.800 mm and the
  ledge 0.000 mm. § *Fixed: the `gripper` tab no longer declares* above carries it.
- ~~**The head has no shell, and `head.md` both requires one and omits it.**~~ **Settled by Mike
  on 2026-09-19: the final head has no shell, and the brief now expects none.** Its
  § *Suggested build order* had a step 9, its § *Acceptance checks* measured a 1.2 mm wall, and its
  own numbers table said *not built, and never has been*. The head measures 263588.0 mm³ solid.
  `head.md` now carries § *The head is solid*, its shell step is gone, and the shelling passages
  are kept under a heading that marks them superseded. **What is not settled is the lesson**: the
  head was the only part that used Shell, an earlier draft put a temporary one on to teach the tool
  and backed it out, and where that leaves the curriculum is a question for the lesson design. The
  brief says so and settles only the inspection.
- ~~**The socket's cavity has two volumes in the briefs.**~~ **Fixed 2026-09-19; it was the same
  settled ruling.** 689.06 mm³ is the cavity at `#grip` 1.9465 mm, which is `#ballLoss` at zero:
  a Ø12.16 sphere less the cap the mouth plane cuts, with the plane 1.9465 mm off centre instead of
  2.2205 mm. So it moved with the mouth's Ø11.520, and it was never an independent question.
  `foot.md` and `limbs.md` now read 717.14 mm³ with the arithmetic beside it.
- **The arms pass mid-thigh by 18.765 mm, and always have.** `assembly.md` calls this *a pure
  ratio, so it should survive the doubling exactly; check it on the assembly, because if it does
  not, something scaled that should not have.* **It did survive**: the arm and the shoulder-to-
  mid-thigh distance both double to the digit, 60.000 to 120.000 and 50.618 to 101.235. What is
  untrue is the premise that they are equal at 120; for that the shoulder ball would have to sit
  96.000 mm above the hip and it sits 77.235 mm above it. A sentence in a brief is wrong and no
  part is; whether the arms should reach mid-thigh, and what moves if they should, is a design
  decision. § *The arms' reach* above carries it, with the three different numbers this has been
  quoted as and why they differ.
- ~~**The robot's height is given twice and differently.**~~ **Fixed 2026-09-19; it was the same
  settled ruling, and calling it unresolved was my error.** `make_plans` has
  `HEAD_B = NECK_Z + COLLAR_L` and `HEAD_T = HEAD_B + HEAD_H`, so the height moves with the collar:
  318.0 mm at `#collar` 10 and 317.0 mm at 9. The 1 mm is `#collar` becoming `#stand`, the same
  ruling as the head's socket centre and its collar height, and the same one `head.md` was still
  printing as 45.000 and +139.00. `assembly.md` and `head.md` now read 318.00 mm.

## Not the design: tools that had gone stale

Recorded here only so the list of what this run found is complete.

- **`measure_walls.py` could not read today's `bodydetails`** — surface types recased and vectors
  turned from maps into lists. Fixed on Mike's word.
- **Two endpoints the 2026-08-30 scripts used are 404** — creating a Variable Studio, and renaming
  an element. Replacements measured and recorded.
- **`shadedviews` ignores `cutPlane` and `sectionPlane`** rather than refusing them, which
  `onshape-gui-howto.md` already carried and this run confirmed.

## Reading the memories, and what the first one paid for

This run had read exactly one memory body — `onshape-api-via-browser-session` — and taken the rest
from the one-line descriptions the index injects. Mike asked what the whole set costs: 28 files,
44,325 characters, about 10,000 tokens. Reading them is cheaper than the three mistakes not reading
them caused.

**Three of this run's own failures are written down in memories it had not opened.**
`feature-edits-apply-live` says a crashed dialog keeps whatever it last applied and a script must
press Escape on every failure path — which is how a stray `Derived 1` was committed to `body`.
`trust-the-user-or-read-the-docs` says grep the how-to first — the section-view procedure was hunted
through three UI surfaces and the how-to had all of it. `test-the-technique-not-a-guess` says not to
write down a negative about a method until the run is shown to have exercised it — which is the
union hypothesis exactly.

**And one paid for itself at once.** `onshape-bodydetails-beats-featurescript` ends with *what it
does not give is the distance between two faces, so minimum wall thickness still needs Feature
Script* — which is the route for the *thinnest wall anywhere* check four briefs ask for and this
run had left open.

## Identified: the thinnest wall anywhere, and the number that was not one

`evDistance` over every pair of faces, keeping the smallest distance that is not zero — faces that
meet share an edge, a vertex or a tangency and measure zero, so a wall is the smallest gap above
that.

**`gripper`: 0.16624 mm, between face 22 and face 29 of its 36.**

**Settled on 2026-09-19**, once `featurescript` answered again: it is the
gap between the clip's Ø10.000 mm outer cylinder and the 45 degree chamfer on its +y side, and it
is a feather edge rather than a wall. § *The gripper's 0.16624 mm, identified* above carries it,
along with the two ways the instrument gave a wrong answer first.

**The follow-up cannot be taken yet: `featurescript` has now spent its own quota**, 8.6 hours,
reset about 16:15 on 2026-09-19; the same clock as `/features`. `bodydetails`, `parts`,
`boundingboxes`, `assemblies` and `variables` all still answer, which is what that memory says to
expect and what this run has been living on.

**The other three tabs have not been measured this way at all.**

## What the rest of the memories changed

All twenty-eight bodies are now read. Three caught something this run was doing.

**`derive-dont-maintain`: stop tallying.** The user's words in it are *you keep on counting things
that don't need to be counted, and then editing the counts — I need you to stop doing that.* This
register and every watchdog report has been doing it: a checklist score restated each tick, the
number of features that build, the number of pairs tested, the number of findings settled against
open. Each is a count of this document's own contents, and each has to be edited the next time the
document grows. It does not forbid a measured number cited as evidence — 22 faces face for face is
a finding; 273 of 364 lines is bookkeeping. The checklist already carries its own state; reading it
back out is the work-making.

**`no-em-dash-near-a-number`: six fixed here.** An em dash beside a figure reads as a minus sign.
Six lines in this file had one and now carry a semicolon. One is left on purpose — `§ *Ring 1 — the
feature*` quotes the plan's own heading, and no reader takes that for a subtraction.

**`every-feature-gets-its-name`: the name goes in first.**
[`scripts/c_gui_derive.py`](scripts/c_gui_derive.py) filled the Derived dialog, ticked it, then
renamed the tree row. The memory says to type the name into the dialog's title before filling it,
because a name set last is wrong in every frame already taken of that step — the tree row and the
dialog header are both in the picture. This draft takes no frames so nothing was spoiled, but the
draft that writes the pages will drive this same script. It now names the dialog first and fails if
a `Derived N` row survives, which is what a naming that did not take looks like.

**Two more that this run had already obeyed by accident rather than by reading.**
`never-busy-wait-in-bash` says run the long job in the background and wait for the notification
rather than polling; the harness refused a `sleep` loop and pushed me there. `agent-browser-borrows-
its-session` gives the exact restart for a dead 9223 — which is what was done twice, both times
after killing it myself with a `pkill` pattern broad enough to match it.
