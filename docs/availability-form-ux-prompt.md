# Brainstorm: Frictionless Availability Collection for BinaryHeart at Northwestern

You are a senior product designer and UX researcher.
Brainstorm a custom UX for collecting weekly availability from new student members, optimized to be as close to zero-friction as humanly possible.

## Context

- BinaryHeart is a student-run nonprofit that refurbishes "retired" computers for donation to underserved groups.
- The Northwestern University chapter meets at its own space at 1910 Orrington Ave, Evanston, about a 4-5 minute walk from campus.
- Weekly meetings are drop-in "open house" repair sessions, not fixed-attendance meetings.
    - Members come to as many or as few sessions as they like, with no time commitment.
    - So the goal is NOT to find one time when everyone is free.
    - The goal is to pick roughly 2-4 recurring weekly blocks that together let the largest number of people attend at least one session each week.
- The first meeting is a drop-in workshop on Thursday, October 8, 2026, 11 AM - 6 PM.
- The Fall 2026 weekly schedule will be announced on Sunday, October 11, 2026, based on the availability collected.
    - Emails start going out in late September, so there are roughly two weeks to collect responses.
- This year there is no application: anyone on the email list is a member.
    - Leadership and director roles are open to everyone through the same pipeline.

## Who fills this out

- Northwestern undergraduates of every major and year, most with no technical background.
- Many are new to the club and have low commitment so far, so any friction means they simply won't respond.
- Most will open the email on their phone, between classes, with seconds of attention.
- By early October they know their class schedule, but not yet their exam, club, or job schedules.

## How they reach the form

- They get it as a link or button inside an HTML email sent through a mail-merge tool.
    - The email supports merge tags such as `{{First Name}}`, and we can likely add others like email address or last name.
    - Northwestern emails usually follow the format `FirstLast202X@u.northwestern.edu`, where 202X is the graduation year.
    - Assume emails cannot run JavaScript, so any interactivity happens after a click.
- The same link also appears on the chapter's Cats on Campus event page, Instagram (@binaryheartatnu), and possibly a QR code at the first meeting.
    - Those channels have no merge tags, so the design needs a path for people who arrive anonymously.

## Current baseline

- For now we are using a Timeful link: https://timeful.app/e/ZG6SVV.
- Treat Timeful (and When2meet, LettuceMeet, Google Forms, Doodle) as the baseline to beat.
    - Name exactly which steps in those tools cost the user time or attention.

## Constraints

- No login or account creation for respondents, ever.
- It must work well on a phone first, and on a laptop second.
- It must be accessible (screen readers, keyboard, color-blind safe), not only drag-to-paint.
- It should take under 30 seconds for a typical respondent, and ideally under 10.
- Collect as little personal data as possible, and say clearly what we do with it.
- A small student team maintains it.
    - Hosting options include our existing website (binaryheart.org, which already has chapter pages like `/nu/join`), a Google Form or Sheet, or a lightweight hosted page.
    - Favor designs we can build in a day or two over ones that need ongoing engineering.
- It must fit BinaryHeart branding: "Binary" in navy #2F4A70 and "Heart" in red #FF0040, always bold when written in color, with the Lexend font and Northwestern purple #4E2A84 as an accent.

## What I want from you

1. Start by breaking down every point of friction between "opens email" and "response recorded," step by step.
2. Brainstorm at least 8 distinct concepts, ranging from small tweaks to unconventional ideas.
    - Include at least one concept where the response is recorded directly from a single tap in the email.
    - Include at least one concept that inverts the question (for example, "tap when you're NOT free" or "pick your top 2 blocks").
    - Include at least one concept that imports existing schedule data (for example, a pasted class schedule, a calendar file, or Google Calendar free/busy), and weigh the privacy cost honestly.
    - Include at least one concept that uses sensible pre-selected defaults so most people only confirm or adjust.
3. For each concept, give the following:
    - A one-sentence summary.
    - The exact user flow, tap by tap, with an estimated number of taps and seconds.
    - What it gains and what it gives up in accuracy, response rate, and effort to build.
    - How it handles someone arriving without merge-tag data.
4. Rank the concepts, and recommend one primary design plus one fallback.
5. For the recommended design, provide the following:
    - A mobile wireframe described screen by screen, including empty, partially filled, and submitted states.
    - The exact microcopy: email button text, page headline, helper text, and confirmation message.
    - How it pre-fills and lets people correct their identity (for example, a name guessed from `FirstLast202X` with a one-tap "Not you?" edit).
    - How respondents can change their answer later without friction.
    - The time grid itself: which days, which hours, and what block size, with a justification for weekday afternoons versus evenings for students.
6. Explain how the team should turn the responses into 2-4 weekly session blocks.
    - Treat it as a coverage problem: maximize the number of people who can attend at least one block, not the overlap for everyone.
    - Give a simple method a student could run in a spreadsheet.
7. Suggest how to boost response rate before the Sunday, October 11 deadline (for example, reminder timing, QR codes at the October 8 meeting, or showing live counts).
    - The first email goes out in late September, and the final push is the 3 days between the October 8 meeting and October 11.
8. Finish with the top 3 risks or open questions I should decide on before building.

## Output format

- Use clear headers for each numbered section above.
- Keep each bullet to one sentence, and use indented sub-bullets for extra detail.
- Be concrete and opinionated, and prefer specific numbers and copy over generalities.
