# A12 — the sheets frozen as r6, and the sketches republished

The last row of phase A. Everything above it changed numbers that the two plan sheets draw and that
six published explanatory pages argue from, so this row is where those catch up.

## The sheets

`make_plans.py` was run with `--no-render` all through phase A, because rasterizing attaches over
CDP and is slow. Run at the end with rendering on, both SVGs came back byte-identical to what A10
left — every change had already reached them — and only the PNGs moved.

**`plan-assembly.png` timed out at Playwright's 30-second default** on *waiting for element to be
stable*, after `plan-parts.png` rendered. Re-run on its own with a 180-second screenshot timeout and
`animations="disabled"` it rendered in one pass. The generator's own `render()` keeps the default,
so the same sheet is likely to time out again; the fix is the timeout, not the drawing.

**Frozen as r6**, copied into [`../../sketches/`](../../sketches/) as `plan-r6-assembly.svg` and
`plan-r6-parts.svg` with a row in that README's revision table. r5 is the last hinge before the
blade's slit came out; r6 is the whole of draft9p1's phase A in one pair of sheets.

## The sketches

Six of the eight explanatory pages carried a number phase A moved. Three of them are drawings whose
argument rests on the joint's fit, and three are dated pages that end on the same sentence about
where the design has got to.

| Page | What moved |
| --- | --- |
| `hip-clearance.html` | The whole drawing. `#fit` 0.08 and `#grip` derived, so the swing is 41.76° against 31.86° and the rim clears the torso by 2.554 rather than 2.191 |
| `socket-wrap.html` | Its third sizing was *grip raised to 3.60 at `#fit` 0.8*, which A2 did not adopt. It is the settled joint now |
| `slit-reach.html` | Same third sizing, and the `#grip` ceiling with it: 3.459 against the settled 1.9465 |
| `collar-step-back.html`, `socket-study.html`, `hinge-stackup.html` | One shared sentence — *the limb is Ø24, the ball Ø12, `#grip` 3.6 and the swing 31.86°* |

**Two of the three drawings got stronger rather than weaker.** `hip-clearance` was drawn to say the
hip reaches its limit without touching the torso, and a wider swing is a harder version of that
claim; it still clears, by 2.554 mm. `socket-wrap` was drawn to say that wrap is not what retains
the ball, and the settled joint wraps 108.9° against the built one's 116.7° while holding 0.480 mm
against 0.197 — less wrap, more retention, which is the page's own thesis stated more sharply than
it could state it before.

**`socket-wrap`'s third panel changed meaning, not just numbers.** It was *twice as big, proposed*
— the route that keeps `#fit` at 0.8 and raises `#grip` to 3.60. That route closes the mouth too,
and A2 rejected it because it only holds near the fit it was dimensioned at. The panel is the
settled joint now and the rejected route is two sentences of prose under it, which is where a route
not taken belongs.

**`slit-reach` barely moved, and that is worth knowing.** The proposal's mouth radius was 5.769 and
the settled one is 5.760, so the slit reaches 0.760 into the mouth against 0.769. Both hold the
mouth near 96% of the ball, by different routes, so the number that decides whether the slit works
was never really in dispute.

## The tab icons are recorded now

A republished artifact keeps its URL and its title, and the icon is what a reader picks it out by in
a gallery. Nothing recorded what each page had been published with, so six were set this run and
written into [`../../sketches/README.md`](../../sketches/README.md) beside the table of links.
`figure-design-sketch` and `shoulder-step` carry no moved number, were not republished, and are not
recorded.
