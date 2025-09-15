# inputs: count, starting num
# output: list
# explicit rules:
    # list has same num of elements as count
    # each element s/b multiple of starting num
    # count >= 0
    # starting num can be any integer
    # if count is 0, return an empty list
# implicit rules:
# data structure: list
# algorithm:
    # Given count and starting_num
    # Create a list of elements from starting_num and incrementing by starting_num until the length of list equals count
        # Set sequence = []
        # Set running_multiple to starting_num
        # For each iteration in range of count
            # Add starting_num to sequence
            # Add starting_num to running_multiple
    # Return sequence
# code:
def sequence(count, starting_num):
    sequence_lst = [starting_num * num for num in range(1, count + 1)]
    return sequence_lst

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True