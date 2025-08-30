# Multiply Lists
# Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain the same number of elements.

#1
def multiply_list(lst1, lst2):
    new_list = []
    for idx in range(len(lst1)):
        new_list.append(lst1[idx] * lst2[idx])
    return new_list

#2
def multiply_list(lst1, lst2):
    new_list = [item1 * item2 for (item1, item2) in zip(lst1, lst2)]
    return new_list

# Example
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True