---
name: counts-catch-what-dimensions-miss
description:
  "A model can pass every dimensional check and still have the wrong topology; check face and patch
  counts against what the analysis assumes."
metadata:
  type: feedback
---

Twenty-seven acceptance rows agreed on stations, radii, areas and angles while the
draft9p1p2 blade still had a Ø4 shaft bridging its slit, tying the two leaves together at
the pin. The user (Mike) caught it by reading the construction, not the numbers.

**Why:** dimensional rows ask "is this face where it should be". They never ask "how many
faces are there", which is the question topology answers. The analysis a part is built to
satisfy assumes a shape, not just sizes; `hinge_spring` presses the axle against a leaf
free to bend, and no station or radius can tell you whether something is propping it.

**How to apply:** for every feature the analysis depends on, add a row that counts its
patches, and say in the row what the wrong count would mean. Feature order is what usually
decides the count; see [[fix-the-model-retake-the-frames]] and
[[design-intent-is-not-sacred]].
