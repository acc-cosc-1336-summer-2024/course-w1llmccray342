#Create a file to read and write

# A simple function to open the file
def open_file(file_name):
    file = open(file_name, 'r')

    file.close()

def write_to_file(file_name):
    file = open(file_name, 'w')

    file.write('John Locke\n')
    file.write('David Hume\n')
    file.write('Edmund Burke\n')

    file.close()

def read_from_file(file_name):
    file = open(file_name, 'r')

    files_lines = file.read()

    print(files_lines)

    file.close()

def read_from_file_one_line_at_a_time(file_name):
    file = open(file_name, 'r')

    line1 = file.readline().rstrip('\n')
    line2 = file.readline().rstrip('\n')
    line3 = file.readline().rstrip('\n')

    print(line1, line2, line3)


def read_from_file_for_loop(file_name):
    pass

