"""Fall 2026 Northwestern kickoff series in the Workbench theme (chapter lockup header, stats row on).

Emails: recruitment (callout / no callout), post-callout, first meeting announcement,
Cats on Campus event description, day-of event notification, welcome.

    from bh_email.series import fall_2026_nu as s
    s.write_all("out/", sender={"name": "...", "email": "..."})
"""
import os
from .. import components as D
from ..components import (NAVY, RED, PURPLE, INK, MUTED, F, MONO, FN, RSVP, AVAIL, LEAD, lead_btn, lead_link, DISCORD, IG, MAP,
                          BH, a, p, btn, cols, row, spacer, lockup, signature, app_row, nonprofit_footer,
                          highlights_list, directions_list, whatwedo_rows, stats_row, T, finish, IMG_BASE)

PAGE, OUT, BLURPLE = "#FDF6EA", "#26303F", "#5865F2"
SLIDES = "[CALLOUT_SLIDES_LINK]"




# ---------------------------------------------------------------- building blocks
def card(inner, pad="20px 20px"):
    return row(inner, pad=pad, bg="#FFFFFF", radius="16px", extra=f" border: 2px solid {OUT};") + spacer(14)


def titled(t, icon=None):
    ic = (f'<img src="{D.img(icon)}" alt="" width="26" height="26" style="width: 26px; height: 26px; vertical-align: -6px; '
          f'border: 0; border-radius: 7px; margin-right: 10px;">') if icon else ""
    return f'<div style="font-family: {F}; font-size: 18px; font-weight: 800; color: {NAVY}; margin-bottom: 10px;">{ic}{t}</div>'


def with_art(text_html, art, w=150):
    """Text beside an illustration on desktop; the illustration drops below the text on phones."""
    return D.stack([(370, f'<div style="padding-right: 16px;">{text_html}</div>'),
                    (190, f'<div style="text-align: center; padding: 8px 0;"><img src="{D.img(art)}" alt="" width="{w}" '
                          f'style="width: {w}px; max-width: 100%; height: auto; display: inline-block; border: 0;"></div>')], align="left")


def header():
    return row(lockup(44, 22, 13), pad="8px 4px 10px 4px")


def hero(art, h1, sub=True, cta=True):
    out = row(f'<img src="{D.img(art)}" alt="Isometric illustration of computer repair" width="600" style="width: 100%; max-width: 600px; height: auto; display: block; border: 0;">', pad="6px 0 4px 0")
    inner = f'<h1 style="margin: 0; font-family: {F}; font-size: 34px; line-height: 1.12; font-weight: 800; letter-spacing: -0.8px; color: {NAVY}; text-align: center;">{h1}</h1>'
    if sub:
        inner += f'<div style="font-family: {F}; font-size: 16px; color: {INK}; text-align: center; margin-top: 10px;"><strong>Thursday, October 8</strong> &middot; 11 AM&ndash;6 PM &middot; {a(MAP, "1910 Orrington Ave", NAVY, 600)}</div>'
    if cta:
        inner += (f'<div style="text-align: center; margin-top: 18px;">{btn(RSVP, "RSVP on Cats on Campus", RED, border=OUT, radius=10)}</div>'
                  f'<div style="font-family: {F}; font-size: 12px; color: {MUTED}; text-align: center; margin-top: 8px;">Optional, but it helps us plan.</div>')
    return out + row(inner, pad="14px 8px 24px 8px")


def letter(paras):
    return card(p(f"Hi {FN},", 16, mb=12) + "".join(p(x) for x in paras[:-1]) + p(paras[-1], mb=0))


def expect_card(extra=""):
    return card(with_art(titled("What to expect") + highlights_list(INK, RED, 14, sub=True) + extra, "toolkit", 160))


