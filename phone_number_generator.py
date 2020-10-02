import string
from random import choices


def create_phone_number(irancell=False, hamrahavval=False):
    numbers = ''.join(choices(string.digits, k=7))

    if irancell:
        phone_number = '0935' + numbers
    if hamrahavval:
        phone_number = '0912' + numbers

    if not hamrahavval and not irancell:
        phone_number = '0935' + numbers

    return phone_number