'''
input: string
output: string w/ "number words" as numeric strings
rules:
- string does not contain any punctuation
- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'

data structure: list or dictionary

algorithm:
- Given string
- Create new_string where number_words are replaced by numeric string
    - Set number_words to list of the number words
    - Create dictionary using number words as keys, their indexes (as strings) as values
    - Create words (a list of words) from string
    - For word in words
        - If the word is in dictionary
            - Reassign word slot in words list to value from dictionary
    - Join all words in words list and convert to new_string
- Return new_string
'''
def word_to_digit(string):
    number_words = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
    ]
    dictionary = {number_word: str(idx) 
                  for idx, number_word in enumerate(number_words)}
    words = string.split()

    for idx, word in enumerate(words):
        if word in dictionary:
            words[idx] = dictionary[word]
    
    return ' '.join(words)

message = 'Please call me at five five five one two three four'
# word_to_digit(message)
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True