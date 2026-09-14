# draft9p1p6 build notes

What the build actually did, including where it departed from [`plan.md`](plan.md). Ids are read off
Onshape, not transcribed.

## Where the work is

| What | Id |
| ---- | -- |
| document `stickbot-draft9p1p6` | `500752af84dc92deea53f9e4` |
| workspace | `f30bf96cfeece59f61e0e7b2` |

The live workspace is
<https://cad.onshape.com/documents/500752af84dc92deea53f9e4/w/f30bf96cfeece59f61e0e7b2>.

| Tab | Element | Type |
| --- | ------- | ---- |
| `robot sizes` | `5e9a0328a109ff92f5f6e9aa` | Variable Studio |
| `ball and socket` | `88ea6b759912b789d6de4647` | Part Studio |
| `hinge` | `62fca6aa5a67b51adcb2318c` | Part Studio |
| `u limb` | `f3f8362fd5e9f31ee2fa5eb2` | Part Studio |
| `l limb` | `261b7ee66567bab16d145c83` | Part Studio |
| `ball with cylinder` | `a1992995b5a775f59d76d561` | Part Studio |
| `socket with cylinder` | `e7dca601f00ea49c3f212d0f` | Part Studio |

## C1 — the copy, and the route that answers it

`plan.md` asks for a copy of draft9p1p5's named version `F done - Phase F proved`. Onshape still has
no version-copy route, so this is again a workspace copy, and draft9p1p5's shortcut for proving the
two are the same does not carry: its workspace microversion and its version's microversion are
different strings. Mike printed from that version, so the question is real rather than procedural.

The gate was moved off the microversion and onto the model. Four reads of draft9p1p5's workspace and
of its version were compared: the Variable Studio's rows and expressions, each tab's feature names
and types in order, every body's face census by surface type, and every feature's status. All four
agree. The only difference anywhere is a `namespace` field on four derive features, which pins the
version of `ball and socket` those derives read; the geometry they build is the same either way.

**The copy route recorded in draft9p1p5's notes answers 404 now.**
`POST /api/documents/d/{did}/workspaces/{wid}/copy` is refused;
`POST /api/documents/{did}/workspaces/{wid}/copy`, without the `d/`, answers 200 with the document
and workspace ids above. Three shapes were tried before one answered, which is worth writing down
because the failure is a plain 404 and reads as a missing document rather than a missing `d`.

`stickbot-draft9p1p5` is untouched and stays the recovery point, and it is the version Mike's
printed parts came from.

## C2 — which references leave the document

None. `GET /documents/d/{did}/w/{wid}/externalreferences` answers 200 with an empty list for all
seven elements under both `elementExternalReferences` and `elementRevisionReferences`,
`elementToHasWorkspaceReferences` is `false` for all seven, the one document it names is
`stickbot-draft9p1p6` and the one version is this document's own `Start`. Separately, every feature
of all six Part Studios was fetched and its JSON searched for draft9p1p5's document id, its
workspace id and its seven element ids. No hit.

## D — five variable expressions, and four of them went into a parameter the model does not read

The hinge is parameterized well enough that the whole of Phase D is five expressions. Both wedge
outline sketches dimension off `#ring_in`, `#ring_out` and `#wedge_w`; both circular patterns count
`#wedges`; the ear ring phases itself by `180 deg / #wedges`; the axle extrudes `#blade + 2 *
#stub_proud`; and the fork's pocket is a circle of `#bore_d`. Nothing was redrawn.

| Where | Variable | From | To |
| ----- | -------- | ---- | -- |
| `robot sizes` | `#wedge_c` | `0.25 mm` | `0.15 mm` |
| `hinge` | `#wedges` | `12` | `24` |
| `hinge` | `#ring_out` | `#flat - 0.4 mm` | `#flat` |
| `hinge` | `#stub_proud` | `2 * #wedge_h + 0.60 mm` | `2 * #wedge_h + 1.50 mm` |
| `hinge` | `#bore_d` | `#stub + 0.4 mm` | `#stub + 0.1 mm` |

**An `assignVariable` feature carries one expression per variable type, and the model reads the one
its type names.** The parameters are `lengthValue`, `angleValue`, `numberValue` and `anyValue`,
selected by a `variableType` enum, and beside them sits a generic `value` that nothing evaluates.
The four hinge edits were written into `value`. Onshape accepted all four, `GET .../features` read
the new expressions back, no feature reported an error, and the geometry did not move.

What that failure looks like from outside is worth knowing, because none of the usual reads catch
it:

- The feature list answers with the expression that was written, so a read-back agrees with itself.
- Every feature status is `OK`, because a `value` nothing reads cannot be wrong.
- The model does rebuild. `#wedge_c` went in through the Variable Studio, which has no typed twin,
  so the limb's flat moved to 20.8988 mm on the same call and the document looked alive.
- `#ring_out` kept evaluating `#flat - 0.4 mm` against the **new** `#flat`, so it answered 10.0494
  rather than either the old 9.9923 or the wanted 10.4494. A stale value that still tracks its
  inputs does not read as stale.

`check.py` caught it: every row that comes from `make_plans` arithmetic passed, the limb flat
passed, and every row that counts a wedge failed. `hinge 31/62`, `u limb 25/40`, `l limb 23/39`.

What found the cause was asking the model rather than the feature.
`getVariable(context, "wedges")` at the end of the tree answered 12 while the feature said 24, which
puts the disagreement inside Onshape rather than in the write. Dumping every parameter of that one
feature then shows `numberValue` holding 12 next to `value` holding 24.

