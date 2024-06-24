import array

def test_config():
    return True

def create_array():
    nums = array.array('i', [6, 1, 3, 10, 15])


    for num in range(0, len(nums)):
        print(nums[num])
