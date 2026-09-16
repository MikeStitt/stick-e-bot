# Run 6 — the joint rework

Run 5 built every joint by sketching it again on each part. Run 6 builds each joint **once** and
adds it wherever it belongs. This note says what changes, what it turns on, and what has to be
measured before any of it is modeled.

Nothing here is built yet. Where a number is computed somewhere already this note links to the
file that computes it rather than repeating it — see
[`../../build-briefs/README.md`](../../build-briefs/README.md).

## The four halves

Two joints, two halves each. These are the parts to model once and reuse:

| joint | half | goes on |
| --- | --- | --- |
| ball and socket | ball stud | torso, and the ball end of a limb |
| ball and socket | socket collar | head, hand, foot, and the socket end of a limb |
| hinge | clevis fork | `limb-socket-clevis` |
| hinge | detent blade | `limb-blade-ball` |

The geometry each one has to hit is already stated in
[`../../build-briefs/ball-and-socket.md`](../../build-briefs/ball-and-socket.md) and
[`../../build-briefs/hinge.md`](../../build-briefs/hinge.md). Run 6 does not redesign the joint.
It changes how many times the joint gets drawn.

## How a half gets added

The route through Onshape is **Derive → Transform → Boolean Union**:

1. **Derive** pulls the half in from its own Part Studio, in this document or another, and keeps
   an associative link back to the source. Its **Locations** field takes a mate connector and
   lands the derived origin on it, which often removes the need for step 2.
2. **Transform → Transform by mate connectors** moves the half so one of its mate connectors
   lands on one of the host's. A Part Studio has no mate solver; this is the closest thing to
   mating in one, and it positions once rather than holding a relationship.
3. **Boolean → Union** merges it into the host part.

Two behaviors of that route decide whether it works at all, and only the first is documented.

- **Transform does not carry mate connectors.** A connector moves with its part only if it is
  selected into **Entities to transform or copy** as well. Left out, the part moves and the
  connector stays. This is the same failure the torso already has, arrived at from the other
  direction.
- **A Boolean Union drops the connectors of every part it consumes.** Measured in both selection
  orders — [`spike-boolean-mate.md`](spike-boolean-mate.md). The union keeps the connectors owned by
  the part listed **first** in Tools and drops the rest, and a dropped one stays in the feature tree,
  error-free, still drawing its triad. Only an assembly shows the loss.

### What the union costs the rework

**Building a joint once does not carry its connectors.** A derived half loses whatever connectors it
arrived with the moment it merges into a host listed first, so every connector is re-made on the
host, against the merged geometry, once per joint per part.

The geometry, the detents and the handedness are still drawn once, and those are the things that get
drawn wrong when they are drawn six times. Connectors are what the rework does not buy.

One rule held before the spike and still does: a Part Studio connector only appears in an assembly
when **the Part is its owner entity**. An ownerless connector survives a union and is invisible
downstream, so it is not the way out.

## The foot joins the standard

Today the foot's ankle socket is the one socket that is not standard. The collar stands straight
off the plate's top face, which makes it stand further proud than the collar every other part
uses, and its relief slits run that whole longer length.

**The change: a pad under the socket.** The standard socket mounts on a face one `grip` below its
rim less its proud length — the face `ball-and-socket.md` calls out twice. The foot's plate top
face sits below that. Adding a pad of the collar's own diameter, tall enough to close that gap,
puts the mounting face where the standard socket expects it, and the standard socket then drops
on unmodified.

What this does and does not change:

- **The outside does not change.** A collar standing its normal proud length on a pad of the same
  diameter is the same cylinder, the same height above the plate, that is there now.
- **The slits change.** They stop at the collar and the pad stays solid, so the tabs get shorter
  and stiffer and their free length finally matches every other socket. Tab flex is what the
  joint's grip depends on, so this is the point of the change, not a side effect.
- **No station moves.** The ball center, the sole and the figure's height are untouched.

**The pad is the collar's diameter, not the limb's.** `ball-and-socket.md` stands its reference
collar on a Ø12 limb stub with a step all the way round. That will not fit here: run 3 measured
the flat left around the collar by the plate's top fillets, and it is under half a millimetre. So
the foot uses the same joint part on a different mount, and that difference is real and should be
said rather than smoothed over.

**What it costs.** `foot.md` records the ankle's swing limit against the collar it has now, so
that figure is recomputed, not carried. Both the socket wall and the four slits are still marked
**proposed** in `ball-and-socket.md` with nobody having measured whether tabs cut this way flex.
This change does not measure them. It reduces two unmeasured joints to one.

**Where the pad height should live.** It follows from the collar's proud length, the grip and the
plate's top face, all of which are already in
[`../../../../instructions/robot-guide/make_plans.py`](../../../../instructions/robot-guide/make_plans.py).
It should be computed there rather than typed into the brief, so that moving the plate or the
collar moves the pad.

## The torso's two shoulder mate connectors

Carried here from run 5 on purpose — see
[`../2026-08-13-run5/register.md`](../2026-08-13-run5/register.md) for the measurement and why it
was not fixed there.

`Shoulder R` and `Shoulder L` are typed offsets from the origin point rather than attachments to
the ball, so they stayed behind when S1 moved the geometry. That fix turned on how joints end up
being added, and the spike settled it: a half cannot bring its connectors through the union, so the
shoulders get theirs the way every other joint does — placed on the ball face, after the union,
attached to the geometry rather than typed as an offset from the origin.

Two connectors in that Part Studio must not be touched. `Shoulder drop axis` and `Shoulder swing
axis` are what the two shoulder rotations are built on.

## The layout sketch and the head's neck

The head moved when it got the standard neck collar, and two places record the stack differently.

`make_plans.py` computes the head's rim, base and top and the figure's height from the collar's
proud length, so the sheets it draws already carry the change — nothing to fix there.

[`../../../robot-build-plan.md`](../../../robot-build-plan.md) is the one that is behind. Its
station table still gives a top-of-head from before two separate findings: the stand-off that
made the figure taller than the round number the plan opened with, and the neck collar that moved
the head again. The layout sketch that table describes is the sketch every part in the taught
path hangs off, so a station line that is wrong there is wrong in every part built from it.

**What run 6 does about it:** bring the station table and the layout sketch to what `make_plans.py`
computes, and make the table point at that file instead of carrying its own numbers, the way the
briefs' README was already made to. This is the same defect the briefs' station table had, in a
second file.

Before the sheets are regenerated, freeze the current ones into
[`../../sketches/`](../../sketches/) under the next revision, so the drawing that matched run 5 is
still readable afterward.

## Not decided

- Whether a half is added by **Derive** or stamped by a **custom feature**. A FeatureScript
  feature could emit geometry and connectors together, which is the only route where building it
  once also covers the connectors. The Constitution requires new structure to earn its place
  against doing it the plain way, and this course is for students who have just learned to sketch
  and extrude — so the reference model and the taught path may want different answers, which
  means building it twice on purpose.
- Whether the socket's proud length becomes a **configuration input**. If it does, a host that
  needs a different length asks for it rather than being modeled separately.
- Whether the hinge halves reuse as cleanly as the ball and socket. The hinge carries detents and
  a handedness the ball joint does not, and nothing here has checked that.
