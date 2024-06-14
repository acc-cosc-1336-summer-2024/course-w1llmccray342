#main program
import void_functions, value_return_functions

FEDERAL_TAX_RATE = .12

void_functions.local_variables(5, 2)

globalVar = "Hi"

def main():

    for i in range(0, 20):
        roll_dice = value_return_functions.get_random_int(1, 20)

        if (roll_dice == 20):
            print(roll_dice, "Critical hit!")
        elif(roll_dice == 1):
            print(roll_dice, "Critical failure!")
        else:
            print("You rolled a ", roll_dice)






    num1 = 2
    num2 = 3

    void_functions.local_variables(3, 2)
    print(num1, num2)

    print(globalVar)
    print(FEDERAL_TAX_RATE)

main()