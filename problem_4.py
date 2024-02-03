def sort_012(arr):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       arr(list): List to be sorted
    """
    
    # zeroes must be in the beginning
    zero_index = 0

    # twos must always be at the end
    two_index = len(arr) - 1

    # start traversing from beginning
    front_index = 0

    while front_index <= two_index:
        if arr[front_index] == 0:
            arr[front_index] = arr[zero_index]
            arr[zero_index] = 0
            zero_index += 1
            front_index += 1
        elif arr[front_index] == 2:
            arr[front_index] = arr[two_index]
            arr[two_index] = 2
            two_index -= 1
        else:
            front_index += 1

    return arr
    
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 2, 0, 0, 0, 2])

# Edge cases
test_function([0, 0, 0, 0, 0, 0, 0, 0]) # only zeroes
test_function([ 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) # no zeroes
test_function([1, 1, 1, 1, 1]) # only ones
test_function([2, 2, 2, 2, 2]) # only twos
test_function([]) # Nothing