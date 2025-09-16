# input: string
# output: list of all substrings of string
# explicit rules:
    # order list by index of where in string the substring begins
    # use leading_substrings function
# data structure: list
# algorithm:
    # Given string
    # Create a list of substrings in order of index of each substring's first char
        # Create substrings list
        # For each index of range of length of string
            # Get a string of the index to end of string
            # Pass the string to leading_substrings
            # Add the returned list elements to substrings
    # Return substrings
# code:
def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    return [
        substring
        for idx in range(len(string)) 
        for substring in leading_substrings(string[idx:])
    ]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]
print(substrings('abcde'))
print(substrings('abcde') == expected_result)  # True