# Email

BinaryHeart emails go out through Gmail.
They're made with a Gmail mail-merge add-on (Open Source Mail Merge, in the BinaryHeart GitHub orgs), and the HTML is injected into the compose window by a Chrome HTML-insert extension.
Gmail rewrites a lot of CSS on the way in, so every email is built to survive that.

## Contents

- Gmail survival rules
- Skeleton
- Components
- The six approved directions
- Content patterns
- Images and hosting
- Checklist

## Gmail survival rules

- Build layout with `<table role="presentation">` and put every style inline on the element.
    - `<style>` blocks, classes, and media queries don't survive injection.
- Never use `display:flex` or `grid`, `position`, `box-shadow`, gradients, SVG, or background images.
    - `border-radius`, `border`, `background-color`, `padding`, and `display:inline-block` on links are all safe.
- Columns are table cells with percentage widths.
    - Keep to two columns, and check that each still reads at about 340px wide, since there's no stacking on phones.
- Fonts: request Lexend with `font-family: Lexend, 'Helvetica Neue', Helvetica, Arial, sans-serif`.
    - Gmail shows Helvetica or Arial, while Apple Mail and iOS may show Lexend.
    - Fira Code is only used for small labels in some directions, falling back to `Menlo, Consolas, 'Courier New', monospace`.
- Encode every non-ASCII character as an HTML entity (`&ndash;` `&middot;` `&rsquo;` `&ldquo;`).
    - There's no charset declaration, so raw characters turn into garbage like "â€“".
- Keep the whole message under about 100 KB, because Gmail clips longer messages behind "View entire message".
- Images must use public `https://` URLs, since data URIs and local paths are blocked.
- Merge tags use `{{First Name}}`, and other columns work the same way if the sheet has them.
- Add hidden preview text as the first element, so the inbox snippet isn't "BinaryHeart at Northwestern University...":
  ```html
  <div style="display: none; font-size: 1px; line-height: 1px; max-height: 0; max-width: 0; opacity: 0; overflow: hidden; mso-hide: all;">Drop in anytime Thursday 11 AM&ndash;6 PM at 1910 Orrington. No experience needed.</div>
  ```

## Skeleton

```html
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600;700;800&family=Fira+Code:wght@500;600;700&display=swap" rel="stylesheet">
<!-- preview text div -->
<div style="margin: 0; padding: 0; background-color: PAGE_BG;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color: PAGE_BG;">
<tr><td align="center" style="padding: 24px 12px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width: 640px; width: 100%; font-family: Lexend, 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #1B2233;">
  <!-- one <tr><td> per block -->
</table>
</td></tr></table>
</div>
```

## Components

`examples/bh_email/components.py` has working, tested versions of every component below.
Copy them from there instead of rewriting them.

- **Header, chapter lockup:** the logo at 40-44px in one cell, with the bold wordmark (20-22px) and "*School* Chapter" (12-13px) in the next.
    - It can sit under a 4-5px stripe made of two cells, red then navy.
- **Header, classic:** a centered logo at 56-64px, then the wordmark at 28-32px, then "at *School*" in the accent at 16-17px.
- **Date panel:** a navy block with the weekday in pink tracked caps, a big date (40-60px, weight 800), and the time.
    - A second column holds the location and square red bullets.
- **Buttons:** an `<a>` with `display: inline-block`, 2px border, 8px radius, `padding: 12px 22px`, and weight 700.
    - Primary is red on navy panels and navy on light cards.
    - Secondary is white with a navy border and navy text.
    - The chapter accent is allowed for a school-platform action (e.g. "RSVP on Cats on Campus").
    - Discord buttons may use blurple `#5865F2`.
- **Connect row:** the Instagram and Discord app icons (28px, 7px radius) sit next to handle and "Join our Discord" labels.
    - Host `assets/app-icons/*.png` first.
- **What we do rows:** a 72px illustration next to a title and a one-line description, for Hardware, Software, and Operations.
- **Stats row (optional):** four cells, each with a 2px left rule, a big number, and a small label.
    - Only use numbers the user has confirmed.
- **Signature:** "Best,", then the sender's name in bold, then "BinaryHeart President (*School* Chapter)" with a bold wordmark, then their email.
- **Nonprofit footer:** a navy band with the legal line and EIN on the left, and `binaryheart.org/<chapter>` plus "Upcycle, Upskill, Uplift" on the right.

