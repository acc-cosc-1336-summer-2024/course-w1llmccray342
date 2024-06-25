import array

def test_config():
    return True

def create_array():
    nums = array.array('i', [6, 1, 3, 10, 15])

    nums.append(4)
    nums.insert(2, 0)


    for num in range(0, len(nums)):
        print(nums[num])


def create_list():
    # Index 0, 4
    nums = [2, 4, 6, 8, 10]

    print(nums[0])
    print(nums[1])
    print(len(nums))

    print("Iterate w for loop")
    
    for i in range(0, len(nums)):
        print(nums[i])

def loop_list_w_while():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    indx = 0

    while(indx < nums[-1]):
        print(nums[indx])
        indx += 1

def use_different_data_types_in_a_list():
    items = [1, 2.5, "fish", True, "python"]

    # Iterate through list
    for i in items:
        print(i)

def return_sum_of_items(self):
    items = [1, 10, 5, 15, 25, 20]
    sum_total = 0

    for item in items:
        sum_total += item

    return sum_total


