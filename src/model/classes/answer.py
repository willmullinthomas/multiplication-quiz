from .operators.equation import Equation

# An Equation with a guess

class Answer:
    def __init__(self, equation: Equation, guess: int):
        self.equation = equation
        self.guess = guess
    
    def get_correct_answer(self):
        self.equation.get_correct_answer()

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
            self.equation == other.equation and \
            self.guess == other.guess
    