# A3 — the reference gripper, measured, and why its square does not scale

**`stickbot-for-bot-review` makes the socket's platform by cutting the clip's own crown flat, and
the flat comes out square and the collar's diameter.** It reads as a technique to copy. Measured, it
is a coincidence of two numbers that no longer coincide: at that size the clip is wider than the
collar, and at 2× the collar is wider than the clip. **The construction copies; the shape does
not.**

Read over REST on 2026-08-27 from `stickbot-for-bot-review` `111f975041ddb104a6028d45`, workspace
`38e73619152eec8be2c51f8b`, `gripper` `b1ff7bea381ab1ce6718d1a1`, and from `stickbot-draft9p1`
`a1a859f4bfdfe42d372aff90`, workspace `d3a590c94880f445e3c56902`, `gripper`
`7ef73a118e1331213bc1554f`. Both documents were read and neither was edited.

## What the reference actually does

Its feature tree, in order:

| Feature | Type |
| ------- | ---- |
| `clip profile` | `newSketch` |
| `clip body` | `extrude` — symmetric, depth 9.4 mm |
| `copy socket` | `importDerived` |
| `plane to cut top of clip` | `cPlane` — **`OFFSET`, offset `0 mm`** |
| `remove top of clip` | `splitPart` — `keepFront`, `keepBothSides` false |
| `gripper mate point` | `mateConnector` |
| `combine parts` | `booleanBodies` |
| `mate to robot` | `mateConnector` |

**Nothing is calculated.** The cut plane is an offset plane at **zero**, referenced to a face rather
than driven to a number, which is `req.model.visible_geometry` doing its job — a student can see
what the plane is on. `remove top of clip` splits the clip body with it and throws the top away.

**The plane lands on the socket's root.** The collar's outside cylinder measures r 4.7 with its top
at z +1.35, and the only downward-facing planes on the part are at **z −4.15** — 5.5 below the
collar's top, which is `#collar` at that size. The clip's top is cut flush with the bottom of the
socket, so the platform and the socket's root are one face.

## Why the flat comes out square

The clip is a horizontal cylinder of **r 5.5** on an axis at z −7.0, extruded **symmetric 9.4**
across. Cutting it at z −4.15 is a chord 2.85 above its axis:

| | |
| --- | --- |
| flat across Y, `2 × √(5.5² − 2.85²)` | **9.4080** |
| flat across X, the extrude's own width | **9.4000** |
| the collar it carries, Ø | **9.4000** |

**Square to 0.008 mm, and the collar's diameter to 0.008 mm — and neither is a dimension anybody
typed.** The X width is `2 × #collarR` and was chosen; the Y width is whatever the chord gives, and
it agrees because the clip's Ø11 is 1.6 wider than the collar's Ø9.4. There is room for the chord to
reach the collar's width before it runs out of crown.

## Why it cannot scale

`#barD` is 3.2 and does not scale, so the clip does not either — Ø11 there, Ø10 in the plan sheets.
The collar doubled to Ø18. **The crown is now narrower than the thing it has to support**, and a
chord across it can be 10.0 at the very most.

Cutting a Ø18 flat at draft9p1's socket root would need a crown of radius
`√(9² + 9.9465²)` = **13.4139** — Ø26.8278 fore-and-aft below the cut, against a clip mouth at
z −17.700. [`../../../build-briefs/gripper.md`](../../../build-briefs/gripper.md) rules exactly that
out: *"a body 18 deep fore-and-aft would close the mouth off."*

## What draft9p1 has now

The same two features are already in draft9p1's tree — B8 kept `plane to cut top of clip` and
`remove top of clip`, and added `body top outline`, `round the body top` and `trim the body top`
after them.

**`clip profile` draws the clip end-on**, the sketch's y being the model's z, and `clip body`
extrudes it symmetric `2 × #collarR`. So 18 across X arrives from the extrude, and what the sketch
gives across Y is a slab dimensioned `#clipR` each side of the axis:

| What the dimension holds | Expression |
| ------------------------ | ---------- |
| the clip circle | `2 * #clipR` |
| the bore | `#bore` |
| the top of the slab, above the clip's axis | `#gripperL - #clipR` |
| the slab, each side of the axis | **`#clipR`** |
| the upper lip, above the clip's axis | `#mouth / 2` |
| the two lips apart | `#mouth` |

**The body is 10 wide fore-and-aft because one dimension reads `#clipR`.** `body top outline` then
draws two concentric circles, `2 * #collarR` and `4 * #collarR`; `round the body top` adds the inner
disc `#collarR - #clipR` deep and `trim the body top` removes the ring around it to the same depth.
The top 4 mm of the body is a Ø18 cylinder and the slab's corners come back below it, which is what
the plan view shows — a circle with four tabs standing out at its edge.

