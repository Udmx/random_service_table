
from phone_number_generator import create_phone_number
from password_generator import create_password
from constants import password_type
from check_password import recognize_password_strength



if __name__ == "__main__":

    show_menu = True
    while show_menu:
        #Code Here
        service_choosed = input(
        '''Choose your service
        1-Phone number generator
        2-Password generator
        3-Check password

        to quit : press q
        \n'''
        )


        if service_choosed == '1':
            operator_choosed = input('''Choose your operator:
                                    1-irancell
                                    2-HamraheAval''')
            phone_number = create_phone_number(operator = operator_choosed)
            print(f"Your suggested phone number :{phone_number}\n")

        elif service_choosed == '2':
            password_type = password_type()
            password_generated = create_password(**password_type)
            print(f"your password generated : {password_generated}\n")

        elif service_choosed == '3':
            user_password = input('enter your password\n')
            password_strenght = recognize_password_strength(user_password)
            print(password_strenght)

        elif service_choosed == 'q':
            print('see you!')
            show_menu = False

        else:
            'you entered wrong!'

        