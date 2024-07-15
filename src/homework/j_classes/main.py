from class_a import Die

def create_menu():
    menu = {1: "Roll", 2: "Exit"}
    return menu

def close_program():
    close_program = input("Would you like to close the program? Y/N: \n").upper()

    if close_program == "Y":
        print("Goodbye!")
        still_in_loop = False
    else:
        still_in_loop = True

    return still_in_loop


def handle_menu(menu):
    still_in_loop = True

    while still_in_loop:
        for key, values in menu.items():
            print(f"{key}. {values}")

        user_input = int(input("Please select what you would like to do: \n"))

        if user_input == 1:
            my_dice = Die()
            my_dice_roll = my_dice.roll()
            print(f"You rolled a... {my_dice.__str__()}")

        still_in_loop = close_program()
        
def main():
    my_menu = create_menu()
    
    handle_menu(my_menu)

if __name__ == "__main__":
    main()    