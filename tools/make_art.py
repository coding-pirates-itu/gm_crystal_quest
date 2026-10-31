"""Draws the Crystal Quest tileset and sprites as simple pixel art. Output: <out>/<sprite>/<n>.png"""
import math, os, random, sys
from PIL import Image, ImageDraw

OUT = sys.argv[1]
T = (0, 0, 0, 0)

def new(w, h):
    return Image.new("RGBA", (w, h), T)

def save(name, frames):
    d = os.path.join(OUT, name)
    os.makedirs(d, exist_ok=True)
    for i, f in enumerate(frames):
        f.save(os.path.join(d, f"{i}.png"))

def rect(d, x0, y0, x1, y1, c):
    d.rectangle([x0, y0, x1, y1], fill=c)

def speckle(img, colours, n, seed):
    rnd = random.Random(seed)
    for _ in range(n):
        x, y = rnd.randrange(32), rnd.randrange(32)
        img.putpixel((x, y), rnd.choice(colours))

OUTL = (40, 30, 30, 255)
SKIN = (240, 195, 150, 255)
EYE = (30, 25, 25, 255)

# ------------------------------------------------------------ tiles
GRASS = (110, 180, 80, 255)

def t_grass(seed=1):
    img = Image.new("RGBA", (32, 32), GRASS)
    speckle(img, [(95, 160, 70, 255), (130, 200, 95, 255)], 70, seed)
    return img

def t_flowers():
    img = t_grass(2)
    d = ImageDraw.Draw(img)
    for (x, y, c) in [(6, 8, (255, 240, 90, 255)), (22, 6, (255, 140, 180, 255)), (14, 18, (255, 255, 255, 255)),
                      (26, 24, (255, 240, 90, 255)), (5, 26, (255, 140, 180, 255))]:
        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            img.putpixel((x + dx, y + dy), c)
        img.putpixel((x, y), (240, 160, 40, 255))
    return img

def t_path():
    img = Image.new("RGBA", (32, 32), (205, 175, 120, 255))
    speckle(img, [(185, 155, 100, 255), (220, 195, 145, 255), (170, 140, 95, 255)], 80, 3)
    return img

def t_floor(cracked=False):
    img = Image.new("RGBA", (32, 32), (120, 110, 105, 255))
    d = ImageDraw.Draw(img)
    for y in (0, 16):
        d.line([0, y, 31, y], fill=(90, 82, 78, 255))
    for (x, y0) in [(0, 0), (16, 0), (8, 16), (24, 16)]:
        d.line([x, y0, x, y0 + 15], fill=(90, 82, 78, 255))
    speckle(img, [(132, 122, 116, 255), (108, 98, 94, 255)], 40, 4)
    if cracked:
        d.line([6, 4, 12, 10, 10, 18, 16, 26], fill=(60, 54, 50, 255))
        d.line([12, 10, 18, 12], fill=(60, 54, 50, 255))
    return img

def t_bridge():
    img = Image.new("RGBA", (32, 32), (70, 120, 200, 255))
    d = ImageDraw.Draw(img)
    for y in range(0, 32, 8):
        rect(d, 0, y, 31, y + 6, (170, 120, 70, 255))
        d.line([0, y, 31, y], fill=(200, 150, 95, 255))
        d.line([0, y + 6, 31, y + 6], fill=(120, 80, 45, 255))
    return img

def t_cave():
    img = t_grass(5)
    d = ImageDraw.Draw(img)
    d.rectangle([2, 0, 29, 31], fill=(110, 105, 100, 255))
    d.ellipse([5, 2, 26, 30], fill=(20, 16, 18, 255))
    d.rectangle([5, 16, 26, 31], fill=(20, 16, 18, 255))
    return img

def t_tree():
    img = t_grass(6)
    d = ImageDraw.Draw(img)
    rect(d, 13, 22, 18, 31, (110, 70, 40, 255))
    d.ellipse([2, 1, 29, 26], fill=(40, 110, 50, 255))
    d.ellipse([5, 3, 24, 20], fill=(55, 140, 60, 255))
    d.ellipse([8, 5, 16, 12], fill=(80, 170, 80, 255))
    return img

def t_bush():
    img = t_grass(7)
    d = ImageDraw.Draw(img)
    d.ellipse([3, 8, 28, 29], fill=(140, 136, 130, 255))
    d.ellipse([6, 10, 20, 22], fill=(170, 166, 160, 255))
    d.line([10, 24, 22, 24], fill=(100, 96, 92, 255))
    return img

