import random
#Create a class die.

class Die:
    
    def roll():
        my_roll = random.randint(1, 6)
        return my_roll
    
    def get_rolled_value(roll):
        return roll
    
    def __str__(roll):
        return f"The rolled value is {roll}"
    
    def __roll_value():
        pass
    
