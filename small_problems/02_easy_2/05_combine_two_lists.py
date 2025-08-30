# Combine Two Lists
# Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.

# You may assume that both input lists are non-empty, and that they have the same number of elements.

def interleave(lst1, lst2):
    alternating_elements = []
    lst_of_tuples = list(zip(lst1, lst2))
    for items in lst_of_tuples:
        alternating_elements.extend(list(items))
    return alternating_elements

# # Example
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True