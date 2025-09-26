'''
Summary: Get the square of the sum of the "first `count` integers", the sum of the squares of the "first `count` integers", and compute the differnce between the results. 
Input: integer
Output: integer (difference)
Rules:
    - integer arg will be positive
    - 1 is the only count, so return is 0 (there is no difference)
    - "first `count` integers": each integer from 1 to integer arg, inclusive

Data structure: probably a list to store the "first `count` integers"

Algorithm:
- Given an integer
- Get the "first `count` integers"
    - IDEA 1: add the integers to a list (helper function?) to then get the two different values
        - Helper function: get_first_count_integers()
            - input: integer
            - output: list of integers
            - data structure: list
    - IDEA 2: add the integers to a list twice (for each), since squaring each integer can be combined with adding "first `count` integers" to a list
- Get their sum and get the square
- Square each integer and get the sum
- Get the difference and return the result
'''
def sum_square_difference(integer):
    first_count_integers = range(1, integer + 1)

    sum_square = sum(first_count_integers) ** 2
    
    square_sum = sum([num ** 2 for num in first_count_integers])
    
    return sum_square - square_sum

# Examples
print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True