#

def get_hamming_distance(dna1, dna2):
    # Comparing two strings against each other
    # For each different letter in the comparative sequence we should store a value of 1
    # Some way to make sure that DNA1 and DNA2 can't go above 1000 base pairs.

    # Initialize a variable, hamming_distance
    hamming_distance = 0
    i = 0 
    

    for base in dna1:
        print(base)

    for base in dna2:
        print(base)    

    
    return hamming_distance



    return hamming_distance

def  get_dna_complement(dna1, dna2):
    pass
    # String formed by reversing the symbols of dna1 and storing them into dna2