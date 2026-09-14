"""How hard the ball is to press into its socket, and how hard it is to pull back out.

The mouth is ``MOUTH`` across and the ball is ``BALL``, so the ball has to open the mouth by
half their difference on the radius before its equator will go through. Four slits cut the
collar's top into four fingers rooted where the slits bottom out, and it is those four
cantilevers that give.

The kinematics is the reason the slits are there. A finger cannot move outward on the same
circle without stretching around the joint, and 0.24 mm on a 5.76 mm radius is 4% strain,
which PETG does not have. What it does instead is open like a petal: the arc keeps its
length, its radius grows, its included angle shrinks, and the slits widen at the rim. That
is bending in the meridian plane, so no hoop term appears anywhere below.

The contact is the mouth's edge on the ball. The rim is flat and the cavity is spherical, so
the mouth is a sharp circular edge and the contact normal is the ball's own radius through
the contact point. That one fact makes pressing in and pulling out cost the same: reverse
the sign of the center's height and the direction of sliding together, and the expression
for the axial force does not change.

Three things this file does not carry, all of them named in ``press``: the root is treated
as built in, the ball is treated as rigid, and the axial half of the contact force is
dropped. The first two make the answer high and the third makes it low.
"""
import math

__all__ = ["Socket", "stiffness", "elastic", "press", "edge_load", "sections"]

E_PETG, YIELD_PETG = 2000.0, 50.0       # MPa
POISSON = 0.4                           # PETG, near enough for the shear term
SHEAR_K = 1.2                           # shear coefficient, rectangular section


class Socket:
    """One socket's spring geometry. Every length is millimeters.

    ``slit_d`` is the free length of a finger, because a slit's depth is where the finger is
    rooted. Stations on the limb axis are measured from the ball's center, so the rim is at
    ``grip`` and the root is below zero.
    """

    def __init__(self, ball, cavity, mouth, collar_r, slit_w, slit_d, slit_in, slits=4):
        self.ball, self.cavity, self.mouth = ball, cavity, mouth
        self.collar_r, self.slit_w, self.slit_d = collar_r, slit_w, slit_d
        self.slit_in, self.slits = slit_in, slits
        self.grip = math.sqrt(cavity ** 2 - (mouth / 2) ** 2)
        self.root = self.grip - slit_d          # where the slits bottom out
        # how high the ball's center is when the mouth first has to open at all
        self.reach = math.sqrt((ball / 2) ** 2 - (mouth / 2) ** 2)
        self.open = ball / 2 - mouth / 2        # and how far it opens at the equator
        # A slit that stops before the cavity ends blind in the wall, and then the fingers
        # are still joined at the root and none of the rest of this file applies.
        floor = math.sqrt(max(cavity ** 2 - self.root ** 2, 0.0))
        if floor <= slit_in:
            raise ValueError(f"the slit bottoms out at r {floor:.3f}, outside the cavity, "
                             f"so it is a blind cut and there is no finger")
        if slit_in >= mouth / 2:
            raise ValueError(f"the slit stops at r {slit_in:g}, outside the mouth, so the "
                             f"mouth cannot open")


def _section(s, y, n=600):
    """Area, centroid radius, second moment and far fiber of one finger's section.

    ``y`` is the height above the ball's center. The section is the annulus from the cavity
    out to the collar, less the two slits that bound the finger, and it bends about a
    circumferential axis, so the second moment is taken about the centroid radius.
    """
    a, b = math.sqrt(max(s.cavity ** 2 - y * y, 0.0)), s.collar_r
    half, pitch = s.slit_w / 2, 2 * math.pi / s.slits
    dr = (b - a) / n
    rs = [a + (b - a) * (i + .5) / n for i in range(n)]
    w = [r * (pitch - 2 * math.asin(min(half / r, 1.0)) if r > s.slit_in else pitch)
         for r in rs]
    area = sum(w) * dr
    rbar = sum(r * wi for r, wi in zip(rs, w)) * dr / area
    inertia = sum(wi * (r - rbar) ** 2 for r, wi in zip(rs, w)) * dr
    return area, rbar, inertia, max(rbar - a, b - rbar)


def stiffness(s, shear=True, n=400):
    """The radial force one finger takes to move its rim out one millimeter, in N/mm.

    A unit load at the rim, integrated down a cantilever whose section changes with depth
    because the cavity is a sphere. The finger is barely three times as long as it is thick,
    so the shear term is not a rounding error and is kept.
    """
    g = E_PETG / (2 * (1 + POISSON))
    flex = 0.0
    for i in range(n):
        t = (i + .5) / n                        # 0 at the root, 1 at the rim
        area, _, inertia, _ = _section(s, s.root + s.slit_d * t)
        arm = s.slit_d * (1 - t)
        flex += (arm ** 2 / (E_PETG * inertia)
                 + (SHEAR_K / (g * area) if shear else 0.0)) * (s.slit_d / n)
    return 1.0 / flex


