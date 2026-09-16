# draft9p1p4 build notes

What the build actually did, tab by tab, including where it departed from
[`plan.md`](plan.md). Ids are read off Onshape, not transcribed.

## The document

| What | Id |
| ---- | -- |
| document `stickbot-draft9p1p4` | `eca1f9c7feff156a3303d563` |
| workspace | `3a7d66574eb06d933f843fae` |
| version `C1 done - Phase C proved` | `be669c9b52ba1f351a4c0e79` |

The recovery point is
<https://cad.onshape.com/documents/eca1f9c7feff156a3303d563/v/be669c9b52ba1f351a4c0e79/e/a4c789e918b85c50bd4e5ca8>,
opened in the browser rather than assembled: it comes up on `ball and socket` with the banner
*Versions are view only*, seven tabs, and both mate connectors regenerating. The live workspace, for
anyone who needs to edit rather than read, is the same document under
`/w/3a7d66574eb06d933f843fae`.

| Tab | Element | Lineage |
| --- | ------- | ------- |
| `robot sizes` | `988b1956623d991267021267` | `stickbot-draft9p3` |
| `ball and socket` | `a4c789e918b85c50bd4e5ca8` | `stickbot-draft9p3` |
| `hinge` | `ec6bde5ed2da077ce95ef48c` | `stickbot-draft9p3` |
| `u limb` | `b7031730f11d5b9421f79441` | `stickbot-draft9p3` |
| `l limb` | `659ecfa1f8cd7ad13d2af8e6` | `stickbot-draft9p1` |
| `robot sizes (1)` | `35c2e16ae618cbda0da2a76e` | `stickbot-draft9p1`, to be removed at B5 |
| `hinge (1)` | `c360fada8952724a7502cee9` | `stickbot-draft9p1`, to be removed at B5 |
| `ball and socket (1)` | `3cbbee82c47aa2349969911f` | `stickbot-draft9p1`, to be removed at B5 |

## B0 deviation — the document is a copy of draft9p3, not an empty document filled tab by tab

`plan.md` declares `from` as `empty`, then copied into tab by tab. The Onshape API does not offer
that. Its whole route list, read from `GET /api/openapi`, holds three copy routes and no other:

- `POST /documents/{did}/workspaces/{wid}/copy`, which copies a whole workspace into a new document
- `POST /elements/copyelement/{did}/workspace/{wid}`, which copies one element between documents
- `POST /appelements/.../copyassociativedata`, which is not about tabs

So the build copied `stickbot-draft9p3`'s workspace into a new document, renamed it, and deleted
`body`, `head`, `foot`, `stickbot` and the bill of materials. The bill of materials went with the
assembly and answered 404 on its own delete, which is the expected order.

**This is a better copy than the plan asked for, not a worse one.** A workspace copy carries the
Variable Studio, which no element route does, and it re-points every reference as it goes.

An earlier probe read `POST /elements/copyelement/{did}/w/{wid}` and got 404 from every shape of it.
The route wants `/workspace/`, spelled out. Reading Onshape's own route list settled in one call
what guessing had not settled in a dozen.

## The lower limb brought its dependencies with it

`copyelement` copies an element **and everything it derives from**. Copying `l limb` out of
`stickbot-draft9p1` therefore also created `hinge (1)`, `ball and socket (1)` and
`robot sizes (1)`, and re-pointed the copied limb at those rather than at the tabs already here.

## Which references leave the document

None. This is the defect B0 exists to find, and there is not one: every derive and every mate
connector names an element in this workspace. Onshape writes a derive's target as a `namespace`
string, and a reference that stays inside the document has no `d` term in it.

| Tab | Feature | Points at |
| --- | ------- | --------- |
| `u limb` | `add socket` | `ball and socket` |
| `u limb` | `add fork` | `hinge` |
| `l limb` | `add blade` | `hinge (1)` |
| `l limb` | `add ball stud` | `ball and socket (1)` |

**The lower limb's two derives are the one thing wrong, and they are wrong inside the document
rather than outside it.** They name the draft9p1 copies. B5 re-points them at `hinge` and
`ball and socket` and then deletes the three trailing tabs. Re-pointing is not free: a derive
carries the geometry id of the part it took, and the draft9p1 hinge and the draft9p3 hinge do not
number their parts the same way, so the query is expected to need picking again.

## B1 — `robot sizes` holds twenty rows and agrees with the design source

The studio now carries the four drivers and the sixteen rows the rule brings up with them, in the
order [`../../../robot-build-plan.md`](../../../robot-build-plan.md) lists them. Nine of those rows
are new here, and three changed: `#wall` is `#torsoH * 3 / 160`, `#collar` is `#stand`, and `#grip`
takes `#ballLoss` off the mouth's half-width.

Every row was read back out of Onshape with `getVariable` inside `ball and socket` and compared with
`make_plans.py` by import. None disagree.

**A variable can only be written after the rows it reads.** `POST /variables/.../variables` takes
the whole table at once but validates each expression against what is already stored, so a table
posted in one call fails on the first row that reads a row in the same call. The build posts the
table once per row, adding one row each time. Twenty calls write twenty rows.

**Where a Part Studio still declares a name the studio holds.** Each is removed as its tab is
edited, because removing one changes what the tab builds:

| Tab | Declares | What it becomes |
| --- | -------- | --------------- |
| `u limb` | `#limbD` | the studio's row, same value |
| `l limb` | `#limbD` | the studio's row, same value |
| `hinge` | `#limbD`, `#blade`, `#blade_out`, `#slot_deep` | the studio's rows, same values |
| `hinge` | `#gap` | the studio's row, and the value moves 0.6 to 0.15 |
| `hinge` | `#slot` | dropped; the studio's `#seat` is the same rule and the settled width |

