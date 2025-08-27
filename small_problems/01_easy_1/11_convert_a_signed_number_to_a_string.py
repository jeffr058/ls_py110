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

def integer_to_string(number):
    nums = []
    remaining_num = number
    
    while True:
        remaining_num, num = divmod(remaining_num, 10)
        nums.insert(0, DIGITS[num])
        if remaining_num == 0:
            break
    
    return ''.join(nums)

def signed_integer_to_string(number):
    numeric_string = integer_to_string(abs(number))

    if number > 0:
        return '+' + numeric_string
    elif number < 0:
        return '-' + numeric_string
    else:
        return numeric_string

# Convert a Signed Number to a String
# In the previous exercise, you developed a function that converts non-negative numbers to strings. In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

# Write a function that takes an integer and converts it to a string representation.

# You may not use any of the standard conversion functions available in Python, such as str. You may, however, use integer_to_string from the previous exercise.

# Examples
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True