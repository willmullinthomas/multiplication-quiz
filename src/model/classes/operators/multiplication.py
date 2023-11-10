from .equation import Equation

# A multiplication equation with a multiplicand and multiplier

class Multiplication(Equation):

    def get_correct_answer(self):
        return self.left * self.right