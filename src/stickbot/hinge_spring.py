"""How hard a detent hinge is to turn, to pinch together, and to twist apart.

Status: illustrative — an analysis tool. It decides no dimension and it names no version:
the geometry arrives in the ``Hinge`` it is handed, so whichever joint is handed to it is the
joint it answers about. The one thing here that is a choice rather than a method is the material,
E_PETG and YIELD_PETG below; change those and every answer moves.

All three answers come from the same picture. The fork's ear and the blade's leaf are
cantilevers cut out of the same Ø ``limb`` rod at different depths, and they meet at a
ring of protrusions standing proud of both faces. The worked description below uses wedges,
because that is the shape the ring has had longest; the ring itself is a radius, a count and a
climb, so a ring of any shape is expressed the same way. Wherever a wedge or the axle needs room, the
pair has to open by that much, and the force it takes is a contact problem: every wedge
*may* push, none may pull, and a wedge the beam has already lifted clear pushes with
nothing.

That last part is the whole reason this file exists rather than a formula. Treating the
ring as a row of independent springs and adding it up overstates the answer several times
over, because opening the pair where one wedge sits lifts every wedge outboard of it
further than its own climb.

The three questions are different load cases and give different answers:

- **turning a seated joint**, where every wedge climbs at once and the axle is home in its
  bore carrying nothing;
- **pinching it together**, where a hand squeezes the two leaves until the axle clears the
  ear's face, which is what replaced pushing the tongue down the slot;
- **twisting it apart**, where a straight joint is wrung about the limb's axis until the
  wedge tips jam diagonally and lever the axle out of its bore.

The leaf tapers, so its stiffness varies along its length and the closed-form cantilever
compliance does not apply. Every member here carries ``EI`` per station and the unit-load
integral is done numerically.

Run this file to see it reproduce the old tooth-and-valley joint's 454 N·mm, which is the
regression that says the rewrite did not move the physics.
"""
import math

__all__ = ["Hinge", "hold", "press", "pinch", "twist", "sections",
           "E_PETG", "YIELD_PETG", "SHEAR_PETG"]

E_PETG, YIELD_PETG = 2000.0, 50.0       # MPa
SHEAR_PETG = 0.577 * YIELD_PETG         # von Mises
STATIONS = 240                          # how finely a member is cut up along its length


class Member:
    """One cantilever, rooted at 0, carrying its own ``EI`` and far fiber per station."""

    def __init__(self, length, ei, far):
        self.length, self.ei, self.far = length, ei, far
        self.dx = length / STATIONS

    def x(self, i):
        return (i + .5) * self.dx

    def compliance(self, p, q):
        """How far a unit load at ``q`` moves the point at ``p``. Both from the root."""
        lo, total = min(p, q), 0.0
        for i in range(STATIONS):
            x = self.x(i)
            if x >= lo:
                break
            total += (q - x) * (p - x) / self.ei[i] * self.dx
        return total

    def stress(self, loads):
        """Peak bending stress anywhere along it, MPa. ``loads`` is [(station, force)]."""
        worst = 0.0
        for i in range(STATIONS):
            x = self.x(i)
            m = sum(f * (q - x) for q, f in loads if q > x)
            worst = max(worst, abs(m) * self.far[i] * E_PETG / self.ei[i])
        return worst


def _section(r, a, b, zmax, n=160):
    """Second moment about its own centroid, and the far fiber, of the slice a..b of a
    Ø 2r rod, bending the way the joint opens.

    ``zmax`` is how tall the slice is allowed to be. It takes height off the slice wherever
    the round rod stood higher, and none off the far fiber, which is measured across the
    slit and not up the chord. Two things cap it: the flat the limb is cut to, and the
    rounded nose, once the station is out past the pin.
    """
    ys = [a + (b - a) * (i + .5) / n for i in range(n)]
    w = [2 * min(math.sqrt(max(r * r - y * y, 0.0)), zmax) for y in ys]
    dy = (b - a) / n
    area = sum(w) * dy
    if area <= 0:
        return 1e-9, 1.0
    yb = sum(y * wi for y, wi in zip(ys, w)) * dy / area
    return (sum(wi * (y - yb) ** 2 for y, wi in zip(ys, w)) * dy,
            max(yb - a, b - yb))