`ball and socket` declares `#slit` only, which is its own and stays.

## B2 — `ball and socket` is the settled socket

The tab keeps five variables now, each named for what it holds rather than for Onshape's
`###name = #value`:

| Variable | Expression | What moved |
| -------- | ---------- | ---------- |
| `#stalk` | `#ball / 2` | new; the stud sketch typed `#ball / 4` for the stalk's radius |
| `#slit` | `1.6 mm` | unchanged |
| `#slit_in` | `sqrt((#ball / 2 + #fit) ^ 2 - (#ball / 3) ^ 2) - #wall / 2` | new; the sketch typed `#ball * 5 / 12`, which is 5 |
| `#slit_d` | `#grip + #ball / 3` | new; the extrude typed `#grip + #ball / 4`, which is 5.2205 |
| `#slit_out` | `#ball` | new; the sketch already wrote `#ball`, so this only names it |

Three dimensions moved with them: the collar circle is `(#ball / 2 + #wall) * 2` where it read
`#collar * 2`, the slit's inner end is `#slit_in`, and the slit's depth is `#slit_d`.

**`#collar` used to mean two things and the two have separated.** At draft9p3 the studio's `#collar`
was `#ball / 2 + #wall`, which came to 9.0, and `collar blank` also extruded `#collar` downward from
the ball's center, which the design source calls a length and also wanted at 9.0. One row was
carrying a radius and a length that happened to be equal. They are 7.8 and 10 now, so the sketch
writes the radius out and the extrude keeps the row, which is the length.

`socket connect to robot` infers `CENTER` where it inferred `CENTROID`, which is task #118.

### What #119 asked for, and what the tab needed

#119 named four tab variables draft9p1 has that draft9p3 does not: `#stalk`, `#stud_len`,
`#slit_in`, `#slit_out`. Three are added above. The fourth, `#stud_len`, is not, because draft9p3
had already replaced it with something better: the stud's top face is dimensioned `#stand` off the
ball's center, and `#stand` is defined as how far a ball center stands off the face it grows from.
A `#stud_len` row would be the same height under a second name. `#slit_d` takes its place in the
count, and the brief now says why neither `#stud_len` nor `#mouth` is a variable here.

### What it measures

Read off `bodydetails`, against `make_plans.py`.

| What | Read | Design source |
| ---- | ---- | ------------- |
| collar radius | 7.8 | `COLLAR_R` 7.8 |
| cavity radius | 6.08 | `BALL / 2 + FIT` 6.08 |
| socket base below the ball's center | 10 | `COLLAR_L` 10 |
| socket face above the ball's center | 2.2205 | `GRIP` 2.2205 |
| socket, base to face | 12.2205 | `COLLAR_PROUD` 12.2205 |
| mouth, where the cavity crosses the face | 11.32 | `MOUTH` 11.32 |
| slit walls | &#177;0.8 | `SLIT_W / 2` 0.8 |
| slit floor, below the face | 6.2205 | `SLIT_D` 6.2205 |
| slit inner end | 3.6789 | `SLIT_IN` 3.6789 |
| ball radius, stalk radius, ball center off the face | 6, 3, 10 | `BALL / 2`, `STALK / 2`, `STAND` |

The slit's inner end is inside the cavity at the depth the slit bottoms out: the cavity is 4.5789
across at that depth and the slit stops 0.9 inside it, so the cut opens into the cavity rather than
ending blind.

## B3 part one — the hinge's numbers

The tab declared twenty-one variables, each feature carrying Onshape's default
`###name = #value` and five of them shadowing a row the Variable Studio holds. The block is
rewritten: fifteen variables, each feature named for what it holds, and nothing declared here that
the studio declares.

| Variable | Expression | Value | Was |
| -------- | ---------- | ----- | --- |
| `#nose` | `#limbD / 2` | 12 | same |
| `#ear` | `(#limbD - #seat) / 2` | 6.85 | `(#limbD - #slot) / 2`, 6.4 |
| `#stub` | `4 mm` | 4 | same |
| `#stub_proud` | `1.30 mm` | 1.30 | 1.6 |
| `#bore_d` | `#stub + 0.4 mm` | 4.4 | `#pocket_d`, typed 4.4 |
| `#slit_h` | `4 mm` | 4 | new |
| `#leaf` | `(#blade - #slit_h) / 2` | 3 | new |
| `#rod_blade` | `#limbCenter - #stand - #tab_free` | 18 | `#rod` = `#ear`, 6.4, for both members |
| `#rod_fork` | `#limbCenter - #collar - #ear_free` | 17 | as above |
| `#teeth` | `24` | 24 | new; the two patterns typed 24 |
| `#valley_d` | `1.70 mm` | 1.70 | 2 |
| `#tooth_flat` | `0.8 mm` | 0.8 | new |
| `#cone_d` | `#valley_d + 2 * #gap` | 2.00 | new |
| `#tooth_proud` | `(#cone_d - #tooth_flat) / 2` | 0.60 | typed 1.2 |
| `#bump_r` | `#flat - 1 mm - #cone_d / 2` | 8.8387 | `(#teeth_ri + #teeth_r) / 2`, 9.6 |

Gone with them: `#limbD`, `#blade`, `#gap`, `#blade_out`, `#slot_deep` (all rows the studio holds),
`#slot` (the studio's `#seat` is the same rule at the settled width), `#blade_half` (the studio's
`#flat`, and the cut moves from the tongue's face to the ear's), `#teeth_ri`, `#teeth_r`,
`#bump_d`, `#valley_deep` and `#rim_break`.

