# inputs: integer (item_id) and transactions list
# outputs: True or False
# explicit rules:
    # return True only if sum of quantity values > 0
    # movement value of in increases quantity, out decreases quantity
    # use transactions_for
# data structure: list?
# algorithm:
    # Given item_id and transactions
    # Set total_quantity to 0
    # For transaction in transactions
        # If item_id is in transaction
            # If movement is in, add quantity value to total_quantity
            # Else if movement is out, subtract quantity value from total_quantity
        # If total_quantity > 0 return True
        # Else return False
# code:
def transactions_for(id_value, transactions_list):
    return [transaction 
            for transaction in transactions_list 
            if transaction['id'] == id_value]

def is_item_available(item_id, transactions):
    total_quantity = 0

    for transaction in transactions_for(item_id, transactions):
        if transaction['movement'] == 'in':
            total_quantity += transaction['quantity']
        elif transaction['movement'] == 'out':
            total_quantity -= transaction['quantity']
    
    return total_quantity > 0

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True