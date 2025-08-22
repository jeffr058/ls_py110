def multiply(numbers, multiplier):
    product_list = []
    for current_number in numbers:
        product_list.append(current_number * multiplier)

    return product_list

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]