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

    try:
        num1 = int(input("Enter num1: "))
        num2 = int(input("Enter num2: "))

        result = num1 * num2
        print(result)

    except ValueError:
        print("ERROR: Values must be numeric")

def multiply_two_numbers_using_loops():

    num1 = ''
        
    while not num1.isdigit():
        num1 = input("Please enter digits.. Enter num1: ")
        
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    result = num1 * num2
    print(result)

def open_file_for_reading(file_name):
    try: 
        file = open(file_name, 'r')

        contents = file.read()
        file.close()

    except IOError:
        print("Cannot read file, location not found")

def open_sales_file_for_reading(sales_file_name):
    
    try:
        
        file = open(sales_file_name, 'r')
        
        total = 0 

        for line in file:
            amount = int(line)
            total += amount

        file.close()
    
    except ValueError:
        print("File contains invalid data") # For the enduser display this
        # Save error contents to error log

