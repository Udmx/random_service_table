


def password_type():
    length = input('how long password length? enter a digit \n')
    upper = input('upper? y or n\n')
    lower = input('lower? y or n\n')
    digits = input('digits? y or n\n')
    pun = input('punctuation? y or n \n')

    return {
        'length' : int(length),
        'upper' : upper,
        'lower' : lower,
        'digit' : digits,
        'pun' : pun
    }