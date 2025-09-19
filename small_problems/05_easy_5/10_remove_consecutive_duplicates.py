'''Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. Return the refined sequence.
I: sequence of integers
O: sequence of successive repeated values filtered out

D: list

A:
- Given sequence of integers
- Create new sequence with successive repeated values filtered out
    - Create new_sequence and set to empty list
    - For each integer in sequence
        - If integer is at idx 0 or does not equal the last value in new_sequence
            - Add integer to new_sequence
    - (For comprehension: if idx is 0 or integer does not equal the value at idx before it)
- Return new_sequence
'''
def unique_sequence(sequence):
     return [
          integer for idx, integer in enumerate(sequence) 
                  if idx == 0 or integer != sequence[idx - 1]]
    # new_sequence = []
    # for idx, integer in enumerate(sequence):
    #     if idx == 0 or integer != new_sequence[-1]:
    #         new_sequence.append(integer)

    # return new_sequence

# Example
original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
print(unique_sequence([]) == [])      # True