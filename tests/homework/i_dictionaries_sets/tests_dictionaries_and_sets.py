import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance

class Test_Config(unittest.TestCase):

    def test_get_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        self.assertEqual(.4, get_p_distance(list1, list2))

    def test_get_p_distance_matrix(self):
        pass