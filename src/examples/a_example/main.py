import devprocess


#"#" is used to denote a line that the 
#Variable result stores the numbers used by devprocess module's add_numbers function
value1 = input("Enter a number: ")
value2 = input("Enter a second number: ")

result_ad = devprocess.add_numbers(int(value1), int(value2))
result_sb = devprocess.subtract_numbers(int(value1), int(value2))

print(result_ad, result_sb)

