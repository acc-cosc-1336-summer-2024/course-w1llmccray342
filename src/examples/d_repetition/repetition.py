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
