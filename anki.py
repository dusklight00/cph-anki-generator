import random
import genanki

model = genanki.Model(
    1607392319,
    "Basic Model",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
)


def generate_id():
    return random.randrange(1 << 30, 1 << 31)


def make_deck(name):
    id = generate_id()
    return genanki.Deck(id, name)


def make_note(front, back):
    note = genanki.Note(model=model, fields=[front, back])
    return note


def generate_anki(deck, output_name):
    return genanki.Package(deck).write_to_file(output_name)
