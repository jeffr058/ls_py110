'''
What will happen if you replace sum_ with sum every place it occurs?

Replacing sum_ with sum every place it occurs will cause variable shadowing to take place; since sum is a built-in function, attempting to reassign it will raise an error because the sum variable will no longer point to the function but instead reference the sum that is attempted to be assigned in the function's scope. Since the attempt to use sum is in conjunction with its assignment, the error will be raised on the first line of the function body.
'''

def sum_square_difference(count):
    sum_ = sum(range(1, count + 1))

    sum_of_squares = 0
    for i in range(1, count + 1):
        sum_of_squares += i**2

    return sum_**2 - sum_of_squares