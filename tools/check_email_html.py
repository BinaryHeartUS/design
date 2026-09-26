#!/usr/bin/env python3
"""Lint BinaryHeart email HTML for Gmail safety and brand rules.

Usage: python3 check_email_html.py FILE.html [FILE2.html ...]
Exit code 1 if any ERROR is found. No dependencies.
"""
import re, sys
from html.parser import HTMLParser

NAVY, RED = "#2f4a70", "#ff0040"
VOID = {"br", "img", "hr", "link", "meta", "input", "source", "wbr", "col", "area", "base"}


class Balance(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.errors = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errors.append(f"line {self.getpos()[0]}: unexpected </{tag}>")


def check(path):
    s = open(path, encoding="utf-8").read()
    low = s.lower()
    out = []

    def err(m): out.append(("ERROR", m))
    def warn(m): out.append(("WARN", m))

    b = Balance(); b.feed(s)
    for e in b.errors[:5]:
        err("unbalanced tags: " + e)
    if b.stack:
        err("unclosed tags: " + ", ".join(f"<{t}> (line {l})" for t, l in b.stack[-5:]))

    if "<style" in low:
        warn("<style> block found: Gmail drops it when HTML is pasted/injected; move styles inline")
    if re.search(r"display\s*:\s*(flex|grid|inline-flex)", low):
        err("display:flex/grid found: Gmail ignores it; use tables")
    if re.search(r"<img[^>]+src=\"data:", low):
        err("data: URI image: Gmail blocks embedded images; host the file and use an https URL")
    for src in re.findall(r"<img[^>]+src=\"([^\"]+)\"", s, flags=re.I):
        if not src.startswith(("http://", "https://", "{{", "cid:")):
            err(f"image src is not a public URL: {src}")
    if "<svg" in low:
        err("inline <svg>: Gmail strips it; use a PNG")
    if re.search(r"box-shadow|position\s*:\s*(absolute|fixed)|linear-gradient", low):
        warn("box-shadow / positioning / gradients are unreliable in Gmail")

    non_ascii = sorted({c for c in s if ord(c) > 127})
    if non_ascii and "charset" not in low:
        warn("non-ASCII characters without a charset (may show as garbage): " + " ".join(non_ascii[:12]) +
             "  -> use HTML entities (&ndash; &middot; &rsquo; ...)")

    kb = len(s.encode()) / 1024
    if kb > 100:
        warn(f"{kb:.0f} KB: Gmail clips messages over ~102 KB")

    # Brand: Binary = navy, Heart = red, always bold
    for m in re.finditer(r"<span[^>]*color:\s*(#[0-9a-fA-F]{6})[^>]*>\s*(?:<strong>)?\s*(Binary|Heart)\b", s):
        color, word = m.group(1).lower(), m.group(2)
        if word == "Binary" and color != NAVY:
            err(f"'Binary' colored {color}; it must be navy {NAVY.upper()} (Binary Blue)")
        if word == "Heart" and color != RED:
            err(f"'Heart' colored {color}; it must be red {RED.upper()} (Red Heart)")
        if word == "Binary":
            before = s[max(0, m.start() - 200):m.start()].lower()
            inside = s[m.start():m.start() + 200].lower()
            bold = ("<strong" in before[-120:] or "<b>" in before[-60:] or "<b " in before[-60:]
                    or re.search(r"font-weight:\s*(700|800|900|bold)", before[-160:] + inside[:120])
                    or "<strong>binary" in inside or re.search(r"<h[1-3][^>]*>[^<]*$", before))
            if not bold:
                err(f"colored wordmark near char {m.start()} is not bold")

    ph = sorted(set(re.findall(r"\[[A-Z0-9_]{4,}\]", s)))
    if ph:
        warn("placeholders still present: " + ", ".join(ph))
    return out


def main(paths):
    bad = False
    for p in paths:
        res = check(p)
        print(f"== {p}: " + ("OK" if not res else f"{sum(1 for l, _ in res if l == 'ERROR')} error(s), {sum(1 for l, _ in res if l == 'WARN')} warning(s)"))
        for level, msg in res:
            print(f"  {level}: {msg}")
            bad |= level == "ERROR"
    return 1 if bad else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1:]))
