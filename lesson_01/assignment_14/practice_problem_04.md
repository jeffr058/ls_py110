# Practice Problem 4
Given the following code, what would the output be? Try to answer without running the code.

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)

# Answer
{
    "Fred": 0, 
    "Barney": 1, 
    "Wilma": 2, 
    "Betty": 3, 
    "Pebbles": 4, 
    "Bambam": 5,
}
