# inputs: list of dictionaries
# output: return a list of only dictionaries w/ even num
# algorithm:
    # given `lst` of dictionaries
    # add only dictionaries w/ even nums to `new_list`
    # return `new_list`

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
# new_list = []
# for dictionary in lst:
#     add_to_list = False
#     for nums in dictionary.values():
#         add_to_list = are_all_even(nums)
#         if not add_to_list:
#             break
#     if add_to_list:
#         new_list.append(dictionary)

lst1 = [1, 2, 3]
lst2 = [4, 8, 12]

def are_all_even(nums):
    return all([num % 2 == 0 for num in nums])

def is_dict_with_only_evens(dictionary):
        return all([are_all_even(nums) for nums in dictionary.values()])

new_list = [dictionary 
            for dictionary in lst 
            if is_dict_with_only_evens(dictionary)]

print(new_list == [{'e': [8], 'f': [6, 10]}])