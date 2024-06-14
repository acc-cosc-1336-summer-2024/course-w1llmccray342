# Distinguish from SRC homework and SRC example, not necessary I think but it does make it easier to follow the flow

from src.homework.c_decisions import decisions

    
# Function to return 
def get_faculty_rating_from_input():
    user_options = input(int("Please enter the number of options: "))
    user_total = input(int("Please enter the desired total: "))

    ratio = decisions.get_options_ratio(user_options, user_total)
    print(decisions.get_faculty_rating(ratio))
   
    # Assuming we want to store the faculty rating we can also add the following code:
    # save_faculty_rating = decisions.get_faculty_rating(ratio)
    # return save_faculty_rating


# Main function to be run in main.py
def main():
    get_faculty_rating_from_input()
main()
