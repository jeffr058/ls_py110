# input: integer representing minutes
# output: string in 24-hour format ('hh:mm')
# explicit:
    # if integer is positive, time is after midnight
    # if integer is negative, time is before midnight
# implicit:
    # time goes from 0:00 to 23:59
    # 00:00 is midnight
    # if integer is 0, time is 00:00
# data structure: not sure one is needed
# algorithm:
    # Given an integer representing minutes before or after midnight
    # Convert the integer to a string in the 24-hour format
        # Use 1440 as minutes rep for 24 hours
        # Use modulo op for integer w/ 1440 to calculate the minutes after midnight
        # Use divmod w/ min_after_midnight and 60
            # where quotient represents hours and remainder represents minutes
            # Pad single digits with a leading 0 and convert string
        # Convert to proper string format using f-string
    # Return the string
# code:
MIN_IN_DAY = 1440
MIN_IN_HR = 60

def pad_with_zero(num):
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)

def time_of_day(integer):
    min_after_midnight = integer % MIN_IN_DAY
    hr_and_min = divmod(min_after_midnight, MIN_IN_HR)
    hr_min_strings = [pad_with_zero(num) 
                      for num in hr_and_min]
    
    return ':'.join(hr_min_strings)

#Examples
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True