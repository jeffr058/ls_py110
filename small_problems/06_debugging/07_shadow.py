'''
I predict that the function raises an error because the function takes the name of built-in function `sum`, so `sum` in the outer scope points to the function object. Since `sum` is invoked inside the function, it won't invoke the built-in function but rather attempt to invoke the function, which raises an error.

To fix this, the function must be named something else.

def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)
'''
def multiply_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(multiply_sum(numbers, 2) == 20)

'''
Though I assumed a function cannot call itself in its body, that was incorrect. The issue, or at least the initial one, was that the function expected 2 arguments but only 1 was passed. The second issue would have been that even if the correct number of args were passed, the function in the local scope would keep calling itself recursively without having a condition ("base case") to prevent it from invoking infinitely.
'''