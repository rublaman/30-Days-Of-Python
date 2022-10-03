'''
Write a pattern which identifies if a string is a valid python variable

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True
'''

import string
import re


def is_valid_variable(str: string):
    find_error = re.findall(r'^[-_0-9]|[-]', str)
    res = False if len(find_error) >= 1 else True
    return res


print(is_valid_variable('first-name'))
