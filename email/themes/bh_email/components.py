"""Shared building blocks for BinaryHeart emails (Gmail-safe tables, inline styles).

Originally written for the Fall 2026 Northwestern kickoff proposals.

Every email is Gmail-safe: table layout, inline styles only, no flex/grid,
no <style> blocks, images referenced by URL. Images are written as
{{IMG:name}} tokens and resolved per output target (relative files for the
Drive folder, data URIs for the gallery artifact).
"""
import os, re

# ---------------------------------------------------------------- brand
NAVY, RED, PURPLE = "#2F4A70", "#FF0040", "#4E2A84"
INK, MUTED, LINE = "#1B2233", "#4A5468", "#D9DEE7"
DEEPRED, PINK = "#C8003A", "#FF8FA8"
BLURPLE = "#5865F2"
F = "Lexend, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'Fira Code', Menlo, Consolas, 'Courier New', monospace"
FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700;800&family=Fira+Code:wght@500;600;700&display=swap" rel="stylesheet">'
FN = "{{First Name}}"

RSVP = "https://cglink.me/23r/r376771/"
# Mailing list sign-up (the weekly schedule is announced to this list). Name kept as AVAIL for compatibility.
AVAIL = "https://join.binaryheart.org/nu"
# Leadership interest form URL. None hides every form button/link and tells people to talk to exec instead.
LEAD = None  # e.g. "https://forms.gle/..." once the form exists
DISCORD = "https://discord.gg/QutKWgv7U"
IG = "https://instagram.com/binaryheartatnu"
MAP = "https://maps.app.goo.gl/7UAMTC36M6UMPhax6"
SITE = "https://www.binaryheart.org/nu"
LOGO = "{{IMG:logo}}"


def lead_btn(label, *args, **kw):
    """Leadership form button, or nothing while LEAD is None."""
    return btn(LEAD, label, *args, **kw) if LEAD else ""


def lead_link(label, *args, **kw):
    """Leadership form text link, or nothing while LEAD is None."""
    return a(LEAD, label, *args, **kw) if LEAD else ""


def img(name):
    return "{{IMG:%s}}" % name


def wm(size=None, dark_bg=False):
    """BinaryHeart wordmark: always bold."""
    fs = f" font-size: {size}px;" if size else ""
    return (f'<strong style="font-weight: 800;{fs}"><span style="color: {NAVY};">Binary</span>'
            f'<span style="color: {RED};">Heart</span></strong>')


BH = wm()
NU = f'<span style="color: {PURPLE}; font-weight: 600;">Northwestern</span>'


def a(url, text, color=NAVY, weight=600, underline=True):
    dec = "underline" if underline else "none"
    return f'<a href="{url}" style="color: {color}; text-decoration: {dec}; font-weight: {weight};">{text}</a>'


def T(rows_html, width=640, pad="20px 16px", bg="#FFFFFF"):
    """Outer email shell: the theme background fills the whole message, with 16px side margins
    between the screen edge and the content so cards never touch the edges on phones.
    (Mail apps may still add their own thin margin outside the email; that can't be removed from Gmail-sent HTML.)
    """
    return f'''<!-- Fonts (used by Apple Mail / iOS; Gmail falls back to Helvetica/Arial) -->
{FONT_LINK}
{{{{PRE}}}}
<div style="margin: 0; padding: 0; background-color: {bg};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="background-color: {bg};">
<tr><td align="center" style="padding: {pad};">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width: {width}px; width: 100%; font-family: {F}; color: {INK};">
{rows_html}
</table>
</td></tr>
</table>
</div>
'''


def row(inner, pad="0", bg=None, radius=None, extra=""):
    st = f"padding: {pad};"
    if bg:
        st += f" background-color: {bg};"
    if radius:
        st += f" border-radius: {radius};"
    return f'<tr><td style="{st}{extra}">{inner}</td></tr>\n'


def spacer(h):
    return f'<tr><td style="height: {h}px; line-height: {h}px; font-size: 1px;">&nbsp;</td></tr>\n'


def p(text, size=15, color=INK, mt=0, mb=14, lh=1.6, extra=""):
    return f'<p style="margin: {mt}px 0 {mb}px 0; font-family: {F}; font-size: {size}px; line-height: {lh}; color: {color};{extra}">{text}</p>'


def btn(url, label, bg, fg="#FFFFFF", border=None, radius=8, font=F, size=15, upper=False, pad="12px 22px"):
    b = border or bg
    tt = " text-transform: uppercase; letter-spacing: 1px;" if upper else ""
    return (f'<a href="{url}" style="display: inline-block; background-color: {bg}; color: {fg}; border: 2px solid {b}; '
            f'border-radius: {radius}px; padding: {pad}; font-family: {font}; font-size: {size}px; font-weight: 700; '
            f'text-decoration: none; line-height: 1.2;{tt}">{label}</a>')


