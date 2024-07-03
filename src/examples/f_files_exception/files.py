#Create a file to read and write

# A simple function to open the file
def open_file(file_name):
    file = open(file_name, 'r')

    file.close()

def write_to_file(file_name):
    file = open(file_name, 'w')

    file.write('John Lock\n')
    file.write('David Hume\n')
    file.write('Edmund Burke\n')

    file.close()
