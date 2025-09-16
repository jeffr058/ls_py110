# inputs: two lists
# output: a set
# rules: the returned set should contain elements unique to the first list
# data structure: set
# algorithm:
    # Given list1 and list2
    # Convert to sets
    # Create a new set that contains elements unique to the first set
    # Return the new set
# code:
def unique_from_first(list1, list2):
    return set(list1) - set(list2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})