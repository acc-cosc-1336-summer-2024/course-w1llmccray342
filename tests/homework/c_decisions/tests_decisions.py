import unittest
from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

class Test_Congfig(unittest.TestCase):

    # Create test case for get_options_ratio
    def test_get_options_ratio(self):
        self.assertEqual(.25, get_options_ratio(5, 20))
        self.assertEqual(.5, get_options_ratio(10, 20))
        self.assertEqual(.75, get_options_ratio(30, 40))

    # Create a test case for get_faculty_rating
    # Test each possible condition.
    # Added test cases for possible error conditions.
    def test_get_faculty_rating(self):
        self.assertEqual("Excellent", get_faculty_rating(.91))
        self.assertEqual("Very Good", get_faculty_rating(.85))
        self.assertEqual("Good", get_faculty_rating(.71))
        self.assertEqual("Needs Improvement", get_faculty_rating(.66))
        self.assertEqual("Unacceptable", get_faculty_rating(.45))
        self.assertEqual("Error", get_faculty_rating(1.01))
        self.assertEqual("Error", get_faculty_rating(-.9))
        self.assertEqual("Error", get_faculty_rating(1))