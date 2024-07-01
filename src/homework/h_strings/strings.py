#

def get_hamming_distance(dna1, dna2):
    # Comparing two strings against each other
    # For each different letter in the comparative sequence we should store a value of 1

    hamming_distance = 0
    i = 0 

    # Iterate through each character in dna1
    for char in dna1[i]:

        # If char in dna1 matches the char in dna2
        if char in dna1[i] == char in dna2[i]:
            # Increment hamming distance + 1
            hamming_distance += 1
        i += 1
    
    return hamming_distance



    return hamming_distance

def  get_dna_complement(dna1, dna2):
    pass
    # String formed by reversing the symbols of dna1 and storing them into dna2