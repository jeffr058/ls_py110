# inputs: string
# output: list
# explicit rules:
    # list of palindromic substrings of string
    # substrings in order of appearance
    # duplicate substrings should be included
    # all chars count
    # case matters
    # single chars do not count
# implicit rules:
    # if no palindrome, return empty list
# data structure: list
# algorithm:
    # Given string
    # Given string

# code:
def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    return [
        substring
        for idx in range(len(string)) 
        for substring in leading_substrings(string[idx:])
    ]

def palindromes(string):
    # palindrome_substrings = []

    # for substring in substrings(string):
    #     if substring == substring[::-1] and len(substring) > 1:
    #         palindrome_substrings.append(substring)

    # return palindrome_substrings
    return [substring 
            for substring in substrings(string) 
            if substring == substring[::-1] 
            if len(substring) > 1]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True