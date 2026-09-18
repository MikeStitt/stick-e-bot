#!/usr/bin/env python3
"""Generate the two plan sheets and render them to PNG.

Status: controlling. This is the design source. Every robot dimension is decided here and
nowhere else, and the brief sheets, the plan sheets and the Variable Studio all follow from it.

Sheet 1 (plan-assembly) — the parts assembled, named, with the overall dimensions.
Sheet 2 (plan-parts)    — the eight unique parts, each named, every joint portion labeled,
                          and two section details that define the joints themselves.

The parts sheet draws real parts: a ball stud stands off its face on a stalk. The assembly
sheet is kinematic — joint centers sit on their station lines — because that is what the
stack of stations means. Where the two disagree, the parts sheet is the honest one.

    uv run python make_plans.py
"""

from __future__ import annotations

import math
import sys

from stickbot import hinge_spring, repo_root

# The sheets land with the other generated drawings, not inside a guide. A generator that
# writes into instructions/ ties the design source to whichever guide happened to be current
# when the path was typed: this one wrote into robot-guide, which teaches a 150 mm robot
# where HEIGHT is now 318 mm. A guide takes a copy when it wants one, deliberately.
IMAGES = repo_root() / ".docs" / "experiments" / "build-briefs" / "images"

# ---------------------------------------------------------------- the numbers

