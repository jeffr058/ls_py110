# input: list of integers
# output: list sorted by English word of integers
# data structure: dictionary
# algorithm:
    # Given numbers
    # Create a dictionary w/ numbers as key & English word as value
    # Sort integers by value
        # Create helper function to return value of num
        # Pass list to sorted function with key keyword and assign to result
    # Return result
# code:
num_words = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 
    'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
    'sixteen', 'seventeen', 'eighteen', 'nineteen'
]

def alphabetic_number_sort(nums):
    def word_of_num(num):
        return num_words[num]

    result = sorted(nums, key=word_of_num)

    return result

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True