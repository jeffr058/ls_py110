'''
inputs: two lists w/ same number of integers 
outputs: new list
rules: elements in new list are products of corresponding elements from the two lists

data structure: list, maybe zip obj?

algorithm:
- Given list1 and list2
- Set new_list to empty list
- Multiply the elements at the same index and add products to a new list
    - For each index
        - Multiply element at that index of list1 by element at that index of list2
        - Add to new_list
- Return new_list
code:
'''
def multiply_items(list1, list2):
    # new_list = []
    # for idx in range(len(list1)):
    #     new_list.append(list1[idx] * list2[idx])
    # return new_list

    return [list1[idx] * list2[idx] 
            for idx in range(len(list1))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True