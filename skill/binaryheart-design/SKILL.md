---
name: binaryheart-design
description: BinaryHeart's brand and design system (the student-run 501(c)(3) that refurbishes donated computers, with chapters at Northwestern, Indiana, Purdue, Rose-Hulman, New Trier, Walter Payton, and IMSA). Use this skill for ANY visual or written deliverable carrying the BinaryHeart name or logo, even when the user doesn't say "brand" or "design" - recruitment and member emails (Gmail mail-merge HTML), posters and flyers, shipping labels for moving devices between chapters, website pages on binaryheart.org or join.binaryheart.org, callout slide decks, Instagram posts and stories, Cats on Campus event descriptions, certificates, and signage. Also use it when reviewing or fixing existing BinaryHeart materials for off-brand colors, an unbolded wordmark, or Gmail rendering problems.
---

# BinaryHeart Design

BinaryHeart materials should look like they came from one organization, whether a chapter lead makes them in an afternoon or the national team makes them for a donor.
This skill gives you the rules that never change, then points you to one reference file per surface.

## Rules that never change

These come straight from the founders' corrections, so treat them as fixed.

1. **Binary Blue, Red Heart.**
    - "Binary" is navy `#2F4A70` and "Heart" is red `#FF0040`, always in that order.
    - The heart logo is a separate asset with its own layout: the red half with the "0" on the left and the navy half with the "1" on the right.
    - Always use the official file and never mirror it to "match" the wordmark.
    - Never swap them, even to "balance" a layout (the current site join page and the old site icon get this wrong, and both are being fixed).
2. **The two-color wordmark is always bold (700-800), with no exceptions.**
    - This includes logo lockups, footers, signatures, and inline mentions in body copy.
    - Write it as one word, "BinaryHeart", and use "BinaryHeart Inc." only for legal lines.
3. **Navy is structure, red is action, and the chapter accent is identity.**
    - Navy carries headings, panels, and footers.
    - Red is reserved for the single most important action or accent on a surface.
    - Each chapter adds one school color (Northwestern purple `#4E2A84`), used for the school name and a few highlights only.
    - Other brand colors (Discord blurple, Instagram gradient) stay inside their own icons and buttons.
4. **Never invent numbers.**
    - Impact stats differ between sources (the poster says 400+ devices and 8 chapters, while binaryheart.org/about says $89.1K+ donated and 6 chapters).
    - Before printing any stat, ask the user for current figures or leave a clearly marked placeholder.
5. **Stay consistent inside one piece.**
    - Pick one card style, one button style per role, and one section color logic.
    - Don't rotate through tints section by section, and never put a navy button on a green box.

## Brand tokens (summary)

| Token | Hex | Use |
|---|---|---|
| Navy | `#2F4A70` | "Binary", headings, panels, footers, primary buttons on light backgrounds |
| Red | `#FF0040` | "Heart", the main CTA, small square bullets, accent bars |
| Deep red | `#C8003A` | Red *text* at small sizes, since `#FF0040` is too light for AA contrast on white |
| Ink | `#1B2233` | Body text |
| Muted | `#4A5468` | Secondary text |
| Line | `#D9DEE7` | Rules and card borders |
| Cream | `#F6F4EF` | Print and poster background |
| Illustration cream | `#FDF6EA` | The background the isometric art was drawn on |
| Pink on navy | `#FF8FA8` | Small labels on navy panels |
| Navy divider | `#4A6389` | Dividers inside navy panels |
| NU purple | `#4E2A84` | Northwestern chapter accent (see chapter table in brand-core.md) |

Taglines:
- **"Spreading Digital Access"** sits under the wordmark in the full logo lockup.
- **"Upcycle · Upskill · Uplift"** goes in footer bands and sign-offs.

Legal footer line: "BinaryHeart Inc. is a student-run 501(c)(3) nonprofit spreading digital access. EIN 93-2078509."

## Pick the surface, then read its reference

| Making... | Read | Fonts |
|---|---|---|
| Email (recruitment, announcements, onboarding, event notifications) | `references/email.md` | Lexend, falling back to Helvetica/Arial |
| Poster, flyer, signage, certificate | `references/print.md` | Archivo + Fira Code (embedded) |
| Shipping label | `references/print.md` | Lato (embedded), matching the Figma original |
| Page on binaryheart.org or join.binaryheart.org | `references/web.md` | System stack (the site's), or Lexend |
| Slide deck, Instagram post or story | `references/slides-social.md` | Archivo + Fira Code |

Always also read `references/brand-core.md` the first time in a session: it covers the logo, chapters, voice, and facts.
Read `references/illustrations.md` whenever a piece needs imagery.

## Assets in this skill

- `assets/logo/heart-logo.svg` is the official logo (the same file as `binaryheart.org/assets/images/chapters/national/icon.svg`), and `heart-logo.png` is a 996px transparent render of it.
    - `heart-logo-email.png` is a 176px version for email, hosted at `https://raw.githubusercontent.com/BinaryHeartUS/design/main/email/assets/logo.png`.
    - `deprecated/heart-logo-poster-variant.png` is the mirrored version (navy "0" left) on the Fall 2026 posters, kept only so you can recognize it and replace it.
- `assets/app-icons/discord.png` and `instagram.png` are app-style rounded-square icons for "connect with us" rows.
- `assets/fonts/` holds Archivo 400-800, Fira Code 400-700, and Lato 300/400/700/900 as woff2 (SIL Open Font License), for embedding in print HTML so it works offline.
- `assets/illustrations/curated/` holds 22 trimmed PNGs, ready for email and web (see illustrations.md).
- `assets/illustrations/full/` holds the complete isometric library (SVG + 2000px PNG + preview sheets).
    - It may be absent in the lightweight upload build, in which case use `curated/`.
- `examples/shipping-label.html` is the 4×6 in shipping label template, with placeholders.
- `examples/poster-first-meeting-nu.html` is the Fall 2026 NU first-meeting poster, the best single example of the print style.
- `examples/bh_email/` is the Python email theme library: shared components, one module per direction in `themes/`, and the Fall 2026 NU Workbench series in `series/`.
- `examples/email-directions-gallery.html` is the interactive gallery with all six directions × 2 emails × 2 headers × stats on or off, so open it to compare themes.
- `scripts/check_email_html.py` lints email HTML for Gmail breakage and brand-rule violations, so run it on every email you produce.
- `scripts/prepare_illustration.py` trims and resizes illustrations (needs Pillow).

## Source of truth

- The skill is built from the public repo `https://github.com/BinaryHeartUS/design` (`skill/build.py`).
    - Edit the repo, then rebuild, instead of editing an installed copy.
- Email images are hosted from that repo under `email/assets/`, so add new images there and push before sending.

## Workflow

1. Identify the surface and the chapter (for the accent color, social handle, and sender).
2. Read brand-core.md plus the surface reference.
3. Gather real details from the user or their existing materials: dates, times, rooms, links, and sender name.
    - Use `[ALL_CAPS_PLACEHOLDER]` for anything unknown, and list the placeholders when you hand the work over.
4. Build it using the tokens above and the surface's components.
5. Check it:
    - For email, run `scripts/check_email_html.py`.
    - For everything, confirm the wordmark is bold and navy-then-red, and that no stats were invented.
6. Hand it over with what still needs the user: placeholders, image hosting, and numbers to confirm.
