import random
#Create a class die.

class Die:
    
    def roll(self):
        self.__my_roll = random.randint(1, 6)
        return self.__my_roll
    
    def get_rolled_value(self, roll):
        return roll
    
    def __str__(self):
        return f"The rolled value is {self.roll()}"
    
    
