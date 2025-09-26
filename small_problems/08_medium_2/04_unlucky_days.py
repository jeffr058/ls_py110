'''
Unlucky Days
Some people believe that Fridays that fall on the 13th day of the month are unlucky days. Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in use for the foreseeable future.

input: year (int)
output: count of Fri the 13ths (int) in year
rules:
- year > 1752

data structure: 

algorithm:
- Given year
- Set count to 0
- For each month in year (range 1, 13)
    - If day is 13 AND day is Friday
        - Add 1 to count
- Return count
'''
from datetime import date

def friday_the_13ths(year):
    count = 0

    for month in range(1, 13):
        if date(year, month, 13).weekday() == 4:
            count += 1

    return count

# Examples
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True