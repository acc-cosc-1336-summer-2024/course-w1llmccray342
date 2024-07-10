from dictionaries import *

choice = 1

while choice == 1:
    display_survey_question()
    choice = int(input("Enter another survey: "))

tabulate_survey_response_results()
average = get_course_average()

print(f"The professor's average is... {average}")