'''
input: positive integer
output: True if integer is prime, False if not
rules:
- valid prime: only divisible by itself or 1
- divisors are up to half the integer if even, up to half - 1 if odd
- 1 is not prime
- even nums EXCEPT 2 are not prime

data structure: list

algorithm:
- Given number
- Determine all possible divisors up to half of number
    - Divisors from 2 thru number divided by 2 + 1
- Determine whether number is divisible by any divisor
    - If number is 1 or number is even and greater than 2
        - Return False
    - Else for each divisor
        - If number divided by divisor has a remainder of 0
            - Return False
- Return True 
'''
def is_prime(number):
    if number == 1 or number % 2 == 0 and number > 2:
        return False
    
    for divisor in range(2, (number // 2) + 1):
        if number % divisor == 0:
            return False
    
    return True

# Examples
print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True