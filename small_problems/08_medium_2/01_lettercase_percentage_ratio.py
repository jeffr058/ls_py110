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
def letter_percentages(string):
    string_length = len(string)
    lowercase = 0
    uppercase = 0
    neither = 0
    result = {}
    for char in string:
        if char.isalpha() and char.islower():
            lowercase += 1
        elif char.isalpha() and char.isupper():
            uppercase += 1
        else:
            neither += 1

    result['lowercase'] = f'{lowercase / string_length * 100:.02f}'
    result['uppercase'] = f'{uppercase / string_length * 100:.02f}'
    result['neither'] = f'{neither / string_length * 100:.02f}'

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