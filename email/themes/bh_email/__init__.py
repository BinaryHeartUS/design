"""BinaryHeart email theme library.

Six Gmail-safe directions, each a module in bh_email.themes with render(email, hdr, stats):

    from bh_email import render
    html = render("workbench", "recruitment", hdr="lockup", stats=True,
                  sender={"name": "Name", "email": "name@binaryheart.org"})

Defaults: Kickoff Poster or Navy Masthead for most emails; Workbench for big events.
Preference order: workbench > navy_masthead > kickoff_poster > admit_one > terminal_session > plain_letter.
"""
from importlib import import_module
from . import components
from .components import finish, IMG_BASE

THEMES = [
    ("kickoff_poster", "01 Kickoff Poster",
     "Lifts the poster straight into the inbox: cream page, navy date card with a big “Oct 8”, monospace eyebrows, white cards."),
    ("plain_letter", "02 Plain Letter",
     "Reads like a personal note from the chapter president. White page, no boxes, hairline rules and red section labels; one navy button."),
    ("navy_masthead", "03 Navy Masthead",
     "A navy masthead carries the headline, a red-navy stripe marks the break, and soft gray cards hold each step."),
    ("terminal_session", "04 Terminal Session",
     "Leans into the “Binary” half: a terminal window, the meeting as command output, // comment labels. 01000010 01001000 is “BH” in ASCII."),
    ("admit_one", "05 Admit One",
     "The first meeting as a ticket with a tear-off date stub in Northwestern purple. Purple leads here; navy and red support."),
    ("workbench", "06 Workbench",
     "Illustration-led: the isometric repair scenes set the mood, outlined cards echo their line work, cream matches the art."),
]
EMAILS = [("recruitment", "Recruitment"), ("announcement", "First Meeting Announcement")]
HEADERS = [("classic", "Classic header"), ("lockup", "Chapter lockup")]


def render(theme, email, hdr="lockup", stats=True, img_base=IMG_BASE, sender=None):
    mod = import_module(f".themes.{theme}", __name__)
    return finish(mod.render(email, hdr, stats), email, img_base, sender)
