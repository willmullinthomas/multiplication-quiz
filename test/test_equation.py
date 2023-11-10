import unittest
import sys
sys.path.append("..") # for running from within tests directory

from src.model.classes.operators.equation import Equation
from src.model.classes.operators.multiplication import Multiplication
from src.model.classes.operators.addition import Addition
from src.model.classes.operators.subtraction import Subtraction
from src.model.classes.answer import Answer

class TestEquation(unittest.TestCase):
    def test_get_correct_multiplication(self):
        test_multiplication_1 = Multiplication(0, 0)
        test_multiplication_2 = Multiplication(5, 6)

        """
        Test that multiplication is correct
        """
        self.assertEqual(test_multiplication_1.get_correct_answer(), 0)
        self.assertEqual(test_multiplication_2.get_correct_answer(), 30)
    
    def test_get_correct_addition(self):
        test_addition_1 = Addition(0, 0)
        test_addition_2 = Addition(5, 6)

        """
        Test that addition is correct
        """
        self.assertEqual(test_addition_1.get_correct_answer(), 0)
        self.assertEqual(test_addition_2.get_correct_answer(), 11)

    def test_get_correct_subtraction(self):
        test_subtraction_1 = Subtraction(0, 0)
        test_subtraction_2 = Subtraction(10, 5)
        test_subtraction_3 = Subtraction(5, 6)

        self.assertEqual(test_subtraction_1.get_correct_answer(), 0)
        self.assertEqual(test_subtraction_2.get_correct_answer(), 5)
        self.assertEqual(test_subtraction_3.get_correct_answer(), -1)

    def test_equation_equality(self):
        test_multiplication_1 = Multiplication(0, 0)
        test_multiplication_2 = Multiplication(5, 6)
        test_addition_2 = Addition(5, 6)
        test_subtraction_2 = Subtraction(5, 6)

        """
        Test multiplication equality
        """
        self.assertEqual(test_multiplication_1, Multiplication(0, 0))
        self.assertEqual(test_multiplication_2, Multiplication(5, 6))
        self.assertNotEqual(test_multiplication_2, Multiplication(0, 0))
        self.assertNotEqual(test_multiplication_2, Multiplication(5, 5))
        self.assertNotEqual(test_multiplication_2, Multiplication(6, 6))
        self.assertNotEqual(test_multiplication_2, test_addition_2)
        self.assertNotEqual(test_multiplication_2, test_subtraction_2)
        self.assertNotEqual(test_addition_2, test_subtraction_2)
        self.assertNotEqual(test_multiplication_1, [0, 0])
        self.assertNotEqual(test_multiplication_1, Answer(Multiplication(0, 0), 0))
        self.assertNotEqual(test_multiplication_1, Answer(Subtraction(0, 0), 0))
    
    def test_get_correct_answer(self):
        test_answer_1 = Answer(Multiplication(0, 0), 0)
        test_answer_2 = Answer(Multiplication(5, 6), 15)
        test_answer_3 = Answer(Addition(5, 6), 15)
        test_answer_4 = Answer(Subtraction(5, 6), 15)

        """
        Test that answer operators are correct
        """
        self.assertEqual(test_answer_1.get_correct_answer(), 0)
        self.assertEqual(test_answer_2.get_correct_answer(), 30)
        self.assertEqual(test_answer_3.get_correct_answer(), 11)
        self.assertEqual(test_answer_4.get_correct_answer(), -1)

    def test_answer_equality(self):
        test_answer_1 = Answer(Multiplication(0, 0), 0)
        test_answer_2 = Answer(Multiplication(5, 6), 15)
        test_answer_3 = Answer(Addition(5, 6), 15)
        
        """
        Test answer equality
        """
        message_test_1 = "left " + str(test_answer_1.left) + " right " + str(test_answer_1.right) + " guess " + str(test_answer_1.guess)
        self.assertEqual(test_answer_1, Answer(0, 0, 0), message_test_1)
        self.assertEqual(test_answer_2, Answer(5, 6, 15))
        self.assertNotEqual(test_answer_1, Answer(Multiplication(0, 0), 15))
        self.assertNotEqual(test_answer_2, Answer(Multiplication(5, 6), 20))
        self.assertNotEqual(test_answer_2, Answer(test_answer_3))
        self.assertNotEqual(test_answer_2, Multiplication(5, 6))

if __name__ == '__main__':
    unittest.main()