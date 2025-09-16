# inputs: string
# outputs: list of substrings of that string
# explicit rules:
    # each substring starts w/ first letter of word
    # list ordered shortest to longest
# implicit rules:
    # single letter returns single letter
# data structure: list
# algorithm:
    # Given string
    # Create substrings
        # Set substrings to empty list
        # For each char in string
            # Combine chars from beginning of string up to and incl index of current char
            # Append to substrings
    # Return substrings
# code:
def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])