TORSO_W, TORSO_H, TORSO_D = 72, 96, 48
HEAD_W = TORSO_W          # 72 — the head is as wide as the body, and reads that way
HEAD_H = HEAD_W           # 72 — a square front
HEAD_D = TORSO_D * 5 / 4  # 60 — a quarter deeper than the body, so it hangs 6 over each face
LIMB = TORSO_H / 4       # 24 — limb rod across, a quarter of the torso's height
LIMB_CENTER = 48         # one limb segment, joint center to joint center
SHOULDER_INSET = 5       # shoulder ball center, down from the upper arm's top end
GRIPPER_L = 24              # wrist center to the bottom of the gripper
FOOT_H = 24                 # ankle center to the sole
FOOT_L, FOOT_W = 4 * FOOT_H, 2 * FOOT_H   # 96 × 48 — the sole, toe to heel and across
RIB_W, RIB_D = FOOT_H / 4, FOOT_H / 12    # 6 × 2 — one tread groove, across the sole
RIB_STEP = 2 * RIB_W                      # 12 — groove and land, and it divides FOOT_L by 8
RIB_N = int(FOOT_L // RIB_STEP)           # 8
# The groove sits in the middle of its own repeat, so the pattern starts and ends with
# land rather than with a groove and the two margins come out the same. That margin is
# RIB_W / 2 and it derives from the groove alone — draft9p0 offset the pattern by
# #foot_l - #heel_y, a heel dimension that has nothing to do with the tread, and put the
# whole run off the end of the foot.
RIB_0 = RIB_W / 2                         # 3 — first groove's near edge, in from the heel end
# The face. Written against the head's width so it follows it, and exact at HEAD_W 36,
# where it reproduces the eyes and mouth slot the sheets have always drawn.
# The eye is an ellipse, wider than it is tall, and both its shape and its place are the
# example stickbot's read off the model on 2026-08-25 and scaled: at HEAD_W 36 it draws
# a 8 x 4 ellipse centered 6 out and 4 up. A circle at 2/9 and r 5/36 reached y 26 on a
# head whose r12 upper rounds eat the front face above y 24, which is the collision.
# There is no pupil. It was a circle of radius HEAD_W / 18, which is the eye's own minor
# radius, so it touched the ellipse top and bottom and left no eye above or below it.
EYE_X, EYE_UP = HEAD_W / 6, HEAD_W / 9   # eye centers, out from and above the head's center
EYE_RX, EYE_RY = HEAD_W / 9, HEAD_W / 18  # major and minor radius — the major runs across
HEAD_ROUND = HEAD_W / 6                  # 12 — `upper rounds`, on the two arch edges
MOUTH_W, MOUTH_H = HEAD_W * 5 / 9, HEAD_W * 5 / 36
MOUTH_DN = HEAD_W * 13 / 72              # the mouth slot's top edge, below that center
CLIP_R = 5.0                # C-clip outer radius — holds BAR, so it does not scale
BALL, STALK, FIT = 12, 6, 0.08   # FIT is set, not scaled: a printing clearance
CAVITY = BALL / 2 + FIT  # 6.08 — cavity radius
# The mouth is the dimension and the ball's depth follows it, so that changing FIT changes
# how deep the ball sits and nothing else. 96% of the ball is the snap: the mouth is that
# much narrower than what goes through it. Dimension the depth instead and a looser FIT
# opens the mouth past the ball, and the joint stops holding.
BALL_LOSS = 0.10         # what a printed ball loses on its radius. The mouth is drawn
                         # twice this much narrower so the printed joint grips what the
                         # drawn one was meant to. It is the one protrusion loss measured
                         # on this printer — the hinge's Ø STUB axle came out 0.10 short a
                         # side — and a caliper across a printed ball replaces it
MOUTH = 0.96 * BALL - 2 * BALL_LOSS   # 11.32 — 94% of the ball drawn, 96% of it printed
GRIP = (CAVITY**2 - (MOUTH / 2) ** 2) ** 0.5   # 2.2205 — how deep the ball's center sits
STAND = BALL * 5 / 6     # 10 — how far a ball center stands off the face it grows from.
                         # Both halves of a ball joint reach this far: a stud stands its ball
                         # this clear of its own face and a socket reaches this far back from
                         # the same center to its root, so the joint is symmetric about the
                         # ball and each member gives up the same length of limb to it. What
                         # sets the number is the swing: at the joint's own limit the socket's
                         # rim comes within STAND - GRIP*cos - COLLAR_R*sin of the other
                         # member's face, which is 3.36 mm here, and shortening either half
                         # spends that clearance
COLLAR_WALL = TORSO_H * 3 / 160   # 1.8 — socket wall. Three tabs build a collar from it,
                         # so it is declared in the Variable Studio and nowhere else. The
                         # wall and SLIT_D together are the socket's spring: the four
                         # fingers the slits leave have to open the mouth by
                         # BALL / 2 - MOUTH / 2 to let the ball's equator through, and come
                         # back. Wall is the cheap half of that force and mouth is the dear
                         # half, because what a finger can open before it yields is set by
                         # its free length and its own far fiber and not by how much section
                         # it has: this fifth more wall buys 1.58 times the force for 7
                         # points of yield, where the mouth's 0.2 buys 1.27 times for 19.
                         # Together they reach 87% of PETG's yield at full opening, against
                         # 59% before. tools/socket_spring.py is where that is worked out
COLLAR_R = BALL / 2 + COLLAR_WALL   # 7.8 — the collar is BALL + 2 × the wall. FIT is
                         # left out on purpose: a printing clearance moves the hollow
                         # and nothing else, so the outside stays put when FIT changes
COLLAR_L = STAND         # 10 — the ball's center to the bottom of the socket, which is
                         # what the stud reaches the other way, so both halves of a ball
                         # joint are the same length from the center it turns about.
                         # Measured from the center and not from the mouth, so FIT moves the
                         # hollow and leaves the robot's height alone. It was COLLAR_R, which
                         # made the socket as deep as it was wide for no reason beyond that,
                         # and left the two halves 7.8 and 10
COLLAR_PROUD = COLLAR_L + GRIP   # 12.2205 — rim to root, which is what a drawing sees.
                         # FIT reaches this number and stops here
SLIT_W = 1.6             # the socket's relief slit, across
SLIT_D = GRIP + BALL / 3  # 6.2205 — cut from the mouth face down to BALL / 3 below the
                         # ball's center, where the cavity is still wider than the slit's
                         # inner edge. So the cut is a slot for all of it, and its depth is
                         # the fingers' free length. That length is the cheapest of the
                         # three ways to buy elastic opening: the opening goes as its
                         # square while the stiffness goes as its cube, where thinning the
                         # wall costs a cube for a first power. Widening the slit buys
                         # nothing at all, because width scales strength and stiffness
                         # alike and the ratio of the two is what opening means
_SLIT_FLOOR_R = (CAVITY ** 2 - (SLIT_D - GRIP) ** 2) ** 0.5   # 4.579 — how wide the cavity
                         # still is where the slits bottom out
SLIT_IN = _SLIT_FLOOR_R - COLLAR_WALL / 2   # 3.679 — how far from the axis a slit's inner
                         # end stops. It has to be inside the mouth radius, or the mouth
                         # cannot open, and inside the cavity where the slit bottoms out,
                         # or the cut ends blind instead of opening into the hollow
BAR = 3.2                # LEGO bar — the gripper holds one; nothing else uses it
CLIP_BORE = BAR + 0.1    # 3.3 — the clip turns on the bar, so the bore is not the bar
CLIP_MOUTH = 2.6         # the gap the bar snaps through, narrower than the bar
CLIP_W = 2 * COLLAR_R    # 15.6 — the body, both across the bar's axis and fore-and-aft at
                         # the top. The one dimension in the robot that another part sets:
                         # it is the collar's own diameter, so the socket standing on it is
                         # flush all the way round
CLIP_CHAM = COLLAR_R - CLIP_R   # 2.8 — the 45° chamfer that necks the platform to the clip.
                         # It lands on the mouth's upper lip, so nothing CLIP_W wide ever
                         # reaches the mouth
BLADE = 10.0             # the tongue, across
T_PRINT = 0.10           # how far one printed surface lands off where it was drawn. Two
                         # surfaces face each other everywhere in this joint, so every
                         # clearance in it is checked against 2 T_PRINT and not against one
LEAF_ROOT = 4.20         # one leaf, across, where it leaves the limb
LEAF_TIP = 1.50          # and at the tongue's tip. The leaf is a wedge because the taper is
                         # nearly free: taking the tip from 3.00 to 1.50 costs 4% of the
                         # detent torque, and giving the root 3.00 to 4.20 buys 31%
SLIT = BLADE - 2 * LEAF_ROOT   # 1.60 — the relief slit up the tongue's middle, at its root.
                         # It opens to 7.00 at the tip. Without it the tongue is stiffer than
                         # the ears by two orders and nothing a hand does moves it
WEDGES = 24              # wedges in a ring on each face of the tongue, and on each ear.
                         # Twenty-four of them puts a detent every 15°, which is the step the
                         # joint is wanted at. The ring pays for it in wedge width, and the
                         # crest is allowed to come to a point rather than hold a flat.
                         # Both members carry protrusions now, so a detent is a wedge sitting
                         # between two wedges, and there are no holes anywhere in the joint.
                         # The old joint's detent was a cone dropping into a hole through the
                         # ear, and the printer put supports in those holes: measured, the
                         # joint held 210 N·mm where it was drawn for 454, and 0.235 of
                         # residue left in a valley — one extrusion width — accounts for it
WEDGE_H = 0.75           # how far a wedge stands proud of its face. A wedge is a pie slice
                         # with 45° sides, so it prints on both flanks without support
WEDGE_C = 0.15           # and how much air is left over its tip at a detent. This is inside
                         # 2 T_PRINT rather than outside it, so a crest that over-prints can
                         # land on the face opposite instead of clearing it. What that costs
                         # is 0.05 of flank engagement, not a joint that will not seat, and
                         # the printed part is what says whether it happens at all
GAP = WEDGE_H + WEDGE_C  # 0.90 — tongue face to ear face at a detent. The old joint's 0.15
                         # was a seat the two faces rested on; this is a space a wedge stands
                         # in, and the faces never touch
SEAT = BLADE + 2 * GAP   # 11.80 — the slot, one width from the fork's tip to its root, so
                         # the ear's whole inner face faces the tongue's
EAR = (LIMB - SEAT) / 2  # 6.10 — the ear is whatever the seat leaves of the limb
CLIMB = 2 * WEDGE_H - GAP   # 0.60 — how far the pair opens to ride from one detent to the
                         # next. Crest on crest the two wedges need 2 WEDGE_H between the
                         # faces, and GAP of that is already there
STUB = 4.0               # the axle across the blade, into a bore through each ear
STUB_PROUD = 2 * WEDGE_H + 1.50   # 3.00 — how far it stands off each face of the blade. It
                         # has to beat 2 WEDGE_H, or the joint lets go of the pin every time
                         # it crosses a detent; the old joint never had to, because its GAP
                         # was smaller than one tooth. What is left holding while riding over
                         # a crest is the 1.50, and at a detent it is ENGAGED
BORE_D = STUB + 0.1      # 4.1 — the bore that takes it, 0.05 of clearance a side. That is
                         # inside one T_PRINT, so whether it is a clearance or an interference
                         # is a question about the printer and not about the drawing
NOSE = LIMB / 2          # every end is rounded on this, about the pin axis
BLADE_OUT = 32           # how far the blade stands out of its own limb
SLOT_DEEP = BLADE_OUT + 1   # the slot that swallows it, from the fork's tip

# A limb prints lying down, its axis along the bed and the chord in the build direction, so
# the top and the bottom of a limb are the two faces the printer has the most trouble with:
# a Ø LIMB rod lying down meets the bed on a line and closes over the top on an overhang.
# Both are cut flat, and where they are cut is not free. The highest material the fork has is
# where the ear's inner face crosses the rod, so a flat there takes 1.55 off the rod's top and
# bottom and nothing at all off the fork. The leaf's inner edge stands 1.52 higher than that
# and loses its top and bottom to the cut, which is 9% of one leaf's stiffness and the only
# thing the cut costs. That was 5% before the leaf was widened to LEAF_ROOT: a wider leaf roots
# closer to the limb's axis, where the rod is tallest and the flat takes the most off it.
FLAT = math.sqrt(NOSE**2 - (SEAT / 2) ** 2)   # 10.4494 — the cut, off the limb's axis
LIMB_FLAT = 2 * FLAT                          # 20.8988 — the limb, top to bottom

# Where the ring of wedges goes. The ring runs out to the edge of the face rather than
# stopping short of it: at FLAT the two ends of the ring touch the limb's top and bottom cut,
# which is as far out as a wedge can reach and the longest lever the detent can act on. Both
# faces are FLAT tall and both carry wedges, so there is one ring and both members get the
# same one.
RING_OUT = FLAT          # 10.4494 — the ring's outer radius, which a wedge runs right out to
RING_IN = 6.0            # and its inner radius. Every wedge runs the whole ring, so this is
                         # also how far in a flank still has material to bear on
RING_CON = RING_OUT - WEDGE_H   # 9.6994 — where a flank actually bears, one wedge height in
                         # from the tip, and the lever the detent torque acts on

# How wide one wedge is. Two things set it, and only one of them is obvious.
#
# The obvious one: a wedge has to fit the half-step gap the mating ring leaves, with room
# for the printer to miss. That room is a length, 2 T_PRINT per flank, but a pie slice's
# room is an angle, so the radius it is measured at settles the angle.
#
# The one that is easy to miss: the two faces sit GAP apart and every flank is drafted 45°,
# so a flank leans inward by its own height above its own face. Both members lean, away
# from each other, and half way up the gap each has leaned GAP / 2. Measure the clearance
# anywhere but there and the wedge comes out too narrow — at 180 / WEDGES it comes out a
# third too narrow, and the joint turns half a step before it touches anything.
#
# Half way up is also where the two radial ends have taken the least off the outer radius,
# because they are drafted 45° as well. So one height and one radius settle the whole fit.
WEDGE_BIND = RING_OUT - GAP / 2   # 9.9994 — the radius the fit is set at, which is the
                         # ring's tip less what the radial draft has eaten by mid-gap
WEDGE_INSET = 2 * math.degrees(math.asin(GAP / 2 / WEDGE_BIND))   # 5.1587 — the two leans
WEDGE_EPS = math.degrees(2 * T_PRINT / WEDGE_BIND)   # 1.1460 — the room a flank needs there
WEDGE_W = 180 / WEDGES + WEDGE_INSET - WEDGE_EPS   # 11.5127 — one wedge, across, at its base
BACKLASH = 2 * WEDGE_EPS   # 2.2920 — how far the joint turns at a detent before a flank
                         # touches. It is the price of a joint that goes together at all, and
                         # it is paid. Halving the step barely moves it, because it is set by
                         # T_PRINT and a radius and not by the pitch, so it went from 8% of a
                         # 30° step to 15% of a 15° one

PETG_E, PETG_YIELD = hinge_spring.E_PETG, hinge_spring.YIELD_PETG   # MPa

# ------------------------------------------------------------- how the hinge springs
#
# Three numbers come out of this: what it takes to pinch the joint together, what it takes
# to turn it once it is together, and what it takes to wring it apart. They are three load
# cases and they do not share an answer.
#
# Pinching, a hand squeezes the two leaves toward each other until the axle clears the ear's
# face, and then slides the tongue in. That is the whole assembly force, and it replaced
# pushing the tongue down the slot as a wedge, which was several times harder and rose all
# the way in. The ear takes no part in it, so this is the leaf alone.
#
# Turning, the joint is seated, the axle is home in its bore carrying nothing, and every
# wedge is asked to climb its CLIMB at once. Two of them do. The rest ride clear, because
# both members are beams: lifting the wedge on the short lever lifts everything outboard of
# it by more than that wedge's own climb.
#
# Twisting, the joint is straight and gets wrung about the limb's axis. Each leaf tilts
# against its ear, the wedge tips jam diagonally — one leaf at the top, the other at the
# bottom — and those two contacts push each leaf in and each ear out, both of which work the
# axle out of its bore.
#
# Which is why this is a contact problem and not a formula, and why it lives in
# tools/hinge_spring.py. Adding the wedges up as independent springs overstates it several
# times over. .docs/reviews/hinge/ has the derivation and the sweeps behind the geometry
# above.
#
# The pinch and the detent are not independent, which is what makes this joint hard to size.
# Both are the same leaf bending over the same span, root to pin, so a leaf thick enough to
# hold a detent is a leaf too stiff to pinch. Only WEDGE_H separates them: it sets how far
# the pair has to open to turn, without touching how far it has to close to assemble.
#
# The free lengths are what makes the joint pinchable. Every end is rounded on NOSE about
# the pin, so the fork's ear tips sweep NOSE from the axis and the blade's limb has to end
# NOSE clear of them or the joint cannot close. That gives 2 * NOSE as the shortest
# BLADE_OUT the joint can close at; it does not give the right one. BLADE_OUT is typed
# longer than that on purpose, because the nine millimeters it buys are free length and
# free length is the only thing that makes this a joint a hand can pinch.
#
# Each member is rooted where its own cut stops, and the limb's rod has to stop there too:
# a rod run on past the slot's root would fill the slot back in and root the ear at NOSE
# instead, which is a factor of five in 1 / L^3.

TAB_FREE = BLADE_OUT - NOSE             # 20 — the tongue's root to the pin
EAR_FREE = SLOT_DEEP - NOSE             # 21 — the slot's root to the pin
# The plain Ø LIMB rod between the two ends, which is what a printer sees. Three, because
# a rod's length is set by the joint at each end and the robot has three combinations.
ROD_ARM = LIMB_CENTER + SHOULDER_INSET - EAR_FREE   # 32 — upper arm: side socket, fork
ROD_FORK = LIMB_CENTER - COLLAR_L - EAR_FREE        # 17 — thigh: socket up, fork
ROD_BLADE = LIMB_CENTER - STAND - TAB_FREE          # 18 — forearm and shin: blade, stud

HINGE = hinge_spring.Hinge(
    limb=LIMB, blade=BLADE, leaf_root=LEAF_ROOT, leaf_tip=LEAF_TIP, gap=GAP,
    tab_free=TAB_FREE, ear_free=EAR_FREE, blade_out=BLADE_OUT, ring_r=RING_CON,
    ring_n=WEDGES, climb=CLIMB, stub_proud=STUB_PROUD, nose=NOSE, flat=FLAT)

PINCH_AT = 30            # where a finger lands on the leaf, out from the tongue's root. At
                         # the tip it is 32 and the pinch is easier; two millimeters further
                         # in it is 28 and the pinch is over what a hand should be asked for
MU = 0.35                # PETG on PETG, dry
MOVE = CLIMB                            # 0.60 — what the pair opens to pass a wedge
ENGAGED = STUB_PROUD - GAP              # 2.10 — how much axle is still in the bore at a
                                        # detent. The axle has to out-engage the wedge, or
                                        # the joint lets go of the pin before it lets go of
                                        # a detent and the blade walks out of the fork
PINCH_F, PINCH_STRESS, PINCH_ROOM = hinge_spring.pinch(HINGE, PINCH_AT)   # N, MPa, mm
HOLD_T, HOLD_WEDGES, EAR_STRESS, LEAF_STRESS = hinge_spring.hold(HINGE)   # N·mm, count, MPa
HOLD_MU = hinge_spring.hold(HINGE, mu=MU)[0]   # N·mm, what a hand actually feels
TWIST_T, TWIST_DEG = hinge_spring.twist(HINGE)  # N·mm and degrees, and both are floors
HOLD_HAND = HOLD_T / 150 / 9.81         # kgf at a hand 150 mm out from the elbow
ARM_DROOP = 26                          # N·mm the elbow needs just to hold the arm up
EAR_MOVE = MOVE

SHOULDER_EL = 53         # the shoulder stud, degrees below horizontal
SHOULDER_AZ = 30         # and degrees toward the front
SHOULDER_L = TORSO_H * 13 / 48   # 26 — side face to ball center, along that stud. The odd
                         # fraction is where the clearance below landed, not a chosen ratio
SHOULDER_DROP = TORSO_H / 12     # 8 — where the stud roots, below the torso's top
BOSS_D = BALL * 4 / 3    # 16 — the boss carrying it, coaxial with the stalk. A third wider
                         # than the ball, so the shoulder around it is BALL / 6 at any size
ELBOW_BEND = 45          # how far the elbow is drawn bent

# ------------------------------------------------- what those angles come to
#
# The stud leaves the torso's side face at SHOULDER_EL below horizontal and
# SHOULDER_AZ toward the front. Only its last STAND is a Ø STALK stalk; the rest is
# a Ø BOSS_D boss, coaxial with that stalk.
#
# Coaxial is the whole trick. A boss square to the side face hangs below the ball,
# and the arm hits it on the way in — worse than no boss at all. Everything a coaxial
# boss occupies sits behind the ball along the stud axis, and the socket only ever
# reaches forward of that, so it cannot cost a degree of swing.
#
# Leaving a vertical face at this angle, the boss traces an ellipse 3.66 mm tall for
# every mm of its diameter, and that runs past the top of a 96 mm torso. It is cut off
# flush there. The cut costs nothing: it takes the part that was never in the way.
#
# SHOULDER_L is set by the torso, not by the joint. The arm is a Ø LIMB rod, so a ball
# standing STAND clear left the rod fouling the torso through the first 12.19° of its
# travel. At 26 along the stud the ball stands 13.55 clear, the whole arc is free, and
# the closest the arm comes to the torso anywhere in it is 1.46. The angle is the same
# at any size — it is a ratio of lengths that all scale together.
#
# The arm does not follow the stud forward. It hangs in a plane parallel to the
# front plane, which is what makes the front elevation true length, and the ball
# takes up the difference — ARM_OFF_STUD is what that costs out of BALL_SWING.

_EL, _AZ = math.radians(SHOULDER_EL), math.radians(SHOULDER_AZ)
STUD_D = (math.cos(_EL) * math.cos(_AZ), -math.cos(_EL) * math.sin(_AZ), -math.sin(_EL))
STUD_R = math.hypot(STUD_D[0], STUD_D[2])   # how much of the stud a front elevation sees
BOSS_L = SHOULDER_L - STAND                 # the fat part; the last STAND is Ø STALK stalk
SH_DX = SHOULDER_L * STUD_D[0]              # ball center, out from the side face
SH_DZ = -SHOULDER_L * STUD_D[2]             # and down from where the stud roots
ARM_PLANE_Y = SHOULDER_L * STUD_D[1]        # how far forward the arm plane sits
ARM_ANGLE = math.degrees(math.atan2(STUD_D[0], -STUD_D[2]))   # from vertical, in that plane
ARM_OFF_STUD = math.degrees(math.acos(STUD_R))

# How far any ball swings before its stalk meets the mouth. Both ways, so the
# cone is twice this. Nothing outside a socket reaches its own ball first.
BALL_SWING = math.degrees(math.acos((STALK / 2) / CAVITY) - math.asin(GRIP / CAVITY))

# What that cone leaves the arm, once the arm is held to a plane. The cone cuts that
# plane in an arc, and the arm is free anywhere along it.
_ARC = math.degrees(math.acos(math.cos(math.radians(BALL_SWING)) / STUD_R))
ARM_LO, ARM_HI = ARM_ANGLE - _ARC, ARM_ANGLE + _ARC

STYLE = """
  .part  { fill:#dfe7ec; stroke:#1d262e; stroke-width:0.9; stroke-linejoin:round; }
  .ghost { fill:#eef2f5; stroke:#8ea0ad; stroke-width:0.7; stroke-linejoin:round; }
  .void  { fill:#ffffff; stroke:#1d262e; stroke-width:0.9; stroke-linejoin:round; }
  .mate  { fill:#f6f9fa; stroke:#1d262e; stroke-width:0.9; stroke-linejoin:round; }
  .hid   { fill:none; stroke:#5b6b78; stroke-width:0.4; stroke-dasharray:2 1.4; }
  .dim   { stroke:#b8156e; stroke-width:0.35; fill:none; }
  .dimt  { fill:#b8156e; font-size:4.2px; font-weight:700; }
  .name  { fill:#12303c; font-size:5px; font-weight:700; letter-spacing:0.06em; }
  .call  { fill:#43525e; font-size:3.4px; }
  .lead  { stroke:#8ea0ad; stroke-width:0.3; fill:none; }
  .lbl   { fill:#43525e; font-size:4.6px; font-weight:700; letter-spacing:0.12em; }
  .note  { fill:#6b7a88; font-size:3.6px; }
  .warn  { fill:#b8156e; font-size:3.6px; font-weight:700; }
  .ctr   { stroke:#7f8f9c; stroke-width:0.3; stroke-dasharray:6 2 1 2; }
  .stn   { stroke:#0b6e86; stroke-width:0.25; stroke-dasharray:3 2; }
  .gnd   { stroke:#0b6e86; stroke-width:0.8; }
  .tooth { stroke:#1d262e; stroke-width:0.5; fill:none; }
  .det * { vector-effect: non-scaling-stroke; }
  .fig * { vector-effect: non-scaling-stroke; }
"""

# ---------------------------------------------------------------- primitives


def chord(a):
    """The full width of the limb circle at a cut a mm off its axis."""
    return 2 * ((LIMB / 2) ** 2 - a**2) ** 0.5


def limb_d(r, f):
    """The limb's cross-section as a path: a Ø 2r circle with the top and the bottom cut
    flat f off the axis. Drawn with the chord across the page, so the two cuts are its ends
    and the two arcs are what is left of the rod."""
    h = (r * r - f * f) ** 0.5
    return (f'M {f:g},{-h:g} V {h:g} A {r:g},{r:g} 0 0 1 {-f:g},{h:g} '
            f'V {-h:g} A {r:g},{r:g} 0 0 1 {f:g},{-h:g} Z')


def flatted(r, f, cls="part"):
    return f'<path class="{cls}" d="{limb_d(r, f)}"/>'


def rect(x, y, w, h, cls="part"):
    return f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}"/>'