| | |
| --- | --- |
| collar, Ø | 18.0 |
| the top 4 mm of the body, Ø | 18.0 |
| the slab below it, across X | 18.0 |
| the slab below it, across Y | **10.0** |
| collar overhang below the rounded top, each side fore-and-aft | **4.0** |

**So the collar is carried on 18 in one direction and cantilevered over 4 mm of air in the other,**
under a rounded top rather than a square one. That is the thing to fix, and the reference's own
construction cannot fix it.

## What A3 does instead

**The square is the slab's own width, and the neck is a 45° chamfer onto a corner the sketch already
has.** Three edits:

- The slab's dimension becomes **`#collarR`**. The extrude already gives `2 × #collarR` across X, so
  the top of the body is 18 × 18 and the Ø18 collar is inscribed in it, tangent on all four sides.
  That is the reference's relationship, reached by dimension instead of by chord.
- Two lines at **45°** run from the slab's sides down to the corners at `#clipR` across and
  `#mouth / 2` above the clip's axis. Those corners are already in the sketch, holding the mouth's
  upper lip. The chamfer's leg is `#collarR − #clipR`, an expression the file already uses.
- `body top outline`, `round the body top` and `trim the body top` are deleted. The gripper goes
  from ten features to seven, and `plane to cut top of clip` and `remove top of clip` keep doing the
  work the reference gave them.

**The mouth is untouched.** Below the upper lip the body is the clip circle and nothing else,
exactly as it is now, so the throat between the lips stays `#mouth`. The chamfer's closest approach
to the clip's axis is 5.1662 against a crown radius of 5, so it stays outside the crown for its
whole length, and 45° is the overhang a printer bridges without support.

**What is left of the platform at full width is the number to watch.** The chamfer's top sits
`#collarR − #clipR` above the lip, and the root comes down to meet it:

| | now | after A2 |
| --- | --- | --- |
| the socket's root | −9.0535 | −9.0000 |
| the top of the chamfer | −13.7000 | −13.7000 |
| the run at full 18 | **4.6465** | **4.7000** |

That run is `#gripperL − #collarR − #mouth / 2 − #collar`. A2 sets `#collar` to `#ball / 2 + #wall`
= 9, which lifts the root 0.0535 and hands the run that much back. Phase C measures what is left
rather than driving it.

## Found while drawing: the sheet's mouth was a V

`clip()` computed one angle, `asin(CLIP_MOUTH / CLIP_BORE)`, and used it on both circles. That is
the right angle for the bore and the wrong one for the outside, which it opened to **3.94** instead
of 2.6 — a radial V, narrowest at the bore. The model cuts both circles where they cross
`#mouth / 2` from the axis, so its mouth is a parallel slot 2.6 tall the whole way out.

**A3 found it by landing on it.** The chamfer stops on the upper lip, and against the drawn V it
stopped inside the opening. Each circle now takes its own angle — `asin(CLIP_MOUTH / (2 * ro))`
outside and `asin(CLIP_MOUTH / (2 * ri))` on the bore — and the two lips come out horizontal, which
is the part that gets built.

The front elevation keeps the two hidden bore lines it has always had. The chamfer leaves no
silhouette looking along the bar, and the robot is drawn small there; three more lines across a
gripper that size read as hatching rather than as edges.

## What the sheet draws now

- `clip()` outlines the platform at `CLIP_W` and chamfers it `CLIP_CHAM` at 45° onto the mouth's
  upper lip, so the side view shows the square and the neck the model will have.
- `CLIP_CHAM = COLLAR_R - CLIP_R` is the one new name, and `CLIP_W`'s comment now says it sets the
  body fore-and-aft as well as across the bar.
- The gripper figure gains two callouts, *platform 18 × 18 mm* and *chamfer 4 mm at 45°*.

## Frames

Rendered with `shadedviews` at 700 × 700, four views each, no edit to either document.

| Frame | What it shows |
| ----- | ------------- |
| [`frames/a3-ref-iso.png`](frames/a3-ref-iso.png) | the reference: a flat square top, the collar sitting inside its edges |
| [`frames/a3-ref-front.png`](frames/a3-ref-front.png) | the same across the bar's axis |
| [`frames/a3-ref-right.png`](frames/a3-ref-right.png) | the crown's chord, and the mouth open below it |
| [`frames/a3-ref-top.png`](frames/a3-ref-top.png) | the square in plan, with the collar inside it |
| [`frames/a3-9p1-iso.png`](frames/a3-9p1-iso.png) | draft9p1: the collar overhanging the body it stands on |
| [`frames/a3-9p1-front.png`](frames/a3-9p1-front.png) | 18 across X, where the collar is supported |
| [`frames/a3-9p1-right.png`](frames/a3-9p1-right.png) | 10 across Y, where it is not |
| [`frames/a3-9p1-top.png`](frames/a3-9p1-top.png) | the same in plan |
