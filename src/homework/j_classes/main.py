from class_a import Die

def create_menu():
    menu = {1: "Roll", 2: "Exit"}
    return menu

def close_program():
    close_program = input("Would you like to close the program? Y/N: \n").upper()

    if close_program == "Y":
        print("Goodbye!")
        return False
    else:
        return True
        



def handle_menu(menu):
    still_in_loop = True

    while still_in_loop:
        for key, values in menu.items():
            print(f"{key}. {values}")

        user_input = int(input("Please select what you would like to do: \n"))

        if user_input == 1:
            my_dice = Die()
            print(f"{my_dice.__str__()}")

        still_in_loop = close_program()
        
def main():
    my_menu = create_menu()
    
    handle_menu(my_menu)

if __name__ == "__main__":
    main()    