def details_card(highlights=True):
    body = (f'<div style="font-family: {F}; font-size: 12px; font-weight: 700; letter-spacing: 1.4px; color: {RED};">THURSDAY</div>'
            f'<div style="font-family: {F}; font-size: 40px; font-weight: 800; line-height: 1; color: {NAVY};">Oct 8</div>'
            f'<div style="font-family: {F}; font-size: 15px; font-weight: 600; color: {INK}; margin-top: 6px;">11 AM &ndash; 6 PM &middot; drop in anytime</div>'
            f'<div style="font-family: {F}; font-size: 14px; margin-top: 6px;">{a(MAP, "1910 Orrington Ave, Evanston", NAVY, 600)}</div>'
            f'<div style="font-family: {F}; font-size: 13px; color: {MUTED}; margin-top: 2px;">Across from Foster-Walker</div>')
    if not highlights:
        return card(body)

    hl = highlights_list(INK, RED, 14)
    head, sep, tail = hl.rpartition("margin: 0 0 9px 0;")  # no trailing gap after the last bullet, so the list centers vertically
    hl = head + "margin: 0;" + tail
    # Desktop: date block and bullets sit side by side, centered as a pair. Phone: bullets drop under the address, left-aligned.
    return card(D.stack([(340, f'<div style="padding: 0 12px 12px 0;">{body}</div>'), (220, hl)], align="left"))


def getting_there():
    return card(titled("Getting there") + directions_list()
                + p(f"Can't find us? DM {a(IG, '@binaryheartatnu', NAVY, 600)} or email {a('mailto:nu@binaryheart.org', 'nu@binaryheart.org', NAVY, 600)}. We watch both during meetings.", 13, MUTED, mt=4, mb=0))


def weekly_card():
    return card(with_art(titled("Join our mailing list") + p(D.C["avail"], 14)
                         + btn(AVAIL, "Join our mailing list", NAVY, border=OUT, size=14, radius=10, pad="10px 18px"), "laptop"))


def lead_card():
    return card(titled("Want to lead?") + p(D.C["lead"], 14)
                + lead_btn("Leadership interest form", "#FFFFFF", NAVY, OUT, size=14, radius=10, pad="10px 18px"))


def whatwedo_card(stats=True):
    inner = titled("What we do") + whatwedo_rows(card_bg=PAGE, radius=12, pad="10px 12px")
    if stats:
        inner += '<div style="height: 6px;">&nbsp;</div>' + stats_row(NAVY, MUTED, "#E3D6BE", F, 20)
    return card(inner)


def discord_card(intro):
    steps = [
        f"Join our server: {a(DISCORD, 'discord.gg/QutKWgv7U', BLURPLE, 600)}",
        "Log in or create a Discord account, then set your <strong>server nickname to your full name</strong> so we know who you are",
        f"Download Discord on <strong>both</strong> your computer and phone and log in: {a('https://discord.com/download', 'discord.com/download', BLURPLE, 600)}",
        "Complete your Discord profile and make sure notifications are enabled on all of your devices",
    ]
    ol = "".join(f'<tr><td valign="top" width="26" style="font-family: {MONO}; font-size: 14px; font-weight: 700; color: {BLURPLE}; padding: 0 0 10px 0;">{i}</td>'
                 f'<td valign="top" style="font-family: {F}; font-size: 14px; line-height: 1.55; color: {INK}; padding: 0 0 10px 0;">{s}</td></tr>'
                 for i, s in enumerate(steps, 1))
    return card(titled("Discord setup", "app-discord") + p(intro, 14)
                + f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{ol}</table>'
                + btn(DISCORD, "Join our Discord", BLURPLE, border=OUT, size=14, radius=10, pad="10px 18px"))


