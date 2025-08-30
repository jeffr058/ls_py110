DEGREE = "\u00B0"
CONVERSION_FACTOR = 60

def dms(angle):
    deg = int(angle)
    angle_decimal_part = angle - deg

    converted_min_decimal = angle_decimal_part * CONVERSION_FACTOR
    min = int(converted_min_decimal)
    min_decimal_part = converted_min_decimal - min

    converted_sec_decimal = min_decimal_part * CONVERSION_FACTOR
    sec = int(converted_sec_decimal)

    return f"{deg % 360}{DEGREE}{min:02}'{sec:02}\""

# Test Cases
print(dms(-1) == "359°00'00\"")  # True
print(dms(400) == "40°00'00\"")  # True
print(dms(-40) == "320°00'00\"")  # True
print(dms(-420) == "300°00'00\"")  # True