def test_config():
    return True

def display_number(number):
    # Need a boolean expression
    i = 0
    
    while(i < number):
        print(i + 1) # We are not changing the value of index.
        # Statement that makes boolean expression false
        i += 1
    print(f"display_number ran {i} times!")

# Function to determine the sum of square values
def sum_of_squares(num):
    sum = 0
    idx = 0

    while(idx <= num):
        sum += idx * idx
        idx += 1
    print(f"The sum of squares is {sum}")
