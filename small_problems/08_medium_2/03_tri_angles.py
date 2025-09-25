'''
Triangle rules:
- Right: 1 angle == 90
- Acute: each of 3 angles < 90
- Obtuse: 1 angle < 90
- Valid triangle rules:
    - sum of angles == 180 degrees
    - every angle > 0

input: 3 integers
output: one of 'right', 'acute', 'obtuse', or 'invalid'
rules: all args are integers and are degrees

data structure: none?

algorithm:
- Given angle1, angle2, angle3 (integers)
- Determine whether the triangle is:
    - Set angles to [angle1, angle2, angle3]
    - right --> if 1 angle == 90
        - If 90 in angles
    - acute --> if each angle < 90
        - if all angles are < 90
    - obtuse --> if 1 angle > 90
        - if 1 angle > 90
    - invalid --> sum != 180, angle == 0
- Return triangle type as string
'''
def triangle(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]
    
    if sum(angles) != 180 or [angle for angle in angles if angle <= 0]:
        print([angle for angle in angles if angle <= 0])
        return 'invalid'
    
    if 90 in angles:
        return 'right'
    
    for angle in angles:
        if angle > 90:
            return 'obtuse'

    return 'acute'

# Examples
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True