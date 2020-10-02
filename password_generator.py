from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choices


def create_password(lenght=8, upper=False, lower=False,
                    digit=False, punc=False):
    pool = ''

    if lower:
        pool += ascii_lowercase

    if upper:
        pool += ascii_uppercase

    if digit:
        pool += digits 

    if punc:
        pool += punctuation

    return ''.join(choices(pool, k = lenght))


password_generated = create_password(lenght=8, lower=True, upper=True, digit=True
                                    ,punc=True)

print(password_generated)