def test_config():
    return True

def get_factorial(num):

    factorial_total = 0

    for value in range (0, num):
     
     # Factorial of 0 is "1!"
     if num == 0:
        factorial_total = 1
     
     factorial_total *= value
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
    
