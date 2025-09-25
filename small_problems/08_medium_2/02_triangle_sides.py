'''
triangle rules:
- equilateral: all sides same length
- isosceles: two sides same length
- scalene: no sides same length
- sum of lengths of shorter sides must be > length of longest side
- each side length must be > 0

inputs: three nums representing three sides
output: string (one of 'equilateral', 'isosceles', 'scalene', or 'invalid')
rules:
- floats are valid args

data structure: possibly none

algorithm:
- Given three sides of a triangle
- Determine the type of triangle
    - If all sides are the same, return 'equilateral'
        side1 == side2 == side3
    - If two sides are the same, return 'isosceles'
        side1 == side2 or side2 == side3 or side1 == side3
    - If no sides are the same, return 'scalene'
        side1 != side2, side2 != side3, side1 != side3
    - If any side is 0 or two sides are < third side, return 'invalid'
        side == 0
        side1 + side2 < side3
        side2 + side3 < side1
        side1 + side3 < side2
- Return the type as string
'''
def triangle(side1, side2, side3):
    sides = [side1, side2, side3]

    for side in sides:
        if side == 0 or side >= sum(sides) / 2:
            return 'invalid'
    
    if side1 == side2 == side3:
        return 'equilateral'
    elif side1 != side2 and side2 != side3 and side1 != side3:
        return 'scalene'
    else:
        return 'isosceles'

# Examples
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True