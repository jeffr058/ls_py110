# input: dictionary
# output: input dictionary's keys
# data structure: list?
# algorithm:
    # Given dictionary
    # Sort the keys according to their values
        # Create helper function give_value to return value
        # Pass dictionary to sorted w/ key keyword and give_value to create list of sorted keys
    # Return the list
# code:
def order_by_value(dictionary):
    def value_of_item(key):
        return dictionary[key]

    return sorted(dictionary, key=value_of_item)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True