def ellipse(cx, cy, rx, ry, cls="part"):
    return f'<ellipse class="{cls}" cx="{cx:g}" cy="{cy:g}" rx="{rx:g}" ry="{ry:g}"/>'


def circle(cx, cy, r, cls="part"):
    return f'<circle class="{cls}" cx="{cx:g}" cy="{cy:g}" r="{r:g}"/>'


def text(x, y, s, cls="call", anchor="start", rot=None):
    t = f' transform="rotate({rot} {x:g} {y:g})"' if rot is not None else ""
    return f'<text class="{cls}" x="{x:g}" y="{y:g}" text-anchor="{anchor}"{t}>{s}</text>'


def mm(v):
    """A derived length, written the way a drawing writes one — no false precision."""
    return f"{v:.2f}".rstrip("0").rstrip(".")


def leader(pts):
    d = " ".join(("M" if i == 0 else "L") + f"{x:g},{y:g}" for i, (x, y) in enumerate(pts))
    return f'<path class="lead" d="{d}"/>'


def arch(x, top, w, h, cls="part"):
    """A head outline: a rectangle capped by a semicircle of half its width.

    The head's profile is a radius and a straight length, both HEAD_W / 2, and that is
    what makes the front square. Both sheets drew it as a plain rectangle until
    draft9p1, so the head on the page did not have the shape of the head in the model.
    """
    r = w / 2
    return (f'<path class="{cls}" d="M {x:g},{top + h:g} V {top + r:g} '
            f'A {r:g},{r:g} 0 0 1 {x + w:g},{top + r:g} V {top + h:g} Z"/>')


def rod(x, y, ang, length, w=LIMB, cls="part"):
    """A rod `w` across, hanging from a joint center at (x, y).

    `ang` is degrees off straight down, positive swinging toward +x. Sheet
    coordinates, so the rotation is negated to turn that way on a y-down page.
    """
    return (f'<rect class="{cls}" x="{-w / 2:g}" y="0" width="{w:g}" height="{length:g}" '
            f'transform="translate({x:.4f},{y:.4f}) rotate({-ang:.4f})"/>')


def shoulder(x, y, sx, top, uid):
    """The shoulder stud, leaving the torso's side face at (x, y). sx is +1 or -1.

    A fat boss for BOSS_L, then a Ø STALK stalk for the last STAND, both on one axis.
    Drawn foreshortened by STUD_R, because the stud also leans into the page.

    `top` is where the torso's top face crosses this view. The boss runs past it, so it
    is cut there — which is why the boss can be as fat as it needs to be without the
    shoulder growing a horn.
    """
    a = sx * ARM_ANGLE
    ar = math.radians(ARM_ANGLE)
    ax, ay = sx * math.sin(ar), math.cos(ar)          # along the stud, down and outward
    px, py = sx * math.cos(ar), -math.sin(ar)         # across it
    bx, by = x + sx * BOSS_L * STUD_D[0], y + BOSS_L * -STUD_D[2]

    # The two long edges run back to the face rather than stopping square across the
    # axis, which is what makes the boss grow out of the torso instead of float beside
    # it. Where they meet the face is the top and bottom of its elliptical footprint.
    pts = []
    for s in (1, -1):
        cx, cy = bx + s * BOSS_D / 2 * px, by + s * BOSS_D / 2 * py
        t = (cx - x) / ax
        pts.append(((cx, cy), (cx - t * ax, cy - t * ay)))
    (b, a_), (c, d) = pts
    body = (f'<path class="part" d="M {a_[0]:.3f},{a_[1]:.3f} L {b[0]:.3f},{b[1]:.3f} '
            f'L {c[0]:.3f},{c[1]:.3f} L {d[0]:.3f},{d[1]:.3f} Z"/>'
            + rod(bx, by, a, STAND * STUD_R, STALK))
    return (f'<clipPath id="sh{uid}">'
            f'<rect x="-400" y="{top:g}" width="800" height="800"/></clipPath>'
            f'<g clip-path="url(#sh{uid})">{body}</g>')


def stud(x, y, d, cls="part"):
    """A ball stud growing out of a face at (x, y), pointing d. Ball center stands STAND off."""
    s, r = STALK / 2, BALL / 2
    box = {
        "up": (x - s, y - STAND, 2 * s, STAND),
        "down": (x - s, y, 2 * s, STAND),
        "left": (x - STAND, y - s, STAND, 2 * s),
        "right": (x, y - s, STAND, 2 * s),
    }[d]
    cx, cy = {
        "up": (x, y - STAND), "down": (x, y + STAND),
        "left": (x - STAND, y), "right": (x + STAND, y),
    }[d]
    return rect(*box, cls) + circle(cx, cy, r, cls)


def socket(x, y, d, cls="void"):
    """A spherical cavity opening through a face at (x, y), facing d.

    The cavity center sits GRIP inside the face, so the mouth is narrower than the ball.
    Drawn as a white void with the mouth on the face line.
    """
    m, g, c = MOUTH / 2, GRIP, CAVITY
    if d in ("up", "down"):
        sgn = 1 if d == "up" else -1          # 'up' = opens upward, material below
        cy = y + sgn * g
        p = (f'M {x - m:g},{y:g} A {c:g},{c:g} 0 1 {0 if sgn > 0 else 1} {x + m:g},{y:g}')
    else:
        sgn = 1 if d == "left" else -1        # 'left' = opens to the left
        cx = x + sgn * g
        p = (f'M {x:g},{y - m:g} A {c:g},{c:g} 0 1 {1 if sgn > 0 else 0} {x:g},{y + m:g}')
    return f'<path class="{cls}" d="{p} Z"/>'


# ---------------------------------------------------------------- the parts


