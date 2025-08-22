# Practice Problem 12
What would be the output of the below code? Try to answer without running the code.

frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)

# Answer
`frozen.add(6)` will raise an error because frozen sets are immutable and cannot be modified.