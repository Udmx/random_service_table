from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choices


def create_password(length=None, upper=None, lower=None,
                    digit=None, pun=None):

    pool = ''

    if lower =='y':
        pool += ascii_lowercase

    if upper =='y':
        pool += ascii_uppercase

    if digit =='y':
        pool += digits 

    if pun =='y':
        pool += punctuation

    if pool != '':
        return ''.join(choices(pool, k=length))



password_generated = create_password(length=8, lower=True, upper=True,
                                     digit=True, pun=True)

print(password_generated)