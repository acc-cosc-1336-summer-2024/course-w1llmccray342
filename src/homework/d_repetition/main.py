import repetition

def main_menu():
    print ("1 - Factorial")
    print("2 - Sum odd numbers")
    print('3 - Exit')

def handle_menu_options():

    main_menu()

    user_option = input("Please select an option: ")

    if user_option == "1" or user_option == "1.":
        handle_factorials()
    
    elif user_option == "2" or user_option == "2.":
        handle_sum_odd_numbers()

    else:
        handle_exit()




def handle_factorials():
    still_in_loop = True

    while(still_in_loop == True):
        user_desired_number_fac = int(input("Please enter a number greater than 1 and less than 10: "))
        
        if (user_desired_number_fac > 1 and user_desired_number_fac < 10):
            repetition.get_factorial(user_desired_number_fac)
            still_in_loop = False
            handle_exit()


def handle_sum_odd_numbers():

    still_in_loop = True
    
    while(still_in_loop == True):
        user_sum_odd_number = int(input("Please enter a number that is greater than 1 and less than 100: "))

        if (user_sum_odd_number > 1 and user_sum_odd_number < 100):
            repetition.sum_odd_numbers(user_sum_odd_number)
            still_in_loop = False
            handle_exit()



def handle_exit():
    user_continue_option = input("Would you like to continue? ")

    while user_continue_option == "Y" or "y":
        
        handle_menu_options()
    
    else:
        print("Goodbye!")


def main():
    handle_menu_options()


main()