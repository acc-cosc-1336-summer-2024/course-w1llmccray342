
# For two strings s1 and s2 of equal length, the p-distance between them, 
# denoted dp(s1,s2), is the proportion of corresponding symbols that differ between s1 and s2.

# That is our distance between the two lists should be 
  # We need to get the hamming distance between our lists
  # We need to get the number of items in our lists
  # We divide our the hamming distance that is generated by the total number of items in our lists
  # Completed function move on to get_p_distance_matrix
def get_p_distance(list1, list2):

    hamming_distance = 0
    count = 0

    if len(list1) == len(list2):

        for item in list1:
            if item not in list2[count]:
                hamming_distance += 1
            count += 1
            print(hamming_distance, count)
    
        p_distance = hamming_distance / count
        
        print(f"P Distance is {p_distance}")
        return p_distance

    
    else:
        print("Mismatch, ERROR")
        return False
    

# For a general matrix distance function d on n taxa s1,s2,…,sn (taxa are often represented by genetic strings), 
# we may encode the distances between pairs of taxa via a distance matrix D in which Di,j=d(si,sj).

# Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given
# in FASTA format.
# Return: The matrix D corresponding to the p-distance dp on the given strings. 
# As always, note that your answer is allowed an absolute error of 0.001.

# Take the first two indexes
def get_p_distance_matrix(parameter):
    p_distance_matrix = []
    # For the range of DNA strings compare each string to each index available
    # DNA 1 -> 4 on each string
    for dna_sequence in parameter:
        dna_sequence_list =[]

        i = range(len(parameter))
        my_loop = 0
        
        while my_loop < i and not my_loop > i:
            p_distance = get_p_distance(dna_sequence, i)
            dna_sequence_list.append(p_distance)
            print(type(i, dna_sequence))
            my_loop += 1
            
        print(dna_sequence_list)
            
    p_distance_matrix.append(dna_sequence_list)
    print(p_distance_matrix)