def torso():
    """Front view. Origin at the torso center — which is the model origin."""
    w, h = TORSO_W / 2, TORSO_H / 2
    # Shoulders first, so the torso's own outline paints over the buried end of each.
    g = [shoulder(sx * w, -h + SHOULDER_DROP, sx, -h, f"p{i}")
         for i, sx in enumerate((-1, 1))]
    g += [rect(-w, -h, TORSO_W, TORSO_H)]
    g += [circle(sx * (w + SH_DX), -h + SHOULDER_DROP + SH_DZ, BALL / 2) for sx in (-1, 1)]
    g += [stud(0, -h, "up")]                                   # neck
    g += [stud(-12, h, "down"), stud(12, h, "down")]           # hips
    g += [f'<line class="ctr" x1="0" y1="{-h - 14:g}" x2="0" y2="{h + 14:g}"/>']
    g += [
        leader([(-2.6, -h - STAND - 1.5), (-14, -h - 13)]),
        text(-15 * PAGE, -h - 12 * PAGE, "+ neck ball stud", anchor="end"),
        leader([(w + SH_DX + 3, -h + SHOULDER_DROP + SH_DZ), (w + 16, -h + 4)]),
        text(w + 16 + PAGE, -h + 4 + PAGE, "+ shoulder ball stud"),
        text(w + 16 + PAGE, -h + 4 + 5.6 * PAGE,
             f"{SHOULDER_EL}&#176; down, {SHOULDER_AZ}&#176; forward"),
        leader([(w + 3, -h + 3), (w + 16, -h + 23)]),
        text(w + 16 + PAGE, -h + 23 + PAGE, f"&#216;{BOSS_D:g} boss on the same axis,"),
        text(w + 16 + PAGE, -h + 23 + 5.6 * PAGE, "cut flush at the top face"),
        leader([(12, h + STAND + 3), (12, h + 13), (26, 13 + h)]),
        text(27 * PAGE, h + 14 * PAGE, "+ hip ball stud"),
        text(0, h + 24 * PAGE, "TORSO", "name", "middle"),
        text(0, h + 31 * PAGE, f"{TORSO_W} &#215; {TORSO_H} &#215; {TORSO_D} mm",
             "note", "middle"),
    ]
    return "".join(g)


def face(cx, cy):
    """The eyes and mouth, in page-down coordinates about the head's center.

    Both sheets drew this from literals — ±8, r5, r2, a 20 × 5 slot — which stayed
    put when the head doubled. It follows HEAD_W now.
    """
    return [ellipse(cx - EYE_X, cy - EYE_UP, EYE_RX, EYE_RY),
            ellipse(cx + EYE_X, cy - EYE_UP, EYE_RX, EYE_RY),
            f'<rect class="part" x="{cx - MOUTH_W / 2:g}" y="{cy + MOUTH_DN:g}" '
            f'width="{MOUTH_W:g}" height="{MOUTH_H:g}" rx="{MOUTH_H / 2:g}"/>']


def head():
    """Front view. Origin at the head center.

    The neck socket is the same collar every other socketed part carries: Ø 2 × coll_r
    standing COLLAR_PROUD of the underside, with the cavity inside it. Drawing it as
    a face-bored socket is what the head was built to through run 5, and it cost the
    joint its relief slits and half its tilt.
    """
    w, coll_r = HEAD_W / 2, COLLAR_R
    rim = w + COLLAR_PROUD                 # the collar's mouth face, below the underside
    g = [arch(-w, -w, HEAD_W, HEAD_H)]
    g += face(0, 0)
    g += [rect(-coll_r, w, 2 * coll_r, COLLAR_PROUD)]    # the collar, standing proud
    g += [socket(0, rim, "down")]
    g += [f'<path class="hid" d="M {-SLIT_W / 2:g},{rim:g} V {rim - SLIT_D:g} '
          f'M {SLIT_W / 2:g},{rim:g} V {rim - SLIT_D:g}"/>']   # relief slits, cut up from
                                                       # the rim and stopping short of the root
    g += [
        leader([(coll_r, w + COLLAR_PROUD / 2), (16, w + 4)]),
        text(17 * PAGE, w + 5 * PAGE, f"+ neck socket, collar &#216;{2 * coll_r:g}"),
        text(17 * PAGE, w + 10 * PAGE,
             f"{mm(COLLAR_PROUD)} mm proud, {SLIT_W:g} mm slits {mm(SLIT_D)} mm deep"),
        leader([(EYE_X, -EYE_UP), (20 * PAGE, -20 * PAGE)]),
        text(21 * PAGE, -20 * PAGE, "eye"),
        leader([(MOUTH_W / 4, MOUTH_DN + MOUTH_H / 2), (20 * PAGE, 16 * PAGE)]),
        text(21 * PAGE, 17 * PAGE, "mouth &#8212; slot"),
        text(0, rim + 12 * PAGE, "HEAD", "name", "middle"),
        text(0, rim + 19 * PAGE, f"{HEAD_W:g} &#215; {HEAD_H:g} &#215; {HEAD_D:g} mm",
             "note", "middle"),
        text(0, rim + 26 * PAGE, f"arch r{HEAD_W / 2:g}, top edges rounded r{HEAD_ROUND:g}",
             "note", "middle"),
    ]
    return "".join(g)


def fork(x, y):
    """Fork end, front view: rounded end, the bore, and the slot walls shown hidden.

    `y` is the pin. The fork stands EAR_FREE out of its own rod's end face, which is where
    the slot's root is, so the two ears are that long before the round end starts.
    """
    r, s = LIMB / 2, SEAT / 2
    root, tip = y - EAR_FREE, y + math.sqrt(NOSE**2 - s**2)
    return "".join([
        f'<path class="part" d="M {x - r:g},{root:g} L {x - r:g},{y:g} '
        f'A {r:g},{r:g} 0 0 0 {x + r:g},{y:g} L {x + r:g},{root:g} Z"/>',
        circle(x, y, BORE_D / 2, "void"),
        f'<path class="hid" d="M {x - s:g},{root:.3f} V {tip:.3f} '
        f'M {x + s:g},{root:.3f} V {tip:.3f} M {x - s:g},{root:.3f} H {x + s:g}"/>',
    ])


def blade(x, y):
    """Tongue end, front view. `y` is the rod's end face; the tongue stands out of it.

    The rod stops at the tongue's root and not at the pin, because a rod run on past it
    would fill the fork's slot back in. That root is TAB_FREE from the pin, and it is the
    tongue's free length: how far it can bend when the ears spread to take it.
    """
    pin = y - TAB_FREE
    return "".join([
        f'<path class="part" d="M {x - BLADE / 2:g},{y:g} L {x - BLADE / 2:g},{pin:g} '
        f'A {NOSE:g},{NOSE:g} 0 0 1 {x + BLADE / 2:g},{pin:g} L {x + BLADE / 2:g},{y:g} Z"/>',
        rect(x - SLIT / 2, pin - NOSE, SLIT, TAB_FREE + NOSE, "void"),
        circle(x, pin, STUB / 2),
    ])


def limb(kind, center, top, bottom, name):
    """A limb rod, drawn hanging downward, with a joint at each end.

    `center` is the joint center to joint center distance — `#limbCenter`, the number the
    elevation spaces the stations by. The rod is shorter or longer than that, because neither
    joint puts its center on the end of the rod it grows from: a socket sinks its cavity center
    GRIP inside the face, and a ball stud stands its center STAND clear of the face. So the rod
    length is derived here, from which joint is at which end, and the sheet labels the stock.
    """
    r = LIMB / 2
    # Where each end's joint center sits, relative to the rod's own end face. A socket
    # standing up out of the rod puts its ball COLLAR_L above the face, because the rod's
    # face is the socket's root; a tongue standing out of the rod puts the pin TAB_FREE
    # above it; the shoulder's socket is in a side face, SHOULDER_INSET down from the top.
    top_at = {"socket-side": SHOULDER_INSET, "socket-up": -COLLAR_L,
              "blade": -TAB_FREE}[top]
    # And where the rod stops at the far end, back from that joint's center. A fork stops
    # at the slot's root and not at the pin; a rod run on to the pin fills the slot in.
    bottom_at = {"fork": EAR_FREE, "stud": STAND}[bottom]
    length = center + top_at - bottom_at
    size_note = (f"&#216;{LIMB:g} &#215; {mm(length)} mm rod, flat to {mm(LIMB_FLAT)} mm, "
                 f"joint centers {center:g} mm")
    g = [rect(-r, 0, LIMB, length)]
    calls = []
    if top == "socket-side":                       # shoulder: cavity in the inboard face
        g += [socket(-r, SHOULDER_INSET, "right")]
        calls += [leader([(-r + 1, SHOULDER_INSET), (-r - 18, SHOULDER_INSET - 3)]),
                  text(-r - 19 * PAGE, (SHOULDER_INSET - 2) * PAGE, "+ shoulder socket",
                       anchor="end")]
    elif top == "socket-up":
        # The collar is narrower than the limb, so it stands proud as its own shape.
        g += [rect(-COLLAR_R, -COLLAR_PROUD, 2 * COLLAR_R, COLLAR_PROUD),
              socket(0, -COLLAR_PROUD, "up")]
        calls += [leader([(COLLAR_R, -COLLAR_PROUD / 2), (-r - 16, -COLLAR_PROUD - 4)]),
                  text(-r - 17 * PAGE, (-COLLAR_PROUD - 3) * PAGE,
                       f"+ {kind} socket", anchor="end")]
    elif top == "blade":
        g += [blade(0, 0)]
        calls += [leader([(0, -TAB_FREE), (-r - 16, -TAB_FREE - 6)]),
                  text(-r - 17 * PAGE, (-TAB_FREE - 5) * PAGE, f"+ {kind} blade",
                       anchor="end")]
    if bottom == "fork":
        g += [fork(0, length + EAR_FREE)]
        calls += [leader([(0, length + EAR_FREE), (r + 16, length + EAR_FREE + 8)]),
                  text(r + 17, length + EAR_FREE + 9,
                       "+ elbow fork" if kind == "shoulder" else "+ knee fork")]
    elif bottom == "stud":
        g += [stud(0, length, "down")]
        calls += [leader([(0, length + STAND), (r + 16, length + 12)]),
                  text(r + 17, length + 13, "+ wrist ball stud" if kind == "elbow"
                       else "+ ankle ball stud")]
    g += calls
    g += [
        text(0, length + 30 * PAGE, name, "name", "middle"),
        text(0, length + 37 * PAGE, size_note, "note", "middle"),
    ]
    return "".join(g)