def _worst(s, n=400):
    """Where a finger is worst stressed, and how badly, in MPa per newton of load at the rim.

    Not always the root, which is the whole reason this is a sweep. The moment falls linearly
    from the root to the rim, but the section thins from the root up to the equator, because
    the cavity is a sphere and the collar is a cylinder. Thickness enters as a square and the
    moment only as itself, so a thin enough wall is worst somewhere in between: at a
    ``COLLAR_WALL`` of 1.5 the worst station is 1.5 above the root and runs 21% over it. Take
    the root alone and every thin-walled answer comes out optimistic.
    """
    out = (0.0, s.root)
    for i in range(n + 1):
        y = s.root + s.slit_d * i / n
        _, _, inertia, c = _section(s, y)
        stress = (s.grip - y) * c / inertia
        if stress > out[0]:
            out = (stress, y)
    return out


def _stress_per_load(s):
    """Bending stress where the finger is worst, in MPa per newton of load at the rim."""
    return _worst(s)[0]


def elastic(s):
    """The most the mouth can open before a finger reaches yield, in millimeters.

    Compare it with ``s.open``. If it is the smaller of the two, the ball does not go in on
    a spring: the roots take a permanent set first, the mouth stays open, and what the joint
    holds afterward is not what any of this predicts.
    """
    return YIELD_PETG / _stress_per_load(s) / stiffness(s)


def press(s, mu=0.35, steps=1201):
    """Pressing the ball in: peak axial force in newtons, where it peaks, and the stress.

    The sweep is over the ball's center height above the rim. At each height the mouth's
    edge sits on the ball at radius ``rho``, the fingers are open by ``rho`` less the mouth's
    own radius, and the axial force is what that radial load costs once the contact's slope
    and its friction are taken off it. Pulling the ball back out costs the same, so this is
    both numbers.

    The fourth number is the bending stress at the worst-stressed station at that instant,
    which is not where the stress peaks over the whole insertion: the fingers keep opening
    after the force has passed its peak, out to ``s.open`` when the ball's equator is level
    with the mouth, and that is the opening ``elastic`` answers.

    What is left out. The root is built in, when it is really the top of a ring that can
    itself give, so the answer is high. The ball is rigid, when it is the same plastic, so
    the answer is high again. Against that, the axial half of the contact force lands inside
    the finger's neutral radius and bends it back inward, worth something like a sixth of the
    root moment at the peak, which the answer does not have, so it is low by about that much.
    """
    k, per_n = stiffness(s), _stress_per_load(s)
    rb = s.ball / 2
    best = (0.0, 0.0, 0.0, 0.0)
    for i in range(steps):
        h = s.reach * (1 - i / (steps - 1.0))
        rho = math.sqrt(max(rb * rb - h * h, 0.0))
        open_by = rho - s.mouth / 2
        if open_by <= 0:
            continue
        load = k * open_by                                       # radial, on one finger
        force = s.slits * load * (h + mu * rho) / (rho - mu * h)
        if force > best[0]:
            best = (force, h, open_by, load * per_n)
    return best


def edge_load(s, mu=0.35):
    """The radial load at the peak spread along the mouth's edge, in newtons per millimeter.

    The mouth is a sharp corner, so this is a line load on the ball rather than a pressure
    on an area. It is here because a high enough one indents the ball instead of bending the
    finger, and nothing above models that.
    """
    radial = stiffness(s) * press(s, mu=mu)[2]
    arc = (2 * math.pi / s.slits - 2 * math.asin(s.slit_w / s.mouth)) * (s.mouth / 2)
    return radial / arc


def sections(s):
    """What a finger measures at four stations: thickness, area, I, centroid radius, far fiber.

    ``worst`` is the station ``_worst`` picks, and it coincides with the root only when the
    wall is thick enough that the section's taper outruns the moment's.
    """
    out = {}
    for name, y in (("root", s.root), ("worst", _worst(s)[1]), ("equator", 0.0),
                    ("rim", s.grip)):
        area, rbar, inertia, c = _section(s, y)
        inner = math.sqrt(max(s.cavity ** 2 - y * y, 0.0))
        out[name] = (s.collar_r - inner, area, inertia, rbar, c)
    return out
