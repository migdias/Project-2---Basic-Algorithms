def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int | str: Floored Square Root
    """
    if not isinstance(number, int):
        return None

    isNeg = False
    if number < 0:
        number = abs(number)
        isNeg = True

    # in case 0 and 1
    if number == 0 or number == 1:
        return number
    
    # keep track of which intervals in order to cut the right place
    start = 0
    end = number
    
    # calculate mid number
    mid = number // 2
    while True:

        # calculate power2 and the power2 of the next number of mid.
        # the idea is that if the power2 is smaller than number and power2_next is bigger then we found our result
        power_mid = mid*mid
        power_mid_next = (mid+1)*(mid+1)
        #print(f'Mid: {mid}, Power2: {power_mid}, Power2 + 1: {power_mid_next}')

        # if the mid has been found then return right away
        # if the result is on the mid+1 return
        # if the power2 is smaller than number and power2_next is bigger then we found our result
        if (power_mid_next == number):
            if isNeg:
                return f'{mid+1}i'
            else:
                return mid+1

        if (power_mid == number) or ((power_mid < number and power_mid_next > number)):
            if isNeg:
                return f'{mid}i'
            else:
                return mid
        
        # otherwise keep separating the number based on the power2 result. If power2 < number then we search the mid on the left side
        # else we search on the right size
        if power_mid < number: # new mid on left side
            start = mid 
        else:
            end = mid

        # find the index of the new mid
        mid = (end + start) // 2

        #print(f'new_mid = {mid}, start-end: {start}-{end}')

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Edge Cases
print ("Pass" if (910716 == sqrt(829405278394)) else "Fail")
print ("Pass" if not sqrt('test') else "Fail")
print ("Pass" if  ('3i' == sqrt(-9)) else "Fail")
print ("Pass" if  ('5i' == sqrt(-27)) else "Fail")
print ("Pass" if  (sqrt(None) is None) else "Fail")