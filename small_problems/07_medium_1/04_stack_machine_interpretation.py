'''
stack: list of values that grows/shrinks dynamically
    - can use list.append (to "push" to stack) and list.pop (to "pop" from stack)
stack-and-register: lang that uses stack, not vars
    - each op in lang operates on a register (current value)
    - regsiter is not part of stack

operation that needs two values pops topmost item from stack, operates on it w/ register value, and stores result as new register value

input: string
output: integer or None (if PRINT not passed to function)
rules:
- all ops are integer ops (important for DIV and REMAINDER)
- initialize stack to [] and register to 0
- all args are valid programs
commands:
- n: place int value in register (don't modify stack)
- PUSH: push current register value onto stack (and leave value in register)
- ADD: pop value from stack, add to register value and store in register
- SUB: pop value from stack, subtract from register value and store in register
- MULT: pop value from stack, multiply w/ register value and store in register
- DIV: pop value from stack, divide register value by it, and store INT in register
- REMAINDER: pop value from stack, divide register value by it, and store INT remainder in register
- POP: remove topmost item from stack, place in register
- PRINT: print register value

data structure: list, maybe dict?

algorithm:
- Execute the commands based on command_string
    - Set stack to [] and register to 0
    - Separate string into commands
    - For each command in commands
        - perform the operation
            - possibly through match statement
                - if n, register = n
                - if PUSH, add register value to stack, leave value in register too
                - if ADD, pop value from stack and add to register
                - if SUB, pop value from stack and subtract from register (store in register)
                - if MULT, pop value from stack and multiply w/ register (store in register)
                - if DIV, pop value from stack and divide register by value (store INTEGER in register)
                - if REMAINDER, pop value from stack and divide register by value (store INTEGER REMAINDER in register)
                - if POP, pop value from stack and have register equal that value
                - if PRINT, print register
'''
def minilang(command_string):
    stack = []
    register = 0
    commands = command_string.split()

    for command in commands:
        match command:
            case 'ADD':
                register += stack.pop()
            case 'SUB':
                register -= stack.pop()
            case 'MULT':
                register *= stack.pop()
            case 'DIV':
                register //= stack.pop()
            case 'REMAINDER':
                register %= stack.pop()
            case 'PUSH':
                stack.append(register)
            case 'POP':
                register = stack.pop()
            case 'PRINT':
                print(register)
            case _:
                register = int(command)

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)