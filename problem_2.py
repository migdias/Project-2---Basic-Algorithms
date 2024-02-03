def rotated_array_search(arr, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
        input_list(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """

    start = 0
    end = len(arr) - 1

    
    while start <= end:
        mid = (end + start) // 2
        mid_elem = arr[mid]

        if (mid_elem == number):
            return mid

        # if sorted left
        if (arr[start] < arr[mid - 1]):
            # number could be there use left sublist
            if (arr[start] <= number <= arr[mid-1]): 
                end = mid + 1
            else: # use right unsorted list to perform modified binary search
                start = mid - 1

        # if sorted right           
        if (arr[end] > arr[mid + 1]):
            # if right could have number
            if (arr[mid + 1] <= number <= arr[end]):
                start = mid + 1
            else:
                end = mid - 1

        
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge cases
test_function([[1, 2, 3, 4, 5, 6, 7], 3]) # not rotated
test_function([[], 3]) # Empty list
test_function([[3], 3]) # list with one item