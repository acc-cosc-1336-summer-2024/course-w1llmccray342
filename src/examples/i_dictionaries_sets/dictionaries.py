def test_config():
    return True

survey_questions_dictionary =  \
{
    "2.1": "The texts, assigned readings, and other course resources help me learn the course material.",
    "2.2": "Clear instructions are provided",
    "2.3": "Tests, papers, assignments, and or other activities include clear instructions",
    "2.4": "Uses instructional technology",
    "2.5": "Tests, papers, assignments, or other activities"
}

survey_response_options = {1: "Never", 2:"Sometimes", 3:"More", 4: "More more", 5: "Always", 6: "Always Always"}
capture_survey_responses = [] # surveyid, questionid, responseid
survey_response_results = {} #key:value
survey_response_results_totals =  {"2.1":0, "2.2":0, "2.3":0, "2.4":0, "2.5":0}



def display_survey_question():
    
    survey_id = 1

    for question_id, question in survey_questions_dictionary.items():
        print(question)

        for option, value in survey_response_options.items():
            print(option, value)

        response = input("Enter option: ")

        capture_survey(survey_id, question_id, int(response))
        survey_id += 1
        print(capture_survey_responses)

def capture_survey(survey_id, question_id, response):
    capture_survey_responses.append([survey_id, question_id, response])

def tabulate_survey_response_results():
    
    cnt = 1
    
    for response in capture_survey_responses:
        survey_response_results_totals[response[1]] += response[2]
        
        if "2.5" == response[1]:
            cnt += 1

    print(survey_response_results_totals)

    for question_id, totals in survey_response_results_totals.items():
        print(totals, cnt)
        survey_response_results[question_id] = totals / cnt

    print(survey_response_results)

    