## The six approved directions

All six follow the same color logic.
Choose one per email series and keep it for the whole quarter so emails look related.

**Defaults (set by the national team, Sept 2026):**
- For most emails, use **01 Kickoff Poster** or **03 Navy Masthead**.
- For big events, like a chapter's first meeting or kickoff series, use **06 Workbench**.
    - Workbench was the favorite, and the Fall 2026 NU series uses it with the chapter lockup header and the stats row on.
- Overall preference: 06 > 03 > 01 > 05 > 04 > 02.
    - Only reach for 05, 04, or 02 when the user asks, or the content clearly fits them.
- `examples/bh_email/series/fall_2026_nu.py` is the full Fall 2026 NU series in Workbench (recruitment, post-callout, announcement, event description, day-of notification, welcome).
    - Use it as the template for a chapter's kickoff series.
- Render any direction with `from bh_email import render; render("navy_masthead", "announcement", hdr="lockup", stats=False, sender={...})`.
- Compare the directions in `examples/email-directions-gallery.html`.

| Direction | Look | Best for |
|---|---|---|
| 01 Kickoff Poster | Cream page, poster-style navy date card, Fira Code eyebrows with a red tick, white cards | First meeting and recruitment, anything paired with the printed poster |
| 02 Plain Letter | White, no boxes, hairline rules, red small-caps section labels, one navy button | Personal notes, onboarding, follow-ups, anything that should feel sent by a person |
| 03 Navy Masthead | Navy top band with the lockup on a white chip, red and navy stripe, soft gray cards | Announcements, newsletters, national-level emails |
| 04 Terminal Session | Window chrome, the event as command output on a dark navy panel, `// comment` labels, Fira Code buttons | Tech-leaning audiences, software and OpenClaw recruiting |
| 05 Admit One | The event as a ticket with a tear-off stub in the chapter accent | Single-event invites and reminders |
| 06 Workbench | Illustration-led, cream `#FDF6EA`, cards with 2px ink outlines echoing the art | Refurbishment-focused emails, donation drives, welcome emails |

Headers: each direction supports both the chapter lockup and the classic stacked header.
Stats row: optional in every direction, and only with confirmed numbers.

## Content patterns

- **Recruitment:** greeting, who we are, "no application", a returning-members line, first meeting details, optional RSVP, availability, leadership, what we do, questions and connect, signature, footer.
- **Announcement (sent 2-3 days before):** greeting, invite, details, getting there (numbered steps), weekly sessions, leadership, connect, signature, and the list-policy note.
- **Day-of notification:** details first, then getting there, then Discord setup.
- **Welcome:** connect, hours, location, Discord setup (join, set server nickname to your full name, install on phone and computer, turn on notifications), then an onboarding step.
- **Subject lines:** lead with the event, not the food.
    - For example, "You're in! BinaryHeart's first meeting is Thursday, Oct 8".
- **Cats on Campus event descriptions** use the same HTML rules.
    - They have no preview text, and the signature is optional.

## Images and hosting

- Prepare illustrations with `scripts/prepare_illustration.py`, which trims them and caps them at 640px wide for a hero or about 240px for icons.
- Host them before sending, by adding them to `email/assets/` in github.com/BinaryHeartUS/design and pushing.
    - Reference them as `https://raw.githubusercontent.com/BinaryHeartUS/design/main/email/assets/<name>.png`.
    - Google Drive links don't work reliably as email images.
- Always set `width`, `alt`, `style="display: block; border: 0; height: auto;"`.
- Use the hosted logo at `.../email/assets/logo.png`, a PNG render of the official `icon.svg`.
    - Gmail can't show SVG.
    - The footer shows the logo on a small white tile, so the navy half stays visible against the navy band.

## Checklist

- [ ] `python3 scripts/check_email_html.py FILE.html` passes with no errors.
- [ ] The wordmark is bold everywhere, with Binary in navy and Heart in red.
- [ ] Every link is real, or a listed `[PLACEHOLDER]`.
- [ ] The preview text is set, and the subject lines are proposed.
- [ ] Images are hosted, or the user has been told which ones need hosting.
- [ ] No unconfirmed stats appear.
