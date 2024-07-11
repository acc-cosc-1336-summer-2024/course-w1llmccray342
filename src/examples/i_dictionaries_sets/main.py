from dictionaries import *

choice = 1

while choice == 1:
    display_survey_question()
    choice = int(input("Enter another survey: "))

tabulate_survey_response_results()
average = get_course_average()
professor_rating = get_faculty_rating(average)

print(f"The professor's average is... {average}")

print(f"The professor's rating is {professor_rating}")