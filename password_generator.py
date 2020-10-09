from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choices
import sys


def create_password(length=None, upper=False, lower=False,
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

    if pool != '':
        return ''.join(choices(pool, k=length))



password_generated = create_password(length=8, lower='y', upper=True,
                                     digit=True, pun=True )
print(sys.argv)
print(password_generated)