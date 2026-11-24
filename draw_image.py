import os
from PIL import Image, ImageDraw, ImageFont

# 1024x1024 canvas
WIDTH = 1024
HEIGHT = 1024

image = Image.new("RGB", (WIDTH, HEIGHT), "#0F172A")
draw = ImageDraw.Draw(image)

FONT_PATH_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_PATH_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def get_font(size, bold=False):
    path = FONT_PATH_BOLD if bold else FONT_PATH_REG
    try:
        return ImageFont.truetype(path, size)
    except IOError:
        return ImageFont.load_default()

# 1. Header Banner (0 to 95)
draw.rectangle([0, 0, WIDTH, 95], fill="#1E293B")
draw.rectangle([0, 92, WIDTH, 95], fill="#3B82F6") # Accent line

font_title = get_font(26, bold=True)
font_subtitle = get_font(14, bold=False)

draw.text((30, 18), "GLOBAL NEWS CHRONICLE", fill="#F8FAFC", font=font_title)
# Thin accent underline below banner title for visual polish
draw.line([30, 50, 360, 50], fill="#60A5FA", width=2)
draw.text((30, 58), "MONDAY, 23 NOVEMBER 2026 · SPECIAL EDITION", fill="#93C5FD", font=font_subtitle)

# Grid layout for 4 panels
panels = [
    {
        "box": (15, 110, 500, 542),
        "title": "1. COP31 Climate Summit Ends in Deadlock",
        "bg": "#FFFBEB", # warm paper
        "accent": "#B45309"
    },
    {
        "box": (524, 110, 1009, 542),
        "title": "2. Ukraine Sinks Warship Merkury in Libya",
        "bg": "#EFF6FF", # ocean light blue
        "accent": "#1D4ED8"
    },
    {
        "box": (15, 562, 500, 994),
        "title": "3. Factory Fire in Banten, Indonesia",
        "bg": "#FFF1F2", # fire light red
        "accent": "#BE123C"
    },
    {
        "box": (524, 562, 1009, 994),
        "title": "4. BepiColombo Enters Mercury Orbit",
        "bg": "#F8FAFC", # space dark / light grey
        "accent": "#334155"
    }
]

font_panel_title = get_font(15, bold=True)
font_caption = get_font(12, bold=True) # Enhanced caption contrast with bold font

for p in panels:
    x0, y0, x1, y1 = p["box"]
    
    # Draw panel background and border
    draw.rectangle([x0, y0, x1, y1], fill=p["bg"], outline="#CBD5E1", width=2)
    
    # Panel Header box
    draw.rectangle([x0, y0, x1, y0 + 36], fill=p["accent"])
    draw.text((x0 + 12, y0 + 10), p["title"], fill="#FFFFFF", font=font_panel_title)

# --- PANEL 1: COP31 Antalya Climate Summit ---
p1_box = panels[0]["box"]
px0, py0, px1, py1 = p1_box
s_top = py0 + 46
s_bot = py1 - 30

# Background sky/sun
draw.rectangle([px0+2, s_top, px1-2, s_bot], fill="#FEF3C7")
# Palm tree silhouettes
for tx in [px0 + 60, px1 - 80]:
    draw.rectangle([tx-4, s_top + 100, tx+4, s_bot - 40], fill="#78350F")
    for angle_offset in [-40, -20, 0, 20, 40]:
        draw.line([tx, s_top + 100, tx + angle_offset * 2, s_top + 70 + abs(angle_offset)], fill="#047857", width=6)

# Podium / Conference table
draw.rectangle([px0 + 100, s_bot - 110, px1 - 100, s_bot - 70], fill="#92400E")
draw.rectangle([px0 + 120, s_bot - 70, px1 - 120, s_bot - 50], fill="#D97706")

# Stamp / Banner: NO DEAL
draw.rectangle([px0 + 70, s_top + 110, px1 - 70, s_top + 180], outline="#DC2626", width=5)
font_stamp = get_font(28, bold=True)
draw.text((px0 + 105, s_top + 125), "COP31: NO DEAL", fill="#DC2626", font=font_stamp)

# Caption
draw.rectangle([px0, py1 - 28, px1, py1], fill="#1E293B")
draw.text((px0 + 12, py1 - 22), "Antalya: ~200 nations fail to agree after 48h overtime", fill="#FFFFFF", font=font_caption)


# --- PANEL 2: Ukraine Sinks Russian Warship Merkury in Libya ---
p2_box = panels[1]["box"]
px0, py0, px1, py1 = p2_box
s_top = py0 + 46
s_bot = py1 - 30

# Sea background
draw.rectangle([px0+2, s_top, px1-2, s_bot], fill="#1E3A8A")
for wy in range(s_top + 50, s_bot, 40):
    draw.arc([px0 + 20, wy, px1 - 20, wy + 30], 0, 180, fill="#3B82F6", width=3)

# Warship hull silhouette
ship_x = px0 + 120
ship_y = s_bot - 150
draw.polygon([
    (ship_x, ship_y + 40),
    (ship_x + 60, ship_y + 80),
    (ship_x + 220, ship_y + 80),
    (ship_x + 260, ship_y + 40),
    (ship_x + 230, ship_y + 20),
    (ship_x + 40, ship_y + 20)
], fill="#475569")
draw.rectangle([ship_x + 100, ship_y - 20, ship_x + 140, ship_y + 20], fill="#64748B")
draw.line([ship_x + 120, ship_y - 20, ship_x + 120, ship_y - 50], fill="#94A3B8", width=3)

