from .equation import Equation

# A subtraction equation

class Subtraction(Equation):

    def get_correct_answer(self):
        return self.left - self.right