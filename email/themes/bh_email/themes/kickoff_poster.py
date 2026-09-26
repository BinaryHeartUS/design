"""Theme: Kickoff Poster."""
from ..components import *  # noqa: F401,F403
from .. import components as _c
C = _c.C


def render(email, hdr="lockup", stats=True):
    """email: 'recruitment' or 'announcement'; hdr: 'lockup' or 'classic'."""
    CREAM, CARD = "#F6F4EF", "#FFFFFF"
    R = ""
    header = (lockup(right=f'<span style="font-family: {MONO}; font-size: 11px; font-weight: 600; letter-spacing: 1px; color: {NAVY}; border: 1.5px solid {NAVY}; border-radius: 999px; padding: 5px 10px; white-space: nowrap;">501(c)(3) NONPROFIT</span>')
              if hdr == "lockup" else header_classic())
    R += row(header, pad="8px 4px 20px 4px")
    if email == "recruitment":
        eb, h1a, h1b = "Now recruiting · <span style=\"color: %s;\">Northwestern</span> chapter" % PURPLE, "Come to our", "first meeting."
    else:
        eb, h1a, h1b = "This Thursday · <span style=\"color: %s;\">Northwestern</span> chapter" % PURPLE, "See you", "Thursday."
    hero = (eyebrow(eb) +
            f'<h1 style="margin: 12px 0 10px 0; font-family: {F}; font-size: 44px; line-height: 1.02; font-weight: 800; letter-spacing: -1.5px; color: {NAVY};">{h1a}<br><span style="color: {RED};">{h1b}</span></h1>' +
            p("We refurbish donated computers, build software, and partner with nonprofits. Open to every major and year.", 16, "#3A4458", mb=0))
    R += row(cols([(64, hero), (36, f'<div style="background-color: {NAVY}; border-radius: 20px; padding: 12px; text-align: center;"><img src="{img("software")}" alt="" width="170" style="width: 100%; max-width: 170px; height: auto; border: 0;"></div>')], gap=16, valign="middle"), pad="0 4px")
    R += spacer(22)
    # navy date card
    left = (f'<div style="font-family: {MONO}; font-size: 13px; font-weight: 600; letter-spacing: 2px; color: {PINK};">THURSDAY</div>'
            f'<div style="font-family: {F}; font-size: 60px; font-weight: 800; letter-spacing: -2px; line-height: 0.95; color: #FFFFFF;">Oct 8</div>'
            f'<div style="font-family: {F}; font-size: 20px; font-weight: 700; color: #FFFFFF; margin-top: 8px;">11 AM &ndash; 6 PM</div>'
            f'<div style="font-family: {F}; font-size: 14px; color: #D5DCE8;">Drop in anytime</div>')
    right = (f'<div style="border-left: 2px solid #4A6389; padding-left: 16px;">'
             f'<div style="font-family: {F}; font-size: 17px; font-weight: 800;"><a href="{MAP}" style="color: #FFFFFF; text-decoration: none;">1910 Orrington Ave</a></div>'
             f'<div style="font-family: {F}; font-size: 13px; color: #D5DCE8; margin-bottom: 12px;">Across from Foster-Walker</div>'
             + highlights_list("#FFFFFF", RED, 14) + '</div>')
    card = (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td style="font-family: {MONO}; font-size: 13px; font-weight: 600; letter-spacing: 2px; color: #FFFFFF;">FALL 2026 KICKOFF</td>'
            f'<td align="right" style="font-family: {F}; font-size: 14px; font-weight: 600; color: #FFFFFF;">No experience needed.</td></tr></table>'
            f'<div style="height: 16px; line-height: 16px;">&nbsp;</div>'
            + cols([(46, left), (54, right)], gap=16, valign="top") +
            f'<div style="height: 18px; line-height: 18px;">&nbsp;</div>'
            + btn(RSVP, "RSVP on Cats on Campus", RED) +
            f'<span style="font-family: {F}; font-size: 12px; color: #D5DCE8; padding-left: 12px;">Optional, but it helps us plan.</span>')
    R += row(card, pad="24px 24px", bg=NAVY, radius="20px")
    R += spacer(16)
    # letter card
    letter = p(f"Hi {FN},", 16, mb=12)
    if email == "recruitment":
        letter += p(C["intro"]) + p(C["noapp"]) + p(C["returning"], mb=0)
    else:
        letter += p(C["ann_intro"]) + p(C["returning"], mb=0)
    R += row(letter, pad="22px 24px", bg=CARD, radius="16px")
    R += spacer(16)
    if email == "announcement":
        R += row(eyebrow("Getting there") + '<div style="height: 12px;">&nbsp;</div>' + directions_list(), pad="22px 24px", bg=CARD, radius="16px")
        R += spacer(16)
    nxt = (eyebrow("Next steps") + '<div style="height: 14px;">&nbsp;</div>'
           + f'<div style="font-family: {F}; font-size: 16px; font-weight: 700; color: {NAVY};">Help set our weekly schedule</div>'
           + p(C["avail"], 14, MUTED, mt=4) + btn(AVAIL, "Share your availability", NAVY, size=14, pad="10px 18px")
           + f'<div style="border-top: 1px solid {LINE}; margin: 20px 0;"></div>'
           + f'<div style="font-family: {F}; font-size: 16px; font-weight: 700; color: {NAVY};">Want to lead?</div>'
           + p(C["lead"], 14, MUTED, mt=4) + lead_btn("Leadership interest form", "#FFFFFF", NAVY, NAVY, size=14, pad="10px 18px"))
    R += row(nxt, pad="22px 24px", bg=CARD, radius="16px")
    R += spacer(22)
    R += row(eyebrow(f'What we do <span style="color: {MUTED}; font-weight: 400; letter-spacing: 0.5px; text-transform: none;">&mdash; a bit of everything, roles come later</span>')
             + '<div style="height: 10px;">&nbsp;</div>' + whatwedo_rows(card_bg=CARD, radius=16), pad="0 4px")
    if stats:
        R += spacer(8)
        R += row(stats_row(), pad="0 4px")
    R += spacer(18)
    q = cols([(30, f'<div style="font-family: {MONO}; font-size: 12px; font-weight: 600; letter-spacing: 1.2px; color: {DEEPRED};">QUESTIONS?</div>'
                   f'<div style="font-family: {F}; font-size: 13px; color: {MUTED}; margin-top: 2px;">Just reply to this email.</div>'),
              (70, f'<div style="text-align: right;">{app_row(size=13, gap=12)}</div>')], valign="middle")
    R += row(q, pad="14px 20px", bg=CARD, radius="16px")
    R += spacer(22)
    R += row(signature(), pad="0 4px 22px 4px")
    if email == "announcement":
        R += row(p(C["removal"], 12, MUTED, mb=0), pad="0 4px 18px 4px")
    R += nonprofit_footer(radius="16px")
    return T(R, bg=CREAM)
