# Practice Problem 7
# Given the following data structure return a new list identical in structure to the original, but containing only the numbers that are multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# The returned list should look like this:

# Expected result
[[], [3, 12], [9], [15, 18]]

# Try to use a comprehension for this. However, we recommend first trying it without comprehensions.

# input: nested list
# output: return new list w/ multiples of 3 only
# implicit: have same number of nested lists
# multiples_of_three = []
# for idx, sublist in enumerate(lst):
#     multiples_of_three.append([])
#     for num in sublist:
#         if num % 3 == 0:
#             multiples_of_three[idx].append(num)
# algorithm:
    # add a nested list for each `sublist` in `lst`
        # output expression is a list
        # add num to the output list if num is multiple of 3
    # if the number in the `sublist` is a multiple of 3
        # add the multiple to the nested list
# code:
multiples_of_three = [[num 
                       for num in sublist 
                       if num % 3 == 0] 
                       for sublist in lst]

print(multiples_of_three == [[], [3, 12], [9], [15, 18]])