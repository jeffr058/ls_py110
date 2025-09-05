# Double Char (Part 1)
# Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

# input: string
# output: string w/ each char doubled
# implicit: empty string returns empty string
# examples: provided
# data structure: none
# algorithm:
    # Given `string`
    # Double every char in `string`
        # Set `result` to empty string
        # For each char in `string`
            # Multiply char by 2 and add to `result`
    # Return `result`
# code:
import pdb
def repeater(string):
    result = ''
    for char in string:
        result += char * 2
    return result

# Examples
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True