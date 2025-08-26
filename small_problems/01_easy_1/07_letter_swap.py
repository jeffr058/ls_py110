# inputs: string of words separated by spaces
# outputs: string of words w/ first & last letters swapped
# explicit:
    # string has min of 1 word
    # words are at min 1 letter
    # string contains only words & single spaces b/w words
    # no leading/trailing spaces in string
# implicit:
    # only letters
    # single letter string returns itself
# questions:
# data structures: list
# algorithm:
    # Given a string of words assigned to `words`
    # 1. Go through each `word` and swap the first letter with the last letter
        # 1. Separate each word and add the words to a list
            # 1. Split `words` and add words to `words_list`
        # 2. For each `word` in `words_list` swap the first and last letters
            # 1. Prior to loop, assign `new_words_list` to empty list
            # 2. If `word` length is 1, append `word` to `new_words_list` and continue to next word
            # 3. Assign a variable `first_ltr` w/ the first char of `word`
            # 4. Assign a variable `last_ltr` w/ the last char of `word`
            # 5. Assign a variable `middle_ltrs` w/ the remaining chars of `word`
            # 6. Concatenate the variables (last, middle, first) and assign to `new_word`
            # 7. Append `new_word` to `new_words_list`
        # 3. Join the words in `new_words_list` separated by space and assign to `result`
    # 2. Return `result`
# code:
def swap(words):
    words_list = words.split()
    new_words_list = []
    
    for word in words_list:
        if len(word) == 1:
            new_words_list.append(word)
            continue

        first_ltr = word[0]
        last_ltr = word[-1]
        middle_ltrs = word[1:-1]
        new_word = last_ltr + middle_ltrs + first_ltr
        new_words_list.append(new_word)

    result = ' '.join(new_words_list)

    return result

# Letter Swap
# Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

# You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

# Examples
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True