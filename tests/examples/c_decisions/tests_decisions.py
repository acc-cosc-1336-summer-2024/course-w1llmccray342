import unittest

from src.examples.c_decisions.decisions import get_generation, is_number_not_in_range, test_config, is_number_in_range

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_number_in_a_range(self):
        self.assertEqual(True, is_number_in_range (1, 1, 10))
        self.assertEqual(False, is_number_in_range(0, 1, 10))
        self.assertEqual(True, is_number_in_range(5, 1, 10))

    def test_if_number_not_in_range(self):
        self.assertEqual(True, is_number_not_in_range(0, 1, 10))
        self.assertEqual(False, is_number_not_in_range(5, 1, 10))
        self.assertEqual(True, is_number_not_in_range(11, 1, 10))

    def test_get_generation(self):
        self.assertEqual('Unknown Generation', get_generation(2222))
        self.assertEqual('Centennial', get_generation(2000))
        self.assertEqual('Millennial', get_generation(1990))
        self.assertEqual('Gen X', get_generation(1970))
        self.assertEqual('Baby Boomer', get_generation(1961))
        self.assertEqual('Unknown Generation', get_generation(1875))