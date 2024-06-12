def test_config():
    return True

def display_number(number):
    # Need a boolean expression
    i = 0
    
    while(i < number):
        print(i + 1) # We are not changing the value of index.
        # Statement that makes boolean expression false
        i += 1

# Function to determine the sum of square values
def sum_of_squares(num):
    sum = 0
    idx = 0

    while(idx <= num):
        sum += idx * idx
        idx += 1
    print(sum)
    return sum

def for_display_number(num):

    for val in range(0, num + 1):
        print(val+1)

def for_sum_of_squares(num):
    sum = 0

    for val in range(0, num):
        sum += (val + 1 ) * (val + 1)
    print(sum)
    return sum


def while_nested_loop_ex(num):
    i =  0
    
    
    while (i < num):
        print(f"Waiting for inner loop; waited {i} times")
        
        j = 0
        
        while (j <= num):
            print(j)
            j += 1

        i += 1

def while_multiplication_table(row, col):
    r = 0

    while (r < row):
        c = 0

        while (c < col):
            product = ((r + 1) * (c + 1))
            print(str(product).rjust(3, " "), end = " ")
            c += 1
        
        r += 1

        print(" ")

def for_nested_multiplication_table(row, col):
    
    for r in range(0, row):

        for c in range(0, col):
            product = (r + 1) * (c * 1)
            print(str(product).rjust(3, " "), end = " ")
        
        print(" ")


def display_menu():
        print("1 - Option 1")
        print("2 - Option 2")
        print("3 - Exit")

def user_controlled_loop():

        choice = 'Y'

        while (option != 3):
    

            option = input("Enter your menu option: ")
            choice = input("Press Y to continue: ")
    
def handle_menu_option(option):
     if(option == '1'):
        option_1()
     elif(option == '2'):
        option_2()
     elif(option == '3'):
        print("Exiting...")

def option_1():
    print("User selected option 1")
    
def option_2():
    print("User selected option 2")