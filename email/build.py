#!/usr/bin/env python3
"""Rebuild everything generated in email/: starter templates, the directions gallery, and the Fall 2026 NU series.

Usage:
  python3 email/build.py                      # public build (sender placeholders), writes into this repo
  python3 email/build.py --sender-name "Name" --sender-email name@binaryheart.org --series-out DIR
                                              # also write a ready-to-send series (real sender) to DIR

No dependencies beyond the Python standard library.
"""
import argparse, base64, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "themes"))
from bh_email import render, THEMES, EMAILS, HEADERS, IMG_BASE  # noqa: E402
from bh_email.series import fall_2026_nu  # noqa: E402

SWATCHES = {
    "kickoff_poster": ["#F6F4EF", "#2F4A70", "#FF0040"],
    "plain_letter": ["#FFFFFF", "#2F4A70", "#FF0040"],
    "navy_masthead": ["#2F4A70", "#F4F6FA", "#FF0040"],
    "terminal_session": ["#1F3050", "#FFFFFF", "#FF8FA8"],
    "admit_one": ["#4E2A84", "#F3F1F7", "#2F4A70"],
    "workbench": ["#FDF6EA", "#26303F", "#FF0040"],
}


def build_templates():
    for key, name, _ in THEMES:
        d = os.path.join(HERE, "templates", key.replace("_", "-"))
        os.makedirs(d, exist_ok=True)
        for email, _ in EMAILS:
            with open(os.path.join(d, f"{email}.html"), "w") as fh:
                fh.write(render(key, email, "lockup", True))


def build_gallery(sender=None, out=None):
    token_base = "__IMG__"
    emails = {}
    for key, _, _ in THEMES:
        emails[key] = {e: {h: {s: render(key, e, h, s == "stats", img_base=token_base, sender=sender)
                               for s in ("stats", "nostats")} for h, _ in HEADERS} for e, _ in EMAILS}
    # Gallery JS swaps {{IMG:name}} for data URIs, so convert our resolved paths back to tokens.
    for key in emails:
        for e in emails[key]:
            for h in emails[key][e]:
                for s in emails[key][e][h]:
                    html = emails[key][e][h][s]
                    import re
                    emails[key][e][h][s] = re.sub(r"__IMG__/([a-z0-9-]+)\.png", r"{{IMG:\1}}", html)
    imgs = {}
    assets = os.path.join(HERE, "assets")
    for f in sorted(os.listdir(assets)):
        if f.endswith(".png"):
            imgs[f[:-4]] = "data:image/png;base64," + base64.b64encode(open(os.path.join(assets, f), "rb").read()).decode()
    payload = {"emails": emails, "images": imgs,
               "directions": [{"key": k, "name": n, "blurb": b} for k, n, b in THEMES]}
    tpl = open(os.path.join(HERE, "gallery", "_template.html")).read()
    html = tpl.replace("__DATA__", json.dumps(payload).replace("</", "<\\/")).replace("__SW__", json.dumps(SWATCHES))
    html = html.replace("let st = {dir:'poster'", "let st = {dir:'workbench'")
    out = out or os.path.join(HERE, "gallery", "index.html")
    with open(out, "w") as fh:
        fh.write(html)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sender-name")
    ap.add_argument("--sender-email")
    ap.add_argument("--series-out", help="also write a ready-to-send series with the real sender here")
    ap.add_argument("--gallery-out", help="also write a gallery with the real sender here")
    a = ap.parse_args()
    build_templates()
    build_gallery()
    fall_2026_nu.write_all(os.path.join(HERE, "series", "2026-fall-nu"))
    sender = {"name": a.sender_name, "email": a.sender_email} if a.sender_name else None
    if a.series_out:
        fall_2026_nu.write_all(a.series_out, sender=sender)
    if a.gallery_out:
        build_gallery(sender=sender, out=a.gallery_out)
    print("built templates, gallery, series")


if __name__ == "__main__":
    main()