Read back with `getVariable` in the tab and compared with `make_plans.py` by import: none disagree.

**#140 is answered by the design source rather than by a change.** It says `#blade_out` is typed
where the rule beside it derives it. `make_plans.py` types it on purpose and says why: two noses is
the shortest the joint can close at, and the nine millimeters past that are free length, which is
what makes the joint pressable by hand. A derived `#blade_out` would be the shortest joint that
closes rather than the one that works. It stays typed, in the Variable Studio, with the reason
recorded in the design source.

## The `/features` read is spent for the day, and the rest of Phase B needs another route

Partway through the variable rewrite, `GET /api/partstudios/.../features` began answering 429 with
`x-rate-limit-remaining: 0` and a retry-after of about 23 hours. That is the spent-quota mode
described in [`../../../../.parts/onshape.md`](../../../../.parts/onshape.md), not a burst block:
waiting does not shorten it.

What was established while working around it:

- **The limit is on that one route, not on the family's writes.** `POST .../features`,
  `POST .../features/rollback` and `POST .../features/featureid/{fid}` all still answer 200. So the
  build can still write features; it cannot read the ones it means to edit.
- `sketches`, `bodydetails`, `parts`, `variables`, `featurescript`, `featurespecs`,
  `currentmicroversion` and the element list all still answer, so every check Phase C runs is still
  available.
- `POST .../features` needs a `serializationVersion` and a `sourceMicroversion` that normally come
  from the read. The rollback route returns both, and `currentmicroversion` returns the second, so a
  feature can be added without reading the tab first.
- Reading `/features` at a version rather than the workspace is the same bucket, and
  `featurescriptrepresentation` answers 500 on this tab, so neither is a way round.

**The rate limit interrupted the variable rewrite between deleting and re-adding, so the tab spent a
few minutes rolled back to twelve features and building nothing.** It was recovered by rolling
forward and adding the last two variables from a template held on disk rather than read back.
`#tooth_proud` was refused once for reading `#cone_d` from a rollback position where `#cone_d` was
not yet active; a variable can only be added where the rows it reads are already in front of it,
which is the same rule the Variable Studio enforces.

The rest of Phase B edits parameters of features that already exist, and that needs the feature's
own JSON. The route left is the GUI, which the refusal itself names as not rate limited.

## The version prefix is not a second bucket, and the GUI is the way through

Onshape's own web client calls `/api/v14/...`, and the session this run drives calls `/api` with no
version at all, so the versioned path was worth one probe. It is the same bucket: `/api/features`
and `/api/v1` through `/api/v14` all answer 429 with `x-rate-limit-remaining: 0` for the same tab in
the same second. Watching the client load the tab settles the other half of it — the client fetches
`documents`, `elements` and `translatorFormats` over REST and nothing else. **The feature tree
arrives over a websocket, so there is no REST route the GUI knows and this run does not.**

`.parts/onshape.md` already says the GUI is not rate limited, and that is the route B3 took.

### Reading a dialog is not reading a field

An Onshape number field **shows the evaluated value when it is blurred and the stored expression
when it has focus.** Setting `blade arm`'s depth to `#rod_blade` and reading the field back gave
`18 mm`, which looks exactly like a variable that was silently replaced by its value; clicking into
the field gives `#rod_blade`. Every expression written in this phase was read back with the field
focused, and a read taken any other way proves nothing about what is stored.

The same is true of a dimension in a sketch. **Turn on `Show expressions`** in the sketch dialog and
each label carries its expression above its value, which is what made the wrong variable visible in
`blade profile` without opening anything.

## B3 part two — the hinge's geometry

The variable rewrite in part one deleted draft9p3's locals, so every feature that read one arrived
in this phase already red. **That is not damage; it is the work list.** Eleven features were in
error and each one names a number the settled design moved: `#blade_half`, `#bump_d`, `#slot`,
`#pocket_d`, `#rod` and `#valley_deep`.

| Feature | Was | Is |
|---|---|---|
| `blade profile` | sides `2 * #blade_half` | `2 * #flat` |
| `blade profile` | tab `#blade_out - #nose` | `#tab_free` |
| `blade bump outline` | `#bump_d` | `#cone_d` |
| `dome blade bump` | fillet on the bump crown | deleted |
| `blade bumps` | count 24, and named for it | `#teeth` |
| `blade arm` | depth `#rod`, offset `20 mm` | `#rod_blade`, `#tab_free` |
| `fork outline` | chord `#slot / 2` | `#seat / 2` |
| `fork blade top cut outline` | bottom `#slot / 2` | `#seat / 2` |
| `pocket axle sketch` | `#pocket_d` | `#bore_d` |
| `ear valley` | BLIND `#valley_deep`, offset `#slot / 2` | THROUGH_ALL, `#seat / 2` |
| `round ear valley rim` | fillet on the valley rim | deleted |
| `ear valleys` | count 24, and named for it | `#teeth` |
| `fork arm` | depth `#rod`, offset `21 mm` | `#rod_fork`, `#ear_free` |

**`#blade_half` was the whole point of the flat.** draft9p3 cut the blade's sides at
`sqrt(#nose^2 - (#blade / 2)^2)`, 10.9087, which flattens at the blade's own width. The settled
design flattens at the seat, `sqrt(#nose^2 - (#seat / 2)^2)`, 10.8387, so the tongue and the limb
lose their tops and bottoms on the same line.

**Deleting a feature that a pattern or a mirror lists leaves the list holding `Missing feature`.**
It is a warning, not an error, and the feature goes on building without it. `blade bumps` and
`mirror blade` each carried one after `dome blade bump` went, and `ear valleys` after
`round ear valley rim`. Dropping the chip is part of deleting the feature, not a separate repair.

