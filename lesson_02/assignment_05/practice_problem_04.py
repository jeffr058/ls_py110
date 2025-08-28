# Practice Problem 4
# One of the most frequently used real-world string operations is that of "string substitution," where we take a hard-coded string and modify it with various parameters from our program.

# Given the object shown below, print the name, age, and gender of each family member:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
# Each output line should follow this pattern:

# (name) is a (age)-year-old (male or female).

# Expected Output
# Herman is a 32-year-old male.
# Lily is a 30-year-old female.
# Grandpa is a 402-year-old male.
# Eddie is a 10-year-old male.
# Marilyn is a 23-year-old female.

# My Answer
for name in munsters:
    print(f'{name} is a {munsters[name]['age']}-year-old {munsters[name]['gender']}.')