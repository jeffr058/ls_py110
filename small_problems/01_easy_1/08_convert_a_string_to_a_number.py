# inputs: string of digits
# outputs: RETURNED integer of digits
# explicit: 
    # don't use standard conversion functions (e.g., int())
    # assume all chars are numeric
# implicit: 
# questions: 
# data structures: list
# algorithm: 
    # Separate digits in `string` and add to `integers` list
    # Convert digits to `integers`
    # Compute integers according to their place values
        # Set `decuple` to 1 and set `place_values` to []
        # For each `integer` in `integers` in reverse order:
            # 1. Multiply `integer` by `decuple`
            # 2. Multiply `decuple` by 10
            # 3. Append `integer` to `place_values`
    # Set `result` to sum of elements in `integers`
    # Return `result`
# code: 
def calc_place_values(integers):
    decuple = 1
    place_values = []

    for integer in integers[::-1]:
        place_values.append(integer * decuple)
        decuple *= 10
    
    return place_values

def string_to_integer(string):
    integers = [int(digit) for digit in string]
    
    result = sum(calc_place_values(integers))

    return result

# Convert a String to a Number
# Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as int. Your function should calculate the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.

# Examples
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
print(string_to_integer("5702134567") == 5702134567)    # True
print(string_to_integer("0") == 0)    # True
# Hint
# To compute an integer value from a string of digits, you should know that the rightmost digit is the "ones" digit; that is, it contributes its value to the overall result. If there's another digit to the left of that digit, that digit is the "tens" digit; it contributes its value times 10 to the overall result.

# To convert a string like "5372" to an integer, you need to understand how our decimal numbers work. In this case, 2 is in the "ones" position, 7 is in the tens position, 3 in the hundreds position, and 5 in the thousands position:

# digits	5	3	7	2
# ones				2
# tens			70	
# hundreds		300		
# thousands	5000			
# Thus, we can calculate the numeric value of "5372" as 5000 + 300 + 70 + 2, or 5372.