def t_water():
    img = Image.new("RGBA", (32, 32), (70, 120, 200, 255))
    d = ImageDraw.Draw(img)
    for (x, y) in [(4, 6), (18, 12), (8, 22), (22, 26)]:
        d.line([x, y, x + 6, y], fill=(140, 190, 240, 255))
    return img

def t_fence():
    img = t_grass(8)
    d = ImageDraw.Draw(img)
    rect(d, 0, 10, 31, 13, (170, 120, 70, 255))
    rect(d, 0, 20, 31, 23, (170, 120, 70, 255))
    for x in (3, 19):
        rect(d, x, 6, x + 5, 28, (190, 140, 85, 255))
        d.line([x, 6, x, 28], fill=(130, 90, 50, 255))
    return img

def t_house():
    img = Image.new("RGBA", (32, 32), (230, 215, 180, 255))
    d = ImageDraw.Draw(img)
    rect(d, 0, 0, 3, 31, (140, 95, 55, 255)); rect(d, 28, 0, 31, 31, (140, 95, 55, 255))
    rect(d, 10, 8, 21, 19, (90, 140, 200, 255))
    d.rectangle([10, 8, 21, 19], outline=(110, 75, 45, 255))
    d.line([15, 8, 15, 19], fill=(110, 75, 45, 255)); d.line([10, 13, 21, 13], fill=(110, 75, 45, 255))
    return img

