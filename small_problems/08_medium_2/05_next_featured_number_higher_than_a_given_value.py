'''
Given an integer, determine the next featured number (multiple of 7 that is odd and whose digits each occur exactly once).

input: integer
outputs: 
    - next featured number greater than integer arg
    - issue error if there is no next featured number
rules:
    - the largest possible featured number is 9876543201

data structure: 

algorithm:

- Given num
- Determine next featured num
    - Find the next featured number after num
        - If num is equal to or greater than 9876543201, return error msg
        - For each number after num
            - Check if it's a featured num
            - HELPER is_featured to determine if num is odd and multiple of 7 whose digits each occur once
                - number must be odd
                - number must be divisible by 7
                - number must have unique individual digits
                    - convert to string
                        - "21"
                    - separate chars and check for duplicates
                        - length of "21" == length of set("21")
                - If all conditions met, return True
            - If it's a featured num
                - Return featured num
                - Else continue to next number
'''
def is_featured(next_num):
    if next_num % 2 == 1 and next_num % 7 == 0:
        next_num_string = str(next_num)
        if len(next_num_string) == len(set(next_num_string)):
            return True
    
    return False

def next_featured(num):
    next_num = num + 1
    while next_num <= 9876543201:
        if is_featured(next_num):
            return next_num
        next_num += 1

    return ("There is no possible number that "
            "fulfills those requirements.")

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True