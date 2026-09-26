"""Theme: Admit One."""
from ..components import *  # noqa: F401,F403
from .. import components as _c
C = _c.C


def render(email, hdr="lockup", stats=True):
    """email: 'recruitment' or 'announcement'; hdr: 'lockup' or 'classic'."""
    PAGE, LIL = "#F3F1F7", "#E9E4F2"
    R = ""
    head = lockup(44, 22, 13) if hdr == "lockup" else header_classic(60, 30, 16)
    R += row(head, pad="8px 4px 22px 4px")
    letter = p(f"Hi {FN},", 16, mb=12)
    letter += (p(C["intro"]) + p(C["noapp"]) + p(C["returning"], mb=0)) if email == "recruitment" else (p(C["ann_intro"]) + p(C["returning"], mb=0))
    R += row(letter, pad="22px 24px", bg="#FFFFFF", radius="14px")
    R += spacer(18)
    main = (f'<div style="font-family: {MONO}; font-size: 11px; font-weight: 600; letter-spacing: 2px; color: {PURPLE};">ADMIT ONE &middot; FREE &middot; DROP IN</div>'
            f'<div style="font-family: {F}; font-size: 22px; font-weight: 800; color: {NAVY}; line-height: 1.2; margin: 8px 0 12px 0;">{BH} First Meeting<br><span style="font-size: 15px; font-weight: 600; color: {MUTED};">Computer Repair Workshop</span></div>'
            + highlights_list(INK, RED, 13, square=False)
            + f'<div style="font-family: {F}; font-size: 13px; color: {MUTED}; margin-top: 8px;">{a(MAP, "1910 Orrington Ave", NAVY, 600)}, across from Foster-Walker</div>')
    stub = (f'<div style="text-align: center;">'
            f'<div style="font-family: {MONO}; font-size: 12px; font-weight: 600; letter-spacing: 2px; color: #D9CCF0;">THU</div>'
            f'<div style="font-family: {F}; font-size: 16px; font-weight: 700; color: #FFFFFF; margin-top: 4px;">OCT</div>'
            f'<div style="font-family: {F}; font-size: 54px; font-weight: 800; line-height: 1; color: #FFFFFF;">8</div>'
            f'<div style="font-family: {F}; font-size: 13px; font-weight: 600; color: #FFFFFF; margin-top: 8px;">11 AM<br>&ndash;<br>6 PM</div></div>')
    ticket = (f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>'
              f'<td width="72%" valign="top" style="background-color: #FFFFFF; border-radius: 14px 0 0 14px; padding: 20px 20px; border: 2px solid {PURPLE}; border-right: 0;">{main}</td>'
              f'<td width="28%" valign="middle" style="background-color: {PURPLE}; border-radius: 0 14px 14px 0; padding: 16px 8px; border-left: 3px dashed #FFFFFF;">{stub}</td>'
              f'</tr></table>')
    R += row(ticket)
    R += spacer(14)
    R += row(btn(RSVP, "RSVP on Cats on Campus", PURPLE) + f'<span style="font-family: {F}; font-size: 12px; color: {MUTED}; padding-left: 12px;">Optional, but it helps us plan.</span>', pad="0 4px")
    R += spacer(22)

    def block(title, inner):
        return row(f'<div style="font-family: {F}; font-size: 17px; font-weight: 700; color: {NAVY}; margin-bottom: 8px;">{title}</div>{inner}', pad="20px 24px", bg="#FFFFFF", radius="14px") + spacer(12)
    if email == "announcement":
        R += block("Getting there", directions_list(num_color=PURPLE))
    R += block("Help set our weekly schedule", p(C["avail"], 14) + btn(AVAIL, "Share your availability", NAVY, size=14, pad="10px 18px"))
    R += block("Want to lead?", p(C["lead"], 14) + lead_btn("Leadership interest form", "#FFFFFF", NAVY, NAVY, size=14, pad="10px 18px"))
    wwd = whatwedo_rows(card_bg=LIL, radius=10, pad="10px 12px")
    if stats:
        wwd += '<div style="height: 6px;">&nbsp;</div>' + stats_row(PURPLE, MUTED, "#CFC6E0", F, 20)
    R += block("What we do", wwd)
    R += row(p("Questions? Just reply to this email.", 15) + app_row(), pad="10px 4px 0 4px")
    R += row(signature(), pad="22px 4px 20px 4px")
    if email == "announcement":
        R += row(p(C["removal"], 12, MUTED, mb=0), pad="0 4px 18px 4px")
    R += nonprofit_footer(bg=PURPLE, muted="#DCD3EC", radius="14px")
    return T(R, bg=PAGE)