The repair writes the typed parameter, and `value` beside it so the two cannot disagree. The model
then answers `wedges 24`, `ring_out 10.4494 mm`, `wedge_w 11.5127 deg`, `stub_proud 3.00 mm` and
`bore_d 4.10 mm`.

`bodydetails` is the other read that would have found it and is cheaper than FeatureScript: the
hinge's two bodies carried 48 cone faces each, and 24 wedges is 96.

## The one open item Phase D did not close

The `hinge` tab still mixes two variable naming conventions: ten variables carry the GUI's
`###name = #value` template as their feature name and six carry a bare name. draft9p1p5 lists this
as blocked on a REST grant and there now is one, but `plan.md` does not ask for it, so it was left
alone rather than folded in silently.

## F1 — `check.py`

166 rows across the six Part Studios, and all 166 agree: 13 in `ball and socket`, 62 in `hinge`, 40
in `u limb`, 39 in `l limb`, 6 in each coupon. The script comes forward from draft9p1p5 with the
document and workspace ids changed and the hinge's wedge rows rewritten; it resolves element ids by
name, so no id list needed updating.

`crest_area`'s clamp is load-bearing now. At 12 wedges the crest was a flat all the way in and the
`max(..., 0)` never fired; at 24 the crest closes to a point at r 7.478 mm and everything inboard of
that contributes zero. One crest measures 0.4972 mm² and the model agrees.

## F2 — the face census under a driven size

All eight bodies were censused by surface type, then `#torsoH` was driven to 120 mm and back to
96 mm, and `#limbD` to 30 mm and back to `#torsoH / 4`. Every studio rebuilt with the same parts and
the same faces at both driven sizes, no feature reported an error, and the way back is exact: every
face count and every bounding box is what it was.

| Body | Faces by surface type |
| ---- | --------------------- |
| `ball and socket` / socket body | 17 plane, 1 cylinder, 1 sphere |
| `ball and socket` / ball stud | 1 plane, 1 cylinder, 1 sphere |
| `hinge` / fork | 150 plane, 6 cylinder, 96 cone |
| `hinge` / blade | 156 plane, 6 cylinder, 96 cone |
| `u limb` | 166 plane, 7 cylinder, 96 cone, 1 sphere |
| `l limb` | 156 plane, 7 cylinder, 96 cone, 1 sphere |
| `ball with cylinder` | 2 plane, 2 cylinder, 1 sphere |
| `socket with cylinder` | 18 plane, 2 cylinder, 1 sphere |

Ninety-six cone faces is 24 wedges times two flanks times two faces.

The hinge's ring was then swept across `#limbD` on its own. It holds 96 cone faces on both bodies at
18, 20, 22, 24, 25, 26, 27, 28, 30, 32, 33 and 33.5 mm. At 34 mm the blade comes back with 94 and
the fork with 96; at 36 mm it is 90 and 92; at 40 mm it is 82 and 84. No feature reports an error at
any of those sizes. draft9p1p5 lost its first wedge at 35 mm, so the twenty-four-wedge ring gives up
one millimeter of headroom. The built size is 24 mm and 34 mm is 1.42 times that, so this was left
open rather than chased.

## F3 — no reference leaves the document

Asked again after the edits, not only at copy time. The C2 reads above were repeated on the finished
model and answer the same way.

## F4 — the model looked at

Twelve frames, four orientations each of `hinge`, `u limb` and `l limb`, taken on the agent's
browser after it was restarted.

- The ring is twenty-four wedges on each face, running right out to the ear's straight side, which
  is what `RING_OUT = FLAT` was for.
- The crests come to points over the inner part of the ring and keep a narrow flat only at the outer
  end, which is what the drawing asks for and what the print is being asked about.
- The axle stands proud in the middle of the blade's ring, and the fork's bore takes it.
- The feature tree reads `#wedges = 24`, `#ring_out = 10.4494 mm` and `#wedge_w = 11.513 deg` in the
  GUI, which is the same answer `getVariable` gives.

**A first pass photographed a sign-in screen.** The capture drove whichever Onshape tab the agent's
browser was showing, and the agent's browser had lost its borrowed session. `agent_browser.py` was
restarted, which borrows again from the signed-in browser, and the capture now opens a page of its
own rather than taking whatever tab it is handed.

## F5 — the named version

`F done - Phase F proved`, id `80c22eb7b8b0342ac03f8a6d`, microversion `dd821b5b9c8498eb568aee67`.

**`POST /documents/d/{did}/w/{wid}/versions` answers 404 as well.** The route that publishes is
`POST /documents/{did}/versions` with the workspace id in the body, which is the same missing `d/`
as the copy route. Probing with `GET` first tells the two apart cheaply: the `/versions` shapes that
answer 200 to a `GET` are the ones a `POST` reaches.

## Which browser did the work, and which one should have

`onshape_session.CDP_URL` was `http://127.0.0.1:9222`, and `connect()` used it unless something set
it first. `onshape_gui.connect()` does set it, to 9223; a script that imports only
`onshape_session` did not. Phase C and Phase D, and `check.py` as it had stood since draft9p1p4,
therefore ran their REST calls through the signed-in browser on 9222 rather than the agent's browser
on 9223.

Every read in F1 to F5 above was re-taken through the agent's browser. **The default is now 9223**,
at Mike's call, and a caller that wants 9222 names it. Neither `browser.py` nor `agent_browser.py`
reads the default; both build their own URL from their own port and hand the page in, so the change
reaches `connect()` and nothing else. `require_signed_in`'s message named `CDP_URL` as the window to
sign in to by hand, which would now point at a headless browser with no window, so it names the two
browsers and their two repairs instead.
