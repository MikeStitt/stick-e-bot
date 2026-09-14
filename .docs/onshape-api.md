# Onshape REST API — verified encodings and traps

Everything here was performed against the live API during this session and observed to work, unless
explicitly marked otherwise. Onshape's own docs and any recalled knowledge should lose to this file,
because this file was measured.

Standard library version in use at the time: **FeatureScript 3044**.

## Authentication

Cookie auth alone returns **401 on writes** (reads are fine). Onshape's own web client echoes the
`XSRF-TOKEN` cookie back as a header, and so must we:

```js
const xsrf = document.cookie.match(/(?:^|;\s*)XSRF-TOKEN=([^;]+)/);
if (xsrf) headers['X-XSRF-TOKEN'] = decodeURIComponent(xsrf[1]);
```

**Match it; do not split it.** The token is base64 and usually ends in `=` or `==` padding, so
`cookie.split('=')[1]` hands back a truncated token — and a truncated token is refused exactly
like no token at all, with a **401 that reads as "cookie auth is read-only"**. Run 3 lost time to
this and so did the head-collar run, which concluded from it that versions cannot be created over
REST. They can.

See [`browser-access.md`](browser-access.md) for how the session is obtained.

## Rate limits — the failure that looks like everything else

Building features in a tight loop earns a **429 "Too many requests"**, and it is worth
knowing four things about it before losing an afternoon:

- **It is per endpoint family, not per document and not account-wide.** Every Part Studio's
  `/features` refuses at once, so it is easy to read as account-wide; but on 2026-08-27, with
  `/features` at zero, `bodydetails`, `parts`, `boundingboxes`, `assemblies`, `variables` and
  `sketches?includeGeometry=true` each still had hundreds to thousands of calls left, and
  `/api/users/sessioninfo` answered throughout. A read-back written against the geometry
  endpoints survives a block that stops the feature endpoint.
- **There are two lengths, and only the response tells them apart.** A burst of writes earns a
  block clocked at 83 seconds once and at over five minutes another time. A spent daily quota is
  a different thing: `/features` answered `retry-after: 67201` beside `x-rate-limit-remaining: 0`,
  which is 18 hours 40 minutes, and that counter runs down with the clock rather than resetting
  when the calls stop. **Read `retry-after` before deciding to wait.** No ladder of retries
  reaches the end of the long one, and the answer to it is a different route rather than a
  longer delay.
- **Unhandled, it does not look like rate limiting.** A `DELETE` quietly does nothing. A
  feature list comes back as an error object with no `features` key, which reads as a
  `KeyError` somewhere unrelated. The next GUI action then fails on a stale assumption. Two
  separate "modeling bugs" in this project turned out to be this.
- **The GUI is not rate limited.** draft9p1p1 read every expression it needed out of the feature
  tree and the dialogs, and deleted three features by right-click, while `/features` was refusing.
- **`x-rate-limit-remaining` comes back on every response, not only on a 429**, so the budget can
  be watched rather than discovered. Measured together on 2026-08-28, with `features` refusing:

  | endpoint | status | remaining |
  | --- | --- | --- |
  | `/api/users/sessioninfo` | 200 | 2950, and it decrements per call |
  | `.../partstudios/…/features` | **429**, `retry-after: 522` | **0** |
  | `.../partstudios/…/bodydetails` | 200 | 486 |
  | `/api/parts/…` | 200 | 500 |
  | `/api/assemblies/…` | 200 | 1000 |

  The families have separate budgets of different sizes, which is the per-family limit seen from
  the other side. The 522 seconds is also worth noting on its own: the wait is whatever the server
  says it is, and reading the number beats knowing which limiter answered.

[`../tools/onshape_session.py`](../tools/onshape_session.py)'s `api()` does this: it keeps the
response headers, honors `retry-after` when the wait is short enough to be worth taking, and
raises `RateLimited` immediately rather than spending a ladder to discover the answer is hours.
Put a few hundred milliseconds between feature writes, with `pace()`, so it never arrives at all.

## Discovering the truth instead of guessing

Three endpoints removed nearly all guesswork. Reach for these first.

- **`GET /api/partstudios/d/{d}/w/{w}/e/{e}/featurespecs`** — the authoritative parameter list for
  every feature type (92 of them), with parameter IDs and enum names. This is how the `extrude`,
  `revolve` and `fillet` parameters below were obtained.
- **`POST /api/partstudios/d/{d}/w/{w}/e/{e}/featurescript`** — evaluate arbitrary FeatureScript
  against the model. Returns `{result, notices}`; the notices carry real error text with line
  numbers. Invaluable both for debugging and for resolving geometry IDs.
- **Build one feature in the GUI, then `GET .../features` and read the JSON.** This is the fastest
  way to learn an encoding you cannot guess. It is how `sketchPlane` and the sketch-region query
  below were found, after guessed forms failed.

The standard library source is readable too — document `12312312345abcabcabcdeff`, version
`e11b9ebdf448b3ebc502b5dc`, `primitives.fs` element `dc9e71d454d34142ae66df18`.

