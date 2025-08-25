def running_total(numbers):
    running_total_list = []
    
    for idx, number in enumerate(numbers):
        if not running_total_list:
            running_total_list.append(number)
        else:
            running_total_list.append(number + running_total_list[idx - 1])

    return running_total_list

# Running Totals
# Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

# Examples
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True