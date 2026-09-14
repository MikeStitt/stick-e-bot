# A5 — where the first tread groove goes

U5 says the pattern's offset is arbitrary and wrong, that the repeat must divide the foot's length
evenly, that no groove sits at either end, and that the number comes with a drawing. The register
also says the choice between *equal margins* and *only solid material at both ends* changes the
arithmetic. It does, and this file settles it.

## What draft9p0 does

The offset is `#foot_l - #heel_y`, which evaluates to **64** on a sole **96** long. With the groove
6 wide and the repeat 12, the eight grooves land at 64, 76, 88 … 148, and the last one ends at
**154**. Most of the pattern is off the end of the foot.

That is worse than the register's reading of it. The finding was recorded as *the first groove
lands on the toe tip*; the arithmetic says only the first three fall on the sole at all, and the
other five are cut in empty air. It regenerates green either way, which is why nobody caught it.

## The two phases, worked

The sole is 96, the groove `#rib_w` is 6, the repeat is `2 × #rib_w` = 12, and 12 divides 96
**eight** times. Margins are measured from the ends of the sole to the nearest groove edge.

| | offset | grooves | first | last | heel margin | toe margin |
| --- | --- | --- | --- | --- | --- | --- |
| draft9p0 | `#foot_l - #heel_y` = 64 | 8 | 64–70 | 148–154 | 64 | **off the foot** |
| **A — groove centered in its repeat** | `#rib_w / 2` = 3 | **8** | 3–9 | 87–93 | **3** | **3** |
| B — U5's second candidate | `repeat − width` = 6 | 7 | 6–12 | 78–84 | 6 | 12 |
| B kept at eight grooves | 6 | 8 | 6–12 | 90–96 | 6 | **0, flush** |

## A is adopted

**The groove sits in the middle of its own repeat.** That is the whole rule, and everything U5 asks
for falls out of it: the repeat divides the length evenly, the run starts and ends with land rather
than with a groove, and the two margins are equal because centering makes them equal.

**The offset derives from the groove and nothing else.** `#rib_w / 2` names the one part it belongs
to. That is the point of the requirement — the old offset borrowed a heel dimension, and a heel
dimension has no business setting a tread phase.

**B leaves the count wrong or an end flush.** At eight grooves the last one runs out to the toe
edge, which is the thing U5 forbids. At seven it works, but the count stops being
`#foot_l / (2 × #rib_w)` and the margins come out 6 and 12 — an asymmetry a reader takes for a
mistake, on a foot that has no other reason to be lopsided.

**3 mm of land at each end is thin, and it is land.** The groove is 2 deep in a 12 plate, so this
is a cosmetic tread and 3 mm of it reads as a deliberate border. If the printed foot says otherwise
the lever is `#rib_w`, and the phase follows it without being touched.

## The drawing

`make_plans.py`'s `foot()` drew no tread at all — the sheet has never shown a groove. It draws all
eight now, on the sole in the side view, with the leader reading *tread — 6 mm grooves, 12 mm
apart*. The heel margin and the toe margin are both 3 on the sheet, which is the check.

## Found while drawing, not fixed here

**The sheet and the model disagree about where the ankle sits along the foot.** `foot()` starts the
sole 40 behind the ankle and runs it 96 forward, so the ankle is 40 from the heel. The register
reads the model's sole as running +32 at the heel to −64 at the toe, which puts the ankle 32 from
the heel. Both are a 96 sole; they differ by 8 in where the ankle stands on it. A5 is phrased
against *the ends of the sole* so it holds either way, and A11 owns the foot's stations.