## Geometry references

Geometry is referenced by short deterministic **`geometryIds`**, not by FeatureScript query strings.
A `queryString` on `BTMIndividualQuery` was silently ignored — the feature failed with
"1 missing selection".

```js
// a plane or a face
{ type: 138, typeName: 'BTMIndividualQuery', message: { geometryIds: ['JCC'], hasUserCode: false } }

// every closed region of a sketch — what the GUI writes for "Faces of Sketch N"
{ type: 140, typeName: 'BTMIndividualSketchRegionQuery',
  message: { featureId: '<sketch featureId>', filterInnerLoops: true } }
```

**Front plane = `JCC`** (verified). Top and Right plane geometry IDs were never checked. Note that
`makeId("Front")`, `makeId("Top")`, `makeId("Right")` and `makeId("Origin")` all resolve inside
FeatureScript — that is a different ID space from `geometryIds`.

### Resolving a face or edge you cannot name

Evaluate a FeatureScript query and read `transientId` off the result — that string is usable
directly as a `geometryId`:

```
var pl = try silent(evPlane(context, { "face" : f }));   // undefined for non-planar faces
return best.transientId;
```

**`qEverything(EntityType.FACE)` includes sketch faces**, which will happily out-rank the solid you
wanted when both have the same area. Filter first:

```
qOwnedByBody(qBodyType(qEverything(EntityType.BODY), BodyType.SOLID), EntityType.FACE)
```

## Sketches

`BTMSketch` is type **151**, `featureType: "newSketch"`. **Sketch geometry is in meters**, while
dialog values are expressions like `"3 in"`.

| Entity | Types                                                        | Notes                                    |
| ------ | ------------------------------------------------------------ | ---------------------------------------- |
| Line   | `BTMSketchCurveSegment` 155 + `BTCurveGeometryLine` 117       | `startParam: 0`, `endParam: length`      |
| Circle | `BTMSketchCurve` 4 + `BTCurveGeometryCircle` 115              | `xCenter`, `yCenter`, `radius`           |
| Arc    | `BTMSketchCurveSegment` 155 + `BTCurveGeometryCircle` 115     | `startParam`/`endParam` are **radians**  |

### Sketch constraints and dimensions

`BTMSketchConstraint` is type **2**. Entities are named by string, not by query, so a constraint
refers to `"<entityId>.bottom"` or `"<entityId>.bottom.start"`. Onshape's own corner-rectangle
tool names the four segments `.top`, `.bottom`, `.left`, `.right` and their endpoints `.start`
and `.end`; following that convention makes hand-built sketches readable.

```js
{ type: 2, typeName: 'BTMSketchConstraint',
  message: { constraintType: 'COINCIDENT', entityId: 'r1.corner0', parameters: [
    { type: 149, typeName: 'BTMParameterString',
      message: { parameterId: 'localFirst',  value: 'r1.bottom.start' } },
    { type: 149, typeName: 'BTMParameterString',
      message: { parameterId: 'localSecond', value: 'r1.left.start' } } ] } }
```

Drawing one corner rectangle in the GUI emits eight constraints on its own: `PERPENDICULAR`,
`PARALLEL` ×2, `HORIZONTAL`, and `COINCIDENT` ×4 (one per corner). Those take only `localFirst`
and, where a second entity is involved, `localSecond`.

**A dimension on a single line is `LENGTH`, not `DISTANCE`:**

| Parameter       | Type                 | Value                        |
| --------------- | -------------------- | ---------------------------- |
| `localFirst`    | `BTMParameterString` 149 | `"r1.bottom"`            |
| `direction`     | `BTMParameterEnum` 145   | `DimensionDirection.MINIMUM` |
| `length`        | `BTMParameterQuantity` 147 | `"8 in"`                   |
| `alignment`     | `BTMParameterEnum` 145   | `DimensionAlignment.ALIGNED` |
| `labelRatio`    | `BTMParameterQuantity` 147 | `"0.25"` — where the label sits |
| `labelDistance` | `BTMParameterQuantity` 147 | meters, label stand-off     |

`ANGLE` between a sketch line and a default plane mixes the two reference styles: `externalFirst`
is a `BTMParameterQueryList` of `geometryIds`, while `localSecond` is a plain string. Expect that
pattern wherever a constraint reaches outside the sketch.

This is the encoding that had been blocking every fully defined sketch. It was read back off a
rectangle drawn and dimensioned by driving the GUI, which remains the only reliable way to learn
one of these.

### Sketch-on-a-face coordinates

For the body's front face (normal −Y), sketch-local `(u, v)` mapped **directly to world (X, Z)**.
The face's plane origin — which `evPlane` reports as sitting at the face centroid height — is *not*
applied. Assuming it was cost a full rebuild: everything on the face landed 8 inches low, and the
smile silently cut empty air.

Do not assume this generalizes. Measure the mapping with a probe sketch before trusting it on a
different face.

## Features