def _member(r, length, pin, thick_at, y_far, flat, nose):
    """Build one member. ``thick_at(x)`` gives its thickness, ``y_far`` the face it keeps."""
    ei, far = [], []
    for i in range(STATIONS):
        x = (i + .5) * length / STATIONS
        past = x - pin
        z = flat if past <= 0 else min(flat, math.sqrt(max(nose ** 2 - past * past, 0.0)))
        t = thick_at(x)
        lo, hi = (y_far - t, y_far) if y_far > 0 else (abs(y_far), abs(y_far) + t)
        i_, c_ = _section(r, lo, hi, z)
        ei.append(E_PETG * i_)
        far.append(c_)
    return Member(length, ei, far)


class Hinge:
    """One hinge's spring geometry. Every length is millimeters.

    ``tab_free`` and ``ear_free`` are where each member is rooted, measured from the pin;
    that is where its limb's rod ends, not where its own slot or tongue stops.

    The detent ring is given as a radius, a count and a climb rather than as wedges, so
    that the old tooth-and-valley joint can be expressed here too and used as a check.
    """

    def __init__(self, limb, blade, leaf_root, leaf_tip, gap, tab_free, ear_free,
                 blade_out, ring_r, ring_n, climb, stub_proud, nose=None, flat=None):
        self.limb, self.blade, self.gap = limb, blade, gap
        self.leaf_root, self.leaf_tip = leaf_root, leaf_tip
        self.tab_free, self.ear_free, self.blade_out = tab_free, ear_free, blade_out
        self.ring_r, self.ring_n, self.climb = ring_r, ring_n, climb
        self.stub_proud = stub_proud
        self.r = limb / 2
        self.nose = self.r if nose is None else nose
        self.slot_half = blade / 2 + gap
        self.flat = (math.sqrt(max(self.nose ** 2 - self.slot_half ** 2, 0.0))
                     if flat is None else flat)
        taper = (leaf_tip - leaf_root) / blade_out
        self.leaf = _member(self.r, blade_out, tab_free,
                            lambda x: leaf_root + taper * x, blade / 2,
                            self.flat, self.nose)
        self.ear = _member(self.r, ear_free + self.nose, ear_free,
                           lambda x: self.r - self.slot_half, -self.slot_half,
                           self.flat, self.nose)
        # Where the ring's contacts land along the limb. Two of them can share a station,
        # and compliance sees only the station, so they are lumped. ``station_wedges`` keeps
        # how many wedges each station stands for, because a count of stations is not a count
        # of wedges and reporting one for the other understates what carries.
        lump = {}
        for k in range(ring_n):
            lump.setdefault(round(ring_r * math.cos(2 * math.pi * k / ring_n), 9), 0)
            lump[round(ring_r * math.cos(2 * math.pi * k / ring_n), 9)] += 1
        self.stations = sorted(lump)
        self.station_wedges = [lump[s] for s in self.stations]

    def slit(self, x):
        """How wide the slit is at station ``x`` from the leaf's root."""
        return self.blade - 2 * (self.leaf_root
                                 + (self.leaf_tip - self.leaf_root) * x / self.blade_out)

    def levers(self):
        """Each contact station, as a distance from the root of each member."""
        return ([e + self.tab_free for e in self.stations],
                [self.ear_free - e for e in self.stations])


def _matrix(hinge, lev_leaf, lev_ear):
    """How much each contact opens per unit force at each other contact."""
    n = len(lev_leaf)
    return [[hinge.leaf.compliance(lev_leaf[i], lev_leaf[j])
             + hinge.ear.compliance(lev_ear[i], lev_ear[j]) for j in range(n)]
            for i in range(n)]


