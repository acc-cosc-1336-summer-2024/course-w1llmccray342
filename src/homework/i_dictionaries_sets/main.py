from dictionary import *

def get_options():
    print("1 - Get p distance matrix")
    print("2 - Exit")

    
def process_exit():
    user_inp = input("Press Y to continue... ")
    user_inp.capitalize()

    if user_inp == "Y":
        return True
    else:
        print("Goodbye!")
        return False

def get_matrix():
    my_sequences_to_test = list(input("Please write a list of strings you would like to check in the following order: [[X, Y, Z], [X, Y, Z], ...] \n"))
    get_distance_mat = get_p_distance_matrix(my_sequences_to_test)
    print(get_distance_mat)
    return get_distance_mat

def handle_options():
    
    keep_running = True
    
    while keep_running: 
        get_options()
        my_choice = int(input("Please select what you would like to do: "))
        
        if my_choice == 1:
            get_matrix()
            keep_running = process_exit()
            
            
        elif my_choice == 2:
           keep_running =  process_exit()

        



def main():
    handle_options()

if __name__ == "__main__":
    main()