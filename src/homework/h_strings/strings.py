#

# Function to check if dna1 and dna2 are valid integers
def check_if_valid(dna1, dna2):

    if len(dna1) != len(dna2):
        print("Invalid sequence, Error")
    
    if len(dna1) < 0 or len(dna1) > 1000:
        print("Invalid sequence, Error")

    if len(dna2) < 0 or len(dna2) > 1000:
        print("Invalid sequence, Error")
    
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
   
   # In order to get this to work we have to take the data set and flip it.
   # Use a for loop to return the values of the opposite, then use another for loop to flip those values.
   # Append each value as we go through.
   # Then we flip the values in it.
   # If we are finding the reverse complement then for ACCCGGTT we need to return AACCGGGT

  dna_complement = ""

  #Flip the DNA sequence
  dna_reverse = dna[::-1]

  #Iterate through each base in the reverse sequence, if a base is detected make sure to append its complement instead.
  for base in dna_reverse:
      if base == "A":
          dna_complement += "T"
      elif base == "T":
          dna_complement += "A"
      elif base == "G":
          dna_complement += "C"
      elif base == "C":
          dna_complement += "G"
  
  return dna_complement
          


       
           
       

       
    

   
       

       
              
       



    
    
    

  
    # Grab values starting from negative indext
    