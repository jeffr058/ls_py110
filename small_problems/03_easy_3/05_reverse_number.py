# inputs: positive integer
# outputs: integer w/ digits reversed
# implicit rules: 
    # single digit returns same single digit
    # trailing zeros are removed
# data structure: maybe list
# algorithm:
    # Given an integer
    # Reverse the order of integer
        # Convert integer to string
        # Reverse the order of the string
            # Slicing entire string with negative step
        # Convert back to integer
    # Return the result
# code:
def reverse_number(integer):
    return int(str(integer)[::-1])

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True