'''
I predict the function will return the same value as the original arg because even though the loop correctly multiplies each element by 2, the value isn't captured, and in the function body `lst` is returned without any change. The code will output False.

def multiply_list(lst):
    for item in lst:
        item *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])

'''

def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])