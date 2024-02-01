
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
    ints(list): list of integers containing one or more integers
    """
    
    # keep track of max and min each iteration
    _max = None
    _min = None

    for n in ints:
        # in the beginning just assign max and min to the first element
        if _min is None and _max is None:
            _min = n
            _max = n

        # if the new number is smaller than the min, itself becomes the min
        if n < _min:
            _min = n
        
        # if the new number is bigger than the max, itself becomes the max
        if n > _max:
            _max = n

    return (_min, _max)


### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Only negative
l = [i for i in range(-180, -2)]  # a list containing -180 - -3
random.shuffle(l)
print ("Pass" if ((-180, -3) == get_min_max(l)) else "Fail")

# negative and positive
l = [i for i in range(-180, 127)]  # a list containing -180 - 126
random.shuffle(l)
print ("Pass" if ((-180, 126) == get_min_max(l)) else "Fail")

# ints with repetitions
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
l.append(4)
l.append(8)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")