def stack(cells, align="center", valign="middle"):
    """Fluid-hybrid columns: cells sit side by side when they fit and stack on narrow screens.

    cells: list of (max_width_px, html). Uses inline-block + max-width, which Gmail keeps
    (media queries and <style> blocks don't survive injection into Gmail).
    """
    parts = "".join(f'<div style="display: inline-block; width: 100%; max-width: {w}px; vertical-align: {valign}; '
                    f'text-align: left; font-size: 14px; box-sizing: border-box;">{html}</div>' for w, html in cells)
    return f'<div style="font-size: 0; line-height: 0; text-align: {align};"><div style="line-height: normal; font-size: 0;">{parts}</div></div>'


def cols(cells, gap=16, valign="top"):
    """cells: list of (width_percent, html). Gmail-safe columns."""
    tds = []
    for i, (w, html) in enumerate(cells):
        pl = 0 if i == 0 else gap // 2
        pr = 0 if i == len(cells) - 1 else gap // 2
        tds.append(f'<td width="{w}%" valign="{valign}" style="padding: 0 {pr}px 0 {pl}px;">{html}</td>')
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{"".join(tds)}</tr></table>'


# ---------------------------------------------------------------- copy
C = {
    "intro": f"Thanks for your interest in {BH}! I'm [SENDER_NAME], president of {BH} at Northwestern. We're a student-run nonprofit that refurbishes “retired” computers and donates them to people who need them. We're open to every major and year, and no technical experience is needed.",
    "noapp": "<strong>There's no application this year.</strong> Being on our email list is all it takes, so you're already in.",
    "returning": "<strong>Returning members:</strong> welcome back! Come say hi on October 8th and help us show new members the ropes.",
    "ann_intro": "You're invited to our first meeting of the 2026&ndash;27 school year: a drop-in computer repair workshop at our space. Come for 20 minutes or stay all afternoon. No experience needed.",
    "highlights": [
        ("Intros every hour", "A quick intro to BinaryHeart at the top of every hour, 11 AM to 5 PM"),
        ("Meet the team", "Get to know exec and other new members"),
        ("Hands-on repair", "Take apart and repair a real laptop on day one"),
        ("Dunkin' donuts", "For everyone who stops by, while they last"),
    ],
    "avail": "Our weekly meeting times will be set based on the availability of active members. We'll announce the schedule on <strong>Sunday, October 11</strong> by email.",
    "lead": ("We're recruiting leaders and directors, with no application or interview. Get involved as a member and step up as the chapter grows, or tell us now with a short form (just your name and email)."
             if LEAD else
             "Attend our weekly meetings regularly this fall, and you'll be considered for a Winter Quarter leadership or director role. We choose Winter leaders at the end of Fall Quarter based on attendance and involvement, with no application or interview."),
    "directions": [
        "Find the house with the screened front porch, directly across from Foster-Walker (2nd house to the right of the apartment building at Orrington &amp; Emerson).",
        "Take the pathway along the right side of the house.",
        "Enter the side door and take the stairs on your right. Someone from exec will meet you and get you set up.",
    ],
    "whatwedo": [
        ("hardware", "Hardware", "Repair and refurbish donated computers"),
        ("software", "Software", "Run AI agents on a 15-device OpenClaw cluster"),
        ("operations", "Operations", "Work with partners, run events, win grants"),
    ],
    # Confirm current numbers before every send (see skill brand-core.md). Confirmed for Fall 2026 NU:
    "stats": [("400+", "devices donated"), ("$89.1K+", "value of devices donated"), ("135+", "student volunteers"), ("3.2K+", "volunteer hours")],
    "removal": f"This is the last general email sent to our full email list. If we haven't seen you at a meeting or heard from you, you'll be removed from future emails. You're always welcome at future {BH} meetings.",
}

PREHEADER = {
    "recruitment": "You're in! Drop in to our first meeting Thursday, Oct 8, 11 AM&ndash;6 PM at 1910 Orrington. No experience needed.",
    "announcement": "Drop in anytime Thursday 11 AM&ndash;6 PM at 1910 Orrington. Intros every hour, no experience needed.",
}


def preheader(email):
    return (f'<div style="display: none; font-size: 1px; line-height: 1px; max-height: 0; max-width: 0; opacity: 0; '
            f'overflow: hidden; mso-hide: all;">{PREHEADER[email]}</div>')


# ---------------------------------------------------------------- shared headers
def stripe(h=4):
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td width="50%" style="height: {h}px; line-height: {h}px; font-size: 1px; background-color: {RED};">&nbsp;</td>'
            f'<td width="50%" style="height: {h}px; line-height: {h}px; font-size: 1px; background-color: {NAVY};">&nbsp;</td>'
            f'</tr></table>')


