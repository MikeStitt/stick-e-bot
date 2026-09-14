# Run 4 — build notes

Run 3's documents copied to run 4, measured, and assembled. **No part geometry was changed.**
Every sketch and every extrude in run 4 is run 3's; the only features added are the ten mate
connectors the assembly needed. Where the measurements disagree with the briefs — in seven
places — the gap was written to [`parked.md`](parked.md) rather than modeled out.

So run 4 answers "do these parts assemble" and not "do these parts match the briefs". The second
question is still open, and three of the seven are ordinary modeling work rather than things that
could not be resolved: the shoulder boss, the rebalanced hinge, and the foot's relief slits.

## The copy

Nine documents copied from run 3 in 22 seconds through
`POST /documents/{did}/workspaces/{wid}/copy`, body
`{"newName", "isPublic": false, "ownerId": <company>, "ownerTypeIndex": 1}`. Every feature came
across `OK`. **Element ids change in the copy** — the run 3 ids are useless against the run 4
documents, which is why [`run4-documents.json`](run4-documents.json) exists.

Six of the nine are robot parts. `ball-socket`, `hinge` and `lesson` are studies, and nothing in
the assembly comes from them.

## Measuring a part from the API

`POST /partstudios/d/{d}/w/{w}/e/{e}/featurescript` runs a script and hands back the value, which
is how every number below was taken. Two things it will not accept, both found the hard way:

- **No `FeatureScript NNNN;` version header and no `import`.** The body is a bare function
  expression, `function(context is Context, queries is map) { ... }`. A version header comes back
  as `extraneous input 'FeatureScript'`.
- **No `try silent(...)`.** It fails to parse. Branch on the type instead —
  `if (sd is Plane) ... else if (sd is Cylinder) ... else continue`.

One more that costs an hour if you get it wrong: **`Sphere` carries `coordSystem`, not `center`.**
`sd.center` throws, and the endpoint answers `200` with `result: null` and an empty `notices`
array, so it looks like the query found nothing rather than like an error.

The reply is a nested `BTFSValue` tree, not JSON — a map is a list of `{key, value}` pairs under
`BTFSValueMap`. [`../../../instructions/robot-guide/`](../../../instructions/robot-guide/) has no
helper for this; `fslib.unwrap` in the scratchpad does it in nine lines.

## What the six parts actually are

Measured, in each part's own frame. Balls are spheres of r 3.000; sockets are cavities of r 3.200.

| Part | Joints, in local coordinates |
| ---- | ---------------------------- |
| Torso | balls at (±23, 0, +24) shoulders, (±12, 0, −29) hips, (0, 0, +29) neck |
| Head | socket center (0, 0, −16.65), mouth plane z = −18, face on −Y |
| Upper arm / thigh | socket center (0, 0, 0), mouth opens +Z; hinge pin at z = −24 |
| Forearm and shin | hinge pin at z = 0; ball at (0, 0, −24) |
| Hand | socket center (0, 0, 0); clip r 5.0 and Ø3.3 bar bore on x = +3 |
| Foot | socket center (0, 0, 0); plate runs x −16 … +32, y ±12 |

**The socket sits 1.35 behind its mouth, not on it.** Every socketed part's bounding box ends
1.35 above the cavity center, which is `#grip`. That single number is what lets a socket be placed
in the assembly: the ball center and the cavity center are the same point, so a socket lands by
putting its own origin on the ball.

The limb collar measures **5.5 long in four tabs** — circumference 26.3 of a possible 29.5, and the
missing 3.2 is four slits of 0.8. The foot's collar is **one face, 7.35 long, with no slits at
all**. See [`parked.md`](parked.md).

The detent is real and it is not what the brief describes: **13 valleys of r 0.5 at 15° spacing on
a radius of 4.800**, cut 0.45 into each face of the blade. The x stations came back as 4.80, 4.64,
4.16, 3.39, 2.40, 1.24, 0.00 and their mirrors, which is `4.8·cos θ` for θ = 0…90 in fifteens.

## The assembly

`robot-run4-assembly`, document `db263a6925572ace7fe54b13`, assembly element
`850c5c3f0005e18b578f3705`. Fourteen instances: one torso, one head, four `Upper arm / thigh`,
four `Forearm and shin`, two hands, two feet. The limbs are modeled once and inserted four times,
which is the thing the part breakdown exists to buy.

Cross-document instances need a **version**, not a workspace, so each of the six part documents
carries a version named `run4-parts` and the assembly cites it. That is the Constitution's rule
and the API enforces it anyway.

Building it took two calls per instance: `POST .../instances` with
`{documentId, versionId, elementId, partId, isAssembly: false, isWholePartStudio: false}`, then
`POST .../occurrencetransforms` with a 16-element row-major matrix. **Translations in that matrix
are meters**, and the rotation block is local-to-global.

### Where each instance goes

Every joint is at zero — each limb runs straight out along the stalk it hangs from. Nothing is
posed, because a zero pose is the one a reader can check against arithmetic.

