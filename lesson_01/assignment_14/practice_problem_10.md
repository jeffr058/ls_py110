# Practice Problem 10
What does the following code print and why?

dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())

# Answer
The code prints `('b': 'bear')` because the popitem method removes and returns the last key/value pair in the dictionary as a tuple.