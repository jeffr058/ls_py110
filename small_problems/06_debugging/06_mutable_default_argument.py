'''
Seeing that the second function call doesn't return `[2]` as expected, I suspect the bug is related to how `lst` is handled. Since a list is not passed as an argument, initially `lst` is assigned `[]` before `lst`'s reference initializes the `lst` variable in the function body. This must mean that `lst` given a default value as an argument occurs in the global scope, so from the first function call, global `lst` must have been mutated to contain `1`, and the second function call appends `2` to `lst`, and `lst` is now `[1, 2]`.

Based on the problem expecting two calls to the function to return a list containing just the argument value if the list passed to the function is in an outer scope (i.e., not mutate an outer list), I conclude that the list modified in and returned from the function should be defined in the local scope.

def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

'''
def append_to_list(value, lst=[]):
    new_lst = lst.copy()
    new_lst.append(value)

    return new_lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

'''
After going through the problem, I found out it's not that the default parameter is initialized in an outer scope at the first function call; it's that when the function is defined, the default parameter value is created as an object in memory, and each time the default parameter is accessed, it is accessing that same object. So if the object is mutable, any mutation in a given function call will be its new state the next time it is accessed through another function call.
'''