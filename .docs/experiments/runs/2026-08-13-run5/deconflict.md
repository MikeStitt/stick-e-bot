# Run 5 — deconflict

Phase 4 of [`../../design-into-cad.md`](../../design-into-cad.md). The audit's repairs examined
together, before any of them is applied.

## The hinge's two halves interlock, and they check out

The fork and the blade are separate documents that have to meet inside one joint, so their numbers
were worked through as a stack rather than trusted because they came from the same file.

| Surface | Where | From |
| ------- | ----- | ---- |
| ear inner face | ±2.8 | `SLOT`/2, the slot being 5.6 |
| blade face | ±2.5 | `BLADE`/2, the blade being 5.0 |
| clearance | 0.3 a side | `GAP` — 2.8 − 2.5 |
| stub tip | ±2.0 | 0.8 `STUB_PROUD` off the ear's inner face |
| interference | 0.5 | 2.5 − 2.0 = `MOVE`, which is `STUB_PROUD − GAP` |
| pocket floor | ±1.5 | 1.0 `POCKET_D` into the blade from its face |
| tooth crest | ±2.2 | 0.6 `TOOTH_PROUD` off the ear's inner face |
| valley floor | ±2.05 | 0.45 into the blade from its land |
| crest in valley | 0.15 clear | 2.2 against 2.05 |
| crest on land | 0.30 interference | 2.2 against 2.5 |

Every one of those falls out of the constants in `target.json`, and the two parts agree at every
surface they share. The pair must be repaired together — repairing one alone leaves a joint that
cannot close.

## Resolved here

**The foot's slit length is 7.35, not `COLLAR_L` 5.5.** The slit exists so the mouth can open, so
it has to run the collar's whole proud length — and on the foot that length is set by the plate at
7.35, which the brief already records. Cutting 5.5 would leave 1.85 of unslit collar doing exactly
what an unslit collar does. This is the general rule rather than a special case: the slit follows
the collar it is cut into.

**The foot is rebuilt with its length along Y**, which settles the brief-versus-model conflict in
the brief's favor. Three reasons and none of them is that the brief outranks the model: run 5's
instructions are written from this CAD and a student following `foot.md` would draw it along Y; it
removes the 90° turn each foot needs in the assembly; and the outline is being re-sketched anyway
to fix the symmetry, so the axis costs nothing extra.

**The foot's outline is drawn symmetric about its own fore-and-aft centerline** in the same
rebuild, with `Symmetric` constraints rather than dimensions on both sides. The measured r4
features at (5.14, 5.94) and (7.10, −6.22) are not a mirror pair and nothing about a foot wants
handedness.

**The brief's detent count is wrong, not the model.** `hinge.md` says run 3 built 13 valleys across
180°. The audit measures 48 r0.5 cylinders, 24 a side, and `STEP` 15 divides 360 into exactly 24.
Run 4 counted faces on one visible arc. The brief gets corrected; the CAD does not.

## Registered, not decided

**The gripper's bore.** 3.3 as built against the 3.6 the radial `#fit` convention would give. The
row is `proposed` and the brief asks the builder to say which was used and why. It is a trade
rather than an error: 3.3 grips harder, 3.6 lets the clip turn on the bar as the brief says it
must, and which is right is a print question. **Cheap answer:** build 3.3, print both, keep the
one that turns without falling off.

**The two feet still touch at x = 0.** The plate is 24 across and the hips are at ±12, so the inner
edges meet exactly, and rebuilding the foot along Y does not change that — it only moves which axis
the coincidence happens on. Narrowing the foot, widening the hips, or accepting splayed legs are
the three ways out, and `#hipHalf` is a driver. **Cheap answer:** accept it for run 5's
screenshots, which are taken at zero pose, and raise it as a design question.

## Order of repair

Follows the plan's order of work.

1. **Prove the sketch-entity route** on a study document. Every rebuild below is a sketch edit, so
   this decides whether the work is API or GUI, and it is cheap only while nothing depends on it.
2. **The torso's shoulder** — hardest, because the stud leaves on a doubly-rotated axis the part
   has no plane for, and because the neck boss is a second new feature on the same part.
3. **The two limb halves, as a pair** — joint-carrying, and they must move together.
4. **The foot** — one new feature and one re-sketched outline.

The head and the hand need no repair.
