'''
input: positive integer
output: sum of integer's digits

data structure: ?

algorithm:
- Given number
- Get total sum of digits
    - Set BASE_10 to 10
    - Set remaining_digits to number
    - Set running_total to 0
    - While remaining_digits >= 10
        - Pass remaining_total to divmod w/ BASE_10 to get quotient and remainder
        - Set remaining_digits to quotient value, remainder to remainder value
        - Add remainder to running_total
    - Add remaining_digits to running_total
- Return running_total
'''
def sum_digits(number):
    BASE_10 = 10
    remaining_digits = number
    running_total = 0

    while remaining_digits >= 10:
        remaining_digits, remainder = divmod(remaining_digits, BASE_10)
        running_total += remainder
    
    running_total += remaining_digits
    
    return running_total

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True