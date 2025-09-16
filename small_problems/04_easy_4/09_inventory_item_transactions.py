# inputs: integer (inventory item ID, value in dictioanry) and list of transactions
# output: list of transactions only for specified inventory item ID
# data structure: list
# algorithm: 
    # Given id_value and transactions
    # Create specified_list list that contains only transactions with id_value
        # For each transaction in transactions
            # Get value from transaction
            # If value from transaction is equal to id_value, add transaction to specified_list
    # Return specified_list
# code:
def transactions_for(id_value, transactions_list):
    return [transaction 
            for transaction in transactions_list 
            if transaction['id'] == id_value]

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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True