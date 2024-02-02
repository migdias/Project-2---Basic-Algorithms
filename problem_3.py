def mergesort(items):

    if len(items) <= 1:
        return items
    
    ## Divide and conquer recursive
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    # recall for left and right. At the end we will have arrays with one element
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]: # we dont want to order normally so we create a custom order
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(arr):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # first we use the normal merge sort from class: O(n log n)
    sorted_arr = mergesort(arr)

    # not that we have them sorted we know that the sum of two numbers always need to have the 
    # maximum available number on the first indexes. Therefore:
    # Number1: Starts with largest number (index: -1). The same logic applies for the other numbers. For each takes the next index - 2
    # Number2: Starts with second largest number (index: -2) The same logic applies for the other numbers. For each takes the next index - 2
    # Example: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #   Number 1: 97531
    #   Number 2: 86420

    number1 = int(''.join(map(str, sorted_arr[-1::-2])))
    number2 = int(''.join(map(str, sorted_arr[-2::-2])))

    return [number1, number2]



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[9, 9, 9, 9], [99, 99]])
test_function([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [97531, 86420]])
test_function([[1, 9, 1, 9, 1, 9, 5, 9], [9951, 9911]])

