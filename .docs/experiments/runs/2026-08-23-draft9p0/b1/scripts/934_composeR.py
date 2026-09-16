from PIL import Image
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"

SU, SL = 6.172, 5.966          # px/mm as measured in each capture
TOP_PX = 164.78                # z = highZ projected to this row in both captures
XC = 923

def strip(path, scale, hi, lo, pad=14):
    im = Image.open(path).convert("RGB")
    y0 = int(TOP_PX - pad)
    y1 = int(TOP_PX + (hi - lo) * scale + pad)
    return im.crop((XC - 100, y0, XC + 100, y1)), y0

u, uy0 = strip(D + "sideR_u_limb.png", SU, 3.6, -112.4)
l, ly0 = strip(D + "sideR_l_limb.png", SL, 12.0, -108.0)

k = SL / SU                                     # match the upper limb to the lower's scale
u = u.resize((round(u.width * k), round(u.height * k)), Image.LANCZOS)

u_elbow = (TOP_PX + (3.6 - (-100.4)) * SU - uy0) * k     # hinge axis row inside the u strip
l_elbow = (TOP_PX + (12.0 - 0.0) * SL - ly0)             # hinge axis row inside the l strip

GAP, MARGIN = 70, 24
Y_L = 620
Y_U = Y_L + l_elbow - u_elbow
top = min(Y_U, Y_L)
Y_U -= top - MARGIN; Y_L -= top - MARGIN

W = MARGIN * 2 + u.width + GAP + l.width
H = MARGIN + max(Y_U + u.height, Y_L + l.height)
out = Image.new("RGB", (W, int(H)), (255, 255, 255))
out.paste(u, (MARGIN, int(Y_U)))
out.paste(l, (MARGIN + u.width + GAP, int(Y_L)))
out.save(F + "cad.parts.limbs.side_by_side.png")
print(out.size, "u elbow row", round(Y_U + u_elbow), "l elbow row", round(Y_L + l_elbow))
