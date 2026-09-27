"""Theme: Workbench."""
from ..components import *  # noqa: F401,F403
from .. import components as _c
C = _c.C


def render(email, hdr="lockup", stats=True):
    """email: 'recruitment' or 'announcement'; hdr: 'lockup' or 'classic'."""
    PAGE, OUT = "#FDF6EA", "#26303F"
    R = ""
    head = lockup(44, 22, 13) if hdr == "lockup" else header_classic(60, 30, 16)
    R += row(head, pad="8px 4px 10px 4px")
    hero_img = "hero-teardown" if email == "recruitment" else "knolling"
    h1 = "Take apart a laptop with us." if email == "recruitment" else "Thursday, the bench is open."
    R += row(f'<img src="{img(hero_img)}" alt="Isometric illustration of a laptop being repaired" width="600" style="width: 100%; max-width: 600px; height: auto; display: block; border: 0;">', pad="6px 0 4px 0")
    R += row(f'<h1 style="margin: 0; font-family: {F}; font-size: 34px; line-height: 1.12; font-weight: 800; letter-spacing: -0.8px; color: {NAVY}; text-align: center;">{h1}</h1>'
             f'<div style="font-family: {F}; font-size: 16px; color: {INK}; text-align: center; margin-top: 10px;"><strong>Thursday, October 8</strong> &middot; 11 AM&ndash;6 PM &middot; {a(MAP, "1910 Orrington Ave", NAVY, 600)}</div>'
             f'<div style="text-align: center; margin-top: 18px;">{btn(RSVP, "RSVP on Cats on Campus", RED, border=OUT, radius=10)}</div>'
             f'<div style="font-family: {F}; font-size: 12px; color: {MUTED}; text-align: center; margin-top: 8px;">Optional, but it helps us plan.</div>', pad="14px 8px 24px 8px")

    def card(inner, pad="22px 24px"):
        return row(inner, pad=pad, bg="#FFFFFF", radius="16px", extra=f" border: 2px solid {OUT};") + spacer(14)

    letter = p(f"Hi {FN},", 16, mb=12)
    letter += (p(C["intro"]) + p(C["noapp"]) + p(C["returning"], mb=0)) if email == "recruitment" else (p(C["ann_intro"]) + p(C["returning"], mb=0))
    R += card(letter)

    def titled(t):
        return f'<div style="font-family: {F}; font-size: 18px; font-weight: 800; color: {NAVY}; margin-bottom: 10px;">{t}</div>'
    R += card(cols([(66, titled("What to expect") + highlights_list(INK, RED, 14, sub=True)),
                    (34, f'<img src="{img("toolkit")}" alt="" width="160" style="width: 100%; max-width: 160px; height: auto; display: block; border: 0;">')], gap=12, valign="middle"))
    if email == "announcement":
        R += card(titled("Getting there") + directions_list())
    R += card(cols([(66, titled("Join our mailing list") + p(C["avail"], 14) + btn(AVAIL, "Join our mailing list", NAVY, border=OUT, size=14, radius=10, pad="10px 18px")),
                    (34, f'<img src="{img("laptop")}" alt="" width="150" style="width: 100%; max-width: 150px; height: auto; display: block; border: 0;">')], gap=12, valign="middle"))
    R += card(titled("Want to lead?") + p(C["lead"], 14) + lead_btn("Leadership interest form", "#FFFFFF", NAVY, OUT, size=14, radius=10, pad="10px 18px"))
    wwd = titled("What we do") + whatwedo_rows(card_bg=PAGE, radius=12, pad="10px 12px")
    if stats:
        wwd += '<div style="height: 6px;">&nbsp;</div>' + stats_row(NAVY, MUTED, "#E3D6BE", F, 22)
    R += card(wwd)
    R += row(p("Questions? Just reply to this email.", 15) + app_row(), pad="6px 4px 0 4px")
    R += row(signature(), pad="22px 4px 20px 4px")
    if email == "announcement":
        R += row(p(C["removal"], 12, MUTED, mb=0), pad="0 4px 18px 4px")
    R += nonprofit_footer(bg=NAVY, radius="16px")
    return T(R, bg=PAGE)
