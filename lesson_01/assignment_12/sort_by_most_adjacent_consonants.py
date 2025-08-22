def count_max_adjacent_consonants(input_string):
    temp_string = ''
    max_count = 0
    last_index = len(input_string) - 1
    VOWELS = ('a', 'e', 'i', 'o', 'u')
    
    for idx, char in enumerate(input_string):
        if char.isspace() or (idx == 0 and char in VOWELS):
            continue
        elif idx == last_index and char not in VOWELS:
            temp_string += char
            if 1 < len(temp_string) > max_count:
                max_count = len(temp_string)
            temp_string = ''
        elif char in VOWELS:
            if 1 < len(temp_string) > max_count:
                max_count = len(temp_string)
            temp_string = ''
        else:
            temp_string += char

    return max_count
    
def sort_by_consonant_count(input_list):
    max_count_dictionary = {}

    for string in input_list:
        max_count_dictionary[string] = count_max_adjacent_consonants(string)

    max_num = max(max_count_dictionary.values())
    ordered_strings_list = []

    while max_num >= 0:
        for string in max_count_dictionary:
            if max_count_dictionary[string] == max_num:
                ordered_strings_list.append(string)
        max_num -= 1

    return ordered_strings_list
    
    # compared to lines 25-39, this solution does the same thing:
    # input_list.sort(key=count_max_adjacent_consonants, reverse=True)
    # return input_list


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) == ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])