# A10 — the gripper's three disagreements, and a fourth

Three sources described this part and no two of them agreed. The build picked one answer per
disagreement and none of the sources were changed, so all three are still live.

| what | `make_plans.py` | `gripper.md` | what draft9p0 built | settled |
| --- | --- | --- | --- | --- |
| the bore's axis | fore-and-aft | parallel to X | parallel to X | **parallel to X** |
| the body across that axis | a literal 6 | follows the collar | `2 × #collarR` = 18 | **`2 × #collarR`** |
| which way the mouth opens | straight down | forward, written **+Y** | forward, −Y | **forward, −Y** |
| the mouth's angle | a typed 50°..130° | a 2.6 gap | not measured | **`asin(#mouth / #bore)`** |

The fourth row was found working the other three.

## The bore runs left-right, and the sheet drew the one part the brief warns about

`gripper.md`'s acceptance list already names this failure exactly:

> The mirror check above does not catch a clip built on `Front` with its mouth opening downward:
> that profile is symmetric about x = 0, so it mirrors onto itself and passes every other check on
> this list, while the bore runs fore-and-aft and the robot grips a bar pointing away from itself.

That is precisely what `make_plans.py` drew — the C in the front elevation, mouth opening down the
part's own centerline — and the docstring defended it on a drawing argument: a bore square to the
page stays a circle when the gripper rotates with a bent forearm, and any other axis reads as a
slot. The argument is true about the picture and says nothing about the part. A sheet that draws
the wrong part so that the right view comes out easy is a sheet that will be built from.

**Both sheets draw it the other way now.** The parts sheet's gripper is a **side** view, page-right
forward, which is the plane the profile is actually sketched on — `Right`, the only plane holding
both the mouth's direction and the part's length. The assembly's front elevation draws the gripper
as what it is from the front: a slab `2 × #collarR` across with the bore crossing it as two hidden
lines.

## The mouth opens the way the robot faces

`build-briefs/README.md` settles the frame in one line — the robot faces −Y — and `gripper.md`
said the mouth opens at +Y. draft9p0 built the brief's sign first, measured the lips, found the
gripper holding its bar behind itself, and rebuilt `clip profile` to open −Y.

**Forward is the whole reason the part has the shape it has.** A clip that opens outward makes the
left gripper the mirror of the right and doubles the part count; opening it forward makes one part
serve both wrists. The brief's own argument was right and its sign was wrong, which is the kind of
error that survives because the sentence around it reads correctly.

The brief now says −Y, in the one step that names a direction. The sheet's label says *opening
forward* and the drawing agrees with it.

## The width is the collar's diameter, and that is what "follows the profile" means

The body was typed 9.4 and went stale twice: once when the collar became Ø9.0, leaving a 0.4
overhang, and again when it became Ø18.0, leaving the gripper half the width of the thing standing
on it. `make_plans.py` never moved off 6 at all.

**`#clipW = 2 × #collarR` = 18.** This is the robot's only cross-part dimension — everywhere else
the socket is added to something already big enough to hold it, and the collar can change without
anything following.

**Flush means the top is the collar's own circle, not a slab wide enough to sit under it.** The
part's top face is a disc of the collar's diameter, coaxial with the socket. Below it the body
necks in fore-and-aft to the clip's Ø10, and it has to: the collar's radius reaches 9 forward while
the clip's reaches 5, so a body that stayed 18 deep fore-and-aft would close the mouth off. That
is why no stem width was ever flush — a round collar and a straight-sided slab cannot share an
outline, and the answer is for the top of the body to be round.

This is what task #28 asked for. B8 builds it.

## The mouth's angle is a result

`make_plans.py` typed the mouth as the arc from 50° to 130°, an 80° gap. The brief specifies a
**2.6 mm** mouth, measured across the opening at its narrowest — between the two lip tips, which
sit on the bore. Those are not the same statement, and at the sheet's angles the gap came out
**2.06**, so a bar the brief calls a snap fit would have been 0.5 mm tighter than intended.

**The angle is `asin(#mouth / #bore)` = ±52.0°**, which puts the lips 2.6 apart by construction.
The sheet also drew the bore at the bar's own Ø3.2 rather than the clip bore's Ø3.3 — the clip has
to turn on the bar — so `CLIP_BORE` exists now and both the bore and the mouth come off it.

## Found while reading

**The register puts the bore's acceptance check in the wrong file.** It says
*"`12-gripper.md`'s acceptance list wants it parallel to X"*. `12-gripper.md` has no acceptance
list; the check is in `build-briefs/gripper.md`. The disagreement is real and its two sides are the
sheet and the brief.

**Ø10 is still a proposal.** `#clipR` has no row in the plan's variables table, and the brief says
so. It is the one number in the robot set by something outside it, and A13 is where a row for it
would go if it gets one. Nothing in this row needs it to be a variable, because the clip's diameter
is not what was in dispute.
