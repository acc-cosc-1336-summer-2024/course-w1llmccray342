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

    
    # Check each base across the length of the variable dna1
    for base in range(len(dna1)):

        # Compare base of dna1 to dna2
        if dna1[base] != dna2[i]:
            hamming_distance += 1
        i += 1

    return hamming_distance

def  get_dna_complement(dna):

    dna_complement = ""

    a_to_replace = 0
    g_to_replace = 0
    t_to_replace = 0
    c_to_replace = 0

    # Find each instance that A, G, T, C are called.
    for value in dna:
        if "A" in value:
            a_to_replace += 1
     
        elif "C" in value:
            c_to_replace += 1

        elif "T" in value:
            t_to_replace += 1

        elif "G" in value:
            g_to_replace += 1
        
    # Use the replace method on dna_complement
    replace_a = dna_complement.replace("A", "T", a_to_replace)
    replace_c = dna_complement.replace("C", "G", c_to_replace)
    replace_t = dna_complement.replace("T", "A", t_to_replace)
    replace_g = dna_complement.replace("G", "C", t_to_replace)

    # Debug statement.
    print(replace_a, replace_c, replace_t, replace_g)
    dna_complement += replace_t + replace_g + replace_c + replace_a

    print(dna_complement)
    return dna_complement


    
    
    

    # If we are finding the reverse complement then for ACCCGGTT we need to return AACCGGGT
    # Grab values starting from negative indext
    