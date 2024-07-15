from class_a import Die

def create_menu():
    menu = {1: "Roll", 2: "Exit"}
    return menu

def close_program():

    close_program = ""

    while not close_program in ["Y", "N"]:
        close_program = input("Would you like to close the program? Y/N: \n").upper()
        print(f"{type(close_program)} and {close_program} selected")
        print("Invalid option")

    if close_program == "Y":
        print("Goodbye!")
        return False
    else:
        return True
            

def handle_menu(menu):
    still_in_loop = True

    while still_in_loop:
        user_input = 0
        
        for key, values in menu.items():
            print(f"{key}. {values}")
        
        # Check to see if user input is valid
        while not user_input in [1, 2]: 
            user_input = int(input("Please select what you would like to do: \n"))
            print(f"DEBUG: {type(user_input)} and {user_input} selected")
            print("Invalid option! User input must be a int value and in the designated range!")
        

        if user_input == 1:
            my_dice = Die()
            my_dice.roll()
            print(f"{my_dice.__str__()}")

        still_in_loop = close_program()
        
def main():
    my_menu = create_menu()
    
    handle_menu(my_menu)

if __name__ == "__main__":
    main()    