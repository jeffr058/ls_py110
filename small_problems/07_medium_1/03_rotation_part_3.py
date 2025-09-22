'''
input: number
output: new number
rules:
- complete a maximum rotation:
    - rotate one digit to the left (from 735291 to 352917)
    - keep first digit in place and rotate the rest one digit to left (352917 to 329175)
    - keep first two digits in place and ... (329175 to 321759)
    - ... (321759 to 321597)
    - ... (321597 to 321579)
- return maximum rotation
- use rotate_rightmost_digits function
- for single number return same number
- for two-digit number return rotated number
- if 0 ends up as leading digit, remove the 0

data structure: possibly list

algorithm:
- Complete a maximum rotation w/ given number
    - Use helper function to rotate digits according to -count
    - Get count that decrements w/ each iteration
        - Set num_string to number converted to string
        - For idx in range of length of num_string to 0 (decrement by 1)
            - Pass number and idx to rotate_rightmost_digits
                - Assign returned value to number
    - Return number
'''
def rotate_rightmost_digits(number, count):
    if count == 1:
        return number
    
    num_string = str(number)

    num_to_move = num_string[-count]
    start_half = num_string[:-count]
    end_half = num_string[-count + 1:]

    return int(start_half + end_half + num_to_move)

def max_rotation(number):
    num_str_length = len(str(number))

    for idx in range(num_str_length, 1, -1):
        number = rotate_rightmost_digits(number, idx)

    return number

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True