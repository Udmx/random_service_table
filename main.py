
from phone_number_generator import create_phone_number
from password_generator import create_password
from constants import password_type
from check_password import recognize_password_strength



if __name__ == "__main__":

    show_menu = True
    while show_menu:
        #Code Here
        service_choice = input(
        '''Choose your service
        1-Phone number generator
        2-Password generator
        3-Check password

        to quit : press q
        \n'''
        )


        if service_choice == '1':
            operator_choice = input('''Choose your operator:
                                    1-irancell
                                    2-HamraheAval''')
            phone_number = create_phone_number(operator = operator_choice)
            print(f"Your suggested phone number :{phone_number}\n")

        elif service_choice == '2':
            password_type = password_type()
            password_generated = create_password(**password_type)
            print(f"your password generated : {password_generated}\n")

        elif service_choice == '3':
            user_password = input('enter your password\n')
            password_strength = recognize_password_strength(user_password)
            print(password_strength)

        elif service_choice == 'q':
            print('see you!')
            show_menu = False



        