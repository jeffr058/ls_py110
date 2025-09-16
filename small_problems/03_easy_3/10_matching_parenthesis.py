# input: string
# output: True if parentheses are properly balanced, False if not
# rules:
    # parentheses must start with '(' not ')'
    # no occurrences returns True
# data structure: list?
# algorithm:
    # Given a string
    # Determine if parentheses are in string
    # Check if '(' comes before ')'
        # Set lst to list comprehension
            # For each char in string
                # If char is '(' or ')' add to lst
        # If count of '(' is same as ')'
        # If even index for each '(' and odd index for each ')'
    # If each ( comes before a ), return True
    # Else return False
# code:
def is_balanced(string):
    counter = 0

    for char in string:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
            if counter < 0:
                return False
    
    return counter == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True