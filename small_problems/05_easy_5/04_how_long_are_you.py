"""
input: string
output: list of words in string
explicit rules:
- each element is word w/ space and length of word
- if arg is omitted or empty string, return empty list
- words will have single space between them

data structure: list

algorithm:
- Given words
- Set result to empty list
- Convert words to list of strings
- For each string in strings
    - If string is not an empty string
        - Set word_and_length to list containing word and length of word as a string
            - (If arg is empty string or there's no arg, see what happens)
        - Join the two elements separated by space and add to result
    - Else move on to next step
- Return result
"""
def word_lengths(words=''):
    strings = words.split()
    return [' '.join([string, str(len(string))]) 
            for string in strings 
            if string]

    # result = []
    # strings = words.split(' ')

    # for string in strings: # ['']
    #     if string:
    #         word_and_length = [string, str(len(string))]
    #         result.append(' '.join(word_and_length))

    # return result

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True