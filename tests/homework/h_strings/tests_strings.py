#
import unittest
from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        dna1 = "ACABGGAC"
        dna2 = "BCCAGGAA"
    
        self.assertEqual(4, get_hamming_distance(dna1, dna2))
        self.assertEqual(7, get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
        self.assertNotEqual(5, get_hamming_distance("GAG", "GAG"))


    def test_get_dna_complement(self):
        dna = "SELF"
        self.assertEqual("SELF", get_dna_complement(dna))
    
