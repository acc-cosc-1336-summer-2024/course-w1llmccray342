#main program
import void_functions, value_return_functions

FEDERAL_TAX_RATE = .12

void_functions.local_variables(5, 2)

globalVar = "Hi"

def main():
    num1 = 2
    num2 = 3

    void_functions.local_variables(3, 2)
    print(num1, num2)

    print(globalVar)
    print(FEDERAL_TAX_RATE)

main()