def _solve(c, need):
    """Solve one set of contacts: each must open at least ``need``, none may pull.

    Active-set, which is the plain way to say it: assume everything touches, drop
    whatever comes out pulling, put back anything that ends up interfering, repeat.
    """
    n = len(need)
    act = list(range(n))
    for _ in range(6 * n + 40):
        m = len(act)
        aug = [[c[i][j] for j in act] + [need[i]] for i in act]
        for col in range(m):
            piv = max(range(col, m), key=lambda r: abs(aug[r][col]))
            aug[col], aug[piv] = aug[piv], aug[col]
            if abs(aug[col][col]) < 1e-18:
                return [0.0] * n
            for row in range(m):
                if row != col and aug[row][col]:
                    f = aug[row][col] / aug[col][col]
                    for cc in range(col, m + 1):
                        aug[row][cc] -= f * aug[col][cc]
        force = [0.0] * n
        for k, i in enumerate(act):
            force[i] = aug[k][m] / aug[k][k]
        pulling = [i for i in act if force[i] < -1e-12]
        if pulling:
            act = [i for i in act if i != pulling[0]]
            continue
        opened = [sum(c[i][j] * force[j] for j in range(n)) for i in range(n)]
        short = [i for i in range(n) if i not in act and opened[i] < need[i] - 1e-9]
        if not short:
            return force
        act = sorted(act + [short[0]])
    return force


def hold(h, mu=0.0):
    """Turning a seated joint: breakaway torque in N·mm, how many carry, two stresses.

    Every wedge climbs at once here, and the axle is home in its bore so it carries
    nothing. A 45° ramp turns the axial spring force into an equal tangential one, so
    frictionless the torque is that force times the ring's radius. ``mu`` adds the
    raising factor (1 + mu) / (1 - mu), which at 45° is where the real answer sits.
    """
    lev_leaf, lev_ear = h.levers()
    f = _solve(_matrix(h, lev_leaf, lev_ear), [h.climb] * len(h.stations))
    torque = 2 * sum(f) * h.ring_r * ((1 + mu) / (1 - mu) if mu else 1.0)
    return (torque,
            sum(w for w, v in zip(h.station_wedges, f) if v > 1e-9),
            h.ear.stress(list(zip(lev_ear, f))),
            h.leaf.stress(list(zip(lev_leaf, f))))


def press(h, steps=453):
    """Pushing it together instead: peak force in N, and the two worst stresses in MPa.

    This is how the joint used to be assembled, and the reason it is not anymore. The tongue
    slides down the slot nose first and holds the pair open as a wedge, widest at its tip,
    so the answer is a sweep: at each depth, which contacts are inside the fork at all, and
    what it costs to open the pair the rest of the way where each one sits. The peak of that
    sweep is what a hand feels, and it rises the whole way in.

    Pinching the two leaves skips every bit of it, which is why ``pinch`` is the number the
    joint is sized on. This one is kept because it is what the change bought.
    """
    best = (0.0, 0.0, 0.0)
    engaged = h.stub_proud - h.gap
    for i in range(steps):
        s = 1.4 + (2 * h.nose - 1.4) * i / (steps - 1.0)
        need = {e: h.climb for e in h.stations if e - s > -h.nose + 1e-9}
        if s < h.nose:
            need[0.0] = max(need.get(0.0, 0.0), engaged)
        at = sorted(need)
        lev_leaf = [e + h.tab_free for e in at]
        lev_ear = [h.ear_free - e + s for e in at]
        f = _solve(_matrix(h, lev_leaf, lev_ear), [need[e] for e in at])
        total = 2 * sum(f)
        if total > best[0]:
            best = (total,
                    h.ear.stress(list(zip(lev_ear, f))),
                    h.leaf.stress(list(zip(lev_leaf, f))))
    return best


def pinch(h, at=None):
    """Pinching it together: the force in N, the stress in MPa, and the slit left over.

    A hand squeezes the two leaves until the axle clears the ear's face, then slides the
    tongue in. The ear takes no part, so this is the leaf alone, loaded where the fingers
    land and measured at the pin. The third number is how much slit is still open at the
    closest point along the tongue; below zero the leaves meet before the axle clears and
    the tips have to be relieved.
    """
    at = h.blade_out - 2 if at is None else at
    travel = max(h.stub_proud - h.gap, h.climb)
    force = travel / h.leaf.compliance(h.tab_free, at)
    room = min(h.slit(x) - 2 * force * h.leaf.compliance(x, at)
               for x in [h.blade_out * i / 120 for i in range(121)])
    return force, h.leaf.stress([(at, force)]), room


