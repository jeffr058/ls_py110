'''
input: nth num
output: Fib num of that nth num
rule:
- use recursive function
    - base case: when arg is 1 or 2, result is 1
    - `fibonacci` calls itself twice
    - each call must come closer to the base case

data structure: possibly none

algorithm:
- Given nth num
- Recursively call `fibonacci` twice per function call until base case reached
    - Follow formula
        - Base case:
            - When nth num is 1 or 2, return 1
        - Call function twice
            - fibonacci(nth - 1) + fibonacci(nth - 2)
- Return Fib num of nth num
'''

def fibonacci(nth):
    if nth <= 2:
        return 1

    return fibonacci(nth - 1) + fibonacci(nth - 2)

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True