# Print: posters, flyers, shipping labels, signage

Print pieces are single self-contained HTML files, with fonts and images embedded as base64, exported to PDF from Chrome.
That way anyone can open, edit, and reprint them without installing anything.

## Contents

- Setup
- Poster and flyer anatomy
- Shipping label anatomy
- Signage and small pieces
- Export

## Setup

- Page sizes, at 96 px per inch:
    - Letter is `816px × 1056px`.
    - Tabloid is `1056px × 1632px`.
    - A 4×6 in label is `384px × 576px`, which you can design at 2× (768 × 1152) and scale.
- Declare `@page { size: 816px 1056px; margin: 0 }` with `.page { width: 816px; height: 1056px; overflow: hidden }`.
    - On screen, show the page on a gray-blue `#9AA6B8` backdrop with a soft shadow, so it reads as paper.
- Fonts: embed `assets/fonts/Archivo-*.woff2` (400-800) and `FiraCode-*.woff2` (400-700) through `@font-face` with base64 `src`.
    - Archivo is for headlines and body text.
    - Fira Code is for eyebrows, labels, numbers, URLs, and the "01" feel.
- The background is cream `#F6F4EF`, with white `#FFFFFF` cards at radius 16px and navy `#2F4A70` panels at radius 20-24px.
- Illustrations: embed the PNGs from `assets/illustrations/` as base64.
    - Place them on a navy tile or directly on cream, and never on a busy background.
- Put a comment block at the top of the file explaining what it is, how to edit it, and how to export it (see the example poster).

## Poster and flyer anatomy

This follows `examples/poster-first-meeting-nu.html`.

1. **Top row:** the logo (52px) plus the bold Fira Code wordmark on the left, and a "501(c)(3) NONPROFIT" pill on the right.
    - The pill is a 1.5px navy outline in Fira Code 12px.
2. **Hero:**
    - It opens with an eyebrow: a 3px red bar followed by Fira Code 13px tracked caps (e.g. "NOW RECRUITING · NORTHWESTERN CHAPTER", with the school in its accent).
    - Below that is a two-line Archivo 800 headline at about 62px, with line one in navy and line two in red.
    - A 19px lede follows, with an illustration on a navy tile to the right.
3. **Event panel (navy):**
    - "FALL 2026 KICKOFF" runs across the top with "No experience needed." on the right.
    - A big date column follows: the weekday in pink `#FF8FA8`, then about 92px "Oct 8", the time, and "Drop in anytime".
    - A 2px `#4A6389` divider separates the location and the red square bullets.
    - A white QR tile carries the caption "SCAN TO JOIN OUR EMAIL LIST" in deep red Fira Code.
4. **What we do:** three white cards (Hardware / Software / Operations), each an illustration beside a title and a one-line description.
5. **Stats strip:** four columns with 2px left rules, each a Fira Code number over a label.
    - Only use confirmed numbers.
6. **Questions bar:** a white card with "QUESTIONS?" in deep red Fira Code, and the email and Instagram on the right.
7. **Footer band:** navy, with the legal line and EIN on the left, and the chapter URL plus "Upcycle, Upskill, Uplift" on the right.

QR codes: leave a dashed 150px placeholder box when no link is given, and say so.
When the user gives a link, generate the QR as a PNG and embed it.

## Shipping label anatomy

This is for moving devices between chapters (Uber Courier and similar).
Start from `examples/shipping-label.html`, which is rebuilt from the Figma original (file "BinaryHeart - to Mo Walter Payton - Shipping Label", frame 2:81).
Change only the text, and keep the layout exactly as it is.

- **Canvas and type:** the canvas is 600×900 px (4×6 in, zoomed to 0.64 for print), in Lato.
- **Frame:** a 3px navy border around a 3px white inset.
- **Header** (97px, with a 3px navy bottom border):
    - A 58px heart logo sits on the left.
    - Next to it is the bold wordmark (32px), with "Spreading Digital Access" under it (10px bold, 1px tracking).
    - `binaryheart.org` sits on the right (11px bold navy).
- **A 4px red bar** runs under the header.
- **Sender** (232px, `#F5F6F8`, with a 20px navy bottom border):
    - A "SENDER" chip in navy (16px bold, 3px tracking).
    - The chapter line in 26px bold navy, set as plain text rather than the two-color wordmark.
    - The contact name in 24px `#555`, and the address in 22px `#777` at 30.8px line height.
- **Deliver to** (fills the remaining space, with content starting 87px down):
    - A red "DELIVER TO" chip (18px bold, 4px tracking).
    - "BinaryHeart / *Chapter* Chapter" in 42px black-weight (900) navy.
    - The contact name in 38px `#333`, and the address in 34px `#444`.
- **Handle with care:** a 45.5px `#F5F6F8` band with a 2px navy top border, holding "HANDLE WITH CARE" in 13px bold navy with 2px tracking.
- **Footer:** a 39.5px navy band holding "UPCYCLE · UPSKILL · UPLIFT" in 10px white with 2px tracking.

Every text field is click-to-edit in the browser.
Ask for addresses and never guess them, and never commit real names or addresses to the public repo.

## Signage and small pieces

- **Door and table signs:** use the cream background, a navy panel with one instruction, and the logo lockup at the top.
- **Certificates:** use the full logo lockup, navy and red rules, Archivo, and the legal line at the bottom.
- Keep one idea per sign.

## Export

- In Chrome, choose Print, then Save as PDF, with margins set to None and "Background graphics" turned on.
- Check the PDF for font fallback (the letterforms should be Archivo, not Times) and that no content is clipped at the page edge.
