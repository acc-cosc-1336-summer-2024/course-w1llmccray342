def test_config():
    return True

#Example string
def create_string():
    lang = "Python"
    print(lang)

def access_chars_in_string():
    lang = "Python"
    print(lang[0])
    print(lang[-1])

def cannot_change_string_chars():
    lang = "Python"

    lang[0] = "P"

    # Strings are immutable, that means they cannot be changed without use of specific methods.

def loop_string_w_while():
    lang = "Python"
    i = 0

    while(i < len(lang)):
        print(lang[i])
        # Statement that eventually stops loop
        i += 1

def loop_string_w_for():
    lang = "Python"

    for i in range(0, len(lang)):
        print(lang[i])

# String methods.

# String searching:


# String replacing:

