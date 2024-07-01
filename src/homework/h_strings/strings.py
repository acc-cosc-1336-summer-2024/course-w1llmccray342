#

# Function to check if dna1 and dna2 are valid integers
def check_if_valid(dna1, dna2):

    if len(dna1) != len(dna2):
        print("Invalid base pairs, Error")
    
    if len(dna1) < 0 or len(dna1) > 1000:
        print("Invalid base pairs, Error")

    if len(dna2) < 0 or len(dna2) > 1000:
        print("Invalid base pairs, Error")
    
    return False


def get_hamming_distance(dna1, dna2):


    # Comparing two strings against each other
    # For each different letter in the comparative sequence we should store a value of 1
    # Some way to make sure that DNA1 and DNA2 can't go above 1000 base pairs.

    # Initialize a variable, hamming_distance
    hamming_distance = 0
    i = 0 

    check_if_valid(dna1, dna2)
    
    # Check each base across the length of the variable dna1
    for base in range(len(dna1)):

        # Compare base of dna1 to dna2
        if dna1[base] != dna2[i]:
            hamming_distance += 1
        i += 1
        print(hamming_distance)

    return hamming_distance


    
    return hamming_distance



    return hamming_distance

def  get_dna_complement(dna1, dna2):

    check_if_valid(dna1, dna2)
    pass
    # String formed by reversing the symbols of dna1 and storing them into dna2



    