**A count in a feature's name is a number with two homes.** `24 blade bumps` and `24 ear valleys`
were renamed `blade bumps` and `ear valleys` in the same edit that made the count `#teeth`, because
a name that says 24 while the model says `#teeth` goes stale the first time the row moves.

### #141 and #142 — the two connectors were placed by two different rules

Read side by side, the two are not variations on one rule; they are two rules:

- `fork to robot connector` sat on the centroid of the fork arm's end face and was then **moved**
  by `#nose - (#slot_deep - #nose + #rod)`.
- `blade to robot connector` sat on the centroid of the blade arm's end face with **no transform at
  all**, every translation zero.

draft9p3's `#rod` was `#ear`, 6.4 mm, so the fork's offset evaluated to −15.4 and meant nothing
under the settled arms. Both connectors now sit on their own arm's end face with no offset, which
is one rule. Both arms end 38 mm from their pin by construction — `#tab_free + #rod_blade` and
`#ear_free + #rod_fork` are both 38 — so the face is the same station on both members, and it is
`#collar` short of `#limbCenter` on both.

**This is a judgement, and the alternative is worth naming.** The connectors could instead sit at
the pin axis, which is what `#limbCenter` measures between. They do not, because the pin axis
already carries `axis for circular patterns` and because a connector belongs on a face that exists
rather than on a point in the air. If B4 and B5 find the limbs want the joint center instead, this
is one field on two features.

### What the parts say, measured rather than read off the dialogs

| Wanted | Where it came from | Blade | Fork |
|---|---|---|---|
| flats at ±`#flat` 10.8387 | `FLAT` | ±10.8387 | none, correctly |
| arm ends 38 from the pin | `#tab_free + #rod_blade`, `#ear_free + #rod_fork` | 38.0 | 38.0 |
| tab end at 20 | `#tab_free` | 20.0 | — |
| nose r12 | `#nose` | r12.0 | r12.0 |
| stub axle r2, proud to ±6.3 | `#stub`, `#blade / 2 + #stub_proud` | r2.0, ±6.3 | — |
| tongue faces at ±5 | `#blade / 2` | ±5.0 | — |
| ear inner faces at ±5.15 | `#seat / 2` | — | ±5.15 |
| valley r0.85 ×48 | `#valley_d`, `#teeth` on two ears | — | r0.85 ×48 |
| axle bore r2.2 | `#bore_d` | — | r2.2 ×2 |

**The fork is supposed to have no flats, and this run nearly cut some.** `make_plans.py` says the
flat "takes 1.16 off the rod's top and bottom and nothing at all off the fork", and `ear_path`
draws each ear "rounded on NOSE about the pin". The measured fork is round at Ø`#limbD` and is
right; the blade's flats are right; there was no work here, only a reading.

**The bumps are still cylinders.** 48 faces at r1.0 and no cone anywhere, where the design wants a
45° cone running `#cone_d` 2.00 down to `#tooth_flat` 0.8 over `#tooth_proud` 0.60. A 45° draft on
that extrude takes 0.6 off the radius and lands on 0.8 exactly, which is why the crown fillet was
deleted rather than resized.

## B3 part three — the bumps become cones, and the tongue gets its slit

**The draft ran the wrong way, and the face counts said so before the picture did.** Ticking
Draft on `blade bump` and typing 45° turned the 48 cylinders into 48 cones, and the part still
looked wrong in the numbers: one plane at y = ±5.6 of 160.35 mm², where 24 bump tops of
π × 0.4² = 0.5027 mm² each belong. A cone that widens from Ø2.00 at its root to Ø3.2 at its
crown is wider than the 2.314 mm of pitch between neighbors on a ring of `#bump_r` 8.8387, so
all 24 run into each other and their crowns merge into one annulus. The flip button beside the
angle fixes it: 48 cones, and 24 separate 0.5027 mm² tops on each face. Ø2.00 at the root,
45° over `#tooth_proud` 0.60, Ø0.80 flat on top; `#cone_d`, `#tooth_proud`, `#tooth_flat`.

**A merged ring and a ring of teeth have the same face count.** Both read `cone r 1.0 x48`.
Only the tops tell them apart, which is the second time this run that counting the small faces
caught what the radii agreed on.

**The relief slit was drawn, not posted.** `tools/onshape_session.py`'s `sketch` and `rect`
emit free geometry at typed coordinates with no constraints and no dimensions, which is the
thing `.parts/onshape.md` exists to forbid, so the slit went in through the sketcher: a corner
rectangle on the Right plane, then four dimensions off the origin — `#slit_h / 2` to each face,
`#tab_free` to the root, `#nose + 1 mm` past the tip so the slit opens at the tongue's end.
Four dimensions is what a rectangle with its corners tied and its sides horizontal and vertical
has left, so the sketch closes fully defined.

**`zoom_to` reports a scale the canvas is not drawing at.** The first rectangle came out two
thirds the size it was clicked at: `gui.project` was self-consistent at 14.2 px/mm while the
canvas was drawing at 21.6, so every click landed at two thirds of its intended distance from
the origin. The camera hook is not the authority on where a millimeter is. What works is
calibrating off the drawing itself: find the shaded sketch region in a screenshot, and with two
of its edges at known sketch coordinates the map is exact. Three cautions came with it. The
region takes two shades, paler outside the sketch plane's box and darker inside. The plane
box's own edge blanks one row of it where it crosses, and the constraint glyphs at a corner
blank twenty, so a strict run of dense rows stops short and puts the origin a millimeter and a
half out. And a two-pixel edge costs 4% across a four millimeter width and a tenth of that
across thirty, so the longer span carries the scale.

