produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(produce_dict):
    only_fruit_dict = {}
    for key, value in produce_dict.items():
        if value == 'Fruit':
            only_fruit_dict[key] = value
    return only_fruit_dict

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }