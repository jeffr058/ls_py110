# input: dictionary w/ unique keys & values
# output: dictionary w/ keys & values inverted
# implicit rule: return the dictionary
# data structure: dictionary, maybe list?
# algorithm:
    # Given a dictionary
    # Swap the keys and values
        # Set inverted_items to empty dictionary
        # Create coll of keys and coll of values
        # Merge the value at each positon with key into separate coll
            # Pass colls to zip function and convert return obj to list
        # Convert object to dictionary and assign to inverted_items
    # Return inverted_items

    # given a dictionary
    # change keys to values and values to keys
        # set inverted_dict to empty dictionary
        # for each key and value in dictionary
            # add the value as key assigned with key
    # return inverted_dict
# code:
def invert_dict(dictionary):
    # zipped_list = list(zip(dictionary.values(), dictionary.keys()))
    # inverted_items = dict(zipped_list)
    
    # return inverted_items

    return {value: key for key, value in dictionary.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True