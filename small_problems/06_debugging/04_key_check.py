'''
I think it is raising an error due to using `my_dict[key]` in the if statement. If the key doesn't exist, there would be no value to evaluate for truthiness. Using the get method is a better way to check to see if a key exists and return its value if it exists or a default value if it doesn't.

def get_key_value(my_dict, key):
    if my_dict[key]:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

'''
def get_key_value(my_dict, key):
    return my_dict.get(key)

print(get_key_value({"a": 1}, "b"))