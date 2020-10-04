
import string
from random import choices


def create_phone_number(operator = None):
    numbers = ''.join(choices(string.digits, k=7))

    if operator == '1':
        phone_number = '0935' + numbers
    if operator == '2':
        phone_number = '0912' + numbers


    return phone_number