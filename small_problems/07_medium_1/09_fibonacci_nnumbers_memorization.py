'''
input: nth num
output: Fib num of nth num
rules:
- use memoization (save previously computed values to use again)

data structure: dictionary

algorithm:
- Set global FIB_DICT to {1: 1, 2: 1} for base case Fib nums
- If n_minus_1 is in FIB_DICT, return the value
- If n_minus_2 is in FIB_DICT, return the value
- Else FIB_DICT[n_minus_1] = fibonacci(n_minus_1)
- Else FIB_DICT[n_minus_2] = fibonacci(n_minus_2)
'''
fib_dict = {}

def fibonacci(n):
    if n <= 2:
        return 1
    elif n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fib_dict[n]

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True