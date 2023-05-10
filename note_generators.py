from utils import pos_to_char

FONT_SIZE = "20px"


def generate_option_string(options):
    option_string = ""
    for i, option in enumerate(options):
        option_char = pos_to_char(i)
        option_elem = f"{option_char}) {option} <br />"
        option_string += option_elem
    return option_string


def generate_front_note(note):
    question = note["question"]
    options = note["options"]
    option_string = generate_option_string(options)
    note = f"""
        <font style='font-size:{FONT_SIZE}'><b>{question}</b></font> <br />
        <font style='font-size:{FONT_SIZE}'>{option_string}</font>
    """
    return note


def generate_back_note(note):
    answer_index = note["answer"]["index"]
    answer_text = note["answer"]["text"]
    answer_char = pos_to_char(answer_index)
    note = f"""
        <font style='font-size:{FONT_SIZE}'>{answer_char}) {answer_text}</font>
    """
    return note
