# Further Exploration
# Try to solve the problem when words are case insensitive, e.g. "suv" and "SUV" represent the same vehicle type.

def count_occurrences(lst):
    frequency_map = {}
    for item in lst:
        if item.lower() not in frequency_map:
            frequency_map[item.lower()] = 0
        frequency_map[item.lower()] += 1

    for key, value in frequency_map.items():
        print(f'{key} => {value}')

# Example
vehicles = ['car', 'CAR', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# Expected Output
# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2