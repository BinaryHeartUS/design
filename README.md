# BinaryHeart Design

This repo is the design system for BinaryHeart, the student-run 501(c)(3) that refurbishes donated computers.
It holds the brand rules, email themes, print templates, the illustration library, and the Claude skill that ties them together.

## Rules that never change

- **Binary Blue, Red Heart:** "Binary" is navy `#2F4A70` and "Heart" is red `#FF0040`, always in that order.
    - The heart logo is the official `binaryheart.org/assets/images/chapters/national/icon.svg`: red "0" half on the left, navy "1" half on the right.
    - Never mirror or recolor it.
- **The two-color wordmark is always bold.**
    - This has no exceptions, including lockups, footers, and signatures.
- **Navy is structure, red is action, and each chapter adds one accent color.**
    - Northwestern's accent is purple `#4E2A84`.
- **Never invent stats.**
    - Confirm current numbers before every use.
- **Never commit personal info here.**
    - This repo is public, so use `[PLACEHOLDERS]` for names, personal emails, phone numbers, and home addresses.

The full rules live in [`skill/binaryheart-design/references/brand-core.md`](skill/binaryheart-design/references/brand-core.md).

## What's where

| Folder | What it holds |
|---|---|
| [`brand/`](brand/) | The heart logo (canonical, email-size, and the deprecated poster variant), fonts (Archivo, Fira Code, Lato, all OFL), and app icons |
| [`email/themes/`](email/themes/) | `bh_email`, the Python theme library: six Gmail-safe directions, shared components, and series |
| [`email/templates/`](email/templates/) | Ready-to-edit HTML per theme (recruitment and announcement), for people who don't code |
| [`email/gallery/`](email/gallery/) | `index.html`, an interactive comparison of all six directions × 2 emails × 2 headers × stats on or off |
| [`email/series/2026-fall-nu/`](email/series/2026-fall-nu/) | The Fall 2026 Northwestern kickoff series in Workbench (callout and no-callout versions), plus subject lines |
| [`email/archive/`](email/archive/) | Earlier NU emails from Fall 2025 and Winter 2026, with personal details redacted |
| [`email/assets/`](email/assets/) | The images emails load from this repo (public raw URLs) |
| [`print/`](print/) | Posters, flyers (HTML source plus PDF), and the 4×6 shipping label template |
| [`illustrations/`](illustrations/) | The full isometric library (`source/`: SVG, PNG, previews) and 22 trimmed PNGs (`curated/`) |
| [`skill/`](skill/) | The `binaryheart-design` Claude skill source, plus `build.py` to package and install it |
| [`tools/`](tools/) | `check_email_html.py` (Gmail and brand linter) and `prepare_illustration.py` (trim and resize) |
| [`docs/`](docs/) | Working docs and prompts, such as the availability-form UX brief |

## Email themes

| Theme | When to use it |
|---|---|
| 01 Kickoff Poster | Default for most emails, and pairs with the printed poster |
| 03 Navy Masthead | Default for most emails, such as announcements and newsletters |
| 06 Workbench | Big events, like a chapter's first meeting or kickoff series |
| 05 Admit One | Single-event invites and reminders |
| 04 Terminal Session | Tech and software recruiting |
| 02 Plain Letter | Personal notes and follow-ups |

The preference order is 06 > 03 > 01 > 05 > 04 > 02.
Open [`email/gallery/index.html`](email/gallery/index.html) in a browser to compare them.

## Common tasks

- **Rebuild the emails, templates, and gallery** with `python3 email/build.py`.
    - To produce ready-to-send copies with a real sender, add `--sender-name "Name" --sender-email name@binaryheart.org --series-out ~/Desktop/out`.
    - Those copies stay out of the repo.
- **Render one email in any theme:**
  ```python
  import sys; sys.path.insert(0, "email/themes")
  from bh_email import render
  html = render("navy_masthead", "announcement", hdr="lockup", stats=False,
                sender={"name": "Name", "email": "name@binaryheart.org"})
  ```
- **Check an email before sending** with `python3 tools/check_email_html.py path/to/email.html`.
- **Add an email image** by putting the PNG in `email/assets/` and pushing.
    - Reference it as `https://raw.githubusercontent.com/BinaryHeartUS/design/main/email/assets/<name>.png`.
- **Package the Claude skill** with `python3 skill/build.py`, which writes `dist/binaryheart-design-lite.zip` (for claude.ai) and `-full.zip`.
    - Add `--install` to install it for Claude Code on this machine.
- **Print a poster or label** by opening the HTML in Chrome and choosing Print, then Save as PDF, with margins set to None and "Background graphics" turned on.

## Sending emails

- Emails are sent with a Gmail mail-merge add-on, with the HTML injected by a Chrome HTML-insert extension.
- Everything in `email/` uses tables and inline styles only, so it survives Gmail.
- Gmail shows Helvetica or Arial in place of Lexend.

## Licenses

- The fonts are under the SIL Open Font License (see `brand/fonts/OFL-*.txt`).
- The logo, illustrations, and all other content are © BinaryHeart Inc. (EIN 93-2078509), all rights reserved.
