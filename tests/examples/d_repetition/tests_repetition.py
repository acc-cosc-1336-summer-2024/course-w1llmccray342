import unittest

from src.examples.d_repetition.repetition import test_config, display_number, sum_of_squares

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_sum_of_squares(self):
        self.assertEqual(14, sum_of_squares(3))
       
    def test_sum_of_squares_1(self):
        self.assertEqual(5, sum_of_squares(2))
    
    def test_sum_of_squares_2(self):
        self.assertEqual(55, sum_of_squares(5))
    
    def test_sum_of_squares_3(self):
        self.assertEqual(91, sum_of_squares(6))