#!/usr/bin/env python3
"""Build a native, fully editable PowerPoint version of the booth loop deck.

Run with: uv run --with python-pptx scripts/build-pptx.py
Output: build/slides-native.pptx

Text, cards and layout are real PowerPoint shapes. Logos and QR codes are
pictures (SVGs are rasterised first, PowerPoint via python-pptx has no SVG).
"""
import subprocess
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
TMP = ROOT / "build" / "pptx-assets"
OUT = ROOT / "build" / "slides-native.pptx"

NAVY = RGBColor(0x12, 0x17, 0x2B)
CYAN = RGBColor(0x09, 0xBA, 0xC8)
CARD = RGBColor(0x1E, 0x25, 0x40)
MUTED = RGBColor(0xC9, 0xCE, 0xDD)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Overpass"

SW, SH = 13.333, 7.5
MARGIN = 0.7


def raster(path: Path, height_px: int = 600) -> Path:
    """Return a PNG for any asset (rasterises SVGs once)."""
    if path.suffix.lower() != ".svg":
        return path
    TMP.mkdir(parents=True, exist_ok=True)
    out = TMP / (path.stem + ".png")
    subprocess.run(
        ["rsvg-convert", "-h", str(height_px), str(path), "-o", str(out)],
        check=True,
    )
    return out


def fill_bg(slide, color):
    bg = slide.background.fill
    bg.solid()
    bg.fore_color.rgb = color


def rect(slide, x, y, w, h, color, shape=MSO_SHAPE.RECTANGLE, shadow=False):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid()
    s.fill.fore_color.rgb = color
    s.line.fill.background()
    if not shadow:
        s.shadow.inherit = False
    return s


