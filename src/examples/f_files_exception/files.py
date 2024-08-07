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
        print(amount, '\n')

        line = file.readline()

    print(total, '\n')

    file.close()

def read_sales_data_w_f_loop(file_name):
    file = open(file_name, 'r')

    total = 0

    for line in file:
       amt = int(line)
       total += amt
       print(amt, '\n')

    print(total, '\n')
    
    file.close()

def write_employee_records(file_name):
    file = open(file_name, 'w')

    choice = '1'

    while choice == '1':
        id = input('Enter id: ')
        name = input('Enter name: ')
        dept = input('Enter dept: ')

        file.write(id + '\t')
        file.write(name + '\t')
        file.write(dept + '\n')

        choice = int(input('Enter 1 to continue'))

    file.close()

def read_employee_records(file_name):
    file = open(file_name, 'r')

    for line in file:
        record = line.split('\t') # Creates a list in this format

        id  = record[0]
        name = record[1]
        dept = record[2].rstrip('\n')

        print(id, name, dept)

    file.close()

def write_2d_list_to_file(file_name):
    file = open(file_name, 'w')

    my_program_lang_list = [['C#', '2001', 'lang'], ['Python', '1996', 'lang'], ['Java', '1991', 'lang']]

    for lang in my_program_lang_list:
        file.write(lang[0] + '\t')
        file.write(lang[1] + '\t')
        file.write(lang[2] + '\n')

    file.close()

def read_prog_langs_records(file_name):
    file = open(file_name, 'r')

    list_langs = []

    for line in file:
        record = line.split('\t')
        lang = record[0]
        year = record[1]
        cat = record[2].rstrip('\n')

        employee = [lang, year, cat]

        list_langs.append(employee)

        for employee in list_langs:
            print(employee[0], employee[1], employee[2])

    file.close()

def write_dict_into_writing(file_name):
    file = open(file_name, 'w')

    dict_to_write = {"Fast": "Car", "Slow": "Bunny", "My": "Password", "Not": True}

    for key, value in dict_to_write.items():
        file.write(key)
        file.write(value)
    
    file.close()


    
        