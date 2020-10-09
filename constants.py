


def password_type():
    length = input('how long password length? enter a digit \n')
    upper = input('upper? y or n\n').lower()
    lower = input('lower? y or n\n').lower()
    digit = input('digits? y or n\n').lower()
    pun = input('punctuation? y or n \n').lower()

    return {
        'length' : int(length),
        'upper' : True if length == 'y' else False,
        'lower' : True if lower == 'y' else False,
        'digit' : True if  digit == 'y' else False,
        'pun'   : True if  pun == 'y' else False
    }