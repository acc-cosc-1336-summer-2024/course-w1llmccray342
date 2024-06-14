def test_config():
    return True

def is_number_in_range(value1, min_range, max_range):
    return value1 >= min_range and value1 <= max_range


def get_options_ratio(option, total):
  get_ratio = option / total
  return get_ratio

# Set up a return function
def get_faculty_rating(get_ratio):
   # Set up conditionals
    rating = ""

    if get_ratio >= 0 and get_ratio <=.59:
        rating = "Unacceptable"
    elif get_ratio > .6 and get_ratio <= .7:
        rating = "Needs Improvement"
    elif get_ratio > .7 and get_ratio <= .8:
        rating = "Good"
    elif get_ratio > .8 and get_ratio <= .9:
        rating = "Very Good"
    elif get_ratio > .9 and get_ratio < 1:
        rating = "Excellent"
    #Sanity check to make sure we're not going below the minvalue or above the maxvalue required in parameters.
    else: 
        rating = "Error"

    return rating


      