import unittest

from src.examples.c_decisions.decisions import test_config, is_number_in_range

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_number_in_a_range(self):
        self.assertEqual(True, is_number_in_range (1, 1, 10))
        self.assertEqual(False, is_number_in_range(0, 1, 10))
        self.assertEqual(True, is_number_in_range(5, 1, 10))

