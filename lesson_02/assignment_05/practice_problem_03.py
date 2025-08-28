# Practice Problem 3
# Given the following code, what will the final values of a and b be? Try to answer without running the code.

a = 2
b = [5, 8]
lst = [a, b]  # [2, [5, 8]]

lst[0] += 2  # [4, [5, 8]]
lst[1][0] -= a  # [4, [3, 8]]

# My Answer
print(a == 2)
print(b == [3, 8])