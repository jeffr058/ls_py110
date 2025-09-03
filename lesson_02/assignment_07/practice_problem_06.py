# Practice Problem 6
# Given the following data structure, return a new list identical in structure to the original but, with each number incremented by 1. Do not modify the original data structure. Use a comprehension.

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# Expected result
[{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

# My Answer
# new_lst = []
# for dct in lst:
#     new_lst.append(dct)
#     for key, value in dct.items():
#         dct[key] = value + 1

new_lst = [{letter: num + 1 
            for letter, num in dct.items()} 
           for dct in lst]
print(new_lst)