# inputs: dictionary w/ list values of strings
# outputs: display list w/ every vowel in the strings
# algorithm:
    # set `list_of_vowels` w/ empty list
    # for each `value` in `dict1`
        # for each `word` in `value`
            # for each `char` in `word`
                # if `char` is in 'aeiou', add `char` to `list_of_vowels`
# code:
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here
# list_of_vowels = []
# for words_value in dict1.values():
#     for word in words_value:
#         for char in word:
#             if char in 'aeiou':
#                 list_of_vowels.append(char)

list_of_vowels = [char 
                  for words_value in dict1.values() 
                  for word in words_value 
                  for char in word 
                  if char in 'aeiou']

print(list_of_vowels == ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o'])