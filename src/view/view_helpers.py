from src.model.classes.answer import Answer
from src.model.helpers import create_equation_table, get_equation_list
from src.model.classes.game_state import GameState

def get_new_game(max: int, count: int, has_addition: bool, has_multiplication: bool, has_subtraction: bool):
    if not has_addition and not has_multiplication and not has_subtraction:
        raise Exception("At least one equation type must be selected")
    equation_table = create_equation_table(max, has_addition, has_multiplication, has_subtraction)
    return GameState(get_equation_list(equation_table, count))

def get_equation_label(left: int, right: int):
    return str(left) + " x " + str(right)

def get_answer_label(answer: Answer, with_guess: bool):
    label = get_equation_label(answer.left, answer.right) + " = " + str(answer.get_correct_answer())
    if with_guess:
        label = label + ", guess: " + str(answer.guess)
    return label