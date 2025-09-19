'''
The function always returns the wrong value because the function name indicates that it is a check for if `date` is available, so if `date` is available (i.e., not in `events`), it should return `True` and `False` otherwise. This is a good example of a logic error, where the code will run successfully but with unintended results.

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date in events:
        return True

    return False

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True

'''
events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    return date not in events

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True