def clip(cx, cy, rot=0):
    """The gripper, seen from the side: a C-clip hanging GRIPPER_L below the wrist.

    Page-right is forward, and the mouth opens forward, because the robot faces
    forward and a clip that opens outward makes the left gripper the mirror of the
    right. The bore's axis runs left-right — square to this page — so the robot
    grips a bar that runs left-right, and the profile is sketched on the plane that
    holds both the mouth's direction and the part's length.

    Both sheets drew this the other way round until draft9p1: the C in the front
    elevation with the mouth opening straight down, which is a part that grips a bar
    pointing away from itself. `gripper.md`'s acceptance list names that exact
    mistake, because the profile is symmetric either way and every other check passes.

    The mouth is a parallel slot CLIP_MOUTH tall, so the two lips are that far apart
    the whole way out and the bar squeezes past the same gap however far in it is.
    Neither lip's angle is chosen: each circle is cut where it crosses CLIP_MOUTH / 2
    from the axis, which is a wider angle on the bore than it is on the outside.

    The body is CLIP_W wide at the top, the same as it is across the bar, so the
    socket stands on a square that is its own diameter and is flush all the way
    round. A 45 degree chamfer of leg CLIP_CHAM brings that width down to the clip's
    own, landing on the mouth's upper lip: below the lip the part is the clip circle
    and nothing else, so nothing CLIP_W wide is ever beside the mouth.

    `cy` is the wrist joint center, which is where the model's origin is. The socket's
    collar stands GRIP above it and its root is COLLAR_L below, and the collar is the
    platform's own diameter, so from the rim down to the chamfer the part is one
    CLIP_W column with no edge across it. That is why the outline starts at the rim
    and the collar needs no separate shape.

    `rot` turns the whole part about the wrist so it can follow a bent forearm.
    """
    ro, ri = CLIP_R, CLIP_BORE / 2
    c = cy + GRIPPER_L - ro
    lip = c - CLIP_MOUTH / 2         # the mouth's upper lip, where the chamfer lands
    cham = lip - CLIP_CHAM           # and where the platform stops being CLIP_W wide
    tho = math.asin(CLIP_MOUTH / (2 * ro))     # where the slot crosses the outside
    thb = math.asin(CLIP_MOUTH / (2 * ri))     # and where it crosses the bore
    po1 = (cx + ro * math.cos(tho), c + ro * math.sin(tho))
    po2 = (cx + ro * math.cos(-tho), c + ro * math.sin(-tho))
    pi1 = (cx + ri * math.cos(thb), c + ri * math.sin(thb))
    pi2 = (cx + ri * math.cos(-thb), c + ri * math.sin(-thb))
    body = (f'<path class="part" d="M {cx - CLIP_W / 2:g},{cy - GRIP:g} '
              f'H {cx + CLIP_W / 2:g} V {cham:g} L {cx + CLIP_R:g},{lip:g} '
              f'V {c:g} H {cx - CLIP_R:g} V {lip:g} '
              f'L {cx - CLIP_W / 2:g},{cham:g} Z"/>'
            + f'<path class="part" d="M {po1[0]:.3f},{po1[1]:.3f} '
              f'A {ro:g},{ro:g} 0 1 1 {po2[0]:.3f},{po2[1]:.3f} '
              f'L {pi2[0]:.3f},{pi2[1]:.3f} '
              f'A {ri:g},{ri:g} 0 1 0 {pi1[0]:.3f},{pi1[1]:.3f} Z"/>')
    if rot:
        return f'<g transform="rotate({-rot:.4f} {cx:.4f} {cy:.4f})">{body}</g>'
    return body


def clip_front(cx, cy, rot=0):
    """The same gripper seen from the front, where it is a slab and not a C.

    The body runs CLIP_W across — the collar's own diameter, so the top of the part
    is flush with the socket standing on it all the way round rather than being a
    shape that happens to be wide enough, and the collar carries that same width on
    up to the rim. `cy` is the wrist joint center. The bore crosses that whole width, so it
    is two hidden lines here and a circle only from the side. The chamfer that necks
    the body fore-and-aft leaves no silhouette in this view and the robot is drawn
    small here, so it stays on the parts sheet where the gripper has a figure of its
    own.
    """
    hw, c = CLIP_W / 2, cy + GRIPPER_L - CLIP_R
    body = (rect(cx - hw, cy - GRIP, CLIP_W, GRIPPER_L + GRIP)
            + f'<path class="hid" d="M {cx - hw:g},{c - CLIP_BORE / 2:g} h {CLIP_W:g} '
              f'M {cx - hw:g},{c + CLIP_BORE / 2:g} h {CLIP_W:g}"/>')
    if rot:
        return f'<g transform="rotate({-rot:.4f} {cx:.4f} {cy:.4f})">{body}</g>'
    return body


def gripper():
    """The gripper, drawn on its own. Origin at the wrist joint center."""
    cy = GRIPPER_L - CLIP_R
    g = [clip(0, 0), socket(0, -GRIP, "up")]     # mouth on the rim, ball center on 0
    g += [
        leader([(0, 0), (-16 * PAGE, -6 * PAGE)]),
        text(-17 * PAGE, -5 * PAGE, "+ wrist socket", anchor="end"),
        leader([(CLIP_R - 1, cy - 2), (18, 4)]),
        text(19 * PAGE, 5 * PAGE, f"clip &#8212; grips &#216;{BAR} mm bar"),
        leader([(CLIP_R, GRIPPER_L - CLIP_R), (18 * PAGE, 22 * PAGE)]),
        text(19 * PAGE, 23 * PAGE, f"mouth {CLIP_MOUTH:g} mm, opening forward"),
        leader([(CLIP_W / 2, COLLAR_L + 1), (16 * PAGE, -9 * PAGE)]),
        text(17 * PAGE, -8 * PAGE, f"platform {CLIP_W:g} &#215; {CLIP_W:g} mm"),
        leader([(CLIP_W / 2 - 1, GRIPPER_L - CLIP_R - CLIP_MOUTH / 2 - CLIP_CHAM + 1),
                (16 * PAGE, 13 * PAGE)]),
        text(17 * PAGE, 14 * PAGE, f"chamfer {CLIP_CHAM:g} mm at 45&#176;"),
        text(0, 46 * PAGE, "GRIPPER", "name", "middle"),
        text(0, 53 * PAGE, f"{GRIPPER_L:g} mm below the wrist &#8212; side view, "
                           f"{CLIP_W:g} mm across the bar", "note", "middle"),
    ]
    return "".join(g)


def foot():
    """Side view, toe to the right. Origin at the ankle joint center."""
    g = [
        f'<path class="part" d="M {-20 * FOOT_H / 12:g},{FOOT_H:g} h {FOOT_L:g} '
        f'a {5 * FOOT_H / 12:g} {5 * FOOT_H / 12:g} 0 0 0 {-FOOT_H / 12:g} {-8 * FOOT_H / 12:g} '
        f'q {-14 * FOOT_H / 12:g} {-FOOT_H / 3:g} {-46 * FOOT_H / 12:g} {-FOOT_H / 3:g} '
        f'a {5 * FOOT_H / 12:g} {5 * FOOT_H / 12:g} 0 0 0 {-FOOT_H / 12:g} {FOOT_H:g} z"/>',
        rect(-COLLAR_R, -GRIP, 2 * COLLAR_R, GRIP + FOOT_H / 2),   # the socket's boss,
        socket(0, -GRIP, "up"),                    # buried in the plate for its lower half
        f'<line class="gnd" x1="{-22 * FOOT_H / 12:g}" y1="{FOOT_H:g}" '
        f'x2="{30 * FOOT_H / 12:g}" y2="{FOOT_H:g}"/>',
    ]
    heel = -20 * FOOT_H / 12                       # the sole's heel end, in this view
    g += [rect(heel + RIB_0 + i * RIB_STEP, FOOT_H - RIB_D, RIB_W, RIB_D, "void")
          for i in range(RIB_N)]
    g += [
        leader([(0, 0), (-18 * PAGE, -6 * PAGE)]),
        text(-19 * PAGE, -5 * PAGE, "+ ankle socket", anchor="end"),
        leader([(22 * FOOT_H / 12, 8 * FOOT_H / 12), (34 * PAGE, 2 * PAGE)]),
        text(35 * PAGE, 3 * PAGE, "toe &#8212; the balance"),
        leader([(-20 * FOOT_H / 12 + RIB_0 + RIB_W / 2, FOOT_H), (-14 * PAGE, 26 * PAGE)]),
        text(-15 * PAGE, 27 * PAGE,
             f"tread &#8212; {RIB_W:g} mm grooves, {RIB_STEP:g} mm apart", anchor="end"),
        text(FOOT_L / 2 - 20 * FOOT_H / 12, 30 * PAGE, "FOOT", "name", "middle"),
        text(FOOT_L / 2 - 20 * FOOT_H / 12, 37 * PAGE,
             f"{FOOT_L:g} &#215; {FOOT_W:g} mm", "note", "middle"),
    ]
    return "".join(g)


# ---------------------------------------------------------------- the details


def _S():
    """The section details were drawn at 3:1 for a 1x robot. The ratio follows the
    design so the inset keeps the same size on the sheet. Labels are not scaled.
    """
    return 3.0 * TO_PAGE


def detail_ball(ox, oy):
    """Section through a ball and its socket. Geometry scaled S:1, labels at sheet size."""
    # The real clearance is 0.2 mm on a 6 mm ball — invisible even at 3:1 — so the cavity
    # is drawn oversize and said to be. Every number on the sheet is the real one.
    cav = BALL / 2 + 0.8 * PAGE
    m = (cav**2 - GRIP**2) ** 0.5
    art = [
        f'<path class="mate" d="M {-14 * PAGE:g},{GRIP:g} L {-m:g},{GRIP:g} '
        f'A {cav:g},{cav:g} 0 1 1 {m:g},{GRIP:g} L {14 * PAGE:g},{GRIP:g} '
        f'L {14 * PAGE:g},{-22 * PAGE:g} L {-14 * PAGE:g},{-22 * PAGE:g} Z"/>',
        rect(-10 * PAGE, STAND, 20 * PAGE, 14 * PAGE),        # inboard part
        stud(0, STAND, "up"),            # its ball stud — ball center lands at (0, 0)
    ]
    geo = f'<g transform="translate({ox:g},{oy:g}) scale({_S()})" class="det">{"".join(art)}</g>'

    def P(px, py):                       # a point on the drawing, in sheet coordinates
        return (ox + _S() * px, oy + _S() * py)

    lab = [
        text(ox, oy - 82, "BALL AND SOCKET, IN SECTION", "lbl", "middle"),
        leader([P(-11 * PAGE, -17 * PAGE), (ox - 50, oy - 54)]),
        text(ox - 52, oy - 53, "socket &#8212; the outboard part", anchor="end"),
        leader([P(-2.4 * PAGE, -1.9 * PAGE), (ox - 50, oy - 26)]),
        text(ox - 52, oy - 25, f"cavity &#216;{2 * CAVITY:g} mm", anchor="end"),
        text(ox - 52, oy - 18, "= ball + 2 &#215; fit", anchor="end"),
        leader([P(-m, GRIP), (ox - 50, oy + 10)]),
        text(ox - 52, oy + 11, f"grip {mm(GRIP)} mm &#8212; sets the mouth", anchor="end"),
        leader([P(m, GRIP), (ox + 50, oy - 20)]),
        text(ox + 52, oy - 19,
             f"mouth &#216;{MOUTH:.4g} mm &#8212; {100 * MOUTH / BALL:.0f}% of the ball"),
        leader([P(2.9 * PAGE, 0.4 * PAGE), (ox + 50, oy + 4)]),
        text(ox + 52, oy + 5, f"ball &#216;{BALL} mm"),
        leader([P(1.5 * PAGE, 3.8 * PAGE), (ox + 50, oy + 24)]),
        text(ox + 52, oy + 25, f"stalk &#216;{STALK} mm"),
        leader([P(8 * PAGE, 12 * PAGE), (ox + 50, oy + 46)]),
        text(ox + 52, oy + 47, "ball stud &#8212; the inboard part"),
        text(ox, oy + 76, "The ball stud goes on the part nearer the torso, the socket on the "
                          "part further out. Always.", "note", "middle"),
        text(ox, oy + 82, "Clearance drawn oversize to be visible; every number here is the "
                          "real one.", "note", "middle"),
    ]
    return geo + "".join(lab)


