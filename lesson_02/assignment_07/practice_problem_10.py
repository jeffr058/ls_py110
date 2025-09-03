# input: none
# output: alphanumeric string representing UUID
# explicit:
    # 32-chars long
    # only chars from 0-9 and a-f
    # in an 8-4-4-4-12 pattern
# implicit:
    # get random characters
    # use at least one comprehension
# data structures: dictionary? list?
# algorithm:
    # generate 32-char string using random module
    # separate the string in the 8-4-4-4-12 pattern
        # set `UUID_PATTERN` w/ the pattern values
        # set `strings' w/ empty list
        # set `start` and `stop` w/ 0
        # for `value` in `UUID_PATTERN`
            # add `value` to `stop`
            # add `string` at indexes `start` and `stop` to `strings`
            # add `value` to `start`
        # join all items in `strings` together w/ hyphens and set to `uuid`
    # return `uuid`
# import random
# UUID_PATTERN = [8, 4, 4, 4, 12]
# VALID_CHARS = '0123456789abcdef'
# hex_chars = ''.join(random.choices(VALID_CHARS, k=32))

# strings = []
# start = 0
# stop = 0

# for value in UUID_PATTERN:
#     stop += value
#     strings.append(hex_chars[start:stop])
#     start += value

# uuid = '-'.join(strings)

import random
UUID_PATTERN = [8, 4, 4, 4, 12]
VALID_CHARS = '0123456789abcdef'

def generate_uuid():
    hex_strings = [''.join(random.choices(VALID_CHARS, k=value))
                   for value in UUID_PATTERN]
    uuid = '-'.join(hex_strings)
    return uuid

print(generate_uuid())