**The cut goes in after `blade arm` and before `fork outline`,** which is where `Roll to here`
on `blade arm` puts the rollback bar: that menu item includes the feature it is called on.
Through all, symmetric, Remove, scoped to the blade. It cuts the axle rather than the axle
bridging it, which is the whole point: two stubs, one rooted in each leaf, each free to move
with the leaf it stands on.

### What the hinge measures now

| What | Asked | Measured |
|---|---|---|
| bump root | `#cone_d` 2.00 | 48 cones, r 1.0 |
| bump crown | `#tooth_flat` 0.80 | 48 tops, 0.5027 mm² each |
| bump ring | `#bump_r` 8.8387 | cone axes at 8.8387 from the pin |
| bump height | `#tooth_proud` 0.60 | tops at y ±5.6 off faces at ±5.0 |
| valleys | `#valley_d` 1.70 | 48 cylinders, r 0.85 |
| leaf | `#leaf` 3.00 | tongue faces ±5.0, slit walls ±2.0 |
| slit | `#slit_h` 4.00 | walls at ±2.0 |
| slit root | `#tab_free` 20 | one face at z −20 |
| stub proud | `#stub_proud` 1.30 | each stub's cylinder is 16.336 mm² = 2π × 2 × 1.30 |
| stub | `#stub` 4.00 | two cylinders, r 2.0 |
| limb flat | `#flat` 10.8387 | four faces at x ±10.8387 |
| seat | `#seat` 10.30 | ear inner faces at y ±5.15 |
| arm ends | 38 from the pin | one face at z −38, one at z 38 |

**Two stubs, not three cylinders.** If the axle bridged the slit there would be a third
cylindrical face at r 2.0 running the slit's width. There are two, and each is 16.336 mm²,
which is `#stub_proud` exactly.

**The parts carry their names.** `Part 1` is the `blade` — the one with the cones and the slit;
`Part 2` is the `fork` — the one with the valleys and the ears.

## B4 — the upper limb

The limb is a socket, a rod and a fork, unioned into one part. Three things were wrong with it and
one thing the plan asked for does not exist here.

| Feature | Was | Is |
|---|---|---|
| `limb` | depth `#limbSeg - #collar - 21 mm` | `#limbCenter - #collar - #ear_free`, 17 |
| `elbow station` | a free sketch point on the Top plane | deleted |
| `elbow end` | two picks that landed on a tooth pocket | on the Origin, moved `-#limbCenter` |

### The limb's flats were being filled back in by the fork

`limb section` cuts the rod flat at ±`#flat`, and the union still measured round at Ø`#limbD`. The
cause was in the hinge, not in the limb: `fork arm outline` and `blade rod outline` were plain
Ø`#limbD` circles, and each arm covers exactly the length the limb's rod occupies, so the arm put
back what the section had taken off.

Both hinge sketches are now the same flatted section the limb and the tongue use: a circle
anchored to the sketch origin, two vertical chords each dimensioned `#flat` from it, and the two
outer caps trimmed away. Both close fully defined. The limb then measures one plane at x −10.8387
and one at x 10.8387, which is the rod's flat and the fork arm's flat merged into a single face.

**The fork's arm and the limb's rod occupy the same 17 mm.** Both are `#rod_fork` by definition, so
the union merges duplicate material there. That is inherited from draft9p3, it produces the correct
part, and changing it is a different piece of work.

### The elbow connector is placed by the rule that defines it

draft9p3 left the limb an `elbow station` sketch holding one free point near, but not on, the pin,
and no connector at the elbow at all. The guide's recipe for it takes two picks on the ears' holes
and puts the connector half way between them. Driven through the API that recipe picked a tooth
pocket rather than a bore, and the connector came out 3.44677 mm off the mid-plane in y, which
reads as a plausible connector and is not one.

`elbow end` is now a mate connector on the Origin's vertex, owned by the `u limb` body, attached to
its owner, and moved `-#limbCenter` along Z. That is the rule the design source states: joint
center to joint center is one number, and `#limbCenter` is that number. It needs no pick, it cannot
land on the wrong face, and driving `#limbCenter` moves both the fork and the connector together.

`shoulder end` is unchanged: on the Origin's vertex, which is where the socket's ball center sits.

Read back off the status bar with the selection cleared first, `shoulder end` is at
(0, 0, 0) and `elbow end` is at (0, 0, −48).

**A connector read is only trustworthy after the selection is cleared.** Onshape's status bar keeps
the previous selection's point until the new one resolves, so a click-then-read loop reports the
row above the one it names. Clearing first and waiting for the bar to go blank makes every read
agree with itself.

**A mate connector added to the hinge to carry the pin across was removed again.** Onshape's
Derived does carry mate connectors, and a connector on the hinge's own origin owned by the `fork`
body does come through `add fork` and does move with `move fork`. It cannot then be picked as
another connector's origin entity from either the graphics or the feature list, so it bought
nothing the Origin plus `-#limbCenter` does not buy, and the hinge is back to its two connectors.

### #125 is a torso item and this draft has no torso

`plan.md` assigns "the shoulder profile's missing projected edge" to B4. #125 is against tutorial 6,
where the **torso** grows its shoulders, and the tabs this document keeps are the joint and the two
limbs. The limb has no shoulder profile: `limb section` sits on the collar's end face, its circle is
anchored to the sketch origin, and there is no coincident edge to project because the collar is
r7.8 and the limb is r12. #125 stays open against the torso, wherever the torso is next built.

### What the upper limb measures

