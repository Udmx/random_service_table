


def password_type():
    lenght = input('how long password lenght? y or n?\n')
    upper = input('upper? y or n\n')
    lower = input('lower? y or n\n')
    digits = input('digits? y or n\n')
    pun = input('punctuation? y or n \n')

    return {
        'length' : int(lenght),
        'upper' : upper,
        'lower' : lower,
        'digit' : digits,
        'pun' : pun
    }