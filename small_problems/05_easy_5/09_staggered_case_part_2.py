'''
I: string
O: string w/ same chars but w/ alpha chars alternating cases

A:
- Given string
- Create new string of the same chars but w/ alpha chars alternating in cases
    1. Convert string to list of chars
        - For each char
            - If char is not alphabetic, add char to non_alpha with its index value
            - Append non_alpha to non_alphas_list
    2. Create alpha_chars_list of just alpha chars in alternating cases
    3. Insert the non_alpha chars at the corresponding index
    4. Convert to string
- Return new string
'''
def staggered_case(string):
    # 1
    non_alpha_list = []
    for idx, char in enumerate(list(string)):
        if not char.isalpha():
            non_alpha = [idx, char]
            non_alpha_list.append(non_alpha)
    
    # 2
    alpha_chars_list = [char for char in string if char.isalpha()]
    
    chars_list = []
    for idx, char in enumerate(alpha_chars_list):
        func = char.upper if idx % 2 == 0 else char.lower
        chars_list.append(func())
    
    #3
    for sublist in non_alpha_list:
        chars_list.insert(sublist[0], sublist[1])
    
    #4
    return ''.join(chars_list)

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True