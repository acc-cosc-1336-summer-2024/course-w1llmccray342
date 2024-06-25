import unittest

from src.examples.g_lists_and_tuples.lists import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def create_empty_list(self):
        list = []
        list.append(10)

        self.assertEqual(True, [10] == list)

    def find_item_in_a_list(self):
        list = [2, 4, 6, 8, 10]

        self.assertEqual(True, )

