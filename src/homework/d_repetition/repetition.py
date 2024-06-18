def test_config():
    return True

def get_factorial(num):

    # Start the total at 1 so we can move from here.
    factorial_total = 1

    for value in range (0, num): 

     factorial_total = value * factorial_total 
     return factorial_total
     
     


def sum_odd_numbers(num):
    val = 0
    running_sum = 0

    # Determine if a number is odd or even using a loop
    while (val <= num):

       # If a number is odd we add it to our running total or else we skip over it.
       if (val % 2 == 1):
          running_sum += val
       val += 1
    return running_sum
    
