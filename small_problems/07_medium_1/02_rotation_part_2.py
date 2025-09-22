'''
input: number, count 
output: number
rules:
- rotate the last count digits of number
- rotate by moving first digit of count from end

data structure: list

algorithm:
- Given number and count
- Get first digit of count from end of number and move it to back of the number
    - If count is 1, return number as is
    - Convert number to string and assign to num_string
    - Get char at index position based on count
        - num_string[-count]
    - Place char at end of num_string
        - Slice start_half + end_half + num_to_move
    - Convert num_string back to integer
- Return the new number
'''
def rotate_rightmost_digits(number, count):
    if count == 1:
        return number
    
    num_string = str(number)

    num_to_move = num_string[-count]
    start_half = num_string[:-count]
    end_half = num_string[-count + 1:]

    return int(start_half + end_half + num_to_move)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True