def test_config():
    return True

def is_number_in_range(value1, min_range, max_range):
    return value1 >= min_range and value1 <= max_range

def is_number_not_in_range(value1, min_range, max_range):
    return value1 <= min_range or value1 >= max_range

def get_generation(year):
    result = ''

    # Test code in sections
    if (year >= 1996 and year <= 2014):
        result = 'Centennial'
    elif (year >= 1977 and year <= 1995):
        result = 'Millennial'
    elif (year >= 1965 and year <= 1976):
        result = 'Gen X'
    elif (year >= 1946 and year <= 1964):
        result = 'Baby Boomer'
    else:
        result = 'Unknown Generation'

    return result