def detail_scale(ox, oy):
    """The joints drawn against the limb they have to fit inside. Same 3:1 as the sections.

    This is the check the other two details cannot make: they draw the joint alone, so a
    joint too big for its limb looks fine. Here the limb is drawn too.
    """
    r = LIMB / 2
    ear, bl, gap = EAR, BLADE, GAP
    art = [
        # left: the socket, cut into a limb seen end-on
        f'<g transform="translate({-13 * PAGE:g},0)">'
        f'{flatted(r, FLAT)}{circle(0, 0, CAVITY, "void")}</g>',
        # right: the fork, on a limb seen end-on. Each layer is clipped to the limb's
        # own outline, because every layer is a full slice of the limb and not a rectangle
        # inside it. The outline is the flatted one, so the cut shows where it bites: it
        # takes the tongue's two leaves down and stops on the ears without touching them.
        f'<clipPath id="limbslice"><path d="{limb_d(r, FLAT)}"/></clipPath>'
        f'<g transform="translate({12 * PAGE:g},0)">{flatted(r, FLAT, "ghost")}</g>'
        f'<g transform="translate({12 * PAGE:g},0)" clip-path="url(#limbslice)">'
        f'{rect(-r, -bl / 2 - gap - ear, LIMB, ear)}{rect(-r, bl / 2 + gap, LIMB, ear)}'
        f'{rect(-r, -bl / 2, LIMB, bl, "mate")}{rect(-r, -SLIT / 2, LIMB, SLIT, "void")}'
        f'</g>',
    ]
    geo = f'<g transform="translate({ox:g},{oy:g}) scale({_S()})" class="det">{"".join(art)}</g>'

    wall = (LIMB - 2 * CAVITY) / 2
    lab = [
        text(ox, oy - 44, "THE JOINTS AGAINST THE LIMB, TO SCALE", "lbl", "middle"),
        text(ox, oy + 48, "The fork is the whole limb with a slot through it, and the tongue "
                          "is what the slot took out.", "note", "middle"),
        text(ox, oy + 54, "Four springs, in two pairs: an ear and a leaf on each side, sharing "
                          "the movement between them.", "note", "middle"),
        text(ox - 39, oy + 30, f"&#216;{LIMB:g} mm limb, &#216;{2 * CAVITY:g} mm cavity",
             "call", "middle"),
        text(ox - 39, oy + 36, f"leaves {wall:g} mm of wall", "call", "middle"),
        text(ox - 39, oy + 42, f"flat top and bottom, {mm(LIMB_FLAT)} mm", "call", "middle"),
        text(ox + 36, oy + 30, f"slot {SEAT:g} mm through a {LIMB:g} mm limb", "call", "middle"),
        text(ox + 36, oy + 36, f"ear {ear:g} either side, tongue {bl:g} between",
             "call", "middle"),
        text(ox + 36, oy + 42, f"split by a {SLIT:g} slit into two leaves, "
                               f"{LEAF_ROOT:g} at the root", "call", "middle"),
    ]
    return geo + "".join(lab)


def detail_hinge(ox, oy):
    """The hinge: two rings of wedges that ride over each other, fifteen degrees apart.

    Two views, because one cannot show both things. Left: a section along the limb, which
    shows the fork's two ears, the tongue between them with its slit, the axle, and the
    wedges standing proud into the space between the faces. Right: one ear's inner face,
    square on, which is the only view the ring reads in.

    The section is cut on the limb's mid-plane, which passes through the pin axis, so the
    ring is cut at its two widest points. The tongue's ring is drawn with a wedge centered
    on each of them, and the fork's wedges then sit a half step away and are cut between
    two of them, so the ear's face reads plain here. That is the joint at a detent.

    Both members are cut off CUT from the pin. Their roots are further out than that, at
    TAB_FREE and EAR_FREE, and those two lengths are what the joint's springiness is made
    of; they are called out in the note rather than drawn, because a detail drawn long
    enough to reach them has nothing left to show at this scale.
    """
    import math
    stub_r, stub_l, bore_r = STUB / 2, STUB_PROUD, BORE_D / 2
    seat = SEAT / 2                            # the ear's inner face, all of it
    half = BLADE / 2                           # the tongue, half of it
    by = -math.sqrt(NOSE**2 - half**2)         # where the tongue's round end meets its side
    CUT = 15                                   # how far either member is drawn from the pin
    LV, RV = -12 * PAGE, 15 * PAGE             # the two views, either side of center

    def ear_path(sx):
        """One ear, rounded on NOSE about the pin, its inner face flat the whole way.

        The face runs out to where the round end crosses it, which is FLAT from the pin
        because that corner is the same right triangle the limb's flats are cut on.
        """
        return (f'<path class="part" d="M {sx * seat:.3f},{-CUT:g} '
                f'L {sx * NOSE:g},{-CUT:g} L {sx * NOSE:g},0 '
                f'A {NOSE:g},{NOSE:g} 0 0 {1 if sx > 0 else 0} '
                f'{sx * seat:.3f},{FLAT:.3f} Z"/>')

    def wedge_cut(sx, sy):
        """One wedge cut down its own middle: a trapezoid, 45 degrees at both ends.

        The cut misses the flanks, which are what actually bear, and catches the two radial
        ends instead. Those are drafted to the same 45 degrees, so that no face on the wedge
        points straight down when the limb prints lying on its flat.
        """
        i, o = sy * RING_IN, sy * RING_OUT
        ci, co = sy * (RING_IN + WEDGE_H), sy * (RING_OUT - WEDGE_H)
        return (f'<path class="mate" d="M {sx * half:.3f},{i:.3f} '
                f'L {sx * (half + WEDGE_H):.3f},{ci:.3f} '
                f'L {sx * (half + WEDGE_H):.3f},{co:.3f} '
                f'L {sx * half:.3f},{o:.3f} Z"/>')

    def pie(cx_deg, r_in, r_out, cls):
        """One wedge seen square on: an annular sector WEDGE_W wide."""
        a0 = math.radians(cx_deg - WEDGE_W / 2)
        a1 = math.radians(cx_deg + WEDGE_W / 2)
        pt = lambda r, a: f"{r * math.cos(a):.3f},{r * math.sin(a):.3f}"
        return (f'<path class="{cls}" d="M {pt(r_in, a0)} '
                f'A {r_in:.3f},{r_in:.3f} 0 0 1 {pt(r_in, a1)} '
                f'L {pt(r_out, a1)} '
                f'A {r_out:.3f},{r_out:.3f} 0 0 0 {pt(r_out, a0)} Z"/>')

    pitch = 360 / WEDGES

    def mid(k, r):
        """A point on the mating ring's kth wedge center, half a step round from ours."""
        a = math.radians(k * pitch + pitch / 2)
        return f"{r * math.cos(a):.3f},{r * math.sin(a):.3f}"

    art = [
        # --- left: section along the limb. The pin axis is the origin, so every rounded
        # end is NOSE from it and everything else reads straight off the drawing.
        f'<g transform="translate({LV:g},0)">'
        + ear_path(-1) + ear_path(1)
        + f'<path class="mate" d="M {-half:g},{CUT:g} L {-half:g},{by:.3f} '
          f'A {NOSE:g},{NOSE:g} 0 0 1 {half:g},{by:.3f} L {half:g},{CUT:g} Z"/>'
        + rect(-SLIT / 2, -NOSE, SLIT, CUT + NOSE, "void")         # the relief slit
        + rect(-NOSE, -bore_r, NOSE - seat, 2 * bore_r, "void")    # bore through the near ear
        + rect(seat, -bore_r, NOSE - seat, 2 * bore_r, "void")     # and through the far one
        + rect(-half - stub_l, -stub_r, stub_l, 2 * stub_r, "mate")  # the axle, proud of the
        + rect(half, -stub_r, stub_l, 2 * stub_r, "mate")            # tongue's two faces
        + "".join(wedge_cut(sx, sy) for sx in (-1, 1) for sy in (-1, 1))
        + f'</g>',
        # --- right: one ear's inner face, square on. It carries the same ring the tongue
        # does; at a detent the tongue's wedges sit in the gaps between these.
        f'<g transform="translate({RV:g},0)">'
        + circle(0, 0, chord(seat) / 2)
        + "".join(pie(k * pitch, RING_IN, RING_OUT, "mate") for k in range(WEDGES))
        # The mating ring is drawn by its wedge centers, not as sectors. A wedge is wider
        # than half a step, so square on the two rings overlap and nothing would read.
        + "".join(f'<path class="hid" d="M {mid(k, RING_IN)} L {mid(k, RING_OUT)}"/>'
                  for k in range(WEDGES))
        + circle(0, 0, bore_r, "void")
        + f'</g>',
    ]
    geo = f'<g transform="translate({ox:g},{oy:g}) scale({_S()})" class="det">{"".join(art)}</g>'

    def P(px, py):
        return (ox + _S() * px, oy + _S() * py)

    lab = [
        text(ox, oy - 82, "HINGE &#8212; TWO RINGS OF WEDGES", "lbl", "middle"),
        text(ox - 36, oy - 66, "ALONG THE LIMB", "call", "middle"),
        text(ox + 45, oy - 66, "ONE EAR, INSIDE", "call", "middle"),
        leader([P(LV - 9, -12), (ox - 70, oy - 46)]),
        text(ox - 72, oy - 45, "fork &#8212; two ears", anchor="end"),
        leader([P(LV - half - WEDGE_H / 2, -RING_CON), (ox - 70, oy - 30)]),
        text(ox - 72, oy - 29, f"wedge &#8212; 45&#176; sides, {WEDGE_H:g} mm proud",
             anchor="end"),
        leader([P(LV - (seat + NOSE) / 2, -1.2), (ox - 70, oy - 14)]),
        text(ox - 72, oy - 13, f"bore &#216;{BORE_D:g} mm through each ear", anchor="end"),
        leader([P(LV - half - stub_l / 2, 1.2), (ox - 70, oy + 2)]),
        text(ox - 72, oy + 3, f"axle &#216;{STUB:g} mm, {STUB_PROUD:g} mm proud", anchor="end"),
        leader([P(LV, CUT - 2), (ox - 70, oy + 18)]),
        text(ox - 72, oy + 19, f"slit {SLIT:g} mm at the root, {mm(BLADE - 2 * LEAF_TIP)} at "
                               f"the tip", anchor="end"),
        leader([P(RV + RING_OUT * 0.966, -RING_OUT * 0.259), (ox + 58, oy - 30)]),
        text(ox + 60, oy - 29, f"{WEDGES} wedges, {pitch:g}&#176; apart, r {mm(RING_IN)} to "
                               f"{mm(RING_OUT)} mm"),
        leader([P(RV + FLAT * 0.45, FLAT * 0.45), (ox + 64, oy + 8)]),
        text(ox + 66, oy + 9, f"the face: one plane, {mm(chord(seat))} mm across,"),
        text(ox + 66, oy + 15, f"standing {GAP:g} mm off the tongue&#8217;s"),
        text(ox + 66, oy + 21, f"dashed: where the tongue&#8217;s {WEDGES} wedges sit, "
             f"half a step round"),
        text(ox, oy + 74, "Elbows and knees. Pinch the two leaves together, slide the tongue "
                          "in, and let go &#8212; the axle springs into the bores and the two "
                          "rings drop into step.",
             "note", "middle"),
        text(ox, oy + 80, f"The two faces never touch. They stand {GAP:g} mm apart, which is "
                          f"one wedge plus {WEDGE_C:g} mm of air over its tip, and every "
                          f"protrusion in the joint", "note", "middle"),
        text(ox, oy + 86, f"is a wedge: there are no holes to clean out. Both members are "
                          f"cut off {CUT:g} mm from the pin here:", "note", "middle"),
        text(ox, oy + 92, f"the tongue roots {TAB_FREE:g} mm out and the ear {EAR_FREE:g}, and "
                          f"those two lengths are the spring.", "note", "middle"),
        text(ox, oy + 98, f"{mm(PINCH_F)} N to pinch together; {mm(HOLD_MU)} N&#183;mm to "
                          f"turn, which is {mm(HOLD_MU / ARM_DROOP)} times what holding the arm "
                          f"up takes.", "note", "middle"),
    ]
    return geo + "".join(lab)


