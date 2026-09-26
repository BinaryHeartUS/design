"""Theme: Plain Letter."""
from ..components import *  # noqa: F401,F403
from .. import components as _c
C = _c.C


def render(email, hdr="lockup", stats=True):
    """email: 'recruitment' or 'announcement'; hdr: 'lockup' or 'classic'."""
    RULE = "#E6E9EF"
    R = ""
    header = (f'<div style="padding-bottom: 18px; border-bottom: 1px solid {RULE};">{lockup(40, 20, 12)}</div>' if hdr == "lockup"
              else f'<div style="padding-bottom: 22px; border-bottom: 1px solid {RULE};">{header_classic(56, 28, 16)}</div>')
    R += row(header, pad="8px 0 0 0")

    def label(t):
        return f'<div style="font-family: {F}; font-size: 12px; font-weight: 700; letter-spacing: 1.6px; text-transform: uppercase; color: {RED}; margin-bottom: 10px;">{t}</div>'

    def section(inner):
        return row(inner, pad="26px 0", extra=f" border-bottom: 1px solid {RULE};")

    letter = p(f"Hi {FN},", 16, mt=0)
    letter += (p(C["intro"]) + p(C["noapp"]) + p(C["returning"], mb=0)) if email == "recruitment" else (p(C["ann_intro"]) + p(C["returning"], mb=0))
    R += section(letter)
    fm = (label("First meeting")
          + f'<div style="font-family: {F}; font-size: 24px; font-weight: 700; color: {NAVY}; line-height: 1.25;">Thursday, October 8</div>'
          + f'<div style="font-family: {F}; font-size: 16px; color: {INK}; margin: 4px 0 2px 0;">11 AM &ndash; 6 PM, drop in anytime</div>'
          + f'<div style="font-family: {F}; font-size: 16px; margin-bottom: 16px;">{a(MAP, "1910 Orrington Ave, Evanston", NAVY, 500)} <span style="color: {MUTED};">&middot; across from Foster-Walker</span></div>'
          + highlights_list(INK, RED, 15, square=False)
          + '<div style="height: 8px;">&nbsp;</div>' + btn(RSVP, "RSVP on Cats on Campus", NAVY, radius=6)
          + f'<div style="font-family: {F}; font-size: 12px; color: {MUTED}; margin-top: 8px;">Optional, but it helps us plan.</div>')
    R += section(fm)
    if email == "announcement":
        R += section(label("Getting there") + directions_list(num_color=NAVY))
    R += section(label("Weekly sessions") + p(C["avail"]) + a(AVAIL, "Share your availability &rarr;", NAVY, 700, False))
    R += section(label("Want to lead?") + p(C["lead"]) + a(LEAD, "Leadership interest form &rarr;", NAVY, 700, False))
    wwd = ""
    for key, t, d in C["whatwedo"]:
        wwd += (f'<tr><td width="56" valign="middle" style="padding: 6px 12px 6px 0;"><img src="{img(key)}" alt="" width="48" style="width: 48px; height: auto; display: block; border: 0;"></td>'
                f'<td valign="middle" style="padding: 6px 0; font-family: {F}; font-size: 14px; color: {MUTED};"><strong style="color: {INK};">{t}.</strong> {d}</td></tr>')
    inner = label("What we do") + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{wwd}</table>'
    if stats:
        inner += '<div style="height: 18px;">&nbsp;</div>' + stats_row(NAVY, MUTED, RULE, F, 22)
    R += section(inner)
    R += row(p("Questions? Just reply to this email.", 15, mb=14) + app_row(INK, 14), pad="26px 0", extra=f" border-bottom: 1px solid {RULE};")
    R += row(signature(), pad="26px 0")
    if email == "announcement":
        R += row(p(C["removal"], 12, MUTED, mb=0), pad="0 0 20px 0")
    R += row(f'<p style="margin: 0; font-family: {F}; font-size: 12px; line-height: 1.6; color: {MUTED};">{BH} Inc. is a student-run 501(c)(3) nonprofit spreading digital access. EIN 93-2078509.<br>'
             f'{a(SITE, "binaryheart.org/nu", MUTED, 600)} &middot; Upcycle, Upskill, Uplift</p>', pad="18px 0 8px 0", extra=f" border-top: 1px solid {RULE};")
    return T(R, width=580, bg="#FFFFFF", pad="28px 20px")
