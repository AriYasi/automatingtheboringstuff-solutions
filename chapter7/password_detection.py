import re

no_space_regex = re.compile(r'^\w{8,}$')
uppercase_regex = re.compile(r'[A-Z]')
lowercase_regex = re.compile(r'[a-z]')
digit_regex = re.compile(r'(\d)')

def detect_strong_password(password):
    if no_space_regex.search(password) == None:
        print('The password has to be at least 8 characters with no spaces.')
        return
    if lowercase_regex.search(password) == None:
        print('You must have at least one lowercase character.')
        return
    if uppercase_regex.search(password) == None:
        print('You must have at least one uppercase character.')
        return
    if digit_regex.search(password) == None:
        print('There is no digits in your password')
        return
    else:
        print('Valid password.')

detect_strong_password('Password123')