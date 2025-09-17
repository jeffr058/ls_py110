# input: list of strings
# output: list of string w/ vowels removed
# rules: case-insensitive, 'y' not considered vowel
# data structure: list
# algorithm:
    # Given strings
    # Create a new_list of strings w/ all vowels removed (case insensitive)
        # For each string
            # Set consonants to empty list
            # Go through each char
                # If char (case insensitive) is a vowel
                    # Move onto the next char
                # Else add char to consonants
            # Join chars of consonants and add resulting string to new_list
    # Return new_list
# code:
def remove_vowels(strings):
    # new_list = []
    # for string in strings:
    #     consonants = []
    #     for char in string:
    #         if char.lower() in ['a', 'e', 'i', 'o', 'u']:
    #             continue
    #         else:
    #             consonants.append(char)
    #     new_list.append(''.join(consonants))
    # return new_list

    return [
        (''.join([char 
                  for char in string 
                  if char.lower() not in ['a', 'e', 'i', 'o', 'u']])) 
                  for string in strings
    ]


# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True