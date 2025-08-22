# Practice Problem 5
Calculate the total age given the following dictionary:

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# Answer
sum(ages.values())  # 6174

total_age = 0
for age in ages.values():
    total_age += age