# Explosion / Smoke
draw.ellipse([ship_x + 80, ship_y - 40, ship_x + 180, ship_y + 30], fill="#EF4444")
draw.ellipse([ship_x + 100, ship_y - 70, ship_x + 160, ship_y - 10], fill="#F97316")
draw.ellipse([ship_x + 90, ship_y - 110, ship_x + 170, ship_y - 40], fill="#64748B")

# Naval drone wake
draw.line([ship_x - 80, ship_y + 100, ship_x, ship_y + 60], fill="#93C5FD", width=4)

# Caption
draw.rectangle([px0, py1 - 28, px1, py1], fill="#1E293B")
draw.text((px0 + 12, py1 - 22), "Benghazi Port: Russian corvette Merkury struck by drone", fill="#FFFFFF", font=font_caption)


# --- PANEL 3: Factory Fire in Banten, Indonesia ---
p3_box = panels[2]["box"]
px0, py0, px1, py1 = p3_box
s_top = py0 + 46
s_bot = py1 - 30

# Night sky background
draw.rectangle([px0+2, s_top, px1-2, s_bot], fill="#0F172A")

# Factory building silhouette
fac_x = px0 + 60
fac_y = s_bot - 160
draw.rectangle([fac_x, fac_y, fac_x + 320, s_bot], fill="#1E293B")
draw.rectangle([fac_x + 60, fac_y - 80, fac_x + 90, fac_y], fill="#334155")
draw.rectangle([fac_x + 220, fac_y - 60, fac_x + 250, fac_y], fill="#334155")

# Flames
for fx in range(fac_x + 40, fac_x + 280, 35):
    draw.polygon([
        (fx, fac_y + 20),
        (fx + 15, fac_y - 50),
        (fx + 30, fac_y + 20)
    ], fill="#EF4444")
    draw.polygon([
        (fx + 5, fac_y + 10),
        (fx + 15, fac_y - 30),
        (fx + 25, fac_y + 10)
    ], fill="#FBBF24")

# Smoke clouds rising
draw.ellipse([fac_x + 40, s_top + 40, fac_x + 180, s_top + 130], fill="#475569")
draw.ellipse([fac_x + 120, s_top + 20, fac_x + 280, s_top + 100], fill="#334155")

# Stat callout box
draw.rectangle([px0 + 40, s_top + 10, px1 - 40, s_top + 50], fill="#7F1D1D", outline="#EF4444", width=2)
font_alert = get_font(13, bold=True)
draw.text((px0 + 55, s_top + 20), "BANTEN BLAZE: 24+ KILLED, ~30 MISSING", fill="#FEE2E2", font=font_alert)

# Caption
draw.rectangle([px0, py1 - 28, px1, py1], fill="#1E293B")
draw.text((px0 + 12, py1 - 22), "Candy factory fire in Indonesia triggers massive rescue", fill="#FFFFFF", font=font_caption)


# --- PANEL 4: BepiColombo Enters Mercury Orbit ---
p4_box = panels[3]["box"]
px0, py0, px1, py1 = p4_box
s_top = py0 + 46
s_bot = py1 - 30

# Space background with stars
draw.rectangle([px0+2, s_top, px1-2, s_bot], fill="#030712")
star_coords = [
    (40, 30), (120, 70), (200, 40), (320, 90), (410, 50), (450, 120),
    (70, 180), (150, 220), (280, 170), (380, 210), (430, 260),
    (90, 310), (210, 340), (300, 300), (400, 350), (460, 310)
]
for sx, sy in star_coords:
    draw.ellipse([px0 + sx, s_top + sy, px0 + sx + 3, s_top + sy + 3], fill="#FFFFFF")

# Planet Mercury
merc_cx = px0 + 150
merc_cy = s_top + 200
merc_r = 75
draw.ellipse([merc_cx - merc_r, merc_cy - merc_r, merc_cx + merc_r, merc_cy + merc_r], fill="#6B7280")
craters = [
    (-25, -20, 12), (20, -30, 16), (-10, 25, 20), (35, 20, 14), (-40, 10, 10)
]
for cx_off, cy_off, cr in craters:
    cx = merc_cx + cx_off
    cy = merc_cy + cy_off
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], outline="#4B5563", width=3)

# Spacecraft (BepiColombo)
sc_x = px0 + 330
sc_y = s_top + 130
draw.rectangle([sc_x - 50, sc_y - 8, sc_x + 50, sc_y + 8], fill="#38BDF8", outline="#0284C7", width=1)
draw.rectangle([sc_x - 12, sc_y - 15, sc_x + 12, sc_y + 15], fill="#E2E8F0")
draw.arc([sc_x + 12, sc_y - 12, sc_x + 28, sc_y + 12], 270, 90, fill="#F59E0B", width=2)
draw.arc([merc_cx - 110, merc_cy - 110, merc_cx + 110, merc_cy + 110], 300, 120, fill="#38BDF8", width=2)

draw.text((px0 + 20, s_top + 10), "ESA / JAXA · 8-YEAR JOURNEY COMPLETE", fill="#38BDF8", font=get_font(11, bold=True))

# Caption
draw.rectangle([px0, py1 - 28, px1, py1], fill="#1E293B")
draw.text((px0 + 12, py1 - 22), "BepiColombo spacecraft successfully enters Mercury orbit", fill="#FFFFFF", font=font_caption)


# Save entry.png
output_path = "entry.png"
image.save(output_path, "PNG", optimize=True)

print(f"Successfully generated {output_path}")
