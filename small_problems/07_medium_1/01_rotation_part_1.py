'''
input: list
output: new list
rules:
- move first element to end of list
- do not mutate original list
- if list empty, return empty list
- if arg not list, return None
- list w/ single element returns list w/ single element

data structure: list

algorithm:
- Given lst
- Create new_lst from lst where first element is at the end
    - If argument is not list type, return None
    - If list is empty...
    - If list has single element...
    - Set new_lst to empty list
    - Add elements from lst to new_lst starting from index 1 to the end
    - Add element at index 1 to new_lst
- Return new_lst
'''
def rotate_list(lst):
    if type(lst) != list:
        return None
    
    if lst == []:
        return []

    new_lst = lst[1:]
    new_lst.append(lst[0])

    return new_lst

# def rotate_list(lst):
#     if type(lst) != list:
#         return None

#     new_lst = []
#     if lst:
#         for num in lst[1:]:
#             new_lst.append(num)

#         new_lst.append(lst[0])

#     return new_lst

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])