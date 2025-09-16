# inputs: two lists
# outputs: frozen set
# rules: 
    # convert lists to frozen sets
    # create frozen set that has common elements of frozen sets
# data structure: frozen set
# algorithm:
    # Given two lists
    # Convert lists to frozen sets
    # Create new frozen set that has common elements of frozen sets
    # Return new frozen set
# code:
def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True