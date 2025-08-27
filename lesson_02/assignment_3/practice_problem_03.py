# Practice Problem 3
# Repeat problem 2 but, this time, sort the list as string values. Both the list passed to the sorting function and the returned list should contain numbers, not strings.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

# Expected result
# [-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort
# [9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort

# My Answer
lst.sort(key=str)
print(lst == [-16, -6, 10, 11, 50, 7, 8, 9])

lst.sort(key=str, reverse=True)
print(lst == [9, 8, 7, 50, 11, 10, -6, -16])