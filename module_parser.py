import string


def parse_questions(path):
    question_module = open(path, "r", encoding="utf-8")
    questions = question_module.read().split("\n\n")

    parsed_questions = []

    for i, question in enumerate(questions):
        question = questions[i].split(")")[0][:-1].replace("\n", "")
        options = questions[i].split(")")[1:]

        for i, option in enumerate(options):
            filtered_option = option
            if i != len(options) - 1:
                filtered_option = filtered_option[:-1]
            filtered_option = filtered_option.replace("\n", "").strip()
            options[i] = filtered_option

        question_object = {"question": question, "options": options}

        parsed_questions.append(question_object)

    return parsed_questions


def parse_answers(path):
    answer_module = open(path, "r", encoding="utf-8")
    answers = answer_module.read().split("\n")
    return answers


def parse_qa_bundle(question_path, answer_path):
    questions = parse_questions(question_path)
    answers = parse_answers(answer_path)

    if len(questions) != len(answers):
        raise Exception("Amount of questions and answers doesn't match")

    notes = []

    for question, answer in zip(questions, answers):
        answer_index = string.ascii_lowercase.index(answer)
        answer_text = question["options"][answer_index]
        question["answer"] = {"index": answer_index, "text": answer_text}
        notes.append(question)

    return notes