def text(slide, x, y, w, h, runs, size, color=WHITE, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, name=None):
    """runs: str or list of (text, bold) tuples."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if name:
        tb.name = name
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    if isinstance(runs, str):
        runs = [(runs, bold)]
    for t, b in runs:
        r = p.add_run()
        r.text = t
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = b
        r.font.color.rgb = color
    return tb


def picture(slide, path, x, y, w, h, align="center", name=None):
    """Place a picture inside the (x, y, w, h) box, preserving aspect ratio."""
    path = raster(Path(path))
    iw, ih = Image.open(path).size
    scale = min(w / iw, h / ih)
    pw, ph = iw * scale, ih * scale
    px = x + (w - pw) / 2 if align == "center" else (x + w - pw if align == "right" else x)
    py = y + (h - ph) / 2
    pic = slide.shapes.add_picture(str(path), Inches(px), Inches(py), Inches(pw), Inches(ph))
    if name:
        pic.name = name
    return pic


def header(slide, title):
    """White slide with a navy title band and the Flatcar logo top-right."""
    fill_bg(slide, WHITE)
    rect(slide, 0, 0, SW, 1.15, NAVY)
    text(slide, MARGIN * 0.8, 0, 10.5, 1.15, title, 36, CYAN, bold=True,
         anchor=MSO_ANCHOR.MIDDLE, name="Title")
    picture(slide, ASSETS / "flatcar-logo.svg", SW - 2.0, 0.12, 1.5, 0.92, align="right",
            name="Flatcar logo")


def slide_qr(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    fill_bg(s, NAVY)
    picture(s, ASSETS / "logos/flatcar-logotype/icon/color/flatcar-icon-color.svg",
            MARGIN, 0.5, 1.6, 1.1, align="left", name="Flatcar logo")
    text(s, 2.65, 0.5, 9.5, 0.7, "Flatcar Container Linux", 40, CYAN, bold=True,
         name="Title")
    text(s, 2.65, 1.2, 9.8, 0.45,
         "A secure, minimal Linux for containers. Scan and come talk to us!",
         18, WHITE, bold=True, name="Subtitle")

    cards = [
        ("flatcar_org.png", "Website", "flatcar.org"),
        ("flatcar_gh.png", "GitHub", "flatcar/Flatcar"),
        ("flatcar_discord.png", "Discord", "Chat with the community"),
        ("flatcar_learning_series.png", "Learning series", "Get started with Flatcar"),
    ]
    gap = 0.45
    cw = (SW - 2 * MARGIN - 3 * gap) / 4
    top, ch = 2.1, 3.75
    for i, (img, label, sub) in enumerate(cards):
        x = MARGIN + i * (cw + gap)
        rect(s, x, top, cw, ch, WHITE, MSO_SHAPE.ROUNDED_RECTANGLE).adjustments[0] = 0.06
        picture(s, ASSETS / "qr" / img, x + 0.15, top + 0.15, cw - 0.3, cw - 0.3,
                name=f"QR {label}")
        text(s, x, top + cw + 0.05, cw, 0.4, label, 20, NAVY, bold=True,
             align=PP_ALIGN.CENTER, name=f"{label} label")
        text(s, x, top + cw + 0.5, cw, 0.35, sub, 13, NAVY, align=PP_ALIGN.CENTER,
             name=f"{label} caption")

    text(s, MARGIN, 6.1, 11.5, 0.4,
         [("Project Pavilion, kiosk P-8A", True), (" · Hall 5, Cosmic Canyon Zone", False)],
         19, WHITE, name="Location")
    text(s, MARGIN, 6.65, 11.5, 0.35,
         [("Office hours", True), (" · every 2nd Thu, 16:30 CEST     ", False),
          ("Dev sync", True), (" · every 4th Thu, 16:30 CEST", False)],
         13, WHITE, name="Meetings")


def slide_bullets(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    header(s, "A secure, minimal Linux for containers")
    items = [
        ("Purpose-built for containers:", " no package manager, no config drift"),
        ("Immutable filesystem:", " eliminates entire classes of vulnerabilities"),
        ("Atomic A/B updates:", " reliable, always-current OS upgrades"),
        ("Ignition provisioning:", " declarative setup on first boot"),
        ("Open and vendor-neutral:", " stewarded by the CNCF"),
    ]
    y = 1.65
    for head, rest in items:
        dot = rect(s, MARGIN, y + 0.14, 0.12, 0.12, CYAN, MSO_SHAPE.OVAL)
        dot.name = "Bullet"
        text(s, MARGIN + 0.35, y, 11.5, 0.5, [(head, True), (rest, False)], 24, NAVY,
             name="Bullet text")
        y += 0.78
    picture(s, ASSETS / "logos/external/cncf-banner.png", 3.9, 5.75, 5.5, 1.4,
            name="CNCF")


def slide_designed(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    fill_bg(s, NAVY)
    # Same geometry as the Marp theme: 10in wide art, anchored right, bleeding
    # off the bottom; cropped so nothing hangs off the slide.
    stairs = raster(ASSETS / "backgrounds/flatcar-staircase-right.svg", 1400)
    left, top, vis_w, vis_h = SW - 9.37, 1.39, 9.37, SH - 1.39
    pic = s.shapes.add_picture(str(stairs), Inches(left), Inches(top), Inches(vis_w),
                               Inches(vis_h))
    pic.crop_right = 0.063
    pic.crop_bottom = 0.5
    pic.name = "Staircase"
    text(s, MARGIN, 1.5, 10, 0.35, "FLATCAR CONTAINER LINUX", 14, CYAN, bold=True,
         name="Kicker")
    text(s, MARGIN, 1.9, 10, 0.9, "Designed for", 40, WHITE, bold=True, name="Title")
    cards = [
        ("01", "Containers", "Kubernetes or your runtime of choice"),
        ("02", "Infra automation", "Declarative provisioning with Ignition"),
        ("03", "Security", "Read-only, verified, automatically updated"),
    ]
    gap = 0.45
    cw = (SW - 2 * MARGIN - 2 * gap) / 3
    top, ch = 3.1, 2.85
    for i, (num, title, sub) in enumerate(cards):
        x = MARGIN + i * (cw + gap)
        rect(s, x, top, cw, ch, CARD).name = f"Card {num}"
        rect(s, x, top, 0.06, ch, CYAN).name = f"Card {num} accent"
        text(s, x + 0.4, top + 0.3, cw - 0.7, 0.3, num, 14, CYAN, bold=True,
             name=f"{title} number")
        text(s, x + 0.4, top + 0.65, cw - 0.7, 0.95, title, 28, WHITE, bold=True,
             name=f"{title} title")
        text(s, x + 0.4, top + 1.8, cw - 0.7, 0.8, sub, 18, MUTED,
             name=f"{title} description")


def slide_everywhere(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    header(s, "Runs everywhere")
    logos = [
        ("aws-logo.svg", "AWS"), ("azure.svg", "Azure"), ("gcp.png", "GCP"),
        ("openstack.png", "OpenStack"), ("hetzner.png", "Hetzner"),
        ("Vmware.svg", "VMware"), ("Logo_Proxmox.svg", "Proxmox"),
        ("Qemu_logo.svg", "QEMU"), ("kube-virt.svg", "KubeVirt"),
        ("akamai-logo.svg", "Akamai"),
    ]
    cols, cell_w, cell_h = 5, 2.2, 1.55
    gx = (SW - cols * cell_w) / (cols + 1)
    for i, (f, name) in enumerate(logos):
        r, c = divmod(i, cols)
        x = gx + c * (cell_w + gx)
        y = 1.75 + r * (cell_h + 0.45)
        picture(s, ASSETS / "logos/external/clouds" / f, x + 0.15, y + 0.1, cell_w - 0.3,
                cell_h - 0.2, name=name)
    text(s, 0, 6.35, SW, 0.5, "Plus bare metal, and many more.", 22, NAVY, bold=True,
         align=PP_ALIGN.CENTER, name="Caption")


def main():
    prs = Presentation()
    prs.slide_width = Inches(SW)
    prs.slide_height = Inches(SH)
    slide_qr(prs)
    slide_bullets(prs)
    slide_designed(prs)
    slide_everywhere(prs)
    OUT.parent.mkdir(exist_ok=True)
    prs.save(OUT)
    print(f"✅ Native PowerPoint: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
