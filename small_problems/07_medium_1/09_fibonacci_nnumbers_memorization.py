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
FIB_DICT = {1: 1, 2: 1}

def fibonacci(n):
    if n <= 2:
        return 1

    n_minus_1 = FIB_DICT.setdefault(n - 1, fibonacci(n - 1))
    n_minus_2 = FIB_DICT.setdefault(n - 2, fibonacci(n - 2))

    return n_minus_1 + n_minus_2

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True