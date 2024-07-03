import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
        
    def test_students_in_base_ball_and_basketball(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])


        expected_set = set(['Jodi', 'Carmen', 'Eva', 'Aida', 'Alicia', 'Sarah'])
        both_sports = baseball.union(basketball)

        self.assertEqual(both_sports, expected_set)
        
    def test_students_in_baseball_but_not_in_basketball(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

        expected_set = set(['Jodi', 'Aida'])
        only_baseball = baseball.difference(basketball)

        self.assertEqual(expected_set, only_baseball)

    def test_students_who_play_only_one_sport(self):
        baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

        expected_set = set(['Jodi', 'Aida', 'Eva', 'Sarah'])
        both_sports_set = baseball.symmetric_difference(basketball)

        self.assertEqual(expected_set, both_sports_set)

        

