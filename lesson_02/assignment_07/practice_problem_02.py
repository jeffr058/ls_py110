# Practice Problem 2
# Given the following data structure, return a new list with the same structure, but with the values in each sublist ordered in ascending order. Use a comprehension if you can. (Try using a for loop first.)

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Expected result
[['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

# The string values should be sorted as strings, while the numeric values should be sorted as numbers.

# My Answer
#1
sorted_items = []
for item in lst:
    sorted_items.append(sorted(item))
print(sorted_items)

#2
sorted_items = [sorted(item) for item in lst]
print(sorted_items)