def t_roof():
    img = Image.new("RGBA", (32, 32), (190, 60, 50, 255))
    d = ImageDraw.Draw(img)
    for y in range(0, 30, 6):
        d.line([0, y, 31, y], fill=(150, 40, 35, 255))
        for x in range((y // 6) % 2 * 4, 32, 8):
            img.putpixel((x, y + 3), (150, 40, 35, 255))
    return img

def t_dwall(torch=False):
    img = Image.new("RGBA", (32, 32), (70, 65, 75, 255))
    d = ImageDraw.Draw(img)
    for row in range(4):
        y0 = row * 8
        off = 0 if row % 2 == 0 else -8
        for col in range(-1, 3):
            x0 = off + col * 16
            rect(d, x0 + 1, y0 + 1, x0 + 14, y0 + 6, (95, 90, 102, 255))
            d.line([x0 + 1, y0 + 1, x0 + 14, y0 + 1], fill=(120, 115, 128, 255))
    if torch:
        rect(d, 14, 14, 17, 24, (110, 70, 40, 255))
        d.ellipse([11, 4, 20, 15], fill=(255, 150, 40, 255))
        d.ellipse([13, 7, 18, 13], fill=(255, 230, 120, 255))
    return img

tiles = [new(32, 32), t_grass(), t_flowers(), t_path(),
         t_floor(), t_bridge(), t_cave(), t_floor(True),
         t_tree(), t_bush(), t_water(), t_fence(),
         t_house(), t_roof(), t_dwall(), t_dwall(True)]
sheet = new(128, 128)
for i, t in enumerate(tiles):
    sheet.alpha_composite(t, ((i % 4) * 32, (i // 4) * 32))
save("tss_World", [sheet])

# ------------------------------------------------------------ heroes (facing right)
def hero(kind, step, idle):
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    bob = 1 if (idle and step == 1) or (not idle and step in (1, 3)) else 0
    top = 3 + bob
    if kind == "knight":
        body, body_d, head = (180, 186, 200, 255), (120, 126, 140, 255), (190, 196, 210, 255)
        cape = (50, 90, 200, 255)
        rect(d, 8, top + 12, 12, top + 24, cape)                       # cape behind
        rect(d, 10, top, 21, top + 10, head)                           # helmet
        rect(d, 10, top, 21, top + 1, (220, 225, 235, 255))
        rect(d, 16, top + 4, 21, top + 6, EYE)                         # visor slit
        rect(d, 14, top - 2, 16, top, (200, 40, 40, 255))              # plume
        rect(d, 10, top + 11, 21, top + 21, body)
        rect(d, 10, top + 11, 11, top + 21, body_d)
        rect(d, 10, top + 18, 21, top + 19, (110, 70, 40, 255))        # belt
        # shield in front
        rect(d, 20, top + 11, 25, top + 21, (50, 90, 200, 255))
        rect(d, 22, top + 12, 23, top + 20, (240, 210, 60, 255))
        legs = (100, 106, 120, 255)
    else:
        hood, hood_d = (60, 140, 60, 255), (40, 100, 45, 255)
        rect(d, 9, top, 22, top + 10, hood)                            # hood
        rect(d, 9, top, 22, top + 1, (90, 170, 85, 255))
        rect(d, 13, top + 3, 22, top + 10, SKIN)                       # face
        rect(d, 18, top + 5, 19, top + 6, EYE)
        rect(d, 9, top + 3, 12, top + 10, hood_d)
        rect(d, 10, top + 11, 21, top + 21, (130, 90, 55, 255))       # leather
        rect(d, 10, top + 11, 11, top + 21, (100, 65, 40, 255))
        rect(d, 10, top + 18, 21, top + 19, (70, 45, 30, 255))
        d.arc([4, top + 6, 14, top + 24], 90, 270, fill=(150, 100, 50, 255))   # bow on the back
        d.line([9, top + 7, 9, top + 23], fill=(230, 230, 230, 255))
        legs = (80, 60, 40, 255)
    # legs
    if idle:
        a, b = 11, 17
    else:
        s = [0, 2, 0, 2][step]
        a, b = (11 - s, 17 + s) if step < 2 else (11 + s, 17 - s)
    rect(d, a, top + 22, a + 3, 29, legs)
    rect(d, b, top + 22, b + 3, 29, legs)
    rect(d, a - 1, 29, a + 4, 30, OUTL)
    rect(d, b - 1, 29, b + 5, 30, OUTL)
    # sword arm
    rect(d, 21 if kind == "ranger" else 6, top + 12, (23 if kind == "ranger" else 8), top + 17, SKIN)
    return img

for kind, name in [("knight", "Knight"), ("ranger", "Ranger")]:
    save(f"s_{name}Idle", [hero(kind, i, True) for i in range(2)])
    save(f"s_{name}Walk", [hero(kind, i, False) for i in range(4)])

# ------------------------------------------------------------ sword slash (pointing right)
def slash(i):
    # a sweeping crescent in front of the hero (right side), growing over 4 frames
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    end = -70 + 45 * (i + 1)
    alpha = [255, 255, 230, 150][i]
    d.arc([-2, 0, 30, 31], -70, end, fill=(255, 255, 255, alpha), width=6)
    d.arc([1, 3, 27, 28], -70, end, fill=(190, 225, 255, alpha), width=3)
    return img

save("s_Slash", [slash(i) for i in range(4)])

# ------------------------------------------------------------ enemies
def slime(i):
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    h = [14, 12, 10, 12][i]
    w = [11, 12, 14, 12][i]
    top = 30 - h
    d.ellipse([16 - w, top, 15 + w, 30 + h // 2], fill=(90, 200, 70, 235), outline=(30, 110, 30, 255))
    rect(d, 0, 31, 31, 31, T)
    rect(d, 16 - w // 2 - 2, top + 3, 16 - w // 2, top + 4, (210, 255, 200, 255))
    rect(d, 11, top + 5, 13, top + 8, (255, 255, 255, 255)); rect(d, 18, top + 5, 20, top + 8, (255, 255, 255, 255))
    rect(d, 12, top + 6, 13, top + 8, EYE); rect(d, 19, top + 6, 20, top + 8, EYE)
    img = img.crop((0, 0, 32, 32))
    return img

def skeleton(i):
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    bone, bone_d = (235, 232, 220, 255), (170, 165, 150, 255)
    bob = i % 2
    top = 3 + bob
    d.ellipse([10, top, 21, top + 10], fill=bone)
    rect(d, 12, top + 4, 14, top + 6, EYE); rect(d, 17, top + 4, 19, top + 6, EYE)
    rect(d, 14, top + 8, 17, top + 9, bone_d)
    rect(d, 15, top + 11, 16, top + 21, bone)                     # spine
    for y in (top + 13, top + 16, top + 19):
        rect(d, 11, y, 20, y, bone)                               # ribs
    s = [0, 2, 0, -2][i]
    rect(d, 8, top + 12 + max(0, s), 9, top + 20 + max(0, s), bone)
    rect(d, 22, top + 12 + max(0, -s), 23, top + 20 + max(0, -s), bone)
    rect(d, 23, top + 6, 24, top + 22, (170, 170, 180, 255))      # rusty sword
    rect(d, 21, top + 18, 26, top + 19, (120, 80, 40, 255))
    a, b = (12 - abs(s) // 2, 18 + abs(s) // 2)
    rect(d, a, top + 22, a + 1, 29, bone); rect(d, b, top + 22, b + 1, 29, bone)
    rect(d, a - 1, 29, a + 2, 30, bone_d); rect(d, b - 1, 29, b + 2, 30, bone_d)
    return img

def guardian(i):
    img = new(64, 64)
    d = ImageDraw.Draw(img)
    stone, stone_d, stone_l = (110, 90, 140, 255), (75, 60, 100, 255), (140, 120, 170, 255)
    bob = [0, 1, 2, 1][i]
    top = 6 + bob
    rect(d, 14, top + 14, 49, top + 44, stone)                     # body
    rect(d, 14, top + 14, 17, top + 44, stone_d)
    rect(d, 20, top, 43, top + 14, stone)                          # head
    rect(d, 20, top, 43, top + 2, stone_l)
    glow = [(255, 80, 60, 255), (255, 140, 60, 255), (255, 200, 80, 255), (255, 140, 60, 255)][i]
    rect(d, 24, top + 5, 29, top + 8, glow); rect(d, 34, top + 5, 39, top + 8, glow)
    rect(d, 4, top + 16, 13, top + 36, stone_d)                    # arms
    rect(d, 50, top + 16, 59, top + 36, stone_d)
    rect(d, 2, top + 34, 14, top + 42, stone)                      # fists
    rect(d, 49, top + 34, 61, top + 42, stone)
    rect(d, 28, top + 22, 35, top + 29, (90, 200, 255, 255))       # crystal in the chest
    rect(d, 30, top + 23, 31, top + 25, (220, 250, 255, 255))
    rect(d, 18, top + 45, 27, 61, stone_d); rect(d, 36, top + 45, 45, 61, stone_d)
    rect(d, 16, 60, 29, 63, OUTL); rect(d, 34, 60, 47, 63, OUTL)
    return img

save("s_Slime", [slime(i) for i in range(4)])
save("s_Skeleton", [skeleton(i) for i in range(4)])
save("s_Guardian", [guardian(i) for i in range(4)])

# ------------------------------------------------------------ villager (facing right)
def villager(i):
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    top = 3 + i
    robe = (150, 60, 160, 255)
    rect(d, 11, top + 2, 21, top + 10, SKIN)
    rect(d, 10, top, 22, top + 2, (220, 220, 220, 255))           # white hair
    rect(d, 17, top + 4, 18, top + 5, EYE)
    rect(d, 12, top + 7, 21, top + 13, (240, 240, 240, 255))      # beard
    rect(d, 9, top + 12, 22, 29, robe)
    rect(d, 9, top + 12, 10, 29, (110, 40, 120, 255))
    rect(d, 24, top + 2, 25, 30, (140, 95, 55, 255))              # staff
    rect(d, 22, top + 14, 24, top + 16, SKIN)
    rect(d, 10, 29, 21, 30, OUTL)
    return img

save("s_Villager", [villager(i) for i in range(2)])

# ------------------------------------------------------------ items
def potion():
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    rect(d, 14, 6, 17, 10, (200, 200, 210, 255))
    rect(d, 13, 4, 18, 6, (140, 95, 55, 255))
    d.ellipse([8, 10, 23, 26], fill=(220, 40, 70, 255), outline=(120, 20, 40, 255))
    rect(d, 11, 14, 13, 16, (255, 180, 190, 255))
    return img

def chest(open_):
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    wood, wood_d = (170, 110, 55, 255), (110, 70, 35, 255)
    gold = (240, 200, 60, 255)
    if open_:
        rect(d, 4, 6, 27, 13, wood_d)                             # lid opened backwards
        rect(d, 4, 14, 27, 28, wood)
        rect(d, 6, 14, 25, 17, (40, 25, 15, 255))                 # empty inside
    else:
        rect(d, 4, 9, 27, 28, wood)
        rect(d, 4, 9, 27, 15, (190, 125, 65, 255))
    if not open_:
        rect(d, 4, 18, 27, 19, gold)
    d.rectangle([4, 9 if not open_ else 14, 27, 28], outline=wood_d)
    rect(d, 14, 16, 17, 20, gold)
    return img

def locked_door():
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    rect(d, 2, 0, 29, 31, (60, 60, 70, 255))
    for x in (6, 12, 18, 24):
        rect(d, x, 0, x + 2, 31, (150, 150, 165, 255))
    rect(d, 2, 6, 29, 8, (150, 150, 165, 255)); rect(d, 2, 22, 29, 24, (150, 150, 165, 255))
    rect(d, 12, 12, 19, 19, (230, 190, 60, 255))                  # lock
    rect(d, 15, 14, 16, 17, EYE)
    return img

def crystal(i):
    img = new(32, 32)
    d = ImageDraw.Draw(img)
    d.polygon([(16, 2), (25, 12), (16, 30), (7, 12)], fill=(90, 200, 255, 255), outline=(30, 90, 170, 255))
    d.polygon([(16, 2), (20, 12), (16, 30), (12, 12)], fill=(160, 230, 255, 255))
    sx, sy = [(12, 8), (19, 11), (16, 18), (13, 13)][i]
    for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        img.putpixel((sx + dx, sy + dy), (255, 255, 255, 255))
    return img

def heart(full):
    img = new(16, 16)
    d = ImageDraw.Draw(img)
    c = (230, 40, 60, 255) if full else (70, 50, 55, 255)
    d.ellipse([1, 2, 8, 9], fill=c); d.ellipse([7, 2, 14, 9], fill=c)
    d.polygon([(1, 6), (14, 6), (8, 14)], fill=c)
    if full:
        d.point([(4, 4), (4, 5), (5, 4)], fill=(255, 190, 200, 255))
    return img

def key():
    img = new(16, 16)
    d = ImageDraw.Draw(img)
    d.ellipse([1, 4, 7, 10], outline=(240, 200, 60, 255), width=2)
    rect(d, 7, 6, 14, 8, (240, 200, 60, 255))
    rect(d, 11, 9, 12, 11, (240, 200, 60, 255)); rect(d, 13, 9, 14, 12, (240, 200, 60, 255))
    return img

def poof(i):
    img = new(32, 32)
    rnd = random.Random(30 + i)
    r = [4, 8, 11, 13, 14, 13][i]
    alpha = [255, 255, 230, 180, 120, 60][i]
    for _ in range(8):
        a = rnd.random() * math.tau
        cx, cy = 16 + math.cos(a) * r * 0.5, 16 + math.sin(a) * r * 0.5
        rr = r * 0.55
        ImageDraw.Draw(img).ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(235, 235, 240, alpha))
    return img

def card():
    img = new(256, 440)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, 255, 439], 16, fill=(240, 225, 185, 255), outline=(140, 95, 55, 255), width=6)
    d.rounded_rectangle([14, 14, 241, 200], 10, fill=(110, 180, 80, 255))
    return img

def room_exit():
    img = Image.new("RGBA", (32, 32), (60, 220, 90, 110))
    d = ImageDraw.Draw(img)
    d.polygon([(8, 8), (24, 16), (8, 24)], fill=(255, 255, 255, 200))
    return img

save("s_Potion", [potion()])
save("s_Chest", [chest(False), chest(True)])
save("s_LockedDoor", [locked_door()])
save("s_Crystal", [crystal(i) for i in range(4)])
save("s_Heart", [heart(True), heart(False)])
save("s_Key", [key()])
save("s_Poof", [poof(i) for i in range(6)])
save("s_Card", [card()])
save("s_RoomExit", [room_exit()])

# preview sheet
names = sorted(n for n in os.listdir(OUT) if os.path.isdir(os.path.join(OUT, n)) and n not in ("s_Card",))
sheet = Image.new("RGBA", (8 * 70 + 160, len(names) * 70 + 70), (40, 40, 48, 255))
d = ImageDraw.Draw(sheet)
for r, n in enumerate(names):
    d.text((4, r * 70 + 30), n, fill=(255, 255, 255, 255))
    files = sorted(os.listdir(os.path.join(OUT, n)), key=lambda f: int(f.split(".")[0]))
    for c, f in enumerate(files):
        im = Image.open(os.path.join(OUT, n, f))
        sheet.alpha_composite(im, (160 + c * 70, r * 70 + 2))
sheet.resize((sheet.width * 2, sheet.height * 2), Image.NEAREST).save(os.path.join(os.path.dirname(OUT.rstrip("/")), "preview.png"))
