from class_a import Die

def create_menu():
    menu = {1: "Roll", 2: "Exit"}
    return menu

def close_program():

    close_program = ""

    while not close_program in ["Y", "N"] or type(close_program) == type(str):
        close_program = input("Would you like to close the program? Y/N: \n").upper()
        print(f"{type(close_program)} and {close_program} selected")
        
        if type(close_program) != str:
            print("Invalid option. Must be type string to continue!")

    if close_program == "Y":
        print("Goodbye!")
        return False
    else:
        return True
            

def handle_menu(menu):
    still_in_loop = True

    while still_in_loop:
        user_input = 0
        
        try:
                for key, values in menu.items():
                    print(f"{key}. {values}")
                
                # Check to see if user input is valid
                while not user_input in [1, 2] or type(user_input) == type(int): 

                        user_input = int(input("Please select what you would like to do: \n"))
            
                if user_input not in [1, 2]:
                    print(f"Invalid option! User input must be in the designated range!")
            
        except ValueError:
            print("ERROR: Input must be an integer to continue")
            continue
                
        

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