# ---------------------------------------------------------------- sheet 1


def sheet_parts():
    g = []
    g.append(f'<g transform="translate(60,60)">{fig(torso())}</g>')
    g.append(f'<g transform="translate(185,52)">{fig(head())}</g>')
    g.append(f'<g transform="translate(310,22)">'
             f'{fig(limb("shoulder", LIMB_CENTER, "socket-side", "fork", "UPPER ARM"))}</g>')
    g.append(f'<g transform="translate(400,22)">'
             f'{fig(limb("elbow", LIMB_CENTER, "blade", "stud", "FOREARM"))}</g>')
    g.append(f'<g transform="translate(490,30)">{fig(gripper())}</g>')
    g.append(f'<g transform="translate(310,160)">'
             f'{fig(limb("hip", LIMB_CENTER, "socket-up", "fork", "THIGH"))}</g>')
    g.append(f'<g transform="translate(400,176)">'
             f'{fig(limb("knee", LIMB_CENTER, "blade", "stud", "SHIN"))}</g>')
    g.append(f'<g transform="translate(495,172)">{fig(foot())}</g>')
    g.append(detail_scale(130, 184))
    g.append(detail_ball(130, 330))
    g.append(detail_hinge(420, 330))

    g.append(text(-60, -36, "SHEET 2 &#8212; THE UNIQUE PARTS", "lbl"))
    g.append(text(-60, -28,
                  "One of each goes in the Part Studio; the assembly makes the copies.",
                  "note"))
    g.append(text(-60, -21,
                  "A + marks a joint part: modeled on its own, then added to the part it sits on. A socket is added too, even though it cuts material away.", "note"))
    g.append(text(-60, 442,
                  "Every ball stud stands off its face on a stalk, as drawn here. On sheet 1 "
                  "the joint centers sit on their station lines instead &#8212; that is the "
                  "kinematic view.", "note"))
    g.append(text(-60, 449,
                  "Where the two sheets disagree, this one is the one to build from.", "note"))
    g.append(text(-60, 460,
                  f"The hip stud stands off the torso&#8217;s bottom face like every other, and "
                  f"the leg drops the {STAND:g} mm with it. A recess into the torso was considered "
                  f"and dropped: it buys no swing, because the {mm(BALL_SWING)}&#176; limit is "
                  f"set inside the socket, by the stalk meeting the mouth.", "note"))
    g.append(text(-60, 471,
                  f"The shoulder is the exception. Its stud runs {SHOULDER_L:g} mm from the side "
                  f"face, of which only the last {STAND:g} is &#216;{STALK}; the rest is a "
                  f"&#216;{BOSS_D:g} boss on the same axis, cut off flush where it crosses the "
                  f"top face. Coaxial is what makes the boss free: it sits behind the ball, and "
                  f"the socket only reaches forward of it.", "note"))
    g.append(text(-60, 482,
                  f"The hinge divides the same &#216;{LIMB:g} three ways: ear {EAR:g}, tongue "
                  f"{BLADE:g}, ear {EAR:g}, and a slit splits the tongue again into two leaves, "
                  f"{LEAF_ROOT:g} thick at the root and {LEAF_TIP:g} at the tip. So each side of "
                  f"the joint is two springs in series, an ear and a leaf, and they share the",
                  "note"))
    g.append(text(-60, 493,
                  f"{mm(MOVE)} mm a wedge needs. Turning it takes {mm(HOLD_MU)} N&#183;mm, which "
                  f"is {mm(HOLD_MU / ARM_DROOP)} times what holding the arm up takes, and only "
                  f"{HOLD_WEDGES} of the {WEDGES} wedges carry it. Pinching it together takes "
                  f"{mm(PINCH_F)} N, which is the harder case at {mm(PINCH_STRESS)} MPa against "
                  f"PETG&#8217;s {PETG_YIELD:g}.", "note"))
    return svg(g, -70, -48, 650, 562, scale=3.4)


# ---------------------------------------------------------------- sheet 2


# ---------------------------------------------------------------- the stations
# Module level so anything measuring the CAD can import them instead of copying
# the arithmetic. Every one is derived: nothing is fitted to a target height, and
# the figure comes out as tall as the parts, the stand-off at each ball, and the
# angle each limb leaves at make it. Change the hip stalk and the ground moves.
_HALF = TORSO_H / 2
HIP_Z, NECK_Z = -_HALF - STAND, _HALF + STAND
KNEE_Z, ANKLE_Z = HIP_Z - LIMB_CENTER, HIP_Z - 2 * LIMB_CENTER
SOLE_Z = ANKLE_Z - FOOT_H
# The head carries the standard socket collar, the same as every other socketed part,
# so its underside stands COLLAR_L off the mouth instead of sitting on it. The collar
# rim is the lowest point of the head.
HEAD_RIM = NECK_Z - GRIP
HEAD_B = NECK_Z + COLLAR_L
HEAD_T = HEAD_B + HEAD_H
HEIGHT = HEAD_T - SOLE_Z

# The shoulder. The pedestal leaves the side face 4 mm below the torso's top;
# the ball lands STAND clear of that face, measured perpendicular to it.
SH_ROOT = _HALF - SHOULDER_DROP
SH_X, SH_Z = TORSO_W / 2 + SH_DX, SH_ROOT - SH_DZ
_A1, _A2 = math.radians(ARM_ANGLE), math.radians(ARM_ANGLE - ELBOW_BEND)
EL_X, EL_Z = SH_X + LIMB_CENTER * math.sin(_A1), SH_Z - LIMB_CENTER * math.cos(_A1)
WR_X, WR_Z = EL_X + LIMB_CENTER * math.sin(_A2), EL_Z - LIMB_CENTER * math.cos(_A2)
GB_Z = WR_Z - GRIPPER_L * math.cos(_A2)

# The torso's width places both pairs of limbs, and its height places neither. A leg's outer
# surface is flush with the side face; a shoulder ball stands SH_DX clear of the same face.
LEG_X = TORSO_W / 2 - LIMB / 2          # legs flush with the torso's sides
FOOT_X = LEG_X                          # the sole is centered on its own leg, so the two
                                        # feet meet at x 0 when the legs hang straight

# Both sheets are laid out in units where the figure stands PAGE_FIG tall — the height
# it had when the layout was drawn. Every page coordinate below, every font size and
# every leader is written in those units, while the figure itself is drawn in millimeters
# off the stations above. PAGE is the ratio between the two, and svg() divides the whole
# sheet by it. So a robot of any size lands on the same sheet at the same size, the type
# beside it stays the same size, and the only thing that changes is what the labels say.
PAGE_FIG = 158.15
PAGE = HEIGHT / PAGE_FIG
TO_PAGE = 1 / PAGE      # millimeters to page units, inside a class="fig" group.
                        # Not #fit — that is the joint's printing clearance, above.

# A class="fig" group carries millimeters onto the page by scaling. That would drag the
# type down with it, so the type inside one is written PAGE times larger and comes back
# out the size type is everywhere else. Sheet 1 puts only geometry in these groups;
# sheet 2 puts a whole part and its callouts in each.
STYLE += "".join(
    f"  .fig .{cls} {{ font-size:{size * PAGE:g}px; }}\n"
    for cls, size in (("call", 3.4), ("note", 3.6), ("name", 5), ("dimt", 4.2),
                      ("lbl", 4.6), ("warn", 3.6)))


def fig(geom):
    """Millimeters onto the page. The type inside comes back out its own size."""
    return f'<g class="fig" transform="scale({TO_PAGE:g})">{geom}</g>'


def fig_at(x, y, geom):
    """The same, anchored at a page position rather than at the cell's own origin."""
    return f'<g transform="translate({x},{y})">{fig(geom)}</g>'


