# Improved "join"
# input: list, delimiter, conjunction
# output: string of list w/ delimiter + joining word for last element
# explicit rules:
    # use function in game
    # optional arg to specify delimiter instead of ', '
    # optional arg to specify word instead of 'or'
# implicit rules:
    # don't convert integer to str before passing to join_or
    # use prompt
    # default delimter is ', '
    # default word preceding last element is 'or' (no trailing space)
    # empty list results in empty string
# examples: provided (see below)
# data structure: list
# algorithm:
    # Given `lst` and optional delimiter and conjunction
    # Convert `lst` to a string separated by the delimiter and the conjunction preceding the last element
        # Use optional parameter `delimiter` with ', ' as default arg
        # Use optional parameter `conjunction` with 'or' as default arg
        # Move `empty_squares = [str(num) for num in lst]` to inside `join_or`
        # If `lst` is empty, return empty string
        # Else if `lst` has one element, return string of element
        # Else if `lst` has two elements, return string w/ conjunction only
        # Else reassign last element of lst w/ conjunction + last element
        # Join elements of `lst` with delimiter and conjunction 
    # Return the string
# code:
def join_or(lst, delimiter=', ', conjunction='or'):
    empty_squares = [str(num) for num in lst]

    if len(empty_squares) == 0:
        return ''
    elif len(empty_squares) == 1:
        return empty_squares[0]
    elif len(empty_squares) == 2:
        return f'{empty_squares[0]} {conjunction} {empty_squares[1]}'
    else:
        empty_squares[-1] = f'{conjunction} {empty_squares[-1]}'
        return delimiter.join(empty_squares)

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"