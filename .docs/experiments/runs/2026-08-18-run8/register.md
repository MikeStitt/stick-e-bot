# Run 8 — the register

What was built, what was measured, what changed under the plan, and what is still open.
The settlements and the recipe are in [`build-sheet.md`](build-sheet.md); the plan is
[`plan.md`](plan.md).

## Where the work is

| | |
| --- | --- |
| document | `run8-ball-and-socket`, `f013e384e9dd4f18f7c46220` |
| workspace (live) | `851000bb87327d8c12e78a2a` |
| element | `ae109d83a758f08b23ba16d0` |
| version | `run8-ball-and-socket-v3`, `5deaaa871bd7babed27d82e8`, created 2026-08-18 — the one the page cites |
| version link | https://cad.onshape.com/documents/f013e384e9dd4f18f7c46220/v/5deaaa871bd7babed27d82e8/e/ae109d83a758f08b23ba16d0 |

`v1` (`7e216d0db72921c75d1d2b4d`) and `v2` (`6ede5b1b4d57423040580c91`) are earlier in the same
day and measure the same geometry. They are superseded because the slit sketch was rebuilt after
each of them, so their trees are not what the figures now show.

`run7p1-ball-and-socket` (`d0bde1d0896bf11c6315ac78`) is untouched and stays as it was.

## Resolved

- **The joint is built from numbers.** No `Variable` features, no `#name` in any dimension box.
  Seven features, two named parts, ten tree rows fewer than run 7p1's eighteen.
- **The slits come from one slot and a sketch circular pattern.** `slit profile` carries one
  `CIRCULAR_PATTERN` constraint with `patternc1` = 4 over four seed entities
  (`HYNGG8B4eF54.top/.bottom/.left/.right`) and twelve copies, read back out of the feature list.
  One `MIDPOINT`, one `LENGTH` and one `DISTANCE` are the constraint and two dimensions S-1 asked
  for.
- **Run 8 reproduces run 7p1 exactly.** Both documents measure two parts with the same faces and
  the same volumes to four decimals: `Ball stud` 128.6210 mm³, `Socket body` 248.9915 mm³.
  Taking the variables out changed no geometry.
- **Every acceptance check measured, not inferred.** Ball sphere r 3.0000 (Ø6.000); cavity sphere
  r 3.2000, truncated at z = +1.3500, so the mouth is 2 × √(3.2² − 1.35²) = Ø5.8026 — confirmed
  independently by the top face's four pieces summing to 37.186 mm², which is the annulus
  π(4.7² − 2.9013²) less four 0.8-wide slot openings; cavity volume 137.258 − 27.777 = 109.48;
  four slit floors at z = −2.6500 in a collar whose base is z = −4.1500, so the floor is 1.5 and
  the cut is 4.0; eight slit side faces at ±0.400 from their centre lines, so each slit is 0.8
  wide.
- **H12 verified in run 8, not taken on trust.** With **Show constraints** unticked, hovering a
  slot's long side puts a strip of four glyphs beside it; the last — a cluster of small circles —
  right-clicks to **Edit pattern**. That is now an advice callout on the page.
- **Every frame the page names exists and Sphinx builds clean.** 49 figures named, 49 on disk,
  none unused, no missing-image warning.

## Changed under the plan, and why

- **S-5, new: a sketch circular pattern does not define its copies.** `slit profile` reports
  *"is not fully defined"*. The seed is black; the three copies are blue. Nothing is loose — they
  rebuild in the same place every time — but the page can no longer promise a fully defined
  sketch here, and the acceptance check changed to say what a reader can see. See
  [`build-sheet.md`](build-sheet.md).
- **The tag frames are shot at the working zoom, not zoomed in.** The plan expected the `3x`/`4x`
  tag to need its own zoomed frame and a separate wide frame. At 80 px/mm the tag is legible in
  the wide frame, so `bs-37a` and `bs-37c` are one frame each instead of two.
- **Four figures gained letter suffixes.** The new steps between selecting the slot's sides and
  naming the sketch needed four frames where the page had one number left: `bs-37a`, `bs-37b`,
  `bs-37c`, `bs-37d`. Renumbering `bs-38` onward would have cost two edits of the page to save
  four letters.
- **Five slugs in the slit section were renamed** rather than reused, because their old names
  described bars that no longer exist: `bs-33` … `bs-37`. Three more lost tails naming variables:
  `bs-22`, `bs-23`, `bs-29`, and `bs-41` became `-the-depth-set-to-4`.
- **The brief's `Ball stud` volume was wrong by an order of magnitude.** It read 935.2249 mm³,
  which runs 2 and 3 measured against the Ø12 ball this joint had before it was resized. It is
  128.6210 mm³ and now says so.
- **The slit sketch was built three times, and the last two were the harness's fault.** Both
  rebuilds were reshoots, not remodels: no dimension or constraint changed, and the geometry
  measured the same each time.

  The first pass shipped nine figures with an Onshape notification strip baked across the top of
  the canvas — *"Sketch 1 has been canceled. Restore"* in `bs-31` and `bs-32`, *"Reduced rendering
  performance detected"* in `bs-33` … `bs-37b`. A banner is not part of the step, and doctoring a
  screenshot to remove one is not something this project does, so the sketch came out and went
  back in.

  The second pass shot `bs-34` mid-flight: a spinner, a *"Poor connection…"* toast, and the slot
  still sitting where it was drawn because the midpoint constraint had not reached the server.
  The same toast had already swallowed an Enter and left the width dimension reading 0.69377
  instead of 0.8.

  Two guards now stand between the harness and the shutter, and both raise rather than shoot:
  `no_banner()` reads the strip across the top of the canvas and dismisses it, and `still()`
  compares consecutive frames and refuses to shoot until nothing has moved. Numbers go in through
  a double-click, a `fill`, and a read-back, and the midpoint is confirmed by watching the slot's
  left edge arrive on the origin rather than by waiting a fixed time.

- **The direction of the cut needs no reversing.** The page tells the reader to check it from the
  corner, and the check is worth keeping, but on a sketch made on the collar's top face the
  Remove arrives running down into the collar already.

## Not attempted

- **The brief's Ø12 limb stub check does not apply to this build.** The guide page builds the
  collar on its own, with no limb stub, so *"the limb stub is Ø12.000 mm and the collar is 9.400,
  so the step around the collar's foot is 1.3 mm wide"* has nothing to measure here. It stands
  for a full test build of the brief, which this run is not.
- **Whether a 1.5 mm floor lets the mouth open far enough to swallow the ball.** Only a print
  settles it — S-3.
- **The ceiling.** The pattern section has not been walked from an empty document by someone who
  did not build it.
