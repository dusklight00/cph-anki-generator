from module_parser import parse_qa_bundle

notes = parse_qa_bundle(
    question_path="modules/module-1.txt", answer_path="modules/module-1-answers.txt"
)

print(notes)
