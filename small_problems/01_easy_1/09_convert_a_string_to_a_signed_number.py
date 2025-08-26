# inputs: string of digits
# outputs: integer of digits
# explicit:
    # if string has leading + or no sign, return positive integer
    # if string has leading -, return negative integer
    # string will always contain valid number
    # don't use any standard conversion functions
    # you can use string_to_integer()
# implicit: 
# questions:
    # is 0 a valid number?
# data structure: 
# algorithm:

    # remove sign from string
        # set clean_string w/ string that has + or - stripped
        # set sign w/ '+' or '-'
            # sign = string[0]
    # convert string to integer
        # pass clean_string to helper function
    # compute integer as positive or negative
        # match sign with appropriate action
            # if sign is -, make integer negative
            # if sign is +, leave integer positive
    # return integer

# code: 

def string_to_integer(string):
    DIGITS = {
        '0': 0, 
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    value = 0
    for char in string:
        value = (10 * value) + DIGITS[char]
    
    return value

def string_to_signed_integer(string):
    clean_string = string.lstrip('+-')

    integer = string_to_integer(clean_string)
    
    match string[0]:
        case '-': return -integer
        case _: return integer

# Convert a String to a Signed Number
# In the previous exercise, you developed a function that converts simple numeric strings to integers. In this exercise, you're going to extend that function to work with signed numbers.

# Write a function that takes a string of digits and returns the appropriate number as an integer. The string may have a leading + or - sign; if the first character is a +, your function should return a positive number; if it is a -, your function should return a negative number. If there is no sign, return a positive number.

# You may assume the string will always contain a valid number.

# You may not use any of the standard conversion functions available in Python, such as int. You may, however, use the string_to_integer function from the previous exercise.

# Examples
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True