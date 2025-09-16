# inputs: two lists
# output: a set
# explicit rules:
    # convert lists to sets
    # output set is union of both sets
# implicit rules:
    # create a function
# data structure: set
# algorithm:
    # Given list1 and list2
    # Convert lists to sets
    # Create a new set containing members of both sets
    # Return the new set
# code:
def merge_sets(list1, list2):
    return set(list1) | set(list2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True