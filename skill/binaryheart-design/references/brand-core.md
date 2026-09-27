# Brand Core

This file covers the logo, wordmark, chapters, voice, and facts that apply to every BinaryHeart surface.

## Contents

- Logo and wordmark
- Lockups
- Color roles
- Chapters and accent colors
- Voice and copy
- Facts, handles, and links
- Known inconsistencies to fix, not copy

## Logo and wordmark

- The heart logo is a heart split vertically, with a red left half carrying a white "0" and a navy right half carrying a white "1".
    - Use `assets/logo/heart-logo.png` and never recolor, mirror, outline, or add effects to it.
    - The official source is `https://www.binaryheart.org/assets/images/chapters/national/icon.svg` (`assets/logo/heart-logo.svg`).
    - For email and other places that can't use SVG, use the PNG render.
    - The Fall 2026 posters use a mirrored version (`deprecated/heart-logo-poster-variant.png`), so swap it for the official one on the next print run.
        - Until a corrected version is hosted, flag it whenever you reference that URL in an email.
- The wordmark is "BinaryHeart": one word, "Binary" in navy `#2F4A70` and "Heart" in red `#FF0040`, always bold (700-800).
    - In HTML, write it as `<strong style="font-weight: 800;"><span style="color: #2F4A70;">Binary</span><span style="color: #FF0040;">Heart</span></strong>`.
    - On a navy background, place the wordmark on a white chip or card rather than recoloring "Binary" white.
    - In plain text with no color, "BinaryHeart" needs no bolding.
- Keep clear space around the logo of at least half the heart's width.
    - The minimum size is 24px on screen or 0.3 in in print.

## Lockups

Use one of these three and don't improvise new ones.

1. **Chapter lockup** (preferred for chapter materials, and used on join.binaryheart.org):
    - The heart logo sits on the left, with the bold wordmark to its right.
    - Under the wordmark goes a smaller line with "*School* Chapter", the school name in the chapter accent and "Chapter" in ink.
    - It can pair with a thin top stripe split red and navy.
2. **Classic stacked** (centered): the heart logo, then the wordmark below it, then "at *School Name*" in the chapter accent.
3. **Full logo lockup** (print, labels, formal): the heart logo plus the wordmark, with "Spreading Digital Access" in small, tracked ink type underneath.
    - The shipping label shows this lockup.

## Color roles

- Navy `#2F4A70` handles structure: headings, date panels, footers, and primary buttons on light backgrounds.
- Red `#FF0040` handles action and emphasis: the single main CTA, small square bullets, and 3px accent bars before eyebrow labels.
    - For red text under 18px, use deep red `#C8003A` so it passes contrast.
- The chapter accent covers the school name, a chapter-only highlight, and an occasional button (for example, a Cats on Campus RSVP).
    - Use at most one accent-colored element per screen, beyond the school name itself.
- For neutrals:
    - Ink `#1B2233` is for body text, and muted `#4A5468` is for secondary text.
    - Line `#D9DEE7` is for rules and borders.
    - Cream `#F6F4EF` is the print background, and white is the email and web card color.
- Pink `#FF8FA8` and navy divider `#4A6389` appear only inside navy panels.
- Don't introduce greens, oranges, or extra blues.
    - The only exceptions are the colors built into the illustrations and third-party icons.

## Chapters and accent colors

Navy and red are constant, and each chapter adds exactly one accent.
Only Northwestern's is confirmed; confirm the others with the chapter lead before using them in anything printed or sent.

| Chapter | Site path | Accent | Status |
|---|---|---|---|
| Northwestern University | `/nu` | Purple `#4E2A84` | Confirmed |
| Indiana University | `/iu` | IU Crimson `#990000` | Verify; it sits close to brand red, so keep it away from "Heart" |
| Purdue University | `/purdue` | Boilermaker Gold `#CFB991`, with Aged `#8E6F3E` for text | Verify; gold is too light for text on white |
| Rose-Hulman Institute of Technology | `/rose-hulman` | TBD | Ask the chapter |
| New Trier (founding chapter, 2016) | `/nt` | TBD | Ask the chapter |
| Walter Payton College Prep | `/wp` | TBD | Ask the chapter |
| IMSA | not on the site yet | TBD | Ask the chapter |

When a chapter's accent is TBD, use navy and red only, and tell the user an accent can be added later.

## Voice and copy

- Write plainly and warmly, the way a student leader talks to a classmate.
    - Use short sentences and active voice.
- Lead with what the reader does next: the date, time, place, and one action.
- Recruitment copy repeats three truths:
    - It's open to every major and year.
    - No experience is needed, because we teach everything.
    - Attendance is drop-in and flexible.
- Keep the food secondary.
    - Mention snacks once, as the last perk in a list, never in the subject line or hero.
- Use the terms "refurbish", "donated computers", "digital access", and "hands-on repair."
    - Avoid "e-waste" as a headline word.
- The Fall 2026 NU pipeline has no application: everyone joins the email list, and leadership comes from active members or a short interest form.
    - Check whether a chapter uses the same pipeline before writing "no application."
- Dates look like "Thursday, October 8" and times like "11 AM – 6 PM" (with an en dash).
    - Never write "Oct 8th" in headlines, though "October 8th" is fine in running prose.
- Sign emails from the chapter president with their title, "BinaryHeart President (*School* Chapter)".
    - Ask who the sender is and never assume.

## Facts, handles, and links

- BinaryHeart Inc. is a student-run 501(c)(3), EIN 93-2078509, founded at New Trier High School in 2016.
- The national site is `https://www.binaryheart.org`, with chapter pages at `/<chapter>/join` (e.g. `/nu/join`).
    - Chapter mailing-list sign-up lives at `https://join.binaryheart.org/<chapter>`.
- National Instagram is `@binaryheart_`, and NU's is `@binaryheartatnu` (other chapters: ask).
- GitHub is `https://github.com/BinaryHeartUS`, and `BinaryHeartUS/design` (public) holds this design system, the themes, and the hosted email images.
    - Never commit personal phone numbers, personal emails, or home addresses there.
- The NU chapter email is `nu@binaryheart.org`, and its space is 1910 Orrington Ave, Evanston (across from Foster-Walker).
- The NU Discord invite is `https://discord.gg/QutKWgv7U`.
    - NU moved from Slack to Discord and dropped Notion for now, so don't reference Slack or Notion.
- Stats (devices, people helped, volunteers, chapters, hours) must always be confirmed with the user before use.

## Known inconsistencies to fix, not copy

- The join page (`binaryheart.org/nu/join`) and join.binaryheart.org color "Binary" red and "Heart" navy.
    - This is backwards, and the colored wordmark there is sometimes not bold.
- The shipping label sets the wordmark in regular weight, so it should be bold.
- The Fall 2026 posters and flyers use the mirrored heart (navy "0" left) instead of the official logo.
- Site prose sometimes writes "Binary Heart" as two words, but the brand name is one word.
