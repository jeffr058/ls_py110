# input: non-negative integer
# output: numeric string
# explicit:
    # no standard conversion functions
# data structure: dictionary?
# algorithm: 
    # Set `DIGITS` w/ dictionary with integer keys and numeric string values
    # Set `nums` w/ empty list
    # Set `remaining_num` w/ `integer`
    # While True
        # 1. Extract the integer in the ones place and set to `num`
            # divmod(dividend, divisor)  # returns (quotient, remainder)
            # Set `remaining_num`, `extracted_num` to divmod(`remaining_num`, 10)
        # 2. Add `num` to `nums` at first index position
        # 3. Repeat 1 & 2 until `remaining_num` equals 0
    # Set `string` w/ elements of `nums` joined together
    # Return `string`

def integer_to_string(integer):
    DIGITS = {
        0: '0', 
        1: '1', 
        2: '2', 
        3: '3', 
        4: '4', 
        5: '5', 
        6: '6', 
        7: '7', 
        8: '8', 
        9: '9',
    }
    nums = []
    remaining_num = integer
    
    while True:
        remaining_num, num = divmod(remaining_num, 10)
        nums.insert(0, DIGITS[num])
        if remaining_num == 0:
            break
    
    string = ''.join(nums)

    return string

# Convert a Number to a String
# In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. In this exercise and the next, you're going to reverse those functions.

# Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

# You may not use any of the standard conversion functions available in Python, such as str. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

# Examples
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True