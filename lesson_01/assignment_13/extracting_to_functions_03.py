def double_odd_indexes(numbers):
    doubled_nums = []
    for idx in range(len(numbers)):
        if idx % 2 == 1:
            doubled_nums.append(numbers[idx] * 2)
        else:
            doubled_nums.append(numbers[idx])

    return doubled_nums

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_indexes(my_numbers))  # [1, 8, 3, 14, 2, 12]

# not mutated
print(my_numbers)                      # [1, 4, 3, 7, 2, 6]