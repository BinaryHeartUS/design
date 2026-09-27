#!/usr/bin/env python3
"""Assemble the binaryheart-design skill from this repo and package it.

  python3 skill/build.py            # writes dist/binaryheart-design-lite.zip and dist/binaryheart-design-full.zip
  python3 skill/build.py --install  # also installs the full build to ~/.claude/skills/binaryheart-design

The lite build (~4 MB) fits claude.ai skill uploads; the full build adds the complete illustration library.
Only SKILL.md and references/ live in skill/binaryheart-design; everything else is copied from the repo.
"""
import argparse, os, shutil, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "skill", "binaryheart-design")
DIST = os.path.join(ROOT, "dist")
IGNORE = shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc", "_template.html")

COPIES = [  # (repo path, path inside the skill)
    ("brand/logo/heart-logo.svg", "assets/logo/heart-logo.svg"),
    ("brand/logo/heart-logo.png", "assets/logo/heart-logo.png"),
    ("brand/logo/heart-logo-email.png", "assets/logo/heart-logo-email.png"),
    ("brand/logo/deprecated", "assets/logo/deprecated"),
    ("brand/app-icons", "assets/app-icons"),
    ("brand/fonts", "assets/fonts"),
    ("illustrations/curated", "assets/illustrations/curated"),
    ("tools/check_email_html.py", "scripts/check_email_html.py"),
    ("tools/prepare_illustration.py", "scripts/prepare_illustration.py"),
    ("email/themes/bh_email", "examples/bh_email"),
    ("email/gallery/index.html", "examples/email-directions-gallery.html"),
    ("print/posters/2026-fall-nu-first-meeting.html", "examples/poster-first-meeting-nu.html"),
    ("print/shipping-label/shipping-label.html", "examples/shipping-label.html"),
]
FULL_ONLY = [("illustrations/source", "assets/illustrations/full")]


def assemble(dest, full):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(SRC, dest, ignore=IGNORE)
    for src, dst in COPIES + (FULL_ONLY if full else []):
        s, d = os.path.join(ROOT, src), os.path.join(dest, dst)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        if os.path.isdir(s):
            shutil.copytree(s, d, ignore=IGNORE)
        else:
            shutil.copy2(s, d)


def zip_dir(folder, out):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(folder):
            for f in files:
                p = os.path.join(root, f)
                z.write(p, os.path.relpath(p, os.path.dirname(folder)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--install", action="store_true")
    a = ap.parse_args()
    os.makedirs(DIST, exist_ok=True)
    for kind in ("lite", "full"):
        stage = os.path.join(DIST, kind, "binaryheart-design")
        assemble(stage, full=(kind == "full"))
        out = os.path.join(DIST, f"binaryheart-design-{kind}.zip")
        zip_dir(stage, out)
        print(f"{out}  {os.path.getsize(out) / 1e6:.1f} MB")
    if a.install:
        target = os.path.expanduser("~/.claude/skills/binaryheart-design")
        if os.path.exists(target):
            shutil.rmtree(target)
        shutil.copytree(os.path.join(DIST, "full", "binaryheart-design"), target)
        print("installed", target)


if __name__ == "__main__":
    main()
