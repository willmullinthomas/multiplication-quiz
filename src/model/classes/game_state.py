from .equation import Equation
from .answer import Answer

# Snapshot of the current state of the game
# Includes the list of all equations for the game, the current equation, and all answers so far

class GameState:
    def __init__(self, equation_list: list[Equation]):
        self.equation_list: list[Equation] = equation_list
        self.count: int = len(equation_list)
        self.current: int = 0
        self.answers: list[Answer] = []

    def get_current_equation(self):
        self.__check_current()
        return self.equation_list[self.current]

    def make_guess(self, guess: int):
        self.__check_current()
        current_equation = self.equation_list[self.current]
        self.answers.append(Answer(current_equation.left, current_equation.right, guess))
        self.current += 1

    def do_equations_remain(self):
        return self.current < self.count

    def get_cur_left(self):
        self.__check_current()
        return self.equation_list[self.current].left

    def get_cur_right(self):
        self.__check_current()
        return self.equation_list[self.current].right

    def get_answer_left(self, index):
        self.__check_index(index)
        return self.answers[index].left
    
    def get_answer_right(self, index):
        self.__check_index(index)
        return self.answers[index].right

    def get_guess(self, index):
        self.__check_index(index)
        return self.answers[index].guess
    
    def __check_index(self, index):
        if index >= len(self.answers):
            raise Exception("Given index is out of bounds")
    
    def __check_current(self):
        if self.current >= self.count:
            raise Exception("All equations have been answered")