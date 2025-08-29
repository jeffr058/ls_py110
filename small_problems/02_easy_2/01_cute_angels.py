DEGREE = "\u00B0"
CONVERSION_FACTOR = 60

def add_leading_zero(arc):
    if arc < 10:
        return '0' + str(arc)
    else:
        return arc

def dms(angle):
    if isinstance(angle, int):
        deg = str(angle)
        min = '00'
        sec = '00'
    else:
        deg = int(angle)  # 93
        angle_decimal_part = angle - deg  # 0.034773000000001275

        converted_min_decimal = angle_decimal_part * CONVERSION_FACTOR  # 2.0863800000000765
        min = int(converted_min_decimal)  # 2
        min_decimal_part = converted_min_decimal - min  # 0.0863800000000765

        converted_sec_decimal = min_decimal_part * CONVERSION_FACTOR  # 5.18280000000459
        sec = int(converted_sec_decimal)  # 5

        min = add_leading_zero(min)
        sec = add_leading_zero(sec)

    return f"{deg}{DEGREE}{min}'{sec}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")