def header_classic(logo=64, title=32, sub=17, align="center"):
    return (f'<div style="text-align: {align};">'
            f'<img src="{LOGO}" alt="BinaryHeart" width="{logo}" style="width: {logo}px; height: auto; display: inline-block; border: 0;">'
            f'<div style="font-family: {F}; font-size: {title}px; line-height: 1.15; margin-top: 10px;">{wm()}</div>'
            f'<div style="font-family: {F}; font-size: {sub}px; font-weight: 600; color: {PURPLE}; margin-top: 4px;">at Northwestern University</div>'
            f'</div>')


def lockup(logo=44, title=22, sub=13, right=""):
    left = (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td valign="middle" style="padding-right: 12px;"><img src="{LOGO}" alt="BinaryHeart" width="{logo}" style="width: {logo}px; height: auto; display: block; border: 0;"></td>'
            f'<td valign="middle"><div style="font-family: {F}; font-size: {title}px; line-height: 1.1;">{wm()}</div>'
            f'<div style="font-family: {F}; font-size: {sub}px; font-weight: 600; color: {INK}; margin-top: 3px;">'
            f'<span style="color: {PURPLE};">Northwestern</span> Chapter</div></td></tr></table>')
    if not right:
        return left
    return (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td valign="middle">{left}</td><td valign="middle" align="right">{right}</td></tr></table>')


def signature(color=INK, muted=MUTED):
    return (f'{p("Best,", mb=4, color=color)}'
            f'<p style="margin: 0; font-family: {F}; font-size: 15px; font-weight: 700; color: {color};">[SENDER_NAME]</p>'
            f'<p style="margin: 2px 0 0 0; font-family: {F}; font-size: 13px; color: {muted};">{BH} President (Northwestern Chapter)</p>'
            f'<p style="margin: 2px 0 0 0; font-family: {F}; font-size: 13px;">{a("mailto:[SENDER_EMAIL]", "[SENDER_EMAIL]", NAVY, 500)}</p>')


def app_row(color=INK, size=14, gap=18):
    """Instagram + Discord links; each item is inline-block so the pair wraps cleanly on phones."""
    def item(icon, label, url):
        return (f'<div style="display: inline-block; padding: 0 {gap}px 8px 0; white-space: nowrap;"><a href="{url}" style="text-decoration: none; color: {color};">'
                f'<img src="{img(icon)}" alt="" width="28" height="28" style="width: 28px; height: 28px; vertical-align: middle; border: 0; border-radius: 7px;">'
                f'<span style="font-family: {F}; font-size: {size}px; font-weight: 600; vertical-align: middle; padding-left: 8px; color: {color};">{label}</span></a></div>')
    return f'<div>{item("app-instagram", "@binaryheartatnu", IG)}{item("app-discord", "Join our Discord", DISCORD)}</div>'


def nonprofit_footer(bg=NAVY, fg="#FFFFFF", muted="#D5DCE8", radius="0 0 16px 16px", mono=True):
    """Logo + legal line, then URL + tagline. Side by side on desktop, stacked on phones."""
    ff = MONO if mono else F
    left = (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td valign="middle" style="padding-right: 12px;"><div style="background-color: #FFFFFF; border-radius: 8px; padding: 5px 5px 4px 5px; line-height: 0;">'
            f'<img src="{LOGO}" alt="BinaryHeart" width="30" style="width: 30px; height: auto; display: block; border: 0;"></div></td>'
            f'<td valign="middle"><p style="margin: 0; font-family: {F}; font-size: 12px; line-height: 1.5; color: {muted};">BinaryHeart Inc. is a student-run 501(c)(3) nonprofit spreading digital access. <span style="white-space: nowrap;">EIN 93-2078509.</span></p></td>'
            f'</tr></table>')
    right = (f'<div style="padding: 6px 0;"><a href="{SITE}" style="font-family: {ff}; font-size: 13px; font-weight: 700; color: {fg}; text-decoration: none;">binaryheart.org/nu</a>'
             f'<div style="font-family: {F}; font-size: 12px; color: {muted}; margin-top: 2px;">Upcycle, Upskill, Uplift</div></div>')
    return row(stack([(340, f'<div style="padding: 6px 16px 6px 0;">{left}</div>'), (170, right)], align="left"),
               pad="14px 22px", bg=bg, radius=radius)


def highlights_list(color=INK, marker=RED, size=15, square=True, sub=False, submuted=MUTED):
    out = ""
    for title, desc in C["highlights"]:
        mk = (f'<span style="display: inline-block; width: 8px; height: 8px; background-color: {marker}; margin-right: 10px; vertical-align: middle;'
              f'{"" if square else " border-radius: 4px;"}"></span>')
        extra = f'<div style="font-weight: 400; font-size: 13px; color: {submuted}; padding-left: 18px;">{desc}</div>' if sub else ""
        out += f'<div style="font-family: {F}; font-size: {size}px; font-weight: 600; color: {color}; line-height: 1.4; margin: 0 0 9px 0;">{mk}{title}{extra}</div>'
    return out


def directions_list(color=INK, num_color=RED, font=F):
    out = ""
    for i, d in enumerate(C["directions"], 1):
        out += (f'<tr><td valign="top" width="28" style="font-family: {MONO}; font-size: 14px; font-weight: 700; color: {num_color}; padding: 0 0 10px 0;">{i}</td>'
                f'<td valign="top" style="font-family: {font}; font-size: 14px; line-height: 1.55; color: {color}; padding: 0 0 10px 0;">{d}</td></tr>')
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{out}</table>'


def whatwedo_rows(title_color=NAVY, desc_color=MUTED, card_bg=None, border=None, radius=14, imgw=72, pad="12px 14px"):
    out = ""
    for key, t, d in C["whatwedo"]:
        st = f"padding: {pad};"
        if card_bg:
            st += f" background-color: {card_bg};"
        if border:
            st += f" border: {border};"
        st += f" border-radius: {radius}px;"
        out += (f'<tr><td style="{st}">'
                + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
                  f'<td width="{imgw + 14}" valign="middle" style="padding-right: 14px;"><img src="{img(key)}" alt="" width="{imgw}" style="width: {imgw}px; height: auto; display: block; border: 0;"></td>'
                  f'<td valign="middle"><div style="font-family: {F}; font-size: 16px; font-weight: 700; color: {title_color};">{t}</div>'
                  f'<div style="font-family: {F}; font-size: 13px; line-height: 1.45; color: {desc_color}; margin-top: 2px;">{d}</div></td></tr></table>'
                + '</td></tr><tr><td style="height: 10px; line-height: 10px; font-size: 1px;">&nbsp;</td></tr>')
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{out}</table>'


def stats_row(num_color=NAVY, label_color=MUTED, rule=LINE, font=MONO, size=22):
    """Four stats in a row on desktop; wraps to two per row on phones (no media queries needed)."""
    cells = []
    for n, l in C["stats"]:
        cells.append((132, f'<div style="border-left: 2px solid {rule}; padding: 0 8px 10px 10px;">'
                           f'<div style="font-family: {font}; font-size: {size}px; font-weight: 700; color: {num_color}; line-height: 1.1;">{n}</div>'
                           f'<div style="font-family: {F}; font-size: 12px; line-height: 1.35; color: {label_color}; margin-top: 3px;">{l}</div></div>'))
    return stack(cells, align="left", valign="top")


def eyebrow(text, color=NAVY, bar=RED, font=MONO, size=12):
    bar_html = f'<span style="display: inline-block; width: 3px; height: 14px; background-color: {bar}; vertical-align: -2px; margin-right: 8px;"></span>' if bar else ""
    return f'<div style="font-family: {font}; font-size: {size}px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; color: {color};">{bar_html}{text}</div>'



# ---------------------------------------------------------------- finishing
PREHEADER.update({
    "postcallout": "Callout slides, first meeting details, and how to join our Discord.",
    "notification": "Today 11 AM&ndash;6 PM at 1910 Orrington: intros every hour and your first laptop repair.",
    "welcome": "Welcome to BinaryHeart! Join our Discord and find our space at 1910 Orrington.",
})

IMG_BASE = "https://raw.githubusercontent.com/BinaryHeartUS/design/main/email/assets"


def finish(html, pre_key=None, img_base=IMG_BASE, sender=None):
    """Insert preview text, resolve {{IMG:name}} tokens, fill sender, and ASCII-encode.

    img_base: URL or relative path prefix for email/assets/*.png.
    sender: optional dict(name=..., email=...) replacing [SENDER_NAME] / [SENDER_EMAIL].
    """
    ph = "" if pre_key is None else (f'<div style="display: none; font-size: 1px; line-height: 1px; max-height: 0; max-width: 0; '
                                     f'opacity: 0; overflow: hidden; mso-hide: all;">{PREHEADER[pre_key]}</div>')
    html = html.replace("{{PRE}}", ph)
    html = re.sub(r"\{\{IMG:([a-z0-9-]+)\}\}", lambda m: f"{img_base}/{m.group(1)}.png", html)
    if sender:
        html = html.replace("[SENDER_NAME]", sender.get("name", "[SENDER_NAME]")).replace("[SENDER_EMAIL]", sender.get("email", "[SENDER_EMAIL]"))
    for month in ("October", "November", "December", "September", "January"):
        html = html.replace(f"{month} ", f"{month[:3]}&zwnj;{month[3:]} ")
    return html.encode("ascii", "xmlcharrefreplace").decode()