def callout_card():
    items = "".join(f'<div style="font-family: {F}; font-size: 14px; font-weight: 600; color: {INK}; margin: 0 0 8px 0;">'
                    f'<span style="display: inline-block; width: 8px; height: 8px; background-color: {RED}; margin-right: 10px; vertical-align: middle;"></span>{t}</div>'
                    for t in ("Background on BinaryHeart", "What each department does", "Leadership opportunities and how to get involved"))
    return card(titled("Callout meeting")
                + p("<strong>[CALLOUT_DATE] &middot; [CALLOUT_TIME] &middot; [CALLOUT_LOCATION]</strong>", 15, mb=10)
                + items
                + p("We'll present for 30&ndash;40 minutes, then take questions (the Q&amp;A is optional). Can't make it? We'll email the slides, and you can still come to our first meeting.", 13, MUTED, mt=6, mb=0))


def connect_and_sign(sign=True, removal=False, question="Questions? Just reply to this email."):
    out = row(p(question, 15) + app_row(), pad="6px 4px 0 4px")
    if sign:
        out += row(signature(), pad="22px 4px 20px 4px")
    else:
        out += spacer(20)
    if removal:
        out += row(p(D.C["removal"], 12, MUTED, mb=0), pad="0 4px 18px 4px")
    return out + nonprofit_footer(bg=NAVY, radius="16px")


_OPTS = {"img_base": IMG_BASE, "sender": None}


def page(rows_html, pre_key):
    return finish(T(rows_html, bg=PAGE), pre_key, _OPTS["img_base"], _OPTS["sender"])


# ---------------------------------------------------------------- emails
def recruitment(callout):
    R = header() + hero("hero-teardown", "Take apart a laptop with us.")
    R += letter([D.C["intro"], D.C["noapp"], D.C["returning"]])
    if callout:
        R += callout_card()
    R += expect_card() + weekly_card() + lead_card() + whatwedo_card()
    closer = "Questions? Just reply to this email. See you at the callout and on October 8!" if callout else "Questions? Just reply to this email. See you on October 8!"
    return page(R + connect_and_sign(question=closer), "recruitment")


def post_callout():
    R = header() + hero("knolling", "Thanks for coming to our callout.", sub=False, cta=False)
    R += card(p(f"Hi {FN},", 16, mb=12)
              + p(f"If you were at today's callout, thank you for coming! If you couldn't make it, {a(SLIDES, 'here are the slides', NAVY, 600)}. Below is everything you need for our first meeting and beyond.")
              + p("As a reminder, <strong>there's no application this year.</strong> You're already on our email list, which is all you need.", mb=0))
    R += details_card(highlights=False)
    R += row(f'<div style="text-align: center;">{btn(RSVP, "RSVP on Cats on Campus", RED, border=OUT, radius=10)}'
             f'<div style="font-family: {F}; font-size: 12px; color: {MUTED}; margin-top: 8px;">Optional, but it helps us plan.</div></div>', pad="0 0 18px 0")
    R += expect_card(p("We'll teach you how to disassemble, diagnose, repair, upgrade, and reassemble devices. No experience or weekly time commitment is ever required.", 13, MUTED, mt=6, mb=0))
    R += getting_there() + weekly_card() + lead_card()
    R += discord_card("We use Discord as our primary communications platform. Please get it set up before your first meeting, as we'll share important onboarding information there.")
    R += whatwedo_card()
    return page(R + connect_and_sign(), "postcallout")


def announcement(callout):
    R = header() + hero("knolling", "Thursday, the bench is open.")
    paras = [D.C["ann_intro"]]
    if callout:
        paras.append(f"Missed our callout meeting? {a(SLIDES, 'Here are the slides', NAVY, 600)} so you can catch up.")
    paras.append(D.C["returning"])
    R += letter(paras)
    R += expect_card() + getting_there() + weekly_card() + lead_card() + whatwedo_card()
    return page(R + connect_and_sign(removal=True), "announcement")