| What | Asked | Measured |
|---|---|---|
| ball center at the shoulder | `#ball / 2` 6, `#fit` 0.08 | sphere r 6.08 |
| collar | `COLLAR_R` 7.8 | cylinder r 7.8 |
| socket base below the ball's center | `#collar` 10 | one plane at z 10 |
| rod | `#rod_fork` 17 | faces at z −10 and z −27 |
| limb flat | `#flat` 10.8387 | one face at x −10.8387, one at x 10.8387 |
| nose | `#nose` 12 | cylinder r 12 |
| ear inner faces | `#seat / 2` 5.15 | y ±5.15 |
| axle bore | `#bore_d` 4.4 | two cylinders, r 2.2 |
| valleys | `#valley_d` 1.70, `#teeth` on two ears | 48 cylinders, r 0.85 |
| slit walls | `SLIT_W / 2` 0.8 | x and y at ±0.8 |
| joint center to joint center | `#limbCenter` 48 | `shoulder end` to `elbow end`, 48 |

No feature in the tab is flagged.

## B5 — the lower limb

The lower limb is a blade, a rod and a ball stud, unioned into one part. It is the tab that came
from draft9p1 rather than draft9p3, so every Derived in it pointed at the copies that came with it,
`hinge (1)` and `ball and socket (1)`, and the tab carried its own `#limbD` row.

| Feature | Was | Is |
|---|---|---|
| `add blade` | derived from `hinge (1)` | derived from this document's `hinge` |
| `add ball stud` | derived from `ball and socket (1)` | derived from this document's `ball and socket` |
| `limb` | a typed depth | `#limbCenter - #stand - #tab_free`, 18, started `#tab_free` from the pin |
| `limb section` | a round Ø`#limbD` circle | the same circle cut flat at ±`#flat` |
| `move ball stud` | a lost From connector | the stud's end face |
| `combine parts` | blade and rod | blade, rod and ball stud |
| `elbow end` | between two faces of `add blade` | on the Origin's vertex |
| `wrist end` | between two faces of `add ball stud` | on the Origin's vertex, moved `-#limbCenter` |
| `#limbD = 24 mm` | declared again inside the tab | deleted; `robot sizes` owns the name |
| the part | `Part 1` | `l limb` |

### Re-pointing a Derived clears what depends on it

Onshape's Derived takes a Part Studio and a list of bodies. Pointing it at a different studio
empties the body list first, so the feature reports Parts (0) until a body is picked again, and
every later feature that named one of the old bodies loses that query. In this tab that is the
Boolean and both connectors, and re-pointing the second Derived breaks the Boolean a second time.

The order that converges is: re-point `add blade`, repair the Boolean, set the rod's numbers, cut
`limb section` flat, re-point `add ball stud`, repair the transform, repair the Boolean again, then
rebuild the two connectors.

To re-point: click the Part Studio field, click the back arrow at the top of the panel that opens
to list every studio in the document, expand the studio you want, click the part, close the panel.

### The derived connector still cannot be picked, and the face it sits on can

`move ball stud` puts the ball stud on the rod's end by matching two mate connectors. Its To is
`mate for ball stud`, on the rod's end face. Its From should be `stud connect to robot`, which
`add ball stud` does carry across from `ball and socket`. As in B4, that connector cannot be picked
into another feature's field, from the feature list or from the graphics.

Two moves make the graphics pick reliable instead:

- Hide every body except the one being placed. The ball stud sits at the origin until it is moved,
  which is inside the blade, so nothing on it can be clicked while the blade is shown.
- Right-click the connector's row at its left edge and choose **Hide other mate connectors**. That
  leaves one triad on screen, so a pick near it cannot land on a different connector.

The pick then lands on the stud's end face and Onshape makes its own connector there, at the face
center with Z along the stud. That is what the named connector says as well: with the selection
cleared first, `stud connect to robot` reads (0, 0, −38) after the move, which is the same face
`mate for ball stud` sits on. The ball's center lands `#stand` beyond it at (0, 0, −48).

An earlier pick, taken with the blade still shown, grabbed the hinge's pin-axis connector and left
the stud lying along Y. Reading the body's bounding box is what caught it: y −0.325 to 15.675 for a
part that should measure ±6 about zero.

### The green check needs a second click after a field is typed into

Typing an expression into a number field and then clicking the check accepts the field, not the
feature; the dialog stays open. Clicking the check again accepts the feature. Two repairs of
`wrist end` looked like they had been accepted, and were then discarded by the next Escape, because
outside a sketch Escape throws away whatever dialog is open. Confirming that `#feature-dialog` is
gone before moving on is what makes the edit stick.

### Both limbs place their joint centers by the same rule

`elbow end` is a mate connector on the Origin's vertex, owned by the `l limb` body and attached to
its owner. `wrist end` is the same connector moved `-#limbCenter` along Z. Read back with the
selection cleared, they are at (0, 0, 0) and (0, 0, −48).

That is the rule the upper limb now uses, so a driven `#limbCenter` moves the ball, the elbow and
the wrist together on both parts, and joint center to joint center is one number twice.

### The copied tabs are gone

With nothing referencing them, `hinge (1)`, `ball and socket (1)` and `robot sizes (1)` were
deleted. Two Variable Studios declaring the same names is the worse half of that: a name typed into
a sketch has one meaning only while one table owns it. The document is now `robot sizes`,
`ball and socket`, `hinge`, `u limb` and `l limb`, and no feature in any of them is flagged.

### What the lower limb measures

