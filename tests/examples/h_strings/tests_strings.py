import unittest

from src.examples.h_strings.strings import test_config, access_chars_in_string

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_access_chars_in_string(self):
        lang = "Python"

        self.assertEqual("P", lang[0])
        self.assertEqual("y", lang[1])
        self.assertEqual("t", lang[2])
        self.assertEqual("h", lang[3])
        self.assertEqual("o", lang[4])
        self.assertEqual("n", lang[5])

    def test_len_of_string(self):
        lang = "Python"

        self.assertEqual(6, len(lang))
        

