from string import punctuation

# these variables are for color



def show_result(password, result):  # this function only levels and prints them
    BOLD, RED, YELLOW, GREEN, BLUE = '\033[1m', '\033[31m', '\033[93m',\
                                 '\033[32m', '\033[34m'
    count_true_result = result.count('True')
    grade = '==='

    if count_true_result == 0:
        print(f' {BOLD}Your Password is : {BLUE}{password}\n'
              f' {RED}{grade}'
              f' \n This password is VeryShort !!!!!!!!')

    if count_true_result == 1:
        print(f' {BOLD}Your Password is : {BLUE}{password}\n'
              f' {RED}{grade}'
              f' \n This password is Week !')

    if count_true_result == 2:
        print(f' {BOLD}Your Password is : {BLUE}{password}\n'
              f' {RED}{grade}{YELLOW}{grade}'
              f' \n This password is Medium :)')

    if count_true_result >= 3:
        print(f' {BOLD}Your Password is : {BLUE}{password}\n'
              f' {RED}{grade}{YELLOW}{grade}{GREEN}{grade}'
              f' \n This password is Strong :D')


def recognize_password_strength(password):  # this func take pass and check it
    result_check = str()

    if len(password) < 8:
        result_check = 'False'
    else:
        result_check += f'{any(char.islower() for char in password)}'
        result_check += f'{any(char.isupper() for char in password)}'
        result_check += f'{any(char.isdigit() for char in password)}'
        result_check += f'{any(char in punctuation for char in password)}'

    show_result(password, result_check)


# pass_user = input(f'{BLUE}Please enter Your password to check : ')
# recognize_password_strength(pass_user)
