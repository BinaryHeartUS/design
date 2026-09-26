"""Theme: Navy Masthead."""
from ..components import *  # noqa: F401,F403
from .. import components as _c
C = _c.C


def render(email, hdr="lockup", stats=True):
    """email: 'recruitment' or 'announcement'; hdr: 'lockup' or 'classic'."""
    PAGE, SOFT = "#EDF0F5", "#F4F6FA"
    R = ""
    chip = (f'<div style="background-color: #FFFFFF; border-radius: 12px; padding: 12px 16px; display: inline-block;">{lockup(38, 19, 12)}</div>' if hdr == "lockup"
            else f'<div style="background-color: #FFFFFF; border-radius: 14px; padding: 16px 28px; display: inline-block;">{header_classic(48, 24, 14)}</div>')
    align = "left" if hdr == "lockup" else "center"
    if email == "recruitment":
        h1, sub = "Come to our first meeting.", "Thursday, October 8 &middot; 11 AM&ndash;6 PM &middot; 1910 Orrington Ave"
    else:
        h1, sub = "See you this Thursday.", "October 8 &middot; drop in anytime 11 AM&ndash;6 PM &middot; 1910 Orrington Ave"
    band = (f'<div style="text-align: {align};">{chip}'
            f'<h1 style="margin: 26px 0 8px 0; font-family: {F}; font-size: 34px; line-height: 1.15; font-weight: 800; color: #FFFFFF;">{h1}</h1>'
            f'<div style="font-family: {F}; font-size: 15px; color: #D5DCE8;">{sub}</div></div>')
    R += row(band, pad="30px 32px 34px 32px", bg=NAVY, radius="16px 16px 0 0")
    R += row(stripe(5))
    body = f'<img src="{img("hero-teardown")}" alt="An open laptop mid-repair with tools laid out" width="536" style="width: 100%; max-width: 536px; height: auto; display: block; margin: 0 auto 22px auto; border: 0;">'
    body += p(f"Hi {FN},", 16, mb=12)
    body += (p(C["intro"]) + p(C["noapp"]) + p(C["returning"])) if email == "recruitment" else (p(C["ann_intro"]) + p(C["returning"]))

    def card(title, inner):
        return (f'<div style="background-color: {SOFT}; border-radius: 12px; padding: 20px 22px; margin-top: 14px;">'
                f'<div style="font-family: {F}; font-size: 18px; font-weight: 700; color: {NAVY}; margin-bottom: 10px;">{title}</div>{inner}</div>')

    fm = (cols([(34, f'<div style="font-family: {F}; font-size: 12px; font-weight: 700; letter-spacing: 1.4px; color: {RED};">THURSDAY</div>'
                     f'<div style="font-family: {F}; font-size: 40px; font-weight: 800; line-height: 1; color: {NAVY};">Oct 8</div>'
                     f'<div style="font-family: {F}; font-size: 14px; font-weight: 600; color: {INK}; margin-top: 6px;">11 AM &ndash; 6 PM</div>'),
                (66, highlights_list(INK, RED, 14))], gap=14)
          + '<div style="height: 10px;">&nbsp;</div>' + btn(RSVP, "RSVP on Cats on Campus", RED)
          + f'<span style="font-family: {F}; font-size: 12px; color: {MUTED}; padding-left: 10px;">Optional</span>')
    body += card("First meeting", fm)
    if email == "announcement":
        body += card("Getting there", directions_list())
    body += card("Help set our weekly schedule", p(C["avail"], 14) + btn(AVAIL, "Share your availability", NAVY, size=14, pad="10px 18px"))
    body += card("Want to lead?", p(C["lead"], 14) + lead_btn("Leadership interest form", "#FFFFFF", NAVY, NAVY, size=14, pad="10px 18px"))
    wwd = whatwedo_rows(card_bg="#FFFFFF", radius=10, pad="10px 12px")
    if stats:
        wwd += '<div style="height: 6px;">&nbsp;</div>' + stats_row(NAVY, MUTED, "#C9D0DC", F, 20)
    body += card("What we do", wwd)
    body += (f'<div style="margin-top: 22px;">' + p("Questions? Just reply to this email.", 15) + app_row() + '</div>')
    body += f'<div style="margin-top: 24px;">{signature()}</div>'
    if email == "announcement":
        body += f'<div style="margin-top: 20px;">{p(C["removal"], 12, MUTED, mb=0)}</div>'
    R += row(body, pad="28px 32px 30px 32px", bg="#FFFFFF")
    R += nonprofit_footer(radius="0 0 16px 16px")
    return T(R, bg=PAGE)
