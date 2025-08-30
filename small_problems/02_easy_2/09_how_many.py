# How Many?
# Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

def count_occurrences(lst):
    frequency_map = {}
    for item in lst:
        if item not in frequency_map:
            frequency_map[item] = 0
        frequency_map[item] += 1
        
    for key, value in frequency_map.items():
        print(f'{key} => {value}')

# Example
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# Expected Output
# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2