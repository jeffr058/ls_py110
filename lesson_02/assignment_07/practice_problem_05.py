# Practice Problem 5
# Given the following data structure, sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain. You shouldn't mutate the original list.

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
# Note that the first sublist has the odd numbers 1 and 7; the second sublist has odd numbers 1, 5, and 3; and the third sublist has 1 and 3. Since (1 + 3) < (1 + 7) < (1 + 5 + 3), the sorted list should look like this:

# Expected result
[[1, 8, 3], [1, 6, 7], [1, 5, 3]]
# Try to use a comprehension in your solution.

# My Answer
def add_odds(nums):
    return sum([num for num in nums if num % 2 == 1])

new_lst = sorted(lst, key=add_odds)