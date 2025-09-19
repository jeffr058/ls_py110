'''
I didn't know why it would raise an error but found out that a set, as the loop variable, cannot change size during iteration.

One way to fix this is to coerce the set to a list and using the list as the loop variable and then coercing the list back to a set. Another way is to create a new set to add the set items that are odd, and this can be cleanly done with a set comprehension.

data_set = {1, 2, 3, 4, 5}

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)
'''
data_set = {1, 2, 3, 4, 5}

new_data_set = {item for item in data_set if item % 2 == 1}