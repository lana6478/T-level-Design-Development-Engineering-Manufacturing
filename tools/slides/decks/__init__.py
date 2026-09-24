"""
Deck content for the lesson slides, one module per area of the course.

Each deck is a dict with:
    area        core | spec   (sets colour and label)
    file        output path under content/05-teaching-resources/slides/
    title       deck title
    unit        short location, e.g. "Core topic 4"
    spec        specification sections covered, e.g. "4.1, 4.2"
    pages       content/ pages the deck is linked from (first = main page)
    objectives  3 to 4 learning objectives
    starter     starter question
    slides      teaching slides (see render.py for the slide types)
    quiz        list of (question, answer)
    activity    {title, time, format, steps, success, notes}
    exit        3 exit-ticket prompts

Never use em or en dashes in deck text; the build refuses them.
"""
SITE = {
    "name": "Design and Development for Engineering and Manufacturing T Level",
    "short": "Design and Development for Engineering and Manufacturing",
    "url": "https://lana6478.github.io/T-level-Design-Development-Engineering-Manufacturing/",
    "author": "Samuel O'Connell",
    "awarding_body": "City & Guilds",
    "spec_url": "https://www.cityandguilds.com/-/media/productdocuments/engineering/mechanical/8714/"
                "centre_documents/dd-t-level-technical-qualification-specification-v15-pdf.pdf",
    # pages listed under "Related pages" on the Lesson Slides index
    "related": [
        "01-core-component/00-overview.md",
        "02-occupational-specialism/00-overview.md",
        "04-help-and-about/01-help.md",
    ],
}

# Areas of the course: label shown on slides, accent colour (hex), and
# light_text for accents dark enough to need white numbers on them.
AREAS = {
    "core": {"label": "Engineering Core", "accent": "F2B705"},
    "spec": {"label": "Mechanical Engineering", "accent": "E0463A", "light_text": True},
}

from . import core_a, core_b, specialism  # noqa: E402

ALL_DECKS = core_a.DECKS + core_b.DECKS + specialism.DECKS

AREA_ORDER = [
    {"key": "core", "heading": "Engineering Core",
     "blurb": "The 17 core topics shared by every Design and Development specialism, plus the Employer-set Project."},
    {"key": "spec", "heading": "Mechanical Engineering specialism",
     "blurb": "The knowledge criteria and the practical Performance Outcomes 2 to 6."},
]