def event_description():
    R = header() + hero("knolling", "First Meeting &middot; Fall 2026", cta=False)
    R += card(p(f"{BH} is a student-run nonprofit at universities and high schools across the US that refurbishes “retired” computers for donation to underserved groups. "
                "Drop in anytime: at the top of every hour we give a quick intro to our mission, history, and plans, then you'll get hands-on experience repairing a real laptop. "
                "Open to all, and no experience is necessary.", mb=0))
    R += details_card() + getting_there() + weekly_card()
    R += row(p(f"Questions? Email {a('mailto:nu@binaryheart.org', 'nu@binaryheart.org', NAVY, 600)} or DM {a(IG, '@binaryheartatnu', NAVY, 600)}.", 15, mb=0), pad="4px 4px 20px 4px")
    return page(R + nonprofit_footer(bg=NAVY, radius="16px"), None)


def event_notification():
    R = header() + hero("hero-teardown", "Today: take apart a laptop with us.", cta=False)
    R += details_card() + getting_there() + weekly_card()
    R += discord_card("We use Discord as our primary communications platform. If you haven't already, please get it set up before your first meeting, as we'll share important onboarding information there.")
    return page(R + connect_and_sign(sign=False, question=f"Questions? Email us at {a('mailto:nu@binaryheart.org', 'nu@binaryheart.org', NAVY, 600)}."), "notification")


def welcome():
    R = header() + hero("bundle", f"Welcome to {BH}!", sub=False, cta=False)
    R += card(p(f"Hi {FN},", 16, mb=12)
              + p("We're excited to have you join our community. Below is everything you need to get connected and start volunteering.", mb=0))
    R += card(with_art(titled("Volunteering hours")
                       + p('We work on an "open house" system: come as much or as little as you like during open hours, with no fixed time commitment.', 14)
                       + p("Our Fall Quarter meeting times will be set based on the availability of active members. "
                           "We'll announce the schedule on <strong>Sunday, October 11</strong> by email.", 14)
                       + btn(AVAIL, "Join our mailing list", NAVY, border=OUT, size=14, radius=10, pad="10px 18px"), "laptop"))
    R += getting_there()
    R += discord_card("We use Discord as our primary communications platform, so please get it set up as soon as you can.")
    R += card(titled("Next step: come to our first meeting")
              + p(f"Attend our first meeting on <strong>Thursday, October 8</strong> (drop in anytime, 11 AM&ndash;6 PM), and we'll get you set up in person. "
                  f"Can't make it? Email {a('mailto:nu@binaryheart.org', 'nu@binaryheart.org', NAVY, 600)} and we'll set up a time that works for you.", 14, mb=0))
    lead_text = (f"Interested in leading a department or project? Fill out our {lead_link('leadership interest form', NAVY, 600)} (just your name and email), or tell anyone on exec at a meeting."
                 if LEAD else "Attend our weekly meetings regularly this fall, and you'll be considered for a Winter Quarter leadership or director role. We choose Winter leaders at the end of Fall Quarter based on attendance and involvement.")
    R += card(titled("Want to lead?") + p(lead_text, 14, mb=0))
    return page(R + connect_and_sign(question="Questions? Just reply to this email."), "welcome")


FILES = {
    "callout": [("recruitment.html", lambda: recruitment(True)), ("post-callout.html", post_callout),
                ("first-meeting-announcement.html", lambda: announcement(True)), ("event-description.html", event_description),
                ("event-notification.html", event_notification), ("welcome.html", welcome)],
    "no-callout": [("recruitment.html", lambda: recruitment(False)), ("first-meeting-announcement.html", lambda: announcement(False)),
                   ("event-description.html", event_description), ("event-notification.html", event_notification),
                   ("welcome.html", welcome)],
}


def write_all(out_dir, img_base=IMG_BASE, sender=None, names=None):
    """Write both versions. names: optional {version: {file: new_name}} to rename outputs."""
    _OPTS.update(img_base=img_base, sender=sender)
    written = []
    for version, items in FILES.items():
        d = os.path.join(out_dir, version)
        os.makedirs(d, exist_ok=True)
        for fn, make in items:
            name = (names or {}).get(version, {}).get(fn, fn)
            open(os.path.join(d, name), "w").write(make())
            written.append(os.path.join(d, name))
    return written
