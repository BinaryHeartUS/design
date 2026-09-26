"""Theme: Terminal Session."""
from ..components import *  # noqa: F401,F403
from .. import components as _c
C = _c.C


def render(email, hdr="lockup", stats=True):
    """email: 'recruitment' or 'announcement'; hdr: 'lockup' or 'classic'."""
    PAGE, TERM, TEXT2 = "#EEF0F4", "#1F3050", "#B9C4D8"
    R = ""
    dots = "".join(f'<span style="display: inline-block; width: 10px; height: 10px; border-radius: 5px; background-color: {c}; margin-right: 6px;"></span>' for c in (RED, PURPLE, NAVY))
    bar = cols([(40, dots), (60, f'<div style="text-align: right; font-family: {MONO}; font-size: 11px; color: {MUTED};">nu@binaryheart:~/fall-2026</div>')], valign="middle")
    R += row(bar, pad="12px 18px", bg="#FFFFFF", radius="14px 14px 0 0", extra=f" border-bottom: 1px solid {LINE};")
    head = (lockup(40, 20, 12, right=f'<span style="font-family: {MONO}; font-size: 11px; color: #9AA5B8;">01000010&nbsp;01001000</span>')
            if hdr == "lockup" else header_classic(56, 28, 15))
    body = f'<div style="padding-bottom: 20px;">{head}</div>'

    def comment(t):
        return f'<div style="font-family: {MONO}; font-size: 13px; font-weight: 600; color: {RED}; margin: 26px 0 10px 0;">// {t}</div>'

    body += p(f"Hi {FN},", 16, mb=12)
    body += (p(C["intro"]) + p(C["noapp"]) + p(C["returning"], mb=0)) if email == "recruitment" else (p(C["ann_intro"]) + p(C["returning"], mb=0))
    body += comment("first_meeting")

    def kv(k, v):
        return (f'<tr><td width="92" valign="top" style="font-family: {MONO}; font-size: 13px; color: {PINK}; padding: 3px 0;">{k}</td>'
                f'<td valign="top" style="font-family: {MONO}; font-size: 13px; color: #FFFFFF; padding: 3px 0;">{v}</td></tr>')
    term = (f'<div style="font-family: {MONO}; font-size: 13px; color: {TEXT2}; margin-bottom: 10px;"><span style="color: #7FD1A8;">$</span> binaryheart --first-meeting</div>'
            f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">'
            + kv("date", "Thursday, Oct 8") + kv("time", "11:00&ndash;18:00, drop in anytime")
            + kv("where", f'<a href="{MAP}" style="color: #FFFFFF; text-decoration: underline;">1910 Orrington Ave</a>, across from Foster-Walker')
            + kv("intros", "top of every hour, 11:00&ndash;17:00") + kv("bring", "nothing. no experience needed")
            + kv("snacks", "Dunkin' donuts, while they last") + '</table>')
    body += (f'<div style="background-color: {TERM}; border-radius: 10px; padding: 18px 20px;">{term}</div>'
             + '<div style="height: 14px;">&nbsp;</div>'
             + btn(RSVP, "rsvp --cats-on-campus", RED, font=MONO, size=14, radius=6)
             + f'<span style="font-family: {MONO}; font-size: 12px; color: {MUTED}; padding-left: 10px;"># optional</span>')
    if email == "announcement":
        body += comment("getting_there") + directions_list(font=F)
    body += comment("weekly_sessions") + p(C["avail"], 14) + btn(AVAIL, "share_availability()", NAVY, font=MONO, size=14, radius=6, pad="10px 18px")
    body += comment("want_to_lead") + p(C["lead"], 14) + btn(LEAD, "leadership_interest()", "#FFFFFF", NAVY, NAVY, font=MONO, size=14, radius=6, pad="10px 18px")
    body += comment("what_we_do") + whatwedo_rows(card_bg="#F6F7FA", radius=10, pad="10px 12px")
    if stats:
        body += '<div style="height: 6px;">&nbsp;</div>' + stats_row(NAVY, MUTED, LINE, MONO, 20)
    body += comment("questions") + p("Reply to this email and a real human will answer.", 14) + app_row(INK, 13)
    body += f'<div style="margin-top: 26px; padding-top: 20px; border-top: 1px dashed {LINE};">{signature()}</div>'
    if email == "announcement":
        body += f'<div style="margin-top: 18px;">{p(C["removal"], 12, MUTED, mb=0)}</div>'
    R += row(body, pad="24px 28px 28px 28px", bg="#FFFFFF")
    R += nonprofit_footer(bg=TERM, radius="0 0 14px 14px")
    return T(R, bg=PAGE)
