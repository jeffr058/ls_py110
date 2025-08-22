# Practice Problem 8
Given the following string, create a dictionary that represents the frequency with which each letter occurs. The frequency count should be case-sensitive:

statement = "The Flintstones Rock"

The output should resemble the following:
 
# Pretty printed for clarity
{
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}

Your program may output the pairs in a different order.

# Answer
counts_of_letters = {}
for letter in statement:
    if letter in counts_of_letters or letter == ' ':
        continue
    count = statement.count(letter)
    counts_of_letters[letter] = count
  
{'T': 1, 'h': 1, 'e': 2, 'F': 1, 'l': 1, 'i': 1, 'n': 2, 't': 2, 's': 2, 'o': 2, 'R': 1, 'c': 1, 'k': 1}