Parameter wrappers: `BTMParameterEnum` 145, `BTMParameterBoolean` 144, `BTMParameterQuantity` 147,
`BTMParameterQueryList` 148. Features themselves are `BTMFeature` 134.

| Feature   | Parameters used                                                                       |
| --------- | -------------------------------------------------------------------------------------- |
| `extrude` | `bodyType`(ExtendedToolBodyType) `operationType`(NewBodyOperationType) `entities` `endBound`(BoundingType=BLIND) `depth` `symmetric` `oppositeDirection` `defaultScope` |
| `revolve` | `bodyType` `operationType` `entities` `axis` `fullRevolve` `defaultScope`              |
| `fillet`  | `filletType`(FilletType=EDGE) `entities` `crossSection`(FilletCrossSection=CIRCULAR) `radius` |

### Two traps that cost the most time

**`defaultScope: true` is required on every Add and Remove.** Without it the feature fails with
"No merge scope selected" — but *not necessarily straight away*. Two of four merge operations
regenerated fine at creation and only broke later, when a metadata write triggered a rebuild.

**An extrude started from a face defaults to pointing outward**, away from the material. A `Remove`
from a face therefore cuts empty air by default and reports `INFO`, not `ERROR`. Set
`oppositeDirection: true` to cut inward.

## Units are not in the API

A new document is in **inches**, and the unit system lives on the *element*
(`lengthUnits`, `areaUnits`, …), visible in `GET /api/documents/d/{d}/w/{w}/elements`.

It is **read-only there**. `POST` to the elements, partstudios and documents endpoints all
answer 405 or 404. The only way found to change it is the GUI: the **☰ menu** beside the
document name → **Workspace units…**.

That matters for a millimeter course, because it has to be step zero of the first lesson and
it cannot be scripted into a starting state. Typing explicit units in a dimension (`24 mm`)
works regardless and is the safe way to build a reference model in a document whose units
have not been set.

The measurement readout follows the document units too, so a script that checks a selection by
reading `Area: 1728.0mm2` will silently fail against an inch document.

## Part metadata

`GET`/`POST /api/metadata/d/{d}/w/{w}/e/{e}/p/{partId}`.

| Property   | ID                          | Value shape                                              |
| ---------- | --------------------------- | -------------------------------------------------------- |
| Name       | `57f3fb8efa3416c06701d60d`  | string                                                    |
| Appearance | `57f3fb8efa3416c06701d60c`  | `{color: {red, green, blue}, opacity: 255, isGenerated: false}` |

**Part IDs are not stable across metadata writes.** A first naming pass wrote to IDs that no longer
existed; the calls returned `200` and four parts silently kept their default names. Re-resolve part
IDs immediately before every write, and read the result back.

## Rendering

`GET /api/partstudios/d/{d}/w/{w}/e/{e}/shadedviews` with
`?viewMatrix=front|isometric&outputHeight=800&outputWidth=800&pixelSize=0&edges=show` returns
`{images: [<base64 png>]}`. Server-side, no browser, no UI chrome — the fastest way to actually look
at what you built.

## Derived (`importDerived`) — the namespace is not the hard part

Inserting another document's parts. Learned 2026-08-11 by building one in the GUI and reading
the JSON, after four API attempts failed.

```json
{"type": 3302, "typeName": "BTMParameterReferencePartStudio", "message": {
  "parameterId": "partStudio",
  "namespace": "d<did>::v<versionId>::e<elementId>::m<microversionId>",
  "partQuery": {"type": 148, "typeName": "BTMParameterQueryList", "message": {
     "parameterId": "partQuery",
     "queries": [{"type": 138, "typeName": "BTMIndividualQuery",
                  "message": {"geometryIds": ["JHD"]}}]}}}}
```

- **The namespace form was right on the first try; the empty `partQuery` was the failure.**
  Derived will not "just take everything" — every part must be named by its **`geometryId`**,
  the same lesson as *Geometry references* above, in a new place. An empty `queries` array
  gives `featureStatus: ERROR` with no message at all.
- The **microversion is required**; `d::v::e` alone fails.
- Get the microversion from `GET /api/documents/d/{d}/v/{v}/elements` → `microversionId`.
- Placement defaults to **Base origin**, so derived parts land on the origin and will sit on
  top of whatever is already there. Add a transform if you want them beside it.
- The picker warns *"N changes since the last version"* when the source workspace has moved on
  past the version you are deriving — a useful reminder that a version is the right thing to
  cite (Branch Policy) and that the workspace is not.

## FeatureScript notes

- **`fSphere` takes a `Query` for `center`** (a vertex you would click), not a vector. Use
  **`opSphere`**, which takes a plain vector center and a radius.
- A custom feature's `namespace` (`e<elementId>::m<microversionId>`) **pins a microversion**.
  Editing the Feature Studio orphans an already-placed feature; it must be deleted and re-added
  against the current namespace from `featurespecs`.
- A newly created Feature Studio is pre-populated with the correct `FeatureScript <version>;`
  header — read it rather than guessing the current standard library version.
