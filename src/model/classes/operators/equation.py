from abc import ABC, abstractmethod

# An abstract class that represents some two number equation

class Equation(ABC):
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right

    @abstractmethod
    def get_correct_answer(self):
        pass

    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
               self.left == other.left and \
               self.right == other.right