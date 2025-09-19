'''
I predict this code will print False and the function will return `ollehhello`, because the string is reassigned in each iteration starting with `h` + `hello`.

def reverse_string(string):
    for char in string:
        string = char + string

    return string

print(reverse_string("hello") == "olleh")

'''
def reverse_string(string):
    new_string = ''
    for char in string:
        new_string = char + new_string

    return new_string

print(reverse_string("hello") == "olleh")