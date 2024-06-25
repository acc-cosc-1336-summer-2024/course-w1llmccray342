import unittest

from src.examples.g_lists_and_tuples.lists import test_config

class Test_Config(unittest.TestCase):

    # Always prefix with 'test_'
    
    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_create_empty_list(self):
        list_a = []
        list_a.append(10)

        self.assertEqual(True, [10] == list_a)

    def test_find_item_in_a_list(self):
        list_b = [2, 4, 6, 8, 10]
        found = 2 in list_b

        self.assertEqual(True, found)

    def test_item_not_in_list(self):
        list_c = [2, 4, 6, 8, 10]

        self.assertEqual(True, 11 not in list_c)

