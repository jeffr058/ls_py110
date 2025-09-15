# input: positive integer
# output: list of all integers between 1 and input (inclusive)
# implicit rule: single digit integer in a list by itself
# data structure = list
# algorithm:
    # Given a positive integer
    # Add each integer between 1 and integer (inclusive) to list
        # Create range with start of 1 and end of integer + 1
    # Return result
# code:
def sequence(integer):
    return list(range(1, integer + 1))

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True