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

    

