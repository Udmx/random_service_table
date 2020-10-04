from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choices


def create_password(length=8, upper=False, lower=False,
                    digit=False, pun=False):
    pool = ''

    if lower:
        pool += ascii_lowercase

    if upper:
        pool += ascii_uppercase

    if digit:
        pool += digits 

    if pun:
        pool += punctuation

    return ''.join(choices(pool, k=length))


password_generated = create_password(length=8, lower=True, upper=True,
                                     digit=True, pun=True)

print(password_generated)