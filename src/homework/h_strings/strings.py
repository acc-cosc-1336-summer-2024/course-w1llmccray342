#

def get_hamming_distance(dna1, dna2):
    # Comparing two strings against each other
    # For each different letter in the comparative sequence we should store a value of 1

    hamming_distance = 0

    for char in dna1:
        for char2 in dna2:
            if char != char2:
                hamming_distance += 1

    return hamming_distance

def  get_dna_complement(dna1, dna2):
    pass
    # String formed by reversing the symbols of dna1