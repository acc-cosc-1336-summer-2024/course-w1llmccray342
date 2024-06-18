def test_config():
    return True

def get_factorial(num):

    factorial_count = 0

    for value in range (0, num):
       # Factorial of 0 is always 1 so if num gets "0" as a value have it return 1
        if num == 0:
            factorial_count = 1
            
        
        factorial_count *= num
        return factorial_count


def sum_odd_numbers(num):
    val = 0
    running_sum = 0

    # Determine if a number is odd or even using a loop
    while (val < num):

       if (val % 1 == 0):
          running_sum += val
       val += 1
    return running_sum
    
