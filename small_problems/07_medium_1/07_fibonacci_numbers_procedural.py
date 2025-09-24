'''
input: nth (integer)
output: Fibonacci number
rules:
- first two Fib numbers: 1 when n = 1; 1 when n = 2
- when n > 2, Fib number can be represented as:
    - F(n - 1) + F(n - 2)
    - If nth is 3: (nth - 1, or value when nth = 2) + (nth - 2, or value when nth = 1)

data structure: possibly none

algorithm:
- Given n number
- Compute the sum of (n - 1) and (n - 2)
    - Set result to 0
    - Set last = 0
    - Set second_to_last = 0
    - For each count up to and incl n (range)
        - If n is 1, set result to 1
        - If n is 2, set result to 1, last to 1, and second_to_last to 1
        - Else get the sum of last and second_to_last
            - Set result to the sum
            - Set second_to_last to last
            - Set last to result
- Return result
'''
def fibonacci(n):
    result = 0
    last = 0
    second_to_last = 0

    for count in range(1, n + 1):
        if count == 1:
            result = 1
        elif count == 2:
            result = 1
            last = 1
            second_to_last = 1
        else:
            result = last + second_to_last
            second_to_last, last = last, result

    return result

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True