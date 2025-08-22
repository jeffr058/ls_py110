# Practice Problem 3
Given two sets:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
How would you obtain a set that contains all the unique values from both sets?

# Answer
a.union(b)
b |= a
c = a | b

# {1, 2, 3, 4, 5, 6}