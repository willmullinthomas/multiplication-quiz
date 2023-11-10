from .equation import Equation

# An addition equation

class Addition(Equation):

    def get_correct_answer(self):
        return self.left + self.right