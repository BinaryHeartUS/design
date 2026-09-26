# Web: binaryheart.org and join.binaryheart.org

The site is a Tailwind-styled single-page app with national pages (`/about`, `/join`, `/faq`, `/donate`, `/request`, `/contact`) and chapter pages at `/<chapter>/join`.
`join.binaryheart.org/<chapter>` is a separate lightweight mailing-list sign-up card.

## Conventions to keep

- Use the system font stack for UI text (`-apple-system, system-ui, "SF Pro Text", "Segoe UI", sans-serif`), matching the existing site.
    - Lexend is fine for new standalone pages.
- The chapter lockup from join.binaryheart.org is the model for chapter headers.
    - It has the logo, then the bold wordmark, then "*School* Chapter" in 13px with the school in its accent.
    - Cards get a 4px top stripe, red to navy.
- The primary button is red, full width on mobile, radius 10-12px, with a subtle red-to-deeper-red gradient on the web (email stays solid).
- Secondary buttons are white with a 1px border.
- Support dark mode, as join.binaryheart.org already does:
    - The background is about `#11151D` and cards about `#1A2030`.
    - Lift navy text to about `#9DB5DD` so it stays readable, and keep the red at about `#FF4D73`.
    - The wordmark on dark backgrounds sits on a light chip, or uses the lifted navy while keeping the red for "Heart".

## Tailwind tokens

When editing the site, add these to the theme instead of scattering arbitrary values:

```js
colors: {
  bh: { navy: '#2F4A70', red: '#FF0040', 'red-text': '#C8003A', ink: '#1B2233',
        muted: '#4A5468', line: '#D9DEE7', cream: '#F6F4EF' },
  chapter: { nu: '#4E2A84' }   // add others as confirmed (see brand-core.md)
}
```

The wordmark component should be one shared piece of markup:

```html
<span class="font-extrabold"><span class="text-bh-navy">Binary</span><span class="text-bh-red">Heart</span></span>
```

## Fixes needed on the live site

- `/nu/join` and join.binaryheart.org color "Binary" red and "Heart" navy.
    - Swap them to Binary navy and Heart red, and make every colored wordmark bold (the first meeting card and the footer "BinaryHeart™" are regular weight).
- Some wordmarks use Tailwind `text-purple-600` or gray.
    - Only the school name should take the chapter accent, and never the wordmark.
- Replace the mirrored heart icon with `assets/logo/heart-logo.png`.

## Page patterns

- **Chapter join page:**
    - A hero ("Join BinaryHeart at *School*"), then the first meeting card (date, time, location with a map link, focus, and getting-there steps).
    - Then weekly meetings, "Everyone is welcome", why join (six benefits), what to expect, and the Instagram and email contacts.
- **Mailing-list card:** the lockup, "Join our mailing list", a school email field with the domain suffix shown, a red Join button, and a "Join by email instead" secondary.
    - Add a privacy line under the buttons.
