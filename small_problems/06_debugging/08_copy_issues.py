'''
I think the end value of `copied[0]` is `[99]`, which is why the output is `False`. The reason the copied list is affected is that `copy()` from the `copy` module creates a shallow copy, meaning the outer list object is a copy but for each element, it is the reference to the object in memory that is copied. So if the element is a nested collection, any modification to the collection through either `original` or `copied` will be made to the same object in memory.

The way to fix this is to utilize `deepcopy()`, which creates copies of all objects, from the outer object to each inner object and its elements.

import copy

original = [[1], [2], [3]]
copied = copy.copy(original)

original[0][0] = 99

print(copied[0] == [1])
'''
import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])