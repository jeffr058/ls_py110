'''
input: string
output: dictionary
rules:
- returned dictionary contains: 
    - % of chars in string that are lowercase
    - % of chars in string that are uppercase
    - % of chars in string that are neither
- % values should be returned as strings between '0.00' and '100.00' (rounded two decimal points)
- strings will contain at least one char
- no alpha chars in string s/b '0.00' for both upper and lower, '100.00' for neither

data structure: list

algorithm:
- Given `string`
- Get the percentages of uppercase, lowercase, and neither for the chars in `string`
    - Get the length of `string`
    - Capture counts of chars that are uppercase, lowercase, or neither
    - Divide each count by length
- Format the percentage to whole numbers rounded to 2 decimal points
- Add data into a dictionary `result`
- Return `result`
'''
# 
def percentage_string(count, total):
    return f'{count / total * 100:.02f}'

def letter_percentages(string):
    string_length = len(string)
    lower_count = 0
    upper_count = 0
    neither_count = 0
    result = {}
    
    for char in string:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        else:
            neither_count += 1

    result['lowercase'] = percentage_string(lower_count, string_length)
    result['uppercase'] = percentage_string(upper_count, string_length)
    result['neither'] = percentage_string(neither_count, string_length)

    return result

# Examples
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)