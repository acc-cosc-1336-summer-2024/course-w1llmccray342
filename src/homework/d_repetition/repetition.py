def test_config():
    return True


def get_factorial(num):
        
    product_factorial = 1
        
    for i in range(0, num):
        product_factorial += product_factorial * i
        print(product_factorial)
        
    return product_factorial

    

     


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
    
