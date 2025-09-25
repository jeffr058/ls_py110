'''
input: num
output: index of first Fib num w/ number of digits specified by num
rules:
- nth num always >= 2

data structure: list (of strings)?

algorithm:
- n = 1
- While True
    - Get the nth Fib num
    - For each Fib num in fib_dict
    - Get the length of string of Fib num
    - If the length equals num, return n
    - Increase n by 1
'''
import sys

fib_dict = {1: 2, 2: 1}

def fibonacci(n):
    if n <= 2:
        return 1
    elif n in fib_dict:
        return fib_dict[n]
    else:
        fib_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return fib_dict[n]

def find_fibonacci_index_by_length(num):
    sys.set_int_max_str_digits(50_000)
    n = 1
    while True:
        if len(str(fibonacci(n))) == num:
            return n
        n += 1

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)