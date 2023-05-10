from module_parser import parse_qa_bundle
from note_generators import generate_front_note, generate_back_note
from anki import make_deck, make_note, generate_anki
from tqdm import tqdm

DECK_NAME = "Module 1 - Indian Constitution"
QUESTION_PATH = "modules/module-1.txt"
ANSWER_PATH = "modules/module-1-answers.txt"
OUTPUT_NAME = DECK_NAME.replace(" ", "_") + ".apkg"

notes = parse_qa_bundle(QUESTION_PATH, ANSWER_PATH)
deck = make_deck(DECK_NAME)

for note in tqdm(notes):
    front_note = generate_front_note(note)
    back_note = generate_back_note(note)
    note = make_note(front_note, back_note)
    deck.add_note(note)

generate_anki(deck, OUTPUT_NAME)
