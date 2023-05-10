from module_parser import parse_qa_bundle
from note_generators import generate_front_note, generate_back_note

notes = parse_qa_bundle(
    question_path="modules/module-1.txt", answer_path="modules/module-1-answers.txt"
)


frontnote = generate_front_note(notes[0])
backnote = generate_back_note(notes[0])


print(frontnote, backnote)
