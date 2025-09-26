'''
Input: list
Output: sorted list
Rules:
    - Use bubble sort:
        1. Two elements are compared in each iteration
        2. If the first value > second value, swap elements
        3. Move the comparison to the greater value element w/ the next element
        4. Repeat 1 and 2
        5. Continues until it performs a pass where no elements are swapped
    - Sort original list in place (mutate)
    - List contains 2 or more elements (either all integers or all strings)
Mental model
    - Compare one element with the next one, swap places if the first element has greater value, and compare the greater value element with the next one. Continue until no more swaps take place. A pass with no swaps must take place for the bubble sort to be complete.

Data structure: possibly list?

Algorithm:
    - Given lst
    - Perform bubble sort on lst
        - While swaps are made
            - For each pair of elements (need index access)
                - Two elements' values are compared
                    - Set first and second values accordingly
                    - If the first value is greater
                        - Swap positions (parallel assignment?)
                        - (Possible guard clause to handle end of list?)
            - If no swaps are made, bubble sort is complete
    - Return lst


lst = [3, 2, 5]
[2, 3, 5]

set is_swap to True
while is_swap is True
    set is_swap to False
    for idx, num in lst 
        guard clause (if idx is last element in list, continue to next part of code)
        if first > second
            first, second = second, first
            set is_swap to True
        else if first < second
            continue
return lst
'''
def bubble_sort(lst):
    is_swap = True
    while is_swap:
        is_swap = False
        
        for idx in range(len(lst) - 1):
            if lst[idx] > lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                is_swap = True

# Examples
lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True