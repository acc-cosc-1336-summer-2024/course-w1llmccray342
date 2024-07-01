#
import unittest
from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        dna1 = "ACABGGAC"
        dna2 = "BCCAGGAA"
    
        self.assertEqual(4, get_hamming_distance(dna1, dna2))


    def test_get_dna_complement(self):
        pass