| What | Asked | Measured |
|---|---|---|
| ball center at the wrist | `#ball / 2` 6 | sphere r 6.0 |
| stalk | `STALK` 6 | cylinder r 3.0 |
| ball center off the rod's end | `#stand` 10 | z −38 to z −48 |
| rod | `#rod_blade` 18 | faces at z −20 and z −38 |
| limb flat | `#flat` 10.8387 | one face at x −10.8387, one at x 10.8387 |
| nose | `#nose` 12 | cylinder r 12 |
| tongue faces | `#blade / 2` 5.0 | y ±5.0 |
| stub axles | `#stub` 4.0 | two cylinders, r 2.0 |
| stub proud of the tongue | `#stub_proud` 1.30 | y ±6.3 |
| relief slit walls | `SLIT / 2` 2.0 | y ±2.0 |
| teeth | `#cone_d` 2.00, `#teeth` on two faces | 48 cones, r 1.0 |
| tooth tops proud of the tongue | `#tooth_proud` 0.60 | y ±5.6, 24 a side |
| joint center to joint center | `#limbCenter` 48 | `elbow end` to `wrist end`, 48 |

## B6 and B7 — the two coupons

`ball with cylinder` and `socket with cylinder` are the two tabs a person prints when they want to
feel the joint before they print a robot. Each one is half of the joint on a handle. Neither tab
draws a joint: the joint arrives as a Derived part from `ball and socket`, so a change to the seat
or the slit reaches both coupons the moment the joint tab rebuilds.

Both tabs hold the same three features and nothing else:

- `add ball stud` or `add socket`, a Derived of one body from `ball and socket`, with the mate
  connectors and the properties carried across.
- `cylinder section`, a circle on the Top plane centered on the sketch origin, dimensioned
  `#limbD`, so the handle is exactly as thick as a limb.
- `cylinder`, a blind extrude of that circle, `#limbD / 2` deep, added to the derived body.

### The handle starts where the joint ends

The stud's flat face is `#stand` above the ball's center and the socket's base is `#collar` below
it, and `#collar` is `#stand` in `robot sizes`. So the two extrudes each begin at the joint's own
robot-side face, and each ends `#limbD / 2` past it:

| Coupon | Direction | Starting offset | Depth | Joint center to the far face |
| ------ | --------- | --------------- | ----- | ---------------------------- |
| `ball with cylinder` | +Z | `#stand` | `#limbD / 2` | 22 |
| `socket with cylinder` | −Z | `-#collar` | `#limbD / 2` | 22 |

The 22 is not typed anywhere. It is `#stand + #limbD / 2` on one coupon and `#collar + #limbD / 2`
on the other, and the two agree because the design source says a ball stands off its face by the
same distance the socket buries it. Drive `#torsoH` and both handles change together.

### The starting offset is signed, not flipped

An extrude's starting offset has no opposite-direction checkbox. It is measured along the sketch
normal, which is +Z here, whichever way the extrude itself runs. The socket's handle runs down, so
its offset is written `-#collar`. Read the pair of rows together and the sign is the only thing
that distinguishes them.

### Reversing an extrude is a click in the graphics

The dialog's `Direction` checkbox does not flip an extrude; it opens a box that wants a line or an
axis to extrude along. What flips it is the arrow the preview draws on the sketch plane. Clicking
that arrow turned the socket's handle downward and the merge scope filled itself in again.

### What the coupons measure

| What | Asked | `ball with cylinder` | `socket with cylinder` |
| ---- | ----- | -------------------- | ---------------------- |
| handle radius | `#limbD / 2` 12 | cylinder r 12 | cylinder r 12 |
| handle length | `#limbD / 2` 12 | z 10 to z 22 | z −10 to z −22 |
| joint center to the far face | 22 | z 0 to z 22 | z 0 to z −22 |
| ball, stalk | `#ball / 2` 6, `STALK / 2` 3 | sphere r 6, cylinder r 3 | |
| seat, collar | `#ball / 2 + #fit` 6.08, `COLLAR_R` 7.8 | | sphere r 6.08, cylinder r 7.8 |
| slit walls | `SLIT_W / 2` 0.8 | | x and y at &#177;0.8 |

Each tab holds one body, named for its tab, and no feature in either is flagged.

## Phase C — proving it

### A feature name is a template, which is why the tree drew `?`

Every variable in `hinge` was written over REST from a template captured out of `u limb`, and each
one arrived in the tree as `?` rather than as its name. The cause is not the write and not the
rename: **Onshape reads a feature's name as a template, in which `#value` names one of that
feature's own parameters.** The default name a variable feature carries is the literal string
`###name = #value`, which is why the tree usually shows `#nose = 12 mm`. Writing `#nose` as the name
asks for a parameter no variable feature has, so the tree renders the miss as `?`. A name with no
`#` in it is shown exactly as it is written, which is what the gate asks for.

The route to fixing it matters as much as the cause, because Onshape offers no way to rename a
variable feature by hand:

- Its context menu has `Edit…`, `Add selection to folder…`, `Suppress`, `Dynamic suppression`,
  `Add comment`, `Show dependencies…`, `Roll to here` and `Delete`, and no `Rename`.
- The dialog's edit-name pencil stays hidden on hover for a variable feature. A named sketch's
  dialog shows the same pencil on the same hover, so this is Onshape's answer rather than a driving
  fault.
- Typing a new **Name** in the dialog renames the *variable*, not the feature, and the row keeps
  whatever the feature's name template says.

So each variable feature was rebuilt from the template with its own `featureId` kept and posted to
`POST .../features/featureid/{fid}`, which the day's rate limit leaves open. The tree now reads the
plain words: `nose`, `ear`, `stub`, `stub_proud`, `bore_d`, `slit_h`, `leaf`, `rod_blade`,
`rod_fork`, `teeth`, `valley_d`, `tooth_flat`, `cone_d`, `tooth_proud`, `bump_r`.

