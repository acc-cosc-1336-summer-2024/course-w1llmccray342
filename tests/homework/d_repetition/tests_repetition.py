import unittest
from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

class Test_Congfig(unittest.TestCase):

    def test_get_factorial(self):
        self.assertEqual(1, get_factorial(0))
        self.assertEqual(24, get_factorial(4))
        self.assertEqual(120, get_factorial(5))
        self.assertEqual(720, get_factorial(6))


    def test_sum_odd_numbers(self):
        self.assertEqual(16, sum_odd_numbers(7))
        self.assertEqual(25, sum_odd_numbers(9))
        self.assertEqual(25, sum_odd_numbers(10))
        self.assertEqual(36, sum_odd_numbers(11))