| Instance | Rotation | Origin (mm) |
| -------- | -------- | ----------- |
| Torso | — | (0, 0, 0) |
| Head | — | (0, 0, +45.65) |
| Thigh R / L | — | (±12, 0, −29) |
| Shin R / L | — | (±12, 0, −53) |
| Foot R / L | −90° about Z | (±12, 0, −77) |
| Upper arm R / L | ∓90° about Y | (±23, 0, +24) |
| Forearm R / L | ∓90° about Y | (±47, 0, +24) |
| Hand R / L | ∓90° about Y | (±71, 0, +24) |

The feet turn because the foot is modeled along its own +X and the robot faces −Y. The arms turn
because the shoulder stalk leaves sideways, so the arm's +Z has to point back down its own stalk.

### The stations check

Assembly bounding box, measured: **x ±83, y −32 … +16, z −89 … +63.65.**

Height is **152.65 mm**, which is the number [`torso.md`](../../build-briefs/torso.md) predicts by
adding stations up, taken here from fourteen independently built solids that were never told what
the total should be. Ground falls at z = −89 and the top of the head at +63.65.

Arm span is 166, wider than the figure is tall. That is a consequence of the T pose, not of the
design — the r2 sheet poses the arms in a plane parallel to the front.

## The mates

The document carries two assemblies. **`Robot mated` is the one to use**; `Robot` is the first
pass, placed by transforms alone, kept because the commit that reached it cites its id.

Ten mate connectors carry the joints, and four of the six parts needed no offset at all because
the joint already sits on the part studio origin. The rest are the origin plus a translation:

| Part | Connectors |
| ---- | ---------- |
| Torso | `Neck`, `Shoulder R`, `Shoulder L`, `Hip R`, `Hip L` |
| Head | `Neck socket` |
| Upper arm / thigh | `Socket`, `Hinge` |
| Forearm and shin | `Hinge`, `Ball` |
| Hand, Foot | `Socket` |

Onshape reports every one of them back at the coordinate it was asked for, which is worth reading
off `GET /assemblies/...?includeMateFeatures=true&includeMateConnectors=true` — `parts[].mateConnectors`
gives each connector's full coordinate system, so the placement can be checked without opening
anything.

Building a connector through the API has one trap. The obvious construction — select the solid,
infer `PART_ORIGIN` — posts **200 and then sits at `ERROR`**, with an empty `notices` array and
nothing in `featureStates` beyond the word. What works is the origin vertex with `POINT`
inference, owned by and attached to the solid:

```
originQuery          qCreatedBy(makeId("Origin"), EntityType.VERTEX)
entityInferenceType  POINT
requireOwnerPart     true,  ownerPart  = the solid
attachmentOption     TO_SELECTION,  attachTo = the solid
transform            true, then translationX/Y/Z and rotationType/rotation
```

The enum names are not guessable and must come from `GET .../featurespecs`:
`OriginCreationType`, `EntityInferenceType`, `RotationType`. A wrong one answers
`400 … does not match its feature spec`, which at least fails loudly.

### The mate query, which is the part worth writing down

An assembly mate is a `BTMMate-64` with a `mateType` enum and a `mateConnectorsQuery` holding two
queries. **The query type is `BTMPartStudioMateConnectorQuery-1324`**, and it addresses a
connector by the instance path plus the connector's part studio feature id:

```json
{"btType": "BTMPartStudioMateConnectorQuery-1324",
 "path": ["<assembly instance id>"],
 "featureId": "<mate connector feature id in the part studio>",
 "queryData": ""}
```

Four other encodings were tried first and all four failed the same silent way: the feature posts
`200`, sits at `ERROR`, and comes back with `matedEntities: []`. The reason is worth keeping,
because it is a general technique — **the server silently drops fields it does not recognise**, so
posting one query stuffed with every candidate field name and reading back which one survived
normalization identified `entityQuery` in a single call. That turned out to be a real field of the
wrong query type, which is why even the surviving field did not bind.

What settled it was building one mate by hand in the UI and reading its JSON back. Expanding an
instance in the Instances list shows its part studio mate connectors by name, so both sides can be
picked from the tree without clicking a triad in the graphics area.

`mateType` takes `BALL` and `REVOLUTE`; its `enumName` really is the display string `Mate type`,
spaces and all.

### What was built

Thirteen mates, all `OK`: **nine `BALL`** — neck, two shoulders, two hips, two wrists, two ankles —
and **four `REVOLUTE`** at the elbows and knees. That is the joint count the design has always
claimed, now solved rather than asserted.

The hinge connectors turn 90° about X so their Z lies along the pin, which runs across the limb
rather than along it. Both sides of each hinge use the same rotation, so superimposing them leaves
the shin's local −Z running on down the thigh's local −Z, and the limb comes out straight.

**The bounding box after mating is identical to the bounding box before it** — x ±83, y −32 … +16,
z −89 … +63.65. The mates found every joint already coincident and moved nothing, which is the
check that the connectors and the transforms agree.

Nothing is fixed to the origin. The robot holds itself together and can be dragged as a unit,
which is what a posable figure wants.

## Screenshots

In [`shots/`](shots/). The four orthographic views come from
`GET /assemblies/.../shadedviews?viewMatrix=front&outputHeight=900&outputWidth=700&pixelSize=0&edges=show`,
which renders server-side with no browser chrome in the frame and is worth using in place of a
screen grab wherever a clean view is wanted.
