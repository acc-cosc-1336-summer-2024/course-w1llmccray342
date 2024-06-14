# Distinguish from SRC homework and SRC example, not necessary I think but it does make it easier to follow the flow

import decisions

# For readability and reusability we should keep functions to fairly simple to understand on their purposes.

# Function to generate a ratio
def get_input_ratio():
    user_options = int(input("Please enter the number of options: "))
    user_total = int(input("Please enter the desired total: "))

    ratio = decisions.get_options_ratio(user_options, user_total)
    return ratio


# Function to return our desired faculty rating
def get_faculty_rating_from_input():
    local_ratio = get_input_ratio()
    print(decisions.get_faculty_rating(local_ratio))
   
    # Assuming we want to store the faculty rating we can also add the following code:
    # save_faculty_rating = decisions.get_faculty_rating(ratio)
    # return save_faculty_rating

# Main function to be run in main.py
def main():
    get_faculty_rating_from_input()
main()
