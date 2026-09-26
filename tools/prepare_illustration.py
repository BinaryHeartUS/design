#!/usr/bin/env python3
"""Trim transparent padding from a BinaryHeart illustration and resize it.

The source PNGs in assets/illustrations/full are 2000x2000 with lots of empty
space. Emails and web pages want tight, small files.

Usage:
  python3 prepare_illustration.py SRC.png OUT.png [--max 640]
  python3 prepare_illustration.py --curated OUT_DIR   # rebuild the curated set

Requires Pillow (pip install pillow).
"""
import argparse, os, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
# Works both inside the skill (assets/illustrations/full) and in the repo (illustrations/source).
FULL = next((p for p in (os.path.join(HERE, "..", "assets", "illustrations", "full"),
                         os.path.join(HERE, "..", "illustrations", "source")) if os.path.isdir(p)),
            os.path.join(HERE, "..", "illustrations", "source"))

# name -> (path under full/, max px). Keep in sync with references/illustrations.md
CURATED = {
    "laptop-teardown": ("repair-and-setup-scenes/png/repair-and-parts/repair-02-laptop-teardown.png", 800),
    "knolling-parts": ("repair-and-setup-scenes/png/repair-and-parts/repair-08-knolling-parts.png", 800),
    "open-test-bench": ("repair-and-setup-scenes/png/repair-and-parts/repair-01-open-test-bench.png", 800),
    "gpu-service": ("repair-and-setup-scenes/png/repair-and-parts/repair-10-gpu-service.png", 800),
    "phone-teardown": ("repair-and-setup-scenes/png/repair-and-parts/repair-05-phone-teardown.png", 800),
    "refurb-bundle": ("repair-and-setup-scenes/png/setups-no-desk/setup-13-refurb-bundle.png", 800),
    "triple-monitor": ("repair-and-setup-scenes/png/setups-no-desk/setup-09-triple-monitor.png", 800),
    "video-call-corner": ("repair-and-setup-scenes/png/setups-no-desk/setup-11-video-call-corner.png", 800),
    "laptop": ("core-devices/png/01-laptop.png", 480),
    "retro-computer": ("core-devices/png/02-retro-computer.png", 480),
    "tower-pc": ("core-devices/png/03-tower-pc.png", 480),
    "smartphone": ("core-devices/png/04-smartphone.png", 480),
    "floppy-stack": ("core-devices/png/05-floppy-stack.png", 480),
    "donation-box": ("core-devices/png/06-donation-box.png", 480),
    "tower-open-repair": ("devices-and-tools/png/towers/tower-03-open-repair.png", 480),
    "green-terminal": ("devices-and-tools/png/monitors/setup-03-green-terminal.png", 480),
    "laptop-refurb-progress": ("devices-and-tools/png/laptops/laptop-05-refurb-progress.png", 480),
    "phone-cracked-repair": ("devices-and-tools/png/phones/phone-04-cracked-repair.png", 480),
    "precision-kit": ("devices-and-tools/png/misc/tool-03-precision-kit.png", 480),
    "toolbox": ("devices-and-tools/png/misc/tool-05-toolbox.png", 480),
    "parts-box": ("devices-and-tools/png/misc/parts-box.png", 480),
    "tablet-videocall": ("devices-and-tools/png/tablets/tablet-01-folio-videocall.png", 480),
}


def prepare(src, out, max_px):
    im = Image.open(src).convert("RGBA")
    box = im.getbbox()
    if box:
        im = im.crop(box)
    im.thumbnail((max_px, max_px), Image.LANCZOS)
    im.save(out, optimize=True)
    return im.size


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", nargs="?")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--max", type=int, default=640)
    ap.add_argument("--curated", metavar="OUT_DIR")
    a = ap.parse_args()
    if a.curated:
        os.makedirs(a.curated, exist_ok=True)
        for name, (rel, mx) in CURATED.items():
            size = prepare(os.path.join(FULL, rel), os.path.join(a.curated, name + ".png"), mx)
            print(f"{name}.png {size[0]}x{size[1]}")
        return
    if not (a.src and a.out):
        ap.error("give SRC and OUT, or --curated OUT_DIR")
    print(prepare(a.src, a.out, a.max))


if __name__ == "__main__":
    sys.exit(main())
