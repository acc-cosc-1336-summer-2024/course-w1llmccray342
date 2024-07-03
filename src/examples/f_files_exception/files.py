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

    file.close()


def append_to_file(file_name):
    file = open(file_name, 'a')

    file.write('Karl Marx\n')

    file.close()

def write_sales_data(file_name):
    file = open(file_name, 'w')

    num1 = input("Enter sales data: ")
    num2 = input("Enter sales data: ")
    num3 = input("Enter sales data: ")

    file.write(num1 + '\n')
    file.write(num2 + '\n')
    file.write(num3 + '\n')

    file.close()

def read_sales_data(file_name):
    file = open(file_name, 'r')

    num1 = file.readline().rstrip('\n')
    num2 = file.readline().rstrip('\n')
    num3 = file.readline().rstrip('\n')

    total = num1 + num2 + num3

    print(f"The total numbers are {num1}, {num2}, and {num3}")
    print(f"The total is {total}")

    file.close()

def read_sales_data_w_while_loop(file_name):
    file = open(file_name, 'r')

    line = file.readline()

    total = 0

    while line != '':
        amount = int(line)
        total += amount
        print(amount)

        line = file.readline()

    print(total)

    file.close()