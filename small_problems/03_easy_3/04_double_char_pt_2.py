# Double Char (Part 2)
# Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

# You may assume that only ASCII characters will be included in the argument.

# input: string
# output: string that doubles every consonant in string
# explicit:
    # don't double vowels or non-letter chars
    # will only ASCII chars included in args
# data structure: list?
# algorithm:
    # Given `string`
    # Double only every consonant in `string`
        # Non-consonants occur once
    # Return result

def double_consonants(string):
    result = ''
    for char in string:
        if char.lower() in 'bcdfghjklmnpqrstvwxyz':
            result += char * 2
        else:
            result += char
    return result

# Examples
# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")