def sheet_assembly():
    """Front and side of the assembled figure, joints drawn on their real centers.

    Two coordinate systems meet here, and until draft9p0 they were the same numbers.
    Geometry is millimeters, straight off the stations. The page furniture — station
    ladders, callout columns, the height dimension, the notes — is page units, and has
    to stay where it is however big the robot gets. TO_PAGE carries one into the other, and
    the geometry rides in a class="fig" group that applies it. Annotations use Y(), which
    lands in page units already, so their type and their leaders never change size.
    """
    half, a1, a2 = _HALF, _A1, _A2
    G = 150                                 # the ground line, in page units
    Gm = G / TO_PAGE                            # and the same line in millimeters

    def y(z):
        """Millimeters, for geometry inside the scaled group."""
        return Gm - (z - SOLE_Z)

    def Y(z):
        """Page units, for anything carrying type."""
        return y(z) * TO_PAGE

    front, front_a = [], []
    for i, sx in enumerate((-1, 1)):
        # The stud and the upper arm are collinear in this view. They are not collinear
        # in space — the arm sits ARM_OFF_STUD off the stud, all of it fore-and-aft, and
        # this view cannot show a fore-and-aft angle.
        front += [shoulder(sx * TORSO_W / 2, y(SH_ROOT), sx, y(half), f"a{i}")]
        front += [rod(sx * SH_X, y(SH_Z), sx * ARM_ANGLE, LIMB_CENTER),
                  rod(sx * EL_X, y(EL_Z), sx * (ARM_ANGLE - ELBOW_BEND), LIMB_CENTER),
                  clip_front(sx * WR_X, y(WR_Z), sx * (ARM_ANGLE - ELBOW_BEND))]
        front += [circle(sx * SH_X, y(SH_Z), BALL / 2),
                  circle(sx * EL_X, y(EL_Z), LIMB / 2),
                  circle(sx * WR_X, y(WR_Z), BALL / 2)]
        # legs hang straight down off a plain stud on the torso's underside
        front += [rod(sx * LEG_X, y(HIP_Z), 0, LIMB_CENTER),
                  rod(sx * LEG_X, y(KNEE_Z), 0, LIMB_CENTER)]
        front += [circle(sx * LEG_X, y(HIP_Z), BALL / 2),
                  circle(sx * LEG_X, y(KNEE_Z), LIMB / 2),
                  circle(sx * LEG_X, y(ANKLE_Z), BALL / 2)]
        front += [rect(sx * FOOT_X - FOOT_W / 2, y(ANKLE_Z), FOOT_W, FOOT_H)]

    front += [rect(-TORSO_W / 2, y(half), TORSO_W, TORSO_H)]
    front += [rect(-STALK / 2, y(NECK_Z + 2), STALK, STAND + 2),
              circle(0, y(NECK_Z), BALL / 2)]
    front += [rect(-COLLAR_R, y(HEAD_B), 2 * COLLAR_R, COLLAR_PROUD),  # the neck collar
              arch(-HEAD_W / 2, y(HEAD_T), HEAD_W, HEAD_H)]
    front += face(0, y(HEAD_B + HEAD_H / 2))
    front += [f'<line class="ctr" x1="0" y1="{y(HEAD_T + 6):g}" x2="0" y2="{y(SOLE_Z - 6):g}"/>']
    front_a += [f'<line class="gnd" x1="-52" y1="{G}" x2="52" y2="{G}"/>']

    # the origin — the test run called this the most useful thing on the sheet
    front_a += [
        f'<circle cx="0" cy="{Y(0):g}" r="1.8" fill="none" stroke="#0b6e86" '
        f'stroke-width="0.8"/>',
        f'<path d="M -4.5 {Y(0):g} H 4.5 M 0 {Y(0) - 4.5:g} V {Y(0) + 4.5:g}" '
        f'stroke="#0b6e86" stroke-width="0.45"/>',
    ]

    stations = [("ankle", ANKLE_Z), ("knee", KNEE_Z), ("hip", HIP_Z), ("shoulder", SH_Z),
                ("neck", NECK_Z), ("head center", HEAD_B + HEAD_H / 2)]
    for nm, z in stations:
        front_a += [f'<line class="stn" x1="-58" y1="{Y(z):g}" x2="58" y2="{Y(z):g}"/>',
                    text(-60, Y(z) + 1.2, f"{nm} {mm(z - SOLE_Z)} mm", "call", "end")]

    front_a += [
        '<g class="dim"><path d="M -70 {a:g} H -78 M -70 {b:g} H -78"/>'
        '<path d="M -75 {a:g} V {b:g}"/>'
        '<path d="M -75 {a:g} l -1.4 4 h 2.8 z" fill="#b8156e"/>'
        '<path d="M -75 {b:g} l -1.4 -4 h 2.8 z" fill="#b8156e"/></g>'.format(
            a=Y(HEAD_T), b=Y(SOLE_Z)),
        text(-79, (Y(HEAD_T) + Y(SOLE_Z)) / 2, f"{mm(HEIGHT)} mm", "dimt", "middle", rot=-90),
    ]

    # Callouts land on one ladder at x = 64, in the order the parts stack up, each
    # pushed down far enough not to sit on the one above it. Anchors are page units.
    calls = [
        ((0, Y(HEAD_B + HEAD_H / 2) - 6), Y(HEAD_T) + 2, "head"),
        ((0, Y(NECK_Z)), Y(NECK_Z), "neck ball joint"),
        ((7, Y(half) + 8), Y(half) + 4, "torso"),
        ((SH_X * TO_PAGE + 3, Y(SH_Z) + 9), Y(SH_Z) + 6, "upper arm"),
        ((2.4, Y(0)), Y(0), "origin &#8212; center of the torso"),
        ((EL_X * TO_PAGE + 2, Y(EL_Z) + 10), Y(EL_Z) + 10, "forearm"),
        ((WR_X * TO_PAGE + 4, Y(WR_Z) + 7), Y(WR_Z) + 4, "gripper"),
        ((LEG_X * TO_PAGE + LIMB * TO_PAGE / 2, Y(HIP_Z) + 20), Y(HIP_Z) + 20, "thigh"),
        ((LEG_X * TO_PAGE, Y(KNEE_Z) + 12), Y(KNEE_Z) + 12, "shin"),
        ((10, Y(ANKLE_Z) + 6), Y(ANKLE_Z) + 4, "foot"),
    ]
    prev = -1e9
    for (ax, ay), ty, nm in sorted(calls, key=lambda c: c[1]):
        ty = max(ty, prev + 6.5)
        prev = ty
        front_a += [leader([(ax, ay), (62, ty)]), text(64, ty + 1.2, nm, "call")]

    # ---- side. Page-right is forward. The arms lie in one plane ARM_PLANE_Y
    # forward of center, so they are seen edge-on and the whole chain is one band.
    AY = -ARM_PLANE_Y
    kf = FOOT_H / 12                        # the sole's outline, drawn once at FOOT_H 12
    side = [rect(-TORSO_D / 2, y(half), TORSO_D, TORSO_H),
            rect(-STALK / 2, y(NECK_Z + 2), STALK, STAND + 2), circle(0, y(NECK_Z), BALL / 2),
            rect(-COLLAR_R, y(HEAD_B), 2 * COLLAR_R, COLLAR_PROUD),
            rect(-HEAD_D / 2, y(HEAD_T), HEAD_D, HEAD_H),
            rect(-LIMB / 2, y(HIP_Z), LIMB, LIMB_CENTER), rect(-LIMB / 2, y(KNEE_Z), LIMB, LIMB_CENTER),
            f'<path class="part" d="M {-20 * kf:g},{Gm:g} h {48 * kf:g} '
            f'a {5 * kf:g} {5 * kf:g} 0 0 0 {-1 * kf:g} {-8 * kf:g} '
            f'q {-14 * kf:g} {-4 * kf:g} {-46 * kf:g} {-4 * kf:g} '
            f'a {5 * kf:g} {5 * kf:g} 0 0 0 {-1 * kf:g} {12 * kf:g} z"/>']
    side += [rect(AY - LIMB / 2, y(-half), LIMB, y(GB_Z) - y(-half)),
             f'<rect class="hid" x="{AY - LIMB / 2:g}" y="{y(SH_Z):g}" width="{LIMB:g}" '
             f'height="{y(-half) - y(SH_Z):g}"/>']
    side += [f'<line class="ctr" x1="0" y1="{y(HEAD_T + 6):g}" x2="0" y2="{y(SOLE_Z - 6):g}"/>']

    side_a = [f'<line class="gnd" x1="-26" y1="{G}" x2="34" y2="{G}"/>']
    side_a += [
        '<g class="dim"><path d="M -12 {a:g} V {c:g} M 12 {a:g} V {c:g}"/>'
        '<path d="M -12 {b:g} H 12"/>'
        '<path d="M -12 {b:g} l 4 -1.4 v 2.8 z" fill="#b8156e"/>'
        '<path d="M 12 {b:g} l -4 -1.4 v 2.8 z" fill="#b8156e"/></g>'
        .format(a=Y(-half), b=Y(-half) + 3.5, c=Y(-half) + 5),
        text(-14, Y(-half) + 2.5, f"{TORSO_D} mm", "dimt", "end"),
        leader([(AY * TO_PAGE, Y(GB_Z) - 8), (26, Y(GB_Z) - 4)]),
        text(27, Y(GB_Z) - 3, "both arms, edge-on", "call"),
        text(4, G + 18, f"The arms lie in one plane {mm(abs(ARM_PLANE_Y))} mm forward of center,",
             "note", "middle"),
        text(4, G + 24, "so this view sees them edge-on and both at once. Dashed", "note",
             "middle"),
        text(4, G + 30, "where the torso is in front of them.", "note", "middle"),
    ]

    g = [f'<g transform="translate(0,0)">{fig("".join(front))}{"".join(front_a)}</g>',
         f'<g transform="translate(196,0)">{fig("".join(side))}{"".join(side_a)}</g>',
         text(0, -10, "FRONT", "lbl", "middle"),
         text(196, -10, "SIDE", "lbl", "middle"),
         text(-86, -52, "SHEET 1 &#8212; ASSEMBLED", "lbl"),
         text(-86, -44,
              "The parts from sheet 2, assembled. Joint centers sit on their station lines, and "
              "every station is derived &#8212; nothing is fitted to a round height.", "note"),
         text(-86, -38,
              f"Shoulder stud {SHOULDER_EL}&#176; down and {SHOULDER_AZ}&#176; forward, "
              f"{SHOULDER_L:g} mm long: a &#216;{BOSS_D:g} boss coaxial with the last {STAND:g} mm of "
              f"&#216;{STALK} stalk, cut flush at the torso\'s top face.", "note"),
         text(-86, -32,
              f"That puts the ball {mm(SH_DX)} mm clear of the side, so a &#216;{LIMB:g} arm "
              f"swings anywhere the socket allows &#8212; {mm(ARM_LO)}&#176; to "
              f"{mm(ARM_HI)}&#176; from vertical.", "note"),
         text(-86, -26,
              f"The arm is drawn at {mm(ARM_ANGLE)}&#176;, hanging {mm(ARM_OFF_STUD)}&#176; off "
              f"the stud. All of that is fore-and-aft, so it stays in one plane and this view "
              f"reads true length.", "note"),
         text(-86, -20,
              f"Elbows bent {ELBOW_BEND}&#176; for the picture; the assembly is saved at rest. "
              f"The gripper\'s bore runs left-right, so it is two hidden lines here and a "
              f"circle on the parts sheet.", "note"),
         text(-86, G + 48,
              f"Session 1 builds the neck as a plain &#216;{LIMB:g} mm post. It becomes the "
              f"ball joint shown here once joints are taught.", "note"),
         ]
    return svg(g, -118, -64, 396, 296)


# ---------------------------------------------------------------- plumbing


def svg(body, x, y, w, h, scale=4.6):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" '
            f'width="{int(w * scale)}" height="{int(h * scale)}" '
            f'font-family="ui-monospace, Menlo, monospace">'
            f"<style>{STYLE}</style>{''.join(body)}</svg>")


def render(svg_path):
    from playwright.sync_api import sync_playwright
    out = svg_path.with_suffix(".png")
    html = "<style>html,body{margin:0;background:#fff}</style>" + svg_path.read_text()
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
        page = b.contexts[0].new_page()
        page.set_viewport_size({"width": 2600, "height": 2200})
        page.set_content(html)
        page.wait_for_timeout(900)
        page.locator("svg").screenshot(path=str(out))
        page.close()
        b.close()
    print(f"  {out.name}  {out.stat().st_size:,} bytes")


def main():
    IMAGES.mkdir(parents=True, exist_ok=True)
    for name, maker in (("plan-parts", sheet_parts), ("plan-assembly", sheet_assembly)):
        path = IMAGES / f"{name}.svg"
        path.write_text(maker())
        print(f"wrote {path.name}")
        if "--no-render" not in sys.argv:
            render(path)
    print(f"\nmouth diameter = {MOUTH:.4f} mm  ({100 * MOUTH / BALL:.0f}% of the ball)")


if __name__ == "__main__":
    main()
