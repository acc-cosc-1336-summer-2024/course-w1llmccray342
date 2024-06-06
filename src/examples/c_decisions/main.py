import decisions

value1 = input("Enter a number here:")
# Check if a value is a number
# If number continue.

result = decisions.is_number_in_range(int(value1), 1, 10)

print(result)