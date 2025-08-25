numbers = []
nth_numbers = ['1st', '2nd', '3rd', '4th', '5th', 'last']

for nth_number in nth_numbers:
    number = input(f'Enter the {nth_number} number: ')
    numbers.append(number)

first_five_numbers = numbers[:-1]
last_number = numbers[-1]
first_five_numbers_strings = ','.join(first_five_numbers)
if last_number in first_five_numbers:
    print(f'{last_number} is in {first_five_numbers_strings}.')
else:
    print(f"{last_number} isn't in {first_five_numbers_strings}.")

# Searching 101
# Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

# Example 1
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.
# Example 2
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.