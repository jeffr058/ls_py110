# input: dictionary, list of keys
# output: new dictionary w/ only keys from list
# data structure: dictionary, maybe list?
# algorithm:
    # Given input_dict and keys_lst
    # Create new_dict that contains only keys from keys_lst
        # For each key and value in input_dict
            # If key is in keys
                # Add to new_dict
    # Return new_dict
# code:
def keep_keys(input_dict, keys_lst):
    return {key: value for key, value in input_dict.items() if key in keys_lst}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True