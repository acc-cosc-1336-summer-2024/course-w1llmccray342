import unittest

from src.examples.h_strings.strings import test_config, access_chars_in_string, loop_string_w_for, loop_string_w_while
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
    

    def test_string_w_in(self):
        lang = "Python"
        result =  'th' in lang

        self.assertEqual(True, result)

        if 'th' in lang:
            print("TH is in python")

    def test_string_n_in(self):
          lang = "Python"

          self.assertEqual(True, 'Th' not in lang)


    def test_string_is_digit(self):
        num = "1234"

        self.assertEqual(True, num.isdigit())
          
    def test_string_is_lower(self):
        lang = "python"

        self.assertEqual(True, lang.islower())

    def test_string_is_alpha(self):
        lang = "ABCDEFG"

        self.assertEqual(True, lang.isalpha())
        