### A variable holds its value in the field its own type names

The naming pass returned 200 on every feature and broke the teeth: `check.py` went from every row
agreeing to reporting two teeth where there should be forty-eight, on three tabs at once, and
`#teeth` read back as zero.

An `assignVariable` feature carries a separate quantity per type: `lengthValue`, `angleValue`,
`numberValue`, `anyValue`, and a `value` beside them. **Onshape reads only the one its
`variableType` names.** The rebuild had written the expression into `value` and `lengthValue`,
which is right for a length and leaves a count at the template's zero. `#teeth` is a count, so it
reads `numberValue`; writing there restored all three tabs.

The rule that comes out of it: a script that writes a variable writes its `variableType` and the
field that type names, and then reads the variable back through `getVariable` rather than trusting
the 200.

### The page never says whether a sketch is solved

The *fully defined* gate has no readable answer anywhere in the page. The sketch dialog carries
`Disable imprinting`, `Show constraints`, `Show expressions` and `Show errors`, and none of them
reports the solve. The dialog's own diagnostics button highlights the sketch in the graphics and
adds no text. So the gate is read the way a person reads it: each sketch is opened for edit and its
curves are looked at, because black is solved and blue is not.

Two things had to be true before that read means anything:

- **The default planes are hidden**, because their outlines are drawn in the same blue.
- **The pointer is parked clear of the geometry.** Zoom to fit leaves the pointer at the middle of
  the canvas, and whatever entity sits under it is drawn selected-orange, which hides the color the
  read is about. The first pass of the scan read `ear valley outline` as one orange circle for
  exactly this reason.

A sketch plane's own outline, the origin arrows and the variable markers put a few dozen blue pixels
on every frame, so the pixel count is triage and the frame is what is looked at.

### `Attachment: To selection` makes **Attach to** a required field

`socket connect to robot` was the one feature in the document that did not regenerate, and it failed
with *Failed to resolve mate connector coordinate system*. Its **Origin entity** held a face of
`collar blank` and read as complete. The empty field was **Attach to**, three fields further down,
which the dialog draws in pink.

A mate connector set to `Attachment: To selection` resolves its coordinate system from the **Attach
to** query; **Origin entity** only says where on that geometry it sits. With **Attach to** empty
there is nothing to resolve, however good the origin looks. The repair cleared both chips and picked
the socket's own end face into each, which puts the connector at (0, 0, -10) on the axis with z
pointing out of the part, as the plan's connector row asks.

### Onshape selects what the pointer hovered, so a click has to be moved to first

`page.mouse.click(x, y)` on the 3D canvas selects nothing, whether or not a query field has focus.
Onshape decides what is under the cursor from its own hover, and a click delivered at coordinates
the pointer never travelled through arrives over nothing.

`gui.pick` moves the mouse to the point, waits for the highlight, clicks, and reads the
selected-pixel count back to confirm the pick landed. Every geometry pick in this run goes through
it. A bare click is what left the mate connector repair's first pass with two empty fields and a
still-red row, with no error to say so.

### The tree reports a failed feature in a CSS class and nowhere else

`check.py` measured every geometry number in the six tabs and printed *every row agrees* while
`socket connect to robot` was red. A mate connector adds no material, so its failure moves no
distance, no face count and no bounding box: a measurement pass cannot see it.

The tree's row carries `ns-list-item-error` in its `className`, and a warning row carries
`ns-list-item-warning`. That class is the only textual place the state appears; the row's text and
its `title` attribute say nothing about it, and the color is the only thing a person sees. So
feature health is read by scanning every row's class in every tab, as a pass of its own beside the
measurements.

### What each Phase C gate was read from

- **The geometry agrees with the design source.** `check.py` imports `make_plans.py` and measures
  the document through `bodydetails`, `parts` and `boundingboxes`. It ends *every row agrees*: 13
  rows on `ball and socket`, 32 on `hinge`, 26 on `u limb`, 25 on `l limb`, and 6 on each coupon.
- **Every sketch reports fully defined.** All 17 sketches were opened for edit and looked at, one
  frame each, because the page carries no readable answer.
- **No reference leaves the document.** `GET .../externalreferences` returns an empty
  `elementExternalReferences` and an empty `elementRevisionReferences` for all seven tabs, so
  nothing names another document and nothing names a version.
- **No feature carries a default name, and none is in error.** The tree row list for each tab was
  read by name, and each row's `className` was read for `ns-list-item-error`.
- **The model was looked at.** Twenty-four frames, four orientations of each of the six studios.

### One driving dimension moves the whole robot, and two numbers stay put on purpose

`#torsoH` was driven from 96 mm to 120 mm and back, and `#limbD` from `#torsoH / 4` to a literal
30 mm and back. All six studios rebuilt at both sizes with the same part names and the same face
count per part, and `statecmp.py` reported `differences: 0` on the way back; every bounding box came
back to the number it started from.

Three things scale by less than the driving number does, and each is the design saying so rather
than a broken relation:

- **The hinge grows 1.2998 across x where it grows 1.25 across y**, because the flat is
  `sqrt((#limbD / 2) ^ 2 - (#seat / 2) ^ 2)` and `#seat` is a printer clearance that does not scale
  with the robot.
- **The limbs keep their length**, because joint center to joint center is `#limbCenter`, which is
  a free 48 mm and not a fraction of `#torsoH`.
- **Driving `#limbD` alone leaves `ball and socket` alone**, because that joint is sized by `#ball`.
  The limb it lives in changes around it, which is what a joint sized by how the plastic bends
  should do.
