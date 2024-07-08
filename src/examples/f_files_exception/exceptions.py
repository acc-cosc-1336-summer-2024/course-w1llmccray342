def test_config():
    return True

def divide_two_numbers(num1, num2):
    
    result = 0

    if num2 != 0:
        result = num1 / num2
    
    else:
        return "No integer is divisible by 0; ERROR"
    
    return result 

def multiply_two_numbers():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    result = num1 * num2

    return result