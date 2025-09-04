# input: string of 24-hr format 
# output: integer (for each function)
# explicit: integer range 0 through 1439
# implicit: "00:00" and "24:00" result in 0
# data structures: unsure
# algorithm:
    # Given time represented as string in 24-hr format
    # For after_midnight function
        # Compute how many minutes time is after midnight
            # Convert hrs and min to total_min
            # Handle wrapping w/ modulo
    # For before_midnight function
        # Compute how many minutes time is before midnight
            # Convert hrs and min to total_min
            # Subtract total_min from MIN_PER_DAY
            # Handle edge case 24:00
    # Return minutes
# code:
MIN_PER_HR = 60
HR_PER_DAY = 24
MIN_PER_DAY = MIN_PER_HR * HR_PER_DAY

def time_to_min(time):
    hr, min = time.split(':')
    total_min = (int(hr) * MIN_PER_HR) + int(min)
    return total_min

def after_midnight(time):
    delta_min = time_to_min(time)
    return delta_min % MIN_PER_DAY

def before_midnight(time):
    delta_min = time_to_min(time)
    return (MIN_PER_DAY - delta_min) if 0 < delta_min < 1440 else 0

# Examples
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True