def twist(h):
    """Twisting it apart: torque in N·mm, and the angle it lets go at in degrees.

    Wring a straight joint about the limb's axis and each leaf tilts against its ear, so
    the wedge tips jam diagonally — one leaf at the top, the other at the bottom. Those
    two contacts push each leaf inward and each ear outward, and both work the axle out of
    its bore. It lets go when the pair has opened at the pin by the whole engagement.

    The lever is the ring's radius, where the wedges reach a little further, and the leaf
    is assumed to carry a corner load through to the pin without dishing. Both understate
    the torque, so this is a floor.
    """
    engaged = h.stub_proud - h.gap
    pair = (h.leaf.compliance(h.tab_free, h.tab_free)
            + h.ear.compliance(h.ear_free, h.ear_free))
    clear = h.gap - (h.gap + h.climb) / 2      # what a wedge tip clears by at a detent
    angle = math.degrees((max(clear, 0.0) + engaged) / h.ring_r)
    return 2 * engaged * h.ring_r / pair, angle


def sections(h):
    """What each member breaks at, in N·mm: swing, sideways, twist.

    Swing is the axis the joint is for; the other two are what a hand does to an arm.
    Strength is a section property, so none of this moves when a root moves. The leaf is
    taken at its root, which is where it is worked hardest and where it breaks.
    """
    r = h.r
    width = lambda x: 2 * math.sqrt(max(r * r - x * x, 0.0))
    n = 20000

    def integrate(lo, hi, f):
        return sum(f(lo + (hi - lo) * (i + .5) / n) * (hi - lo) / n for i in range(n))

    out = {}
    ear_i, ear_c = _section(r, h.slot_half, r, h.flat)
    ear_y = math.sqrt(max(r * r - h.slot_half ** 2, 0.0))
    ear_t = lambda y: math.sqrt(max(r * r - y * y, 0.0)) - h.slot_half
    out["fork"] = (
        2 * integrate(h.slot_half, r, lambda x: width(x) ** 3 / 12) / ear_y * YIELD_PETG,
        2 * ear_i / ear_c * YIELD_PETG,
        2 * integrate(-ear_y, ear_y, lambda y: ear_t(y) ** 3 / 3)
        / (r - h.slot_half) * SHEAR_PETG)
    leaf_i, leaf_c = _section(r, h.blade / 2 - h.leaf_root, h.blade / 2, h.flat)
    leaf_y = math.sqrt(max(r * r - (h.blade / 2) ** 2, 0.0))
    out["blade"] = (
        2 * integrate(h.blade / 2 - h.leaf_root, h.blade / 2,
                      lambda x: width(x) ** 3 / 12) / leaf_y * YIELD_PETG,
        2 * leaf_i / leaf_c * YIELD_PETG,
        2 * (2 * leaf_y) * h.leaf_root ** 2 / 3 * SHEAR_PETG)
    return out


if __name__ == "__main__":
    old = Hinge(limb=24.0, blade=10.0, leaf_root=3.0, leaf_tip=3.0, gap=0.15,
                tab_free=20.0, ear_free=21.0, blade_out=32.0, ring_r=8.8387,
                ring_n=24, climb=0.45, stub_proud=1.30, nose=12.0, flat=10.8387)
    t, carry, ear_mpa, leaf_mpa = hold(old)
    print("old tooth-and-valley joint, through this model")
    print("  hold %.0f N*mm, expected 454 N*mm   %s" % (t, "OK" if abs(t - 454) < 1 else "MOVED"))
    print("  %d of %d teeth carry, on %d stations, ear %.1f MPa, leaf %.1f MPa"
          % (carry, old.ring_n, len(old.stations), ear_mpa, leaf_mpa))
    f, ear_p, leaf_p = press(old)
    print("  press %.1f N (%.2f kgf), expected 7.16 kgf   %s"
          % (f, f / 9.81, "OK" if abs(f / 9.81 - 7.16) < 0.02 else "MOVED"))
    print("  ear %.1f MPa, leaf %.1f MPa" % (ear_p, leaf_p))
