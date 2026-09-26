# Email

This folder holds BinaryHeart's Gmail-safe email system.
It uses tables and inline styles only, and loads images from `email/assets/` in this repo.

- `themes/bh_email/` is the Python theme library.
    - `components.py` holds the shared building blocks and copy.
    - `themes/*.py` holds one module per direction.
    - `series/fall_2026_nu.py` is the Fall 2026 NU kickoff series in Workbench.
- `templates/<theme>/` holds a starter recruitment and announcement email for each theme.
    - To reuse one, find and replace the example details, meaning the date, place, links, `[SENDER_NAME]`, and `[SENDER_EMAIL]`.
- `gallery/index.html` is the interactive comparison of every theme and variant.
    - `gallery/_template.html` is its source.
- `series/2026-fall-nu/` holds the Fall 2026 NU emails, built with placeholders for the sender.
- `archive/` holds earlier NU emails with personal details and internal links redacted.
- `build.py` regenerates templates, the gallery, and series.

Run `python3 tools/check_email_html.py` on anything before sending.
